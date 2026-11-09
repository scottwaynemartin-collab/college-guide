# Unit 2 exam items E01-E25. Run via assemble.py (data.py names are preloaded).
E = []
def q(**k): E.append(k)


q(id="U2-E01", n=1, topic="2.1", lo="PSO-2.A", skill="2.B", difficulty="medium",
  stem="Most of Russia's people live west of the Ural Mountains, even though most of Russia's land lies east of them. Which of the following best explains this distribution?",
  options={
    "A": "Russia's government has banned permanent settlement in Siberia ever since the Soviet era.",
    "B": "Most of Russia's oil and natural gas fields are located west of the Ural Mountains.",
    "C": "The west has a milder climate and a longer history of farming, cities, and trade links.",
    "D": "Eastern Russia is mostly hot desert that gets too little rain to support farming.",
    "E": "The Ural Mountains are so high and rugged that few settlers have ever crossed them."},
  answer="C",
  rationales={
    "A": "Incorrect. Russia has not banned settlement east of the Urals. The Soviet Union actually encouraged people to settle and work in Siberia, where cities such as Novosibirsk grew.",
    "B": "Incorrect. Much of Russia's oil and natural gas comes from western Siberia, east of the Urals, so resource location does not explain the pattern.",
    "C": "Correct. Physical factors (a milder climate and longer growing season in the west, compared with long, severe winters and permafrost across much of Siberia) combine with human factors (centuries of farming, city growth, industry, and transportation links to the rest of Europe) to concentrate Russia's population west of the Urals.",
    "D": "Incorrect. Most of Siberia and the Russian Far East is cold forest (taiga) and tundra, not hot desert. Cold, not heat, limits settlement there.",
    "E": "Incorrect. The Urals are relatively low, old mountains, and roads and the Trans-Siberian Railway cross them. They are not a major barrier to settlement."},
  explanation="Western Russia is warmer and has a longer growing season, so farms and cities grew there first, and it is closer to the rest of Europe for trade. Most of Siberia has long, very cold winters and frozen ground (permafrost). Both physical factors (climate) and human factors (history, economics, transportation) explain where people live.")

q(id="U2-E02", n=2, topic="2.2", lo="PSO-2.D", skill="1.B", difficulty="medium",
  stem="A children's hospital that specializes in rare cancers is far more likely to be located in a large, densely populated metropolitan area than in a sparsely populated rural county. Which of the following best explains this pattern?",
  options={
    "A": "A specialized hospital needs a large number of possible patients within reach to keep operating.",
    "B": "Rural counties have higher physiological densities, which leaves little land for large hospitals.",
    "C": "Land in rural counties costs more than in metropolitan areas, which makes hospitals too costly to build.",
    "D": "National laws in most countries forbid hospitals from being built outside large cities.",
    "E": "Children in metropolitan areas are far more likely than rural children to develop cancer."},
  answer="A",
  rationales={
    "A": "Correct. Population density affects the provision of services. A highly specialized hospital needs many patients, doctors, and researchers to operate, so it locates where large numbers of people live within reach, and patients from sparsely populated rural areas travel to it.",
    "B": "Incorrect. Physiological density compares people with farmland. Sparsely populated rural counties usually have more land per person, not less, so a shortage of land is not the reason.",
    "C": "Incorrect. Land is usually cheaper in rural counties, where demand for it is lower.",
    "D": "Incorrect. Rural hospitals and clinics exist in many countries; no general law limits hospitals to large cities.",
    "E": "Incorrect. The hospital's location is explained by the number of patients who can reach it, not by a higher cancer rate among city children."},
  explanation="Expensive, specialized services need lots of patients or customers nearby. A big metro area has enough people to keep a specialty hospital busy. A sparse rural county does not, so families travel to the city. This is how population density shapes services like medical care.")

# ---- Set A: Country A pyramid, E03-E05 ----
q(id="U2-E03", n=3, set="pyrA", setLabel="Questions 3–5 refer to the population pyramid below.", topic="2.3", lo="PSO-2.F", skill="3.B", difficulty="easy",
  stimulus=dict(type="pyramid",
    title="POPULATION PYRAMID, COUNTRY A, 2025 (HYPOTHETICAL DATA)",
    ageGroups=AGES, male=PYR_A_M, female=PYR_A_F,
    description="Population pyramid for Country A with 17 five-year age groups, from 0–4 at the bottom to 80+ at the top. Males are on the left and females on the right; bar length is the percent of the total population.",
    source="Hypothetical data"),
  stem="Which of the following best describes the population of Country A shown in the pyramid?",
  options={
    "A": "It is aging, because older adults make up the largest share of the population.",
    "B": "It is shrinking, because each new group of children is smaller than the one before.",
    "C": "It is stable, because each age group is about the same size as the one above it.",
    "D": "It is young and growing quickly, because a large share of the population is under 15.",
    "E": "It has a high dependency ratio, mainly because so many people are 65 or older."},
  answer="D",
  rationales={
    "A": "Incorrect. People 65 and older are only about 3 percent of Country A's population; the top of the pyramid is very narrow.",
    "B": "Incorrect. A shrinking population would have a base narrower than the bars above it. Country A's base is its widest bar.",
    "C": "Incorrect. A stable (stationary) population has bars of similar size, like a column. Country A's bars shrink steadily with age.",
    "D": "Correct. The wide base shows that about 43 percent of the population is under age 15. This expansive pyramid signals high birth rates and rapid growth, because many young people will soon reach childbearing age.",
    "E": "Incorrect. Country A's dependency ratio is high, but because of its many children; people 65 and older are only about 3 percent of the population."},
  explanation="A wide bottom and a narrow top = an expansive pyramid. About 43% of Country A's people are under 15, and only about 3% are 65 or older. Lots of children today means lots of future parents, so the population will keep growing fast.")

q(id="U2-E04", n=4, set="pyrA", topic="2.5", lo="IMP-2.B", skill="3.C", difficulty="medium",
  stem="Country A's crude birth rate has stayed near 40 per 1,000 since 1980, while its crude death rate has fallen from 20 to 9 per 1,000. Based on this information and the pyramid, Country A is most likely in which stage of the demographic transition model?",
  options={
    "A": "Stage 1, because its birth and death rates are both high",
    "B": "Stage 2, because births stay high while deaths have fallen",
    "C": "Stage 3, because its birth rate is dropping toward its death rate",
    "D": "Stage 4, because its birth and death rates are both low",
    "E": "Stage 5, because its death rate is higher than its birth rate"},
  answer="B",
  rationales={
    "A": "Incorrect. In Stage 1 both rates are high, but Country A's death rate has fallen to 9 per 1,000, which is low.",
    "B": "Correct. A high, steady birth rate (about 40 per 1,000) combined with a sharply falling death rate is the signature of Stage 2. The widening gap between births and deaths produces rapid natural increase, which matches the pyramid's wide base.",
    "C": "Incorrect. In Stage 3 the birth rate falls, but Country A's birth rate has stayed near 40 per 1,000.",
    "D": "Incorrect. Country A's birth rate is high, and its wide-based pyramid shows many young people.",
    "E": "Incorrect. Country A's birth rate is far higher than its death rate, so its population is growing, not shrinking."},
  explanation="Stage 2 = deaths drop, births stay high, and the population booms. Country A's death rate fell from 20 to 9, but its birth rate stayed near 40. That big gap is why the pyramid has such a wide base.")

q(id="U2-E05", n=5, set="pyrA", topic="2.8", lo="SPS-2.B", skill="2.C", difficulty="medium",
  stem="Which of the following changes would most likely lower Country A's total fertility rate over the next several decades?",
  options={
    "A": "Lowering the minimum legal age at which women are allowed to marry",
    "B": "Expanding government cash programs that reward families for each additional child",
    "C": "Increasing the share of the workforce employed in subsistence farming",
    "D": "Reducing the number of clinics and midwives that serve rural villages",
    "E": "Expanding girls' schooling and women's access to health care and contraception"},
  answer="E",
  rationales={
    "A": "Incorrect. Earlier marriage usually means women begin having children earlier, which tends to raise fertility.",
    "B": "Incorrect. Rewards for each additional child are pronatalist incentives designed to raise fertility.",
    "C": "Incorrect. Farm families often rely on children's labor, so a larger farming workforce is associated with higher fertility.",
    "D": "Incorrect. Fewer clinics would likely raise infant and child deaths; where child deaths are high, families tend to have more children.",
    "E": "Correct. As the AP course framework notes, access to education, employment, health care, and contraception has reduced fertility rates in most parts of the world. Women with more schooling tend to marry later, work outside the home, and choose smaller families."},
  explanation="When girls stay in school longer, they usually marry later and have fewer children. When women can get health care and contraception, they can choose when and how many children to have, and more babies survive, so families do not need as many births. This is how changing roles for women lower fertility.")

q(id="U2-E06", n=6, topic="2.4", lo="IMP-2.A", skill="1.D", difficulty="medium",
  stem=f"Country R has a crude birth rate of {E06['cbr']} per 1,000 and a crude death rate of {E06['cdr']} per 1,000. If these rates stay the same and there is no migration, about how many years will it take Country R's population to double?",
  options={
    "A": "About 3.5 years",
    "B": "About 20 years",
    "C": "About 35 years",
    "D": "About 70 years",
    "E": "About 140 years"},
  answer="C",
  rationales={
    "A": "Incorrect. This divides 70 by 20 without first converting 20 per 1,000 into a percentage (2.0 percent).",
    "B": "Incorrect. This treats the natural increase of 20 per 1,000 as a number of years.",
    "C": "Correct. The rate of natural increase is (26 − 6) ÷ 10 = 2.0 percent. Using the rule of 70, the doubling time is 70 ÷ 2.0 = 35 years.",
    "D": "Incorrect. A doubling time of 70 years matches a growth rate of 1.0 percent, half of Country R's rate.",
    "E": "Incorrect. This multiplies 70 by 2.0 instead of dividing 70 by 2.0."},
  explanation="Two steps. 1) RNI = (26 − 6) ÷ 10 = 2.0%. 2) Rule of 70: 70 ÷ 2.0 = 35 years.")

q(id="U2-E07", n=7, topic="2.4", lo="IMP-2.A", skill="3.F", difficulty="hard",
  stem="In 2024, Japan's crude death rate was about 13 deaths per 1,000 people, while Niger's was about 9 per 1,000. Japan has one of the highest life expectancies in the world. Which of the following best explains why Japan's crude death rate is higher?",
  options={
    "A": "The crude death rate does not adjust for age, and Japan has a far larger share of older adults.",
    "B": "Japan's health-care system is less effective than Niger's at treating infectious diseases.",
    "C": "Niger's infant mortality rate is lower than Japan's, so fewer babies die in Niger each year.",
    "D": "Many older adults leave Niger to retire in other countries, which lowers Niger's death count.",
    "E": "Japan has a larger total population than Niger, so it records a higher number of deaths."},
  answer="A",
  rationales={
    "A": "Correct. The crude death rate counts all deaths per 1,000 people without adjusting for age structure. Japan's population is very old (about 3 in 10 people are 65 or older), while Niger's is very young, so Japan records more deaths per 1,000 people even though people in Japan live much longer. This is a limitation of the crude death rate.",
    "B": "Incorrect. Japan has a strong health-care system and very few deaths from infectious disease; its life expectancy is far higher than Niger's.",
    "C": "Incorrect. Niger's infant mortality rate is much higher than Japan's.",
    "D": "Incorrect. Retirement migration is not what keeps Niger's crude death rate low; its very young age structure is.",
    "E": "Incorrect. A crude death rate is a rate per 1,000 people, so it already accounts for total population size."},
  explanation="The crude death rate is just deaths per 1,000 people. It does not care how old the people are. Japan has lots of elderly people, and older people are more likely to die each year, even with great health care. Niger has mostly children and young adults. So Japan's crude death rate is higher even though people in Japan live much longer.")

q(id="U2-E08", n=8, topic="2.6", lo="IMP-2.B", skill="1.C", difficulty="hard",
  stem="Which of the following best describes how Esther Boserup's view of population growth differs from Thomas Malthus's view?",
  options={
    "A": "Boserup argued that food supply grows geometrically, while Malthus argued it grows arithmetically.",
    "B": "Boserup agreed that famine would limit population growth but predicted it would happen sooner.",
    "C": "Boserup argued that industrialization causes population growth, while Malthus blamed farming.",
    "D": "Boserup argued that population growth would damage the environment, not just the food supply.",
    "E": "Boserup argued that population pressure pushes farmers to farm more intensively and raise output."},
  answer="E",
  rationales={
    "A": "Incorrect. Boserup did not simply reverse Malthus's growth curves; she argued that population pressure itself leads to changes in farming methods.",
    "B": "Incorrect. Boserup was a critic of Malthus; she did not predict earlier famine.",
    "C": "Incorrect. The two disagreed about how food production responds to population growth, not about what causes population growth.",
    "D": "Incorrect. Concern about resource depletion and environmental damage beyond food is associated with neo-Malthusians, not with Boserup.",
    "E": "Correct. Boserup argued that as population grows, farmers respond by intensifying production (for example, shortening fallow periods, adding labor, irrigating, and adopting new tools), so food output can rise along with population. Malthus argued that food supply could not keep pace."},
  explanation="Malthus: more people → not enough food → famine. Boserup: more people → farmers work the land harder and smarter (more labor, less time leaving fields empty, irrigation, new tools) → more food. She saw population growth as a cause of change in farming, not just a problem.")

q(id="U2-E09", n=9, topic="2.7", lo="SPS-2.A", skill="2.D", difficulty="medium",
  stem="In the 1970s, Singapore's government urged families to \"Stop at Two.\" In 1987, it began urging families who could afford it to have three or more children and offered incentives for larger families. Which of the following best explains this change?",
  options={
    "A": "Singapore's death rate rose sharply in the 1980s, so more births were needed to replace deaths.",
    "B": "Once fertility fell below replacement, the government moved from antinatalist to pronatalist policy.",
    "C": "International agreements required Singapore to raise its birth rate to ease global labor shortages.",
    "D": "Singapore's population was growing too fast, so the government wanted larger, more stable families.",
    "E": "The government shifted from pronatalist to antinatalist policy in order to slow population growth."},
  answer="B",
  rationales={
    "A": "Incorrect. Singapore's death rate was low in the 1980s; the concern was that births had fallen too far.",
    "B": "Correct. \"Stop at Two\" was an antinatalist campaign. After Singapore's total fertility rate fell below replacement level (about 2.1) by the late 1970s (about 1.8 in 1977), the government grew concerned about an aging population and future labor shortages, so it switched to pronatalist incentives.",
    "C": "Incorrect. Population policies like these are set by national governments for national goals, not required by international agreements.",
    "D": "Incorrect. Encouraging larger families would speed up population growth, not slow it.",
    "E": "Incorrect. The order is reversed: Singapore moved from an antinatalist policy (\"Stop at Two\") to a pronatalist one (three or more)."},
  explanation="First Singapore wanted FEWER births (antinatalist: \"Stop at Two\"). Fertility fell below replacement level (about 2.1 children per woman). Then the government worried about too few future workers and too many older people, so it flipped to pronatalist: encouraging families who could afford it to have three or more children.")

# ---- Set B: Country B pyramid, E10-E11 ----
q(id="U2-E10", n=10, set="pyrB", setLabel="Questions 10–11 refer to the population pyramid below.", topic="2.9", lo="SPS-2.C", skill="3.B", difficulty="medium",
  stimulus=dict(type="pyramid",
    title="POPULATION PYRAMID, COUNTRY B, 2025 (HYPOTHETICAL DATA)",
    ageGroups=AGES, male=PYR_B_M, female=PYR_B_F,
    description="Population pyramid for Country B with 17 five-year age groups, from 0–4 at the bottom to 80+ at the top. Males are on the left and females on the right; bar length is the percent of the total population.",
    source="Hypothetical data"),
  stem="Which of the following conclusions is best supported by Country B's population pyramid?",
  options={
    "A": "Country B's birth rate has risen steadily over the past 25 years.",
    "B": "Country B's population is young, with most people under age 30.",
    "C": "Country B has more males than females in its oldest age groups.",
    "D": "Country B has more people aged 65 and older than children under 15.",
    "E": "Country B's death rates are much higher for women than for men."},
  answer="D",
  rationales={
    "A": "Incorrect. Each of the youngest age groups is smaller than the one above it, so births have been falling, not rising.",
    "B": "Incorrect. The largest age groups are people in their 40s, 50s, and 60s, and people under 30 are only about one-quarter of the population.",
    "C": "Incorrect. In the 80+ group, the female bar is much longer than the male bar.",
    "D": "Correct. About one-quarter of Country B's population is 65 or older, compared with about 12 percent under age 15. A pyramid that is narrow at the base and wide near the top signals decades of low fertility and long life expectancy, which together produce an aging population.",
    "E": "Incorrect. More women than men survive to old age, which shows that women's death rates are lower, not higher."},
  explanation="Add up the bars: about a quarter of Country B's people are 65 or older, but only about 12% are under 15. A narrow base and a wide top mean few babies and many older people. That is an aging population.")

q(id="U2-E11", n=11, set="pyrB", topic="2.9", lo="SPS-2.C", skill="3.E", difficulty="medium",
  stem="If the trends shown in the pyramid continue, which of the following is most likely to happen in Country B over the next 20 years?",
  options={
    "A": "Its working-age population will shrink as retirees increase, straining pensions.",
    "B": "Its dependency ratio will fall as large numbers of children reach working age.",
    "C": "It will need many more elementary schools to serve a growing number of young children.",
    "D": "Its crude death rate will fall as the large middle-aged groups grow older.",
    "E": "Its labor force will grow quickly as many young adults enter the job market."},
  answer="A",
  rationales={
    "A": "Correct. The large groups now aged 45–64 will move into retirement over the next 20 years, while much smaller groups replace them in the workforce. Fewer workers supporting more retirees raises the dependency ratio and strains pension and health-care systems.",
    "B": "Incorrect. The child age groups are the smallest in the pyramid, so few people will enter the workforce, and the dependency ratio will most likely rise.",
    "C": "Incorrect. The base of the pyramid is narrow and shrinking, so the number of children is falling.",
    "D": "Incorrect. As the large middle-aged groups grow older, more people will reach ages with high death rates, so the crude death rate will likely rise.",
    "E": "Incorrect. The groups entering the job market (today's 0- to 19-year-olds) are small, so the labor force will likely shrink."},
  explanation="The biggest groups in Country B are in their 40s, 50s, and 60s. In 20 years most of them will be retired. The groups that replace them as workers are much smaller. Fewer workers paying taxes and more retirees collecting pensions and needing health care = pressure on the system.")

q(id="U2-E12", n=12, topic="2.7", lo="SPS-2.A", skill="2.C", difficulty="hard",
  stem="Country J's total fertility rate is 1.3, and its working-age population has begun to shrink. Which policy would most quickly increase the number of working-age people in Country J?",
  options={
    "A": "Offering a large cash bonus to parents for each child born in the next five years",
    "B": "Expanding free access to contraception and family-planning services",
    "C": "Admitting more immigrants aged 20 to 40 through new work visas",
    "D": "Lowering the age at which workers can retire with a full pension",
    "E": "Raising the minimum age at which young people may leave school"},
  answer="C",
  rationales={
    "A": "Incorrect. Even if a pronatalist bonus raised births, babies born now would not reach working age for 15 to 20 years.",
    "B": "Incorrect. Family-planning services tend to lower birth rates, which would shrink future working-age groups even more.",
    "C": "Correct. Of the policies listed, only admitting working-age immigrants adds people to the 15–64 age groups right away. Immigration policy can change a population's size and composition quickly, which is why many low-fertility countries use immigration to address labor shortages.",
    "D": "Incorrect. Retirement age does not change how many people are aged 15 to 64, and earlier retirement would reduce the number of people actually working.",
    "E": "Incorrect. School-leaving age does not change how many people are of working age; it only delays young people's entry into the workforce."},
  explanation="Babies take about 20 years to grow into workers, so pronatalist bonuses are slow. Immigrants who are already 20 to 40 years old join the working-age group the day they arrive. That is why countries with very low fertility often use immigration to fill jobs.")

q(id="U2-E13", n=13, topic="2.3", lo="PSO-2.E", skill="5.B", difficulty="medium",
  stem="Country L's national sex ratio is about 100. However, in a remote mining region of Country L, the sex ratio for people aged 20 to 49 is about 160. Which of the following best explains the difference between these two scales?",
  options={
    "A": "Women in the mining region have much longer life expectancies than women in other regions.",
    "B": "The national sex ratio is calculated differently from a regional sex ratio.",
    "C": "Most babies born in the mining region are girls, which lowers the regional sex ratio.",
    "D": "Women from across Country L move to the mining region to take mining jobs.",
    "E": "Mining jobs attract young men from other regions, many of whom move without families."},
  answer="E",
  rationales={
    "A": "Incorrect. Longer-lived women would increase the number of women, which would lower the sex ratio, not raise it.",
    "B": "Incorrect. Sex ratio is calculated the same way at every scale: males per 100 females.",
    "C": "Incorrect. More girls would lower the sex ratio, but a ratio of 160 means far more males than females.",
    "D": "Incorrect. If many women moved in, the regional sex ratio would fall below 100, not rise to 160.",
    "E": "Correct. A sex ratio of 160 means about 160 men for every 100 women. Migration for jobs filled mostly by men, such as mining, concentrates young men in one region. At the national scale this local imbalance is averaged out, which shows that sex-ratio patterns vary with the scale of analysis."},
  explanation="Sex ratio = males per 100 females, so 160 means 160 men for every 100 women. Remote mining jobs draw lots of young men who come to work, often leaving families at home. When you look at the whole country, this one region is averaged in with everyone else, so the national number stays near 100.")

q(id="U2-E14", n=14, topic="2.8", lo="SPS-2.B", skill="2.B", difficulty="medium",
  stem="The average total fertility rate in Latin America and the Caribbean fell from about 5.2 children per woman in 1970 to about 1.9 in 2020. Which of the following best explains this decline?",
  options={
    "A": "Governments across the region adopted one-child policies modeled on China's policy.",
    "B": "As cities grew, women gained more schooling, paid work, and access to contraception.",
    "C": "Rising infant mortality led families to put off having children until conditions improved.",
    "D": "Most young women emigrated from the region, leaving few women of childbearing age.",
    "E": "Farming became the main source of jobs, so families needed fewer children to help."},
  answer="B",
  rationales={
    "A": "Incorrect. Latin American governments did not adopt one-child policies; the decline came mainly from social and economic change.",
    "B": "Correct. As the region urbanized, more women stayed in school longer, worked outside the home, and gained access to health care and contraception. As the AP course framework notes, these changes in women's roles have reduced fertility rates in most parts of the world.",
    "C": "Incorrect. Infant mortality fell, not rose, across the region during these decades.",
    "D": "Incorrect. Emigration from the region was large, but most women of childbearing age stayed. The total fertility rate measures births per woman, not the number of women.",
    "E": "Incorrect. The region urbanized rapidly, and the share of workers in farming fell. Farm families also tend to have more children, not fewer."},
  explanation="In 50 years, the average number of children per woman in Latin America dropped from about 5 to under 2. As people moved to cities, girls stayed in school longer, more women took paid jobs, and birth control became easier to get. Those changes in women's lives led families to have fewer children.")

q(id="U2-E15", n=15, topic="2.11", lo="IMP-2.D", skill="1.D", difficulty="easy",
  stem="A journalist receives threats after reporting on government corruption. She flies to another country and applies for protection there. Her application has not yet been decided. She is best described as",
  options={
    "A": "an internally displaced person",
    "B": "a guest worker",
    "C": "an economic migrant",
    "D": "an asylum seeker",
    "E": "a step migrant"},
  answer="D",
  rationales={
    "A": "Incorrect. Internally displaced persons flee their homes but remain inside their own country; the journalist crossed an international border.",
    "B": "Incorrect. Guest workers move by choice for temporary jobs, usually through a labor program.",
    "C": "Incorrect. She left because of threats to her safety, not mainly to find a job or higher wages.",
    "D": "Correct. An asylum seeker is a person who has fled to another country and asked for protection but whose claim has not yet been decided. If her claim is approved, she may be granted refugee status.",
    "E": "Incorrect. Step migration is a series of moves from smaller to larger places; she made one move to escape danger."},
  explanation="Asylum seeker = someone who fled to another country, asked for protection, and is still waiting for an answer. If the answer is yes, she may become a recognized refugee. If she had fled but stayed inside her own country, she would be an internally displaced person.")

# ---- Set C: Country M DTM line graph, E16-E17 ----
q(id="U2-E16", n=16, set="dtmM", setLabel="Questions 16–17 refer to the graph below.", topic="2.5", lo="IMP-2.B", skill="3.B", difficulty="medium",
  stimulus=dict(type="line",
    title="CRUDE BIRTH AND DEATH RATES, COUNTRY M, 1800–2025 (HYPOTHETICAL DATA)",
    xLabel="Year", yLabel="Rate per 1,000 people",
    categories=DTM_M_YEARS,
    series=[dict(name="Crude birth rate", values=DTM_M_CBR), dict(name="Crude death rate", values=DTM_M_CDR)],
    yMax=40,
    description="Line graph of Country M's crude birth rate and crude death rate, per 1,000 people, from 1800 to 2025. Points are every 25 years.",
    source="Hypothetical data"),
  stem="During which period was Country M most clearly in Stage 2 of the demographic transition model?",
  options={
    "A": "1800 to 1825",
    "B": "1825 to 1875",
    "C": "1900 to 1950",
    "D": "1950 to 1975",
    "E": "2000 to 2025"},
  answer="B",
  rationales={
    "A": "Incorrect. From 1800 to 1825, birth and death rates were both high (35 to 38 per 1,000) and close together, with little natural increase: Stage 1.",
    "B": "Correct. From 1825 to 1875, the death rate fell from 35 to 23 per 1,000 while the birth rate stayed near 37 to 38. A falling death rate with a high, steady birth rate defines Stage 2, and natural increase rose from 0.3 percent to 1.4 percent a year.",
    "C": "Incorrect. From 1900 to 1950, the birth rate fell steeply (34 to 21) while the death rate fell more slowly: Stage 3.",
    "D": "Incorrect. From 1950 to 1975, the birth rate was still falling toward an already low death rate, which is late Stage 3.",
    "E": "Incorrect. From 2000 to 2025, both rates were low and close together: Stage 4."},
  explanation="Stage 2 = the death rate drops while the birth rate stays high. On the graph, that happens from 1825 to 1875: deaths fall from 35 to 23, but births stay around 37 to 38. The gap between the lines gets wider, so the population grows faster.")

q(id="U2-E17", n=17, set="dtmM", topic="2.5", lo="IMP-2.B", skill="1.B", difficulty="medium",
  stem="Which of the following best explains the decline in Country M's crude death rate between 1825 and 1925?",
  options={
    "A": "A rise in deaths from heart disease and cancer as people lived longer",
    "B": "A drop in the birth rate that reduced the number of infants who died",
    "C": "An increase in the share of older adults in Country M's population",
    "D": "Large-scale emigration of the oldest and sickest residents",
    "E": "Better sanitation, cleaner water, and a more reliable food supply"},
  answer="E",
  rationales={
    "A": "Incorrect. A shift toward chronic diseases such as heart disease and cancer happens after deaths from infectious disease have fallen; it does not by itself lower the death rate.",
    "B": "Incorrect. The death rate began falling around 1825, while the birth rate stayed high until about 1875, so falling births cannot be the main cause; the decline came from fewer deaths from disease and hunger.",
    "C": "Incorrect. A larger share of older adults would tend to raise the crude death rate, not lower it.",
    "D": "Incorrect. Most migrants are young adults; emigration of the old and sick is not a typical cause of falling death rates.",
    "E": "Correct. According to the epidemiological transition, death rates fall as improvements in sanitation, clean water, nutrition, and later medicine reduce deaths from infectious and parasitic diseases and from famine."},
  explanation="Death rates drop first because fewer people die young from infections and hunger. Clean water, sewers, better food, and later vaccines and medicine stop diseases like cholera. This is the epidemiological transition, and it explains Stage 2 of the DTM.")

q(id="U2-E18", n=18, topic="2.10", lo="IMP-2.C", skill="1.D", difficulty="medium",
  stem="Migrants from Country P hoping to reach jobs in Country Q must cross a wide desert and pass through Country S, which requires a transit visa that is expensive and slow to obtain. The desert and the visa requirement are best described as",
  options={
    "A": "pull factors",
    "B": "push factors",
    "C": "intervening obstacles",
    "D": "intervening opportunities",
    "E": "examples of distance decay"},
  answer="C",
  rationales={
    "A": "Incorrect. Pull factors attract migrants to a destination, such as the jobs in Country Q.",
    "B": "Incorrect. Push factors are conditions at the origin that make people want to leave Country P.",
    "C": "Correct. Intervening obstacles are barriers between the origin and the destination that make migration harder. The desert is an environmental obstacle, and the costly transit visa is a political obstacle.",
    "D": "Incorrect. Intervening opportunities are attractive options along the way that lead migrants to stop before reaching their destination.",
    "E": "Incorrect. Distance decay describes how interaction declines as distance increases; the desert and the visa rule are specific barriers along the route."},
  explanation="Intervening obstacles are things in the way between home and the destination. A desert is a physical (environmental) obstacle. A hard-to-get visa is a political obstacle. Obstacles do not make people want to leave or want to go; they make the trip harder.")

q(id="U2-E19", n=19, topic="2.1", lo="PSO-2.B", skill="1.D", difficulty="medium",
  stem="Country X has 60 million people and 400,000 square kilometers of land. Fifteen percent of its land is arable, and 24 million of its people work as farmers. What is Country X's physiological density?",
  options={
    "A": "60 people per square kilometer",
    "B": "150 people per square kilometer",
    "C": "400 people per square kilometer",
    "D": "1,000 people per square kilometer",
    "E": "10,000 people per square kilometer"},
  answer="D",
  rationales={
    "A": "Incorrect. This divides the number of farmers (24 million) by all land (400,000 square kilometers), which is not a standard density measure.",
    "B": "Incorrect. 150 is the arithmetic density: 60 million people ÷ 400,000 square kilometers of total land.",
    "C": "Incorrect. 400 is the agricultural density: 24 million farmers ÷ 60,000 square kilometers of arable land.",
    "D": "Correct. Arable land = 15 percent of 400,000 = 60,000 square kilometers. Physiological density = 60 million people ÷ 60,000 square kilometers = 1,000 people per square kilometer of arable land.",
    "E": "Incorrect. This results from treating 1.5 percent, rather than 15 percent, of the land as arable."},
  explanation="Physiological density = ALL people ÷ ARABLE land. Arable land: 15% × 400,000 = 60,000 sq km. Then 60,000,000 ÷ 60,000 = 1,000 people per sq km of farmland. (Arithmetic density uses all land; agricultural density counts only farmers.)")

q(id="U2-E20", n=20, topic="2.11", lo="IMP-2.D", skill="1.A", difficulty="easy",
  stem="Each spring, herders in the Alps move their cattle up to high mountain pastures, and each fall they bring the herds back down to valley farms. This seasonal movement is called",
  options={
    "A": "transhumance",
    "B": "step migration",
    "C": "chain migration",
    "D": "rural-to-urban migration",
    "E": "forced migration"},
  answer="A",
  rationales={
    "A": "Correct. Transhumance is the seasonal movement of herders and livestock between highland summer pastures and lowland winter pastures. It is one of the types of voluntary migration in the AP course framework.",
    "B": "Incorrect. Step migration is a series of moves, usually toward larger places, that does not repeat every year.",
    "C": "Incorrect. Chain migration is following relatives or friends who moved earlier.",
    "D": "Incorrect. The herders move between pastures and farms, not from the countryside to cities.",
    "E": "Incorrect. The herders choose to move with the seasons; no one forces them."},
  explanation="Transhumance = moving animals up to cool mountain pastures in summer and back down to the valleys in winter, every year. It happens in the Alps, the Andes, the Himalayas, and parts of Africa.")

# ---- Set D: Country V map, E21-E23 ----
q(id="U2-E21", n=21, set="mapV", setLabel="Questions 21–23 refer to the map and information below.", topic="2.1", lo="PSO-2.A", skill="4.C", difficulty="medium",
  stimulus=dict(type="schematicMap",
    title="POPULATION AND MIGRATION IN COUNTRY V, 2000–2020 (HYPOTHETICAL)",
    canvas=dict(width=800, height=420),
    features=[
      dict(kind="land", name="Coastal plain", polygon=[[118, 0], [250, 0], [250, 420], [110, 420], [92, 330], [112, 250], [90, 170], [114, 95], [96, 40]], labelAt=[180, 385], style="small"),
      dict(kind="land", name="River valley", polygon=[[250, 160], [630, 150], [630, 240], [250, 255]], labelAt=[470, 228], style="small"),
      dict(kind="land", name="Dry interior", polygon=[[250, 0], [630, 0], [630, 150], [250, 160]], labelAt=[440, 45]),
      dict(kind="land", name="Dry interior", polygon=[[250, 255], [630, 240], [630, 420], [250, 420]], labelAt=[440, 385]),
      dict(kind="land", name="Mountains", polygon=[[630, 0], [800, 0], [800, 420], [630, 420]], labelAt=[706, 210], style="power"),
      dict(kind="marker", name="City or town", points=[[160, 90], [150, 330], [330, 198], [450, 193], [560, 190]], symbol="baseN"),
      dict(kind="marker", name="Rural village", points=[[400, 90], [560, 70], [420, 330], [560, 340]], symbol="house"),
      dict(kind="marker", name="Capital city and main port", points=[[165, 205]], symbol="conflict"),
      dict(kind="arrow", name="Migration flow from an interior village to the capital", **{"from": [392, 96], "to": [188, 196]}),
      dict(kind="arrow", name="Migration flow from an interior village to the capital", **{"from": [552, 78], "to": [192, 190]}),
      dict(kind="arrow", name="Migration flow from an interior village to the capital", **{"from": [412, 324], "to": [188, 214]}),
      dict(kind="arrow", name="Migration flow from an interior village to the capital", **{"from": [552, 334], "to": [192, 222]})],
    legend=[dict(swatch="small", label="Coastal plain and river valley (fertile, well watered)"), dict(swatch="land", label="Dry interior"), dict(swatch="power", label="Mountains"),
            dict(swatch="conflict", label="Capital city and main port"), dict(swatch="baseN", label="City or town"), dict(swatch="house", label="Rural village"), dict(swatch="water", label="Ocean")],
    description="Map of Country V. The ocean is on the west. A fertile coastal plain runs along the coast, and a river valley crosses the country from the mountains in the east to the coast. The rest of the interior is dry. The capital city, the main port, sits on the coast where the river valley meets the ocean. The other cities and towns are on the coastal plain and in the river valley. Small villages are scattered across the dry interior. Arrows run from four interior villages to the capital.",
    note="Arrows show the largest migration flows from 2000 to 2020. During those years, the dry interior had repeated droughts, and the capital's port and new factories added many jobs.",
    source="Hypothetical map"),
  stem="Most of Country V's cities and towns are located on the coastal plain and in the river valley. Which of the following best explains this pattern?",
  options={
    "A": "The dry interior has been set aside as a protected national park.",
    "B": "The coast and valley have the coolest year-round temperatures in Country V.",
    "C": "The mountains block people in the interior from reaching other areas.",
    "D": "The coast and valley were the first areas where the land was surveyed.",
    "E": "The coast and valley have water, flat fertile land, and access to trade."},
  answer="E",
  rationales={
    "A": "Incorrect. The map shows no park, and people do live in small villages in the interior; the interior is sparsely settled because it is dry.",
    "B": "Incorrect. Nothing on the map shows that the lowlands are cooler, and mountains are usually cooler than lowlands.",
    "C": "Incorrect. The mountains lie along the eastern edge of the country; they do not separate the interior villages from the coast.",
    "D": "Incorrect. The order in which land was surveyed does not explain this distribution; the physical environment does.",
    "E": "Correct. Physical factors such as water bodies, landforms, and climate influence population distribution. The coast and the river valley provide water for people and irrigation, flat and fertile land, and easy transportation, so cities grew there, while the dry interior and the mountains remain sparsely settled."},
  explanation="People settle where life is easier: near water, on flat land with good soil, and where boats and roads make trade easy. In Country V that means the coast and the river valley. The dry interior and the mountains have far fewer people.")

q(id="U2-E22", n=22, set="mapV", topic="2.11", lo="IMP-2.D", skill="4.B", difficulty="easy",
  stem="The arrows on the map best illustrate which type of migration?",
  options={
    "A": "Internal, rural-to-urban migration",
    "B": "International, transnational migration",
    "C": "Seasonal transhumance",
    "D": "Urban-to-rural migration",
    "E": "Guest worker migration"},
  answer="A",
  rationales={
    "A": "Correct. The arrows begin at rural villages in the dry interior and end at the capital city, and none of them crosses Country V's borders. This is internal migration from rural to urban areas, one of the types of voluntary migration in the AP course framework.",
    "B": "Incorrect. The arrows do not cross an international border, so the map does not show international or transnational migration.",
    "C": "Incorrect. Transhumance is the seasonal movement of herders and livestock; the arrows show one-way moves from villages to a city.",
    "D": "Incorrect. The arrows point from rural villages toward the capital, the opposite of urban-to-rural migration.",
    "E": "Incorrect. Guest workers move to another country for temporary jobs; these migrants stay in their own country."},
  explanation="Follow the arrows: they start at small villages in the dry interior and end at the capital. They never leave Country V. Moving from the countryside to a city inside your own country = internal, rural-to-urban migration.")

q(id="U2-E23", n=23, set="mapV", topic="2.10", lo="IMP-2.C", skill="4.E", difficulty="medium",
  stem="Based on the map and its note, which combination of factors best explains the migration flows shown?",
  options={
    "A": "A political push factor in the interior and a cultural pull factor in the capital",
    "B": "An environmental push factor in the interior and an economic pull factor in the capital",
    "C": "An economic push factor in the capital and an environmental pull factor in the interior",
    "D": "An intervening opportunity in the interior and an intervening obstacle on the coast",
    "E": "A demographic pull factor in the interior and a political push factor in the capital city"},
  answer="B",
  rationales={
    "A": "Incorrect. The note describes droughts and new jobs, not war, persecution, or cultural ties.",
    "B": "Correct. Repeated droughts in the dry interior are an environmental push factor that makes farming harder, and new port and factory jobs in the capital are an economic pull factor. Together they explain the flows from interior villages to the capital.",
    "C": "Incorrect. This reverses the direction: push factors operate at the origin (the interior), and pull factors at the destination (the capital).",
    "D": "Incorrect. An intervening opportunity would cause migrants to stop partway, and nothing on the map shows an obstacle on the coast; the migrants reach the capital.",
    "E": "Incorrect. People are moving away from the interior, not toward it, and the capital is attracting migrants, not pushing them away."},
  explanation="Push = what makes people leave (drought in the interior: environmental). Pull = what draws them in (jobs at the port and factories: economic). Push factors are at the starting place; pull factors are at the destination.")

q(id="U2-E24", n=24, topic="2.12", lo="IMP-2.E", skill="5.B", difficulty="medium",
  stem="Which of the following best describes the effects of remittances at different scales in a country where remittances equal about one-fifth of its gross domestic product (GDP)?",
  options={
    "A": "They help individual households but have little effect on the national economy as a whole.",
    "B": "They strengthen the national economy but seldom reach individual families in rural villages.",
    "C": "They mainly benefit the destination countries where the migrants work and earn their wages.",
    "D": "Households use them for food, school, and housing, and nationally they are a major income source.",
    "E": "They mainly slow emigration, because families that receive the money no longer need to move."},
  answer="D",
  rationales={
    "A": "Incorrect. When remittances equal about one-fifth of GDP, they are a large part of the national economy, not a small one.",
    "B": "Incorrect. Remittances are sent directly to migrants' families, so they reach households first.",
    "C": "Incorrect. Remittances flow from destination countries back to migrants' home countries.",
    "D": "Correct. At the household and local scale, remittances pay for food, school fees, health care, and new homes. At the national scale, they bring in foreign currency and can make up a large share of GDP; in 2024, remittances equaled about one-quarter of GDP in Nepal and in Honduras.",
    "E": "Incorrect. Remittances often help pay the costs of moving and show families the rewards of working abroad, so they can encourage more emigration, not less."},
  explanation="Think at two scales. Family scale: the money buys food, pays for school, and builds houses. Country scale: when remittances equal one-fifth of everything the economy produces, the whole country depends on them. That also means a recession in the countries where migrants work can hurt the home country.")

q(id="U2-E25", n=25, topic="2.12", lo="IMP-2.E", skill="2.C", difficulty="hard",
  stem="For 30 years, many young adults from rural villages in Country H have migrated abroad for work. Which of the following is the most likely effect on those villages?",
  options={
    "A": "Village populations grow younger as migrants' children move back to run the family farms.",
    "B": "Villages gain more working-age adults than they lose, so farm labor becomes cheaper.",
    "C": "Villages are left with mostly older adults and children, and farms face labor shortages.",
    "D": "Villages develop sex ratios well above 100, because the migrants are mostly young men.",
    "E": "Villages see rising birth rates, because the people who remain are mostly young couples."},
  answer="C",
  rationales={
    "A": "Incorrect. Most migrants are young adults, and many do not return to farm, so the villages tend to grow older, not younger.",
    "B": "Incorrect. The villages lose working-age adults to emigration, which tends to create labor shortages and raise farm wages.",
    "C": "Correct. Migration is selective by age: most migrants are young adults. Their departure leaves sending villages with mostly older adults and children, labor shortages on farms, and in some cases abandoned fields, even as remittances help families pay for food and housing.",
    "D": "Incorrect. If more young men than young women leave, the villages are left with more women than men, a sex ratio below 100, not above it.",
    "E": "Incorrect. The people most likely to have children are the young adults who left, so birth rates in the villages tend to fall."},
  explanation="Most people who migrate for work are young adults. When they leave, the village is left with grandparents and children. There are fewer people to farm, so some fields may go unplanted, even though money sent home (remittances) helps families buy food and build houses.")
