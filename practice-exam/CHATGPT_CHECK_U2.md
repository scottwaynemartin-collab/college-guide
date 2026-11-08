# AP Human Geography Unit 2 practice-exam bank: full export for review (v2026-11-08b)

## What this is

- **Unit:** Population and Migration Patterns and Processes (Topics 2.1–2.12). The exam weighting is 12–17% of the AP Exam multiple-choice section.
- **Where it is used:** the "AP Practice Exam" page of a teacher's GeoArcade study site. The page is a Google Sites full-page embed used by 9th-grade AP Human Geography students.
- **Practice:** 42 untimed questions, filtered by topic. After each answer the student sees `explanation`, written at about a 6th-grade level, then one `whyNot` line for each wrong option.
- **Exam:** 25 questions in 25 minutes, 5 options each, with 10 stimulus-based questions in 4 sets. The review screen shows `rationales` (a College Board-style note on every option) and the student `explanation`.
- **Data:** stimuli labeled "Hypothetical" are invented on purpose. P02, P13 and P40 use real World Bank data, and E07, E14 and E24 quote real figures. SOURCES.md, at the end of this file, lists every real figure and how it was checked.

## How each stimulus type is displayed

- **`table`:** an HTML table. The header row comes from `columns`, the first cell of each row is a row header, the title is above and `source` is below. A table's `description` is not shown.
- **`bar`:** a vertical bar chart in SVG with y-axis gridlines and ticks up to `yMax`, the `yLabel` on the axis, category labels under the bars, and the value printed above each bar. Every Unit 2 bar chart has 1 series. `text` is shown under the chart; `description` is not shown. Screen readers get a hidden data table.
- **`line`:** a multi-series line chart in SVG with gridlines and ticks up to `yMax`. Categories are evenly spaced on the x-axis. Each series has its own marker and dash pattern: crude birth rate or population is a blue solid line with circles, and crude death rate or food production is an orange dashed line with squares. A legend sits above the chart. Point values are not printed; screen readers get them in the SVG description and a hidden table. `description` is shown as a paragraph under the chart.
- **`pyramid`:** a back-to-back horizontal bar chart. Age groups run from youngest at the bottom to oldest at the top, with labels in the center. Male bars (blue) run left and female bars (orange, hatched) run right. The x-axis is "Percent of total population", with ticks on both sides. Bar values are not printed; screen readers get them in a hidden table. `description` is shown as a paragraph under the chart.
- **`schematicMap`:** an SVG map on a `canvas`. The whole background is ocean-blue water.
  - `land` polygons are filled in one of three tints: default beige, `small` cream, or `power` lavender. Their `name` is drawn as a label at `labelAt`.
  - `island` features are drawn as labeled circles and are used as settlements in P37.
  - `marker` features are drawn as small symbols: `baseN` is a purple square, `house` is a dark house icon, and `conflict` is a red starburst, used here for the capital.
  - `arrow` features are dark arrows.
  - The legend comes from `legend`. `description` and `note` are shown as paragraphs under the map.
- **`set`:** exam questions that share a stimulus carry the same `set` id. The stimulus is stored on the first question and stays pinned beside each question in the set. Practice stimuli are self-contained.

## unit2.json (complete)

```json
{
 "unit": 2,
 "title": "Population and Migration Patterns and Processes",
 "examWeighting": "12–17% of the AP Exam multiple-choice section",
 "version": "2026-11-08b",
 "calibration": "Modeled on the format of the College Board 2020 AP Human Geography Practice Exam and the Course and Exam Description (5 answer choices, set-based stimulus questions, skills 1–5). All questions, stimuli, and data are original or compiled from public facts; no College Board items are reproduced.",
 "checked": "Nov 8, 2026: automated checks in u2/assemble.py (answer balance and runs, option-length tells, absolute-word tells, field completeness, set structure, stimulus fields, LO-to-topic match); every rate, ratio, density, and doubling-time answer recomputed by script from the stimulus data (u2/data.py); real-data tables (P02, P13, P40) and the figures quoted in E07, E14, and E24 pulled from the World Bank WDI API (see u2/SOURCES.md). Independent Claude checker agent (v2026-11-08a): blind key agreement 67/67, all WDI figures and every computed answer re-verified by a separate script. Fixes applied in v2026-11-08b: visible stimulus descriptions made neutral (P09, P10, P18, P22, E03, E10, E16); E10 rationale B; E21 city marker symbol matches legend; E21 and P04 maps no longer drawn as islands; E16 last point moved to 2025 so the x-axis spacing is even; P11 key rewritten to require the table; P05 C/D and P07 D distractors replaced; P35 explanation tied to intervening obstacles (IMP-2.C.2); E25 skill 5.B to 2.C; wording in P02, P04, P05, E09, E14.",
 "schemaNotes": {
  "stimulus.type": "table | bar | districtMap | schematicMap | rings | pyramid | line (rings = von Thünen-style concentric ring diagram: center, rings[].label, outer, description; pyramid = back-to-back population pyramid: ageGroups youngest first, male[] and female[] as percent of the TOTAL population, description, source; line = multi-series line chart: categories (x labels), series[].name/values, xLabel, yLabel, optional yMax, description, source)",
  "practice[].explanation": "6th-grade-level reason the answer is right (show this first)",
  "practice[].whyNot": "one line per wrong option",
  "exam.questions[].rationales": "College Board-style note on every option A–E",
  "exam.questions[].explanation": "6th-grade-level version for the review screen",
  "set": "questions sharing a stimulus carry the same set id; the stimulus object lives on the first question of the set (exam only; each practice stimulus is self-contained because practice can be filtered by topic)"
 },
 "topics": [
  {
   "id": "2.1",
   "name": "Population Distribution",
   "lo": "PSO-2.A, PSO-2.B, PSO-2.C"
  },
  {
   "id": "2.2",
   "name": "Consequences of Population Distribution",
   "lo": "PSO-2.D"
  },
  {
   "id": "2.3",
   "name": "Population Composition",
   "lo": "PSO-2.E, PSO-2.F"
  },
  {
   "id": "2.4",
   "name": "Population Dynamics",
   "lo": "IMP-2.A"
  },
  {
   "id": "2.5",
   "name": "The Demographic Transition Model",
   "lo": "IMP-2.B"
  },
  {
   "id": "2.6",
   "name": "Malthusian Theory",
   "lo": "IMP-2.B"
  },
  {
   "id": "2.7",
   "name": "Population Policies",
   "lo": "SPS-2.A"
  },
  {
   "id": "2.8",
   "name": "Women and Demographic Change",
   "lo": "SPS-2.B"
  },
  {
   "id": "2.9",
   "name": "Aging Populations",
   "lo": "SPS-2.C"
  },
  {
   "id": "2.10",
   "name": "Causes of Migration",
   "lo": "IMP-2.C"
  },
  {
   "id": "2.11",
   "name": "Forced and Voluntary Migration",
   "lo": "IMP-2.D"
  },
  {
   "id": "2.12",
   "name": "Effects of Migration",
   "lo": "IMP-2.E"
  }
 ],
 "practice": [
  {
   "id": "U2-P01",
   "topic": "2.1",
   "lo": "PSO-2.A",
   "skill": "2.A",
   "difficulty": "easy",
   "stem": "Large parts of northern Canada and northern Russia have very low population densities. Which physical factor best explains this pattern?",
   "options": {
    "A": "Frequent tropical storms that damage homes and destroy crops",
    "B": "A lack of rivers and lakes that can supply fresh water",
    "C": "Long, cold winters and short growing seasons that limit farming",
    "D": "Thick tropical rain forests that are difficult to clear for settlement",
    "E": "High temperatures and very little rainfall throughout the year"
   },
   "answer": "C",
   "explanation": "Northern Canada and northern Russia (Siberia) are very cold for most of the year. Winters are long, the ground can stay frozen, and the growing season is too short for most crops. Because it is hard to grow food there, few people live there. Climate is one of the main physical factors that shape where people live.",
   "whyNot": {
    "A": "Tropical storms hit warm places near the equator, not the far north.",
    "B": "These regions actually have many rivers and lakes. Water is not the problem; cold is.",
    "D": "Rain forests grow in warm, wet tropical places like the Amazon, not near the Arctic.",
    "E": "Hot and dry describes deserts like the Sahara. The far north is cold."
   },
   "vocab": [
    "population distribution",
    "population density",
    "physical factors"
   ]
  },
  {
   "id": "U2-P02",
   "topic": "2.1",
   "lo": "PSO-2.C",
   "skill": "3.D",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "POPULATION DENSITY IN FOUR COUNTRIES, 2024",
    "columns": [
     "Country",
     "Population",
     "Land area (sq km)",
     "Arable land (sq km)",
     "Arithmetic density (people per sq km of land)",
     "Physiological density (people per sq km of arable land)"
    ],
    "rows": [
     [
      "Egypt",
      "116.5 million",
      "995,450",
      "32,740",
      "117",
      "3,560"
     ],
     [
      "Netherlands",
      "18.0 million",
      "33,670",
      "10,030",
      "534",
      "1,794"
     ],
     [
      "Japan",
      "124.0 million",
      "364,500",
      "40,230",
      "340",
      "3,082"
     ],
     [
      "Canada",
      "41.3 million",
      "8,788,700",
      "380,640",
      "4.7",
      "108"
     ]
    ],
    "description": "Table comparing Egypt, the Netherlands, Japan, and Canada: population, land area, arable land, arithmetic density, and physiological density in 2024.",
    "source": "World Bank, World Development Indicators: population (SP.POP.TOTL), land area (AG.LND.TOTL.K2), and arable land (AG.LND.ARBL.HA), 2024 values, accessed November 8, 2026. Densities calculated from these figures; arable land converted from hectares (100 hectares = 1 sq km)."
   },
   "stem": "The data in the table best support which of the following conclusions?",
   "options": {
    "A": "Egypt has a lower arithmetic density than the Netherlands but more people per square kilometer of farmland.",
    "B": "Canada has the highest physiological density in the table because it has the largest total land area.",
    "C": "Japan's arithmetic density is higher than its physiological density because much of Japan is mountainous.",
    "D": "The Netherlands has the highest physiological density in the table because it has the highest arithmetic density.",
    "E": "Egypt and Canada have similar physiological densities because each has a small share of land that is arable."
   },
   "answer": "A",
   "explanation": "Arithmetic density divides people by ALL land. Physiological density divides people by only the land that can grow crops (arable land). Egypt's arithmetic density (117) is lower than the Netherlands' (534). But only about 3% of Egypt's land is arable. Most of it lies along the Nile River and its delta. So Egypt has about 3,560 people per square kilometer of farmland, about twice the Netherlands' 1,794. Physiological density shows pressure on farmland better than arithmetic density does.",
   "whyNot": {
    "B": "Canada has the LOWEST physiological density in the table (108). A huge land area spreads people out; it does not crowd them.",
    "C": "Physiological density can never be lower than arithmetic density, because arable land is just part of all land. Japan: 340 vs. 3,082.",
    "D": "The Netherlands has the highest arithmetic density (534), but its physiological density (1,794) is lower than Egypt's and Japan's.",
    "E": "Both have small shares of arable land, but Egypt has about 3,560 people per sq km of farmland and Canada about 108. Canada has far fewer people."
   },
   "vocab": [
    "arithmetic density",
    "physiological density",
    "arable land"
   ]
  },
  {
   "id": "U2-P03",
   "topic": "2.1",
   "lo": "PSO-2.C",
   "skill": "1.B",
   "difficulty": "hard",
   "stem": "Country X and Country Y have about the same physiological density. However, Country X's agricultural density is five times as high as Country Y's. Which of the following best explains this difference?",
   "options": {
    "A": "Country X has much more arable land per person than Country Y has.",
    "B": "Country Y has a much larger total land area than Country X has.",
    "C": "Country X imports most of its food, so a smaller share of its people need to farm.",
    "D": "A larger share of Country X's people work as farmers, likely with less machinery.",
    "E": "Country Y has more people living on each square kilometer of arable land."
   },
   "answer": "D",
   "explanation": "Physiological density = all people ÷ arable land. Agricultural density = farmers ÷ arable land. If both countries have the same number of people per square kilometer of farmland, but X has five times as many FARMERS per square kilometer of farmland, then a much bigger share of X's people must be farmers. That usually means farming in X uses more hand labor and less machinery. High agricultural density is common in less developed, more rural countries.",
   "whyNot": {
    "A": "More arable land per person would make X's physiological density LOWER, but the two countries' physiological densities are the same.",
    "B": "Total land area changes arithmetic density, not agricultural density.",
    "C": "Fewer farmers would make X's agricultural density lower, not higher.",
    "E": "People per square kilometer of arable land is physiological density, which the stem says is about the same in both countries."
   },
   "vocab": [
    "agricultural density",
    "physiological density",
    "arable land"
   ]
  },
  {
   "id": "U2-P04",
   "topic": "2.1",
   "lo": "PSO-2.A",
   "skill": "5.B",
   "difficulty": "medium",
   "stimulus": {
    "type": "schematicMap",
    "title": "ARITHMETIC POPULATION DENSITY BY PROVINCE, COUNTRY Z (HYPOTHETICAL)",
    "canvas": {
     "width": 800,
     "height": 360
    },
    "features": [
     {
      "kind": "land",
      "name": "Coastal Province: 410 people per sq km",
      "polygon": [
       [
        96,
        0
       ],
       [
        230,
        0
       ],
       [
        230,
        360
       ],
       [
        92,
        360
       ],
       [
        70,
        280
       ],
       [
        88,
        200
       ],
       [
        64,
        120
       ],
       [
        84,
        60
       ]
      ],
      "labelAt": [
       160,
       180
      ],
      "style": "power"
     },
     {
      "kind": "land",
      "name": "River Valley Province: 180 people per sq km",
      "polygon": [
       [
        230,
        0
       ],
       [
        390,
        0
       ],
       [
        390,
        360
       ],
       [
        230,
        360
       ]
      ],
      "labelAt": [
       310,
       180
      ],
      "style": "power"
     },
     {
      "kind": "land",
      "name": "Highland Province: 35 people per sq km",
      "polygon": [
       [
        390,
        0
       ],
       [
        570,
        0
       ],
       [
        570,
        360
       ],
       [
        390,
        360
       ]
      ],
      "labelAt": [
       480,
       180
      ]
     },
     {
      "kind": "land",
      "name": "Desert Province: 3 people per sq km",
      "polygon": [
       [
        570,
        0
       ],
       [
        800,
        0
       ],
       [
        800,
        360
       ],
       [
        570,
        360
       ]
      ],
      "labelAt": [
       675,
       180
      ],
      "style": "small"
     }
    ],
    "legend": [
     {
      "swatch": "power",
      "label": "More than 100 people per sq km"
     },
     {
      "swatch": "land",
      "label": "10 to 100 people per sq km"
     },
     {
      "swatch": "small",
      "label": "Fewer than 10 people per sq km"
     },
     {
      "swatch": "water",
      "label": "Ocean"
     }
    ],
    "description": "Map of Country Z, which has four provinces in a row from the ocean on the west to the desert on the east. Each province is labeled with its arithmetic population density: Coastal Province 410, River Valley Province 180, Highland Province 35, and Desert Province 3 people per square kilometer.",
    "note": "Country Z as a whole: 16.1 million people on 250,000 sq km, an arithmetic density of about 64 people per sq km. Province areas: Coastal 20,000 sq km; River Valley 30,000 sq km; Highland 60,000 sq km; Desert 140,000 sq km. Map not drawn to scale.",
    "source": "Hypothetical data"
   },
   "stem": "A government report describes Country Z as having a density of about 64 people per square kilometer. Based on the map, which statement best explains why this national figure gives an incomplete picture of where people live?",
   "options": {
    "A": "The national figure divides people by arable land, so it overstates how crowded the four provinces are.",
    "B": "The national average hides that most people live in the two western provinces, while the desert is nearly empty.",
    "C": "Provincial densities should not be compared with a national density, because the two use different units of measure.",
    "D": "The Highland Province's density is closest to the national figure, so most of Country Z's people live there.",
    "E": "The national figure measures physiological density, while the map shows agricultural density by province."
   },
   "answer": "B",
   "explanation": "The national number (about 64 per sq km) is an average for the whole country. The map zooms in to a more local scale of analysis, the province, and shows that people are very unevenly spread. About 84% of the people live in the Coastal and River Valley provinces, which cover only 20% of the land, while the Desert Province has about 3 people per sq km. Changing the scale of analysis can reveal patterns that an average hides.",
   "whyNot": {
    "A": "Arithmetic density divides people by ALL land, not just arable land. The note says the national figure is an arithmetic density.",
    "C": "Both are people per square kilometer, so they can be compared. The problem is that one average hides big differences.",
    "D": "Highland's 35 is the closest number to 64, but most people live in the coastal and river-valley provinces (410 and 180 per sq km).",
    "E": "The map title and the note both say arithmetic density."
   },
   "vocab": [
    "arithmetic density",
    "scale of analysis",
    "population distribution"
   ]
  },
  {
   "id": "U2-P05",
   "topic": "2.2",
   "lo": "PSO-2.D",
   "skill": "2.C",
   "difficulty": "easy",
   "stem": "A sparsely populated ranching region is hundreds of kilometers from the nearest large city. Which outcome is most likely for the people who live there?",
   "options": {
    "A": "They live closer to hospitals than city residents do, because land for building is cheap.",
    "B": "They pay much higher land prices than city residents, because land in the region is scarce.",
    "C": "They rely on public buses and trains more than city residents do, because fewer families own cars.",
    "D": "They can choose among many specialized doctors, because clinics locate where land is cheapest.",
    "E": "They travel long distances for medical care, because few doctors and hospitals locate there."
   },
   "answer": "E",
   "explanation": "Hospitals, specialists, and many other services need enough patients or customers nearby to stay open. Where few people live spread over a big area, there are fewer clinics and hospitals. People often drive long distances, and some places rely on telemedicine or flying-doctor services. Population density affects how services such as medical care are provided.",
   "whyNot": {
    "A": "Low density spreads services far apart, so rural residents are usually FARTHER from hospitals.",
    "B": "Land is usually cheaper in sparsely populated areas, because fewer people want it.",
    "C": "Sparse areas have little public transit, so rural residents depend on cars more, not less.",
    "D": "Specialists locate where many patients live, mostly in cities, not where land is cheapest."
   },
   "vocab": [
    "population density",
    "provision of services",
    "rural"
   ]
  },
  {
   "id": "U2-P06",
   "topic": "2.2",
   "lo": "PSO-2.D",
   "skill": "1.D",
   "difficulty": "medium",
   "stem": "Which of the following scenarios best illustrates a population exceeding the carrying capacity of its environment?",
   "options": {
    "A": "Herders add animals to a dry pasture until the grass cannot regrow and the soil erodes.",
    "B": "A city builds apartment towers so that more people can live on the same amount of land.",
    "C": "Farmers build terraces on steep hillsides so they can grow rice without losing their soil.",
    "D": "A rural village loses half of its people as young adults move away to work in cities.",
    "E": "A coastal town builds a desalination plant to supply fresh water to its new residents."
   },
   "answer": "A",
   "explanation": "Carrying capacity is the largest population an environment can support without being damaged. When herders keep more animals than the grass can feed, the animals eat plants faster than they regrow. Bare soil blows or washes away, and later the land can support even fewer animals. That is a population (of people and their herds) going past the land's carrying capacity.",
   "whyNot": {
    "B": "Building up lets more people live in a small area. Density rises, but nothing shows the environment is being used up.",
    "C": "Terracing protects soil and helps land support more people. It works within the carrying capacity, not past it.",
    "D": "People moving away lowers pressure on the land. It does not show overuse.",
    "E": "Desalination is a technology that raises the number of people an area can supply with water."
   },
   "vocab": [
    "carrying capacity",
    "overgrazing",
    "population density"
   ]
  },
  {
   "id": "U2-P07",
   "topic": "2.2",
   "lo": "PSO-2.D",
   "skill": "2.B",
   "difficulty": "medium",
   "stem": "Mexico City is one of the largest metropolitan areas in the world and is built on the bed of a former lake. Which of the following best explains why parts of the city have been sinking?",
   "options": {
    "A": "Rising sea levels have flooded the low-lying neighborhoods closest to the coast.",
    "B": "Volcanic eruptions have caused the ground under older neighborhoods to collapse.",
    "C": "Pumping huge amounts of groundwater for residents has made the soil compact.",
    "D": "Rivers flowing through the city have carved deep channels that undercut its neighborhoods.",
    "E": "Coal mining under the city has left large empty tunnels beneath the streets."
   },
   "answer": "C",
   "explanation": "Millions of people need water, and much of Mexico City's water is pumped from an aquifer under the city. As the water is pulled out, the soft clay of the old lake bed dries out and packs down, so the ground sinks. Some areas sink tens of centimeters a year, which cracks pipes, buildings, and subway lines. This shows how a large, dense population can strain natural resources.",
   "whyNot": {
    "A": "Mexico City is far inland and more than 2,000 meters above sea level, so sea-level rise is not the cause.",
    "B": "The region has earthquakes and nearby volcanoes, but eruptions are not what makes the city slowly sink.",
    "D": "Most of the valley's old rivers now run through pipes. The ground sinks because water is pumped out of the clay below.",
    "E": "Coal mining is not the cause. The ground sinks because water is pumped out of the clay below."
   },
   "vocab": [
    "natural resources",
    "population density",
    "carrying capacity"
   ]
  },
  {
   "id": "U2-P08",
   "topic": "2.3",
   "lo": "PSO-2.E",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "A country reports a sex ratio of 105. What does this number mean?",
   "options": {
    "A": "There are 105 births each year for every 1,000 people.",
    "B": "There are 105 males for every 100 females.",
    "C": "There are 105 females for every 100 males.",
    "D": "There are 105 dependents for every 100 working-age people.",
    "E": "There are 105 infant deaths for every 1,000 live births."
   },
   "answer": "B",
   "explanation": "Sex ratio compares the number of males to the number of females. It is usually given as males per 100 females. A ratio of 105 means 105 males for every 100 females. Above 100 = more males; below 100 = more females.",
   "whyNot": {
    "A": "Births per 1,000 people is the crude birth rate.",
    "C": "That flips it. Sex ratio is males per 100 females.",
    "D": "Dependents per 100 working-age people is the dependency ratio.",
    "E": "Infant deaths per 1,000 live births is the infant mortality rate."
   },
   "vocab": [
    "sex ratio",
    "population composition"
   ]
  },
  {
   "id": "U2-P09",
   "topic": "2.3",
   "lo": "PSO-2.F",
   "skill": "3.E",
   "difficulty": "medium",
   "stimulus": {
    "type": "pyramid",
    "title": "POPULATION PYRAMID, COUNTRY C, 2025 (HYPOTHETICAL DATA)",
    "ageGroups": [
     "0–4",
     "5–9",
     "10–14",
     "15–19",
     "20–24",
     "25–29",
     "30–34",
     "35–39",
     "40–44",
     "45–49",
     "50–54",
     "55–59",
     "60–64",
     "65–69",
     "70–74",
     "75–79",
     "80+"
    ],
    "male": [
     2.4,
     2.5,
     2.6,
     2.7,
     2.8,
     3.0,
     3.1,
     3.2,
     3.1,
     2.9,
     3.2,
     4.1,
     4.2,
     3.8,
     2.4,
     1.6,
     1.6
    ],
    "female": [
     2.2,
     2.4,
     2.5,
     2.6,
     2.7,
     2.8,
     3.1,
     3.2,
     3.0,
     2.9,
     3.2,
     4.2,
     4.4,
     4.2,
     2.8,
     2.0,
     2.6
    ],
    "description": "Population pyramid for Country C with 17 five-year age groups, from 0–4 at the bottom to 80+ at the top. Males are on the left and females on the right; bar length is the percent of the total population.",
    "source": "Hypothetical data"
   },
   "stem": "Based on the population pyramid, demand for which of the following will most likely grow the most in Country C over the next 15 years?",
   "options": {
    "A": "Elementary schools and children's clothing",
    "B": "Maternity wards and child-care centers",
    "C": "College dormitories and entry-level jobs",
    "D": "Nursing homes and health care for older adults",
    "E": "Starter apartments for young, newly married couples"
   },
   "answer": "D",
   "explanation": "The widest bars are people now aged 55–69. In 15 years they will be 70–84. Older people need more doctor visits, medicines, home care, and nursing homes, so demand for those will grow. The narrow base shows fewer children are being born, so demand for schools and baby products will not grow much. Population pyramids help predict markets for goods and services.",
   "whyNot": {
    "A": "The base is narrow, and each younger group is smaller, so the number of children is not growing.",
    "B": "Births are low (narrow base), so demand for maternity wards and child care is unlikely to rise much.",
    "C": "The children and teens who will reach college age and start work in the next 15 years are small groups.",
    "E": "Today's 5- to 19-year-olds will be young adults in 15 years, and those groups are small."
   },
   "vocab": [
    "population pyramid",
    "age structure",
    "aging population"
   ]
  },
  {
   "id": "U2-P10",
   "topic": "2.3",
   "lo": "PSO-2.E",
   "skill": "3.C",
   "difficulty": "hard",
   "stimulus": {
    "type": "pyramid",
    "title": "POPULATION PYRAMID, COUNTRY G, 2025 (HYPOTHETICAL DATA)",
    "ageGroups": [
     "0–4",
     "5–9",
     "10–14",
     "15–19",
     "20–24",
     "25–29",
     "30–34",
     "35–39",
     "40–44",
     "45–49",
     "50–54",
     "55–59",
     "60–64",
     "65–69",
     "70–74",
     "75–79",
     "80+"
    ],
    "male": [
     3.0,
     2.8,
     2.5,
     2.3,
     7.4,
     11.6,
     12.5,
     10.4,
     7.7,
     5.2,
     3.4,
     1.9,
     0.9,
     0.5,
     0.2,
     0.1,
     0.1
    ],
    "female": [
     2.8,
     2.7,
     2.4,
     2.0,
     2.3,
     3.0,
     3.2,
     2.7,
     2.0,
     1.5,
     1.0,
     0.7,
     0.5,
     0.3,
     0.2,
     0.1,
     0.1
    ],
    "description": "Population pyramid for Country G with 17 five-year age groups, from 0–4 at the bottom to 80+ at the top. Males are on the left and females on the right; bar length is the percent of the total population.",
    "source": "Hypothetical data"
   },
   "stem": "Which of the following best explains the shape of Country G's population pyramid?",
   "options": {
    "A": "A pronatalist policy that raised birth rates sharply about 30 years ago",
    "B": "Sex-selective abortion that has favored male births since the 1990s",
    "C": "A large number of women leaving Country G to work in other countries",
    "D": "A war that killed many working-age women living in Country G",
    "E": "Large numbers of working-age men moving to Country G as guest workers"
   },
   "answer": "E",
   "explanation": "Look at ages 20–49. The male bars are much longer than the female bars AND much longer than the bars for boys. Without migration, an age group can only shrink as it gets older, so many people must have moved IN, mostly men of working age. A country that hires many foreign men as guest workers (for construction, oil, and service jobs) gets a pyramid like this. Some oil-rich Persian Gulf countries, such as Qatar and the United Arab Emirates, have pyramids with this shape.",
   "whyNot": {
    "A": "A baby boom would widen the bars for both sexes at the same ages, not mostly the male bars.",
    "B": "Sex-selective abortion would show up as extra boys in the youngest groups, but the bars for children here are balanced.",
    "C": "If many women left, the female bars would shrink, but the male bars would not become about four times as wide as the bars for boys.",
    "D": "A war would shrink some bars. It could not make the male bars wider than the bars for boys."
   },
   "vocab": [
    "population pyramid",
    "sex ratio",
    "guest worker"
   ]
  },
  {
   "id": "U2-P11",
   "topic": "2.3",
   "lo": "PSO-2.E",
   "skill": "5.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "AGE STRUCTURE OF A COUNTRY AND THREE OF ITS COUNTIES (HYPOTHETICAL DATA)",
    "columns": [
     "Place",
     "Under 15 (%)",
     "15–24 (%)",
     "25–64 (%)",
     "65 and older (%)"
    ],
    "rows": [
     [
      "Country (national total)",
      "18",
      "13",
      "52",
      "17"
     ],
     [
      "County U",
      "11",
      "38",
      "41",
      "10"
     ],
     [
      "County R",
      "10",
      "7",
      "41",
      "42"
     ],
     [
      "County F",
      "21",
      "12",
      "47",
      "20"
     ]
    ],
    "description": "Table showing the percent of the population in four age groups for a whole country and for three of its counties, U, R, and F.",
    "source": "Hypothetical data"
   },
   "stem": "Which of the following conclusions about population composition is best supported by the table?",
   "options": {
    "A": "Counties U and R differ sharply from the national age structure, suggesting migration sorts people by age.",
    "B": "County U has the highest birth rate in the table, because it has the largest share of people aged 15–24.",
    "C": "County R is likely to need more schools, because its population is older than the nation's.",
    "D": "The national age structure is a reliable guide to the age structure of each of the three counties in the table.",
    "E": "County F's age structure shows that it is losing population faster than Counties U and R."
   },
   "answer": "A",
   "explanation": "County U has 38% of its people aged 15–24, about three times the national 13%. That fits a college town, where students move in. County R has 42% aged 65 and older, about two and a half times the national 17%, which fits a place where retirees move. Zooming from the national scale to the county scale shows that migration can sort people by age into different places.",
   "whyNot": {
    "B": "The table shows age groups, not births. County U's share of children (11%) is lower than the nation's (18%).",
    "C": "Older places need more health care and senior services, not more schools. County R has only 10% under 15.",
    "D": "Counties U and R are very different from the national numbers, so the national pattern is a poor guide for them.",
    "E": "The table shows age structure at one point in time. It does not show whether any county is growing or shrinking."
   },
   "vocab": [
    "population composition",
    "age structure",
    "scale of analysis"
   ]
  },
  {
   "id": "U2-P12",
   "topic": "2.4",
   "lo": "IMP-2.A",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following best describes the rate of natural increase (RNI)?",
   "options": {
    "A": "The number of children an average woman will have during her lifetime",
    "B": "The difference between immigrants and emigrants per 1,000 people",
    "C": "The crude birth rate minus the crude death rate, not counting migration",
    "D": "The number of years it will take a population to double in size",
    "E": "The number of deaths of children under age 1 per 1,000 live births"
   },
   "answer": "C",
   "explanation": "RNI = crude birth rate minus crude death rate. It is usually shown as a percent, so you divide by 10. Example: a birth rate of 30 per 1,000 and a death rate of 10 per 1,000 gives 20 per 1,000, or 2.0%. RNI leaves out migration, so a country's real growth can be higher or lower than its RNI.",
   "whyNot": {
    "A": "That is the total fertility rate (TFR).",
    "B": "That is the net migration rate. RNI leaves migration out.",
    "D": "That is the doubling time, which you can estimate from RNI (70 ÷ RNI).",
    "E": "That is the infant mortality rate (IMR)."
   },
   "vocab": [
    "rate of natural increase",
    "crude birth rate",
    "crude death rate"
   ]
  },
  {
   "id": "U2-P13",
   "topic": "2.4",
   "lo": "IMP-2.A",
   "skill": "3.C",
   "difficulty": "hard",
   "stimulus": {
    "type": "table",
    "title": "BIRTHS, DEATHS, AND POPULATION GROWTH IN FIVE COUNTRIES, 2024",
    "columns": [
     "Country",
     "Crude birth rate (births per 1,000 people)",
     "Crude death rate (deaths per 1,000 people)",
     "Population growth rate (%)"
    ],
    "rows": [
     [
      "Niger",
      "41.4",
      "8.7",
      "3.3"
     ],
     [
      "India",
      "16.0",
      "6.6",
      "0.9"
     ],
     [
      "Canada",
      "8.9",
      "7.9",
      "3.0"
     ],
     [
      "Germany",
      "8.1",
      "12.1",
      "0.3"
     ],
     [
      "Japan",
      "5.7",
      "13.3",
      "−0.4"
     ]
    ],
    "description": "Table of the 2024 crude birth rate, crude death rate, and population growth rate for Niger, India, Canada, Germany, and Japan.",
    "source": "World Bank, World Development Indicators: crude birth rate (SP.DYN.CBRT.IN), crude death rate (SP.DYN.CDRT.IN), and population growth (SP.POP.GROW), 2024 values, accessed November 8, 2026."
   },
   "stem": "According to the table, which country's population grew in 2024 even though it had more deaths than births, and what best explains that growth?",
   "options": {
    "A": "Japan, because more people moved into Japan than moved out",
    "B": "Germany, because more people moved into Germany than moved out",
    "C": "Canada, because its birth rate was much higher than its death rate",
    "D": "Germany, because its death rate fell below its birth rate during the year",
    "E": "Niger, because it had the highest rate of natural increase in the table"
   },
   "answer": "B",
   "explanation": "Germany's death rate (12.1) was higher than its birth rate (8.1), so its rate of natural increase was negative: (8.1 − 12.1) ÷ 10 = −0.4%. Yet its population grew 0.3%. The only other way to add people is migration, so more people moved into Germany than moved out. Population change = natural increase + net migration.",
   "whyNot": {
    "A": "Japan also had more deaths than births, but the table shows its population shrank (−0.4%).",
    "C": "Canada's birth rate (8.9) was only a little higher than its death rate (7.9), an RNI of 0.1%. Its 3.0% growth came mostly from migration, not births.",
    "D": "The table shows Germany's death rate (12.1) was higher than its birth rate (8.1).",
    "E": "Niger had far more births than deaths, so it does not fit the question."
   },
   "vocab": [
    "rate of natural increase",
    "net migration",
    "crude death rate"
   ]
  },
  {
   "id": "U2-P14",
   "topic": "2.4",
   "lo": "IMP-2.A",
   "skill": "1.D",
   "difficulty": "medium",
   "stem": "Country Q has a crude birth rate of 31 per 1,000 and a crude death rate of 7 per 1,000. Assuming no migration and no change in these rates, about how long will it take Country Q's population to double?",
   "options": {
    "A": "About 3 years",
    "B": "About 10 years",
    "C": "About 23 years",
    "D": "About 29 years",
    "E": "About 168 years"
   },
   "answer": "D",
   "explanation": "Step 1: RNI = (31 − 7) ÷ 10 = 2.4%. Step 2: Use the rule of 70: 70 ÷ 2.4 ≈ 29 years. A population growing 2.4% a year doubles in about 29 years.",
   "whyNot": {
    "A": "You divided 70 by 24. First change 24 per 1,000 into a percent: 2.4%.",
    "B": "You used only the death rate (70 ÷ 7). Use birth rate minus death rate.",
    "C": "You used only the birth rate (70 ÷ 3.1). Subtract the death rate first.",
    "E": "You multiplied 70 by 2.4. Divide instead: 70 ÷ 2.4."
   },
   "vocab": [
    "doubling time",
    "rate of natural increase",
    "rule of 70"
   ]
  },
  {
   "id": "U2-P15",
   "topic": "2.4",
   "lo": "IMP-2.A",
   "skill": "2.B",
   "difficulty": "medium",
   "stem": "In many rural farming areas of lower-income countries, families tend to have more children than families in the same countries' cities. Which of the following best explains this pattern?",
   "options": {
    "A": "Rural areas usually have more hospitals, so more babies survive to adulthood.",
    "B": "Rural families usually have higher incomes, so they can afford larger families.",
    "C": "Rural areas usually have more schools, so children are cheaper to educate.",
    "D": "Governments usually pay rural families more than city families for each child.",
    "E": "Rural families often rely on children for farm work and for care in old age."
   },
   "answer": "E",
   "explanation": "On a farm, children can help plant, herd animals, and carry water, so each child adds a worker. Where there are few pensions, grown children also care for their parents when they are old. In cities, children cost more (rent, school fees) and add less income. Economic factors like these help explain differences in fertility.",
   "whyNot": {
    "A": "Rural areas usually have FEWER hospitals and doctors than cities.",
    "B": "Rural incomes are usually LOWER than city incomes.",
    "C": "Cities usually have more schools. And school costs tend to shrink families, not grow them.",
    "D": "Payments for having children are usually national programs. They do not explain the rural-urban gap."
   },
   "vocab": [
    "total fertility rate",
    "economic factors",
    "rural"
   ]
  },
  {
   "id": "U2-P16",
   "topic": "2.4",
   "lo": "IMP-2.A",
   "skill": "1.B",
   "difficulty": "medium",
   "stem": "Geographers often use the infant mortality rate (IMR) as an indicator of a country's overall health and living conditions. Which of the following best explains why?",
   "options": {
    "A": "Whether infants survive depends on clean water, nutrition, and medical care.",
    "B": "Infants make up the largest share of the population in most countries.",
    "C": "Infant deaths are the main reason that a population's median age rises.",
    "D": "A high IMR means a country's population is aging and its birth rate is falling.",
    "E": "The IMR includes deaths of adults as well as infants, so it describes the whole population."
   },
   "answer": "A",
   "explanation": "Babies are very fragile. Whether they live to age 1 depends on things like clean water, enough food for mothers and babies, vaccines, and doctors or nurses at birth. So a low IMR usually means good health care and living conditions, and a high IMR usually means those are missing. IMR = deaths of babies under age 1 per 1,000 live births.",
   "whyNot": {
    "B": "Babies under age 1 are a small share of any population.",
    "C": "Median age rises mainly because birth rates fall and people live longer.",
    "D": "A high IMR is common where birth rates are high and the population is young.",
    "E": "The IMR counts only deaths of babies under age 1. The crude death rate counts deaths at all ages."
   },
   "vocab": [
    "infant mortality rate",
    "crude death rate"
   ]
  },
  {
   "id": "U2-P17",
   "topic": "2.5",
   "lo": "IMP-2.B",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following best describes what happens during Stage 2 of the demographic transition model?",
   "options": {
    "A": "Birth and death rates are both high, so the population grows slowly.",
    "B": "Death rates fall sharply while birth rates stay high, so the population grows rapidly.",
    "C": "Birth rates fall sharply while death rates stay low, so population growth slows.",
    "D": "Birth and death rates are both low, so the population grows slowly or stays stable.",
    "E": "Birth rates drop below death rates, so the population begins to shrink."
   },
   "answer": "B",
   "explanation": "In Stage 2, better food supplies, clean water, and basic medicine help more people survive, so the death rate drops. Birth rates stay high because families have not yet changed how many children they have. The big gap between births and deaths makes the population grow fast. Some countries, such as Niger, still have Stage 2 patterns today.",
   "whyNot": {
    "A": "That is Stage 1.",
    "C": "That is Stage 3.",
    "D": "That is Stage 4.",
    "E": "That is Stage 5, which some geographers add to the model."
   },
   "vocab": [
    "demographic transition model",
    "crude birth rate",
    "crude death rate"
   ]
  },
  {
   "id": "U2-P18",
   "topic": "2.5",
   "lo": "IMP-2.B",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "line",
    "title": "CRUDE BIRTH AND DEATH RATES, COUNTRY K, 1900–2020 (HYPOTHETICAL DATA)",
    "xLabel": "Year",
    "yLabel": "Rate per 1,000 people",
    "categories": [
     "1900",
     "1920",
     "1940",
     "1960",
     "1980",
     "2000",
     "2020"
    ],
    "series": [
     {
      "name": "Crude birth rate",
      "values": [
       44,
       44,
       45,
       44,
       35,
       26,
       19
      ]
     },
     {
      "name": "Crude death rate",
      "values": [
       38,
       33,
       26,
       18,
       11,
       8,
       7
      ]
     }
    ],
    "yMax": 50,
    "description": "Line graph of Country K's crude birth rate and crude death rate, per 1,000 people, every 20 years from 1900 to 2020.",
    "source": "Hypothetical data"
   },
   "stem": "Which of the following most likely explains the change in Country K's crude birth rate between 1960 and 2020?",
   "options": {
    "A": "An increase in infant deaths made parents decide to have fewer children.",
    "B": "A government policy began paying families a bonus for each new child.",
    "C": "Many workers left factory jobs in growing cities and returned to farming villages.",
    "D": "Cities grew, more girls stayed in school, and contraception became easier to get.",
    "E": "A disease outbreak killed many adults of childbearing age in Country K."
   },
   "answer": "D",
   "explanation": "Between 1960 and 2020 the birth rate fell from 44 to 19 per 1,000. That is Stage 3 of the demographic transition. In Stage 3, more people move to cities where children cost more, girls and women get more education and jobs, and family planning is easier to get, so families choose to have fewer children.",
   "whyNot": {
    "A": "The death rate was falling in these years (18 to 7), so infant deaths were most likely falling, not rising.",
    "B": "A bonus for having children is a pronatalist policy. It would push the birth rate up, not down.",
    "C": "Moving from cities back to farms usually raises birth rates, because children are more useful on farms.",
    "E": "The death rate kept falling in these years, so the graph does not show a deadly outbreak."
   },
   "vocab": [
    "demographic transition model",
    "Stage 3",
    "crude birth rate"
   ]
  },
  {
   "id": "U2-P19",
   "topic": "2.5",
   "lo": "IMP-2.B",
   "skill": "1.B",
   "difficulty": "easy",
   "stem": "According to the epidemiological transition model, as a country develops, the leading causes of death shift in which way?",
   "options": {
    "A": "From heart disease and cancer to infectious diseases such as cholera and measles",
    "B": "From accidents and violence to diseases spread by mosquitoes",
    "C": "From infectious and parasitic diseases to chronic diseases such as heart disease",
    "D": "From diseases of old age to diseases that mainly affect infants",
    "E": "From diseases spread by dirty water to diseases spread by spoiled or undercooked food"
   },
   "answer": "C",
   "explanation": "In the early stages, most people die young from infections like cholera, measles, and tuberculosis, and from famine. As clean water, vaccines, and medicine spread, those deaths drop. People live longer, so more of them die later in life from chronic (degenerative) diseases like heart disease, cancer, and stroke. The epidemiological transition explains why death rates fall in the demographic transition.",
   "whyNot": {
    "A": "That is backward. Infectious diseases were the leading killers first.",
    "B": "Mosquito-borne diseases like malaria are infectious diseases, which decline as countries develop.",
    "D": "As countries develop, fewer infants die, and deaths shift toward old age.",
    "E": "Both of these are infectious diseases. The model's shift is from infectious diseases to chronic ones."
   },
   "vocab": [
    "epidemiological transition",
    "infectious disease",
    "chronic disease"
   ]
  },
  {
   "id": "U2-P20",
   "topic": "2.5",
   "lo": "IMP-2.B",
   "skill": "1.E",
   "difficulty": "hard",
   "stem": "Which of the following is a limitation of the demographic transition model when it is used to predict population change in lower-income countries today?",
   "options": {
    "A": "It leaves out birth rates, so it is unable to show why a country's growth speeds up or slows down.",
    "B": "It describes how individual cities grow, so it does not apply to a whole country's population.",
    "C": "It assumes that countries move backward from Stage 4 to Stage 1 as they develop and industrialize.",
    "D": "It counts migration as part of growth, so it overstates growth in countries that send many emigrants.",
    "E": "It is based on Europe's past, so it may not fit places where imported medicines cut death rates quickly."
   },
   "answer": "E",
   "explanation": "The DTM was built from the history of Europe and North America, where death rates fell slowly over many decades as farming, industry, and sanitation improved. In many lower-income countries in the 1900s, vaccines and antibiotics from abroad cut death rates within a few decades, often before much industry developed. Birth rates also fall at different speeds because of culture and government policy. So the model may not predict when or how fast these countries move through the stages.",
   "whyNot": {
    "A": "Birth rates are one of the two main lines in the model.",
    "B": "The DTM describes the population of a country, not how individual cities grow.",
    "C": "Countries are expected to move forward from Stage 1 toward Stage 4, not backward.",
    "D": "The DTM uses only births and deaths. Leaving migration out is actually another one of its limits."
   },
   "vocab": [
    "demographic transition model",
    "limitations of models"
   ]
  },
  {
   "id": "U2-P21",
   "topic": "2.6",
   "lo": "IMP-2.B",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "In 1798, Thomas Malthus predicted that famine and other disasters would eventually limit population growth. Which reasoning was the basis of his prediction?",
   "options": {
    "A": "Population tends to grow geometrically, while food supply grows only arithmetically.",
    "B": "Food supply tends to grow geometrically, while population grows only arithmetically.",
    "C": "Birth rates fall as countries industrialize, so populations will soon begin to shrink.",
    "D": "Population growth leads farmers to adopt new methods that raise food production.",
    "E": "Migration to cities will leave too few farmers in the countryside to grow enough food."
   },
   "answer": "A",
   "explanation": "Malthus said population grows geometrically (1, 2, 4, 8, 16…), because each generation can double. Food supply grows arithmetically (1, 2, 3, 4, 5…), adding about the same amount each time. Sooner or later, people would outnumber the food. He thought 'positive checks' like famine, disease, and war would then raise death rates, unless people married later and had fewer children.",
   "whyNot": {
    "B": "That flips Malthus's idea. He said population, not food, grows faster.",
    "C": "That describes later stages of the demographic transition model, an idea developed long after Malthus.",
    "D": "That is Esther Boserup's argument, which criticizes Malthus.",
    "E": "Malthus focused on population growing faster than food, not on migration to cities."
   },
   "vocab": [
    "Malthusian theory",
    "geometric growth",
    "arithmetic growth"
   ]
  },
  {
   "id": "U2-P22",
   "topic": "2.6",
   "lo": "IMP-2.B",
   "skill": "2.E",
   "difficulty": "medium",
   "stimulus": {
    "type": "line",
    "title": "POPULATION AND FOOD PRODUCTION IN COUNTRY N, 1960–2020 (INDEX, 1960 = 100) (HYPOTHETICAL DATA)",
    "xLabel": "Year",
    "yLabel": "Index (1960 = 100)",
    "categories": [
     "1960",
     "1970",
     "1980",
     "1990",
     "2000",
     "2010",
     "2020"
    ],
    "series": [
     {
      "name": "Population",
      "values": [
       100,
       125,
       155,
       185,
       213,
       240,
       265
      ]
     },
     {
      "name": "Food production",
      "values": [
       100,
       135,
       180,
       230,
       285,
       340,
       395
      ]
     }
    ],
    "yMax": 400,
    "description": "Line graph with two lines, population and food production, for Country N from 1960 to 2020. Both lines are index numbers that start at 100 in 1960.",
    "source": "Hypothetical data"
   },
   "stem": "To what degree does Malthusian theory explain the trends in Country N shown in the graph?",
   "options": {
    "A": "It explains them well, because population grew geometrically and caused famine by 2000.",
    "B": "It explains them well, because food grew arithmetically while population grew faster.",
    "C": "It explains them partly, because population and food production grew at the same rate.",
    "D": "It explains them poorly, because food production grew faster than population did.",
    "E": "It explains them poorly, because Country N's population declined after 1960."
   },
   "answer": "D",
   "explanation": "Malthus predicted population would outgrow food. In Country N the opposite happened: from 1960 to 2020, population grew to 2.65 times its 1960 level, but food production grew to 3.95 times. That means about 49% more food per person (395 ÷ 265 ≈ 1.49). Critics of Malthus point to cases like this, where new technology, such as Green Revolution seeds and fertilizer, raised food output faster than population.",
   "whyNot": {
    "A": "The graph shows no famine. Food production stayed ahead of population the whole time.",
    "B": "Food production (395) grew faster than population (265), the opposite of what Malthus predicted.",
    "C": "The two lines split apart after 1960. Food production grew much faster.",
    "E": "Population rose every decade, from 100 to 265."
   },
   "vocab": [
    "Malthusian theory",
    "critiques of Malthus",
    "Green Revolution"
   ]
  },
  {
   "id": "U2-P23",
   "topic": "2.6",
   "lo": "IMP-2.B",
   "skill": "1.C",
   "difficulty": "hard",
   "stem": "Which of the following best describes how neo-Malthusians, such as Paul Ehrlich, built on the ideas of Thomas Malthus?",
   "options": {
    "A": "They argued that population growth encourages farmers to invent better tools and farming methods.",
    "B": "They warned that growing populations also use up water, energy, and other resources and harm the environment.",
    "C": "They argued that hunger results mainly from poverty and unequal food distribution, not from too many people.",
    "D": "They predicted that birth rates would rise again once countries reach the last stage of the demographic transition.",
    "E": "They argued that new technology lets food supply grow faster than population, so famine is unlikely."
   },
   "answer": "B",
   "explanation": "Malthus focused on food. Neo-Malthusians, like Paul Ehrlich in The Population Bomb (1968), widened the worry: more people also means more demand for water, energy, land, and minerals, plus more pollution. They argue that Earth has a carrying capacity, and many support family planning to slow growth.",
   "whyNot": {
    "A": "That is Esther Boserup's critique of Malthus, not a neo-Malthusian idea.",
    "C": "That is a critique of Malthus. These critics say poverty and unequal distribution, not population size, cause hunger.",
    "D": "Neo-Malthusians worry about too much growth. They did not predict birth rates rising again.",
    "E": "That is the hopeful view of Malthus's critics, the opposite of a neo-Malthusian warning."
   },
   "vocab": [
    "neo-Malthusian",
    "Malthusian theory",
    "carrying capacity"
   ]
  },
  {
   "id": "U2-P24",
   "topic": "2.7",
   "lo": "SPS-2.A",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "A government offers families a cash payment for each baby, extends paid parental leave, and pays for most child-care costs. These steps are best described as",
   "options": {
    "A": "an antinatalist policy",
    "B": "an immigration policy",
    "C": "a pronatalist policy",
    "D": "a family-planning program",
    "E": "a guest worker program"
   },
   "answer": "C",
   "explanation": "Pronatalist policies try to raise the birth rate. Cash for babies, paid leave, and cheaper child care lower the cost of raising children, so families may decide to have more. France and several other European and East Asian countries use policies like these because their fertility rates are below replacement level (about 2.1 children per woman).",
   "whyNot": {
    "A": "Antinatalist policies try to LOWER the birth rate.",
    "B": "Immigration policies control who can move into a country. These steps are about births.",
    "D": "Family-planning programs help people choose to have fewer children or space them out. That usually lowers birth rates.",
    "E": "Guest worker programs bring in temporary foreign workers. They do not reward births."
   },
   "vocab": [
    "pronatalist policy",
    "antinatalist policy",
    "replacement level"
   ]
  },
  {
   "id": "U2-P25",
   "topic": "2.7",
   "lo": "SPS-2.A",
   "skill": "2.C",
   "difficulty": "medium",
   "stem": "China's one-child policy, in place from about 1980 until 2015, limited most urban couples to one child. Which of the following is a long-term consequence of this policy?",
   "options": {
    "A": "A sharp rise in the share of children under age 15 in China's population",
    "B": "A large increase in China's total fertility rate during the 1990s",
    "C": "A sex ratio at birth that favored girls over boys for several decades",
    "D": "A large wave of older adults emigrating from China to retire abroad",
    "E": "A rapidly aging population and more boys than girls born for many years"
   },
   "answer": "E",
   "explanation": "With far fewer births, China now has a smaller share of young people and a growing share of older people, so it is aging quickly and its workforce is shrinking. Because many families preferred sons, some used sex-selective abortion, so for many years far more boys than girls were born. China switched to a two-child policy in 2016 and a three-child policy in 2021.",
   "whyNot": {
    "A": "Fewer births made the share of children go DOWN, not up.",
    "B": "The policy lowered fertility. China's TFR fell well below replacement level.",
    "C": "It was the reverse: more boys than girls were born.",
    "D": "China's aging comes from low births and longer lives, not from older people leaving."
   },
   "vocab": [
    "antinatalist policy",
    "sex ratio",
    "aging population"
   ]
  },
  {
   "id": "U2-P26",
   "topic": "2.7",
   "lo": "SPS-2.A",
   "skill": "2.C",
   "difficulty": "medium",
   "stem": "Country P adopts a points-based immigration system that gives applicants points for university degrees, job skills in demand, language ability, and being of working age. Which outcome is most likely?",
   "options": {
    "A": "Most new immigrants will be retirees moving to join their adult children in Country P.",
    "B": "New immigrants will tend to be younger, skilled workers who add to the labor force.",
    "C": "Most new immigrants will be refugees fleeing armed conflict in nearby countries.",
    "D": "The share of Country P's population aged 65 and older will rise more quickly.",
    "E": "Country P's sending countries will gain skilled workers who move from Country P."
   },
   "answer": "B",
   "explanation": "A points system picks immigrants based on what the country wants. Points for degrees, needed skills, language, and age favor young, educated workers. That adds people to the working-age part of the population pyramid, which can help a country with low birth rates. Canada and Australia are well-known users of points-based systems.",
   "whyNot": {
    "A": "Points for being of working age make retirees less likely to qualify.",
    "C": "Refugees are admitted for protection, not through points for job skills.",
    "D": "Adding young workers slows aging. It does not speed it up.",
    "E": "Skilled workers move INTO Country P, so it gains skills (a brain gain), and sending countries may lose them."
   },
   "vocab": [
    "immigration policy",
    "brain drain",
    "labor force"
   ]
  },
  {
   "id": "U2-P27",
   "topic": "2.8",
   "lo": "SPS-2.B",
   "skill": "3.D",
   "difficulty": "medium",
   "stimulus": {
    "type": "bar",
    "title": "AVERAGE TOTAL FERTILITY RATE OF DISTRICTS IN COUNTRY E, GROUPED BY SHARE OF WOMEN AGED 20–24 WHO COMPLETED SECONDARY SCHOOL (HYPOTHETICAL DATA)",
    "categories": [
     "Under 20%",
     "20–39%",
     "40–59%",
     "60–79%",
     "80% or more"
    ],
    "series": [
     {
      "name": "Average total fertility rate (children per woman)",
      "values": [
       5.9,
       4.8,
       3.6,
       2.6,
       1.9
      ]
     }
    ],
    "yLabel": "Children per woman",
    "yMax": 7,
    "text": "Each district in Country E is placed in one group based on the share of its women aged 20–24 who completed secondary school.",
    "description": "Bar chart with five groups of districts. Districts where under 20% of young women completed secondary school average 5.9 children per woman; 20–39%, 4.8; 40–59%, 3.6; 60–79%, 2.6; 80% or more, 1.9.",
    "source": "Hypothetical data"
   },
   "stem": "Which of the following conclusions is best supported by the chart?",
   "options": {
    "A": "Districts where more women finished secondary school tend to have lower fertility rates.",
    "B": "Districts in the highest education group still have fertility above replacement level.",
    "C": "Moving from the 60–79% group to the top group lowers fertility by about two children.",
    "D": "Fertility in the lowest education group is about twice the fertility in the top group.",
    "E": "The chart proves that schooling by itself made fertility fall in each district over time."
   },
   "answer": "A",
   "explanation": "Going from districts where few women finished secondary school to districts where most did, the average fertility rate drops step by step, from 5.9 to 1.9 children per woman. Your AP course guide says more education, jobs, health care, and access to contraception for women have lowered fertility in most of the world. The chart shows a link (a correlation); by itself it does not prove the cause.",
   "whyNot": {
    "B": "Replacement level is about 2.1. The top group's 1.9 is below replacement.",
    "C": "The drop from 2.6 to 1.9 is about 0.7 children, not 2.",
    "D": "5.9 is about three times 1.9, not twice.",
    "E": "The chart compares districts at one point in time. It shows a pattern, not proof of a single cause or of change over time."
   },
   "vocab": [
    "total fertility rate",
    "replacement level",
    "correlation"
   ]
  },
  {
   "id": "U2-P28",
   "topic": "2.8",
   "lo": "SPS-2.B",
   "skill": "1.B",
   "difficulty": "medium",
   "stem": "As more women in a country take paid jobs outside the home, the country's total fertility rate often falls. Which of the following best explains this relationship?",
   "options": {
    "A": "Women with paid jobs usually marry earlier, which shortens their childbearing years.",
    "B": "Paid jobs usually require women to move to rural areas, where families are smaller.",
    "C": "Countries with more working women usually pass laws that limit the size of families.",
    "D": "Working women often delay marriage and children, and each child costs more lost income.",
    "E": "Women with paid jobs usually have less access to health care and to contraception."
   },
   "answer": "D",
   "explanation": "When women have careers, many choose to finish school and start working before they marry or have children. Starting later leaves fewer years to have children. Also, each child can mean time away from a paying job (economists call this an opportunity cost), so many families choose to have fewer children.",
   "whyNot": {
    "A": "It is the reverse: women with paid jobs tend to marry LATER.",
    "B": "Paid jobs are more common in cities, and rural families are usually larger, not smaller.",
    "C": "Few countries limit family size by law. Lower fertility here comes mostly from families' own choices.",
    "E": "Women with paid jobs usually have MORE access to health care and contraception."
   },
   "vocab": [
    "total fertility rate",
    "women and demographic change",
    "opportunity cost"
   ]
  },
  {
   "id": "U2-P29",
   "topic": "2.8",
   "lo": "SPS-2.B",
   "skill": "1.D",
   "difficulty": "medium",
   "stem": "In the 1880s, E. G. Ravenstein observed that women were more likely than men to migrate within their home country, while men were more likely to move to other countries. Today, women and girls make up almost half of all international migrants. Which of the following best explains this change?",
   "options": {
    "A": "Laws in most countries now limit men's emigration, so more women move abroad instead.",
    "B": "Women today have more children than in the 1880s, so whole families move abroad together.",
    "C": "Women's economic roles have expanded, and many now move abroad for jobs such as nursing.",
    "D": "Most international moves are now short trips across one border, like women's moves in the 1880s.",
    "E": "Destination countries now give women's visa applications priority over applications from men."
   },
   "answer": "C",
   "explanation": "Ravenstein's laws describe migration in the 1800s, when most women's moves were short, for example from farms to nearby towns to work as household servants. Since then, women's roles in the economy have grown. Many women now migrate on their own for work, for example as nurses, caregivers, and domestic and service workers. That helps explain why women and girls are now about 48% of international migrants.",
   "whyNot": {
    "A": "Countries do not generally stop men from leaving. Men are still a little more than half of international migrants.",
    "B": "Women today have FEWER children than in the 1880s.",
    "D": "International migrants move many different distances. The change comes from women's changing economic roles.",
    "E": "There is no general rule that favors women's visas. Women's share grew because more women migrate for work."
   },
   "vocab": [
    "Ravenstein's laws of migration",
    "international migration",
    "women and demographic change"
   ]
  },
  {
   "id": "U2-P30",
   "topic": "2.9",
   "lo": "SPS-2.C",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "The dependency ratio compares which groups in a population?",
   "options": {
    "A": "The number of people who live in cities and the number who live in rural areas",
    "B": "The number of men and the number of women in the same age group",
    "C": "The number of births and the number of deaths in a single year",
    "D": "The number of immigrants and the number of emigrants in a single year",
    "E": "People under age 15 or age 65 and older, compared with people aged 15 to 64"
   },
   "answer": "E",
   "explanation": "Dependency ratio = (people aged 0–14 + people 65 and older) ÷ people aged 15–64 × 100. Children and older adults are called 'dependents' because most do not work full-time, so working-age people support them through families and taxes. A higher ratio means each worker supports more people.",
   "whyNot": {
    "A": "That compares the urban and rural population.",
    "B": "That is the sex ratio.",
    "C": "Births minus deaths gives the rate of natural increase.",
    "D": "That is net migration."
   },
   "vocab": [
    "dependency ratio",
    "aging population"
   ]
  },
  {
   "id": "U2-P31",
   "topic": "2.9",
   "lo": "SPS-2.C",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "POPULATION OF COUNTRY T BY BROAD AGE GROUP, 2025 (HYPOTHETICAL DATA)",
    "columns": [
     "Age group",
     "Population (millions)"
    ],
    "rows": [
     [
      "0–14",
      "9.6"
     ],
     [
      "15–64",
      "40.0"
     ],
     [
      "65 and older",
      "14.4"
     ],
     [
      "Total",
      "64.0"
     ]
    ],
    "description": "Table of Country T's population in three broad age groups, in millions: 0–14, 9.6; 15–64, 40.0; 65 and older, 14.4; total, 64.0.",
    "source": "Hypothetical data"
   },
   "stem": "Based on the table, what is Country T's dependency ratio?",
   "options": {
    "A": "24",
    "B": "36",
    "C": "60",
    "D": "62.5",
    "E": "167"
   },
   "answer": "C",
   "explanation": "Dependents are ages 0–14 and 65+: 9.6 + 14.4 = 24.0 million. Working-age people (15–64): 40.0 million. Dependency ratio = 24.0 ÷ 40.0 × 100 = 60. So there are 60 dependents for every 100 working-age people.",
   "whyNot": {
    "A": "24 counts only the children (9.6 ÷ 40 × 100). Add the people 65 and older too.",
    "B": "36 counts only the people 65 and older (14.4 ÷ 40 × 100). Add the children too.",
    "D": "62.5 is working-age people as a percent of the total (40 ÷ 64 × 100).",
    "E": "167 flips the fraction (40 ÷ 24 × 100). Put the dependents on top."
   },
   "vocab": [
    "dependency ratio",
    "working-age population"
   ]
  },
  {
   "id": "U2-P32",
   "topic": "2.9",
   "lo": "SPS-2.C",
   "skill": "2.C",
   "difficulty": "medium",
   "stem": "In Country S, life expectancy is rising, and the fertility rate has been below replacement level for 30 years. Which of the following is the most likely economic consequence over the next 20 years?",
   "options": {
    "A": "Fewer workers paying taxes for each retiree, straining pension and health systems",
    "B": "A growing number of young workers competing for a shrinking number of jobs",
    "C": "Rising demand for new elementary schools as the number of children increases",
    "D": "A falling dependency ratio as more and more people move into the working-age group",
    "E": "A rapid rise in the crude birth rate as the large older generation retires"
   },
   "answer": "A",
   "explanation": "Low fertility means fewer young people are growing up to become workers. Longer lives mean more people are retired, and for longer. So each worker pays taxes that support more retirees, and health care costs rise. Governments may respond by raising the retirement age, raising taxes, cutting benefits, encouraging births, or admitting more working-age immigrants. Japan and Italy face this challenge today.",
   "whyNot": {
    "B": "Low fertility means FEWER young workers, so labor shortages are more likely than job competition.",
    "C": "Fertility is below replacement, so the number of children is shrinking, not growing.",
    "D": "As the older group grows and the working-age group shrinks, the dependency ratio RISES.",
    "E": "Retiring does not raise birth rates. An older population usually has a LOWER crude birth rate."
   },
   "vocab": [
    "aging population",
    "dependency ratio",
    "replacement level"
   ]
  },
  {
   "id": "U2-P33",
   "topic": "2.10",
   "lo": "IMP-2.C",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Several years of drought destroy crops in a farming region, and many families move to cities in another part of the country. The drought is best described as which type of migration factor?",
   "options": {
    "A": "An economic pull factor",
    "B": "A political push factor",
    "C": "A cultural pull factor",
    "D": "An environmental push factor",
    "E": "An intervening opportunity along the way"
   },
   "answer": "D",
   "explanation": "A push factor makes people want to LEAVE a place. A drought comes from the natural environment, so it is an environmental push factor. Floods, hurricanes, and rising sea levels are other environmental push factors.",
   "whyNot": {
    "A": "Pull factors attract people TO a place, like jobs in a city. The drought pushes people away.",
    "B": "Political push factors include war, persecution, and unfair laws. A drought is a natural event.",
    "C": "Cultural pull factors include joining a community that shares your language or religion.",
    "E": "An intervening opportunity is a chance found along the way that makes a migrant stop before reaching the planned destination."
   },
   "vocab": [
    "push factor",
    "pull factor",
    "environmental factors"
   ]
  },
  {
   "id": "U2-P34",
   "topic": "2.10",
   "lo": "IMP-2.C",
   "skill": "1.D",
   "difficulty": "medium",
   "stem": "Amina leaves her village planning to look for work in the capital city, 600 kilometers away. On the way, she stops in a mining town 200 kilometers from home, finds a good job, and settles there. Her decision to stay in the mining town is an example of",
   "options": {
    "A": "an intervening obstacle",
    "B": "a forced migration",
    "C": "an intervening opportunity",
    "D": "chain migration",
    "E": "a political push factor at the origin"
   },
   "answer": "C",
   "explanation": "An intervening opportunity is a chance (like a job) found between where a migrant started and where she planned to go, so she stops early. Amina found a job in the mining town, so she never went on to the capital. An intervening obstacle is the opposite: something that blocks or slows a move, like a mountain range or a strict border.",
   "whyNot": {
    "A": "An obstacle blocks a move. Amina was not blocked; she found something better along the way.",
    "B": "Amina chose to move, so this is voluntary migration.",
    "D": "Chain migration means following family or friends who moved earlier. Amina followed a job.",
    "E": "Political push factors include war and persecution. Amina left to find work, an economic reason."
   },
   "vocab": [
    "intervening opportunity",
    "intervening obstacle",
    "voluntary migration"
   ]
  },
  {
   "id": "U2-P35",
   "topic": "2.10",
   "lo": "IMP-2.C",
   "skill": "3.E",
   "difficulty": "medium",
   "stimulus": {
    "type": "bar",
    "title": "PEOPLE WHO MOVED TO CITY M IN 2025, BY DISTANCE FROM THEIR PREVIOUS HOME (HYPOTHETICAL DATA)",
    "categories": [
     "Under 50 km",
     "50–199 km",
     "200–499 km",
     "500–999 km",
     "1,000 km or more"
    ],
    "series": [
     {
      "name": "Migrants (thousands)",
      "values": [
       42,
       24,
       12,
       6,
       4
      ]
     }
    ],
    "yLabel": "Thousands of migrants",
    "yMax": 50,
    "description": "Bar chart of people who moved to City M in 2025, grouped by how far away they lived before: under 50 km, 42 thousand; 50–199 km, 24 thousand; 200–499 km, 12 thousand; 500–999 km, 6 thousand; 1,000 km or more, 4 thousand.",
    "source": "Hypothetical data"
   },
   "stem": "The pattern in the chart is most consistent with which of Ravenstein's laws of migration?",
   "options": {
    "A": "Each migration flow produces a counterflow in the opposite direction.",
    "B": "Long-distance migrants usually head for major centers of trade and industry.",
    "C": "Women are more likely than men to migrate within their home country.",
    "D": "Most migrants move for economic reasons, such as finding better jobs.",
    "E": "Most migrants move a short distance from where they lived before."
   },
   "answer": "E",
   "explanation": "The bars get shorter as distance gets longer: 42,000 people came from less than 50 km away, but only 4,000 came from 1,000 km or more. Ravenstein noticed this in the 1880s: most migrants move a short distance. This is called distance decay. Distance itself is an intervening obstacle, because longer moves cost more and people know less about faraway places.",
   "whyNot": {
    "A": "The chart shows only people arriving in City M, not anyone leaving, so it cannot show a counterflow.",
    "B": "The chart shows one city only, so it cannot show where long-distance migrants usually go.",
    "C": "The chart does not separate migrants by sex.",
    "D": "The chart shows distance, not the reasons people moved."
   },
   "vocab": [
    "Ravenstein's laws of migration",
    "distance decay"
   ]
  },
  {
   "id": "U2-P36",
   "topic": "2.11",
   "lo": "IMP-2.D",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Fighting between armed groups forces thousands of families to leave their homes. They move to a camp in another province of the same country. These families are best described as",
   "options": {
    "A": "refugees",
    "B": "internally displaced persons",
    "C": "asylum seekers awaiting a decision",
    "D": "guest workers",
    "E": "transnational migrants"
   },
   "answer": "B",
   "explanation": "Internally displaced persons (IDPs) are forced to flee their homes but stay inside their own country. These families did not cross an international border, so they are IDPs, not refugees. Refugees have crossed into another country to escape war, violence, or persecution.",
   "whyNot": {
    "A": "Refugees have crossed an international border. These families stayed in their own country.",
    "C": "Asylum seekers have asked another country for protection and are waiting for a decision.",
    "D": "Guest workers choose to move for temporary jobs in another country.",
    "E": "Transnational migrants live in one country while keeping strong ties to another. These families were forced to move within their own country."
   },
   "vocab": [
    "internally displaced persons",
    "refugee",
    "forced migration"
   ]
  },
  {
   "id": "U2-P37",
   "topic": "2.11",
   "lo": "IMP-2.D",
   "skill": "4.B",
   "difficulty": "medium",
   "stimulus": {
    "type": "schematicMap",
    "title": "ONE FAMILY'S MOVES WITHIN COUNTRY W, 1998–2015 (HYPOTHETICAL)",
    "canvas": {
     "width": 800,
     "height": 340
    },
    "features": [
     {
      "kind": "land",
      "name": "",
      "polygon": [
       [
        30,
        30
       ],
       [
        760,
        18
       ],
       [
        782,
        170
       ],
       [
        760,
        322
       ],
       [
        40,
        318
       ],
       [
        18,
        180
       ]
      ],
      "style": "small"
     },
     {
      "kind": "island",
      "name": "Village",
      "center": [
       110,
       255
      ],
      "radius": 9
     },
     {
      "kind": "island",
      "name": "Market town",
      "center": [
       300,
       205
      ],
      "radius": 15
     },
     {
      "kind": "island",
      "name": "Regional city",
      "center": [
       495,
       145
      ],
      "radius": 23
     },
     {
      "kind": "island",
      "name": "Capital city",
      "center": [
       680,
       88
      ],
      "radius": 33
     },
     {
      "kind": "arrow",
      "name": "Move 1 (1998): village to market town",
      "from": [
       122,
       250
      ],
      "to": [
       283,
       211
      ]
     },
     {
      "kind": "arrow",
      "name": "Move 2 (2006): market town to regional city",
      "from": [
       316,
       199
      ],
      "to": [
       470,
       153
      ]
     },
     {
      "kind": "arrow",
      "name": "Move 3 (2015): regional city to capital city",
      "from": [
       519,
       137
      ],
      "to": [
       645,
       98
      ]
     }
    ],
    "legend": [
     {
      "swatch": "small",
      "label": "Country W"
     },
     {
      "swatch": "land",
      "label": "Settlement (larger circle = larger population)"
     }
    ],
    "description": "Map of Country W. Arrows show one family's three moves: from a village to a market town in 1998, from the market town to a regional city in 2006, and from the regional city to the capital city in 2015. Each place is larger than the one before it.",
    "source": "Hypothetical map"
   },
   "stem": "The map shows the moves made by one family over 17 years. Which type of migration does it best illustrate?",
   "options": {
    "A": "Step migration",
    "B": "Chain migration",
    "C": "Transhumance",
    "D": "Forced migration",
    "E": "Transnational migration"
   },
   "answer": "A",
   "explanation": "Step migration means moving in a series of smaller steps, usually from smaller places to bigger ones: village → market town → regional city → capital. Ravenstein noticed this pattern in the 1880s. Each step can give migrants time to save money and get used to city life before the next move.",
   "whyNot": {
    "B": "Chain migration means following relatives or friends who moved earlier. The map shows one family's own moves.",
    "C": "Transhumance is moving herds between seasonal pastures and back again every year.",
    "D": "Nothing on the map shows that the family was forced to move.",
    "E": "Transnational migrants move to another country and keep ties to both. These moves all stay inside Country W."
   },
   "vocab": [
    "step migration",
    "internal migration",
    "rural-to-urban migration"
   ]
  },
  {
   "id": "U2-P38",
   "topic": "2.11",
   "lo": "IMP-2.D",
   "skill": "1.D",
   "difficulty": "medium",
   "stem": "In the early 1900s, a man from a small town in southern Italy moved to Buenos Aires, Argentina. Over the next 20 years, his brothers, cousins, and neighbors followed him, helped by his letters and money, and settled in the same neighborhood. This pattern is best described as",
   "options": {
    "A": "step migration",
    "B": "forced migration",
    "C": "internal migration",
    "D": "chain migration",
    "E": "transhumance"
   },
   "answer": "D",
   "explanation": "Chain migration happens when migrants follow family members or friends who moved before them. The first migrants send information and money and help with housing and jobs, so the next people can move more easily. It explains why people from one place often cluster in one neighborhood, like many Italian families in Buenos Aires.",
   "whyNot": {
    "A": "Step migration is one migrant moving in stages, like village → town → city.",
    "B": "These people chose to move, with help from relatives. That is voluntary migration.",
    "C": "They crossed an ocean to another country. That is international, not internal, migration.",
    "E": "Transhumance is moving with livestock between seasonal pastures."
   },
   "vocab": [
    "chain migration",
    "voluntary migration",
    "international migration"
   ]
  },
  {
   "id": "U2-P39",
   "topic": "2.11",
   "lo": "IMP-2.D",
   "skill": "1.D",
   "difficulty": "medium",
   "stem": "A nurse from the Philippines works in a hospital in Canada. She sends money to her parents in Manila every month, video-calls her family daily, votes in Philippine elections from abroad, and plans to retire in the Philippines. She is best described as",
   "options": {
    "A": "an internally displaced person",
    "B": "an asylum seeker",
    "C": "a step migrant",
    "D": "a refugee",
    "E": "a transnational migrant"
   },
   "answer": "E",
   "explanation": "A transnational migrant lives in one country but keeps strong ties to another: sending money home (remittances), staying in close contact, taking part in politics back home, and often planning to return. Cheap calls, video chats, and air travel make it easier than ever to live 'between' two countries.",
   "whyNot": {
    "A": "IDPs are forced to flee but stay inside their own country.",
    "B": "Asylum seekers are asking for protection from danger. She moved for work.",
    "C": "Step migration is a series of moves from smaller to larger places. Nothing here shows steps.",
    "D": "Refugees flee war, violence, or persecution. She chose to move for a job."
   },
   "vocab": [
    "transnational migration",
    "remittances",
    "voluntary migration"
   ]
  },
  {
   "id": "U2-P40",
   "topic": "2.12",
   "lo": "IMP-2.E",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "PERSONAL REMITTANCES RECEIVED BY SIX COUNTRIES, 2024",
    "columns": [
     "Country",
     "Remittances received (billions of US dollars)",
     "Remittances as a share of GDP (%)"
    ],
    "rows": [
     [
      "India",
      "137.7",
      "3.7"
     ],
     [
      "Mexico",
      "67.9",
      "3.7"
     ],
     [
      "Philippines",
      "40.3",
      "8.7"
     ],
     [
      "Nepal",
      "11.3",
      "26.0"
     ],
     [
      "Tajikistan",
      "6.8",
      "47.2"
     ],
     [
      "Tonga",
      "0.26",
      "39.4"
     ]
    ],
    "description": "Table of personal remittances received in 2024 by India, Mexico, the Philippines, Nepal, Tajikistan, and Tonga, in billions of US dollars and as a percent of each country's GDP.",
    "source": "World Bank, World Development Indicators: personal remittances, received (current US$) (BX.TRF.PWKR.CD.DT) and personal remittances, received (% of GDP) (BX.TRF.PWKR.DT.GD.ZS), 2024 values, accessed November 8, 2026."
   },
   "stem": "Which of the following conclusions is best supported by the table?",
   "options": {
    "A": "India depends more on remittances than Nepal does, because India receives more money.",
    "B": "The countries with the largest populations depend most heavily on remittances.",
    "C": "The countries that receive the most remittance money depend on it least as a share of GDP.",
    "D": "Tonga's remittances are too small to matter much compared with the size of its economy.",
    "E": "Remittances make up a larger share of the economy in the Philippines than in Nepal."
   },
   "answer": "C",
   "explanation": "Look at both columns. India and Mexico receive the most money ($137.7 billion and $67.9 billion), but their economies are so big that remittances are only about 3.7% of their GDP. Smaller economies like Tajikistan (47.2%), Tonga (39.4%), and Nepal (26.0%) get far less money, yet it makes up a big part of their economies. For those countries, a recession in the places where their migrants work can hurt the whole country.",
   "whyNot": {
    "A": "Remittances are 26.0% of Nepal's GDP but only 3.7% of India's, so Nepal depends on them more.",
    "B": "India has the largest population in the table but the smallest share (3.7%, tied with Mexico).",
    "D": "Tonga's remittances are only $0.26 billion, but that equals 39.4% of its GDP.",
    "E": "Remittances are 8.7% of GDP in the Philippines and 26.0% in Nepal."
   },
   "vocab": [
    "remittances",
    "gross domestic product (GDP)",
    "effects of migration"
   ]
  },
  {
   "id": "U2-P41",
   "topic": "2.12",
   "lo": "IMP-2.E",
   "skill": "2.C",
   "difficulty": "medium",
   "stem": "Over 20 years, many doctors and nurses trained in Country D move to higher-income countries for better pay. Which of the following is the most likely effect on Country D?",
   "options": {
    "A": "A shortage of health-care workers after Country D paid to train them",
    "B": "A surplus of doctors that lowers wages for health-care workers in Country D",
    "C": "A brain gain that increases the number of medical specialists in Country D",
    "D": "A sharp rise in Country D's birth rate as more young adults stay at home",
    "E": "A drop in the money that families in Country D receive from relatives abroad"
   },
   "answer": "A",
   "explanation": "This is brain drain: highly educated, skilled people emigrate. Country D spent money training these doctors and nurses, but now other countries benefit from their skills. Patients in Country D may face longer waits and fewer clinics. Migrants may send money home, which helps some families, but it does not replace the lost health workers.",
   "whyNot": {
    "B": "Doctors are leaving, so there would be fewer, not more.",
    "C": "A brain gain happens in the countries that receive the doctors, not in Country D.",
    "D": "The people leaving are young adults, so this would tend to lower, not raise, births at home.",
    "E": "Migrants working abroad usually send MORE money home, not less."
   },
   "vocab": [
    "brain drain",
    "remittances",
    "effects of migration"
   ]
  },
  {
   "id": "U2-P42",
   "topic": "2.12",
   "lo": "IMP-2.E",
   "skill": "1.B",
   "difficulty": "medium",
   "stem": "Which of the following is the best example of a political effect of migration?",
   "options": {
    "A": "Restaurants serving migrants' home cooking open in a destination city's downtown.",
    "B": "A party in a destination country wins seats by promising to limit immigration.",
    "C": "Migrants send home money that pays for new houses in their home villages.",
    "D": "Children of migrants grow up speaking both their parents' language and the local one.",
    "E": "A destination country's construction industry fills jobs with migrant workers."
   },
   "answer": "B",
   "explanation": "Political effects involve laws, governments, voting, and power. When migration becomes a big election issue, parties can gain or lose seats because of their immigration plans, and governments may change border and citizenship laws. Migration also has economic effects (jobs, remittances) and cultural effects (food, language, religion).",
   "whyNot": {
    "A": "New restaurants are a cultural (and economic) effect: the spread of food traditions.",
    "C": "Money sent home (remittances) is an economic effect.",
    "D": "Children who speak two languages is a cultural effect.",
    "E": "Filling jobs with migrant workers is an economic effect."
   },
   "vocab": [
    "effects of migration",
    "political effects",
    "cultural effects"
   ]
  }
 ],
 "exam": {
  "title": "Unit 2 Practice Exam: Population and Migration Patterns and Processes",
  "timeMinutes": 25,
  "questionCount": 25,
  "directions": "Each of the questions or incomplete statements below is followed by five suggested answers or completions. Select the one that is best in each case. Your score is based only on the number of questions answered correctly, so answer every question. Work quickly without losing accuracy, and come back to any question you skipped if time allows.",
  "stimulusCount": 10,
  "questions": [
   {
    "id": "U2-E01",
    "n": 1,
    "topic": "2.1",
    "lo": "PSO-2.A",
    "skill": "2.B",
    "difficulty": "medium",
    "stem": "Most of Russia's people live west of the Ural Mountains, even though most of Russia's land lies east of them. Which of the following best explains this distribution?",
    "options": {
     "A": "Russia's government has banned permanent settlement in Siberia ever since the Soviet era.",
     "B": "Most of Russia's oil and natural gas fields are located west of the Ural Mountains.",
     "C": "The west has a milder climate and a longer history of farming, cities, and trade links.",
     "D": "Eastern Russia is mostly hot desert that gets too little rain to support farming.",
     "E": "The Ural Mountains are so high and rugged that few settlers have ever crossed them."
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. Russia has not banned settlement east of the Urals. The Soviet Union actually encouraged people to settle and work in Siberia, where cities such as Novosibirsk grew.",
     "B": "Incorrect. Much of Russia's oil and natural gas comes from western Siberia, east of the Urals, so resource location does not explain the pattern.",
     "C": "Correct. Physical factors (a milder climate and longer growing season in the west, compared with long, severe winters and permafrost across much of Siberia) combine with human factors (centuries of farming, city growth, industry, and transportation links to the rest of Europe) to concentrate Russia's population west of the Urals.",
     "D": "Incorrect. Most of Siberia and the Russian Far East is cold forest (taiga) and tundra, not hot desert. Cold, not heat, limits settlement there.",
     "E": "Incorrect. The Urals are relatively low, old mountains, and roads and the Trans-Siberian Railway cross them. They are not a major barrier to settlement."
    },
    "explanation": "Western Russia is warmer and has a longer growing season, so farms and cities grew there first, and it is closer to the rest of Europe for trade. Most of Siberia has long, very cold winters and frozen ground (permafrost). Both physical factors (climate) and human factors (history, economics, transportation) explain where people live."
   },
   {
    "id": "U2-E02",
    "n": 2,
    "topic": "2.2",
    "lo": "PSO-2.D",
    "skill": "1.B",
    "difficulty": "medium",
    "stem": "A children's hospital that specializes in rare cancers is far more likely to be located in a large, densely populated metropolitan area than in a sparsely populated rural county. Which of the following best explains this pattern?",
    "options": {
     "A": "A specialized hospital needs a large number of possible patients within reach to keep operating.",
     "B": "Rural counties have higher physiological densities, which leaves little land for large hospitals.",
     "C": "Land in rural counties costs more than in metropolitan areas, which makes hospitals too costly to build.",
     "D": "National laws in most countries forbid hospitals from being built outside large cities.",
     "E": "Children in metropolitan areas are far more likely than rural children to develop cancer."
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. Population density affects the provision of services. A highly specialized hospital needs many patients, doctors, and researchers to operate, so it locates where large numbers of people live within reach, and patients from sparsely populated rural areas travel to it.",
     "B": "Incorrect. Physiological density compares people with farmland. Sparsely populated rural counties usually have more land per person, not less, so a shortage of land is not the reason.",
     "C": "Incorrect. Land is usually cheaper in rural counties, where demand for it is lower.",
     "D": "Incorrect. Rural hospitals and clinics exist in many countries; no general law limits hospitals to large cities.",
     "E": "Incorrect. The hospital's location is explained by the number of patients who can reach it, not by a higher cancer rate among city children."
    },
    "explanation": "Expensive, specialized services need lots of patients or customers nearby. A big metro area has enough people to keep a specialty hospital busy. A sparse rural county does not, so families travel to the city. This is how population density shapes services like medical care."
   },
   {
    "id": "U2-E03",
    "n": 3,
    "set": "pyrA",
    "topic": "2.3",
    "lo": "PSO-2.F",
    "skill": "3.B",
    "difficulty": "easy",
    "stimulus": {
     "type": "pyramid",
     "title": "POPULATION PYRAMID, COUNTRY A, 2025 (HYPOTHETICAL DATA)",
     "ageGroups": [
      "0–4",
      "5–9",
      "10–14",
      "15–19",
      "20–24",
      "25–29",
      "30–34",
      "35–39",
      "40–44",
      "45–49",
      "50–54",
      "55–59",
      "60–64",
      "65–69",
      "70–74",
      "75–79",
      "80+"
     ],
     "male": [
      8.1,
      7.2,
      6.4,
      5.5,
      4.6,
      3.9,
      3.2,
      2.6,
      2.1,
      1.7,
      1.4,
      1.1,
      0.8,
      0.6,
      0.4,
      0.3,
      0.2
     ],
     "female": [
      7.9,
      7.0,
      6.2,
      5.4,
      4.6,
      3.8,
      3.2,
      2.7,
      2.2,
      1.8,
      1.4,
      1.1,
      0.9,
      0.7,
      0.5,
      0.3,
      0.2
     ],
     "description": "Population pyramid for Country A with 17 five-year age groups, from 0–4 at the bottom to 80+ at the top. Males are on the left and females on the right; bar length is the percent of the total population.",
     "source": "Hypothetical data"
    },
    "stem": "Which of the following best describes the population of Country A shown in the pyramid?",
    "options": {
     "A": "It is aging, because older adults make up the largest share of the population.",
     "B": "It is shrinking, because each new group of children is smaller than the one before.",
     "C": "It is stable, because each age group is about the same size as the one above it.",
     "D": "It is young and growing quickly, because a large share of the population is under 15.",
     "E": "It has a high dependency ratio, mainly because so many people are 65 or older."
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. People 65 and older are only about 3 percent of Country A's population; the top of the pyramid is very narrow.",
     "B": "Incorrect. A shrinking population would have a base narrower than the bars above it. Country A's base is its widest bar.",
     "C": "Incorrect. A stable (stationary) population has bars of similar size, like a column. Country A's bars shrink steadily with age.",
     "D": "Correct. The wide base shows that about 43 percent of the population is under age 15. This expansive pyramid signals high birth rates and rapid growth, because many young people will soon reach childbearing age.",
     "E": "Incorrect. Country A's dependency ratio is high, but because of its many children; people 65 and older are only about 3 percent of the population."
    },
    "explanation": "A wide bottom and a narrow top = an expansive pyramid. About 43% of Country A's people are under 15, and only about 3% are 65 or older. Lots of children today means lots of future parents, so the population will keep growing fast."
   },
   {
    "id": "U2-E04",
    "n": 4,
    "set": "pyrA",
    "topic": "2.5",
    "lo": "IMP-2.B",
    "skill": "3.C",
    "difficulty": "medium",
    "stem": "Country A's crude birth rate has stayed near 40 per 1,000 since 1980, while its crude death rate has fallen from 20 to 9 per 1,000. Based on this information and the pyramid, Country A is most likely in which stage of the demographic transition model?",
    "options": {
     "A": "Stage 1, because its birth and death rates are both high",
     "B": "Stage 2, because births stay high while deaths have fallen",
     "C": "Stage 3, because its birth rate is dropping toward its death rate",
     "D": "Stage 4, because its birth and death rates are both low",
     "E": "Stage 5, because its death rate is higher than its birth rate"
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. In Stage 1 both rates are high, but Country A's death rate has fallen to 9 per 1,000, which is low.",
     "B": "Correct. A high, steady birth rate (about 40 per 1,000) combined with a sharply falling death rate is the signature of Stage 2. The widening gap between births and deaths produces rapid natural increase, which matches the pyramid's wide base.",
     "C": "Incorrect. In Stage 3 the birth rate falls, but Country A's birth rate has stayed near 40 per 1,000.",
     "D": "Incorrect. Country A's birth rate is high, and its wide-based pyramid shows many young people.",
     "E": "Incorrect. Country A's birth rate is far higher than its death rate, so its population is growing, not shrinking."
    },
    "explanation": "Stage 2 = deaths drop, births stay high, and the population booms. Country A's death rate fell from 20 to 9, but its birth rate stayed near 40. That big gap is why the pyramid has such a wide base."
   },
   {
    "id": "U2-E05",
    "n": 5,
    "set": "pyrA",
    "topic": "2.8",
    "lo": "SPS-2.B",
    "skill": "2.C",
    "difficulty": "medium",
    "stem": "Which of the following changes would most likely lower Country A's total fertility rate over the next several decades?",
    "options": {
     "A": "Lowering the minimum legal age at which women are allowed to marry",
     "B": "Expanding government cash programs that reward families for each additional child",
     "C": "Increasing the share of the workforce employed in subsistence farming",
     "D": "Reducing the number of clinics and midwives that serve rural villages",
     "E": "Expanding girls' schooling and women's access to health care and contraception"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. Earlier marriage usually means women begin having children earlier, which tends to raise fertility.",
     "B": "Incorrect. Rewards for each additional child are pronatalist incentives designed to raise fertility.",
     "C": "Incorrect. Farm families often rely on children's labor, so a larger farming workforce is associated with higher fertility.",
     "D": "Incorrect. Fewer clinics would likely raise infant and child deaths; where child deaths are high, families tend to have more children.",
     "E": "Correct. As the AP course framework notes, access to education, employment, health care, and contraception has reduced fertility rates in most parts of the world. Women with more schooling tend to marry later, work outside the home, and choose smaller families."
    },
    "explanation": "When girls stay in school longer, they usually marry later and have fewer children. When women can get health care and contraception, they can choose when and how many children to have, and more babies survive, so families do not need as many births. This is how changing roles for women lower fertility."
   },
   {
    "id": "U2-E06",
    "n": 6,
    "topic": "2.4",
    "lo": "IMP-2.A",
    "skill": "1.D",
    "difficulty": "medium",
    "stem": "Country R has a crude birth rate of 26 per 1,000 and a crude death rate of 6 per 1,000. If these rates stay the same and there is no migration, about how many years will it take Country R's population to double?",
    "options": {
     "A": "About 3.5 years",
     "B": "About 20 years",
     "C": "About 35 years",
     "D": "About 70 years",
     "E": "About 140 years"
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. This divides 70 by 20 without first converting 20 per 1,000 into a percentage (2.0 percent).",
     "B": "Incorrect. This treats the natural increase of 20 per 1,000 as a number of years.",
     "C": "Correct. The rate of natural increase is (26 − 6) ÷ 10 = 2.0 percent. Using the rule of 70, the doubling time is 70 ÷ 2.0 = 35 years.",
     "D": "Incorrect. A doubling time of 70 years matches a growth rate of 1.0 percent, half of Country R's rate.",
     "E": "Incorrect. This multiplies 70 by 2.0 instead of dividing 70 by 2.0."
    },
    "explanation": "Two steps. 1) RNI = (26 − 6) ÷ 10 = 2.0%. 2) Rule of 70: 70 ÷ 2.0 = 35 years."
   },
   {
    "id": "U2-E07",
    "n": 7,
    "topic": "2.4",
    "lo": "IMP-2.A",
    "skill": "3.F",
    "difficulty": "hard",
    "stem": "In 2024, Japan's crude death rate was about 13 deaths per 1,000 people, while Niger's was about 9 per 1,000. Japan has one of the highest life expectancies in the world. Which of the following best explains why Japan's crude death rate is higher?",
    "options": {
     "A": "The crude death rate does not adjust for age, and Japan has a far larger share of older adults.",
     "B": "Japan's health-care system is less effective than Niger's at treating infectious diseases.",
     "C": "Niger's infant mortality rate is lower than Japan's, so fewer babies die in Niger each year.",
     "D": "Many older adults leave Niger to retire in other countries, which lowers Niger's death count.",
     "E": "Japan has a larger total population than Niger, so it records a higher number of deaths."
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. The crude death rate counts all deaths per 1,000 people without adjusting for age structure. Japan's population is very old (about 3 in 10 people are 65 or older), while Niger's is very young, so Japan records more deaths per 1,000 people even though people in Japan live much longer. This is a limitation of the crude death rate.",
     "B": "Incorrect. Japan has a strong health-care system and very few deaths from infectious disease; its life expectancy is far higher than Niger's.",
     "C": "Incorrect. Niger's infant mortality rate is much higher than Japan's.",
     "D": "Incorrect. Retirement migration is not what keeps Niger's crude death rate low; its very young age structure is.",
     "E": "Incorrect. A crude death rate is a rate per 1,000 people, so it already accounts for total population size."
    },
    "explanation": "The crude death rate is just deaths per 1,000 people. It does not care how old the people are. Japan has lots of elderly people, and older people are more likely to die each year, even with great health care. Niger has mostly children and young adults. So Japan's crude death rate is higher even though people in Japan live much longer."
   },
   {
    "id": "U2-E08",
    "n": 8,
    "topic": "2.6",
    "lo": "IMP-2.B",
    "skill": "1.C",
    "difficulty": "hard",
    "stem": "Which of the following best describes how Esther Boserup's view of population growth differs from Thomas Malthus's view?",
    "options": {
     "A": "Boserup argued that food supply grows geometrically, while Malthus argued it grows arithmetically.",
     "B": "Boserup agreed that famine would limit population growth but predicted it would happen sooner.",
     "C": "Boserup argued that industrialization causes population growth, while Malthus blamed farming.",
     "D": "Boserup argued that population growth would damage the environment, not just the food supply.",
     "E": "Boserup argued that population pressure pushes farmers to farm more intensively and raise output."
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. Boserup did not simply reverse Malthus's growth curves; she argued that population pressure itself leads to changes in farming methods.",
     "B": "Incorrect. Boserup was a critic of Malthus; she did not predict earlier famine.",
     "C": "Incorrect. The two disagreed about how food production responds to population growth, not about what causes population growth.",
     "D": "Incorrect. Concern about resource depletion and environmental damage beyond food is associated with neo-Malthusians, not with Boserup.",
     "E": "Correct. Boserup argued that as population grows, farmers respond by intensifying production (for example, shortening fallow periods, adding labor, irrigating, and adopting new tools), so food output can rise along with population. Malthus argued that food supply could not keep pace."
    },
    "explanation": "Malthus: more people → not enough food → famine. Boserup: more people → farmers work the land harder and smarter (more labor, less time leaving fields empty, irrigation, new tools) → more food. She saw population growth as a cause of change in farming, not just a problem."
   },
   {
    "id": "U2-E09",
    "n": 9,
    "topic": "2.7",
    "lo": "SPS-2.A",
    "skill": "2.D",
    "difficulty": "medium",
    "stem": "In the 1970s, Singapore's government urged families to \"Stop at Two.\" In 1987, it began urging families who could afford it to have three or more children and offered incentives for larger families. Which of the following best explains this change?",
    "options": {
     "A": "Singapore's death rate rose sharply in the 1980s, so more births were needed to replace deaths.",
     "B": "Once fertility fell below replacement, the government moved from antinatalist to pronatalist policy.",
     "C": "International agreements required Singapore to raise its birth rate to ease global labor shortages.",
     "D": "Singapore's population was growing too fast, so the government wanted larger, more stable families.",
     "E": "The government shifted from pronatalist to antinatalist policy in order to slow population growth."
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. Singapore's death rate was low in the 1980s; the concern was that births had fallen too far.",
     "B": "Correct. \"Stop at Two\" was an antinatalist campaign. After Singapore's total fertility rate fell below replacement level (about 2.1) by the late 1970s (about 1.8 in 1977), the government grew concerned about an aging population and future labor shortages, so it switched to pronatalist incentives.",
     "C": "Incorrect. Population policies like these are set by national governments for national goals, not required by international agreements.",
     "D": "Incorrect. Encouraging larger families would speed up population growth, not slow it.",
     "E": "Incorrect. The order is reversed: Singapore moved from an antinatalist policy (\"Stop at Two\") to a pronatalist one (three or more)."
    },
    "explanation": "First Singapore wanted FEWER births (antinatalist: \"Stop at Two\"). Fertility fell below replacement level (about 2.1 children per woman). Then the government worried about too few future workers and too many older people, so it flipped to pronatalist: encouraging families who could afford it to have three or more children."
   },
   {
    "id": "U2-E10",
    "n": 10,
    "set": "pyrB",
    "topic": "2.9",
    "lo": "SPS-2.C",
    "skill": "3.B",
    "difficulty": "medium",
    "stimulus": {
     "type": "pyramid",
     "title": "POPULATION PYRAMID, COUNTRY B, 2025 (HYPOTHETICAL DATA)",
     "ageGroups": [
      "0–4",
      "5–9",
      "10–14",
      "15–19",
      "20–24",
      "25–29",
      "30–34",
      "35–39",
      "40–44",
      "45–49",
      "50–54",
      "55–59",
      "60–64",
      "65–69",
      "70–74",
      "75–79",
      "80+"
     ],
     "male": [
      1.8,
      2.0,
      2.2,
      2.3,
      2.5,
      2.6,
      2.8,
      3.0,
      3.2,
      3.8,
      4.0,
      3.8,
      3.5,
      3.1,
      2.9,
      2.3,
      2.6
     ],
     "female": [
      1.7,
      1.9,
      2.1,
      2.2,
      2.3,
      2.5,
      2.7,
      2.9,
      3.2,
      3.8,
      4.1,
      3.9,
      3.7,
      3.5,
      3.4,
      3.1,
      4.6
     ],
     "description": "Population pyramid for Country B with 17 five-year age groups, from 0–4 at the bottom to 80+ at the top. Males are on the left and females on the right; bar length is the percent of the total population.",
     "source": "Hypothetical data"
    },
    "stem": "Which of the following conclusions is best supported by Country B's population pyramid?",
    "options": {
     "A": "Country B's birth rate has risen steadily over the past 25 years.",
     "B": "Country B's population is young, with most people under age 30.",
     "C": "Country B has more males than females in its oldest age groups.",
     "D": "Country B has more people aged 65 and older than children under 15.",
     "E": "Country B's death rates are much higher for women than for men."
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Each of the youngest age groups is smaller than the one above it, so births have been falling, not rising.",
     "B": "Incorrect. The largest age groups are people in their 40s, 50s, and 60s, and people under 30 are only about one-quarter of the population.",
     "C": "Incorrect. In the 80+ group, the female bar is much longer than the male bar.",
     "D": "Correct. About one-quarter of Country B's population is 65 or older, compared with about 12 percent under age 15. A pyramid that is narrow at the base and wide near the top signals decades of low fertility and long life expectancy, which together produce an aging population.",
     "E": "Incorrect. More women than men survive to old age, which shows that women's death rates are lower, not higher."
    },
    "explanation": "Add up the bars: about a quarter of Country B's people are 65 or older, but only about 12% are under 15. A narrow base and a wide top mean few babies and many older people. That is an aging population."
   },
   {
    "id": "U2-E11",
    "n": 11,
    "set": "pyrB",
    "topic": "2.9",
    "lo": "SPS-2.C",
    "skill": "3.E",
    "difficulty": "medium",
    "stem": "If the trends shown in the pyramid continue, which of the following is most likely to happen in Country B over the next 20 years?",
    "options": {
     "A": "Its working-age population will shrink as retirees increase, straining pensions.",
     "B": "Its dependency ratio will fall as large numbers of children reach working age.",
     "C": "It will need many more elementary schools to serve a growing number of young children.",
     "D": "Its crude death rate will fall as the large middle-aged groups grow older.",
     "E": "Its labor force will grow quickly as many young adults enter the job market."
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. The large groups now aged 45–64 will move into retirement over the next 20 years, while much smaller groups replace them in the workforce. Fewer workers supporting more retirees raises the dependency ratio and strains pension and health-care systems.",
     "B": "Incorrect. The child age groups are the smallest in the pyramid, so few people will enter the workforce, and the dependency ratio will most likely rise.",
     "C": "Incorrect. The base of the pyramid is narrow and shrinking, so the number of children is falling.",
     "D": "Incorrect. As the large middle-aged groups grow older, more people will reach ages with high death rates, so the crude death rate will likely rise.",
     "E": "Incorrect. The groups entering the job market (today's 0- to 19-year-olds) are small, so the labor force will likely shrink."
    },
    "explanation": "The biggest groups in Country B are in their 40s, 50s, and 60s. In 20 years most of them will be retired. The groups that replace them as workers are much smaller. Fewer workers paying taxes and more retirees collecting pensions and needing health care = pressure on the system."
   },
   {
    "id": "U2-E12",
    "n": 12,
    "topic": "2.7",
    "lo": "SPS-2.A",
    "skill": "2.C",
    "difficulty": "hard",
    "stem": "Country J's total fertility rate is 1.3, and its working-age population has begun to shrink. Which policy would most quickly increase the number of working-age people in Country J?",
    "options": {
     "A": "Offering a large cash bonus to parents for each child born in the next five years",
     "B": "Expanding free access to contraception and family-planning services",
     "C": "Admitting more immigrants aged 20 to 40 through new work visas",
     "D": "Lowering the age at which workers can retire with a full pension",
     "E": "Raising the minimum age at which young people may leave school"
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. Even if a pronatalist bonus raised births, babies born now would not reach working age for 15 to 20 years.",
     "B": "Incorrect. Family-planning services tend to lower birth rates, which would shrink future working-age groups even more.",
     "C": "Correct. Of the policies listed, only admitting working-age immigrants adds people to the 15–64 age groups right away. Immigration policy can change a population's size and composition quickly, which is why many low-fertility countries use immigration to address labor shortages.",
     "D": "Incorrect. Retirement age does not change how many people are aged 15 to 64, and earlier retirement would reduce the number of people actually working.",
     "E": "Incorrect. School-leaving age does not change how many people are of working age; it only delays young people's entry into the workforce."
    },
    "explanation": "Babies take about 20 years to grow into workers, so pronatalist bonuses are slow. Immigrants who are already 20 to 40 years old join the working-age group the day they arrive. That is why countries with very low fertility often use immigration to fill jobs."
   },
   {
    "id": "U2-E13",
    "n": 13,
    "topic": "2.3",
    "lo": "PSO-2.E",
    "skill": "5.B",
    "difficulty": "medium",
    "stem": "Country L's national sex ratio is about 100. However, in a remote mining region of Country L, the sex ratio for people aged 20 to 49 is about 160. Which of the following best explains the difference between these two scales?",
    "options": {
     "A": "Women in the mining region have much longer life expectancies than women in other regions.",
     "B": "The national sex ratio is calculated differently from a regional sex ratio.",
     "C": "Most babies born in the mining region are girls, which lowers the regional sex ratio.",
     "D": "Women from across Country L move to the mining region to take mining jobs.",
     "E": "Mining jobs attract young men from other regions, many of whom move without families."
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. Longer-lived women would increase the number of women, which would lower the sex ratio, not raise it.",
     "B": "Incorrect. Sex ratio is calculated the same way at every scale: males per 100 females.",
     "C": "Incorrect. More girls would lower the sex ratio, but a ratio of 160 means far more males than females.",
     "D": "Incorrect. If many women moved in, the regional sex ratio would fall below 100, not rise to 160.",
     "E": "Correct. A sex ratio of 160 means about 160 men for every 100 women. Migration for jobs filled mostly by men, such as mining, concentrates young men in one region. At the national scale this local imbalance is averaged out, which shows that sex-ratio patterns vary with the scale of analysis."
    },
    "explanation": "Sex ratio = males per 100 females, so 160 means 160 men for every 100 women. Remote mining jobs draw lots of young men who come to work, often leaving families at home. When you look at the whole country, this one region is averaged in with everyone else, so the national number stays near 100."
   },
   {
    "id": "U2-E14",
    "n": 14,
    "topic": "2.8",
    "lo": "SPS-2.B",
    "skill": "2.B",
    "difficulty": "medium",
    "stem": "The average total fertility rate in Latin America and the Caribbean fell from about 5.2 children per woman in 1970 to about 1.9 in 2020. Which of the following best explains this decline?",
    "options": {
     "A": "Governments across the region adopted one-child policies modeled on China's policy.",
     "B": "As cities grew, women gained more schooling, paid work, and access to contraception.",
     "C": "Rising infant mortality led families to put off having children until conditions improved.",
     "D": "Most young women emigrated from the region, leaving few women of childbearing age.",
     "E": "Farming became the main source of jobs, so families needed fewer children to help."
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. Latin American governments did not adopt one-child policies; the decline came mainly from social and economic change.",
     "B": "Correct. As the region urbanized, more women stayed in school longer, worked outside the home, and gained access to health care and contraception. As the AP course framework notes, these changes in women's roles have reduced fertility rates in most parts of the world.",
     "C": "Incorrect. Infant mortality fell, not rose, across the region during these decades.",
     "D": "Incorrect. Emigration from the region was large, but most women of childbearing age stayed. The total fertility rate measures births per woman, not the number of women.",
     "E": "Incorrect. The region urbanized rapidly, and the share of workers in farming fell. Farm families also tend to have more children, not fewer."
    },
    "explanation": "In 50 years, the average number of children per woman in Latin America dropped from about 5 to under 2. As people moved to cities, girls stayed in school longer, more women took paid jobs, and birth control became easier to get. Those changes in women's lives led families to have fewer children."
   },
   {
    "id": "U2-E15",
    "n": 15,
    "topic": "2.11",
    "lo": "IMP-2.D",
    "skill": "1.D",
    "difficulty": "easy",
    "stem": "A journalist receives threats after reporting on government corruption. She flies to another country and applies for protection there. Her application has not yet been decided. She is best described as",
    "options": {
     "A": "an internally displaced person",
     "B": "a guest worker",
     "C": "an economic migrant",
     "D": "an asylum seeker",
     "E": "a step migrant"
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Internally displaced persons flee their homes but remain inside their own country; the journalist crossed an international border.",
     "B": "Incorrect. Guest workers move by choice for temporary jobs, usually through a labor program.",
     "C": "Incorrect. She left because of threats to her safety, not mainly to find a job or higher wages.",
     "D": "Correct. An asylum seeker is a person who has fled to another country and asked for protection but whose claim has not yet been decided. If her claim is approved, she may be granted refugee status.",
     "E": "Incorrect. Step migration is a series of moves from smaller to larger places; she made one move to escape danger."
    },
    "explanation": "Asylum seeker = someone who fled to another country, asked for protection, and is still waiting for an answer. If the answer is yes, she may become a recognized refugee. If she had fled but stayed inside her own country, she would be an internally displaced person."
   },
   {
    "id": "U2-E16",
    "n": 16,
    "set": "dtmM",
    "topic": "2.5",
    "lo": "IMP-2.B",
    "skill": "3.B",
    "difficulty": "medium",
    "stimulus": {
     "type": "line",
     "title": "CRUDE BIRTH AND DEATH RATES, COUNTRY M, 1800–2025 (HYPOTHETICAL DATA)",
     "xLabel": "Year",
     "yLabel": "Rate per 1,000 people",
     "categories": [
      "1800",
      "1825",
      "1850",
      "1875",
      "1900",
      "1925",
      "1950",
      "1975",
      "2000",
      "2025"
     ],
     "series": [
      {
       "name": "Crude birth rate",
       "values": [
        38,
        38,
        38,
        37,
        34,
        28,
        21,
        15,
        12,
        11
       ]
      },
      {
       "name": "Crude death rate",
       "values": [
        36,
        35,
        29,
        23,
        18,
        14,
        11,
        10,
        9,
        9
       ]
      }
     ],
     "yMax": 40,
     "description": "Line graph of Country M's crude birth rate and crude death rate, per 1,000 people, from 1800 to 2025. Points are every 25 years.",
     "source": "Hypothetical data"
    },
    "stem": "During which period was Country M most clearly in Stage 2 of the demographic transition model?",
    "options": {
     "A": "1800 to 1825",
     "B": "1825 to 1875",
     "C": "1900 to 1950",
     "D": "1950 to 1975",
     "E": "2000 to 2025"
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. From 1800 to 1825, birth and death rates were both high (35 to 38 per 1,000) and close together, with little natural increase: Stage 1.",
     "B": "Correct. From 1825 to 1875, the death rate fell from 35 to 23 per 1,000 while the birth rate stayed near 37 to 38. A falling death rate with a high, steady birth rate defines Stage 2, and natural increase rose from 0.3 percent to 1.4 percent a year.",
     "C": "Incorrect. From 1900 to 1950, the birth rate fell steeply (34 to 21) while the death rate fell more slowly: Stage 3.",
     "D": "Incorrect. From 1950 to 1975, the birth rate was still falling toward an already low death rate, which is late Stage 3.",
     "E": "Incorrect. From 2000 to 2025, both rates were low and close together: Stage 4."
    },
    "explanation": "Stage 2 = the death rate drops while the birth rate stays high. On the graph, that happens from 1825 to 1875: deaths fall from 35 to 23, but births stay around 37 to 38. The gap between the lines gets wider, so the population grows faster."
   },
   {
    "id": "U2-E17",
    "n": 17,
    "set": "dtmM",
    "topic": "2.5",
    "lo": "IMP-2.B",
    "skill": "1.B",
    "difficulty": "medium",
    "stem": "Which of the following best explains the decline in Country M's crude death rate between 1825 and 1925?",
    "options": {
     "A": "A rise in deaths from heart disease and cancer as people lived longer",
     "B": "A drop in the birth rate that reduced the number of infants who died",
     "C": "An increase in the share of older adults in Country M's population",
     "D": "Large-scale emigration of the oldest and sickest residents",
     "E": "Better sanitation, cleaner water, and a more reliable food supply"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. A shift toward chronic diseases such as heart disease and cancer happens after deaths from infectious disease have fallen; it does not by itself lower the death rate.",
     "B": "Incorrect. The death rate began falling around 1825, while the birth rate stayed high until about 1875, so falling births cannot be the main cause; the decline came from fewer deaths from disease and hunger.",
     "C": "Incorrect. A larger share of older adults would tend to raise the crude death rate, not lower it.",
     "D": "Incorrect. Most migrants are young adults; emigration of the old and sick is not a typical cause of falling death rates.",
     "E": "Correct. According to the epidemiological transition, death rates fall as improvements in sanitation, clean water, nutrition, and later medicine reduce deaths from infectious and parasitic diseases and from famine."
    },
    "explanation": "Death rates drop first because fewer people die young from infections and hunger. Clean water, sewers, better food, and later vaccines and medicine stop diseases like cholera. This is the epidemiological transition, and it explains Stage 2 of the DTM."
   },
   {
    "id": "U2-E18",
    "n": 18,
    "topic": "2.10",
    "lo": "IMP-2.C",
    "skill": "1.D",
    "difficulty": "medium",
    "stem": "Migrants from Country P hoping to reach jobs in Country Q must cross a wide desert and pass through Country S, which requires a transit visa that is expensive and slow to obtain. The desert and the visa requirement are best described as",
    "options": {
     "A": "pull factors",
     "B": "push factors",
     "C": "intervening obstacles",
     "D": "intervening opportunities",
     "E": "examples of distance decay"
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. Pull factors attract migrants to a destination, such as the jobs in Country Q.",
     "B": "Incorrect. Push factors are conditions at the origin that make people want to leave Country P.",
     "C": "Correct. Intervening obstacles are barriers between the origin and the destination that make migration harder. The desert is an environmental obstacle, and the costly transit visa is a political obstacle.",
     "D": "Incorrect. Intervening opportunities are attractive options along the way that lead migrants to stop before reaching their destination.",
     "E": "Incorrect. Distance decay describes how interaction declines as distance increases; the desert and the visa rule are specific barriers along the route."
    },
    "explanation": "Intervening obstacles are things in the way between home and the destination. A desert is a physical (environmental) obstacle. A hard-to-get visa is a political obstacle. Obstacles do not make people want to leave or want to go; they make the trip harder."
   },
   {
    "id": "U2-E19",
    "n": 19,
    "topic": "2.1",
    "lo": "PSO-2.B",
    "skill": "1.D",
    "difficulty": "medium",
    "stem": "Country X has 60 million people and 400,000 square kilometers of land. Fifteen percent of its land is arable, and 24 million of its people work as farmers. What is Country X's physiological density?",
    "options": {
     "A": "60 people per square kilometer",
     "B": "150 people per square kilometer",
     "C": "400 people per square kilometer",
     "D": "1,000 people per square kilometer",
     "E": "10,000 people per square kilometer"
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. This divides the number of farmers (24 million) by all land (400,000 square kilometers), which is not a standard density measure.",
     "B": "Incorrect. 150 is the arithmetic density: 60 million people ÷ 400,000 square kilometers of total land.",
     "C": "Incorrect. 400 is the agricultural density: 24 million farmers ÷ 60,000 square kilometers of arable land.",
     "D": "Correct. Arable land = 15 percent of 400,000 = 60,000 square kilometers. Physiological density = 60 million people ÷ 60,000 square kilometers = 1,000 people per square kilometer of arable land.",
     "E": "Incorrect. This results from treating 1.5 percent, rather than 15 percent, of the land as arable."
    },
    "explanation": "Physiological density = ALL people ÷ ARABLE land. Arable land: 15% × 400,000 = 60,000 sq km. Then 60,000,000 ÷ 60,000 = 1,000 people per sq km of farmland. (Arithmetic density uses all land; agricultural density counts only farmers.)"
   },
   {
    "id": "U2-E20",
    "n": 20,
    "topic": "2.11",
    "lo": "IMP-2.D",
    "skill": "1.A",
    "difficulty": "easy",
    "stem": "Each spring, herders in the Alps move their cattle up to high mountain pastures, and each fall they bring the herds back down to valley farms. This seasonal movement is called",
    "options": {
     "A": "transhumance",
     "B": "step migration",
     "C": "chain migration",
     "D": "rural-to-urban migration",
     "E": "forced migration"
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. Transhumance is the seasonal movement of herders and livestock between highland summer pastures and lowland winter pastures. It is one of the types of voluntary migration in the AP course framework.",
     "B": "Incorrect. Step migration is a series of moves, usually toward larger places, that does not repeat every year.",
     "C": "Incorrect. Chain migration is following relatives or friends who moved earlier.",
     "D": "Incorrect. The herders move between pastures and farms, not from the countryside to cities.",
     "E": "Incorrect. The herders choose to move with the seasons; no one forces them."
    },
    "explanation": "Transhumance = moving animals up to cool mountain pastures in summer and back down to the valleys in winter, every year. It happens in the Alps, the Andes, the Himalayas, and parts of Africa."
   },
   {
    "id": "U2-E21",
    "n": 21,
    "set": "mapV",
    "topic": "2.1",
    "lo": "PSO-2.A",
    "skill": "4.C",
    "difficulty": "medium",
    "stimulus": {
     "type": "schematicMap",
     "title": "POPULATION AND MIGRATION IN COUNTRY V, 2000–2020 (HYPOTHETICAL)",
     "canvas": {
      "width": 800,
      "height": 420
     },
     "features": [
      {
       "kind": "land",
       "name": "Coastal plain",
       "polygon": [
        [
         118,
         0
        ],
        [
         250,
         0
        ],
        [
         250,
         420
        ],
        [
         110,
         420
        ],
        [
         92,
         330
        ],
        [
         112,
         250
        ],
        [
         90,
         170
        ],
        [
         114,
         95
        ],
        [
         96,
         40
        ]
       ],
       "labelAt": [
        180,
        385
       ],
       "style": "small"
      },
      {
       "kind": "land",
       "name": "River valley",
       "polygon": [
        [
         250,
         160
        ],
        [
         630,
         150
        ],
        [
         630,
         240
        ],
        [
         250,
         255
        ]
       ],
       "labelAt": [
        470,
        228
       ],
       "style": "small"
      },
      {
       "kind": "land",
       "name": "Dry interior",
       "polygon": [
        [
         250,
         0
        ],
        [
         630,
         0
        ],
        [
         630,
         150
        ],
        [
         250,
         160
        ]
       ],
       "labelAt": [
        440,
        45
       ]
      },
      {
       "kind": "land",
       "name": "Dry interior",
       "polygon": [
        [
         250,
         255
        ],
        [
         630,
         240
        ],
        [
         630,
         420
        ],
        [
         250,
         420
        ]
       ],
       "labelAt": [
        440,
        385
       ]
      },
      {
       "kind": "land",
       "name": "Mountains",
       "polygon": [
        [
         630,
         0
        ],
        [
         800,
         0
        ],
        [
         800,
         420
        ],
        [
         630,
         420
        ]
       ],
       "labelAt": [
        706,
        210
       ],
       "style": "power"
      },
      {
       "kind": "marker",
       "name": "City or town",
       "points": [
        [
         160,
         90
        ],
        [
         150,
         330
        ],
        [
         330,
         198
        ],
        [
         450,
         193
        ],
        [
         560,
         190
        ]
       ],
       "symbol": "baseN"
      },
      {
       "kind": "marker",
       "name": "Rural village",
       "points": [
        [
         400,
         90
        ],
        [
         560,
         70
        ],
        [
         420,
         330
        ],
        [
         560,
         340
        ]
       ],
       "symbol": "house"
      },
      {
       "kind": "marker",
       "name": "Capital city and main port",
       "points": [
        [
         165,
         205
        ]
       ],
       "symbol": "conflict"
      },
      {
       "kind": "arrow",
       "name": "Migration flow from an interior village to the capital",
       "from": [
        392,
        96
       ],
       "to": [
        188,
        196
       ]
      },
      {
       "kind": "arrow",
       "name": "Migration flow from an interior village to the capital",
       "from": [
        552,
        78
       ],
       "to": [
        192,
        190
       ]
      },
      {
       "kind": "arrow",
       "name": "Migration flow from an interior village to the capital",
       "from": [
        412,
        324
       ],
       "to": [
        188,
        214
       ]
      },
      {
       "kind": "arrow",
       "name": "Migration flow from an interior village to the capital",
       "from": [
        552,
        334
       ],
       "to": [
        192,
        222
       ]
      }
     ],
     "legend": [
      {
       "swatch": "small",
       "label": "Coastal plain and river valley (fertile, well watered)"
      },
      {
       "swatch": "land",
       "label": "Dry interior"
      },
      {
       "swatch": "power",
       "label": "Mountains"
      },
      {
       "swatch": "conflict",
       "label": "Capital city and main port"
      },
      {
       "swatch": "baseN",
       "label": "City or town"
      },
      {
       "swatch": "house",
       "label": "Rural village"
      },
      {
       "swatch": "water",
       "label": "Ocean"
      }
     ],
     "description": "Map of Country V. The ocean is on the west. A fertile coastal plain runs along the coast, and a river valley crosses the country from the mountains in the east to the coast. The rest of the interior is dry. The capital city, the main port, sits on the coast where the river valley meets the ocean. The other cities and towns are on the coastal plain and in the river valley. Small villages are scattered across the dry interior. Arrows run from four interior villages to the capital.",
     "note": "Arrows show the largest migration flows from 2000 to 2020. During those years, the dry interior had repeated droughts, and the capital's port and new factories added many jobs.",
     "source": "Hypothetical map"
    },
    "stem": "Most of Country V's cities and towns are located on the coastal plain and in the river valley. Which of the following best explains this pattern?",
    "options": {
     "A": "The dry interior has been set aside as a protected national park.",
     "B": "The coast and valley have the coolest year-round temperatures in Country V.",
     "C": "The mountains block people in the interior from reaching other areas.",
     "D": "The coast and valley were the first areas where the land was surveyed.",
     "E": "The coast and valley have water, flat fertile land, and access to trade."
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. The map shows no park, and people do live in small villages in the interior; the interior is sparsely settled because it is dry.",
     "B": "Incorrect. Nothing on the map shows that the lowlands are cooler, and mountains are usually cooler than lowlands.",
     "C": "Incorrect. The mountains lie along the eastern edge of the country; they do not separate the interior villages from the coast.",
     "D": "Incorrect. The order in which land was surveyed does not explain this distribution; the physical environment does.",
     "E": "Correct. Physical factors such as water bodies, landforms, and climate influence population distribution. The coast and the river valley provide water for people and irrigation, flat and fertile land, and easy transportation, so cities grew there, while the dry interior and the mountains remain sparsely settled."
    },
    "explanation": "People settle where life is easier: near water, on flat land with good soil, and where boats and roads make trade easy. In Country V that means the coast and the river valley. The dry interior and the mountains have far fewer people."
   },
   {
    "id": "U2-E22",
    "n": 22,
    "set": "mapV",
    "topic": "2.11",
    "lo": "IMP-2.D",
    "skill": "4.B",
    "difficulty": "easy",
    "stem": "The arrows on the map best illustrate which type of migration?",
    "options": {
     "A": "Internal, rural-to-urban migration",
     "B": "International, transnational migration",
     "C": "Seasonal transhumance",
     "D": "Urban-to-rural migration",
     "E": "Guest worker migration"
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. The arrows begin at rural villages in the dry interior and end at the capital city, and none of them crosses Country V's borders. This is internal migration from rural to urban areas, one of the types of voluntary migration in the AP course framework.",
     "B": "Incorrect. The arrows do not cross an international border, so the map does not show international or transnational migration.",
     "C": "Incorrect. Transhumance is the seasonal movement of herders and livestock; the arrows show one-way moves from villages to a city.",
     "D": "Incorrect. The arrows point from rural villages toward the capital, the opposite of urban-to-rural migration.",
     "E": "Incorrect. Guest workers move to another country for temporary jobs; these migrants stay in their own country."
    },
    "explanation": "Follow the arrows: they start at small villages in the dry interior and end at the capital. They never leave Country V. Moving from the countryside to a city inside your own country = internal, rural-to-urban migration."
   },
   {
    "id": "U2-E23",
    "n": 23,
    "set": "mapV",
    "topic": "2.10",
    "lo": "IMP-2.C",
    "skill": "4.E",
    "difficulty": "medium",
    "stem": "Based on the map and its note, which combination of factors best explains the migration flows shown?",
    "options": {
     "A": "A political push factor in the interior and a cultural pull factor in the capital",
     "B": "An environmental push factor in the interior and an economic pull factor in the capital",
     "C": "An economic push factor in the capital and an environmental pull factor in the interior",
     "D": "An intervening opportunity in the interior and an intervening obstacle on the coast",
     "E": "A demographic pull factor in the interior and a political push factor in the capital city"
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. The note describes droughts and new jobs, not war, persecution, or cultural ties.",
     "B": "Correct. Repeated droughts in the dry interior are an environmental push factor that makes farming harder, and new port and factory jobs in the capital are an economic pull factor. Together they explain the flows from interior villages to the capital.",
     "C": "Incorrect. This reverses the direction: push factors operate at the origin (the interior), and pull factors at the destination (the capital).",
     "D": "Incorrect. An intervening opportunity would cause migrants to stop partway, and nothing on the map shows an obstacle on the coast; the migrants reach the capital.",
     "E": "Incorrect. People are moving away from the interior, not toward it, and the capital is attracting migrants, not pushing them away."
    },
    "explanation": "Push = what makes people leave (drought in the interior: environmental). Pull = what draws them in (jobs at the port and factories: economic). Push factors are at the starting place; pull factors are at the destination."
   },
   {
    "id": "U2-E24",
    "n": 24,
    "topic": "2.12",
    "lo": "IMP-2.E",
    "skill": "5.B",
    "difficulty": "medium",
    "stem": "Which of the following best describes the effects of remittances at different scales in a country where remittances equal about one-fifth of its gross domestic product (GDP)?",
    "options": {
     "A": "They help individual households but have little effect on the national economy as a whole.",
     "B": "They strengthen the national economy but seldom reach individual families in rural villages.",
     "C": "They mainly benefit the destination countries where the migrants work and earn their wages.",
     "D": "Households use them for food, school, and housing, and nationally they are a major income source.",
     "E": "They mainly slow emigration, because families that receive the money no longer need to move."
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. When remittances equal about one-fifth of GDP, they are a large part of the national economy, not a small one.",
     "B": "Incorrect. Remittances are sent directly to migrants' families, so they reach households first.",
     "C": "Incorrect. Remittances flow from destination countries back to migrants' home countries.",
     "D": "Correct. At the household and local scale, remittances pay for food, school fees, health care, and new homes. At the national scale, they bring in foreign currency and can make up a large share of GDP; in 2024, remittances equaled about one-quarter of GDP in Nepal and in Honduras.",
     "E": "Incorrect. Remittances often help pay the costs of moving and show families the rewards of working abroad, so they can encourage more emigration, not less."
    },
    "explanation": "Think at two scales. Family scale: the money buys food, pays for school, and builds houses. Country scale: when remittances equal one-fifth of everything the economy produces, the whole country depends on them. That also means a recession in the countries where migrants work can hurt the home country."
   },
   {
    "id": "U2-E25",
    "n": 25,
    "topic": "2.12",
    "lo": "IMP-2.E",
    "skill": "2.C",
    "difficulty": "hard",
    "stem": "For 30 years, many young adults from rural villages in Country H have migrated abroad for work. Which of the following is the most likely effect on those villages?",
    "options": {
     "A": "Village populations grow younger as migrants' children move back to run the family farms.",
     "B": "Villages gain more working-age adults than they lose, so farm labor becomes cheaper.",
     "C": "Villages are left with mostly older adults and children, and farms face labor shortages.",
     "D": "Villages develop sex ratios well above 100, because the migrants are mostly young men.",
     "E": "Villages see rising birth rates, because the people who remain are mostly young couples."
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. Most migrants are young adults, and many do not return to farm, so the villages tend to grow older, not younger.",
     "B": "Incorrect. The villages lose working-age adults to emigration, which tends to create labor shortages and raise farm wages.",
     "C": "Correct. Migration is selective by age: most migrants are young adults. Their departure leaves sending villages with mostly older adults and children, labor shortages on farms, and in some cases abandoned fields, even as remittances help families pay for food and housing.",
     "D": "Incorrect. If more young men than young women leave, the villages are left with more women than men, a sex ratio below 100, not above it.",
     "E": "Incorrect. The people most likely to have children are the young adults who left, so birth rates in the villages tend to fall."
    },
    "explanation": "Most people who migrate for work are young adults. When they leave, the village is left with grandparents and children. There are fewer people to farm, so some fields may go unplanted, even though money sent home (remittances) helps families buy food and build houses."
   }
  ]
 }
}
```

## SOURCES.md (complete)

# Unit 2 bank — sources and verification notes (v2026-11-08b)

All stimuli are hypothetical (labeled "Hypothetical data" / "Hypothetical map") except the three World Bank tables below.
Every rate, ratio, density, share and doubling time in the bank is recomputed by `u2/assemble.py` from `u2/data.py`
(the `VERIFY` block); the build fails if any keyed number or quoted figure drifts. Raw API responses are saved in
`u2/data_raw/` (pulled Nov 8, 2026; WDI `lastupdated` = 2026-10-08).

## Real-data stimuli (World Bank, World Development Indicators)

| Item | Indicators (2024 values) | API query used | What was verified |
|---|---|---|---|
| U2-P02 density table | SP.POP.TOTL, AG.LND.TOTL.K2, AG.LND.ARBL.HA | https://api.worldbank.org/v2/country/EGY;NLD;CAN;JPN/indicator/{code}?format=json&date=2019:2024 | Population, land area and arable land for Egypt, Netherlands, Japan, Canada; arithmetic and physiological densities computed by script (arable ha ÷ 100 = sq km). Arithmetic densities cross-checked against WDI EN.POP.DNST 2024 (Egypt 117.07, Netherlands 534.41, Japan 340.12, Canada 4.69): exact match. Key: Egypt arithmetic 117 < Netherlands 534, physiological 3,560 > 1,794 (ratio 1.98, "about twice"); Egypt arable share 3.29%. |
| U2-P13 vital-rates table | SP.DYN.CBRT.IN, SP.DYN.CDRT.IN, SP.POP.GROW | https://api.worldbank.org/v2/country/NER;IND;CAN;DEU;JPN/indicator/{code}?format=json&date=2021:2024 | Niger 41.42 / 8.719 / 3.28%; India 15.981 / 6.587 / 0.89%; Canada 8.9 / 7.9 / 2.98%; Germany 8.1 / 12.1 / 0.27%; Japan 5.7 / 13.3 / −0.44%. Script confirms Germany is the only country with deaths > births and positive growth (RNI −0.4%, growth +0.3%); Japan's growth is negative; Canada RNI 0.1%. |
| U2-P40 remittances table | BX.TRF.PWKR.CD.DT, BX.TRF.PWKR.DT.GD.ZS | https://api.worldbank.org/v2/country/IND;MEX;PHL;NPL;TJK;TON/indicator/{code}?format=json&date=2021:2024 | India $137.7B / 3.66%; Mexico $67.9B / 3.71%; Philippines $40.3B / 8.72%; Nepal $11.3B / 25.99%; Tajikistan $6.8B / 47.15%; Tonga $0.26B / 39.41%. Script confirms the two largest receivers (India, Mexico) have the two lowest GDP shares. |

## Real figures quoted in stems, keys, or rationales

| Item | Claim | Source checked |
|---|---|---|
| U2-E07 | 2024 crude death rate: Japan about 13, Niger about 9 per 1,000; Japan about 3 in 10 people 65+; Japan life expectancy among the world's highest; Niger IMR much higher than Japan's | WDI SP.DYN.CDRT.IN 2024 (13.3, 8.719); SP.POP.65UP.TO.ZS 2024 (Japan 29.8%, Niger 2.6%); SP.DYN.LE00.IN 2024 (Japan 84.0, Niger 61.4, world 73.5); SP.DYN.IMRT.IN 2024 (Japan 1.8, Niger 65.6) |
| U2-E14 | Latin America & Caribbean TFR about 5.2 (1970) to about 1.9 (2020); infant mortality fell; region urbanized | WDI SP.DYN.TFRT.IN, aggregate LCN (5.18 → 1.86); SP.DYN.IMRT.IN: the LCN aggregate starts in 1990 (44.1 → 14.4 in 2020), and the country series cover 1970–2020 (Brazil 102.2 → 12.8, Mexico 82.0 → 13.4, Peru 127.3 → 12.2, Haiti 168.0 → 43.6 per 1,000; https://api.worldbank.org/v2/country/BRA;MEX;PER;HTI/indicator/SP.DYN.IMRT.IN?format=json&date=1970:2020, saved as data_raw/IMR_LAC_countries.json); SP.URB.TOTL.IN.ZS LCN (56.5% in 1970 → 80.4% in 2020) |
| U2-E24 | Remittances about one-quarter of GDP in Nepal and Honduras in 2024 | WDI BX.TRF.PWKR.DT.GD.ZS 2024 (Nepal 25.99%, Honduras 25.74%) |
| U2-P29 | Women and girls are almost half (about 48%) of international migrants | UN DESA International Migrant Stock 2024, as reported by Dawn, Feb 18, 2025: https://dawn.com/news/1892702/number-of-migrants-doubled-since-1990-un ("just under half (48pc) of all international migrants worldwide were women or girls") |
| U2-P07 | Groundwater pumping makes parts of Mexico City sink, in places tens of centimeters a year | Eos (AGU): https://eos.org/articles/groundwater-pumping-is-causing-mexico-city-to-sink ("groundwater pumping is the main driver of subsidence"; "about 35 centimeters (14 inches) per year"). Elevation ~2,240 m (standard reference). |
| U2-E01 | Most Russians live west of the Urals, on a minority of the land | Wikipedia, European Russia: https://wikiwand.com/en/articles/European_Russia ("about 80% of Russia's total population"; c. 23% of territory). Item wording avoids a precise percentage. |
| U2-E09 | Singapore "Stop at Two" campaign in the 1970s; "Have Three or More (if you can afford it)" announced 1987; fertility below replacement by the late 1970s (about 1.8 in 1977) | Wikipedia, Population planning in Singapore: https://en.wikipedia.org/wiki/Population_planning_in_Singapore. The independent checker confirmed Singapore's TFR was 2.07 in 1975, 2.11 in 1976, 1.82 in 1977, and below 2.1 every year since. |

## Standard-textbook facts (no figures), wording kept conservative

China one-child policy about 1980–2015, two-child 2016, three-child 2021 (P25); Malthus 1798 (P21); Paul Ehrlich, *The Population Bomb*, 1968 (P23);
Esther Boserup's intensification argument (E08); Ravenstein's laws, 1880s, including short-distance moves, step migration, long-distance
migrants heading for centers of commerce and industry, and women more migratory within their home country (P29, P35, P37);
Canada and Australia use points-based immigration systems (P26); Qatar and the UAE have strongly male-skewed working-age pyramids
because of foreign labor (P10 explanation); Alpine transhumance (E20); Soviet-era growth of Siberian cities such as Novosibirsk, oil and gas
mainly in western Siberia, the Urals as low mountains crossed by the Trans-Siberian Railway (E01 rationales).

## Notes for reviewers

- Ravenstein's laws appear in the course framework only under SPS-2.B.2 (Topic 2.8, women). P29 is tagged there. P35 (distance decay) stays at 2.10 / IMP-2.C and is tied to IMP-2.C.2: its explanation treats distance itself as an intervening obstacle (longer moves cost more and people know less about faraway places).
- Practice stimuli are self-contained (no `set`), as in units 4 and 5, because app.js renders practice stimuli from `q.stimulus` only and practice can be filtered by topic.
