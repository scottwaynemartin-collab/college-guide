# Unit 2 practice items P01-P21 (topics 2.1-2.6). Run via assemble.py (data.py names are preloaded).
P = []


def _n(v, d=0):
    return f"{v:,.{d}f}"


# ---------------- 2.1 Population Distribution (PSO-2.A, PSO-2.B, PSO-2.C) ----------------
P.append(dict(id="U2-P01", topic="2.1", lo="PSO-2.A", skill="2.A", difficulty="easy",
  stem="Large parts of northern Canada and northern Russia have very low population densities. Which physical factor best explains this pattern?",
  options={
    "A": "Frequent tropical storms that damage homes and destroy crops",
    "B": "A lack of rivers and lakes that can supply fresh water",
    "C": "Long, cold winters and short growing seasons that limit farming",
    "D": "Thick tropical rain forests that are difficult to clear for settlement",
    "E": "High temperatures and very little rainfall throughout the year"},
  answer="C",
  explanation="Northern Canada and northern Russia (Siberia) are very cold for most of the year. Winters are long, the ground can stay frozen, and the growing season is too short for most crops. Because it is hard to grow food there, few people live there. Climate is one of the main physical factors that shape where people live.",
  whyNot={
    "A": "Tropical storms hit warm places near the equator, not the far north.",
    "B": "These regions actually have many rivers and lakes. Water is not the problem; cold is.",
    "D": "Rain forests grow in warm, wet tropical places like the Amazon, not near the Arctic.",
    "E": "Hot and dry describes deserts like the Sahara. The far north is cold."},
  vocab=["population distribution", "population density", "physical factors"]))

_drows = []
for _c, _pop, _land, _ar, _a, _p in density_rows():
    _drows.append([_c, f"{_pop / 1e6:.1f} million", _n(_land), _n(_ar),
                   (f"{_a:.1f}" if _a < 10 else _n(_a)), _n(_p)])
P.append(dict(id="U2-P02", topic="2.1", lo="PSO-2.C", skill="3.D", difficulty="medium",
  stimulus=dict(type="table",
    title="POPULATION DENSITY IN FOUR COUNTRIES, 2024",
    columns=["Country", "Population", "Land area (sq km)", "Arable land (sq km)", "Arithmetic density (people per sq km of land)", "Physiological density (people per sq km of arable land)"],
    rows=_drows,
    description="Table comparing Egypt, the Netherlands, Japan, and Canada: population, land area, arable land, arithmetic density, and physiological density in 2024.",
    source="World Bank, World Development Indicators: population (SP.POP.TOTL), land area (AG.LND.TOTL.K2), and arable land (AG.LND.ARBL.HA), 2024 values, accessed November 8, 2026. Densities calculated from these figures; arable land converted from hectares (100 hectares = 1 sq km)."),
  stem="The data in the table best support which of the following conclusions?",
  options={
    "A": "Egypt has a lower arithmetic density than the Netherlands but more people per square kilometer of farmland.",
    "B": "Canada has the highest physiological density in the table because it has the largest total land area.",
    "C": "Japan's arithmetic density is higher than its physiological density because much of Japan is mountainous.",
    "D": "The Netherlands has the highest physiological density in the table because it has the highest arithmetic density.",
    "E": "Egypt and Canada have similar physiological densities because each has a small share of land that is arable."},
  answer="A",
  explanation="Arithmetic density divides people by ALL land. Physiological density divides people by only the land that can grow crops (arable land). Egypt's arithmetic density (117) is lower than the Netherlands' (534). But only about 3% of Egypt's land is arable. Most of it lies along the Nile River and its delta. So Egypt has about 3,560 people per square kilometer of farmland, about twice the Netherlands' 1,794. Physiological density shows pressure on farmland better than arithmetic density does.",
  whyNot={
    "B": "Canada has the LOWEST physiological density in the table (108). A huge land area spreads people out; it does not crowd them.",
    "C": "Physiological density can never be lower than arithmetic density, because arable land is just part of all land. Japan: 340 vs. 3,082.",
    "D": "The Netherlands has the highest arithmetic density (534), but its physiological density (1,794) is lower than Egypt's and Japan's.",
    "E": "Both have small shares of arable land, but Egypt has about 3,560 people per sq km of farmland and Canada about 108. Canada has far fewer people."},
  vocab=["arithmetic density", "physiological density", "arable land"]))

P.append(dict(id="U2-P03", topic="2.1", lo="PSO-2.C", skill="1.B", difficulty="hard",
  stem="Country X and Country Y have about the same physiological density. However, Country X's agricultural density is five times as high as Country Y's. Which of the following best explains this difference?",
  options={
    "A": "Country X has much more arable land per person than Country Y has.",
    "B": "Country Y has a much larger total land area than Country X has.",
    "C": "Country X imports most of its food, so a smaller share of its people need to farm.",
    "D": "A larger share of Country X's people work as farmers, likely with less machinery.",
    "E": "Country Y has more people living on each square kilometer of arable land."},
  answer="D",
  explanation="Physiological density = all people ÷ arable land. Agricultural density = farmers ÷ arable land. If both countries have the same number of people per square kilometer of farmland, but X has five times as many FARMERS per square kilometer of farmland, then a much bigger share of X's people must be farmers. That usually means farming in X uses more hand labor and less machinery. High agricultural density is common in less developed, more rural countries.",
  whyNot={
    "A": "More arable land per person would make X's physiological density LOWER, but the two countries' physiological densities are the same.",
    "B": "Total land area changes arithmetic density, not agricultural density.",
    "C": "Fewer farmers would make X's agricultural density lower, not higher.",
    "E": "People per square kilometer of arable land is physiological density, which the stem says is about the same in both countries."},
  vocab=["agricultural density", "physiological density", "arable land"]))

_tz = sum(p for _, _, p in PROV_Z); _az = sum(a for _, a, _ in PROV_Z)
_pd = {n: round(p / a) for n, a, p in PROV_Z}
P.append(dict(id="U2-P04", topic="2.1", lo="PSO-2.A", skill="5.B", difficulty="medium",
  stimulus=dict(type="schematicMap",
    title="ARITHMETIC POPULATION DENSITY BY PROVINCE, COUNTRY Z (HYPOTHETICAL)",
    canvas=dict(width=800, height=360),
    features=[
      dict(kind="land", name=f"Coastal Province: {_pd['Coastal Province']} people per sq km", polygon=[[96, 0], [250, 0], [250, 360], [92, 360], [70, 280], [88, 200], [64, 120], [84, 60]], labelAt=[172, 180]),
      dict(kind="land", name=f"River Valley Province: {_pd['River Valley Province']} people per sq km", polygon=[[250, 0], [450, 0], [450, 360], [250, 360]], labelAt=[350, 180]),
      dict(kind="land", name=f"Highland Province: {_pd['Highland Province']} people per sq km", polygon=[[450, 0], [620, 0], [620, 360], [450, 360]], labelAt=[535, 180], style="small"),
      dict(kind="land", name=f"Desert Province: {_pd['Desert Province']} people per sq km", polygon=[[620, 0], [800, 0], [800, 360], [620, 360]], labelAt=[710, 180], style="small")],
    legend=[dict(swatch="land", label="More than 100 people per sq km"), dict(swatch="small", label="Fewer than 100 people per sq km"), dict(swatch="water", label="Ocean")],
    description="Map of Country Z, which has four provinces in a row from the ocean on the west to the desert on the east. Each province is labeled with its arithmetic population density: Coastal Province 410, River Valley Province 180, Highland Province 35, and Desert Province 3 people per square kilometer.",
    note=f"Country Z as a whole: {_tz / 1e6:.1f} million people on {_n(_az)} sq km, an arithmetic density of about {round(_tz / _az)} people per sq km. Province areas: Coastal 20,000 sq km; River Valley 30,000 sq km; Highland 60,000 sq km; Desert 140,000 sq km. Map not drawn to scale.",
    source="Hypothetical data"),
  stem="A government report describes Country Z as having a density of about 64 people per square kilometer. Based on the map, which statement best explains why this national figure gives an incomplete picture of where people live?",
  options={
    "A": "The national figure divides people by arable land, so it overstates how crowded the four provinces are.",
    "B": "The national average hides that most people live in the two western provinces, while the desert is nearly empty.",
    "C": "Provincial densities should not be compared with a national density, because the two use different units of measure.",
    "D": "The Highland Province's density is closest to the national figure, so most of Country Z's people live there.",
    "E": "The national figure measures physiological density, while the map shows agricultural density by province."},
  answer="B",
  explanation="The national number (about 64 per sq km) is an average for the whole country. The map zooms in to a more local scale of analysis, the province, and shows that people are very unevenly spread. About 84% of the people live in the Coastal and River Valley provinces, which cover only 20% of the land, while the Desert Province has about 3 people per sq km. Changing the scale of analysis can reveal patterns that an average hides.",
  whyNot={
    "A": "Arithmetic density divides people by ALL land, not just arable land. The note says the national figure is an arithmetic density.",
    "C": "Both are people per square kilometer, so they can be compared. The problem is that one average hides big differences.",
    "D": "Highland's 35 is the closest number to 64, but most people live in the coastal and river-valley provinces (410 and 180 per sq km).",
    "E": "The map title and the note both say arithmetic density."},
  vocab=["arithmetic density", "scale of analysis", "population distribution"]))

# ---------------- 2.2 Consequences of Population Distribution (PSO-2.D) ----------------
P.append(dict(id="U2-P05", topic="2.2", lo="PSO-2.D", skill="2.C", difficulty="easy",
  stem="A sparsely populated ranching region is hundreds of kilometers from the nearest large city. Which outcome is most likely for the people who live there?",
  options={
    "A": "They live closer to hospitals than city residents do, because land for building is cheap.",
    "B": "They pay much higher land prices than city residents, because land in the region is scarce.",
    "C": "They rely on public buses and trains more than city residents do, because fewer families own cars.",
    "D": "They can choose among many specialized doctors, because clinics locate where land is cheapest.",
    "E": "They travel long distances for medical care, because few doctors and hospitals locate there."},
  answer="E",
  explanation="Hospitals, specialists, and many other services need enough patients or customers nearby to stay open. Where few people live spread over a big area, there are fewer clinics and hospitals. People often drive long distances, and some places rely on telemedicine or flying-doctor services. Population density affects how services such as medical care are provided.",
  whyNot={
    "A": "Low density spreads services far apart, so rural residents are usually FARTHER from hospitals.",
    "B": "Land is usually cheaper in sparsely populated areas, because fewer people want it.",
    "C": "Sparse areas have little public transit, so rural residents depend on cars more, not less.",
    "D": "Specialists locate where many patients live, mostly in cities, not where land is cheapest."},
  vocab=["population density", "provision of services", "rural"]))

P.append(dict(id="U2-P06", topic="2.2", lo="PSO-2.D", skill="1.D", difficulty="medium",
  stem="Which of the following scenarios best illustrates a population exceeding the carrying capacity of its environment?",
  options={
    "A": "Herders add animals to a dry pasture until the grass cannot regrow and the soil erodes.",
    "B": "A city builds apartment towers so that more people can live on the same amount of land.",
    "C": "Farmers build terraces on steep hillsides so they can grow rice without losing their soil.",
    "D": "A rural village loses half of its people as young adults move away to work in cities.",
    "E": "A coastal town builds a desalination plant to supply fresh water to its new residents."},
  answer="A",
  explanation="Carrying capacity is the largest population an environment can support without being damaged. When herders keep more animals than the grass can feed, the animals eat plants faster than they regrow. Bare soil blows or washes away, and later the land can support even fewer animals. That is a population (of people and their herds) going past the land's carrying capacity.",
  whyNot={
    "B": "Building up lets more people live in a small area. Density rises, but nothing shows the environment is being used up.",
    "C": "Terracing protects soil and helps land support more people. It works within the carrying capacity, not past it.",
    "D": "People moving away lowers pressure on the land. It does not show overuse.",
    "E": "Desalination is a technology that raises the number of people an area can supply with water."},
  vocab=["carrying capacity", "overgrazing", "population density"]))

P.append(dict(id="U2-P07", topic="2.2", lo="PSO-2.D", skill="2.B", difficulty="medium",
  stem="Mexico City is one of the largest metropolitan areas in the world and is built on the bed of a former lake. Which of the following best explains why parts of the city have been sinking?",
  options={
    "A": "Rising sea levels have flooded the low-lying neighborhoods closest to the coast.",
    "B": "Volcanic eruptions have caused the ground under older neighborhoods to collapse.",
    "C": "Pumping huge amounts of groundwater for residents has made the soil compact.",
    "D": "Rivers flowing through the city have carved deep channels that undercut its neighborhoods.",
    "E": "Coal mining under the city has left large empty tunnels beneath the streets."},
  answer="C",
  explanation="Millions of people need water, and much of Mexico City's water is pumped from an aquifer under the city. As the water is pulled out, the soft clay of the old lake bed dries out and packs down, so the ground sinks. Some areas sink tens of centimeters a year, which cracks pipes, buildings, and subway lines. This shows how a large, dense population can strain natural resources.",
  whyNot={
    "A": "Mexico City is far inland and more than 2,000 meters above sea level, so sea-level rise is not the cause.",
    "B": "The region has earthquakes and nearby volcanoes, but eruptions are not what makes the city slowly sink.",
    "D": "Most of the valley's old rivers now run through pipes. The ground sinks because water is pumped out of the clay below.",
    "E": "Coal mining is not the cause. The ground sinks because water is pumped out of the clay below."},
  vocab=["natural resources", "population density", "carrying capacity"]))

# ---------------- 2.3 Population Composition (PSO-2.E, PSO-2.F) ----------------
P.append(dict(id="U2-P08", topic="2.3", lo="PSO-2.E", skill="1.A", difficulty="easy",
  stem="A country reports a sex ratio of 105. What does this number mean?",
  options={
    "A": "There are 105 births each year for every 1,000 people.",
    "B": "There are 105 males for every 100 females.",
    "C": "There are 105 females for every 100 males.",
    "D": "There are 105 dependents for every 100 working-age people.",
    "E": "There are 105 infant deaths for every 1,000 live births."},
  answer="B",
  explanation="Sex ratio compares the number of males to the number of females. It is usually given as males per 100 females. A ratio of 105 means 105 males for every 100 females. Above 100 = more males; below 100 = more females.",
  whyNot={
    "A": "Births per 1,000 people is the crude birth rate.",
    "C": "That flips it. Sex ratio is males per 100 females.",
    "D": "Dependents per 100 working-age people is the dependency ratio.",
    "E": "Infant deaths per 1,000 live births is the infant mortality rate."},
  vocab=["sex ratio", "population composition"]))

P.append(dict(id="U2-P09", topic="2.3", lo="PSO-2.F", skill="3.E", difficulty="medium",
  stimulus=dict(type="pyramid",
    title="POPULATION PYRAMID, COUNTRY C, 2025 (HYPOTHETICAL DATA)",
    ageGroups=AGES, male=PYR_C_M, female=PYR_C_F,
    description="Population pyramid for Country C with 17 five-year age groups, from 0–4 at the bottom to 80+ at the top. Males are on the left and females on the right; bar length is the percent of the total population.",
    source="Hypothetical data"),
  stem="Based on the population pyramid, demand for which of the following will most likely grow the most in Country C over the next 15 years?",
  options={
    "A": "Elementary schools and children's clothing",
    "B": "Maternity wards and child-care centers",
    "C": "College dormitories and entry-level jobs",
    "D": "Nursing homes and health care for older adults",
    "E": "Starter apartments for young, newly married couples"},
  answer="D",
  explanation="The widest bars are people now aged 55–69. In 15 years they will be 70–84. Older people need more doctor visits, medicines, home care, and nursing homes, so demand for those will grow. The narrow base shows fewer children are being born, so demand for schools and baby products will not grow much. Population pyramids help predict markets for goods and services.",
  whyNot={
    "A": "The base is narrow, and each younger group is smaller, so the number of children is not growing.",
    "B": "Births are low (narrow base), so demand for maternity wards and child care is unlikely to rise much.",
    "C": "The children and teens who will reach college age and start work in the next 15 years are small groups.",
    "E": "Today's 5- to 19-year-olds will be young adults in 15 years, and those groups are small."},
  vocab=["population pyramid", "age structure", "aging population"]))

P.append(dict(id="U2-P10", topic="2.3", lo="PSO-2.E", skill="3.C", difficulty="hard",
  stimulus=dict(type="pyramid",
    title="POPULATION PYRAMID, COUNTRY G, 2025 (HYPOTHETICAL DATA)",
    ageGroups=AGES, male=PYR_G_M, female=PYR_G_F,
    description="Population pyramid for Country G with 17 five-year age groups, from 0–4 at the bottom to 80+ at the top. Males are on the left and females on the right; bar length is the percent of the total population.",
    source="Hypothetical data"),
  stem="Which of the following best explains the shape of Country G's population pyramid?",
  options={
    "A": "A pronatalist policy that raised birth rates sharply about 30 years ago",
    "B": "Sex-selective abortion that has favored male births since the 1990s",
    "C": "A large number of women leaving Country G to work in other countries",
    "D": "A war that killed many working-age women living in Country G",
    "E": "Large numbers of working-age men moving to Country G as guest workers"},
  answer="E",
  explanation="Look at ages 20–49. The male bars are much longer than the female bars AND much longer than the bars for boys. Without migration, an age group can only shrink as it gets older, so many people must have moved IN, mostly men of working age. A country that hires many foreign men as guest workers (for construction, oil, and service jobs) gets a pyramid like this. Some oil-rich Persian Gulf countries, such as Qatar and the United Arab Emirates, have pyramids with this shape.",
  whyNot={
    "A": "A baby boom would widen the bars for both sexes at the same ages, not mostly the male bars.",
    "B": "Sex-selective abortion would show up as extra boys in the youngest groups, but the bars for children here are balanced.",
    "C": "If many women left, the female bars would shrink, but the male bars would not become about four times as wide as the bars for boys.",
    "D": "A war would shrink some bars. It could not make the male bars wider than the bars for boys."},
  vocab=["population pyramid", "sex ratio", "guest worker"]))

P.append(dict(id="U2-P11", topic="2.3", lo="PSO-2.E", skill="5.C", difficulty="medium",
  stimulus=dict(type="table",
    title="AGE STRUCTURE OF A COUNTRY AND THREE OF ITS COUNTIES (HYPOTHETICAL DATA)",
    columns=["Place", "Under 15 (%)", "15–24 (%)", "25–64 (%)", "65 and older (%)"],
    rows=[[p] + [str(v) for v in vals] for p, vals in COUNTY_ROWS],
    description="Table showing the percent of the population in four age groups for a whole country and for three of its counties, U, R, and F.",
    source="Hypothetical data"),
  stem="Which of the following conclusions about population composition is best supported by the table?",
  options={
    "A": "Counties U and R differ sharply from the national age structure, suggesting migration sorts people by age.",
    "B": "County U has the highest birth rate in the table, because it has the largest share of people aged 15–24.",
    "C": "County R is likely to need more schools, because its population is older than the nation's.",
    "D": "The national age structure is a reliable guide to the age structure of each of the three counties in the table.",
    "E": "County F's age structure shows that it is losing population faster than Counties U and R."},
  answer="A",
  explanation="County U has 38% of its people aged 15–24, about three times the national 13%. That fits a college town, where students move in. County R has 42% aged 65 and older, about two and a half times the national 17%, which fits a place where retirees move. Zooming from the national scale to the county scale shows that migration can sort people by age into different places.",
  whyNot={
    "B": "The table shows age groups, not births. County U's share of children (11%) is lower than the nation's (18%).",
    "C": "Older places need more health care and senior services, not more schools. County R has only 10% under 15.",
    "D": "Counties U and R are very different from the national numbers, so the national pattern is a poor guide for them.",
    "E": "The table shows age structure at one point in time. It does not show whether any county is growing or shrinking."},
  vocab=["population composition", "age structure", "scale of analysis"]))

# ---------------- 2.4 Population Dynamics (IMP-2.A) ----------------
P.append(dict(id="U2-P12", topic="2.4", lo="IMP-2.A", skill="1.A", difficulty="easy",
  stem="Which of the following best describes the rate of natural increase (RNI)?",
  options={
    "A": "The number of children an average woman will have during her lifetime",
    "B": "The difference between immigrants and emigrants per 1,000 people",
    "C": "The crude birth rate minus the crude death rate, not counting migration",
    "D": "The number of years it will take a population to double in size",
    "E": "The number of deaths of children under age 1 per 1,000 live births"},
  answer="C",
  explanation="RNI = crude birth rate minus crude death rate. It is usually shown as a percent, so you divide by 10. Example: a birth rate of 30 per 1,000 and a death rate of 10 per 1,000 gives 20 per 1,000, or 2.0%. RNI leaves out migration, so a country's real growth can be higher or lower than its RNI.",
  whyNot={
    "A": "That is the total fertility rate (TFR).",
    "B": "That is the net migration rate. RNI leaves migration out.",
    "D": "That is the doubling time, which you can estimate from RNI (70 ÷ RNI).",
    "E": "That is the infant mortality rate (IMR)."},
  vocab=["rate of natural increase", "crude birth rate", "crude death rate"]))

P.append(dict(id="U2-P13", topic="2.4", lo="IMP-2.A", skill="3.C", difficulty="hard",
  stimulus=dict(type="table",
    title="BIRTHS, DEATHS, AND POPULATION GROWTH IN FIVE COUNTRIES, 2024",
    columns=["Country", "Crude birth rate (births per 1,000 people)", "Crude death rate (deaths per 1,000 people)", "Population growth rate (%)"],
    rows=[[c, f"{b:.1f}", f"{d:.1f}", f"{g:.1f}".replace("-", "−")] for c, (b, d, g) in WB_VITAL_2024.items()],
    description="Table of the 2024 crude birth rate, crude death rate, and population growth rate for Niger, India, Canada, Germany, and Japan.",
    source="World Bank, World Development Indicators: crude birth rate (SP.DYN.CBRT.IN), crude death rate (SP.DYN.CDRT.IN), and population growth (SP.POP.GROW), 2024 values, accessed November 8, 2026."),
  stem="According to the table, which country's population grew in 2024 even though it had more deaths than births, and what best explains that growth?",
  options={
    "A": "Japan, because more people moved into Japan than moved out",
    "B": "Germany, because more people moved into Germany than moved out",
    "C": "Canada, because its birth rate was much higher than its death rate",
    "D": "Germany, because its death rate fell below its birth rate during the year",
    "E": "Niger, because it had the highest rate of natural increase in the table"},
  answer="B",
  explanation="Germany's death rate (12.1) was higher than its birth rate (8.1), so its rate of natural increase was negative: (8.1 − 12.1) ÷ 10 = −0.4%. Yet its population grew 0.3%. The only other way to add people is migration, so more people moved into Germany than moved out. Population change = natural increase + net migration.",
  whyNot={
    "A": "Japan also had more deaths than births, but the table shows its population shrank (−0.4%).",
    "C": "Canada's birth rate (8.9) was only a little higher than its death rate (7.9), an RNI of 0.1%. Its 3.0% growth came mostly from migration, not births.",
    "D": "The table shows Germany's death rate (12.1) was higher than its birth rate (8.1).",
    "E": "Niger had far more births than deaths, so it does not fit the question."},
  vocab=["rate of natural increase", "net migration", "crude death rate"]))

P.append(dict(id="U2-P14", topic="2.4", lo="IMP-2.A", skill="1.D", difficulty="medium",
  stem=f"Country Q has a crude birth rate of {P14['cbr']} per 1,000 and a crude death rate of {P14['cdr']} per 1,000. Assuming no migration and no change in these rates, about how long will it take Country Q's population to double?",
  options={
    "A": "About 3 years",
    "B": "About 10 years",
    "C": "About 23 years",
    "D": "About 29 years",
    "E": "About 168 years"},
  answer="D",
  explanation="Step 1: RNI = (31 − 7) ÷ 10 = 2.4%. Step 2: Use the rule of 70: 70 ÷ 2.4 ≈ 29 years. A population growing 2.4% a year doubles in about 29 years.",
  whyNot={
    "A": "You divided 70 by 24. First change 24 per 1,000 into a percent: 2.4%.",
    "B": "You used only the death rate (70 ÷ 7). Use birth rate minus death rate.",
    "C": "You used only the birth rate (70 ÷ 3.1). Subtract the death rate first.",
    "E": "You multiplied 70 by 2.4. Divide instead: 70 ÷ 2.4."},
  vocab=["doubling time", "rate of natural increase", "rule of 70"]))

P.append(dict(id="U2-P15", topic="2.4", lo="IMP-2.A", skill="2.B", difficulty="medium",
  stem="In many rural farming areas of lower-income countries, families tend to have more children than families in the same countries' cities. Which of the following best explains this pattern?",
  options={
    "A": "Rural areas usually have more hospitals, so more babies survive to adulthood.",
    "B": "Rural families usually have higher incomes, so they can afford larger families.",
    "C": "Rural areas usually have more schools, so children are cheaper to educate.",
    "D": "Governments usually pay rural families more than city families for each child.",
    "E": "Rural families often rely on children for farm work and for care in old age."},
  answer="E",
  explanation="On a farm, children can help plant, herd animals, and carry water, so each child adds a worker. Where there are few pensions, grown children also care for their parents when they are old. In cities, children cost more (rent, school fees) and add less income. Economic factors like these help explain differences in fertility.",
  whyNot={
    "A": "Rural areas usually have FEWER hospitals and doctors than cities.",
    "B": "Rural incomes are usually LOWER than city incomes.",
    "C": "Cities usually have more schools. And school costs tend to shrink families, not grow them.",
    "D": "Payments for having children are usually national programs. They do not explain the rural-urban gap."},
  vocab=["total fertility rate", "economic factors", "rural"]))

P.append(dict(id="U2-P16", topic="2.4", lo="IMP-2.A", skill="1.B", difficulty="medium",
  stem="Geographers often use the infant mortality rate (IMR) as an indicator of a country's overall health and living conditions. Which of the following best explains why?",
  options={
    "A": "Whether infants survive depends on clean water, nutrition, and medical care.",
    "B": "Infants make up the largest share of the population in most countries.",
    "C": "Infant deaths are the main reason that a population's median age rises.",
    "D": "A high IMR means a country's population is aging and its birth rate is falling.",
    "E": "The IMR includes deaths of adults as well as infants, so it describes the whole population."},
  answer="A",
  explanation="Babies are very fragile. Whether they live to age 1 depends on things like clean water, enough food for mothers and babies, vaccines, and doctors or nurses at birth. So a low IMR usually means good health care and living conditions, and a high IMR usually means those are missing. IMR = deaths of babies under age 1 per 1,000 live births.",
  whyNot={
    "B": "Babies under age 1 are a small share of any population.",
    "C": "Median age rises mainly because birth rates fall and people live longer.",
    "D": "A high IMR is common where birth rates are high and the population is young.",
    "E": "The IMR counts only deaths of babies under age 1. The crude death rate counts deaths at all ages."},
  vocab=["infant mortality rate", "crude death rate"]))

# ---------------- 2.5 The Demographic Transition Model (IMP-2.B) ----------------
P.append(dict(id="U2-P17", topic="2.5", lo="IMP-2.B", skill="1.A", difficulty="easy",
  stem="Which of the following best describes what happens during Stage 2 of the demographic transition model?",
  options={
    "A": "Birth and death rates are both high, so the population grows slowly.",
    "B": "Death rates fall sharply while birth rates stay high, so the population grows rapidly.",
    "C": "Birth rates fall sharply while death rates stay low, so population growth slows.",
    "D": "Birth and death rates are both low, so the population grows slowly or stays stable.",
    "E": "Birth rates drop below death rates, so the population begins to shrink."},
  answer="B",
  explanation="In Stage 2, better food supplies, clean water, and basic medicine help more people survive, so the death rate drops. Birth rates stay high because families have not yet changed how many children they have. The big gap between births and deaths makes the population grow fast. Some countries, such as Niger, still have Stage 2 patterns today.",
  whyNot={
    "A": "That is Stage 1.",
    "C": "That is Stage 3.",
    "D": "That is Stage 4.",
    "E": "That is Stage 5, which some geographers add to the model."},
  vocab=["demographic transition model", "crude birth rate", "crude death rate"]))

P.append(dict(id="U2-P18", topic="2.5", lo="IMP-2.B", skill="3.C", difficulty="medium",
  stimulus=dict(type="line",
    title="CRUDE BIRTH AND DEATH RATES, COUNTRY K, 1900–2020 (HYPOTHETICAL DATA)",
    xLabel="Year", yLabel="Rate per 1,000 people",
    categories=DTM_K_YEARS,
    series=[dict(name="Crude birth rate", values=DTM_K_CBR), dict(name="Crude death rate", values=DTM_K_CDR)],
    yMax=50,
    description="Line graph of Country K's crude birth rate and crude death rate, per 1,000 people, every 20 years from 1900 to 2020.",
    source="Hypothetical data"),
  stem="Which of the following most likely explains the change in Country K's crude birth rate between 1960 and 2020?",
  options={
    "A": "An increase in infant deaths made parents decide to have fewer children.",
    "B": "A government policy began paying families a bonus for each new child.",
    "C": "Many workers left factory jobs in growing cities and returned to farming villages.",
    "D": "Cities grew, more girls stayed in school, and contraception became easier to get.",
    "E": "A disease outbreak killed many adults of childbearing age in Country K."},
  answer="D",
  explanation="Between 1960 and 2020 the birth rate fell from 44 to 19 per 1,000. That is Stage 3 of the demographic transition. In Stage 3, more people move to cities where children cost more, girls and women get more education and jobs, and family planning is easier to get, so families choose to have fewer children.",
  whyNot={
    "A": "The death rate was falling in these years (18 to 7), so infant deaths were most likely falling, not rising.",
    "B": "A bonus for having children is a pronatalist policy. It would push the birth rate up, not down.",
    "C": "Moving from cities back to farms usually raises birth rates, because children are more useful on farms.",
    "E": "The death rate kept falling in these years, so the graph does not show a deadly outbreak."},
  vocab=["demographic transition model", "Stage 3", "crude birth rate"]))

P.append(dict(id="U2-P19", topic="2.5", lo="IMP-2.B", skill="1.B", difficulty="easy",
  stem="According to the epidemiological transition model, as a country develops, the leading causes of death shift in which way?",
  options={
    "A": "From heart disease and cancer to infectious diseases such as cholera and measles",
    "B": "From accidents and violence to diseases spread by mosquitoes",
    "C": "From infectious and parasitic diseases to chronic diseases such as heart disease",
    "D": "From diseases of old age to diseases that mainly affect infants",
    "E": "From diseases spread by dirty water to diseases spread by spoiled or undercooked food"},
  answer="C",
  explanation="In the early stages, most people die young from infections like cholera, measles, and tuberculosis, and from famine. As clean water, vaccines, and medicine spread, those deaths drop. People live longer, so more of them die later in life from chronic (degenerative) diseases like heart disease, cancer, and stroke. The epidemiological transition explains why death rates fall in the demographic transition.",
  whyNot={
    "A": "That is backward. Infectious diseases were the leading killers first.",
    "B": "Mosquito-borne diseases like malaria are infectious diseases, which decline as countries develop.",
    "D": "As countries develop, fewer infants die, and deaths shift toward old age.",
    "E": "Both of these are infectious diseases. The model's shift is from infectious diseases to chronic ones."},
  vocab=["epidemiological transition", "infectious disease", "chronic disease"]))

P.append(dict(id="U2-P20", topic="2.5", lo="IMP-2.B", skill="1.E", difficulty="hard",
  stem="Which of the following is a limitation of the demographic transition model when it is used to predict population change in lower-income countries today?",
  options={
    "A": "It leaves out birth rates, so it is unable to show why a country's growth speeds up or slows down.",
    "B": "It describes how individual cities grow, so it does not apply to a whole country's population.",
    "C": "It assumes that countries move backward from Stage 4 to Stage 1 as they develop and industrialize.",
    "D": "It counts migration as part of growth, so it overstates growth in countries that send many emigrants.",
    "E": "It is based on Europe's past, so it may not fit places where imported medicines cut death rates quickly."},
  answer="E",
  explanation="The DTM was built from the history of Europe and North America, where death rates fell slowly over many decades as farming, industry, and sanitation improved. In many lower-income countries in the 1900s, vaccines and antibiotics from abroad cut death rates within a few decades, often before much industry developed. Birth rates also fall at different speeds because of culture and government policy. So the model may not predict when or how fast these countries move through the stages.",
  whyNot={
    "A": "Birth rates are one of the two main lines in the model.",
    "B": "The DTM describes the population of a country, not how individual cities grow.",
    "C": "Countries are expected to move forward from Stage 1 toward Stage 4, not backward.",
    "D": "The DTM uses only births and deaths. Leaving migration out is actually another one of its limits."},
  vocab=["demographic transition model", "limitations of models"]))

# ---------------- 2.6 Malthusian Theory (IMP-2.B) ----------------
P.append(dict(id="U2-P21", topic="2.6", lo="IMP-2.B", skill="1.A", difficulty="easy",
  stem="In 1798, Thomas Malthus predicted that famine and other disasters would eventually limit population growth. Which reasoning was the basis of his prediction?",
  options={
    "A": "Population tends to grow geometrically, while food supply grows only arithmetically.",
    "B": "Food supply tends to grow geometrically, while population grows only arithmetically.",
    "C": "Birth rates fall as countries industrialize, so populations will soon begin to shrink.",
    "D": "Population growth leads farmers to adopt new methods that raise food production.",
    "E": "Migration to cities will leave too few farmers in the countryside to grow enough food."},
  answer="A",
  explanation="Malthus said population grows geometrically (1, 2, 4, 8, 16…), because each generation can double. Food supply grows arithmetically (1, 2, 3, 4, 5…), adding about the same amount each time. Sooner or later, people would outnumber the food. He thought 'positive checks' like famine, disease, and war would then raise death rates, unless people married later and had fewer children.",
  whyNot={
    "B": "That flips Malthus's idea. He said population, not food, grows faster.",
    "C": "That describes later stages of the demographic transition model, an idea developed long after Malthus.",
    "D": "That is Esther Boserup's argument, which criticizes Malthus.",
    "E": "Malthus focused on population growing faster than food, not on migration to cities."},
  vocab=["Malthusian theory", "geometric growth", "arithmetic growth"]))
