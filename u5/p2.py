# Unit 5 practice items P19-P36 (topics 5.7-5.12)
P = []

# ---------------- 5.7 Spatial Organization of Agriculture (PSO-5.C) ----------------
P.append(dict(id="U5-P19", topic="5.7", lo="PSO-5.C", skill="1.D", difficulty="easy",
  stem="A single company owns chicken hatcheries and feed mills, signs contracts with farmers to raise its chickens, and runs its own processing plants and delivery trucks. This is an example of",
  options={
    "A": "subsistence agriculture",
    "B": "shifting cultivation",
    "C": "vertical integration in agribusiness",
    "D": "the Columbian Exchange",
    "E": "community-supported agriculture"},
  answer="C",
  explanation="Agribusiness means farming run like a big business, with large companies involved at many steps. Vertical integration means one company controls several steps of the chain: here it owns the chicks, the feed, the processing, and the trucks, and farmers raise the birds under contract. The U.S. poultry industry works this way.",
  whyNot={
    "A": "Subsistence farmers grow food for their own families, not for a corporation.",
    "B": "Shifting cultivation is clearing and farming forest plots for a few years, then moving on.",
    "D": "The Columbian Exchange was the swap of crops and animals after 1492.",
    "E": "Community-supported agriculture connects local customers directly to a small farm."},
  vocab=["agribusiness", "vertical integration", "commodity chain"]))

P.append(dict(id="U5-P20", topic="5.7", lo="PSO-5.C", skill="1.D", difficulty="medium",
  stem="Which development best illustrates technology increasing the carrying capacity of farmland?",
  options={
    "A": "Farmers abandon fields after the soil loses its fertility.",
    "B": "Center-pivot irrigation and improved seeds let the same acreage feed more people.",
    "C": "A region converts farmland into new housing subdivisions.",
    "D": "Herders move their animals to new pastures each season.",
    "E": "A farm stops using machinery and returns to plowing with animals."},
  answer="B",
  explanation="Carrying capacity is how many people the land can support. If the same acres produce more food, the land can feed more people. Irrigation brings water to dry fields, and better seeds grow bigger harvests. The CED says technology has increased economies of scale in agriculture and the carrying capacity of the land.",
  whyNot={
    "A": "Abandoning worn-out fields lowers how many people the land supports.",
    "C": "Turning farms into housing removes farmland. It does not raise its output.",
    "D": "Seasonal herding is a traditional practice, not new technology raising output.",
    "E": "Going back to animal plowing usually lowers output per acre and per worker."},
  vocab=["carrying capacity", "economies of scale", "center-pivot irrigation"]))

P.append(dict(id="U5-P21", topic="5.7", lo="PSO-5.C", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="FARMS IN COUNTRY Z, 1950–2020 (HYPOTHETICAL DATA)",
    columns=["Year", "Number of farms (millions)", "Average farm size (acres)", "Total farmland (millions of acres)"],
    rows=[
      ["1950", "5.4", "215", "1,161"],
      ["1980", "2.4", "425", "1,020"],
      ["2020", "2.0", "445", "890"]],
    source="Hypothetical data"),
  stem="The trend in the table best illustrates which of the following?",
  options={
    "A": "Large-scale commercial operations replacing small family farms",
    "B": "A shift from commercial farming to subsistence farming",
    "C": "A rapid increase in the total amount of land being farmed",
    "D": "The breakup of large estates into many small peasant farms",
    "E": "A return to shifting cultivation as farmers move to new land"},
  answer="A",
  explanation="The number of farms fell by more than half (5.4 million to 2.0 million) while the average farm doubled in size (215 to 445 acres). That means small farms were bought up or combined into bigger ones. Big operations can buy machines and supplies in bulk and spread the cost over more acres (economies of scale). The CED says large-scale commercial operations are replacing small family farms.",
  whyNot={
    "B": "Bigger farms with fewer owners point to MORE commercial farming, not subsistence.",
    "C": "Total farmland FELL, from 1,161 to 890 million acres.",
    "D": "Farms got bigger and fewer, the opposite of breaking up estates.",
    "E": "Nothing in the table suggests shifting cultivation, and farm counts would not fall that way."},
  vocab=["agribusiness", "economies of scale", "family farm"]))

# ---------------- 5.8 Von Thunen Model (PSO-5.D) ----------------
P.append(dict(id="U5-P22", topic="5.8", lo="PSO-5.D", skill="1.A", difficulty="easy",
  stem="In von Thünen's model of agricultural land use, which activity is located in the ring closest to the market city?",
  options={
    "A": "Market gardening and dairying",
    "B": "Livestock ranching",
    "C": "Grain and field crops",
    "D": "Forestry for firewood and lumber",
    "E": "Unused wilderness"},
  answer="A",
  explanation="Von Thünen said the most perishable and expensive-to-ship products go closest to the city. Fresh vegetables and milk spoil fast, so they were grown right next to the market (in the 1820s, there were no refrigerated trucks). Then came forest, then grain, then ranching, with wilderness beyond.",
  whyNot={
    "B": "Ranching is in the outermost farming ring, because it needs lots of cheap land and animals can walk to market.",
    "C": "Grain is in the third ring. It keeps well, so it can travel farther.",
    "D": "Forest is in the second ring, close because wood is heavy and costly to haul.",
    "E": "Wilderness lies beyond all the rings."},
  vocab=["von Thünen model", "market gardening", "perishable"]))

P.append(dict(id="U5-P23", topic="5.8", lo="PSO-5.D", skill="5.B", difficulty="medium",
  stimulus=dict(type="rings",
    title="VON THÜNEN'S MODEL OF RURAL LAND USE",
    center="Market city",
    rings=[dict(label="1"), dict(label="2"), dict(label="3"), dict(label="4")],
    outer="Wilderness",
    description="Four rings surround a single market city on a flat, uniform plain. Ring 1 touches the city; ring 4 is farthest away. Farmers haul their own goods to the city, so transportation cost rises with distance.",
    source="Simplified from von Thünen, The Isolated State (1826)"),
  stem="In von Thünen's original model, shown in the diagram, which land use occupied ring 2, and why?",
  options={
    "A": "Ranching, because cattle can walk to the city on their own",
    "B": "Grain, because wheat spoils quickly and must be sold within a day",
    "C": "Market gardening, because vegetables need the most land per farm",
    "D": "Forestry, because wood for fuel and building was heavy and costly to haul",
    "E": "Dairying, because milk could be stored for months without spoiling"},
  answer="D",
  explanation="This surprises people: von Thünen put FOREST in ring 2, right after the vegetable and dairy ring. In the 1820s, cities burned wood for heat and cooking and built with lumber. Wood is heavy and bulky, so hauling it far by horse cart cost too much. Grain (ring 3) keeps well and is lighter for its value. Ranching (ring 4) needs the most land.",
  whyNot={
    "A": "Ranching is the outermost ring (ring 4).",
    "B": "Grain is in ring 3, and it keeps a long time. It does not spoil in a day.",
    "C": "Market gardening is ring 1, and it uses SMALL plots, not the most land.",
    "E": "Dairying is in ring 1 because milk spoils fast."},
  vocab=["von Thünen model", "transportation cost"]))

P.append(dict(id="U5-P24", topic="5.8", lo="PSO-5.D", skill="1.E", difficulty="hard",
  stem="Which observation most challenges the usefulness of von Thünen's model for explaining agricultural land use today?",
  options={
    "A": "Dairy farms are still common on the edges of some large cities.",
    "B": "Land prices near a city are usually higher than land prices far from it.",
    "C": "Refrigerated ships and air freight let fresh grapes from Chile reach stores in North America and Europe.",
    "D": "Cattle ranching is still common in thinly populated areas far from cities.",
    "E": "Farmers still consider transportation cost when they decide what to grow."},
  answer="C",
  explanation="Von Thünen's model depends on transportation cost rising steeply with distance, so perishable foods must be grown close to the market. Refrigeration and fast, cheap shipping break that rule: fresh grapes can travel thousands of miles from Chile and still beat local fruit in winter. The CED notes that specialty farming regions do not always fit the rings.",
  whyNot={
    "A": "Dairying near cities fits the model.",
    "B": "Higher land prices near the market match bid-rent and the model.",
    "D": "Ranching far from cities fits the outer ring of the model.",
    "E": "That supports the model's main idea, transportation cost."},
  vocab=["von Thünen model", "time-space compression", "specialty agriculture"]))

# ---------------- 5.9 The Global System of Agriculture (PSO-5.E) ----------------
P.append(dict(id="U5-P25", topic="5.9", lo="PSO-5.E", skill="1.B", difficulty="easy",
  stem="Countries whose export earnings depend heavily on one agricultural commodity, such as coffee or cocoa, are especially vulnerable to",
  options={
    "A": "falling birth rates",
    "B": "declining tourism in their capital cities",
    "C": "the loss of their official language",
    "D": "sharp drops in the world price of that commodity",
    "E": "an increase in the number of manufacturing jobs"},
  answer="D",
  explanation="If most of a country's money from exports comes from one crop, its whole economy rides on that crop's price. When world cocoa or coffee prices fall, the country earns much less, and farmers, workers, and the government all have less money. The CED says some countries have become highly dependent on one or more export commodities.",
  whyNot={
    "A": "Birth rates are not tied to dependence on one crop export.",
    "B": "Tourism is a separate part of the economy.",
    "C": "Language has nothing to do with commodity dependence.",
    "E": "More manufacturing jobs would REDUCE dependence on one crop, not threaten the country."},
  vocab=["commodity dependence", "export commodity", "global supply chain"]))

P.append(dict(id="U5-P26", topic="5.9", lo="PSO-5.E", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="TRADE PROFILE OF FIVE COUNTRIES (HYPOTHETICAL DATA)",
    columns=["Country", "Top export", "Top export's share of export earnings (%)", "Share of food supply that is imported (%)"],
    rows=[
      ["Country A", "Machinery", "18", "15"],
      ["Country B", "Cocoa", "45", "20"],
      ["Country C", "Natural gas", "60", "85"],
      ["Country D", "Wheat", "25", "5"],
      ["Country E", "Electronics", "30", "40"]],
    source="Hypothetical data"),
  stem="Based on the table, which country's food supply would be most threatened by a sharp rise in world grain prices?",
  options={
    "A": "Country A",
    "B": "Country B",
    "C": "Country C",
    "D": "Country D",
    "E": "Country E"},
  answer="C",
  explanation="Look at the last column: how much of each country's food comes from other countries. Country C imports 85% of its food, so when world grain prices jump, it has to pay much more to feed its people. Country D exports wheat and imports only 5% of its food, so it might even gain from higher grain prices. This shows how food links countries together in a global system.",
  whyNot={
    "A": "Country A imports only 15% of its food.",
    "B": "Country B depends on cocoa EXPORTS, which is a different risk. It imports only 20% of its food.",
    "D": "Country D is a wheat exporter that imports just 5% of its food.",
    "E": "Country E imports 40% of its food. That is a real risk, but less than Country C's 85%."},
  vocab=["food security", "global supply chain", "interdependence"]))

P.append(dict(id="U5-P27", topic="5.9", lo="PSO-5.E", skill="5.D", difficulty="hard",
  stem="In 2022, the war in Ukraine blocked grain shipments from Black Sea ports, and bread and flour prices rose in wheat-importing countries such as Egypt and Lebanon. This example best illustrates which concept?",
  options={
    "A": "Global food distribution networks are affected by political relationships and trade routes.",
    "B": "Von Thünen's model predicts the location of wheat farming within a single country.",
    "C": "The Green Revolution ended wheat imports in North Africa and Southwest Asia.",
    "D": "Subsistence farmers are the main suppliers of wheat to global markets.",
    "E": "Food prices are set only by local weather in the country where food is eaten."},
  answer="A",
  explanation="Egypt and Lebanon buy a lot of wheat from abroad, much of it from Ukraine and Russia. When war blocked the ships leaving Black Sea ports, those countries could not get the grain as easily, so prices rose. A conflict in one place hurt food prices in another. The CED says global food distribution is shaped by political relationships, infrastructure, and patterns of world trade.",
  whyNot={
    "B": "Von Thünen explains land use around one market, not a war disrupting global trade.",
    "C": "These countries still import large amounts of wheat. That is why prices rose.",
    "D": "Most wheat on world markets comes from large commercial farms, not subsistence farmers.",
    "E": "Prices rose because of a war in another country, not local weather."},
  vocab=["global supply chain", "food security", "interdependence"]))

# ---------------- 5.10 Consequences of Agricultural Practices (IMP-5.A) ----------------
P.append(dict(id="U5-P28", topic="5.10", lo="IMP-5.A", skill="1.A", difficulty="easy",
  stem="Which of the following best describes soil salinization?",
  options={
    "A": "The washing away of topsoil by heavy rain on bare fields",
    "B": "The planting of different crops in a field each year to restore nutrients",
    "C": "The clearing of forest by cutting and burning vegetation",
    "D": "The spread of desert-like conditions into dry grasslands",
    "E": "The buildup of salts in soil, often caused by irrigation in dry climates where water evaporates quickly"},
  answer="E",
  explanation="All water carries a little bit of salt. When farmers irrigate in a hot, dry place, the water evaporates and leaves the salt behind. Year after year the salt builds up until crops can't grow well. This has happened in parts of Pakistan, Iraq, Australia, and California's Central Valley.",
  whyNot={
    "A": "That is soil erosion.",
    "B": "That is crop rotation, a conservation practice.",
    "C": "That is slash and burn.",
    "D": "That is desertification."},
  vocab=["soil salinization", "irrigation"]))

P.append(dict(id="U5-P29", topic="5.10", lo="IMP-5.A", skill="2.E", difficulty="medium",
  stem="Rice terraces carved into steep hillsides in the Philippines and on the Indonesian island of Bali best illustrate which of the following?",
  options={
    "A": "Desertification caused by overgrazing on hillsides",
    "B": "Farmers changing the landscape to create flat fields and control water on steep slopes",
    "C": "Land left as forest because it is too steep to farm",
    "D": "The long-lot survey system dividing land along a river",
    "E": "Shifting cultivation moving from one hillside to another every few years"},
  answer="B",
  explanation="Rice paddies need flat, flooded fields. Farmers on steep mountains built terraces, like giant stairs, so each step holds water and soil. Terraces slow down rain running downhill, which cuts erosion. The CED lists terraces as an agricultural practice that alters the landscape.",
  whyNot={
    "A": "Terraces are for crops, and they fight erosion. They are not caused by overgrazing.",
    "C": "The hills ARE farmed. That is the whole point of terraces.",
    "D": "Long lots are strips along rivers in French areas, not hillside steps.",
    "E": "Terraces are permanent. Farmers use the same terraces for generations."},
  vocab=["terrace farming", "landscape modification"]))

P.append(dict(id="U5-P30", topic="5.10", lo="IMP-5.A", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="LAND COVER IN A TROPICAL FRONTIER REGION (HYPOTHETICAL DATA)",
    columns=["Year", "Forest (% of region)", "Cattle pasture (% of region)", "Cropland, mostly soybeans (% of region)"],
    rows=[
      ["1990", "82", "10", "2"],
      ["2005", "70", "19", "6"],
      ["2020", "61", "25", "11"]],
    source="Hypothetical data"),
  stem="Which conclusion is best supported by the data in the table?",
  options={
    "A": "Forest in the region expanded as farmland was abandoned.",
    "B": "Cropland in the region was converted back into forest.",
    "C": "Forest was cleared and replaced mainly by cattle pasture and soybean fields.",
    "D": "Cattle pasture in the region decreased by more than half.",
    "E": "Land cover in the region stayed about the same over 30 years."},
  answer="C",
  explanation="Forest fell from 82% to 61% of the region, a loss of 21 percentage points. Over the same time, pasture rose 15 points and cropland rose 9 points. So the forest was cut down and turned into ranches and soybean farms. This is land cover change, an environmental effect of agriculture listed in the CED, and it matches what has happened in parts of the Amazon.",
  whyNot={
    "A": "Forest SHRANK, from 82% to 61%.",
    "B": "Cropland grew, from 2% to 11%.",
    "D": "Pasture more than DOUBLED, from 10% to 25%.",
    "E": "Every row changed by many percentage points."},
  vocab=["deforestation", "land cover change"]))

# ---------------- 5.11 Challenges of Contemporary Agriculture (IMP-5.B) ----------------
P.append(dict(id="U5-P31", topic="5.11", lo="IMP-5.B", skill="1.A", difficulty="easy",
  stem="Which of the following best describes a food desert?",
  options={
    "A": "An area where residents have limited access to affordable, healthy food, such as fresh fruits and vegetables",
    "B": "A dry region where crops can be grown only with irrigation",
    "C": "A region that produces more food than its people can eat",
    "D": "A farm that grows only one crop for export",
    "E": "Land that has been damaged by overgrazing and turned into desert"},
  answer="A",
  explanation="A food desert has nothing to do with sand. It is a neighborhood, often a low-income city area or an isolated rural area, where there is no full-service grocery store nearby, so people mostly buy food at gas stations or fast-food places. The CED lists food deserts as a challenge to feeding people.",
  whyNot={
    "B": "That describes a dry farming region, not a food desert.",
    "C": "That is a food surplus region.",
    "D": "That is monocropping for export.",
    "E": "That is desertification."},
  vocab=["food desert", "food insecurity"]))

P.append(dict(id="U5-P32", topic="5.11", lo="IMP-5.B", skill="1.D", difficulty="easy",
  stem="Families pay a nearby farm at the start of the growing season and then pick up a box of fresh produce from that farm every week. This arrangement is an example of",
  options={
    "A": "plantation agriculture",
    "B": "agribusiness vertical integration",
    "C": "pastoral nomadism",
    "D": "community-supported agriculture",
    "E": "the Green Revolution"},
  answer="D",
  explanation="In community-supported agriculture (CSA), customers buy a \"share\" of a local farm's harvest ahead of time. The farmer gets money up front, and the families get fresh, local food each week. It is part of the local-food movement listed in the CED.",
  whyNot={
    "A": "Plantations grow cash crops on large estates, usually for export.",
    "B": "Vertical integration is one big company controlling many steps of food production.",
    "C": "Pastoral nomadism is moving herds of animals to find pasture.",
    "E": "The Green Revolution spread high-yield seeds and chemicals in developing countries."},
  vocab=["community-supported agriculture (CSA)", "local-food movement"]))

P.append(dict(id="U5-P33", topic="5.11", lo="IMP-5.B", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="THREE COUNTIES NEAR A FAST-GROWING METROPOLITAN AREA (HYPOTHETICAL DATA)",
    columns=["County", "Distance from city center (miles)", "Farmland 2000 (acres)", "Farmland 2020 (acres)", "Population growth 2000–2020 (%)"],
    rows=[
      ["North County", "15", "220,000", "120,000", "+140"],
      ["West County", "35", "310,000", "250,000", "+60"],
      ["Far County", "70", "400,000", "395,000", "+5"]],
    source="Hypothetical data"),
  stem="The data in the table best illustrate which challenge of contemporary agriculture?",
  options={
    "A": "Farmland lost to suburbanization as a metropolitan area expands",
    "B": "Soil salinization caused by heavy irrigation",
    "C": "Loss of biodiversity from genetically modified crops",
    "D": "Growth of shifting cultivation near large cities",
    "E": "Food deserts forming in remote rural counties"},
  answer="A",
  explanation="The county closest to the city grew the fastest (+140%) and lost the most farmland (100,000 acres, almost half). The far county barely grew and kept almost all its farms. As the city spreads, houses, roads, and shopping centers are built on farmland. The CED lists land lost to suburbanization as a challenge to feeding a growing population.",
  whyNot={
    "B": "The table shows nothing about irrigation or salt.",
    "C": "The table shows nothing about crop types or biodiversity.",
    "D": "Shifting cultivation is not practiced in this setting, and farmland is disappearing, not moving.",
    "E": "The table measures farmland and population, not access to grocery stores."},
  vocab=["suburbanization", "urban sprawl", "farmland loss"]))

# ---------------- 5.12 Women in Agriculture (IMP-5.C) ----------------
P.append(dict(id="U5-P34", topic="5.12", lo="IMP-5.C", skill="2.B", difficulty="medium",
  stem="In many rural regions where men migrate to cities or other countries for wage work, the role of women in agriculture tends to",
  options={
    "A": "disappear, because farms are abandoned when men leave",
    "B": "grow, because women take on more of the farm work and decision-making",
    "C": "shift entirely to factory work in the same rural region",
    "D": "stay exactly the same, because migration does not affect farm labor",
    "E": "become limited to large mechanized wheat farms"},
  answer="B",
  explanation="When men leave to earn wages somewhere else, someone still has to grow the family's food. In much of South Asia, Sub-Saharan Africa, and Central America, women pick up more of the farm work and start making more of the farm decisions. Researchers call this the \"feminization of agriculture.\" The CED says women's roles in food production vary from place to place depending on the type of production.",
  whyNot={
    "A": "Farms usually keep running, with women doing more of the work.",
    "C": "The farm work still needs doing, and rural regions often have few factory jobs.",
    "D": "Migration changes who does the farm work.",
    "E": "Families affected by this migration are mostly small farms, not large mechanized wheat farms."},
  vocab=["feminization of agriculture", "rural-to-urban migration"]))

P.append(dict(id="U5-P35", topic="5.12", lo="IMP-5.C", skill="3.D", difficulty="medium",
  stimulus=dict(type="bar",
    title="WOMEN'S ROLE IN AGRICULTURE IN FOUR COUNTRIES (HYPOTHETICAL DATA)",
    categories=["Country 1", "Country 2", "Country 3", "Country 4"],
    series=[dict(name="Women as % of agricultural workers", values=[48, 42, 30, 25]),
            dict(name="Women as % of agricultural landholders", values=[15, 12, 20, 18])],
    yLabel="Percent", yMax=60,
    source="Hypothetical data"),
  stem="Which conclusion is best supported by the chart?",
  options={
    "A": "In every country, women hold a larger share of farmland than men do.",
    "B": "Country 4 has the largest share of women working in agriculture.",
    "C": "In every country, women's share of farm work is greater than their share of landholding.",
    "D": "In Country 3, women hold a larger share of farmland than they do of farm work.",
    "E": "Women make up more than half of agricultural workers in every country."},
  answer="C",
  explanation="Compare the two bars for each country. The first bar (share of workers) is always taller than the second (share of landholders): 48 vs. 15, 42 vs. 12, 30 vs. 20, 25 vs. 18. So women do a big part of the farm work but hold a much smaller part of the land. This gap is real in many countries, and it matters because people without land titles often can't get loans, seed, or fertilizer.",
  whyNot={
    "A": "Women hold 12% to 20% of landholdings. Men hold the rest, so men hold more everywhere.",
    "B": "Country 4 has the SMALLEST share (25%). Country 1 has the largest (48%).",
    "D": "In Country 3, women are 30% of workers but only 20% of landholders.",
    "E": "No country reaches 50%. The highest is 48%."},
  vocab=["women in agriculture", "land tenure"]))

P.append(dict(id="U5-P36", topic="5.12", lo="IMP-5.C", skill="2.D", difficulty="hard",
  stem="Which statement best explains why women's roles in food production differ between small-scale subsistence farming regions and highly mechanized commercial farming regions?",
  options={
    "A": "Women are not involved in any kind of food production in commercial farming regions.",
    "B": "Subsistence farming uses so much machinery that women are not needed in the fields.",
    "C": "Women's roles depend only on climate, not on the type of farming.",
    "D": "In subsistence regions women often do much of the hand labor of growing and preparing food, while mechanized farms need fewer workers and are more often owned and run by men.",
    "E": "Mechanized commercial farms always employ more women than subsistence farms do."},
  answer="D",
  explanation="On small subsistence farms, growing food takes lots of hand work, and in many regions women do much of the planting, weeding, harvesting, and food processing for the family. On big mechanized farms, machines do most of the work, so far fewer workers are needed, and owners and operators have more often been men. Women's roles change with the TYPE of farming, which is exactly what the CED says.",
  whyNot={
    "A": "Women work and run farms and food businesses in commercial regions too. The roles just differ.",
    "B": "Subsistence farming uses very LITTLE machinery and lots of hand labor.",
    "C": "The CED says roles depend on the type of production, not only on climate.",
    "E": "\"Always\" is wrong, and mechanized farms employ far fewer people of any gender."},
  vocab=["women in agriculture", "subsistence agriculture", "commercial agriculture"]))
