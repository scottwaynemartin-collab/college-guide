# Unit 2 practice items P22-P42 (topics 2.6-2.12). Run via assemble.py (data.py names are preloaded).
P = []

# ---------------- 2.6 Malthusian Theory (IMP-2.B) ----------------
P.append(dict(id="U2-P22", topic="2.6", lo="IMP-2.B", skill="2.E", difficulty="medium",
  stimulus=dict(type="line",
    title="POPULATION AND FOOD PRODUCTION IN COUNTRY N, 1960–2020 (INDEX, 1960 = 100) (HYPOTHETICAL DATA)",
    xLabel="Year", yLabel="Index (1960 = 100)",
    categories=MAL_YEARS,
    series=[dict(name="Population", values=MAL_POP), dict(name="Food production", values=MAL_FOOD)],
    yMax=400,
    description="Line graph with two lines, population and food production, for Country N from 1960 to 2020. Both lines are index numbers that start at 100 in 1960.",
    source="Hypothetical data"),
  stem="To what degree does Malthusian theory explain the trends in Country N shown in the graph?",
  options={
    "A": "It explains them well, because population grew geometrically and caused famine by 2000.",
    "B": "It explains them well, because food grew arithmetically while population grew faster.",
    "C": "It explains them partly, because population and food production grew at the same rate.",
    "D": "It explains them poorly, because food production grew faster than population did.",
    "E": "It explains them poorly, because Country N's population declined after 1960."},
  answer="D",
  explanation="Malthus predicted population would outgrow food. In Country N the opposite happened: from 1960 to 2020, population grew to 2.65 times its 1960 level, but food production grew to 3.95 times. That means about 49% more food per person (395 ÷ 265 ≈ 1.49). Critics of Malthus point to cases like this, where new technology, such as Green Revolution seeds and fertilizer, raised food output faster than population.",
  whyNot={
    "A": "The graph shows no famine. Food production stayed ahead of population the whole time.",
    "B": "Food production (395) grew faster than population (265), the opposite of what Malthus predicted.",
    "C": "The two lines split apart after 1960. Food production grew much faster.",
    "E": "Population rose every decade, from 100 to 265."},
  vocab=["Malthusian theory", "critiques of Malthus", "Green Revolution"]))

P.append(dict(id="U2-P23", topic="2.6", lo="IMP-2.B", skill="1.C", difficulty="hard",
  stem="Which of the following best describes how neo-Malthusians, such as Paul Ehrlich, built on the ideas of Thomas Malthus?",
  options={
    "A": "They argued that population growth encourages farmers to invent better tools and farming methods.",
    "B": "They warned that growing populations also use up water, energy, and other resources and harm the environment.",
    "C": "They argued that hunger results mainly from poverty and unequal food distribution, not from too many people.",
    "D": "They predicted that birth rates would rise again once countries reach the last stage of the demographic transition.",
    "E": "They argued that new technology lets food supply grow faster than population, so famine is unlikely."},
  answer="B",
  explanation="Malthus focused on food. Neo-Malthusians, like Paul Ehrlich in The Population Bomb (1968), widened the worry: more people also means more demand for water, energy, land, and minerals, plus more pollution. They argue that Earth has a carrying capacity, and many support family planning to slow growth.",
  whyNot={
    "A": "That is Esther Boserup's critique of Malthus, not a neo-Malthusian idea.",
    "C": "That is a critique of Malthus. These critics say poverty and unequal distribution, not population size, cause hunger.",
    "D": "Neo-Malthusians worry about too much growth. They did not predict birth rates rising again.",
    "E": "That is the hopeful view of Malthus's critics, the opposite of a neo-Malthusian warning."},
  vocab=["neo-Malthusian", "Malthusian theory", "carrying capacity"]))

# ---------------- 2.7 Population Policies (SPS-2.A) ----------------
P.append(dict(id="U2-P24", topic="2.7", lo="SPS-2.A", skill="1.A", difficulty="easy",
  stem="A government offers families a cash payment for each baby, extends paid parental leave, and pays for most child-care costs. These steps are best described as",
  options={
    "A": "an antinatalist policy",
    "B": "an immigration policy",
    "C": "a pronatalist policy",
    "D": "a family-planning program",
    "E": "a guest worker program"},
  answer="C",
  explanation="Pronatalist policies try to raise the birth rate. Cash for babies, paid leave, and cheaper child care lower the cost of raising children, so families may decide to have more. France and several other European and East Asian countries use policies like these because their fertility rates are below replacement level (about 2.1 children per woman).",
  whyNot={
    "A": "Antinatalist policies try to LOWER the birth rate.",
    "B": "Immigration policies control who can move into a country. These steps are about births.",
    "D": "Family-planning programs help people choose to have fewer children or space them out. That usually lowers birth rates.",
    "E": "Guest worker programs bring in temporary foreign workers. They do not reward births."},
  vocab=["pronatalist policy", "antinatalist policy", "replacement level"]))

P.append(dict(id="U2-P25", topic="2.7", lo="SPS-2.A", skill="2.C", difficulty="medium",
  stem="China's one-child policy, in place from about 1980 until 2015, limited most urban couples to one child. Which of the following is a long-term consequence of this policy?",
  options={
    "A": "A sharp rise in the share of children under age 15 in China's population",
    "B": "A large increase in China's total fertility rate during the 1990s",
    "C": "A sex ratio at birth that favored girls over boys for several decades",
    "D": "A large wave of older adults emigrating from China to retire abroad",
    "E": "A rapidly aging population and more boys than girls born for many years"},
  answer="E",
  explanation="With far fewer births, China now has a smaller share of young people and a growing share of older people, so it is aging quickly and its workforce is shrinking. Because many families preferred sons, some used sex-selective abortion, so for many years far more boys than girls were born. China switched to a two-child policy in 2016 and a three-child policy in 2021.",
  whyNot={
    "A": "Fewer births made the share of children go DOWN, not up.",
    "B": "The policy lowered fertility. China's TFR fell well below replacement level.",
    "C": "It was the reverse: more boys than girls were born.",
    "D": "China's aging comes from low births and longer lives, not from older people leaving."},
  vocab=["antinatalist policy", "sex ratio", "aging population"]))

P.append(dict(id="U2-P26", topic="2.7", lo="SPS-2.A", skill="2.C", difficulty="medium",
  stem="Country P adopts a points-based immigration system that gives applicants points for university degrees, job skills in demand, language ability, and being of working age. Which outcome is most likely?",
  options={
    "A": "Most new immigrants will be retirees moving to join their adult children in Country P.",
    "B": "New immigrants will tend to be younger, skilled workers who add to the labor force.",
    "C": "Most new immigrants will be refugees fleeing armed conflict in nearby countries.",
    "D": "The share of Country P's population aged 65 and older will rise more quickly.",
    "E": "Country P's sending countries will gain skilled workers who move from Country P."},
  answer="B",
  explanation="A points system picks immigrants based on what the country wants. Points for degrees, needed skills, language, and age favor young, educated workers. That adds people to the working-age part of the population pyramid, which can help a country with low birth rates. Canada and Australia are well-known users of points-based systems.",
  whyNot={
    "A": "Points for being of working age make retirees less likely to qualify.",
    "C": "Refugees are admitted for protection, not through points for job skills.",
    "D": "Adding young workers slows aging. It does not speed it up.",
    "E": "Skilled workers move INTO Country P, so it gains skills (a brain gain), and sending countries may lose them."},
  vocab=["immigration policy", "brain drain", "labor force"]))

# ---------------- 2.8 Women and Demographic Change (SPS-2.B) ----------------
P.append(dict(id="U2-P27", topic="2.8", lo="SPS-2.B", skill="3.D", difficulty="medium",
  stimulus=dict(type="bar",
    title="AVERAGE TOTAL FERTILITY RATE OF DISTRICTS IN COUNTRY E, GROUPED BY SHARE OF WOMEN AGED 20–24 WHO COMPLETED SECONDARY SCHOOL (HYPOTHETICAL DATA)",
    categories=EDU_CATS,
    series=[dict(name="Average total fertility rate (children per woman)", values=EDU_TFR)],
    yLabel="Children per woman", yMax=7,
    text="Each district in Country E is placed in one group based on the share of its women aged 20–24 who completed secondary school.",
    description="Bar chart with five groups of districts. Districts where under 20% of young women completed secondary school average 5.9 children per woman; 20–39%, 4.8; 40–59%, 3.6; 60–79%, 2.6; 80% or more, 1.9.",
    source="Hypothetical data"),
  stem="Which of the following conclusions is best supported by the chart?",
  options={
    "A": "Districts where more women finished secondary school tend to have lower fertility rates.",
    "B": "Districts in the highest education group still have fertility above replacement level.",
    "C": "Moving from the 60–79% group to the top group lowers fertility by about two children.",
    "D": "Fertility in the lowest education group is about twice the fertility in the top group.",
    "E": "The chart proves that schooling by itself made fertility fall in each district over time."},
  answer="A",
  explanation="Going from districts where few women finished secondary school to districts where most did, the average fertility rate drops step by step, from 5.9 to 1.9 children per woman. Your AP course guide says more education, jobs, health care, and access to contraception for women have lowered fertility in most of the world. The chart shows a link (a correlation); by itself it does not prove the cause.",
  whyNot={
    "B": "Replacement level is about 2.1. The top group's 1.9 is below replacement.",
    "C": "The drop from 2.6 to 1.9 is about 0.7 children, not 2.",
    "D": "5.9 is about three times 1.9, not twice.",
    "E": "The chart compares districts at one point in time. It shows a pattern, not proof of a single cause or of change over time."},
  vocab=["total fertility rate", "replacement level", "correlation"]))

P.append(dict(id="U2-P28", topic="2.8", lo="SPS-2.B", skill="1.B", difficulty="medium",
  stem="As more women in a country take paid jobs outside the home, the country's total fertility rate often falls. Which of the following best explains this relationship?",
  options={
    "A": "Women with paid jobs usually marry earlier, which shortens their childbearing years.",
    "B": "Paid jobs usually require women to move to rural areas, where families are smaller.",
    "C": "Countries with more working women usually pass laws that limit the size of families.",
    "D": "Working women often delay marriage and children, and each child costs more lost income.",
    "E": "Women with paid jobs usually have less access to health care and to contraception."},
  answer="D",
  explanation="When women have careers, many choose to finish school and start working before they marry or have children. Starting later leaves fewer years to have children. Also, each child can mean time away from a paying job (economists call this an opportunity cost), so many families choose to have fewer children.",
  whyNot={
    "A": "It is the reverse: women with paid jobs tend to marry LATER.",
    "B": "Paid jobs are more common in cities, and rural families are usually larger, not smaller.",
    "C": "Few countries limit family size by law. Lower fertility here comes mostly from families' own choices.",
    "E": "Women with paid jobs usually have MORE access to health care and contraception."},
  vocab=["total fertility rate", "women and demographic change", "opportunity cost"]))

P.append(dict(id="U2-P29", topic="2.8", lo="SPS-2.B", skill="1.D", difficulty="medium",
  stem="In the 1880s, E. G. Ravenstein observed that women were more likely than men to migrate within their home country, while men were more likely to move to other countries. Today, women and girls make up almost half of all international migrants. Which of the following best explains this change?",
  options={
    "A": "Laws in most countries now limit men's emigration, so more women move abroad instead.",
    "B": "Women today have more children than in the 1880s, so whole families move abroad together.",
    "C": "Women's economic roles have expanded, and many now move abroad for jobs such as nursing.",
    "D": "Most international moves are now short trips across one border, like women's moves in the 1880s.",
    "E": "Destination countries now give women's visa applications priority over applications from men."},
  answer="C",
  explanation="Ravenstein's laws describe migration in the 1800s, when most women's moves were short, for example from farms to nearby towns to work as household servants. Since then, women's roles in the economy have grown. Many women now migrate on their own for work, for example as nurses, caregivers, and domestic and service workers. That helps explain why women and girls are now about 48% of international migrants.",
  whyNot={
    "A": "Countries do not generally stop men from leaving. Men are still a little more than half of international migrants.",
    "B": "Women today have FEWER children than in the 1880s.",
    "D": "International migrants move many different distances. The change comes from women's changing economic roles.",
    "E": "There is no general rule that favors women's visas. Women's share grew because more women migrate for work."},
  vocab=["Ravenstein's laws of migration", "international migration", "women and demographic change"]))

# ---------------- 2.9 Aging Populations (SPS-2.C) ----------------
P.append(dict(id="U2-P30", topic="2.9", lo="SPS-2.C", skill="1.A", difficulty="easy",
  stem="The dependency ratio compares which groups in a population?",
  options={
    "A": "The number of people who live in cities and the number who live in rural areas",
    "B": "The number of men and the number of women in the same age group",
    "C": "The number of births and the number of deaths in a single year",
    "D": "The number of immigrants and the number of emigrants in a single year",
    "E": "People under age 15 or age 65 and older, compared with people aged 15 to 64"},
  answer="E",
  explanation="Dependency ratio = (people aged 0–14 + people 65 and older) ÷ people aged 15–64 × 100. Children and older adults are called 'dependents' because most do not work full-time, so working-age people support them through families and taxes. A higher ratio means each worker supports more people.",
  whyNot={
    "A": "That compares the urban and rural population.",
    "B": "That is the sex ratio.",
    "C": "Births minus deaths gives the rate of natural increase.",
    "D": "That is net migration."},
  vocab=["dependency ratio", "aging population"]))

_t = AGE_T
P.append(dict(id="U2-P31", topic="2.9", lo="SPS-2.C", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="POPULATION OF COUNTRY T BY BROAD AGE GROUP, 2025 (HYPOTHETICAL DATA)",
    columns=["Age group", "Population (millions)"],
    rows=[["0–14", f"{_t['young']:.1f}"], ["15–64", f"{_t['work']:.1f}"], ["65 and older", f"{_t['old']:.1f}"],
          ["Total", f"{_t['young'] + _t['work'] + _t['old']:.1f}"]],
    description="Table of Country T's population in three broad age groups, in millions: 0–14, 9.6; 15–64, 40.0; 65 and older, 14.4; total, 64.0.",
    source="Hypothetical data"),
  stem="Based on the table, what is Country T's dependency ratio?",
  options={"A": "24", "B": "36", "C": "60", "D": "62.5", "E": "167"},
  answer="C",
  explanation="Dependents are ages 0–14 and 65+: 9.6 + 14.4 = 24.0 million. Working-age people (15–64): 40.0 million. Dependency ratio = 24.0 ÷ 40.0 × 100 = 60. So there are 60 dependents for every 100 working-age people.",
  whyNot={
    "A": "24 counts only the children (9.6 ÷ 40 × 100). Add the people 65 and older too.",
    "B": "36 counts only the people 65 and older (14.4 ÷ 40 × 100). Add the children too.",
    "D": "62.5 is working-age people as a percent of the total (40 ÷ 64 × 100).",
    "E": "167 flips the fraction (40 ÷ 24 × 100). Put the dependents on top."},
  vocab=["dependency ratio", "working-age population"]))

P.append(dict(id="U2-P32", topic="2.9", lo="SPS-2.C", skill="2.C", difficulty="medium",
  stem="In Country S, life expectancy is rising, and the fertility rate has been below replacement level for 30 years. Which of the following is the most likely economic consequence over the next 20 years?",
  options={
    "A": "Fewer workers paying taxes for each retiree, straining pension and health systems",
    "B": "A growing number of young workers competing for a shrinking number of jobs",
    "C": "Rising demand for new elementary schools as the number of children increases",
    "D": "A falling dependency ratio as more and more people move into the working-age group",
    "E": "A rapid rise in the crude birth rate as the large older generation retires"},
  answer="A",
  explanation="Low fertility means fewer young people are growing up to become workers. Longer lives mean more people are retired, and for longer. So each worker pays taxes that support more retirees, and health care costs rise. Governments may respond by raising the retirement age, raising taxes, cutting benefits, encouraging births, or admitting more working-age immigrants. Japan and Italy face this challenge today.",
  whyNot={
    "B": "Low fertility means FEWER young workers, so labor shortages are more likely than job competition.",
    "C": "Fertility is below replacement, so the number of children is shrinking, not growing.",
    "D": "As the older group grows and the working-age group shrinks, the dependency ratio RISES.",
    "E": "Retiring does not raise birth rates. An older population usually has a LOWER crude birth rate."},
  vocab=["aging population", "dependency ratio", "replacement level"]))

# ---------------- 2.10 Causes of Migration (IMP-2.C) ----------------
P.append(dict(id="U2-P33", topic="2.10", lo="IMP-2.C", skill="1.A", difficulty="easy",
  stem="Several years of drought destroy crops in a farming region, and many families move to cities in another part of the country. The drought is best described as which type of migration factor?",
  options={
    "A": "An economic pull factor",
    "B": "A political push factor",
    "C": "A cultural pull factor",
    "D": "An environmental push factor",
    "E": "An intervening opportunity along the way"},
  answer="D",
  explanation="A push factor makes people want to LEAVE a place. A drought comes from the natural environment, so it is an environmental push factor. Floods, hurricanes, and rising sea levels are other environmental push factors.",
  whyNot={
    "A": "Pull factors attract people TO a place, like jobs in a city. The drought pushes people away.",
    "B": "Political push factors include war, persecution, and unfair laws. A drought is a natural event.",
    "C": "Cultural pull factors include joining a community that shares your language or religion.",
    "E": "An intervening opportunity is a chance found along the way that makes a migrant stop before reaching the planned destination."},
  vocab=["push factor", "pull factor", "environmental factors"]))

P.append(dict(id="U2-P34", topic="2.10", lo="IMP-2.C", skill="1.D", difficulty="medium",
  stem="Amina leaves her village planning to look for work in the capital city, 600 kilometers away. On the way, she stops in a mining town 200 kilometers from home, finds a good job, and settles there. Her decision to stay in the mining town is an example of",
  options={
    "A": "an intervening obstacle",
    "B": "a forced migration",
    "C": "an intervening opportunity",
    "D": "chain migration",
    "E": "a political push factor at the origin"},
  answer="C",
  explanation="An intervening opportunity is a chance (like a job) found between where a migrant started and where she planned to go, so she stops early. Amina found a job in the mining town, so she never went on to the capital. An intervening obstacle is the opposite: something that blocks or slows a move, like a mountain range or a strict border.",
  whyNot={
    "A": "An obstacle blocks a move. Amina was not blocked; she found something better along the way.",
    "B": "Amina chose to move, so this is voluntary migration.",
    "D": "Chain migration means following family or friends who moved earlier. Amina followed a job.",
    "E": "Political push factors include war and persecution. Amina left to find work, an economic reason."},
  vocab=["intervening opportunity", "intervening obstacle", "voluntary migration"]))

P.append(dict(id="U2-P35", topic="2.10", lo="IMP-2.C", skill="3.E", difficulty="medium",
  stimulus=dict(type="bar",
    title="PEOPLE WHO MOVED TO CITY M IN 2025, BY DISTANCE FROM THEIR PREVIOUS HOME (HYPOTHETICAL DATA)",
    categories=DIST_CATS,
    series=[dict(name="Migrants (thousands)", values=DIST_VALS)],
    yLabel="Thousands of migrants", yMax=50,
    description="Bar chart of people who moved to City M in 2025, grouped by how far away they lived before: under 50 km, 42 thousand; 50–199 km, 24 thousand; 200–499 km, 12 thousand; 500–999 km, 6 thousand; 1,000 km or more, 4 thousand.",
    source="Hypothetical data"),
  stem="The pattern in the chart is most consistent with which of Ravenstein's laws of migration?",
  options={
    "A": "Each migration flow produces a counterflow in the opposite direction.",
    "B": "Long-distance migrants usually head for major centers of trade and industry.",
    "C": "Women are more likely than men to migrate within their home country.",
    "D": "Most migrants move for economic reasons, such as finding better jobs.",
    "E": "Most migrants move a short distance from where they lived before."},
  answer="E",
  explanation="The bars get shorter as distance gets longer: 42,000 people came from less than 50 km away, but only 4,000 came from 1,000 km or more. Ravenstein noticed this in the 1880s: most migrants move a short distance. This is called distance decay. Distance itself is an intervening obstacle, because longer moves cost more and people know less about faraway places.",
  whyNot={
    "A": "The chart shows only people arriving in City M, not anyone leaving, so it cannot show a counterflow.",
    "B": "The chart shows one city only, so it cannot show where long-distance migrants usually go.",
    "C": "The chart does not separate migrants by sex.",
    "D": "The chart shows distance, not the reasons people moved."},
  vocab=["Ravenstein's laws of migration", "distance decay"]))

# ---------------- 2.11 Forced and Voluntary Migration (IMP-2.D) ----------------
P.append(dict(id="U2-P36", topic="2.11", lo="IMP-2.D", skill="1.A", difficulty="easy",
  stem="Fighting between armed groups forces thousands of families to leave their homes. They move to a camp in another province of the same country. These families are best described as",
  options={
    "A": "refugees",
    "B": "internally displaced persons",
    "C": "asylum seekers awaiting a decision",
    "D": "guest workers",
    "E": "transnational migrants"},
  answer="B",
  explanation="Internally displaced persons (IDPs) are forced to flee their homes but stay inside their own country. These families did not cross an international border, so they are IDPs, not refugees. Refugees have crossed into another country to escape war, violence, or persecution.",
  whyNot={
    "A": "Refugees have crossed an international border. These families stayed in their own country.",
    "C": "Asylum seekers have asked another country for protection and are waiting for a decision.",
    "D": "Guest workers choose to move for temporary jobs in another country.",
    "E": "Transnational migrants live in one country while keeping strong ties to another. These families were forced to move within their own country."},
  vocab=["internally displaced persons", "refugee", "forced migration"]))

P.append(dict(id="U2-P37", topic="2.11", lo="IMP-2.D", skill="4.B", difficulty="medium",
  stimulus=dict(type="schematicMap",
    title="ONE FAMILY'S MOVES WITHIN COUNTRY W, 1998–2015 (HYPOTHETICAL)",
    canvas=dict(width=800, height=340),
    features=[
      dict(kind="land", name="", polygon=[[30, 30], [760, 18], [782, 170], [760, 322], [40, 318], [18, 180]], style="small"),
      dict(kind="island", name="Village", center=[110, 255], radius=9),
      dict(kind="island", name="Market town", center=[300, 205], radius=15),
      dict(kind="island", name="Regional city", center=[495, 145], radius=23),
      dict(kind="island", name="Capital city", center=[680, 88], radius=33),
      dict(kind="arrow", name="Move 1 (1998): village to market town", **{"from": [122, 250], "to": [283, 211]}),
      dict(kind="arrow", name="Move 2 (2006): market town to regional city", **{"from": [316, 199], "to": [470, 153]}),
      dict(kind="arrow", name="Move 3 (2015): regional city to capital city", **{"from": [519, 137], "to": [645, 98]})],
    legend=[dict(swatch="small", label="Country W"), dict(swatch="land", label="Settlement (larger circle = larger population)")],
    description="Map of Country W. Arrows show one family's three moves: from a village to a market town in 1998, from the market town to a regional city in 2006, and from the regional city to the capital city in 2015. Each place is larger than the one before it.",
    source="Hypothetical map"),
  stem="The map shows the moves made by one family over 17 years. Which type of migration does it best illustrate?",
  options={
    "A": "Step migration",
    "B": "Chain migration",
    "C": "Transhumance",
    "D": "Forced migration",
    "E": "Transnational migration"},
  answer="A",
  explanation="Step migration means moving in a series of smaller steps, usually from smaller places to bigger ones: village → market town → regional city → capital. Ravenstein noticed this pattern in the 1880s. Each step can give migrants time to save money and get used to city life before the next move.",
  whyNot={
    "B": "Chain migration means following relatives or friends who moved earlier. The map shows one family's own moves.",
    "C": "Transhumance is moving herds between seasonal pastures and back again every year.",
    "D": "Nothing on the map shows that the family was forced to move.",
    "E": "Transnational migrants move to another country and keep ties to both. These moves all stay inside Country W."},
  vocab=["step migration", "internal migration", "rural-to-urban migration"]))

P.append(dict(id="U2-P38", topic="2.11", lo="IMP-2.D", skill="1.D", difficulty="medium",
  stem="In the early 1900s, a man from a small town in southern Italy moved to Buenos Aires, Argentina. Over the next 20 years, his brothers, cousins, and neighbors followed him, helped by his letters and money, and settled in the same neighborhood. This pattern is best described as",
  options={
    "A": "step migration",
    "B": "forced migration",
    "C": "internal migration",
    "D": "chain migration",
    "E": "transhumance"},
  answer="D",
  explanation="Chain migration happens when migrants follow family members or friends who moved before them. The first migrants send information and money and help with housing and jobs, so the next people can move more easily. It explains why people from one place often cluster in one neighborhood, like many Italian families in Buenos Aires.",
  whyNot={
    "A": "Step migration is one migrant moving in stages, like village → town → city.",
    "B": "These people chose to move, with help from relatives. That is voluntary migration.",
    "C": "They crossed an ocean to another country. That is international, not internal, migration.",
    "E": "Transhumance is moving with livestock between seasonal pastures."},
  vocab=["chain migration", "voluntary migration", "international migration"]))

P.append(dict(id="U2-P39", topic="2.11", lo="IMP-2.D", skill="1.D", difficulty="medium",
  stem="A nurse from the Philippines works in a hospital in Canada. She sends money to her parents in Manila every month, video-calls her family daily, votes in Philippine elections from abroad, and plans to retire in the Philippines. She is best described as",
  options={
    "A": "an internally displaced person",
    "B": "an asylum seeker",
    "C": "a step migrant",
    "D": "a refugee",
    "E": "a transnational migrant"},
  answer="E",
  explanation="A transnational migrant lives in one country but keeps strong ties to another: sending money home (remittances), staying in close contact, taking part in politics back home, and often planning to return. Cheap calls, video chats, and air travel make it easier than ever to live 'between' two countries.",
  whyNot={
    "A": "IDPs are forced to flee but stay inside their own country.",
    "B": "Asylum seekers are asking for protection from danger. She moved for work.",
    "C": "Step migration is a series of moves from smaller to larger places. Nothing here shows steps.",
    "D": "Refugees flee war, violence, or persecution. She chose to move for a job."},
  vocab=["transnational migration", "remittances", "voluntary migration"]))

# ---------------- 2.12 Effects of Migration (IMP-2.E) ----------------
P.append(dict(id="U2-P40", topic="2.12", lo="IMP-2.E", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="PERSONAL REMITTANCES RECEIVED BY SIX COUNTRIES, 2024",
    columns=["Country", "Remittances received (billions of US dollars)", "Remittances as a share of GDP (%)"],
    rows=[[c, (f"{usd / 1e9:.2f}" if usd < 1e9 else f"{usd / 1e9:.1f}"), f"{pct:.1f}"] for c, (usd, pct) in WB_REMIT_2024.items()],
    description="Table of personal remittances received in 2024 by India, Mexico, the Philippines, Nepal, Tajikistan, and Tonga, in billions of US dollars and as a percent of each country's GDP.",
    source="World Bank, World Development Indicators: personal remittances, received (current US$) (BX.TRF.PWKR.CD.DT) and personal remittances, received (% of GDP) (BX.TRF.PWKR.DT.GD.ZS), 2024 values, accessed November 8, 2026."),
  stem="Which of the following conclusions is best supported by the table?",
  options={
    "A": "India depends more on remittances than Nepal does, because India receives more money.",
    "B": "The countries with the largest populations depend most heavily on remittances.",
    "C": "The countries that receive the most remittance money depend on it least as a share of GDP.",
    "D": "Tonga's remittances are too small to matter much compared with the size of its economy.",
    "E": "Remittances make up a larger share of the economy in the Philippines than in Nepal."},
  answer="C",
  explanation="Look at both columns. India and Mexico receive the most money ($137.7 billion and $67.9 billion), but their economies are so big that remittances are only about 3.7% of their GDP. Smaller economies like Tajikistan (47.2%), Tonga (39.4%), and Nepal (26.0%) get far less money, yet it makes up a big part of their economies. For those countries, a recession in the places where their migrants work can hurt the whole country.",
  whyNot={
    "A": "Remittances are 26.0% of Nepal's GDP but only 3.7% of India's, so Nepal depends on them more.",
    "B": "India has the largest population in the table but the smallest share (3.7%, tied with Mexico).",
    "D": "Tonga's remittances are only $0.26 billion, but that equals 39.4% of its GDP.",
    "E": "Remittances are 8.7% of GDP in the Philippines and 26.0% in Nepal."},
  vocab=["remittances", "gross domestic product (GDP)", "effects of migration"]))

P.append(dict(id="U2-P41", topic="2.12", lo="IMP-2.E", skill="2.C", difficulty="medium",
  stem="Over 20 years, many doctors and nurses trained in Country D move to higher-income countries for better pay. Which of the following is the most likely effect on Country D?",
  options={
    "A": "A shortage of health-care workers after Country D paid to train them",
    "B": "A surplus of doctors that lowers wages for health-care workers in Country D",
    "C": "A brain gain that increases the number of medical specialists in Country D",
    "D": "A sharp rise in Country D's birth rate as more young adults stay at home",
    "E": "A drop in the money that families in Country D receive from relatives abroad"},
  answer="A",
  explanation="This is brain drain: highly educated, skilled people emigrate. Country D spent money training these doctors and nurses, but now other countries benefit from their skills. Patients in Country D may face longer waits and fewer clinics. Migrants may send money home, which helps some families, but it does not replace the lost health workers.",
  whyNot={
    "B": "Doctors are leaving, so there would be fewer, not more.",
    "C": "A brain gain happens in the countries that receive the doctors, not in Country D.",
    "D": "The people leaving are young adults, so this would tend to lower, not raise, births at home.",
    "E": "Migrants working abroad usually send MORE money home, not less."},
  vocab=["brain drain", "remittances", "effects of migration"]))

P.append(dict(id="U2-P42", topic="2.12", lo="IMP-2.E", skill="1.B", difficulty="medium",
  stem="Which of the following is the best example of a political effect of migration?",
  options={
    "A": "Restaurants serving migrants' home cooking open in a destination city's downtown.",
    "B": "A party in a destination country wins seats by promising to limit immigration.",
    "C": "Migrants send home money that pays for new houses in their home villages.",
    "D": "Children of migrants grow up speaking both their parents' language and the local one.",
    "E": "A destination country's construction industry fills jobs with migrant workers."},
  answer="B",
  explanation="Political effects involve laws, governments, voting, and power. When migration becomes a big election issue, parties can gain or lose seats because of their immigration plans, and governments may change border and citizenship laws. Migration also has economic effects (jobs, remittances) and cultural effects (food, language, religion).",
  whyNot={
    "A": "New restaurants are a cultural (and economic) effect: the spread of food traditions.",
    "C": "Money sent home (remittances) is an economic effect.",
    "D": "Children who speak two languages is a cultural effect.",
    "E": "Filling jobs with migrant workers is an economic effect."},
  vocab=["effects of migration", "political effects", "cultural effects"]))

# ---------------- v2026-11-08c additions (coverage gaps named in the ChatGPT Pro review) ----------------
P.append(dict(id="U2-P43", topic="2.11", lo="IMP-2.D", skill="1.D", difficulty="easy",
  stem="During a civil war, members of a family in Country R are threatened because of their ethnic group. They cross the border into Country S and ask for protection. Country S approves their claim because they would face persecution if they returned. The family members are now best described as",
  options={
    "A": "internally displaced persons",
    "B": "refugees",
    "C": "asylum seekers",
    "D": "guest workers",
    "E": "step migrants"},
  answer="B",
  explanation="Refugees are people who have fled their country because of persecution, war, or violence and who are protected in another country. This family crossed an international border, and Country S approved their claim, so they are refugees. Before the decision, they were asylum seekers. People who flee but stay inside their own country are internally displaced persons.",
  whyNot={
    "A": "Internally displaced persons stay inside their own country. This family crossed into Country S.",
    "C": "Asylum seekers are still waiting for a decision. Once Country S approved the claim, the family became refugees.",
    "D": "Guest workers are admitted for temporary jobs. This family fled persecution.",
    "E": "Step migration is a series of moves from smaller to larger places. This family made one move to escape danger."},
  vocab=["refugee", "asylum seeker", "forced migration"]))

P.append(dict(id="U2-P44", topic="2.11", lo="IMP-2.D", skill="1.D", difficulty="easy",
  stem="From the 1500s to the 1800s, the transatlantic slave trade carried millions of people from West and Central Africa to plantations and mines in the Americas. Which of the following best describes this movement?",
  options={
    "A": "Voluntary migration, drawn mainly by economic pull factors such as plantation jobs",
    "B": "Chain migration, because each group followed relatives who had moved earlier",
    "C": "Guest worker migration, because people were recruited for a fixed number of years",
    "D": "Forced migration, because people were captured and moved against their will",
    "E": "Step migration, because people moved through a series of larger and larger ports"},
  answer="D",
  explanation="The transatlantic slave trade was forced migration: people were captured, enslaved, and shipped across the Atlantic against their will. Your AP course guide lists slavery as a type of forced migration. Its effects still shape the Americas today, including the music, foods, religions, and languages of places such as Brazil, the Caribbean, and the United States.",
  whyNot={
    "A": "Voluntary migration means people decide to move. Enslaved people had no choice.",
    "B": "Chain migration means choosing to follow relatives. These people were taken by force.",
    "C": "Guest workers agree to work for a set time and are paid. Enslaved people had no such choice.",
    "E": "People were shipped by force; they did not move step by step on their own."},
  vocab=["forced migration", "slavery", "transatlantic slave trade"]))

P.append(dict(id="U2-P45", topic="2.12", lo="IMP-2.E", skill="1.D", difficulty="medium",
  stem="Since the 1950s, many people from India, Pakistan, and what is now Bangladesh have settled in cities in the United Kingdom. Which of the following is the best example of a cultural effect of this migration on those cities?",
  options={
    "A": "Many migrants send part of their wages each month to relatives in South Asia.",
    "B": "Hospitals in these cities hire migrant doctors and nurses to help fill staff shortages.",
    "C": "Political parties debate whether to raise or lower the number of visas issued.",
    "D": "The average age of residents in these cities becomes slightly younger.",
    "E": "Restaurants, mosques, temples, and festivals like Diwali become part of city life."},
  answer="E",
  explanation="Cultural effects involve food, religion, language, music, and celebrations. When migrants settle in a city, their traditions become part of its cultural landscape: restaurants, places of worship, shops, and festivals. Over time, people who are not migrants may share in these traditions too.",
  whyNot={
    "A": "Money sent home (remittances) is an economic effect, mostly felt in the home region.",
    "B": "Filling jobs is an economic effect on the destination.",
    "C": "Debates over visa numbers are a political effect.",
    "D": "A younger average age is a demographic effect."},
  vocab=["effects of migration", "cultural landscape", "cultural effects"]))

P.append(dict(id="U2-P46", topic="2.11", lo="IMP-2.D", skill="1.D", difficulty="easy",
  stem="In 1961, West Germany and Turkey signed an agreement under which Turkish workers came to West Germany to fill factory and construction jobs for a limited time. Under this agreement, the workers were admitted as",
  options={
    "A": "guest workers",
    "B": "refugees",
    "C": "asylum seekers",
    "D": "internally displaced persons",
    "E": "transnational migrants"},
  answer="A",
  explanation="Guest workers are people a country admits to work for a limited time. In the 1950s and 1960s, West Germany recruited workers from Italy, Greece, Turkey, and other countries. Recruitment stopped in 1973, but many Turkish workers stayed, and their families joined them, so a temporary flow became a permanent community. Many of these migrants also became transnational, keeping close ties to Turkey.",
  whyNot={
    "B": "Refugees flee persecution or war. These workers were recruited for jobs.",
    "C": "Asylum seekers ask another country for protection. These workers came under a labor agreement.",
    "D": "Internally displaced persons stay inside their own country. These workers moved from Turkey to West Germany.",
    "E": "Many of these workers later kept strong ties to both countries, which is transnational, but the agreement admitted them as temporary guest workers."},
  vocab=["guest worker", "transnational migration", "chain migration"]))
