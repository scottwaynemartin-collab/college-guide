# Unit 5 exam items E01-E25
E = []
def q(**k): E.append(k)

q(id="U5-E01", n=1, topic="5.1", lo="PSO-5.A", skill="1.A", difficulty="easy",
  stem="Which of the following best describes the difference between intensive and extensive agriculture?",
  options={
    "A": "Intensive agriculture is always subsistence farming, whereas extensive agriculture is always commercial farming.",
    "B": "Intensive agriculture is found only in developed countries, whereas extensive agriculture is found only in developing countries.",
    "C": "Intensive agriculture grows only grains, whereas extensive agriculture raises only animals.",
    "D": "Intensive agriculture uses large inputs of labor or capital per unit of land, whereas extensive agriculture uses few inputs spread over large areas.",
    "E": "Intensive agriculture relies on rainfall, whereas extensive agriculture relies on irrigation."},
  answer="D",
  rationales={
    "A": "Incorrect. Both kinds can be subsistence or commercial. Wet-rice farming is intensive subsistence; a large market garden is intensive commercial; nomadic herding is extensive subsistence; ranching is extensive commercial.",
    "B": "Incorrect. Both are found in developed and developing countries, for example ranching in the United States and Argentina and intensive rice farming in Japan and Bangladesh.",
    "C": "Incorrect. The distinction is about inputs per unit of land, not crop versus livestock. Dairying is intensive livestock farming; shifting cultivation is extensive crop farming.",
    "D": "Correct. Intensive agriculture concentrates labor, capital, fertilizer, or machinery on relatively small areas to get high output per unit of land. Extensive agriculture uses relatively few inputs per unit of land over large areas, as in ranching, nomadic herding, and shifting cultivation.",
    "E": "Incorrect. Water source does not define the two categories; many intensive and extensive systems are rain-fed, and some of each are irrigated."},
  explanation="Intensive = lots of work and money on a small piece of land (vegetable farms, rice paddies, dairies). Extensive = little work and money spread over a huge area (ranching, nomadic herding, shifting cultivation). It is about inputs per acre, not about rich or poor countries or crops versus animals.")

q(id="U5-E02", n=2, topic="5.2", lo="PSO-5.B", skill="1.A", difficulty="easy",
  stem="A rural settlement pattern in which farm families live together in a village and walk out to fields that surround it is called a",
  options={
    "A": "clustered settlement",
    "B": "dispersed settlement",
    "C": "linear settlement",
    "D": "long-lot settlement",
    "E": "township-and-range settlement"},
  answer="A",
  rationales={
    "A": "Correct. Clustered (nucleated) settlements group homes together in a village, with farmland around it. They are common in much of Europe, Asia, and Africa, often for defense, shared water, or community services.",
    "B": "Incorrect. In dispersed settlements, each family lives on its own farm, separated from neighbors, as in much of the U.S. Midwest.",
    "C": "Incorrect. Linear settlements string homes along a river, road, or canal.",
    "D": "Incorrect. Long lot is a survey method that usually produces a linear pattern along a river, not a central village.",
    "E": "Incorrect. Township and range is a survey method; it usually produces a dispersed pattern of isolated farmsteads."},
  explanation="Clustered = everyone's house is together in a village, and the fields are around the outside. Dispersed = every farmhouse sits alone on its own land. Linear = houses in a line along a river or road.")

# ---- Set A: von Thunen diagram, E03-E05 ----
q(id="U5-E03", n=3, set="vonthunen", topic="5.8", lo="PSO-5.D", skill="4.A", difficulty="easy",
  stimulus=dict(type="rings",
    title="LAND USE AROUND A MARKET CITY ON AN ISOLATED, UNIFORM PLAIN",
    center="Market city",
    rings=[dict(label="W"), dict(label="X"), dict(label="Y"), dict(label="Z")],
    outer="Wilderness",
    description="Four rings, labeled W, X, Y, and Z, surround a single market city. Ring W touches the city; ring Z is farthest away. The plain is flat with equal soil everywhere, there are no roads or rivers, and farmers carry their own goods to the city.",
    source="Based on the model in von Thünen, The Isolated State (1826)"),
  stem="According to von Thünen's model, which ring in the diagram would most likely be used for growing grain and other field crops?",
  options={"A": "Ring W", "B": "Ring X", "C": "Ring Y", "D": "Ring Z", "E": "The market city"},
  answer="C",
  rationales={
    "A": "Incorrect. Ring W, nearest the city, is for perishable, high-value products such as vegetables and milk.",
    "B": "Incorrect. In von Thünen's original model, the second ring is forest for firewood and lumber, which were heavy and costly to haul.",
    "C": "Correct. Grain and field crops occupy the third ring. Grain keeps well and is worth enough to be hauled a moderate distance, but it needs more land than ring W uses.",
    "D": "Incorrect. Ring Z, the outermost farming ring, is for livestock ranching, which needs the most land and the cheapest land.",
    "E": "Incorrect. The city is the market, where farm products are sold, not where field crops are grown."},
  explanation="Remember the order from the city out: 1) vegetables and dairy, 2) forest, 3) grain, 4) ranching. Ring Y is the third ring, so it is grain.")

q(id="U5-E04", n=4, set="vonthunen", topic="5.8", lo="PSO-5.D", skill="1.B", difficulty="medium",
  stem="According to von Thünen's model, which of the following best explains why ring Z is used for livestock ranching?",
  options={
    "A": "Ranching produces the most valuable product per hectare, so it can pay the highest land rent.",
    "B": "Ranching needs very large areas of land, land rent is lowest far from the city, and animals can be walked to market.",
    "C": "Cattle must be kept close to the city because meat spoils within hours.",
    "D": "The soil in ring Z is poorer than the soil in the other rings.",
    "E": "Government rules in the model prohibit ranching near the city."},
  answer="B",
  rationales={
    "A": "Incorrect. Ranching earns relatively little per hectare, which is why it is pushed to the outer ring where land rent is lowest.",
    "B": "Correct. Ranching needs a lot of land. Far from the market, land rent is low, and livestock can walk to the city instead of being hauled, which lowers transport costs over long distances.",
    "C": "Incorrect. In the model, live animals walk to market, so distance matters less for them, not more.",
    "D": "Incorrect. The model assumes the same soil everywhere on a uniform plain. Differences come from distance to market, not soil.",
    "E": "Incorrect. The model is based on economics (land rent and transport cost), not government rules."},
  explanation="Ranching takes a LOT of land and does not earn much per acre, so it goes where land is cheapest: far from the city. And cattle can walk themselves to market, so the long trip costs less than hauling heavy crops would.")

q(id="U5-E05", n=5, set="vonthunen", topic="5.8", lo="PSO-5.D", skill="5.B", difficulty="hard",
  stem="Suppose a navigable canal were built from the market city straight out through rings W, X, Y, and Z. Based on von Thünen's reasoning, which change would most likely occur?",
  options={
    "A": "All four rings would disappear because farmers would move into the city.",
    "B": "The rings would shrink toward the city because transport costs would rise along the canal.",
    "C": "Each ring would stretch outward along the canal because shipping goods by water lowers transport costs.",
    "D": "Ranching would move into ring W because cattle could no longer walk to the market.",
    "E": "The order of the rings would reverse, with ranching nearest the city and vegetables farthest out."},
  answer="C",
  rationales={
    "A": "Incorrect. A canal would make farming farther from the city more profitable, not end it.",
    "B": "Incorrect. Cheap water transport lowers transport costs, so the rings would extend, not shrink.",
    "C": "Correct. Von Thünen himself showed that a navigable river distorts the rings. Lower transport costs along the waterway let each land use extend farther from the city in a band along the canal, so the circles stretch into elongated shapes.",
    "D": "Incorrect. Cattle could still walk or be shipped; nothing in the change would push ranching onto the highest-rent land.",
    "E": "Incorrect. The canal lowers costs along one line; it does not change which products are most perishable or most valuable per hectare."},
  explanation="The rings exist because hauling goods costs more the farther you go. A canal makes shipping much cheaper along its route. So farmers along the canal can grow each product farther from the city, and each ring stretches out along the water like a tongue. Von Thünen showed this with a river in his own book.")

q(id="U5-E06", n=6, topic="5.3", lo="SPS-5.A", skill="1.A", difficulty="easy",
  stem="Which of the following correctly pairs an early hearth of domestication with crops first domesticated there?",
  options={
    "A": "Mesoamerica (Central America) — rice and soybeans",
    "B": "Southeast Asia — maize and potatoes",
    "C": "Fertile Crescent — cassava and sweet potatoes",
    "D": "Northern Europe — coffee and cacao",
    "E": "Mesoamerica (Central America) — maize, beans, and squash"},
  answer="E",
  rationales={
    "A": "Incorrect. Rice and soybeans were domesticated in East and Southeast Asia, not Mesoamerica.",
    "B": "Incorrect. Maize comes from Mesoamerica and potatoes from the Andes of South America.",
    "C": "Incorrect. The Fertile Crescent is known for wheat, barley, lentils, sheep, and goats. Cassava and sweet potatoes come from the Americas.",
    "D": "Incorrect. Northern Europe was not an early hearth. Coffee was first cultivated in the Ethiopia-Yemen region, and cacao in the Americas.",
    "E": "Correct. Mesoamerica (Central America and southern Mexico), one of the hearths named in the CED, domesticated maize, beans, and squash, often grown together as the \"three sisters.\""},
  explanation="Mesoamerica gave the world maize (corn), beans, and squash, often grown together as the \"three sisters.\" The Fertile Crescent gave wheat, barley, sheep, and goats. Southeast and East Asia gave rice.")

q(id="U5-E07", n=7, topic="5.3", lo="SPS-5.B", skill="2.B", difficulty="medium",
  stem="After the potato arrived in Europe from the Americas, it contributed to population growth in places such as Ireland and northern Europe in the 1700s and 1800s mainly because it",
  options={
    "A": "could be grown only on large commercial plantations",
    "B": "produced many calories per acre and grew well in cool, wet climates",
    "C": "required no labor to plant or harvest",
    "D": "was first domesticated in Ireland, so farmers already knew how to grow it",
    "E": "replaced all other foods in the European diet within a few years"},
  answer="B",
  rationales={
    "A": "Incorrect. Potatoes were grown widely on small family plots, which is one reason they fed so many poor households.",
    "B": "Correct. As part of the Columbian Exchange, the Andean potato reached Europe, where it produced more food energy per acre than grains and thrived in cool, damp climates. More food from small plots supported population growth.",
    "C": "Incorrect. Potatoes still require planting, weeding, and digging.",
    "D": "Incorrect. Potatoes were domesticated in the Andes of South America.",
    "E": "Incorrect. Potatoes became very important, especially in Ireland, but they did not replace all other foods across Europe."},
  explanation="The potato came from the Andes Mountains in South America through the Columbian Exchange. It grows lots of food on a small patch of ground and likes cool, wet weather, which is exactly what Ireland and northern Europe have. More food meant more families could survive and grow.")

q(id="U5-E08", n=8, topic="5.4", lo="SPS-5.C", skill="1.D", difficulty="medium",
  stem="The enclosure movement in Britain during the Second Agricultural Revolution most directly resulted in",
  options={
    "A": "the division of large estates into small plots for landless peasants",
    "B": "the return of farmland to forest to protect wildlife",
    "C": "a decline in food production as farms became less efficient",
    "D": "an increase in the number of people working as farm laborers",
    "E": "the consolidation of open fields and common land into larger private farms, pushing many rural people toward cities"},
  answer="E",
  rationales={
    "A": "Incorrect. Enclosure did the opposite, combining small strips and common land into larger private holdings.",
    "B": "Incorrect. Enclosed land was used for more efficient crops and pasture, not returned to forest.",
    "C": "Incorrect. Consolidated farms adopted new methods such as crop rotation and selective breeding, and output rose.",
    "D": "Incorrect. Larger, more efficient farms needed fewer laborers per unit of output, and many rural families lost access to common land.",
    "E": "Correct. Enclosure fenced off open fields and common land into larger private farms. More efficient farms needed fewer workers, and families who lost access to the commons moved to growing industrial cities, supplying factory labor."},
  explanation="Enclosure means landowners fenced in the open fields and shared \"common\" land and made them into bigger private farms. Bigger farms could use new methods and needed fewer workers. Many poor rural families lost the land they had used and moved to cities, where they worked in factories.")

# ---- Set B: Green Revolution table, E09-E10 ----
q(id="U5-E09", n=9, set="greenrev", topic="5.5", lo="SPS-5.D", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="WHEAT FARMING IN COUNTRY M, 1960–1990 (HYPOTHETICAL DATA)",
    columns=["Year", "Wheat yield (tonnes per hectare)", "Cropland that is irrigated (%)", "Fertilizer used (kg per hectare)", "Population (millions)"],
    rows=[
      ["1960", "0.8", "18", "3", "450"],
      ["1975", "1.4", "25", "20", "610"],
      ["1990", "2.3", "32", "70", "850"]],
    source="Hypothetical data"),
  stem="Which conclusion is best supported by the data in the table?",
  options={
    "A": "Wheat yields rose as irrigation and fertilizer use increased, consistent with the Green Revolution.",
    "B": "Wheat yields fell as the population grew, as Malthus predicted.",
    "C": "Irrigation decreased because the new seeds needed less water.",
    "D": "Fertilizer use stayed about the same from 1960 to 1990.",
    "E": "Population growth stopped once wheat yields began to rise."},
  answer="A",
  rationales={
    "A": "Correct. Yield nearly tripled (0.8 to 2.3 tonnes per hectare) while irrigated cropland rose from 18 to 32 percent and fertilizer use rose from 3 to 70 kg per hectare. That combination of inputs and high-yield seeds is the Green Revolution package.",
    "B": "Incorrect. Yields rose in each period; food production outpaced the Malthusian prediction.",
    "C": "Incorrect. The irrigated share rose in each period.",
    "D": "Incorrect. Fertilizer use rose more than twentyfold.",
    "E": "Incorrect. Population kept growing, from 450 to 850 million."},
  explanation="Every column goes up. Yields almost tripled, more land was irrigated, and fertilizer use jumped from 3 to 70 kilograms per hectare. High-yield seeds plus water plus fertilizer is the Green Revolution recipe.")

q(id="U5-E10", n=10, set="greenrev", topic="5.5", lo="SPS-5.D", skill="2.D", difficulty="hard",
  stem="Which of the following is a likely negative consequence of the changes shown in the table?",
  options={
    "A": "Lower wheat yields caused by the loss of irrigation",
    "B": "A shortage of fertilizer that forced farmers back to subsistence farming",
    "C": "Falling groundwater levels and water pollution from fertilizer runoff",
    "D": "Rapid growth of forests on abandoned wheat fields",
    "E": "An end to wheat exports because farmers grew only vegetables"},
  answer="C",
  rationales={
    "A": "Incorrect. The table shows irrigation expanding and yields rising.",
    "B": "Incorrect. Fertilizer use rose sharply; nothing suggests a shortage.",
    "C": "Correct. Expanding irrigation often means heavy pumping of groundwater, lowering water tables, and much heavier fertilizer use can wash into rivers and wells. These environmental costs accompanied the Green Revolution in places such as Punjab.",
    "D": "Incorrect. Fields were farmed more intensively, not abandoned.",
    "E": "Incorrect. The table shows rising wheat yields, not a switch to vegetables."},
  explanation="More irrigation means pumping more water out of the ground, so water tables fall. Way more fertilizer means some of it washes into rivers and wells and pollutes them. Bigger harvests came with environmental costs.")

q(id="U5-E11", n=11, topic="5.4", lo="SPS-5.C", skill="2.D", difficulty="medium",
  stem="The Second Agricultural Revolution was closely linked to the Industrial Revolution because",
  options={
    "A": "factories replaced farms as the main source of food",
    "B": "higher farm productivity freed workers for factory jobs, and industrial inventions such as steel plows and mechanical reapers raised farm output further",
    "C": "governments banned machinery on farms to protect factory jobs",
    "D": "industrial cities grew their own food on rooftops, so farms were no longer needed",
    "E": "the Industrial Revolution began in rural areas and later spread to cities"},
  answer="B",
  rationales={
    "A": "Incorrect. Food still came from farms; factories processed some of it later.",
    "B": "Correct. The two revolutions reinforced each other. Productive farms needed fewer workers and fed growing cities, supplying labor and food for industry, while industrial products such as steel plows, reapers, and later tractors and fertilizer made farms more productive still.",
    "C": "Incorrect. Farms adopted more machinery, not less.",
    "D": "Incorrect. Cities depended on farms in the countryside for food.",
    "E": "Incorrect. Industrialization was centered in growing cities and mill towns, drawing workers away from rural areas."},
  explanation="The two revolutions helped each other. Better farming meant fewer farmers could feed everyone, so extra people could work in factories. And factories built new farm tools like steel plows and reapers, which made farms even more productive.")

q(id="U5-E12", n=12, topic="5.6", lo="PSO-5.C", skill="1.D", difficulty="medium",
  stem="Large estates in tropical regions that grow a single cash crop, such as bananas, sugarcane, or palm oil, mainly for export to distant markets are an example of",
  options={
    "A": "shifting cultivation",
    "B": "pastoral nomadism",
    "C": "subsistence agriculture",
    "D": "plantation agriculture",
    "E": "market gardening"},
  answer="D",
  rationales={
    "A": "Incorrect. Shifting cultivation clears small forest plots for a few years of food crops, then moves on; it is mostly subsistence.",
    "B": "Incorrect. Pastoral nomadism is moving herds to find pasture.",
    "C": "Incorrect. Subsistence agriculture grows food mainly for the farm family's own use, not for export.",
    "D": "Correct. Plantations are large commercial estates, often in tropical regions, that specialize in one export crop (monoculture). Many began with colonial investment, and the CED classifies plantation agriculture as intensive.",
    "E": "Incorrect. Market gardening grows a variety of fruits and vegetables for nearby city markets."},
  explanation="A plantation is a big farm in a warm, tropical place that grows one crop to sell to faraway countries: bananas, sugarcane, coffee, or palm oil. It is commercial (for sale), monoculture (one crop), and intensive (lots of workers and money).")

q(id="U5-E13", n=13, topic="5.6", lo="PSO-5.C", skill="2.E", difficulty="hard",
  stem="Dairy farms historically surrounded large cities such as New York and Chicago in zones known as \"milksheds.\" Bid-rent theory best explains this pattern because",
  options={
    "A": "dairy cattle need more land per animal than beef cattle on open ranges",
    "B": "milk keeps for months, so it can be shipped very long distances cheaply",
    "C": "land near cities was cheaper than land in remote rural areas",
    "D": "city governments required all milk to be produced inside city limits",
    "E": "fresh milk is perishable and costly to transport, so dairying earned enough near the market to outbid less intensive land uses"},
  answer="E",
  rationales={
    "A": "Incorrect. Dairying is usually more intensive than ranching, using less land per unit of output.",
    "B": "Incorrect. Fresh milk spoils quickly, which is why it was produced near consumers before modern refrigeration.",
    "C": "Incorrect. Bid-rent theory predicts land is more expensive closer to the market.",
    "D": "Incorrect. The pattern reflects land rent and transport costs, not a law requiring production inside the city.",
    "E": "Correct. Because fresh milk was perishable and expensive to ship, producers close to the city could earn more per acre, so dairying outbid less intensive uses for the high-rent land near the market."},
  explanation="Fresh milk goes bad fast, and moving it far used to be hard and expensive. So dairy farmers near the city could make more money per acre than, say, grain farmers. That let them pay the high price of land close to the city. That is bid-rent: whoever earns the most from being close wins the close land.")

# ---- Set C: commodity dependence table, E14-E15 ----
q(id="U5-E14", n=14, set="exports", topic="5.9", lo="PSO-5.E", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="EXPORT EARNINGS OF FIVE COUNTRIES (HYPOTHETICAL DATA)",
    columns=["Country", "Largest export", "Share of export earnings from largest export (%)", "Second-largest export", "Share from second-largest export (%)"],
    rows=[
      ["Country P", "Coffee", "62", "Bananas", "9"],
      ["Country Q", "Automobiles", "14", "Coffee", "3"],
      ["Country R", "Copper", "48", "Coffee", "11"],
      ["Country S", "Coffee", "21", "Textiles", "19"],
      ["Country T", "Software services", "25", "Coffee", "6"]],
    source="Hypothetical data"),
  stem="Based on the table, which country's export earnings would be most harmed by a 40 percent drop in the world price of coffee?",
  options={"A": "Country Q", "B": "Country R", "C": "Country T", "D": "Country S", "E": "Country P"},
  answer="E",
  rationales={
    "A": "Incorrect. Coffee is only 3 percent of Country Q's export earnings.",
    "B": "Incorrect. Coffee is 11 percent of Country R's earnings; its larger exposure is to copper prices.",
    "C": "Incorrect. Coffee is only 6 percent of Country T's export earnings.",
    "D": "Incorrect. Coffee is Country S's largest export, but at 21 percent its earnings are more diversified than Country P's.",
    "E": "Correct. Coffee provides 62 percent of Country P's export earnings, so a large fall in coffee prices would cut its total export income far more than any other country's."},
  explanation="Find the country that gets the biggest share of its export money from coffee. Country P gets 62% from coffee, way more than anyone else, so a coffee price crash would hurt it the most.")

q(id="U5-E15", n=15, set="exports", topic="5.9", lo="PSO-5.E", skill="5.D", difficulty="hard",
  stem="The table best illustrates which aspect of the global system of agriculture?",
  options={
    "A": "Most countries grow all of their own food and export nothing.",
    "B": "Some countries depend heavily on a few export commodities, tying their national economies to world prices set by distant buyers.",
    "C": "Commodity prices are set by each producing country's government and do not change.",
    "D": "Coffee is grown mainly in countries with cold winters and is sold mostly to tropical countries.",
    "E": "Countries with diversified exports are more affected by changes in a single crop's price."},
  answer="B",
  rationales={
    "A": "Incorrect. Every country in the table earns money from exports.",
    "B": "Correct. Countries P and R earn about half or more of their export income from a single primary commodity, so global market prices, shaped by consumers and traders in other countries, drive their national income. The CED notes that some countries are highly dependent on one or more export commodities.",
    "C": "Incorrect. Commodity prices are set on world markets and can change sharply.",
    "D": "Incorrect. Coffee is a tropical crop, and the largest consumer markets include the United States and Europe.",
    "E": "Incorrect. Diversified economies, such as Country Q's, are less affected by a single crop's price."},
  explanation="Some countries make most of their export money from one product, like coffee or copper. The price is set by buyers and traders all over the world, so a price drop somewhere else can hurt that whole country's economy. That is what it means to be part of a global system.")

# ---- Set D: time-use bar chart, E16-E18 ----
q(id="U5-E16", n=16, set="timeuse", topic="5.12", lo="IMP-5.C", skill="3.D", difficulty="medium",
  stimulus=dict(type="bar",
    title="AVERAGE HOURS PER WEEK SPENT ON FOOD-RELATED WORK, BY SEX, IN A RURAL REGION (HYPOTHETICAL DATA)",
    categories=["Growing food crops for the household", "Growing cash crops for sale", "Processing and preparing food", "Selling at local markets"],
    series=[dict(name="Women (hours per week)", values=[18, 6, 14, 6]),
            dict(name="Men (hours per week)", values=[9, 16, 2, 3])],
    yLabel="Hours per week", yMax=20,
    text="In this region, most land titles and most bank loans for farming are held by men.",
    source="Hypothetical data"),
  stem="Which conclusion is best supported by the chart?",
  options={
    "A": "Men spend more time than women on every type of food-related work.",
    "B": "Women spend more time than men growing cash crops for sale.",
    "C": "Women and men spend equal time processing and preparing food.",
    "D": "Women spend more time than men on household food crops and food processing, while men spend more time on cash crops.",
    "E": "Neither women nor men spend any time selling food at local markets."},
  answer="D",
  rationales={
    "A": "Incorrect. Women spend more time than men in three of the four categories.",
    "B": "Incorrect. Men spend 16 hours on cash crops; women spend 6.",
    "C": "Incorrect. Women spend 14 hours processing and preparing food; men spend 2.",
    "D": "Correct. Women average 18 hours on household food crops and 14 on processing, compared with 9 and 2 for men, while men average 16 hours on cash crops compared with 6 for women.",
    "E": "Incorrect. Women spend 6 hours and men 3 hours per week selling at local markets."},
  explanation="Compare the pairs of bars. Women's bars are taller for household food crops (18 vs. 9), processing food (14 vs. 2), and selling (6 vs. 3). Men's bar is taller only for cash crops (16 vs. 6).")

q(id="U5-E17", n=17, set="timeuse", topic="5.10", lo="IMP-5.A", skill="2.B", difficulty="hard",
  stem="Which of the following best explains the pattern shown in the chart?",
  options={
    "A": "Women in the region are not allowed to work outdoors.",
    "B": "Cash crops require no labor, so most of the work goes into household food crops.",
    "C": "A gendered division of labor in which men control most land and cash income while women are mainly responsible for household food",
    "D": "Food processing is fully mechanized in the region, so women's processing hours are spent operating machines.",
    "E": "Men in the region have left farming entirely for jobs in distant cities."},
  answer="C",
  rationales={
    "A": "Incorrect. Women spend more hours than men on field work for household food crops.",
    "B": "Incorrect. Men spend 16 hours per week on cash crops, so they do require labor.",
    "C": "Correct. The chart and note show a common gendered division of labor: men hold most land titles and credit and focus on income-earning cash crops, while women carry most of the work of feeding the household. The CED lists the role of women in agricultural production as a societal effect of agricultural practices.",
    "D": "Incorrect. Nothing in the chart indicates mechanization, and 14 hours per week of processing suggests largely manual work.",
    "E": "Incorrect. Men still spend many hours on farm work, especially cash crops."},
  explanation="The note says men hold most of the land and loans. That helps explain why men do more of the farming for money (cash crops), while women do more of the farming and cooking that feeds the family. This kind of split is called a gendered division of labor.")

q(id="U5-E18", n=18, set="timeuse", topic="5.12", lo="IMP-5.C", skill="3.F", difficulty="hard",
  stem="Which of the following is a limitation of the chart for understanding women's role in agriculture in the region?",
  options={
    "A": "It shows only hours worked, not who decides what to grow or who keeps the income from sales.",
    "B": "It compares women and men in the same region.",
    "C": "It includes more than one type of food-related work.",
    "D": "It measures time in hours per week.",
    "E": "It shows the work of both women and men."},
  answer="A",
  rationales={
    "A": "Correct. Hours worked do not show control over land, decisions, or income. Two groups can work similar hours with very different power over resources, so the chart alone cannot show who benefits from the work.",
    "B": "Incorrect. Comparing women and men in the same region is a strength of the chart, not a limitation.",
    "C": "Incorrect. Including several types of work gives a fuller picture, which is a strength.",
    "D": "Incorrect. Hours per week is a clear, appropriate unit for time use.",
    "E": "Incorrect. Showing both groups allows comparison, which is a strength."},
  explanation="The chart tells us how many HOURS each group works. It does not tell us who makes the decisions or who gets to keep the money. That missing piece matters a lot for understanding women's role in farming.")

q(id="U5-E19", n=19, topic="5.7", lo="PSO-5.C", skill="1.D", difficulty="medium",
  stem="Since the mid-1900s, the number of farms in the United States has fallen sharply while the average size of a farm has grown. Which of the following best explains this trend?",
  options={
    "A": "Farmers moved from commercial farming back to subsistence farming.",
    "B": "Government programs divided large farms into small plots for new farmers.",
    "C": "Shifting cultivation became the main farming method in the Midwest.",
    "D": "Most farmland was converted to forest after 1950.",
    "E": "Mechanization and economies of scale favored large operations, which bought out or absorbed many smaller farms."},
  answer="E",
  rationales={
    "A": "Incorrect. U.S. agriculture became more commercial, not less.",
    "B": "Incorrect. Farms consolidated into fewer, larger units.",
    "C": "Incorrect. Shifting cultivation is not practiced in the U.S. Midwest.",
    "D": "Incorrect. Most farmland stayed in production; the change was in how many operations controlled it.",
    "E": "Correct. Expensive machinery, seed, and chemical inputs are cheaper per acre for large farms (economies of scale). Large commercial operations and agribusinesses expanded while many smaller family farms sold out. The CED says large-scale commercial operations are replacing small family farms."},
  explanation="Big farms can spread the cost of a $500,000 combine over thousands of acres, so they make more per acre. Small farms can't compete as well and often sell to bigger ones. So there are fewer farms, but each one is bigger.")

q(id="U5-E20", n=20, topic="5.7", lo="PSO-5.C", skill="1.D", difficulty="medium",
  stem="Coffee beans grown on small farms in Colombia are sold to an exporter, roasted in a plant in New Jersey, packaged, shipped to a distribution center, and sold in a café in Chicago. This sequence best illustrates",
  options={
    "A": "a commodity chain linking places of agricultural production and consumption",
    "B": "the von Thünen model of land use around a single market city",
    "C": "subsistence agriculture practiced by the coffee farmers",
    "D": "the Second Agricultural Revolution in Colombia",
    "E": "a food desert in the city of Chicago"},
  answer="A",
  rationales={
    "A": "Correct. A commodity chain is the linked series of steps (growing, buying, processing, packaging, distributing, and selling) that connects a product's producers to its consumers, often across several countries. The CED says complex commodity chains link production and consumption of agricultural products.",
    "B": "Incorrect. Von Thünen's model explains land use around one local market; this example crosses countries and involves processing and distribution steps.",
    "C": "Incorrect. The coffee is grown for sale, not for the farmers' own consumption.",
    "D": "Incorrect. The example describes a modern global supply chain, not the 1700s–1800s agricultural changes in Europe.",
    "E": "Incorrect. A café selling coffee says nothing about residents' access to affordable, healthy food."},
  explanation="Follow the coffee from farm to cup: grown in Colombia, sold, roasted in New Jersey, packed, shipped, and sold in Chicago. That chain of steps connecting the farmer to the customer is a commodity chain.")

q(id="U5-E21", n=21, topic="5.10", lo="IMP-5.A", skill="2.E", difficulty="medium",
  stem="In parts of the Sahel region of Africa, which human activity has most contributed to desertification during periods of drought?",
  options={
    "A": "Overgrazing and removing trees and shrubs on dry grasslands, which leaves soil exposed to wind and erosion",
    "B": "Building terraces on steep hillsides to grow rice",
    "C": "Converting desert land into irrigated rice paddies",
    "D": "Planting belts of trees to block the wind",
    "E": "Rotating crops to restore soil nutrients"},
  answer="A",
  rationales={
    "A": "Correct. When too many animals graze, or trees and shrubs are cut for fuel and farmland, the protective plant cover is lost. During droughts, bare soil dries out and blows away, and the land becomes desert-like. Climate variability plays a large role, but these land uses make the damage worse.",
    "B": "Incorrect. Terracing is a conservation practice that reduces erosion, and the Sahel is not a hillside rice region.",
    "C": "Incorrect. Irrigated paddies are rare in the Sahel; irrigation can cause salinization, but it is not the main driver of Sahel desertification.",
    "D": "Incorrect. Tree belts, such as the Great Green Wall effort, are meant to fight desertification.",
    "E": "Incorrect. Crop rotation protects soil fertility; it does not cause desertification."},
  explanation="The Sahel is a dry strip of land just south of the Sahara. When animals eat too much of the grass, and people cut down trees and bushes, the soil has nothing to hold it. During a drought the soil dries and blows away, and the land turns more like a desert. That is desertification.")

q(id="U5-E22", n=22, topic="5.1", lo="PSO-5.A", skill="2.D", difficulty="medium",
  stem="Pastoral nomadism is most common in dry grasslands and deserts, such as parts of Central Asia, the Sahel, and the Arabian Peninsula, because",
  options={
    "A": "these regions have the most fertile soils in the world for growing grain",
    "B": "rainfall is too low and unreliable for most crops, so herders move animals seasonally to find water and pasture",
    "C": "governments in these regions require all farmers to raise animals",
    "D": "these regions are close to large cities that buy fresh milk every day",
    "E": "heavy year-round rainfall makes it impossible to keep animals in one place"},
  answer="B",
  rationales={
    "A": "Incorrect. These regions have thin soils and little rain, which is why crop farming is difficult there.",
    "B": "Correct. Where rain is scarce and unpredictable, growing crops is risky. Herding livestock (camels, goats, sheep, cattle) and moving them with the seasons lets people use sparse grass and water spread across large areas, an extensive practice shaped by the physical environment.",
    "C": "Incorrect. The pattern reflects climate and environment, not government requirements.",
    "D": "Incorrect. Nomadic herders typically live far from large city markets.",
    "E": "Incorrect. These regions are dry; heavy year-round rain is the opposite of their climate."},
  explanation="In very dry places, crops often fail because there is not enough rain. But animals can eat the scattered grass. So herders move their animals from place to place with the seasons to find grass and water. The dry climate is the reason.")

q(id="U5-E23", n=23, topic="5.11", lo="IMP-5.B", skill="1.C", difficulty="medium",
  stem="Supporters of genetically modified (GM) crops argue that they can raise yields and resist pests. Which of the following is a concern raised by critics of GM crops?",
  options={
    "A": "GM crops always produce smaller harvests than traditional seeds.",
    "B": "GM crops can be grown only by subsistence farmers.",
    "C": "GM crops cannot be sold in any country.",
    "D": "Reduced crop biodiversity and farmers' dependence on seed companies that hold patents",
    "E": "GM crops require farmers to stop using all fertilizer and pesticides."},
  answer="D",
  rationales={
    "A": "Incorrect. Many GM varieties raise yields or reduce crop losses; critics' concerns center elsewhere.",
    "B": "Incorrect. GM crops are planted mostly on large commercial farms, for example soybeans and maize in the Americas.",
    "C": "Incorrect. GM crops are widely traded, though some countries restrict them.",
    "D": "Correct. Critics worry that planting a few patented varieties over huge areas reduces biodiversity and that farmers must buy new seed from a few large companies each season. The CED lists debates over reduced biodiversity and fertilizer and pesticide use.",
    "E": "Incorrect. Some GM crops are bred to tolerate herbicides, and critics argue this can increase, not end, chemical use."},
  explanation="Critics say that when farmers everywhere plant the same few GM varieties, there is less variety in crops (less biodiversity). They also worry that farmers have to buy patented seeds from a few big companies every year.")

q(id="U5-E24", n=24, topic="5.11", lo="IMP-5.B", skill="1.A", difficulty="easy",
  stem="Which of the following best describes the fair trade movement in agriculture?",
  options={
    "A": "A system that removes all tariffs between countries",
    "B": "A government program that pays farmers not to grow crops",
    "C": "A certification system that sets minimum prices and labor and environmental standards for producers, often in developing countries",
    "D": "A plan to replace imported food with food grown in each consumer's backyard",
    "E": "A treaty that requires every country to grow its own coffee"},
  answer="C",
  rationales={
    "A": "Incorrect. That describes free trade, not fair trade.",
    "B": "Incorrect. That describes some conservation or price-support programs.",
    "C": "Correct. Fair trade certification guarantees producers, such as coffee, cocoa, and banana growers, a minimum price and sets standards for working conditions and environmental practices. The CED lists fair trade among movements influencing food production and consumption.",
    "D": "Incorrect. That is closer to urban farming or the local-food movement.",
    "E": "Incorrect. Coffee grows only in suitable tropical climates; no such treaty exists."},
  explanation="Fair trade labels (like the one on some coffee and chocolate) promise that the farmers were paid at least a minimum price and that workers were treated fairly. Shoppers pay a little more so more money gets back to the growers.")

q(id="U5-E25", n=25, topic="5.2", lo="PSO-5.B", skill="1.D", difficulty="medium",
  stem="Property boundaries in parts of the original thirteen U.S. colonies were described using natural features such as streams, large trees, and stones, producing irregularly shaped parcels. This survey method is called",
  options={
    "A": "township and range",
    "B": "the long-lot system",
    "C": "metes and bounds",
    "D": "the Public Land Survey System",
    "E": "enclosure"},
  answer="C",
  rationales={
    "A": "Incorrect. Township and range uses a rectangular grid of squares, not natural landmarks.",
    "B": "Incorrect. Long lots are narrow strips running back from a river, used in French settlement areas.",
    "C": "Correct. Metes and bounds describes boundaries by distances and directions between landmarks such as streams, trees, and stones, producing irregular parcels. It was widely used in the colonial East and came from British practice.",
    "D": "Incorrect. The Public Land Survey System is another name for township and range.",
    "E": "Incorrect. Enclosure is the British consolidation of open fields and common land, not a surveying method."},
  explanation="Metes and bounds uses landmarks to mark property lines: \"from the big oak tree, 200 feet to the creek, then along the creek to the stone wall.\" Because nature is not in straight lines, the parcels have odd, irregular shapes. You see it in the eastern U.S.")
