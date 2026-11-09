# Unit 7 practice items P33-P38: coverage additions after the ChatGPT Pro review (Nov 8, 2026, item 26):
# complementarity, economies of scale, growth poles, social measures of development,
# sustainable urban transportation, and how a financial crisis spreads between economies.
# Appended (not inserted) so existing item IDs do not change.
P = []

P.append(dict(id="U7-P33", topic="7.6", lo="PSO-7.A", skill="1.D", difficulty="easy",
  stem="Country J has large forests but few paper mills. Country K has many paper mills but has already cut most of its own forests. Country J ships logs to Country K. Which concept best explains why trade happens between these two places?",
  options={
    "A": "Deindustrialization",
    "B": "Economies of scale",
    "C": "Import substitution",
    "D": "Complementarity",
    "E": "A break-of-bulk point"},
  answer="D",
  explanation="Complementarity means one place has a supply of something that another place needs. Country J has extra logs, and Country K needs logs for its mills, so trade makes sense. Your AP course guide names complementarity and comparative advantage as the two bases for trade.",
  whyNot={
    "A": "Deindustrialization is the loss of factory jobs. Nothing here says jobs are disappearing.",
    "B": "Economies of scale means making more units lowers the cost of each one. It does not explain why these two places trade.",
    "C": "Import substitution means making goods at home instead of importing them. Country K is importing logs, not replacing imports.",
    "E": "A break-of-bulk point is where cargo switches transport modes. It does not explain why the trade exists."},
  vocab=["complementarity", "comparative advantage"]))

P.append(dict(id="U7-P34", topic="7.7", lo="PSO-7.A", skill="1.D", difficulty="medium",
  stem="A carmaker closes three small assembly plants and builds one very large plant that makes as many cars as the three plants did together, at a lower cost per car. Which concept best explains the lower cost per car?",
  options={
    "A": "Economies of scale",
    "B": "The multiplier effect",
    "C": "Deindustrialization",
    "D": "Just-in-time delivery",
    "E": "Outsourcing of production"},
  answer="A",
  explanation="Economies of scale means the cost of making each unit drops as a company makes more units in one place. One big plant can spread the cost of its buildings, machines, and managers over many more cars, so each car costs less to make.",
  whyNot={
    "B": "The multiplier effect is about new jobs spreading to other local businesses, not the cost of each car.",
    "C": "Deindustrialization is a decline in manufacturing. The company is still making the same number of cars.",
    "D": "Just-in-time delivery is about timing parts deliveries. The stem is about making more cars in one bigger plant.",
    "E": "Outsourcing means hiring another company to do the work. Here the carmaker builds its own bigger plant."},
  vocab=["economies of scale", "post-Fordism"]))

P.append(dict(id="U7-P35", topic="7.7", lo="PSO-7.A", skill="1.B", difficulty="medium",
  stem="A government picks one small inland city and invests heavily there, building a new airport and a technology park and offering tax breaks to high-tech firms. Its goal is for growth in that city to spread to the surrounding region. This strategy is best described as creating",
  options={
    "A": "a break-of-bulk point",
    "B": "a commodity-dependent economy",
    "C": "a maquiladora district",
    "D": "a deindustrialized region",
    "E": "a growth pole"},
  answer="E",
  explanation="A growth pole is a place where a government or company concentrates investment so that growth will spread outward to nearby areas. New firms bring jobs, those jobs bring suppliers and services, and the surrounding region benefits too.",
  whyNot={
    "A": "A break-of-bulk point is where cargo switches transport modes, such as ship to train. An inland technology park is not that.",
    "B": "A commodity-dependent economy relies on exporting a few raw materials. This plan targets high-tech firms.",
    "C": "Maquiladoras are assembly plants in Mexico near the U.S. border, not inland technology parks.",
    "D": "Deindustrialization is a loss of industry. This plan is trying to add new industry and jobs."},
  vocab=["growth pole", "multiplier effect", "high-technology industry"]))

P.append(dict(id="U7-P36", topic="7.3", lo="SPS-7.C", skill="1.A", difficulty="easy",
  stem="Which of the following sets of data would best show differences in social development, rather than economic output, among countries?",
  options={
    "A": "GDP per capita, GNI per capita, and GNP per capita",
    "B": "Infant mortality rates, literacy rates, and access to health care",
    "C": "Number of factories, kilometers of railroad, and coal output",
    "D": "Share of workers in industry, manufactured exports, and tariffs",
    "E": "Foreign direct investment, national debt, and currency exchange rates"},
  answer="B",
  explanation="Social measures show how well people live: whether babies survive, whether people can read, and whether they can see a doctor. Your AP course guide lists infant mortality, literacy, and access to health care as measures of development, alongside economic measures like GDP and GNI.",
  whyNot={
    "A": "GDP, GNI, and GNP all measure economic output or income, not social development.",
    "C": "Factories, railroads, and coal output measure industry, not people's health or education.",
    "D": "Industrial jobs, exports, and tariffs describe the economy and trade, not social well-being.",
    "E": "Investment, debt, and exchange rates are financial measures, not social ones."},
  vocab=["infant mortality rate", "literacy rate", "social development"]))

P.append(dict(id="U7-P37", topic="7.8", lo="IMP-7.A", skill="2.C", difficulty="medium",
  stem="A fast-growing city has heavy traffic, poor air quality, and many residents who cannot afford cars. Which project best fits the goals of sustainable development?",
  options={
    "A": "Widening the main highways so that more private cars can reach downtown each day",
    "B": "Building a new coal-fired power plant to keep electricity cheap for local factories",
    "C": "Opening a low-fare electric bus line that links poorer neighborhoods to job centers",
    "D": "Moving the city's most polluting factories to a poorer district at the city's edge",
    "E": "Replacing a downtown park with parking garages so drivers spend less time circling"},
  answer="C",
  explanation="Sustainable development meets people's needs today without harming the future. A low-fare electric bus line cuts car traffic and air pollution, and it helps people without cars reach jobs. Your AP course guide names public transportation projects as one way the UN Sustainable Development Goals measure progress.",
  whyNot={
    "A": "More highway lanes usually invite more car traffic and pollution, and they do not help people who cannot afford cars.",
    "B": "Burning more coal adds air pollution and greenhouse gases.",
    "D": "Moving polluting factories shifts the harm onto poorer residents instead of reducing it.",
    "E": "Losing a park and adding parking encourages more driving and removes green space."},
  vocab=["sustainable development", "public transportation", "Sustainable Development Goals (SDGs)"]))

P.append(dict(id="U7-P38", topic="7.6", lo="PSO-7.A", skill="5.B", difficulty="medium",
  stem="In 2008, a financial crisis that began with failing home loans in the United States spread around the world. Within months, many export factories in China cut jobs. Which of the following best explains how the crisis reached factory workers in China?",
  options={
    "A": "Spending fell in the United States and Europe, so orders for exported goods dropped.",
    "B": "Chinese banks had made most of the home loans in the United States.",
    "C": "The World Trade Organization ordered China to close its export factories.",
    "D": "China raised tariffs on imported parts, so its export factories could no longer get supplies.",
    "E": "The crisis pushed Chinese wages up sharply, so factories could no longer afford their workers."},
  answer="A",
  explanation="When the crisis hit, people and businesses in the United States and Europe cut back on spending. They bought fewer phones, clothes, and toys, many of which were made in China. With fewer orders, Chinese export factories cut jobs. A problem that started in one country's housing market reached workers on the other side of the world because their economies were connected by trade.",
  whyNot={
    "B": "U.S. home loans were made mostly by U.S. banks and lenders, not Chinese banks.",
    "C": "The WTO sets trade rules. It does not order countries to close factories.",
    "D": "The crisis did not spread through new Chinese tariffs. Factories cut jobs because orders from abroad fell.",
    "E": "Wages did not jump because of the crisis. Factories cut jobs because they had fewer orders to fill."},
  vocab=["global financial crisis", "interdependence", "globalization"]))

# P39 added after the final blind check (Nov 8): agglomeration was never the keyed concept.
P.append(dict(id="U7-P39", topic="7.7", lo="PSO-7.A", skill="1.D", difficulty="easy",
  stem="Hundreds of computer-chip and software firms have located near one another in one metropolitan area, where they share skilled workers, specialized suppliers, and new ideas. This clustering is best described as",
  options={
    "A": "deindustrialization",
    "B": "commodity dependence",
    "C": "a break-of-bulk point",
    "D": "import substitution",
    "E": "agglomeration"},
  answer="E",
  explanation="Agglomeration means firms cluster together so they can share workers, suppliers, and ideas, which lowers their costs. Silicon Valley in California is a famous example.",
  whyNot={
    "A": "Deindustrialization is a loss of manufacturing jobs. These firms are gathering in one place, not leaving.",
    "B": "Commodity dependence means relying on exporting a few raw materials or crops, not clustering high-tech firms.",
    "C": "A break-of-bulk point is where cargo switches from one kind of transport to another, such as ship to train.",
    "D": "Import substitution is a policy of making goods at home instead of importing them. It does not describe firms clustering."},
  vocab=["agglomeration", "high-technology industry"]))
