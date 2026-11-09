# Unit 6 question bank: full export for outside review

Unit 6, Cities and Urban Land-Use Patterns and Processes. Version 2026-11-08d.
47 untimed practice questions (instant feedback: a 6th-grade-level explanation plus one "why not" line per wrong option)
and a 25-question timed exam (25 minutes, choices A–E, College Board-style rationales for every option,
10 stimulus questions in 4 sets). Students are 9th graders in AP Human Geography.

Everything below is the complete data file the page uses (unit6.json), followed by the sources note (SOURCES.md).

How the stimulus types render (the JSON holds all of their data):
- table: an HTML table with the given columns and rows; `note` and `text` show under the table, then the source line.
  Row labels such as "City P" and "Tract 101" contain a non-breaking space (shown in JSON as a plain-looking space).
  No Unit 6 table uses `note`; U6-E20's inflation statement is part of its source line.
- bar: grouped vertical bars, one group per category, at most two series, value printed on each bar; `text` shows under
  the chart. Bar charts: U6-P40 (two series) and U6-P46 (one series).
- line: one line per series across the categories, each series with its own marker shape and dash pattern, y-axis from 0
  (to `yMax` when given). Point values are not printed on the chart; students read them against the grid lines. The
  `description` paragraph shows under the chart. Line charts: U6-P02, U6-P17, U6-E02 (set for E02–E03).
- rings (U6-P16): a dark center disk labeled "CBD" inside four concentric rings labeled V (innermost), W, X, Y (outermost);
  each ring letter is printed on four sides, and "Rural land" is printed in two corners. Ring names are not printed.
- schematicMap: an SVG drawn from `canvas` (pixel width and height) and `features` (polygon coordinates in pixels; the
  background is water). Land areas use up to three fill colors; a lavender ("power") fill prints its label larger. The
  `description` and `note` paragraphs show under the map.
  - U6-P18 (City W, 800×400): a lake fills the top strip (y 0–50). The CBD is a blue half-disk (radius 45) on the shore at
    (400,50). Six wedges run from the CBD to the map edges; angles are measured clockwise from due east: 0–40° "High
    income" (east, along the lake), 40–65° "Middle income", 65–82° "Low income", 82–98° "Industry" (due south), 98–125° "Low
    income", 125–180° "Middle income" (west, along the lake). A dashed colored "Railroad" line runs straight south from the
    CBD through the Industry wedge; a dashed "Lakeshore boulevard" runs along the shore east of the CBD (y 60, x 445–800).
    Wedges alternate two fill colors, and all wedge labels are the same size.
  - U6-P35 (City H, 800×400): a 3×3-style grid. Top row (y 0–130): Grade A, Grade B, Grade A. Middle row (y 130–260): Grade C,
    CBD (lavender, larger label), Grade C. Bottom strip (y 260–340): Grade D (left half) and "Factories and rail yards" (right
    half). A dashed rail line crosses the whole map at y 260 (the top edge of the Grade D strip), and a river (water) fills y 340–400. The note box explains the
    A ("best") to D ("hazardous") grades.
  - U6-E11 to E13 (Latin American city model, 800×420, center (400,210)): Area 5 is the cream background filling the whole
    canvas; Area 4 is a beige disk (radius 150); Area 3 a cream disk (radius 95); Area 1 a beige disk (radius 35) at the center.
    Area 2 is a lavender wedge from radius 35 to 205 between −105° and −75° (pointing north, reaching about y 5), with a dashed
    "Main boulevard" running up its middle. Area 6 is a narrow lavender wedge from radius 35 to 205 between 40° and 55° (pointing
    southeast; its outer end is about (538,361), inside Area 5). Only the numbers 1–6 are printed (labels "2" and "6" print
    larger because of their fill style); zone names are not printed because the questions ask students to identify them.
- In the exam, a set's stimulus is stored on the first question of the set (with `setLabel`) and shown beside every
  question in the set. Practice questions do not use sets; each practice stimulus belongs to its own question.

===== unit6.json =====
{
 "unit": 6,
 "title": "Cities and Urban Land-Use Patterns and Processes",
 "examWeighting": "12–17% of the AP Exam multiple-choice section",
 "version": "2026-11-08d",
 "calibration": "Modeled on the format of the College Board 2020 AP Human Geography Practice Exam and the Course and Exam Description (5 answer choices, set-based stimulus questions, skills 1–5). All questions, stimuli, and data are original or compiled from public facts; no College Board items are reproduced. Designed to approximate AP multiple-choice format and pacing; difficulty labels are author estimates pending student piloting. Real data (World Bank urban-share series; U.S. Census Bureau city populations) were checked against the official source files listed in u6/SOURCES.md.",
 "checked": "Nov 8, 2026: draft. Automated checks in u6/assemble.py (answer balance and runs, option-length tells, absolute-word tells, field completeness, set structure, student-facing wording, reading level) and u6/verify.py (every number and computed answer re-derived by script; World Bank and Census values matched to the source files, re-fetched live). Independent blind Claude check (Nov 8): 66/66 keys agreed; World Bank and Census values re-downloaded and matched; fixes applied for P13 (Pair 3 distance 25 km so the key holds whether or not distance is squared), E11 diagram description, E20 inflation note moved to the source line, E16 D, E19 distractors (two benefits replace reversed-praise options; skill 1.B), absolute-word tells in P29/P33/P36, E11/E12 disamenity wording, P21 and P06 explanations, E22 stem tied to the data, E25 skill 5.B. ChatGPT Pro full review (Nov 8, 11 min, version b): no rekeying; applied in u6/fixes_c.py: gravity formula stated in P13/E09; Griffin–Ford spine vs. elite-sector wording (E11–E13, P19); secure land tenure vs. ownership (P36, E13); aggregate-data inference limits (P02, P04, P23, P31, P32, P33, E20); HOLC/redlining causal wording (P35, E23); central place wording (E10, P14); boomburb attribution (P06, SOURCES); governmental authority (P38, E25); explanations P05, P09, P30, P39, P41, E03, E06, E08; E02 distractor D; P17 and E19 and E24 rewritten so the stimulus or scenario is needed; P18 options reduced to model names; smaller edits P03, P15, P16, P22, P26, P28, P29; skill and difficulty tags; six practice items added (P42–P47: galactic city, metacity, environmental injustice, local food movement, urban heat island, historic character). Final blind Claude check of version c (Nov 8): 72/72 keys agreed, no must-fix; sources re-downloaded and every number recomputed; applied in u6/fixes_d.py: E25 and P47 and P45 distractors no longer refutable from the stem, P46 options rebuilt (key moved to E), E24 options use brownfield/greenfield/inclusionary-zoning vocabulary, P36 E, P15 and E10 and E12 and P37 key wording, P02 why-not D, simpler P36/P42/P45 explanations, P23 wording, P40 stem, E17 hedge, P35 rail line moved to the Grade D edge, E13/E14 options swapped to break the E11-E13 key run.",
 "schemaNotes": {
  "stimulus.type": "table | bar | line | districtMap | schematicMap | rings (line = multi-series line chart: categories[] on the x-axis, series[].name/values[], xLabel, yLabel, optional yMax; rings = concentric ring diagram: center, rings[].label, outer, description)",
  "practice[].explanation": "6th-grade-level reason the answer is right (show this first)",
  "practice[].whyNot": "one line per wrong option",
  "exam.questions[].rationales": "College Board-style note on every option A–E",
  "exam.questions[].explanation": "6th-grade-level version for the review screen",
  "set": "questions sharing a stimulus carry the same set id; the stimulus object (and setLabel) lives on the first question of the set. Practice items do not use sets: each practice stimulus is attached to its own question."
 },
 "topics": [
  {
   "id": "6.1",
   "name": "The Origin and Influences of Urbanization",
   "lo": "PSO-6.A"
  },
  {
   "id": "6.2",
   "name": "Cities Across the World",
   "lo": "PSO-6.A"
  },
  {
   "id": "6.3",
   "name": "Cities and Globalization",
   "lo": "PSO-6.B"
  },
  {
   "id": "6.4",
   "name": "The Size and Distribution of Cities",
   "lo": "PSO-6.C"
  },
  {
   "id": "6.5",
   "name": "The Internal Structure of Cities",
   "lo": "PSO-6.D"
  },
  {
   "id": "6.6",
   "name": "Density and Land Use",
   "lo": "IMP-6.A"
  },
  {
   "id": "6.7",
   "name": "Infrastructure",
   "lo": "IMP-6.B"
  },
  {
   "id": "6.8",
   "name": "Urban Sustainability",
   "lo": "IMP-6.C, IMP-6.D"
  },
  {
   "id": "6.9",
   "name": "Urban Data",
   "lo": "IMP-6.E"
  },
  {
   "id": "6.10",
   "name": "Challenges of Urban Changes",
   "lo": "SPS-6.A"
  },
  {
   "id": "6.11",
   "name": "Challenges of Urban Sustainability",
   "lo": "SPS-6.B"
  }
 ],
 "practice": [
  {
   "id": "U6-P01",
   "topic": "6.1",
   "lo": "PSO-6.A",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following describes a city's situation rather than its site?",
   "options": {
    "A": "It was built on a hill above a river floodplain.",
    "B": "It has a deep, sheltered natural harbor where ships can dock.",
    "C": "It sits on flat land with plenty of fresh groundwater.",
    "D": "It lies on the main rail line between two large cities.",
    "E": "It was founded on a rocky island that was easy to defend."
   },
   "answer": "D",
   "explanation": "Situation is where a city is compared with OTHER places: the routes, cities, and regions around it. Being on the main rail line between two big cities is about connections to other places, so it is situation. Site is the physical land at the exact spot: hills, harbors, soil, and water.",
   "whyNot": {
    "A": "A hill above a floodplain is a feature of the land itself. That is site.",
    "B": "A harbor is a physical feature of the exact spot. That is site.",
    "C": "Flat land and groundwater are physical features of the spot. That is site.",
    "E": "An island that is easy to defend describes the land the city sits on. That is site."
   },
   "vocab": [
    "site",
    "situation",
    "relative location"
   ]
  },
  {
   "id": "U6-P02",
   "topic": "6.1",
   "lo": "PSO-6.A",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "line",
    "title": "URBAN AND RURAL POPULATION OF COUNTRY X, 1960–2020 (HYPOTHETICAL DATA)",
    "xLabel": "Year",
    "yLabel": "Population (millions)",
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
      "name": "Urban population",
      "values": [
       4,
       5,
       7,
       11,
       18,
       27,
       38
      ]
     },
     {
      "name": "Rural population",
      "values": [
       16,
       19,
       22,
       24,
       23,
       21,
       19
      ]
     }
    ],
    "yMax": 40,
    "description": "Line graph of the urban population and the rural population of Country X, in millions, every ten years from 1960 to 2020.",
    "source": "Hypothetical data"
   },
   "stem": "Which process could help explain both the increase in urban population and the decrease in rural population shown between 1990 and 2020?",
   "options": {
    "A": "Counterurbanization moved people from cities to rural areas, so rural areas grew faster than cities.",
    "B": "Net migration from rural areas to cities added residents to cities while reducing the rural population.",
    "C": "High rural birth rates, with little migration to cities, made the rural population grow faster than the urban population.",
    "D": "Suburbanization moved city residents out into rural counties, so the rural share of the country's population rose.",
    "E": "Deindustrialization closed many city factories, so the urban population grew more slowly after 1990 than it had before."
   },
   "answer": "B",
   "explanation": "Urban population rose from 11 million to 38 million, while rural population fell from 24 million to 19 million. More people moving from rural areas to cities (net rural-to-urban migration) could cause both changes. The graph alone does not show how much of the change came from migration, from births and deaths, or from places being reclassified as urban.",
   "whyNot": {
    "A": "Counterurbanization means moving OUT of cities. Here the rural population fell and cities grew.",
    "C": "The rural population shrank after 1990. It did not grow faster than the urban population.",
    "D": "Suburbs usually count as urban areas, so suburbanization would not make the country more rural. The rural share actually fell, from about 69% in 1990 to about 33% in 2020.",
    "E": "Urban growth sped up after 1990: it rose by 27 million from 1990 to 2020, compared with 7 million from 1960 to 1990."
   },
   "vocab": [
    "rural-to-urban migration",
    "urbanization",
    "pull factor"
   ]
  },
  {
   "id": "U6-P03",
   "topic": "6.1",
   "lo": "PSO-6.A",
   "skill": "1.B",
   "difficulty": "medium",
   "stem": "Which of the following best explains the rapid growth of suburbs in the United States in the decades after World War II?",
   "options": {
    "A": "Streetcar lines expanded quickly after the war, letting workers commute from new suburbs to downtown jobs.",
    "B": "Urban renewal programs built large numbers of single-family homes in downtown neighborhoods.",
    "C": "Federally backed mortgages and new highways made buying a suburban home and commuting by car easier.",
    "D": "Factories moved into central business districts, drawing workers away from the edges of cities.",
    "E": "Greenbelt laws in most large cities required new housing to be built beyond the city limits."
   },
   "answer": "C",
   "explanation": "After 1945, the federal government backed home loans (through programs such as the FHA and the GI Bill), so many families could afford a new house with a small down payment. Then new highways, including the interstate system that began in 1956, made it fast to drive from a suburb to a city job. Cheap loans + cars + highways = suburbs.",
   "whyNot": {
    "A": "Streetcar suburbs grew from the late 1800s to the 1920s. After World War II, most streetcar lines were shrinking, and the car took over.",
    "B": "Urban renewal tore down older city neighborhoods for highways, offices, and public housing. It did not build suburbs.",
    "D": "Factories were moving OUT toward the suburbs, not into downtown.",
    "E": "Greenbelts LIMIT building at a city's edge, and they were not common in U.S. cities."
   },
   "vocab": [
    "suburbanization",
    "Federal Housing Administration (FHA)",
    "Interstate Highway System"
   ]
  },
  {
   "id": "U6-P04",
   "topic": "6.1",
   "lo": "PSO-6.A",
   "skill": "2.D",
   "difficulty": "medium",
   "stem": "During the 1800s, the growth of cities in Great Britain was closely tied to the spread of factory jobs. Today, many cities in sub-Saharan Africa are growing quickly even though manufacturing employs a relatively small share of their workers. Which of the following best explains this difference?",
   "options": {
    "A": "Wealthy residents are moving from the suburbs back to downtown areas, so central neighborhoods are growing quickly.",
    "B": "Natural increase and migration from rural areas drive growth, and many newcomers work in the informal economy.",
    "C": "Deindustrialization in the region has forced factory workers to leave cities and return to farming villages.",
    "D": "Most new city residents in the region are international migrants arriving from core countries.",
    "E": "Colonial governments are building new ports and capital cities to export the region's raw materials to Europe."
   },
   "answer": "B",
   "explanation": "A city can grow in three ways. More babies can be born than people die. More people can move in than move out. Or the city's borders can be drawn bigger. In many sub-Saharan African cities, the number of people has grown faster than the number of factory jobs. Many people earn money in informal work, like selling goods on the street, though this differs from city to city. Britain's cities in the 1800s grew mostly because new factories pulled people in.",
   "whyNot": {
    "A": "Moving from suburbs back downtown shifts people around inside a city. It does not explain fast growth of the whole city.",
    "C": "People leaving cities would work against urban growth. It does not explain the fast growth described in the stem.",
    "D": "Most newcomers come from the same country, especially from rural areas, not from core countries.",
    "E": "Colonial rule in the region ended decades ago. Colonial ports and capitals explain how some cities began, not why they are growing today."
   },
   "vocab": [
    "natural increase",
    "rural-to-urban migration",
    "informal economy"
   ]
  },
  {
   "id": "U6-P05",
   "topic": "6.2",
   "lo": "PSO-6.A",
   "skill": "1.D",
   "difficulty": "easy",
   "stem": "Near a busy beltway interchange, a suburban area has grown into a cluster of office towers, a regional shopping mall, hotels, and corporate campuses. More people work there each weekday than live there. This area is best described as",
   "options": {
    "A": "an exurb",
    "B": "a boomburb",
    "C": "a central business district",
    "D": "a zone in transition",
    "E": "an edge city"
   },
   "answer": "E",
   "explanation": "An edge city is a big cluster of offices, stores, and jobs outside the old downtown, often near a highway interchange. Workers commute to it from other parts of the metro area. The office towers, regional mall, and large daytime workforce fit this pattern.",
   "whyNot": {
    "A": "An exurb is a mostly residential area of homes on large lots beyond the suburbs, with few offices.",
    "B": "A boomburb is a fast-growing suburban CITY with more than 100,000 residents. The clue here is jobs and offices, not a large, fast-growing population.",
    "C": "The CBD is the old downtown in the center of the city, not a suburban cluster near a beltway.",
    "D": "The zone in transition is the ring of older housing and factories right next to the CBD in the Burgess model."
   },
   "vocab": [
    "edge city",
    "decentralization",
    "beltway"
   ]
  },
  {
   "id": "U6-P06",
   "topic": "6.2",
   "lo": "PSO-6.A",
   "skill": "3.D",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "POPULATION OF FOUR CITIES IN THE DALLAS–FORT WORTH METROPOLITAN AREA, 2000–2024",
    "columns": [
     "City",
     "2000 Census",
     "2010 Census",
     "July 1, 2024 estimate"
    ],
    "rows": [
     [
      "Dallas",
      "1,188,580",
      "1,197,816",
      "1,326,087"
     ],
     [
      "Plano",
      "222,030",
      "259,841",
      "293,286"
     ],
     [
      "McKinney",
      "54,369",
      "131,117",
      "227,526"
     ],
     [
      "Frisco",
      "33,714",
      "116,989",
      "235,208"
     ]
    ],
    "source": "U.S. Census Bureau, Population Estimates Program: Census 2000 and 2010 counts from the subcounty population files SUB-EST2009_48 and SUB-EST2020_48; July 1, 2024 estimates from SUB-EST2024_48 (Vintage 2024). Populations are for each city's incorporated limits."
   },
   "stem": "Based on the table, Frisco and McKinney are best described as",
   "options": {
    "A": "boomburbs, because they are fast-growing suburban cities of more than 100,000 people that are not the region's main city",
    "B": "edge cities, because they are suburban centers where office and retail jobs outnumber the people who live there",
    "C": "exurbs, because they are small, low-density communities beyond the suburbs where most residents commute long distances to work",
    "D": "primate cities, because each one is more than twice as large as the next-largest city in its region",
    "E": "central cities that lost residents to their suburbs as the metropolitan area decentralized after 2000"
   },
   "answer": "A",
   "explanation": "Frisco grew from about 34,000 people in 2000 to about 235,000 in 2024, about seven times as large. McKinney became about four times as large. Both had more than 100,000 residents by 2010, and both are suburbs in the Dallas–Fort Worth metropolitan area, not its largest city. Large, fast-growing suburban cities of more than 100,000 people like these are often called boomburbs.",
   "whyNot": {
    "B": "The table shows how many people LIVE in each city, not how many jobs or offices it has. Edge cities are defined by jobs and office space.",
    "C": "The table shows rapid growth in large cities. It gives no evidence of low density, a location beyond the suburbs, or long commutes.",
    "D": "Dallas is much larger than Frisco and McKinney, so neither of them is a primate city.",
    "E": "None of the four cities lost residents. Frisco and McKinney grew the fastest."
   },
   "vocab": [
    "boomburb",
    "suburbanization",
    "metropolitan area"
   ]
  },
  {
   "id": "U6-P07",
   "topic": "6.2",
   "lo": "PSO-6.A",
   "skill": "2.D",
   "difficulty": "medium",
   "stem": "In 1950, most of the world's largest cities were in core countries such as the United States, the United Kingdom, and Japan. Today, most of the world's megacities are in semiperiphery and periphery countries. Which of the following best explains this change?",
   "options": {
    "A": "Cities in core countries have lost most of their residents through counterurbanization since 1950.",
    "B": "Factory jobs moved from periphery countries to core countries after 1950, pulling workers away from periphery cities.",
    "C": "High natural increase and rural-to-urban migration made cities in those countries grow faster than core cities.",
    "D": "Periphery countries reached the later stages of the demographic transition before core countries did.",
    "E": "Most of today's megacities were built as new planned capital cities by periphery governments after independence."
   },
   "answer": "C",
   "explanation": "A megacity has 10 million or more people. Since 1950, many countries in Asia, Africa, and Latin America have had lots of births. Huge numbers of people also moved from farms to cities. So their cities grew much faster than cities in rich core countries. That is why most megacities today are in semiperiphery and periphery countries.",
   "whyNot": {
    "A": "Big core-country cities such as New York and Tokyo are larger now than in 1950. They did not lose most of their people.",
    "B": "Factory jobs mostly moved the other way, from core countries to semiperiphery and periphery countries.",
    "D": "Core countries went through the demographic transition FIRST. Many periphery countries still have higher birth rates.",
    "E": "A few planned capitals exist (such as Brasília and Abuja), but most megacities grew from older cities."
   },
   "vocab": [
    "megacity",
    "metacity",
    "periphery",
    "semiperiphery"
   ]
  },
  {
   "id": "U6-P08",
   "topic": "6.3",
   "lo": "PSO-6.B",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following characteristics best identifies a city as a world city (global city)?",
   "options": {
    "A": "It has the largest population of any city in its country.",
    "B": "It is the national capital of a large and powerful country.",
    "C": "It has 10 million or more people living in its metropolitan area.",
    "D": "It grew up at a break-of-bulk point on a major river or coast.",
    "E": "It is a center of global finance and corporate headquarters."
   },
   "answer": "E",
   "explanation": "A world city sits at the top of the global urban hierarchy because of what it CONTROLS and CONNECTS, not because of its size. World cities hold headquarters of big companies, banks, stock exchanges, and business services, and they are tied to other world cities by flights, money, and information. London, New York, and Tokyo are top examples.",
   "whyNot": {
    "A": "Being the biggest city in a country does not make a city a world city if it has few global connections.",
    "B": "Some capitals are world cities, but many are not. New York is a world city and is not a national capital.",
    "C": "That is a megacity. Some megacities have far fewer global business links than smaller world cities.",
    "D": "Break-of-bulk describes a city's situation for trade. It does not make a city a world city."
   },
   "vocab": [
    "world city",
    "global city",
    "urban hierarchy"
   ]
  },
  {
   "id": "U6-P09",
   "topic": "6.3",
   "lo": "PSO-6.B",
   "skill": "5.B",
   "difficulty": "medium",
   "stem": "A bank headquartered in London decides to close a customer-service center in a mid-sized city in India and move the jobs to a city in the Philippines. Which statement best explains the relationship among places at different scales in this example?",
   "options": {
    "A": "Local governments in India decide where transnational banks locate their offices.",
    "B": "A decision made at a world-city headquarters shifts local employment between cities in other countries.",
    "C": "Decisions made in smaller cities shape the economies of the larger world cities that are linked to them.",
    "D": "The change will mainly affect London's own local economy, with little effect on the two cities in Asia.",
    "E": "Cities lower in the urban hierarchy are cut off from global networks of trade and information."
   },
   "answer": "B",
   "explanation": "The bank's headquarters is in London, a world city. From there it runs offices around the world. When it closes one office and opens another, people in India lose jobs and people in the Philippines gain them. A choice made in one world city changes jobs in places far away.",
   "whyNot": {
    "A": "The bank's headquarters made this choice. Local governments can offer incentives, but they do not make the company's decision.",
    "C": "Here the decision flows the other way: from the world-city headquarters to the cities in Asia.",
    "D": "The biggest effects are in Asia, where jobs are lost in one city and gained in another.",
    "E": "Both Asian cities are clearly linked into the bank's global network."
   },
   "vocab": [
    "world city",
    "urban hierarchy",
    "scale of analysis",
    "outsourcing"
   ]
  },
  {
   "id": "U6-P10",
   "topic": "6.3",
   "lo": "PSO-6.B",
   "skill": "3.E",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "SELECTED CHARACTERISTICS OF FIVE CITIES (HYPOTHETICAL DATA)",
    "columns": [
     "City",
     "Metropolitan population (millions)",
     "Headquarters of the world's 500 largest companies",
     "International flights per week",
     "Major stock exchange"
    ],
    "rows": [
     [
      "City P",
      "24.0",
      "3",
      "900",
      "No"
     ],
     [
      "City Q",
      "8.5",
      "40",
      "4,800",
      "Yes"
     ],
     [
      "City R",
      "15.2",
      "6",
      "1,500",
      "Yes"
     ],
     [
      "City S",
      "3.1",
      "9",
      "1,900",
      "Yes"
     ],
     [
      "City T",
      "11.0",
      "12",
      "2,100",
      "Yes"
     ]
    ],
    "source": "Hypothetical data"
   },
   "stem": "Based on the data, which city most likely ranks highest in the global urban hierarchy?",
   "options": {
    "A": "City P",
    "B": "City Q",
    "C": "City R",
    "D": "City S",
    "E": "City T"
   },
   "answer": "B",
   "explanation": "The top of the global urban hierarchy is about connections and control. City Q has the most headquarters of giant companies (40), by far the most international flights (4,800 a week), and a major stock exchange. It is not the biggest city, but it is the most connected one, so it ranks highest.",
   "whyNot": {
    "A": "City P has the most people, but it has few company headquarters, the fewest flights, and no stock exchange. Big population does not equal world-city rank.",
    "C": "City R is large, but it has far fewer headquarters and flights than City Q.",
    "D": "City S is well connected for its size, but City Q has more than four times as many headquarters.",
    "E": "City T is the second-best connected city, but it has far fewer headquarters and flights than City Q."
   },
   "vocab": [
    "world city",
    "megacity",
    "urban hierarchy"
   ]
  },
  {
   "id": "U6-P11",
   "topic": "6.4",
   "lo": "PSO-6.C",
   "skill": "1.D",
   "difficulty": "easy",
   "stem": "The largest city in Country N has 6 million residents. If the country's cities follow the rank-size rule, about how many residents would its third-largest city have?",
   "options": {
    "A": "1.2 million",
    "B": "1.5 million",
    "C": "2 million",
    "D": "3 million",
    "E": "4 million"
   },
   "answer": "C",
   "explanation": "The rank-size rule says the city ranked n has 1/n as many people as the largest city. The third-largest city should have 1/3 of 6 million, which is 2 million.",
   "whyNot": {
    "A": "1.2 million is 1/5 of 6 million, the size of the fifth-largest city.",
    "B": "1.5 million is 1/4 of 6 million, the size of the fourth-largest city.",
    "D": "3 million is 1/2 of 6 million, the size of the second-largest city.",
    "E": "4 million is 2/3 of 6 million. The rule divides the largest city's population by the rank: 6 ÷ 3 = 2."
   },
   "vocab": [
    "rank-size rule",
    "urban hierarchy"
   ]
  },
  {
   "id": "U6-P12",
   "topic": "6.4",
   "lo": "PSO-6.C",
   "skill": "3.B",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "POPULATION OF THE FIVE LARGEST CITIES IN THREE COUNTRIES (HYPOTHETICAL DATA, MILLIONS)",
    "columns": [
     "City rank",
     "Country F",
     "Country G",
     "Country H"
    ],
    "rows": [
     [
      "1",
      "9.0",
      "4.8",
      "6.0"
     ],
     [
      "2",
      "1.6",
      "2.4",
      "4.5"
     ],
     [
      "3",
      "1.1",
      "1.6",
      "3.8"
     ],
     [
      "4",
      "0.9",
      "1.2",
      "3.0"
     ],
     [
      "5",
      "0.8",
      "1.0",
      "2.7"
     ]
    ],
    "source": "Hypothetical data"
   },
   "stem": "Which of the following statements is best supported by the table?",
   "options": {
    "A": "Country F has a primate city, and Country G's city sizes closely follow the rank-size rule.",
    "B": "Country H follows the rank-size rule, because each city is smaller than the city ranked above it.",
    "C": "Country G has a primate city, and Country F's city sizes closely follow the rank-size rule.",
    "D": "Country H has a primate city, because its largest city has the most people of any city in its country.",
    "E": "Country F follows the rank-size rule, because its largest city is much larger than its other cities."
   },
   "answer": "A",
   "explanation": "Country F's largest city (9.0 million) is more than five times the size of its second city (1.6 million). A city that big compared with the rest is a primate city. Country G fits the rank-size rule: 4.8 ÷ 2 = 2.4, 4.8 ÷ 3 = 1.6, 4.8 ÷ 4 = 1.2, and 4.8 ÷ 5 ≈ 1.0.",
   "whyNot": {
    "B": "Every country's cities get smaller as rank goes down. Under the rule, H's second city would be 3.0 million, not 4.5 million.",
    "C": "This has the two countries backward. G matches the rule; F has the primate city.",
    "D": "Every country's largest city has the most people. A primate city must be MUCH larger (often more than twice) than the second city, and H's is not (6.0 vs. 4.5).",
    "E": "A largest city that dwarfs the others is the sign of a primate city, the opposite of the rank-size rule."
   },
   "vocab": [
    "primate city",
    "rank-size rule"
   ]
  },
  {
   "id": "U6-P13",
   "topic": "6.4",
   "lo": "PSO-6.C",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "POPULATION AND DISTANCE FOR FIVE PAIRS OF CITIES (HYPOTHETICAL DATA)",
    "columns": [
     "City pair",
     "Population of first city",
     "Population of second city",
     "Distance between the cities (km)"
    ],
    "rows": [
     [
      "Pair 1",
      "400,000",
      "100,000",
      "100"
     ],
     [
      "Pair 2",
      "800,000",
      "200,000",
      "400"
     ],
     [
      "Pair 3",
      "200,000",
      "200,000",
      "25"
     ],
     [
      "Pair 4",
      "1,000,000",
      "50,000",
      "200"
     ],
     [
      "Pair 5",
      "900,000",
      "400,000",
      "300"
     ]
    ],
    "source": "Hypothetical data"
   },
   "stem": "Using the gravity model, in which interaction = (population 1 × population 2) ÷ distance², which pair of cities would be expected to have the greatest interaction, such as trips, phone calls, and trade?",
   "options": {
    "A": "Pair 1",
    "B": "Pair 2",
    "C": "Pair 3",
    "D": "Pair 4",
    "E": "Pair 5"
   },
   "answer": "C",
   "explanation": "An interaction index can be calculated as (population 1 × population 2) ÷ distance². Distance matters a LOT because it is squared. Pair 3 is only 25 km apart: 200,000 × 200,000 ÷ 25² = 64,000,000. That beats every other pair. Pair 5 has the largest population product, but its cities are 300 km apart, so its score is only 4,000,000.",
   "whyNot": {
    "A": "Pair 1: 400,000 × 100,000 ÷ 100² = 4,000,000. That is one-sixteenth of Pair 3.",
    "B": "Pair 2: 800,000 × 200,000 ÷ 400² = 1,000,000. The long distance shrinks the interaction.",
    "D": "Pair 4: 1,000,000 × 50,000 ÷ 200² = 1,250,000.",
    "E": "Pair 5 has the largest population product, but 900,000 × 400,000 ÷ 300² = 4,000,000. Remember to SQUARE the distance."
   },
   "vocab": [
    "gravity model",
    "distance decay",
    "spatial interaction"
   ]
  },
  {
   "id": "U6-P14",
   "topic": "6.4",
   "lo": "PSO-6.C",
   "skill": "1.B",
   "difficulty": "medium",
   "stem": "According to central place theory, why does a region usually have many small towns with gas stations and grocery stores but only a few large cities with specialized hospitals and major league sports teams?",
   "options": {
    "A": "Low-order goods need small thresholds and short ranges; high-order services need large thresholds and long ranges.",
    "B": "High-order services have small thresholds, so they can make a profit in towns with very few nearby customers.",
    "C": "Low-order goods have long ranges, so people are willing to travel great distances to buy them in large cities.",
    "D": "Large and small central places are spaced the same distance apart, so each offers the same set of services.",
    "E": "Large cities lie at the edges of hexagonal market areas, where competition from other central places is weakest."
   },
   "answer": "A",
   "explanation": "Threshold = how many customers a business needs to stay open. Range = how far people will travel to get it. People buy gas and groceries often and usually go to nearby sellers, so small market areas can support them. A specialized hospital needs a very large number of patients, and people will travel farther to reach it, so these hospitals are found in higher-order central places.",
   "whyNot": {
    "B": "Backward. High-order services need a LARGE threshold, so they need lots of customers.",
    "C": "Backward. People will not travel far for everyday goods like gas, so those goods have SHORT ranges.",
    "D": "In the theory, larger central places are farther apart and offer more services than smaller ones.",
    "E": "In the theory, central places sit at the CENTER of their hexagonal market areas, not at the edges."
   },
   "vocab": [
    "central place theory",
    "threshold",
    "range",
    "high-order and low-order goods"
   ]
  },
  {
   "id": "U6-P15",
   "topic": "6.4",
   "lo": "PSO-6.C",
   "skill": "1.E",
   "difficulty": "medium",
   "stem": "Central place theory predicts regularly spaced central places, each with a hexagonal market area. Which of the following best explains why real towns in a mountainous region crossed by one major highway often do not match this prediction?",
   "options": {
    "A": "The theory assumes a flat, uniform plain where travel is equally easy in every direction.",
    "B": "The theory was designed to explain where factories locate rather than where services and shops locate.",
    "C": "The theory assumes that shoppers travel to the farthest central place, so it overstates the size of market areas.",
    "D": "The theory assumes that one primate city holds most of the population, so it fails to explain regions with many towns.",
    "E": "The theory leaves out threshold and range, which are especially important in mountainous areas."
   },
   "answer": "A",
   "explanation": "Christaller built his model on a flat, even plain where people can travel the same in every direction. Real places have mountains, rivers, and highways. In a mountain region, towns line up in valleys and along the one big highway instead of forming neat, evenly spaced hexagons.",
   "whyNot": {
    "B": "Central place theory is about services and shops. Weber's model is the one about factory location.",
    "C": "The theory assumes shoppers go to the NEAREST central place that offers what they need.",
    "D": "The theory describes a whole hierarchy of many towns, not one primate city.",
    "E": "Threshold and range are the core ideas of central place theory, not things it leaves out."
   },
   "vocab": [
    "central place theory",
    "hexagonal market area",
    "model assumptions"
   ]
  },
  {
   "id": "U6-P16",
   "topic": "6.5",
   "lo": "PSO-6.D",
   "skill": "4.B",
   "difficulty": "easy",
   "stimulus": {
    "type": "rings",
    "title": "A MODEL OF URBAN LAND USE",
    "center": "CBD",
    "rings": [
     {
      "label": "V"
     },
     {
      "label": "W"
     },
     {
      "label": "X"
     },
     {
      "label": "Y"
     }
    ],
    "outer": "Rural land",
    "description": "Four rings, labeled V, W, X, and Y, surround a central business district (CBD). Ring V touches the CBD; ring Y is farthest from it.",
    "source": "Simplified from the concentric zone model of Ernest W. Burgess (1925)"
   },
   "stem": "According to the concentric zone model shown in the diagram, which area would most likely have older, crowded housing mixed with factories and warehouses, where many newcomers to the city first settled?",
   "options": {
    "A": "The CBD",
    "B": "Ring V",
    "C": "Ring W",
    "D": "Ring X",
    "E": "Ring Y"
   },
   "answer": "B",
   "explanation": "In the Burgess model, the ring right next to the CBD is the zone in transition (ring V). It had factories, warehouses, and old, crowded housing. The model places many newcomers with limited incomes in this zone, and some households move to outer residential zones as their incomes rise.",
   "whyNot": {
    "A": "The CBD is the business center with offices and stores, not the ring of crowded housing and factories.",
    "C": "Ring W is the zone of working-class homes, where many factory workers lived after moving out of ring V.",
    "D": "Ring X is the zone of better, middle-class residences.",
    "E": "Ring Y is the commuters' zone, home to higher-income families farthest from the center."
   },
   "vocab": [
    "concentric zone model",
    "zone in transition",
    "CBD"
   ]
  },
  {
   "id": "U6-P17",
   "topic": "6.5",
   "lo": "PSO-6.D",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "line",
    "title": "BID-RENT CURVES FOR THREE LAND USES IN CITY T (HYPOTHETICAL DATA)",
    "xLabel": "Distance from the center of the CBD (kilometers)",
    "yLabel": "Rent bid ($ per square meter per year)",
    "categories": [
     "0",
     "1",
     "2",
     "3",
     "4",
     "5",
     "6",
     "7",
     "8"
    ],
    "series": [
     {
      "name": "Commercial (stores and offices)",
      "values": [
       1000,
       700,
       450,
       250,
       120,
       50,
       20,
       10,
       5
      ]
     },
     {
      "name": "Industrial",
      "values": [
       500,
       450,
       400,
       340,
       260,
       150,
       90,
       40,
       20
      ]
     },
     {
      "name": "Residential",
      "values": [
       300,
       280,
       260,
       230,
       200,
       185,
       160,
       130,
       100
      ]
     }
    ],
    "yMax": 1000,
    "description": "Line graph of the highest rent that commercial, industrial, and residential users would each pay for land at distances of 0 to 8 kilometers from the center of the CBD.",
    "source": "Hypothetical data"
   },
   "stem": "Based on the graph, which land uses would make the highest bids for land 3 kilometers and 6 kilometers from the center of the CBD, respectively?",
   "options": {
    "A": "Commercial and industrial",
    "B": "Commercial and residential",
    "C": "Residential and industrial",
    "D": "Industrial and residential",
    "E": "Industrial and commercial"
   },
   "answer": "D",
   "explanation": "In bid-rent theory, each piece of land goes to the user who will pay the most, which is the highest line at that distance. At 3 km, industry bids $340, more than commercial users ($250) and residents ($230). At 6 km, residents bid $160, more than industry ($90) and commercial users ($20). Overall, the graph shows the usual pattern: stores and offices near the center, then industry, then housing farther out.",
   "whyNot": {
    "A": "Industry outbids commercial users at 3 km, and residents outbid industry at 6 km.",
    "B": "Residential is right for 6 km, but industry makes the highest bid at 3 km.",
    "C": "Residents make the LOWEST bid at 3 km, and they make the highest bid at 6 km.",
    "E": "Industry is right for 3 km, but residents outbid commercial users at 6 km."
   },
   "vocab": [
    "bid-rent theory",
    "accessibility",
    "CBD"
   ]
  },
  {
   "id": "U6-P18",
   "topic": "6.5",
   "lo": "PSO-6.D",
   "skill": "4.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "schematicMap",
    "title": "LAND USE IN CITY W (HYPOTHETICAL)",
    "canvas": {
     "width": 800,
     "height": 400
    },
    "features": [
     {
      "kind": "zone",
      "name": "CBD",
      "polygon": [
       [
        445.0,
        50.0
       ],
       [
        444.6,
        55.9
       ],
       [
        443.5,
        61.6
       ],
       [
        441.6,
        67.2
       ],
       [
        439.0,
        72.5
       ],
       [
        435.7,
        77.4
       ],
       [
        431.8,
        81.8
       ],
       [
        427.4,
        85.7
       ],
       [
        422.5,
        89.0
       ],
       [
        417.2,
        91.6
       ],
       [
        411.6,
        93.5
       ],
       [
        405.9,
        94.6
       ],
       [
        400.0,
        95.0
       ],
       [
        394.1,
        94.6
       ],
       [
        388.4,
        93.5
       ],
       [
        382.8,
        91.6
       ],
       [
        377.5,
        89.0
       ],
       [
        372.6,
        85.7
       ],
       [
        368.2,
        81.8
       ],
       [
        364.3,
        77.4
       ],
       [
        361.0,
        72.5
       ],
       [
        358.4,
        67.2
       ],
       [
        356.5,
        61.6
       ],
       [
        355.4,
        55.9
       ],
       [
        355.0,
        50.0
       ]
      ],
      "labelAt": [
       400,
       80
      ]
     },
     {
      "kind": "land",
      "name": "High income",
      "style": "small",
      "polygon": [
       [
        800.0,
        50.0
       ],
       [
        800.0,
        67.5
       ],
       [
        800.0,
        85.0
       ],
       [
        800.0,
        102.7
       ],
       [
        800.0,
        120.5
       ],
       [
        800.0,
        138.7
       ],
       [
        800.0,
        157.2
       ],
       [
        800.0,
        176.1
       ],
       [
        800.0,
        195.6
       ],
       [
        800.0,
        215.7
       ],
       [
        800.0,
        236.5
       ],
       [
        800.0,
        258.2
       ],
       [
        800.0,
        280.9
       ],
       [
        800.0,
        304.8
       ],
       [
        800.0,
        330.1
       ],
       [
        800.0,
        356.9
       ],
       [
        800.0,
        385.6
       ],
       [
        434.5,
        78.9
       ],
       [
        435.7,
        77.4
       ],
       [
        436.9,
        75.8
       ],
       [
        438.0,
        74.2
       ],
       [
        439.0,
        72.5
       ],
       [
        439.9,
        70.8
       ],
       [
        440.8,
        69.0
       ],
       [
        441.6,
        67.2
       ],
       [
        442.3,
        65.4
       ],
       [
        442.9,
        63.5
       ],
       [
        443.5,
        61.6
       ],
       [
        443.9,
        59.7
       ],
       [
        444.3,
        57.8
       ],
       [
        444.6,
        55.9
       ],
       [
        444.8,
        53.9
       ],
       [
        445.0,
        52.0
       ],
       [
        445.0,
        50.0
       ]
      ],
      "labelAt": [
       640,
       135
      ]
     },
     {
      "kind": "land",
      "name": "Middle income",
      "style": "land",
      "polygon": [
       [
        800.0,
        385.6
       ],
       [
        800,
        400
       ],
       [
        782.0,
        400.0
       ],
       [
        750.0,
        400.0
       ],
       [
        720.7,
        400.0
       ],
       [
        693.7,
        400.0
       ],
       [
        668.6,
        400.0
       ],
       [
        645.1,
        400.0
       ],
       [
        623.0,
        400.0
       ],
       [
        602.1,
        400.0
       ],
       [
        582.2,
        400.0
       ],
       [
        563.2,
        400.0
       ],
       [
        419.0,
        90.8
       ],
       [
        420.8,
        89.9
       ],
       [
        422.5,
        89.0
       ],
       [
        424.2,
        88.0
       ],
       [
        425.8,
        86.9
       ],
       [
        427.4,
        85.7
       ],
       [
        428.9,
        84.5
       ],
       [
        430.4,
        83.2
       ],
       [
        431.8,
        81.8
       ],
       [
        433.2,
        80.4
       ],
       [
        434.5,
        78.9
       ]
      ],
      "labelAt": [
       585,
       290
      ]
     },
     {
      "kind": "land",
      "name": "Low income",
      "style": "small",
      "polygon": [
       [
        563.2,
        400.0
       ],
       [
        545.5,
        400.0
       ],
       [
        528.4,
        400.0
       ],
       [
        511.8,
        400.0
       ],
       [
        495.7,
        400.0
       ],
       [
        479.9,
        400.0
       ],
       [
        464.4,
        400.0
       ],
       [
        449.2,
        400.0
       ],
       [
        406.3,
        94.6
       ],
       [
        408.1,
        94.3
       ],
       [
        410.0,
        93.9
       ],
       [
        411.9,
        93.4
       ],
       [
        413.7,
        92.9
       ],
       [
        415.5,
        92.2
       ],
       [
        417.3,
        91.6
       ],
       [
        419.0,
        90.8
       ]
      ],
      "labelAt": [
       497,
       372
      ]
     },
     {
      "kind": "land",
      "name": "Industry",
      "style": "land",
      "polygon": [
       [
        449.2,
        400.0
       ],
       [
        432.7,
        400.0
       ],
       [
        416.3,
        400.0
       ],
       [
        400.0,
        400.0
       ],
       [
        383.7,
        400.0
       ],
       [
        367.3,
        400.0
       ],
       [
        350.8,
        400.0
       ],
       [
        393.7,
        94.6
       ],
       [
        395.8,
        94.8
       ],
       [
        397.9,
        95.0
       ],
       [
        400.0,
        95.0
       ],
       [
        402.1,
        95.0
       ],
       [
        404.2,
        94.8
       ],
       [
        406.3,
        94.6
       ]
      ],
      "labelAt": [
       400,
       300
      ]
     },
     {
      "kind": "land",
      "name": "Low income",
      "style": "small",
      "polygon": [
       [
        350.8,
        400.0
       ],
       [
        335.4,
        400.0
       ],
       [
        319.8,
        400.0
       ],
       [
        303.8,
        400.0
       ],
       [
        287.5,
        400.0
       ],
       [
        270.7,
        400.0
       ],
       [
        253.4,
        400.0
       ],
       [
        235.4,
        400.0
       ],
       [
        216.7,
        400.0
       ],
       [
        197.2,
        400.0
       ],
       [
        176.6,
        400.0
       ],
       [
        154.9,
        400.0
       ],
       [
        374.2,
        86.9
       ],
       [
        375.8,
        87.9
       ],
       [
        377.4,
        88.9
       ],
       [
        379.1,
        89.9
       ],
       [
        380.9,
        90.7
       ],
       [
        382.6,
        91.5
       ],
       [
        384.4,
        92.2
       ],
       [
        386.2,
        92.8
       ],
       [
        388.1,
        93.4
       ],
       [
        389.9,
        93.9
       ],
       [
        391.8,
        94.3
       ],
       [
        393.7,
        94.6
       ]
      ],
      "labelAt": [
       270,
       330
      ]
     },
     {
      "kind": "land",
      "name": "Middle income",
      "style": "land",
      "polygon": [
       [
        154.9,
        400.0
       ],
       [
        131.4,
        400.0
       ],
       [
        106.3,
        400.0
       ],
       [
        79.3,
        400.0
       ],
       [
        50.0,
        400.0
       ],
       [
        18.0,
        400.0
       ],
       [
        0,
        400
       ],
       [
        0.0,
        385.6
       ],
       [
        0.0,
        356.9
       ],
       [
        0.0,
        330.1
       ],
       [
        0.0,
        304.8
       ],
       [
        0.0,
        280.9
       ],
       [
        0.0,
        258.2
       ],
       [
        0.0,
        236.5
       ],
       [
        0.0,
        215.7
       ],
       [
        0.0,
        195.6
       ],
       [
        0.0,
        176.1
       ],
       [
        0.0,
        157.2
       ],
       [
        0.0,
        138.7
       ],
       [
        0.0,
        120.5
       ],
       [
        0.0,
        102.7
       ],
       [
        0.0,
        85.0
       ],
       [
        0.0,
        67.5
       ],
       [
        0.0,
        50.0
       ],
       [
        355.0,
        50.0
       ],
       [
        355.0,
        52.0
       ],
       [
        355.2,
        53.9
       ],
       [
        355.4,
        55.9
       ],
       [
        355.7,
        57.8
       ],
       [
        356.1,
        59.7
       ],
       [
        356.5,
        61.6
       ],
       [
        357.1,
        63.5
       ],
       [
        357.7,
        65.4
       ],
       [
        358.4,
        67.2
       ],
       [
        359.2,
        69.0
       ],
       [
        360.1,
        70.8
       ],
       [
        361.0,
        72.5
       ],
       [
        362.0,
        74.2
       ],
       [
        363.1,
        75.8
       ],
       [
        364.3,
        77.4
       ],
       [
        365.5,
        78.9
       ],
       [
        366.8,
        80.4
       ],
       [
        368.2,
        81.8
       ],
       [
        369.6,
        83.2
       ],
       [
        371.1,
        84.5
       ],
       [
        372.6,
        85.7
       ],
       [
        374.2,
        86.9
       ]
      ],
      "labelAt": [
       180,
       170
      ]
     },
     {
      "kind": "shippingLane",
      "name": "Railroad",
      "line": [
       [
        400,
        95
       ],
       [
        400,
        400
       ]
      ],
      "dashed": true
     },
     {
      "kind": "line",
      "name": "Lakeshore boulevard",
      "line": [
       [
        445,
        60
       ],
       [
        800,
        60
       ]
      ],
      "dashed": true
     }
    ],
    "legend": [
     {
      "swatch": "water",
      "label": "Lake"
     },
     {
      "swatch": "lane",
      "label": "Railroad"
     },
     {
      "swatch": "road",
      "label": "Lakeshore boulevard"
     }
    ],
    "description": "City W lies on the south shore of a lake, with its CBD on the shore. Wedge-shaped areas of land use spread out from the CBD. East of the CBD, a high-income wedge runs along a lakeshore boulevard, next to a middle-income wedge. Due south, an industry wedge follows a railroad straight out from the CBD, with low-income wedges on both sides. A second middle-income wedge lies west of the CBD along the lake.",
    "source": "Hypothetical map"
   },
   "stem": "The land-use pattern in City W best supports which model of urban structure?",
   "options": {
    "A": "The Burgess concentric zone model",
    "B": "The Harris and Ullman multiple nuclei model",
    "C": "The galactic city model",
    "D": "Bid-rent theory",
    "E": "The Hoyt sector model"
   },
   "answer": "E",
   "explanation": "Look at the SHAPES. The land uses are wedges (slices of pie) coming out from the CBD, not rings. Industry and low-income housing follow the railroad, and high-income housing follows the lakeshore boulevard. Hoyt's sector model says cities grow outward in wedges along transportation routes and attractive features like a lakeshore.",
   "whyNot": {
    "A": "The Burgess model has rings around the CBD. These areas are wedges, not rings.",
    "B": "The map shows one business center, the CBD, not several separate centers.",
    "C": "There is no beltway or edge city on the map, and the CBD is still the center.",
    "D": "Bid-rent theory links land prices to accessibility. The wedges that follow the railroad and the lakeshore are better explained by Hoyt's sector model."
   },
   "vocab": [
    "sector model",
    "concentric zone model",
    "CBD"
   ]
  },
  {
   "id": "U6-P19",
   "topic": "6.5",
   "lo": "PSO-6.D",
   "skill": "1.E",
   "difficulty": "medium",
   "stem": "Which of the following is a strength of the Harris and Ullman multiple nuclei model, compared with the Burgess concentric zone model, for explaining a large, car-oriented metropolitan area?",
   "options": {
    "A": "It shows that high-income housing extends outward from the CBD in wedges along major transportation routes.",
    "B": "It recognizes that a city can grow around several centers, such as an airport or a university.",
    "C": "It explains why the wealthiest residents of many Latin American cities live along a commercial spine.",
    "D": "It assumes the city sits on a flat plain where land values fall at the same rate in each direction from the CBD.",
    "E": "It focuses on the old colonial port zone as the main center of commercial activity in the city."
   },
   "answer": "B",
   "explanation": "The multiple nuclei model says a city can have several centers, called nuclei. An airport, a university, or a port can each be a center. Each one pulls in its own kinds of businesses and homes. Cars let people spread out, so big metro areas grow around many centers, not just one downtown.",
   "whyNot": {
    "A": "Wedges along transportation routes describe Hoyt's sector model.",
    "C": "The commercial spine with elite housing is part of the Latin American city model.",
    "D": "Assuming one center on a flat plain is a weakness of the concentric zone model, not a strength of the multiple nuclei model.",
    "E": "A colonial port zone at the center is part of the Southeast Asian city model."
   },
   "vocab": [
    "multiple nuclei model",
    "concentric zone model",
    "node"
   ]
  },
  {
   "id": "U6-P20",
   "topic": "6.5",
   "lo": "PSO-6.D",
   "skill": "1.A",
   "difficulty": "medium",
   "stem": "Unlike the Burgess concentric zone model, McGee's model of the Southeast Asian city does not place a single CBD at its center. Instead, the focus of the city is",
   "options": {
    "A": "the old colonial port zone, with commercial districts that grew up around it",
    "B": "three separate business districts: a colonial CBD, a traditional market, and a transitional center",
    "C": "a commercial spine that extends from the CBD, lined on each side by elite housing",
    "D": "a ring of edge cities connected by a beltway around an older downtown",
    "E": "a large squatter settlement that formed the city's original core"
   },
   "answer": "A",
   "explanation": "McGee noticed that many Southeast Asian cities grew around an old colonial PORT. Ships and trade made the port the heart of the city. Commercial districts grew up near the port, and other zones spread out from there.",
   "whyNot": {
    "B": "Three CBDs are part of de Blij's model of the sub-Saharan African city.",
    "C": "A commercial spine with elite housing is part of the Latin American city model.",
    "D": "Edge cities on a beltway describe the galactic (peripheral) city model of North America.",
    "E": "In the models, squatter settlements are usually at the city's edge, not its original core."
   },
   "vocab": [
    "Southeast Asian city model",
    "port zone",
    "colonialism"
   ]
  },
  {
   "id": "U6-P21",
   "topic": "6.5",
   "lo": "PSO-6.D",
   "skill": "2.B",
   "difficulty": "medium",
   "stem": "De Blij's model of the sub-Saharan African city shows three separate CBDs. Which of the following best explains this feature of the model?",
   "options": {
    "A": "Rapid suburbanization of offices created several edge cities around a beltway.",
    "B": "Airports and universities each attracted their own business districts, as in the multiple nuclei model.",
    "C": "The city's wealthiest residents built a commercial spine that extends out from the original CBD.",
    "D": "The city grew around a colonial port zone instead of around a central business district.",
    "E": "Colonial rule added a European-style business district alongside traditional local markets."
   },
   "answer": "E",
   "explanation": "In many African cities, colonial rulers built a European-style downtown with offices and stores. Local open-air markets kept going nearby. A third, in-between kind of business area also grew, with small shops, stalls, and sellers along the curb. So the model has three business centers because of the region's colonial past.",
   "whyNot": {
    "A": "Edge cities along a beltway describe the galactic city model of North America.",
    "B": "The three CBDs come from colonial and traditional commerce, not from airports and universities.",
    "C": "A spine of elite housing and businesses is part of the Latin American city model.",
    "D": "A port zone as the city's focus is part of the Southeast Asian city model."
   },
   "vocab": [
    "African city model",
    "CBD",
    "colonialism"
   ]
  },
  {
   "id": "U6-P22",
   "topic": "6.6",
   "lo": "IMP-6.A",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following is the best example of medium-density housing?",
   "options": {
    "A": "Detached single-family homes on one-acre lots",
    "B": "Rows of attached townhouses with small yards",
    "C": "High-rise apartment towers next to a downtown transit station",
    "D": "Scattered mobile homes on rural land beyond the suburbs",
    "E": "Closely spaced 20-story condominium towers on small lots"
   },
   "answer": "B",
   "explanation": "Density is how many homes fit on a piece of land. Townhouses share walls and sit close together, so they fit more homes than detached houses but far fewer than apartment towers. That middle level is medium density. Detached houses on big lots are low density, and big apartment buildings are high density.",
   "whyNot": {
    "A": "Detached houses on large lots put very few homes on each acre. That is low density.",
    "C": "Apartment towers stack hundreds of homes on a small lot. That is high density.",
    "D": "Scattered homes on rural land are very low density.",
    "E": "Tall, closely spaced buildings put many homes on each acre. That is high density."
   },
   "vocab": [
    "medium-density housing",
    "residential density",
    "townhouse"
   ]
  },
  {
   "id": "U6-P23",
   "topic": "6.6",
   "lo": "IMP-6.A",
   "skill": "3.D",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "HOUSING IN THREE NEIGHBORHOODS OF CITY K (HYPOTHETICAL DATA)",
    "columns": [
     "Neighborhood",
     "Distance from the CBD (km)",
     "Decade when most homes were built",
     "Housing units per hectare",
     "Most common housing type"
    ],
    "rows": [
     [
      "Old Mill",
      "1.5",
      "1910s",
      "60",
      "Apartment buildings and row houses"
     ],
     [
      "Maple Park",
      "7",
      "1950s",
      "12",
      "Detached houses on small lots"
     ],
     [
      "Cedar Ridge",
      "22",
      "2000s",
      "4",
      "Detached houses on large lots"
     ]
    ],
    "source": "Hypothetical data"
   },
   "stem": "Which of the following conclusions is best supported by the data?",
   "options": {
    "A": "Density falls with distance from the CBD, and neighborhoods built in the car era are less dense.",
    "B": "Housing density increases with distance from the CBD, because land at the edge of the city is cheaper.",
    "C": "The oldest neighborhood has the lowest density, because it was built before public transportation existed.",
    "D": "Cedar Ridge is an example of infilling, because it is the neighborhood built most recently.",
    "E": "Maple Park has the highest density, because it was built during the housing boom after World War II."
   },
   "answer": "A",
   "explanation": "Old Mill has 60 homes per hectare, Maple Park has 12, and Cedar Ridge has 4. In these three neighborhoods, density drops as distance from the CBD grows. The newer neighborhoods are also less dense, which fits car-oriented suburban growth from the 1950s on (the table does not measure car ownership).",
   "whyNot": {
    "B": "The numbers go DOWN with distance: 60, then 12, then 4.",
    "C": "Old Mill is the oldest AND the densest. Cities in the 1910s already had streetcars, and people lived close together near jobs and transit.",
    "D": "Infilling means building on empty or underused land inside an area that is already developed. Being built recently and far from the CBD does not show that Cedar Ridge is infill.",
    "E": "Maple Park has 12 homes per hectare. Old Mill, with 60, is the densest."
   },
   "vocab": [
    "residential density",
    "sprawl",
    "infilling"
   ]
  },
  {
   "id": "U6-P24",
   "topic": "6.6",
   "lo": "IMP-6.A",
   "skill": "2.C",
   "difficulty": "medium",
   "stem": "A city rezones vacant lots and surface parking lots in its older neighborhoods so that apartment buildings and townhouses can be built on them. Which outcome is most likely?",
   "options": {
    "A": "Sprawl will increase, because most of the new housing will be built on farmland at the city's outer edge.",
    "B": "Population density in the older neighborhoods will fall as residents move into the new buildings.",
    "C": "The older neighborhoods will become zones of abandonment as businesses leave them.",
    "D": "Population density will rise inside the city, easing pressure to build new housing at its edge.",
    "E": "The city will have to annex land beyond its borders to make room for the new housing."
   },
   "answer": "D",
   "explanation": "Building on empty lots inside the city is called infilling. New apartments and townhouses add more homes to land the city already uses, so more people live in the same area (higher density). If more people can live inside the city, fewer new houses are needed on farmland at the edge.",
   "whyNot": {
    "A": "The new housing goes on lots INSIDE the city, not on farmland at the edge.",
    "B": "Adding apartments to empty lots puts more homes in the same area, so density goes UP.",
    "C": "New housing brings more residents and customers, which usually attracts businesses rather than driving them away.",
    "E": "The new homes fit on land the city already has, so no new land is needed."
   },
   "vocab": [
    "infilling",
    "residential density",
    "zoning"
   ]
  },
  {
   "id": "U6-P25",
   "topic": "6.7",
   "lo": "IMP-6.B",
   "skill": "2.C",
   "difficulty": "easy",
   "stem": "A city opens a new light-rail line that connects several neighborhoods to the CBD. Which change is most likely to occur near the new stations over the next ten years?",
   "options": {
    "A": "Land values will fall as residents move away to avoid the noise of the trains.",
    "B": "Density will decrease as single-family homes replace apartment buildings.",
    "C": "Land values will rise as denser housing and shops are built nearby.",
    "D": "Businesses near the stations will move out toward highway interchanges.",
    "E": "Neighborhoods near the stations will become more cut off from the CBD."
   },
   "answer": "C",
   "explanation": "A train line makes the land near each station easier to reach. Land that is easy to reach is worth more, so prices go up. Builders then put up apartments, offices, and shops near the stations so more people can use the train. Infrastructure changes where development happens.",
   "whyNot": {
    "A": "Better access usually makes land near stations MORE valuable, not less.",
    "B": "Higher land values push builders to build MORE homes per acre, not fewer.",
    "D": "Stations bring riders and customers, which attracts businesses rather than driving them away.",
    "E": "The new line connects these neighborhoods to the CBD, so they become LESS cut off."
   },
   "vocab": [
    "infrastructure",
    "transportation-oriented development",
    "accessibility"
   ]
  },
  {
   "id": "U6-P26",
   "topic": "6.7",
   "lo": "IMP-6.B",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "TRANSPORTATION ACCESS IN FOUR NEIGHBORHOODS OF CITY R (HYPOTHETICAL DATA)",
    "columns": [
     "Neighborhood",
     "Households without a car (%)",
     "Median household income (dollars)",
     "Average one-way commute by public transit (minutes)",
     "Jobs reachable within 45 minutes by public transit"
    ],
    "rows": [
     [
      "Northgate",
      "4",
      "98,000",
      "38",
      "210,000"
     ],
     [
      "Riverside",
      "31",
      "34,000",
      "72",
      "45,000"
     ],
     [
      "Hillcrest",
      "8",
      "76,000",
      "35",
      "190,000"
     ],
     [
      "Eastfield",
      "27",
      "39,000",
      "66",
      "60,000"
     ]
    ],
    "source": "Hypothetical data"
   },
   "stem": "Which of the following conclusions about City R is best supported by the data?",
   "options": {
    "A": "Neighborhoods with the most households that lack cars have the shortest transit commutes, because residents live near their jobs.",
    "B": "Higher-income neighborhoods have the fewest jobs that residents can reach by public transit.",
    "C": "Transit commutes are about the same length in each neighborhood, so access to jobs is roughly equal across the city.",
    "D": "Lower-income neighborhoods have fewer reachable jobs mainly because residents choose jobs within walking distance.",
    "E": "Neighborhoods where many households lack cars have the weakest transit access, which limits residents' access to jobs."
   },
   "answer": "E",
   "explanation": "Riverside and Eastfield have the highest shares of households without cars (31% and 27%). Those are the people who most need buses and trains. But they also have the longest transit commutes (72 and 66 minutes) and can reach the fewest jobs (45,000 and 60,000). Weak transit in these neighborhoods makes it harder for residents to get to work.",
   "whyNot": {
    "A": "Riverside and Eastfield have the LONGEST transit commutes, not the shortest.",
    "B": "Northgate and Hillcrest, the higher-income neighborhoods, can reach the MOST jobs by transit.",
    "C": "Commutes range from 35 to 72 minutes, and job access ranges from 45,000 to 210,000. That is not equal.",
    "D": "The table does not show residents' job choices or jobs within walking distance. It shows unequal access by public transit."
   },
   "vocab": [
    "infrastructure",
    "spatial mismatch",
    "public transit"
   ]
  },
  {
   "id": "U6-P27",
   "topic": "6.7",
   "lo": "IMP-6.B",
   "skill": "2.B",
   "difficulty": "medium",
   "stem": "During the 1950s and 1960s, many new urban interstate highways in the United States were routed through low-income and predominantly Black neighborhoods, splitting them apart and displacing many residents. Which of the following best explains why planners often chose these routes?",
   "options": {
    "A": "Residents of these neighborhoods asked for highways to replace their bus and streetcar lines.",
    "B": "Federal law required interstate highways to pass through each city's oldest neighborhoods.",
    "C": "Planners wanted to raise housing density in these neighborhoods by adding apartments near the highways.",
    "D": "Land there was cheaper to buy, and residents had less political power to stop the projects.",
    "E": "Highways had to follow the routes of old streetcar lines, which ran mainly through these neighborhoods."
   },
   "answer": "D",
   "explanation": "Building a highway means buying and clearing land. Land in low-income neighborhoods cost less. Also, because of discrimination, these residents had little say in city government, so it was hard for them to block the plans. The highways split neighborhoods and forced many families to move. This shows how infrastructure choices reflect who holds political power.",
   "whyNot": {
    "A": "Residents in many of these neighborhoods protested the highways. They did not ask for them.",
    "B": "No federal law required highways to go through a city's oldest neighborhoods. Local and state planners chose the routes.",
    "C": "The highways tore down homes and REDUCED housing in these neighborhoods.",
    "E": "Interstates were new, wide, limited-access roads. They did not have to follow old streetcar lines."
   },
   "vocab": [
    "infrastructure",
    "urban renewal",
    "displacement"
   ]
  },
  {
   "id": "U6-P28",
   "topic": "6.8",
   "lo": "IMP-6.C",
   "skill": "1.D",
   "difficulty": "easy",
   "stem": "A new development has narrow streets, wide sidewalks, homes with front porches set close to the street, and shops and offices within walking distance of most houses. This development best reflects which planning approach?",
   "options": {
    "A": "Single-use zoning",
    "B": "Urban renewal",
    "C": "Suburban sprawl",
    "D": "New Urbanism",
    "E": "A greenbelt policy"
   },
   "answer": "D",
   "explanation": "New Urbanism designs neighborhoods like old-fashioned towns: homes close together, front porches, sidewalks, and shops you can walk to. Mixing homes and businesses means people can walk instead of driving everywhere.",
   "whyNot": {
    "A": "Single-use zoning keeps homes, shops, and offices in SEPARATE areas. This development mixes them.",
    "B": "Urban renewal means redeveloping existing city areas. It is not a particular street and building design; a renewal project could even use New Urbanism.",
    "C": "Sprawl is spread-out, car-dependent growth with homes far from shops.",
    "E": "A greenbelt is a ring of protected open land around a city, not a neighborhood design."
   },
   "vocab": [
    "New Urbanism",
    "mixed land use",
    "walkability"
   ]
  },
  {
   "id": "U6-P29",
   "topic": "6.8",
   "lo": "IMP-6.D",
   "skill": "1.B",
   "difficulty": "medium",
   "stem": "A city allows apartments, offices, and shops to be built within a short walk of each of its commuter rail stations. Which of the following is the benefit that supporters of this transportation-oriented development would most likely point to?",
   "options": {
    "A": "Lower population density near the stations, because buildings are set far apart",
    "B": "More housing on farmland at the city's edge, because development moves outward",
    "C": "Fewer car trips, because more residents can walk to transit, shops, and jobs",
    "D": "Separation of homes from businesses, because each land use gets its own zone",
    "E": "Lower land values near the stations, because rail noise discourages building"
   },
   "answer": "C",
   "explanation": "Transportation-oriented development puts homes, jobs, and stores right next to train stations. People can walk to the train and to shops, so they drive less. Fewer car trips means less traffic and less air pollution.",
   "whyNot": {
    "A": "This kind of development packs MORE homes and businesses near stations, raising density.",
    "B": "The policy directs growth toward rail stations. It does not require building on farmland.",
    "D": "It MIXES homes and businesses together instead of separating them.",
    "E": "Being near a station usually makes land MORE valuable."
   },
   "vocab": [
    "transportation-oriented development",
    "mixed land use",
    "smart growth"
   ]
  },
  {
   "id": "U6-P30",
   "topic": "6.8",
   "lo": "IMP-6.D",
   "skill": "2.C",
   "difficulty": "medium",
   "stem": "City Q surrounds itself with a greenbelt and limits new construction at its edge. Which of the following is the most likely criticism of this policy?",
   "options": {
    "A": "It will lower land values inside the city, because demand for housing there will fall.",
    "B": "It will reduce population density in the city's older neighborhoods.",
    "C": "It will spread homes farther apart, making the city's neighborhoods less walkable.",
    "D": "It will make it harder to protect parks and open space around the city.",
    "E": "It will limit the land available for building, which can push up housing prices."
   },
   "answer": "E",
   "explanation": "A greenbelt protects open land, so there are fewer places to build new homes. If many people still want to live in the city and building inside it does not keep up, housing prices can rise. How much prices rise depends on how much new housing local rules allow inside the city.",
   "whyNot": {
    "A": "Limiting land usually RAISES land values, because the same demand chases less land.",
    "B": "A greenbelt does not make older neighborhoods less dense. Infill can raise density where local rules allow it.",
    "C": "A greenbelt does not spread existing neighborhoods out. Some building may jump beyond the protected belt, but that is a different outcome.",
    "D": "Protecting open space around the city is the main GOAL of a greenbelt."
   },
   "vocab": [
    "greenbelt",
    "smart growth",
    "housing affordability"
   ]
  },
  {
   "id": "U6-P31",
   "topic": "6.9",
   "lo": "IMP-6.E",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "A researcher studying how a neighborhood has changed collects several kinds of information. Which of the following is an example of qualitative data?",
   "options": {
    "A": "Census counts of the neighborhood's total population in 2010 and in 2020",
    "B": "Recorded interviews in which longtime residents describe the changes",
    "C": "The median monthly rent of apartments in the neighborhood from a housing survey",
    "D": "The percentage of the neighborhood's workers who walk or bike to work",
    "E": "The number of new building permits the city issued for the neighborhood each year"
   },
   "answer": "B",
   "explanation": "Qualitative data are words and pictures, like interview answers, field notes, or photos. Quantitative data are numbers, like counts, percents, and averages. Recorded interviews give residents' own words about change. A survey can also turn opinions into numbers. What matters is how the facts are recorded.",
   "whyNot": {
    "A": "Population counts are numbers. That is quantitative data.",
    "C": "A median rent is a number. That is quantitative data.",
    "D": "A percentage is a number. That is quantitative data.",
    "E": "A count of permits is a number. That is quantitative data."
   },
   "vocab": [
    "qualitative data",
    "quantitative data",
    "field study"
   ]
  },
  {
   "id": "U6-P32",
   "topic": "6.9",
   "lo": "IMP-6.E",
   "skill": "3.E",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "SELECTED CENSUS TRACT DATA, CITY L, 2000 AND 2020 (HYPOTHETICAL DATA)",
    "columns": [
     "Census tract",
     "Location",
     "Population, 2000",
     "Population, 2020",
     "Vacant housing units, 2000 (%)",
     "Vacant housing units, 2020 (%)"
    ],
    "rows": [
     [
      "Tract 11",
      "Inner city, near closed factories",
      "6,200",
      "3,900",
      "9",
      "28"
     ],
     [
      "Tract 12",
      "Inner city, next to the CBD",
      "4,800",
      "5,100",
      "6",
      "5"
     ],
     [
      "Tract 45",
      "Edge of the city, former farmland",
      "1,100",
      "7,900",
      "4",
      "3"
     ],
     [
      "Tract 46",
      "Older suburb",
      "5,500",
      "5,600",
      "5",
      "6"
     ]
    ],
    "source": "Hypothetical data. Tract boundaries are the same in both years."
   },
   "stem": "Which of the following processes is best illustrated by the data for Tract 11?",
   "options": {
    "A": "Gentrification, as higher-income households move into and renovate older housing",
    "B": "Suburban sprawl onto former farmland at the edge of the city",
    "C": "Infilling, as new housing is built on vacant lots",
    "D": "The growth of a zone of abandonment as residents leave and homes sit empty",
    "E": "Rising density as apartment buildings replace single-family homes"
   },
   "answer": "D",
   "explanation": "Tract 11 lost more than a third of its people (6,200 down to 3,900), and empty homes jumped from 9% to 28%. It is near factories that have closed. When jobs disappear, people move away, and buildings are left empty. A place like that is called a zone of abandonment.",
   "whyNot": {
    "A": "The table shows no rising incomes, rents, or new investment. A big jump in empty homes points to abandonment, not gentrification.",
    "B": "Sprawl onto farmland fits Tract 45, which grew from 1,100 to 7,900 people at the city's edge.",
    "C": "The table shows no new building on vacant lots. Falling population and many more empty homes point to abandonment, not infilling.",
    "E": "Rising density means more people in the same area. Tract 11's population fell."
   },
   "vocab": [
    "zone of abandonment",
    "census tract",
    "disinvestment"
   ]
  },
  {
   "id": "U6-P33",
   "topic": "6.9",
   "lo": "IMP-6.E",
   "skill": "3.F",
   "difficulty": "hard",
   "stem": "A student uses census tract data from 2010 and 2020 to show that median household income and median rent rose sharply in one neighborhood. Which of the following is a limitation of using only these data to conclude that longtime residents were displaced?",
   "options": {
    "A": "Census tracts are too large to show changes in a single neighborhood of a city.",
    "B": "Ten years is too short a period for census data to show how a neighborhood has changed.",
    "C": "Interviews with residents would give less useful information about the change than the census does.",
    "D": "The data summarize the tract at two dates, not which earlier households moved or why.",
    "E": "Rising rents show that the tract's total population declined during the same decade."
   },
   "answer": "D",
   "explanation": "The medians describe the tract at two points in time. They do not follow the same households. Median income could rise because current residents earned more, richer people moved in, lower-income people moved out, or all three. To know whether housing costs pushed people out, you need to track the earlier households.",
   "whyNot": {
    "A": "Census tracts are small parts of a city, usually a few thousand people each. They are often used to study single neighborhoods.",
    "B": "Ten years is plenty of time to see change. The student's data already show income and rent rising sharply.",
    "C": "Interviews can explain residents' experiences and reasons for moving. The two medians alone cannot.",
    "E": "Rising rent does not prove that population fell. The student's data do not include population at all."
   },
   "vocab": [
    "census tract",
    "displacement",
    "quantitative data",
    "qualitative data"
   ]
  },
  {
   "id": "U6-P34",
   "topic": "6.10",
   "lo": "SPS-6.A",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "In some U.S. cities during the mid-1900s, real estate agents told white homeowners that Black families were moving into their neighborhood and that property values would soon fall. The agents bought the homes cheaply and resold them at much higher prices to Black families. This practice is known as",
   "options": {
    "A": "redlining",
    "B": "gentrification",
    "C": "urban renewal",
    "D": "filtering",
    "E": "blockbusting"
   },
   "answer": "E",
   "explanation": "Blockbusting was a dishonest and discriminatory practice. Agents used racist fears to get white families to sell quickly and cheaply, then sold the same homes for much more to Black families who had few other places they were allowed to buy. The agents made money from both sides, and neighborhoods changed very quickly.",
   "whyNot": {
    "A": "Redlining was banks and government agencies refusing or limiting loans in certain neighborhoods, often because of residents' race.",
    "B": "Gentrification is higher-income people moving into and fixing up a lower-income neighborhood.",
    "C": "Urban renewal was government clearing of old neighborhoods for new projects.",
    "D": "Filtering is housing slowly passing from higher-income to lower-income residents as it ages."
   },
   "vocab": [
    "blockbusting",
    "housing discrimination",
    "redlining"
   ]
  },
  {
   "id": "U6-P35",
   "topic": "6.10",
   "lo": "SPS-6.A",
   "skill": "4.E",
   "difficulty": "medium",
   "stimulus": {
    "type": "schematicMap",
    "title": "NEIGHBORHOOD GRADES ON A 1930s-STYLE MORTGAGE RISK MAP OF CITY H (HYPOTHETICAL)",
    "canvas": {
     "width": 800,
     "height": 400
    },
    "features": [
     {
      "kind": "land",
      "name": "Grade A",
      "style": "small",
      "polygon": [
       [
        0,
        0
       ],
       [
        270,
        0
       ],
       [
        270,
        130
       ],
       [
        0,
        130
       ]
      ],
      "labelAt": [
       135,
       65
      ]
     },
     {
      "kind": "land",
      "name": "Grade B",
      "style": "land",
      "polygon": [
       [
        270,
        0
       ],
       [
        530,
        0
       ],
       [
        530,
        130
       ],
       [
        270,
        130
       ]
      ],
      "labelAt": [
       400,
       65
      ]
     },
     {
      "kind": "land",
      "name": "Grade A",
      "style": "small",
      "polygon": [
       [
        530,
        0
       ],
       [
        800,
        0
       ],
       [
        800,
        130
       ],
       [
        530,
        130
       ]
      ],
      "labelAt": [
       665,
       65
      ]
     },
     {
      "kind": "land",
      "name": "Grade C",
      "style": "land",
      "polygon": [
       [
        0,
        130
       ],
       [
        270,
        130
       ],
       [
        270,
        260
       ],
       [
        0,
        260
       ]
      ],
      "labelAt": [
       135,
       195
      ]
     },
     {
      "kind": "land",
      "name": "CBD",
      "style": "power",
      "polygon": [
       [
        270,
        130
       ],
       [
        530,
        130
       ],
       [
        530,
        260
       ],
       [
        270,
        260
       ]
      ],
      "labelAt": [
       400,
       195
      ]
     },
     {
      "kind": "land",
      "name": "Grade C",
      "style": "land",
      "polygon": [
       [
        530,
        130
       ],
       [
        800,
        130
       ],
       [
        800,
        260
       ],
       [
        530,
        260
       ]
      ],
      "labelAt": [
       665,
       195
      ]
     },
     {
      "kind": "land",
      "name": "Grade D",
      "style": "small",
      "polygon": [
       [
        0,
        260
       ],
       [
        400,
        260
       ],
       [
        400,
        340
       ],
       [
        0,
        340
       ]
      ],
      "labelAt": [
       200,
       300
      ]
     },
     {
      "kind": "land",
      "name": "Factories and rail yards",
      "style": "land",
      "polygon": [
       [
        400,
        260
       ],
       [
        800,
        260
       ],
       [
        800,
        340
       ],
       [
        400,
        340
       ]
      ],
      "labelAt": [
       600,
       300
      ]
     },
     {
      "kind": "line",
      "name": "Rail line",
      "line": [
       [
        0,
        260
       ],
       [
        800,
        260
       ]
      ],
      "dashed": true
     }
    ],
    "legend": [
     {
      "swatch": "water",
      "label": "River"
     },
     {
      "swatch": "road",
      "label": "Rail line"
     }
    ],
    "note": "Grades recorded appraisers' judgments of the risk of lending money for home loans, often shaped by racial and ethnic discrimination: Grade A = \"best\" through Grade D = \"hazardous.\" On the original federal maps, Grade D areas were shaded red.",
    "description": "Map of City H. Two Grade A neighborhoods and one Grade B neighborhood lie along the northern edge, farthest from the river. Two Grade C neighborhoods lie on either side of the CBD. In the south, between a rail line and the river, a Grade D neighborhood sits next to factories and rail yards.",
    "source": "Hypothetical map modeled on the residential security maps of the federal Home Owners' Loan Corporation (1930s)"
   },
   "stem": "Which of the following was commonly associated over the long term with neighborhoods given the grade shown between the rail line and the river?",
   "options": {
    "A": "Lenders competed to make loans there, which led to rapid gentrification in the 1940s.",
    "B": "The grade protected the neighborhood from later highway construction and urban renewal projects in the city.",
    "C": "Banks offered home loans there at the lowest interest rates in the city, which drew new suburban-style development.",
    "D": "The grade required the city to rezone the neighborhood for low-density, single-family homes.",
    "E": "Lenders often refused or limited home loans there, leading to disinvestment and low home values for decades."
   },
   "answer": "E",
   "explanation": "Grade D marked neighborhoods that appraisers called hazardous for lending, often based on discriminatory judgments about the people who lived there. In many such neighborhoods, residents had a hard time getting home loans. That made it harder to buy or repair homes and build wealth, which helped create inequalities that lasted for decades. This practice is called redlining.",
   "whyNot": {
    "A": "A \"hazardous\" grade scared lenders AWAY. It did not make them compete to lend there.",
    "B": "Redlined neighborhoods were often the ones chosen LATER for highways and urban renewal.",
    "C": "Lenders charged more or refused to lend in Grade D areas. Federal loan programs of the time favored new suburbs instead.",
    "D": "The grades were about lending risk. They did not rezone land."
   },
   "vocab": [
    "redlining",
    "disinvestment",
    "housing discrimination"
   ]
  },
  {
   "id": "U6-P36",
   "topic": "6.10",
   "lo": "SPS-6.A",
   "skill": "2.B",
   "difficulty": "medium",
   "stem": "In some rapidly growing cities, residents have built squatter settlements without formal permission to occupy the land, sometimes on steep hillsides or floodplains. Which of the following best explains why these settlements may lack piped water, sewers, and electricity?",
   "options": {
    "A": "Their high population density leaves too little open land for water pipes and power lines.",
    "B": "Most of these neighborhoods are inside the CBD, where land is reserved for offices and stores.",
    "C": "Bid-rent theory predicts that utilities will be built first at the urban edge, where land is cheapest.",
    "D": "Uncertain land rights and limited official recognition can delay investment in basic services.",
    "E": "Steep hillsides and floodplains are usually too far from the CBD for water and power lines to reach."
   },
   "answer": "D",
   "explanation": "Land tenure means a person's right to use or live on a piece of land. In many squatter settlements that right is not clear, and the city does not officially count the neighborhood. So the city and utility companies are slow to put in pipes and power lines. Lack of money and very fast growth can slow things down too.",
   "whyNot": {
    "A": "Dense neighborhoods in many cities have full water and power service. Density is not the barrier.",
    "B": "Squatter settlements usually form on unused or risky land, often at the city's edge, not mostly in the CBD. A CBD location is not why services are missing.",
    "C": "Bid-rent theory explains land values and land use. It does not say utilities are built first at the edge.",
    "E": "Distance is not the main barrier. Many squatter settlements are close to areas that have services; some hillside favelas in Rio de Janeiro sit right above wealthy neighborhoods."
   },
   "vocab": [
    "squatter settlement",
    "land tenure",
    "informal settlement"
   ]
  },
  {
   "id": "U6-P37",
   "topic": "6.10",
   "lo": "SPS-6.A",
   "skill": "2.C",
   "difficulty": "medium",
   "stem": "Higher-income households begin buying and renovating older homes in a low-income inner-city neighborhood. New cafés and shops open, and property values rise. Which of the following is the most likely negative consequence for longtime residents?",
   "options": {
    "A": "Rising rents and property taxes may price some of them out of the neighborhood.",
    "B": "The neighborhood's tax base may shrink, reducing the money available for city services.",
    "C": "Urban renewal may clear the neighborhood's homes to make room for highways and offices.",
    "D": "The neighborhood may become a zone of abandonment as investment leaves it.",
    "E": "Lenders may begin redlining the neighborhood and refuse to make loans there."
   },
   "answer": "A",
   "explanation": "This is gentrification. Fixed-up homes and new shops make the neighborhood more desirable, so rents and property taxes go up. Some longtime residents, especially renters with low incomes, can no longer afford to stay and have to move. That is called displacement.",
   "whyNot": {
    "B": "Rising property values make the tax base GROW, not shrink.",
    "C": "Urban renewal is a government program that clears old neighborhoods. Here private buyers are fixing up homes, which is gentrification.",
    "D": "Money is flowing INTO this neighborhood, the opposite of abandonment.",
    "E": "Lenders are investing here. Redlining was the refusal to lend in certain neighborhoods."
   },
   "vocab": [
    "gentrification",
    "displacement",
    "affordability"
   ]
  },
  {
   "id": "U6-P38",
   "topic": "6.10",
   "lo": "SPS-6.A",
   "skill": "5.B",
   "difficulty": "hard",
   "stem": "A metropolitan area includes one central city, more than 80 suburban municipalities, several counties, dozens of school districts, and separate water and transit agencies. The region struggles to agree on a transit line that would link low-income neighborhoods in the central city to jobs in the suburbs. Which concept best explains this challenge?",
   "options": {
    "A": "Primacy, because the central city is much larger than any one of its suburbs",
    "B": "Central place theory, because each suburb has its own threshold and range for its public services",
    "C": "Redlining, because lenders refuse to finance new transit lines that serve low-income neighborhoods",
    "D": "Annexation, because the central city has absorbed its suburbs into one government",
    "E": "Fragmentation of local government, which splits authority among many units at different scales"
   },
   "answer": "E",
   "explanation": "Power is split among many governments: a city, more than 80 suburbs, several counties, school districts, and special agencies. A transit line that crosses many of their borders needs agreement on the route, money, and approvals, and each has its own priorities. That makes regional problems hard to solve. Your AP course guide calls this functional and geographic fragmentation of governments.",
   "whyNot": {
    "A": "Primacy is about city size in a country. It does not explain why many governments struggle to agree.",
    "B": "Central place theory explains where goods and services are offered, not how governments make decisions.",
    "C": "Redlining was about home loans, not transit planning.",
    "D": "Annexation brings land into a city. The stem describes the opposite: many separate local governments."
   },
   "vocab": [
    "fragmentation of local government",
    "metropolitan area",
    "scale"
   ]
  },
  {
   "id": "U6-P39",
   "topic": "6.11",
   "lo": "SPS-6.B",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "An abandoned factory site near a city's downtown has soil that may be contaminated from past industrial use. The city plans to clean up the site and build housing and a park there. This project is an example of",
   "options": {
    "A": "brownfield redevelopment",
    "B": "greenfield development",
    "C": "a greenbelt policy",
    "D": "an urban growth boundary",
    "E": "suburban sprawl at the urban edge"
   },
   "answer": "A",
   "explanation": "A brownfield is a property that may be polluted, which makes it harder to reuse. Old factories, gas stations, and dry cleaners are examples. Remediation means cleaning it up, and redevelopment means building something new on it. Reusing the site adds homes or a park without building on open land at the edge.",
   "whyNot": {
    "B": "A greenfield is land that has never been built on, like farmland. This site was a factory.",
    "C": "A greenbelt is a ring of protected open land around a city.",
    "D": "An urban growth boundary is a line that limits where a city can grow.",
    "E": "Sprawl is spread-out building at the city's edge. This project reuses land near downtown."
   },
   "vocab": [
    "brownfield",
    "remediation",
    "redevelopment"
   ]
  },
  {
   "id": "U6-P40",
   "topic": "6.11",
   "lo": "SPS-6.B",
   "skill": "3.D",
   "difficulty": "medium",
   "stimulus": {
    "type": "bar",
    "title": "FARMLAND CONVERTED TO URBAN USE EACH YEAR IN TWO METROPOLITAN AREAS (HYPOTHETICAL DATA)",
    "yLabel": "Hectares per year (average)",
    "categories": [
     "2000–2009",
     "2010–2019"
    ],
    "series": [
     {
      "name": "Metro A",
      "values": [
       1800,
       600
      ]
     },
     {
      "name": "Metro B",
      "values": [
       1700,
       1900
      ]
     }
    ],
    "text": "Metro A adopted an urban growth boundary in 2010. Metro B did not.",
    "description": "Grouped bar chart. Metro A converted an average of 1,800 hectares of farmland per year in 2000–2009 and 600 hectares per year in 2010–2019. Metro B converted 1,700 hectares per year in 2000–2009 and 1,900 hectares per year in 2010–2019.",
    "source": "Hypothetical data"
   },
   "stem": "Which conclusion is best supported by the graph?",
   "options": {
    "A": "The growth boundary appears to have increased the amount of farmland Metro A converted.",
    "B": "The two metro areas converted farmland at about the same rate after 2010.",
    "C": "Farmland loss slowed in Metro A after its boundary took effect but grew in Metro B.",
    "D": "Metro B converted less farmland per year than Metro A in both periods shown.",
    "E": "The growth boundary appears to have raised housing prices inside Metro A during the 2010s."
   },
   "answer": "C",
   "explanation": "After Metro A drew its growth boundary in 2010, its farmland loss dropped from 1,800 to 600 hectares a year, a two-thirds drop. Metro B, with no boundary, went UP from 1,700 to 1,900. Comparing the two suggests the boundary helped protect farmland from sprawl.",
   "whyNot": {
    "A": "Metro A's farmland loss went DOWN after 2010, from 1,800 to 600 hectares a year.",
    "B": "After 2010, Metro B converted more than three times as much farmland as Metro A (1,900 vs. 600).",
    "D": "That is true for 2000–2009 (1,700 vs. 1,800), but not for 2010–2019 (1,900 vs. 600).",
    "E": "Housing prices may rise with a growth boundary, but the graph shows only farmland, not prices."
   },
   "vocab": [
    "urban growth boundary",
    "farmland protection",
    "sprawl"
   ]
  },
  {
   "id": "U6-P41",
   "topic": "6.11",
   "lo": "SPS-6.B",
   "skill": "2.D",
   "difficulty": "medium",
   "stem": "Which of the following best explains why many fast-growing cities in periphery countries face greater sanitation challenges than most cities in core countries?",
   "options": {
    "A": "Cities in periphery countries have larger ecological footprints per person than cities in core countries.",
    "B": "Urban growth boundaries in periphery countries prevent water pipes from reaching the edges of cities.",
    "C": "Population growth has outpaced the building of sewers and water treatment plants.",
    "D": "Cities in periphery countries have such low population densities that sewer systems are not practical.",
    "E": "Most of the growth in these cities comes from gentrification of older neighborhoods near the CBD."
   },
   "answer": "C",
   "explanation": "In many fast-growing cities, people arrive faster than new water pipes and sewers can be built. Building them takes a lot of time and money, so the gap grows. The key is how fast the population grows compared with how fast pipes and treatment plants are added. Conditions also differ from city to city.",
   "whyNot": {
    "A": "People in core countries use more resources, so core cities usually have LARGER footprints per person.",
    "B": "Growth boundaries limit where building happens. Nothing in the stem points to them as the reason sanitation has fallen behind.",
    "D": "Many of these cities are very dense. Low density is not the reason sanitation lags.",
    "E": "Gentrification changes who lives in existing neighborhoods. It does not explain the overall growth pressure on sanitation systems."
   },
   "vocab": [
    "sanitation",
    "informal settlement",
    "urban sustainability"
   ]
  },
  {
   "id": "U6-P42",
   "topic": "6.5",
   "lo": "PSO-6.D",
   "skill": "1.D",
   "difficulty": "medium",
   "stem": "A U.S. metropolitan area still has its old downtown, but most of its office jobs and big stores are now spread among several suburban centers near interchanges on a ring highway and near the airport. Suburban neighborhoods fill the land between these centers. Which model of urban structure best describes this metropolitan area?",
   "options": {
    "A": "The Burgess concentric zone model",
    "B": "The Hoyt sector model",
    "C": "The Latin American (Griffin–Ford) city model",
    "D": "The galactic city (peripheral) model",
    "E": "The Southeast Asian (McGee) city model"
   },
   "answer": "D",
   "explanation": "The galactic city model is also called the peripheral model. A ring highway (beltway) links many suburban centers, like edge cities, office parks, and the airport. The old downtown is still there, but it is no longer the only place for jobs and shopping. Homes fill the spaces in between.",
   "whyNot": {
    "A": "The Burgess model has rings of land use around ONE CBD. Here, jobs and stores are spread among suburban centers.",
    "B": "Hoyt's wedges grow outward from the CBD along routes. They do not show suburban centers along a ring highway.",
    "C": "The Latin American model has an elite spine running out from the CBD and poor settlements at the edge, not suburban job centers on a beltway.",
    "E": "The Southeast Asian model centers on an old colonial port zone, not a ring highway with suburban centers."
   },
   "vocab": [
    "galactic city model",
    "peripheral model",
    "edge city",
    "beltway"
   ]
  },
  {
   "id": "U6-P43",
   "topic": "6.2",
   "lo": "PSO-6.A",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following best describes the difference between a megacity and a metacity?",
   "options": {
    "A": "A metacity is a world city that controls global finance; a megacity is any city with a large population.",
    "B": "A metacity has more than 20 million people; a megacity has 10 million or more.",
    "C": "A metacity is a ring of edge cities around a beltway; a megacity has a single CBD.",
    "D": "A metacity is more than twice the size of its country's second city; a megacity is not.",
    "E": "A metacity grows mainly through suburbanization; a megacity grows mainly through migration."
   },
   "answer": "B",
   "explanation": "Both words are about size. A megacity has 10 million or more people. A metacity is even bigger: more than 20 million people. Your AP course guide says both are increasingly found in semiperiphery and periphery countries.",
   "whyNot": {
    "A": "Control of global finance makes a city a world city. Metacity is about population size.",
    "C": "A ring of edge cities around a beltway describes the galactic city model, not a metacity.",
    "D": "A city that much bigger than its country's second city is a primate city.",
    "E": "The two terms are defined by population size, not by how the city grows."
   },
   "vocab": [
    "metacity",
    "megacity",
    "urban hierarchy"
   ]
  },
  {
   "id": "U6-P44",
   "topic": "6.10",
   "lo": "SPS-6.A",
   "skill": "3.E",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "SELECTED CONDITIONS IN FOUR NEIGHBORHOODS OF CITY J (HYPOTHETICAL DATA)",
    "columns": [
     "Neighborhood",
     "Households below the poverty line (%)",
     "Distance to the nearest highway or large factory (meters)",
     "Days per year with unhealthy air at the local monitor",
     "Tree canopy cover (%)"
    ],
    "rows": [
     [
      "Elm Hollow",
      "8",
      "1,900",
      "4",
      "38"
     ],
     [
      "Larkspur",
      "34",
      "150",
      "22",
      "9"
     ],
     [
      "Millbank",
      "29",
      "250",
      "19",
      "12"
     ],
     [
      "Ridgeview",
      "11",
      "1,600",
      "6",
      "31"
     ]
    ],
    "source": "Hypothetical data"
   },
   "stem": "The pattern in the table best illustrates which of the following?",
   "options": {
    "A": "Gentrification",
    "B": "Transportation-oriented development",
    "C": "Counterurbanization",
    "D": "Environmental injustice",
    "E": "Blockbusting"
   },
   "answer": "D",
   "explanation": "Look at who lives closest to pollution. Larkspur and Millbank have the most households in poverty (34% and 29%). They are also closest to highways or factories (150 and 250 meters), have the most days with unhealthy air (22 and 19), and have the least tree cover. When lower-income neighborhoods carry more of a city's pollution and get fewer of its green spaces, that is called environmental injustice.",
   "whyNot": {
    "A": "Gentrification is a change over time, as higher-income people move in. The table shows one point in time, not a change in who lives there.",
    "B": "Transportation-oriented development puts housing and shops near transit stations. The table is about pollution exposure, not transit.",
    "C": "Counterurbanization is people moving from cities to rural areas. The table compares neighborhoods within one city.",
    "E": "Blockbusting was real estate agents using racial fear to buy homes cheaply and resell them. The table is about pollution, not home sales."
   },
   "vocab": [
    "environmental injustice",
    "air quality",
    "disamenity"
   ]
  },
  {
   "id": "U6-P45",
   "topic": "6.10",
   "lo": "SPS-6.A",
   "skill": "2.C",
   "difficulty": "medium",
   "stem": "Several neighborhoods in a city have no full-service grocery store within walking distance. The city helps residents turn vacant lots into community gardens and opens a weekly farmers' market that accepts food assistance benefits. Which outcome is most likely?",
   "options": {
    "A": "Most households will grow enough of their own food that the neighborhoods will no longer need grocery stores.",
    "B": "Large supermarket chains will soon open full-service stores there, because the market shows strong demand.",
    "C": "Residents will gain better access to fresh produce, though they will still need other food stores.",
    "D": "Property values will fall, because community gardens and markets make neighborhoods less attractive.",
    "E": "Food prices across the whole city will fall sharply, because local produce costs less to ship."
   },
   "answer": "C",
   "explanation": "Community gardens and farmers' markets are part of the local food movement. They bring fresh fruits and vegetables close to people who have few places to buy them. Taking food assistance benefits helps families with less money shop there. But a few gardens and a weekly market are small, so families still need other stores.",
   "whyNot": {
    "A": "Gardens on a few vacant lots cannot feed whole neighborhoods. They add some fresh food, not most of it.",
    "B": "A few gardens and a weekly market do not prove enough steady demand to bring a full supermarket.",
    "D": "Turning vacant lots into gardens usually makes a block MORE attractive, not less.",
    "E": "A few gardens and one weekly market are too small to change food prices across a whole city."
   },
   "vocab": [
    "local food movement",
    "food desert",
    "community garden"
   ]
  },
  {
   "id": "U6-P46",
   "topic": "6.11",
   "lo": "SPS-6.B",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "bar",
    "title": "AVERAGE SUMMER AFTERNOON SURFACE TEMPERATURE BY LAND COVER IN CITY V (HYPOTHETICAL DATA)",
    "yLabel": "Surface temperature (°C)",
    "categories": [
     "Downtown core",
     "Tree-lined area",
     "City park",
     "Farmland"
    ],
    "series": [
     {
      "name": "Average surface temperature (°C)",
      "values": [
       48,
       38,
       31,
       33
      ]
     }
    ],
    "yMax": 60,
    "text": "Downtown core: mostly rooftops and pavement. Tree-lined area: an older neighborhood with many street trees. City park: grass and trees. Farmland: crops outside the city.",
    "description": "Bar chart of average summer afternoon surface temperature in four kinds of places in City V: downtown core 48°C, tree-lined area 38°C, city park 31°C, farmland outside the city 33°C.",
    "source": "Hypothetical data"
   },
   "stem": "Based on the graph, which strategy would most likely lower summer surface temperatures in City V's downtown core?",
   "options": {
    "A": "Replacing downtown parks with paved parking to speed the flow of traffic",
    "B": "Converting more land outside the city to farmland, since farmland is cooler than downtown",
    "C": "Building taller downtown towers closer together to trap cool air",
    "D": "Replacing the city park with tree-lined housing, since tree-lined areas are cooler than downtown",
    "E": "Adding street trees, green roofs, and small parks among the downtown buildings"
   },
   "answer": "E",
   "explanation": "Downtown, covered in rooftops and pavement, is the hottest place on the graph (48°C). The city park (31°C) and the tree-lined area (38°C) are much cooler, because plants shade surfaces and release water that cools the air. Adding trees, green roofs, and small parks downtown matches what the graph shows. Extra heat in built-up areas is called the urban heat island effect.",
   "whyNot": {
    "A": "Pavement soaks up heat. The graph shows the paved downtown is the hottest land cover, so more pavement would make it hotter.",
    "B": "Farmland is cooler, but it is outside the city. More farmland there would not cool the rooftops and pavement downtown.",
    "C": "Tall buildings packed close together trap heat between them and block cooling breezes.",
    "D": "The park (31°C) is cooler than tree-lined areas (38°C), and this change happens outside the downtown core."
   },
   "vocab": [
    "urban heat island",
    "green roof",
    "urban sustainability"
   ]
  },
  {
   "id": "U6-P47",
   "topic": "6.8",
   "lo": "IMP-6.D",
   "skill": "2.C",
   "difficulty": "medium",
   "stem": "A city rezones a neighborhood of 100-year-old two-story shops and row houses so that eight-story mixed-use buildings can be built near a new light-rail station. Which criticism would opponents of the plan most likely raise?",
   "options": {
    "A": "Older buildings could be torn down, weakening the historic character of the neighborhood's streets.",
    "B": "It could increase sprawl, because mixed-use buildings use more land per resident than row houses.",
    "C": "It could separate homes from stores, because mixed-use zoning puts housing and shops in different districts.",
    "D": "It could lower land values near the station, because rail stations make nearby land less accessible.",
    "E": "It could make the area less walkable, because mixed-use buildings face parking lots instead of sidewalks."
   },
   "answer": "A",
   "explanation": "Building taller near transit is a smart-growth idea, and it can add homes and riders. But to make room, old shops and row houses may be torn down. Your AP course guide lists the possible loss of historical or place character as a criticism of urban design initiatives like this one.",
   "whyNot": {
    "B": "Mixed-use buildings stack homes and shops, so they use LESS land per person and ease pressure to build on farmland.",
    "C": "Mixed-use zoning puts homes and shops in the SAME building or block. Single-use zoning separates them.",
    "D": "A rail station makes nearby land EASIER to reach, so land values usually rise.",
    "E": "Mixed-use buildings near transit are usually built up to the sidewalk with shops on the ground floor, which makes walking easier."
   },
   "vocab": [
    "historic preservation",
    "place character",
    "transportation-oriented development",
    "mixed land use"
   ]
  }
 ],
 "exam": {
  "title": "Unit 6 Practice Exam: Cities and Urban Land-Use Patterns and Processes",
  "timeMinutes": 25,
  "questionCount": 25,
  "directions": "Each of the questions or incomplete statements below is followed by five suggested answers or completions. Select the one that is best in each case. Your score is based only on the number of questions answered correctly, so answer every question. Work quickly without losing accuracy, and come back to any question you skipped if time allows.",
  "stimulusCount": 10,
  "questions": [
   {
    "id": "U6-E01",
    "n": 1,
    "topic": "6.1",
    "lo": "PSO-6.A",
    "skill": "2.B",
    "difficulty": "medium",
    "stem": "Which of the following best explains why cities such as Richmond, Virginia, and Trenton, New Jersey, grew up along the Atlantic Seaboard fall line?",
    "options": {
     "A": "The fall line marks where wide river deltas meet the ocean, creating deep natural harbors for ocean ships.",
     "B": "Colonial governments required new towns to be built at equal distances from the Atlantic coast.",
     "C": "Waterfalls powered mills and blocked river boats, so cargo was moved between boats and land transport.",
     "D": "Steep, rocky land along the fall line was poor for farming, so settlers there turned to fishing instead.",
     "E": "The fall line formed the boundary between British and French colonial claims, so forts were built along it."
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. The fall line lies inland, where rivers drop from the harder rocks of the Piedmont to the softer Coastal Plain, not at river mouths on the ocean.",
     "B": "Incorrect. No colonial rule required towns to be spaced evenly from the coast; fall line cities grew because of the advantages of their site and situation.",
     "C": "Correct. Falls and rapids gave the site water power for mills, and they marked the head of navigation, so the situation made these places break-of-bulk points where cargo moved between river boats and wagons or rail.",
     "D": "Incorrect. Fall line cities grew as milling and trading centers, not fishing towns, and much of the surrounding Piedmont was farmed.",
     "E": "Incorrect. The fall line was not a colonial boundary; British and French rivalry centered farther west and north, in areas such as the Ohio Valley and the Great Lakes region."
    },
    "explanation": "Along the fall line, rivers drop over waterfalls. The falling water could turn mill wheels (a SITE advantage). Boats coming up from the coast could not get past the falls, so goods had to be unloaded and moved by land there (a SITUATION advantage). Both helped towns grow at the falls."
   },
   {
    "id": "U6-E02",
    "n": 2,
    "set": "urbanshare",
    "setLabel": "Questions 2–3 refer to the graph below.",
    "topic": "6.1",
    "lo": "PSO-6.A",
    "skill": "3.D",
    "difficulty": "medium",
    "stimulus": {
     "type": "line",
     "title": "URBAN POPULATION AS A PERCENTAGE OF TOTAL POPULATION, SELECTED COUNTRIES, 1960–2020",
     "xLabel": "Year",
     "yLabel": "Urban population (% of total population)",
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
       "name": "United Kingdom",
       "values": [
        78.6,
        76.9,
        78.6,
        78.1,
        79.8,
        81.0,
        82.9
       ]
      },
      {
       "name": "China",
       "values": [
        19.7,
        17.4,
        19.4,
        26.2,
        36.4,
        49.2,
        63.5
       ]
      },
      {
       "name": "Nigeria",
       "values": [
        14.2,
        20.2,
        27.4,
        35.2,
        43.3,
        51.7,
        59.8
       ]
      },
      {
       "name": "India",
       "values": [
        17.9,
        19.7,
        23.5,
        25.6,
        27.6,
        30.9,
        34.1
       ]
      }
     ],
     "yMax": 100,
     "description": "Line graph of the percentage of each country's population living in urban areas, every ten years from 1960 to 2020.",
     "source": "World Bank, World Development Indicators, indicator SP.URB.TOTL.IN.ZS, Urban population (% of total population), from UN Population Division, World Urbanization Prospects (national definitions of urban). Data last updated Oct 8, 2026; accessed Nov 8, 2026. Values rounded to one decimal."
    },
    "stem": "Which of the following statements is best supported by the graph?",
    "options": {
     "A": "Nigeria's urban share was higher than China's in both 1960 and 2020.",
     "B": "Of the four countries, China's urban share rose by the most percentage points from 1980 to 2020.",
     "C": "India's urban share rose by more percentage points between 1990 and 2020 than Nigeria's urban share did.",
     "D": "The gap between the United Kingdom's and China's urban shares was larger in 2020 than in 1960.",
     "E": "China's urban share was higher than India's in 1980."
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. China's urban share was higher than Nigeria's in both years: 19.7 vs. 14.2 percent in 1960 and 63.5 vs. 59.8 percent in 2020.",
     "B": "Correct. China's urban share rose from 19.4 to 63.5 percent, a gain of about 44 percentage points. Nigeria gained about 32 points, India about 11, and the United Kingdom about 4.",
     "C": "Incorrect. India's urban share rose about 8.5 points (25.6 to 34.1), while Nigeria's rose about 24.6 points (35.2 to 59.8).",
     "D": "Incorrect. The gap narrowed from about 59 percentage points in 1960 (78.6 vs. 19.7 percent) to about 19 points in 2020 (82.9 vs. 63.5 percent).",
     "E": "Incorrect. In 1980, China's urban share (19.4 percent) was lower than India's (23.5 percent)."
    },
    "explanation": "Subtract to find each country's gain from 1980 to 2020. China: 63.5 − 19.4 = about 44 points. Nigeria: about 32. India: about 11. The United Kingdom: about 4. China's line climbs the most."
   },
   {
    "id": "U6-E03",
    "n": 3,
    "set": "urbanshare",
    "topic": "6.2",
    "lo": "PSO-6.A",
    "skill": "2.D",
    "difficulty": "medium",
    "stem": "The rapid urbanization of China and Nigeria shown in the graph is most closely associated with which of the following global patterns?",
    "options": {
     "A": "Counterurbanization, as residents of large cities move to small towns and rural areas",
     "B": "Deindustrialization, as factory jobs move from semiperiphery countries to core countries",
     "C": "New world cities in Asia and Africa replacing London and New York at the top of the global urban hierarchy",
     "D": "The decline of primate cities, as governments move their capitals to smaller cities",
     "E": "The growing share of the world's megacities located in semiperiphery and periphery countries"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. Counterurbanization would lower the urban share; the graph shows China's and Nigeria's urban shares rising steeply.",
     "B": "Incorrect. Since the late 1900s, much manufacturing has shifted from core countries toward semiperiphery and periphery countries such as China, not the other way.",
     "C": "Incorrect. London and New York remain at the top of the global urban hierarchy; rising urban shares do not by themselves create world cities.",
     "D": "Incorrect. The graph shows national urban shares, not the size of capital cities, and rapid urbanization has not generally produced a decline in primate cities.",
     "E": "Correct. Because of rapid urbanization in semiperiphery and periphery countries, most of today's megacities, such as Shanghai and Lagos, are located outside the core."
    },
    "explanation": "China and Nigeria became much more urban very quickly. Fast city growth in semiperiphery and periphery countries is part of why most megacities are now outside the core. A megacity has 10 million or more people. Shanghai and Lagos are examples. The graph shows national percentages, not the size of single cities."
   },
   {
    "id": "U6-E04",
    "n": 4,
    "topic": "6.2",
    "lo": "PSO-6.A",
    "skill": "1.D",
    "difficulty": "easy",
    "stem": "Families move into new subdivisions of homes on large lots about 50 miles from a city's CBD, in a county that was mostly farmland ten years ago. Most adults drive long distances to jobs elsewhere in the metropolitan area. This type of place is best described as",
    "options": {
     "A": "an exurb",
     "B": "an edge city",
     "C": "a boomburb",
     "D": "a New Urbanist development",
     "E": "a zone in transition"
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. Exurbs are low-density residential areas beyond the suburbs, often on former farmland, whose residents commute long distances to jobs in the metropolitan area.",
     "B": "Incorrect. An edge city is a suburban node with large amounts of office and retail space and more jobs than residents.",
     "C": "Incorrect. A boomburb is a rapidly growing suburban city of more than 100,000 people, not a scattering of new subdivisions on the rural fringe.",
     "D": "Incorrect. New Urbanist developments are compact and walkable, with mixed land uses, not large-lot, car-dependent subdivisions.",
     "E": "Incorrect. In the Burgess model, the zone in transition is next to the CBD, not 50 miles away."
    },
    "explanation": "An exurb is past the suburbs, out where farms used to be. Houses sit on big lots, and people drive a long way to work. It is the far outer edge of a metro area's growth."
   },
   {
    "id": "U6-E05",
    "n": 5,
    "topic": "6.3",
    "lo": "PSO-6.B",
    "skill": "1.B",
    "difficulty": "medium",
    "stem": "Which of the following best explains why cities such as London, New York, and Tokyo are considered to be at the top of the global urban hierarchy?",
    "options": {
     "A": "They have the largest populations of any cities in the world.",
     "B": "They are the national capital cities of three of the world's largest countries as measured by land area.",
     "C": "They were the first cities in the world to industrialize, beginning with steam-powered factories.",
     "D": "They concentrate corporate headquarters and financial markets that direct activity worldwide.",
     "E": "They have grown faster in population than nearly any other large city in the world since 1950."
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Several megacities are larger than London, and population size alone does not determine a city's place in the global hierarchy.",
     "B": "Incorrect. New York is not a national capital, and the United Kingdom and Japan are not among the largest countries by area.",
     "C": "Incorrect. Industrialization began in Britain in the late 1700s; New York and especially Tokyo industrialized later.",
     "D": "Correct. World cities concentrate the headquarters of transnational corporations, stock exchanges, banks, and business services, and their links to one another let them direct global flows of money, information, and decisions.",
     "E": "Incorrect. These cities grow slowly compared with many cities in semiperiphery and periphery countries."
    },
    "explanation": "London, New York, and Tokyo are at the top because of what happens there: giant companies have headquarters there, and huge amounts of money are traded there. Decisions made in these cities affect places all over the world."
   },
   {
    "id": "U6-E06",
    "n": 6,
    "topic": "6.3",
    "lo": "PSO-6.B",
    "skill": "5.B",
    "difficulty": "hard",
    "stem": "A clothing company headquartered in Paris designs garments that are sewn in factories in Bangladesh, shipped through the port of Singapore, and sold in stores in hundreds of cities. Which of the following best describes the role of cities in this example?",
    "options": {
     "A": "Each city works on its own, because global trade has made the links among cities much less important than before.",
     "B": "The smaller cities control the network, because most of the production takes place there.",
     "C": "Cities at different levels of the urban hierarchy are linked, and the world city coordinates the network.",
     "D": "The network illustrates the rank-size rule, because each city is about half as large as the one before it.",
     "E": "The cities are linked mainly by migration rather than by flows of goods, money, and information."
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. Global trade depends on links among cities; the example shows cities tied together by design, production, shipping, and sales.",
     "B": "Incorrect. Control rests with the headquarters city, which makes design and sourcing decisions; factory cities carry out production.",
     "C": "Correct. Decisions made at a world-city headquarters (Paris) coordinate an international production network and affect local employment in connected places, linking the global and local scales.",
     "D": "Incorrect. The rank-size rule describes city sizes within one country, not the links in a global production network.",
     "E": "Incorrect. The example describes flows of goods, money, and decisions, not migration."
    },
    "explanation": "Managers in Paris run a chain that links factories in Bangladesh, ships passing through Singapore, and stores in many cities. Choices made in this world city affect jobs and businesses in places all over the world."
   },
   {
    "id": "U6-E07",
    "n": 7,
    "set": "ranksize",
    "setLabel": "Questions 7–8 refer to the table below.",
    "topic": "6.4",
    "lo": "PSO-6.C",
    "skill": "3.B",
    "difficulty": "easy",
    "stimulus": {
     "type": "table",
     "title": "POPULATION OF THE FIVE LARGEST CITIES IN COUNTRY P AND COUNTRY Q (HYPOTHETICAL DATA)",
     "columns": [
      "City rank",
      "Country P",
      "Country Q"
     ],
     "rows": [
      [
       "1",
       "7,200,000",
       "9,600,000"
      ],
      [
       "2",
       "3,600,000",
       "1,300,000"
      ],
      [
       "3",
       "2,400,000",
       "1,000,000"
      ],
      [
       "4",
       "1,800,000",
       "850,000"
      ],
      [
       "5",
       "1,440,000",
       "700,000"
      ]
     ],
     "source": "Hypothetical data"
    },
    "stem": "Which of the following best describes the urban hierarchies shown in the table?",
    "options": {
     "A": "Country P has a primate city, while Country Q's city sizes follow the rank-size rule.",
     "B": "Both countries follow the rank-size rule, because each city is smaller than the city ranked above it.",
     "C": "Both countries have primate cities, because in each country the largest city has more people than any other city.",
     "D": "Country Q follows the rank-size rule, because its second city is about half the size of its first.",
     "E": "Country P's city sizes follow the rank-size rule, while Country Q has a primate city."
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. This reverses the two countries. Country P's cities match the rank-size rule, and Country Q's largest city is more than seven times the size of its second city.",
     "B": "Incorrect. In every country, cities get smaller as rank goes down; the rank-size rule requires a specific pattern (the nth city is 1/n the size of the largest), and Country Q does not fit it.",
     "C": "Incorrect. Every country's largest city has more people than its other cities; a primate city must be disproportionately larger than the second city. Country P's cities fit the rank-size rule exactly, so its largest city is not a primate city.",
     "D": "Incorrect. Country Q's second city (1.3 million) is less than one-seventh of its largest city (9.6 million), not about half.",
     "E": "Correct. Country P's cities are 1/2, 1/3, 1/4, and 1/5 the size of its largest city, matching the rank-size rule. Country Q's largest city is more than seven times as large as its second city, the mark of a primate city."
    },
    "explanation": "Rank-size rule: city #2 is 1/2 of city #1, city #3 is 1/3, and so on. Country P fits exactly: 7.2 million ÷ 2 = 3.6 million, ÷ 3 = 2.4 million, and so on. Country Q's biggest city is HUGE compared with the rest (9.6 million vs. 1.3 million). That is a primate city."
   },
   {
    "id": "U6-E08",
    "n": 8,
    "set": "ranksize",
    "topic": "6.4",
    "lo": "PSO-6.C",
    "skill": "2.B",
    "difficulty": "medium",
    "stem": "Which of the following best explains the pattern of city sizes shown for Country Q?",
    "options": {
     "A": "Government power, investment, and jobs became concentrated in one city, drawing migrants from across the country.",
     "B": "Central place theory predicts that a country's largest city will be about twice the size of its second-largest city.",
     "C": "The gravity model predicts that migrants will choose smaller cities that are farther away from the largest city.",
     "D": "Counterurbanization moved people out of the largest city and into the country's smaller cities.",
     "E": "Bid-rent theory predicts that land values will be highest in the country's smallest cities."
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. When government power, investment, and jobs concentrate in one city (often a national capital, main port, or former colonial capital), migrants are drawn there far more than to other cities, producing a primate city like Country Q's.",
     "B": "Incorrect. The expectation that the largest city is about twice the second city comes from the rank-size rule, not central place theory, and Country Q does not fit it.",
     "C": "Incorrect. The gravity model predicts more interaction with larger, closer places, which would draw migrants toward the largest city.",
     "D": "Incorrect. Counterurbanization would shrink the largest city relative to the others, the opposite of the pattern shown.",
     "E": "Incorrect. Bid-rent theory describes land values within a city, which are highest near the most accessible center, not across a country's cities."
    },
    "explanation": "Country Q's largest city is more than seven times the size of its second city, so it is a primate city. That usually happens when one city gets most of the government offices, money, and jobs, so people from all over the country move there."
   },
   {
    "id": "U6-E09",
    "n": 9,
    "topic": "6.4",
    "lo": "PSO-6.C",
    "skill": "2.C",
    "difficulty": "medium",
    "stem": "According to the gravity model, in which interaction = (population 1 × population 2) ÷ distance², if the distance between two cities doubled while their populations stayed the same, the expected interaction between them would",
    "options": {
     "A": "double",
     "B": "stay the same",
     "C": "be one-half as large",
     "D": "be one-fourth as large",
     "E": "be one-eighth as large"
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Greater distance reduces interaction in the gravity model; it does not increase it.",
     "B": "Incorrect. Distance is part of the gravity model, so changing it changes the predicted interaction.",
     "C": "Incorrect. One-half would result from dividing by distance rather than distance squared. This question uses the distance-squared version.",
     "D": "Correct. Doubling distance multiplies the denominator by 2² = 4. With the population product unchanged, predicted interaction becomes one-fourth as large.",
     "E": "Incorrect. One-eighth would result from cubing the distance (2³ = 8). This question uses distance squared."
    },
    "explanation": "In this version of the model, distance is squared. Doubling the distance multiplies the bottom of the fraction by 2 × 2 = 4, so the cities would interact only one-fourth as much as before."
   },
   {
    "id": "U6-E10",
    "n": 10,
    "topic": "6.4",
    "lo": "PSO-6.C",
    "skill": "2.C",
    "difficulty": "medium",
    "stem": "A company plans a store that sells expensive, specialized camera equipment, which people buy only once in a while. According to central place theory, in which kind of place is the store most likely to succeed?",
    "options": {
     "A": "In a small town, because the store's threshold is low and its customers will not travel far",
     "B": "In a village with a grocery store, because shoppers buying everyday goods will also buy cameras",
     "C": "Halfway between two small towns, because bid-rent theory shows that land there is cheapest",
     "D": "In the smallest central place in the region, because high-order goods have the shortest range",
     "E": "In a high-order central place, whose large market area can meet the store's high threshold"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. A specialized, expensive good has a high threshold; a small town lacks enough customers to support it.",
     "B": "Incorrect. A village is a low-order place; shoppers who come for groceries do not supply the large threshold that a high-order good needs.",
     "C": "Incorrect. Low land cost alone does not mean a location can attract enough customers, and central place theory places services at central places, not between them.",
     "D": "Incorrect. High-order goods have long ranges, not short ones, and they are found in the largest central places.",
     "E": "Correct. Specialized goods bought rarely are high-order goods, found in higher-order central places that serve large markets. Threshold is the minimum number of customers needed to stay open; range is how far customers will travel."
    },
    "explanation": "Expensive cameras are a high-order good. A camera store needs LOTS of customers to stay open (a big threshold), and people will travel a long way to buy one (a long range). A high-order central place, such as a large city or a major shopping center in a big metro area, serves a market big enough to support it."
   },
   {
    "id": "U6-E11",
    "n": 11,
    "set": "latam",
    "setLabel": "Questions 11–13 refer to the diagram below.",
    "topic": "6.5",
    "lo": "PSO-6.D",
    "skill": "4.B",
    "difficulty": "easy",
    "stimulus": {
     "type": "schematicMap",
     "title": "MODEL OF LAND USE IN LATIN AMERICAN CITIES",
     "canvas": {
      "width": 800,
      "height": 420
     },
     "features": [
      {
       "kind": "land",
       "name": "5",
       "style": "small",
       "polygon": [
        [
         0,
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
         0,
         420
        ]
       ],
       "labelAt": [
        222,
        210
       ]
      },
      {
       "kind": "land",
       "name": "4",
       "style": "land",
       "polygon": [
        [
         550.0,
         210.0
        ],
        [
         549.4,
         223.1
        ],
        [
         547.7,
         236.0
        ],
        [
         544.9,
         248.8
        ],
        [
         541.0,
         261.3
        ],
        [
         535.9,
         273.4
        ],
        [
         529.9,
         285.0
        ],
        [
         522.9,
         296.0
        ],
        [
         514.9,
         306.4
        ],
        [
         506.1,
         316.1
        ],
        [
         496.4,
         324.9
        ],
        [
         486.0,
         332.9
        ],
        [
         475.0,
         339.9
        ],
        [
         463.4,
         345.9
        ],
        [
         451.3,
         351.0
        ],
        [
         438.8,
         354.9
        ],
        [
         426.0,
         357.7
        ],
        [
         413.1,
         359.4
        ],
        [
         400.0,
         360.0
        ],
        [
         386.9,
         359.4
        ],
        [
         374.0,
         357.7
        ],
        [
         361.2,
         354.9
        ],
        [
         348.7,
         351.0
        ],
        [
         336.6,
         345.9
        ],
        [
         325.0,
         339.9
        ],
        [
         314.0,
         332.9
        ],
        [
         303.6,
         324.9
        ],
        [
         293.9,
         316.1
        ],
        [
         285.1,
         306.4
        ],
        [
         277.1,
         296.0
        ],
        [
         270.1,
         285.0
        ],
        [
         264.1,
         273.4
        ],
        [
         259.0,
         261.3
        ],
        [
         255.1,
         248.8
        ],
        [
         252.3,
         236.0
        ],
        [
         250.6,
         223.1
        ],
        [
         250.0,
         210.0
        ],
        [
         250.6,
         196.9
        ],
        [
         252.3,
         184.0
        ],
        [
         255.1,
         171.2
        ],
        [
         259.0,
         158.7
        ],
        [
         264.1,
         146.6
        ],
        [
         270.1,
         135.0
        ],
        [
         277.1,
         124.0
        ],
        [
         285.1,
         113.6
        ],
        [
         293.9,
         103.9
        ],
        [
         303.6,
         95.1
        ],
        [
         314.0,
         87.1
        ],
        [
         325.0,
         80.1
        ],
        [
         336.6,
         74.1
        ],
        [
         348.7,
         69.0
        ],
        [
         361.2,
         65.1
        ],
        [
         374.0,
         62.3
        ],
        [
         386.9,
         60.6
        ],
        [
         400.0,
         60.0
        ],
        [
         413.1,
         60.6
        ],
        [
         426.0,
         62.3
        ],
        [
         438.8,
         65.1
        ],
        [
         451.3,
         69.0
        ],
        [
         463.4,
         74.1
        ],
        [
         475.0,
         80.1
        ],
        [
         486.0,
         87.1
        ],
        [
         496.4,
         95.1
        ],
        [
         506.1,
         103.9
        ],
        [
         514.9,
         113.6
        ],
        [
         522.9,
         124.0
        ],
        [
         529.9,
         135.0
        ],
        [
         535.9,
         146.6
        ],
        [
         541.0,
         158.7
        ],
        [
         544.9,
         171.2
        ],
        [
         547.7,
         184.0
        ],
        [
         549.4,
         196.9
        ]
       ],
       "labelAt": [
        278,
        210
       ]
      },
      {
       "kind": "land",
       "name": "3",
       "style": "small",
       "polygon": [
        [
         495.0,
         210.0
        ],
        [
         494.6,
         218.3
        ],
        [
         493.6,
         226.5
        ],
        [
         491.8,
         234.6
        ],
        [
         489.3,
         242.5
        ],
        [
         486.1,
         250.1
        ],
        [
         482.3,
         257.5
        ],
        [
         477.8,
         264.5
        ],
        [
         472.8,
         271.1
        ],
        [
         467.2,
         277.2
        ],
        [
         461.1,
         282.8
        ],
        [
         454.5,
         287.8
        ],
        [
         447.5,
         292.3
        ],
        [
         440.1,
         296.1
        ],
        [
         432.5,
         299.3
        ],
        [
         424.6,
         301.8
        ],
        [
         416.5,
         303.6
        ],
        [
         408.3,
         304.6
        ],
        [
         400.0,
         305.0
        ],
        [
         391.7,
         304.6
        ],
        [
         383.5,
         303.6
        ],
        [
         375.4,
         301.8
        ],
        [
         367.5,
         299.3
        ],
        [
         359.9,
         296.1
        ],
        [
         352.5,
         292.3
        ],
        [
         345.5,
         287.8
        ],
        [
         338.9,
         282.8
        ],
        [
         332.8,
         277.2
        ],
        [
         327.2,
         271.1
        ],
        [
         322.2,
         264.5
        ],
        [
         317.7,
         257.5
        ],
        [
         313.9,
         250.1
        ],
        [
         310.7,
         242.5
        ],
        [
         308.2,
         234.6
        ],
        [
         306.4,
         226.5
        ],
        [
         305.4,
         218.3
        ],
        [
         305.0,
         210.0
        ],
        [
         305.4,
         201.7
        ],
        [
         306.4,
         193.5
        ],
        [
         308.2,
         185.4
        ],
        [
         310.7,
         177.5
        ],
        [
         313.9,
         169.9
        ],
        [
         317.7,
         162.5
        ],
        [
         322.2,
         155.5
        ],
        [
         327.2,
         148.9
        ],
        [
         332.8,
         142.8
        ],
        [
         338.9,
         137.2
        ],
        [
         345.5,
         132.2
        ],
        [
         352.5,
         127.7
        ],
        [
         359.9,
         123.9
        ],
        [
         367.5,
         120.7
        ],
        [
         375.4,
         118.2
        ],
        [
         383.5,
         116.4
        ],
        [
         391.7,
         115.4
        ],
        [
         400.0,
         115.0
        ],
        [
         408.3,
         115.4
        ],
        [
         416.5,
         116.4
        ],
        [
         424.6,
         118.2
        ],
        [
         432.5,
         120.7
        ],
        [
         440.1,
         123.9
        ],
        [
         447.5,
         127.7
        ],
        [
         454.5,
         132.2
        ],
        [
         461.1,
         137.2
        ],
        [
         467.2,
         142.8
        ],
        [
         472.8,
         148.9
        ],
        [
         477.8,
         155.5
        ],
        [
         482.3,
         162.5
        ],
        [
         486.1,
         169.9
        ],
        [
         489.3,
         177.5
        ],
        [
         491.8,
         185.4
        ],
        [
         493.6,
         193.5
        ],
        [
         494.6,
         201.7
        ]
       ],
       "labelAt": [
        335,
        210
       ]
      },
      {
       "kind": "land",
       "name": "2",
       "style": "power",
       "polygon": [
        [
         346.9,
         12.0
        ],
        [
         355.6,
         9.9
        ],
        [
         364.4,
         8.1
        ],
        [
         373.2,
         6.8
        ],
        [
         382.1,
         5.8
        ],
        [
         391.1,
         5.2
        ],
        [
         400.0,
         5.0
        ],
        [
         408.9,
         5.2
        ],
        [
         417.9,
         5.8
        ],
        [
         426.8,
         6.8
        ],
        [
         435.6,
         8.1
        ],
        [
         444.4,
         9.9
        ],
        [
         453.1,
         12.0
        ],
        [
         409.1,
         176.2
        ],
        [
         407.6,
         175.8
        ],
        [
         406.1,
         175.5
        ],
        [
         404.6,
         175.3
        ],
        [
         403.1,
         175.1
        ],
        [
         401.5,
         175.0
        ],
        [
         400.0,
         175.0
        ],
        [
         398.5,
         175.0
        ],
        [
         396.9,
         175.1
        ],
        [
         395.4,
         175.3
        ],
        [
         393.9,
         175.5
        ],
        [
         392.4,
         175.8
        ],
        [
         390.9,
         176.2
        ]
       ],
       "labelAt": [
        430,
        70
       ]
      },
      {
       "kind": "land",
       "name": "6",
       "style": "power",
       "polygon": [
        [
         557.0,
         341.8
        ],
        [
         551.1,
         348.5
        ],
        [
         545.0,
         355.0
        ],
        [
         538.5,
         361.1
        ],
        [
         531.8,
         367.0
        ],
        [
         524.8,
         372.6
        ],
        [
         517.6,
         377.9
        ],
        [
         420.1,
         238.7
        ],
        [
         421.3,
         237.8
        ],
        [
         422.5,
         236.8
        ],
        [
         423.6,
         235.8
        ],
        [
         424.7,
         234.7
        ],
        [
         425.8,
         233.6
        ],
        [
         426.8,
         232.5
        ]
       ],
       "labelAt": [
        501,
        321
       ]
      },
      {
       "kind": "land",
       "name": "1",
       "style": "land",
       "polygon": [
        [
         435.0,
         210.0
        ],
        [
         434.9,
         213.1
        ],
        [
         434.5,
         216.1
        ],
        [
         433.8,
         219.1
        ],
        [
         432.9,
         222.0
        ],
        [
         431.7,
         224.8
        ],
        [
         430.3,
         227.5
        ],
        [
         428.7,
         230.1
        ],
        [
         426.8,
         232.5
        ],
        [
         424.7,
         234.7
        ],
        [
         422.5,
         236.8
        ],
        [
         420.1,
         238.7
        ],
        [
         417.5,
         240.3
        ],
        [
         414.8,
         241.7
        ],
        [
         412.0,
         242.9
        ],
        [
         409.1,
         243.8
        ],
        [
         406.1,
         244.5
        ],
        [
         403.1,
         244.9
        ],
        [
         400.0,
         245.0
        ],
        [
         396.9,
         244.9
        ],
        [
         393.9,
         244.5
        ],
        [
         390.9,
         243.8
        ],
        [
         388.0,
         242.9
        ],
        [
         385.2,
         241.7
        ],
        [
         382.5,
         240.3
        ],
        [
         379.9,
         238.7
        ],
        [
         377.5,
         236.8
        ],
        [
         375.3,
         234.7
        ],
        [
         373.2,
         232.5
        ],
        [
         371.3,
         230.1
        ],
        [
         369.7,
         227.5
        ],
        [
         368.3,
         224.8
        ],
        [
         367.1,
         222.0
        ],
        [
         366.2,
         219.1
        ],
        [
         365.5,
         216.1
        ],
        [
         365.1,
         213.1
        ],
        [
         365.0,
         210.0
        ],
        [
         365.1,
         206.9
        ],
        [
         365.5,
         203.9
        ],
        [
         366.2,
         200.9
        ],
        [
         367.1,
         198.0
        ],
        [
         368.3,
         195.2
        ],
        [
         369.7,
         192.5
        ],
        [
         371.3,
         189.9
        ],
        [
         373.2,
         187.5
        ],
        [
         375.3,
         185.3
        ],
        [
         377.5,
         183.2
        ],
        [
         379.9,
         181.3
        ],
        [
         382.5,
         179.7
        ],
        [
         385.2,
         178.3
        ],
        [
         388.0,
         177.1
        ],
        [
         390.9,
         176.2
        ],
        [
         393.9,
         175.5
        ],
        [
         396.9,
         175.1
        ],
        [
         400.0,
         175.0
        ],
        [
         403.1,
         175.1
        ],
        [
         406.1,
         175.5
        ],
        [
         409.1,
         176.2
        ],
        [
         412.0,
         177.1
        ],
        [
         414.8,
         178.3
        ],
        [
         417.5,
         179.7
        ],
        [
         420.1,
         181.3
        ],
        [
         422.5,
         183.2
        ],
        [
         424.7,
         185.3
        ],
        [
         426.8,
         187.5
        ],
        [
         428.7,
         189.9
        ],
        [
         430.3,
         192.5
        ],
        [
         431.7,
         195.2
        ],
        [
         432.9,
         198.0
        ],
        [
         433.8,
         200.9
        ],
        [
         434.5,
         203.9
        ],
        [
         434.9,
         206.9
        ]
       ],
       "labelAt": [
        400,
        210
       ]
      },
      {
       "kind": "line",
       "name": "Main boulevard",
       "line": [
        [
         400,
         175
        ],
        [
         400,
         5
        ]
       ],
       "dashed": true
      }
     ],
     "legend": [
      {
       "swatch": "road",
       "label": "Main boulevard"
      }
     ],
     "description": "Area 1 is at the center of the city. Area 2 is a wedge that extends north from Area 1 across Areas 3, 4, and 5, with a main boulevard running through its middle. Areas 3 and 4 are rings around Area 1, with Area 3 closer to the center. Area 5 surrounds Area 4 and extends to the outer edge of the diagram. Area 6 is a narrow wedge that extends southeast from Area 1 across Areas 3 and 4 and into Area 5.",
     "source": "Simplified from the Griffin–Ford model of Latin American city structure (1980)"
    },
    "stem": "According to the model, which area is most likely to contain the homes of the city's wealthiest residents?",
    "options": {
     "A": "Area 1",
     "B": "Area 2",
     "C": "Area 3",
     "D": "Area 5",
     "E": "Area 6"
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. Area 1 is the CBD, the commercial core of the city, not the main elite residential area.",
     "B": "Correct. Area 2 is the spine and elite residential sector: a commercial boulevard extending from the CBD, lined with the homes of the wealthiest residents and with offices, shops, and amenities.",
     "C": "Incorrect. Area 3 is the zone of maturity, an area of older, well-established housing for middle-income residents, not the wealthiest.",
     "D": "Incorrect. Area 5 is the zone of peripheral squatter settlements, where many of the poorest residents, often recent migrants, live.",
     "E": "Incorrect. Area 6 is the disamenity sector, one of the poorest parts of the city, where many homes lack regular city services."
    },
    "explanation": "In the Latin American city model, Area 2 has two parts. The spine is a strip of stores and offices running out from the CBD. Around it is the elite sector, where the richest families live. This area has the best services and shops."
   },
   {
    "id": "U6-E12",
    "n": 12,
    "set": "latam",
    "topic": "6.5",
    "lo": "PSO-6.D",
    "skill": "1.C",
    "difficulty": "medium",
    "stem": "Which of the following best describes a key difference between the model shown and the Burgess concentric zone model?",
    "options": {
     "A": "The model shown has no CBD, while the Burgess model is organized around a single CBD.",
     "B": "The model shown places factories in rings around the CBD, while the Burgess model places them in a single wedge from the center.",
     "C": "Apart from the elite spine, the model shown gets poorer toward the edge, while the Burgess model gets wealthier.",
     "D": "The model shown assumes a city grows around several separate nuclei, while the Burgess model assumes one center.",
     "E": "The model shown was designed for cities that grew without colonial influence, while the Burgess model was based on colonial cities."
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. Both models are organized around a CBD; Area 1 in the diagram is the CBD.",
     "B": "Incorrect. The Burgess model places factories in the zone in transition, a ring around the CBD, not in a wedge; wedges of industry along transportation routes are a feature of the Hoyt sector model.",
     "C": "Correct. In the Latin American model, outside the elite spine, housing quality and income generally decline from the zone of maturity outward to peripheral squatter settlements. In the Burgess model, higher-income residents live in the outer zones and commute to the CBD.",
     "D": "Incorrect. Several separate nuclei describe the Harris and Ullman multiple nuclei model; the Latin American model has a single CBD.",
     "E": "Incorrect. Latin American cities were shaped by Spanish and Portuguese colonial planning, and the Burgess model was based on Chicago."
    },
    "explanation": "In a U.S. city in the Burgess model, the richer families live far out in the suburbs. In the Latin American model, it is mostly the opposite: apart from the spine and the disamenity sector, the farther you go from the center, the poorer the neighborhoods, and many of the poorest live at the very edge."
   },
   {
    "id": "U6-E13",
    "n": 13,
    "set": "latam",
    "topic": "6.10",
    "lo": "SPS-6.A",
    "skill": "4.E",
    "difficulty": "medium",
    "stem": "Which of the following best explains the growth of the settlements in Area 5?",
    "options": {
     "A": "Wealthy residents moved to the urban edge to escape crowding and pollution near the CBD, as in many U.S. suburbs.",
     "B": "Rural migrants arrived faster than affordable housing was built, so many built homes without secure land rights.",
     "C": "Gentrification of the outer zone raised property values and attracted high-income buyers.",
     "D": "Urban renewal programs relocated the city's elite families to new planned communities at the edge of the city.",
     "E": "Factories moved to Area 5 to take advantage of the city's highest land values at the urban edge."
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. Area 5 represents peripheral informal settlements. Wealthy households are concentrated in Area 2, the elite residential sector, which can also extend to the urban edge; distance from the CBD alone does not determine neighborhood income.",
     "B": "Correct. Rapid rural-to-urban migration outpaced the supply of affordable formal housing, so newcomers built self-made homes at the city's edge without secure rights to occupy the land, creating squatter settlements.",
     "C": "Incorrect. Area 5 is the zone of peripheral squatter settlements, which house many of the city's poorest residents; gentrification is not what created it.",
     "D": "Incorrect. The elite are concentrated in the spine sector, and Area 5 is mostly informal housing, not planned communities.",
     "E": "Incorrect. Land values are generally lowest, not highest, at the urban edge, and Area 5 is mainly residential."
    },
    "explanation": "Lots of people moved from the countryside to the city looking for work. There were not enough affordable homes for them, so they built their own homes at the edge of the city without secure rights to the land. Those neighborhoods are squatter settlements."
   },
   {
    "id": "U6-E14",
    "n": 14,
    "topic": "6.5",
    "lo": "PSO-6.D",
    "skill": "1.E",
    "difficulty": "medium",
    "stem": "Which of the following is a limitation of the Burgess concentric zone model when it is applied to large U.S. metropolitan areas today?",
    "options": {
     "A": "It places the wealthiest residents in the zone closest to the CBD, which does not match most U.S. cities.",
     "B": "It leaves out the CBD, which is still the main center of many U.S. cities.",
     "C": "It was based on cities in Latin America, so it does not reflect the history of U.S. cities.",
     "D": "It assumes a single CBD, but many metropolitan areas now have several suburban business centers.",
     "E": "It assumes that land uses form wedges along transportation routes, which is rare in U.S. cities."
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. The Burgess model places higher-income commuters in the outer zones, not next to the CBD.",
     "B": "Incorrect. The CBD is the center of the Burgess model.",
     "C": "Incorrect. Burgess based his model on Chicago in the 1920s.",
     "D": "Correct. The model assumes growth outward from one CBD. Large metropolitan areas today also contain edge cities and suburban business centers, a pattern better described by the multiple nuclei and galactic city models.",
     "E": "Incorrect. Wedges along transportation routes describe the Hoyt sector model, not the Burgess model."
    },
    "explanation": "Burgess drew his rings around ONE downtown. Today, many big metro areas have several job centers, like edge cities near highways. A model with only one center cannot show that."
   },
   {
    "id": "U6-E15",
    "n": 15,
    "topic": "6.5",
    "lo": "PSO-6.D",
    "skill": "2.C",
    "difficulty": "medium",
    "stem": "A new beltway with several interchanges is built around a metropolitan area. According to bid-rent theory, which change in land values is most likely?",
    "options": {
     "A": "Land values near the interchanges will rise, because those sites become highly accessible.",
     "B": "Land values near the interchanges will fall, because traffic noise will drive businesses away.",
     "C": "Land values in the CBD will rise sharply, because commuters will no longer be able to reach the suburbs.",
     "D": "Land values will become nearly equal across the metropolitan area, because travel times will shrink.",
     "E": "Farmland far beyond the beltway will gain the most value, because it is farthest from traffic."
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. Bid-rent theory links land value to accessibility. Interchanges become new points of high accessibility, so commercial users bid up land near them, creating new peaks of land value away from the CBD.",
     "B": "Incorrect. In bid-rent theory, accessibility raises what businesses will pay; interchange sites attract offices, stores, and hotels.",
     "C": "Incorrect. A beltway makes the suburbs easier to reach, not harder.",
     "D": "Incorrect. Better roads change which places are most accessible; they create new high-value locations rather than making values equal everywhere.",
     "E": "Incorrect. Land far from the beltway is less accessible, so it gains less value than land near the interchanges."
    },
    "explanation": "In bid-rent theory, land that is easy to reach is worth more. A beltway interchange is very easy to reach by car, so businesses will pay a lot for land there. That creates new high-value spots out in the suburbs, not just downtown."
   },
   {
    "id": "U6-E16",
    "n": 16,
    "topic": "6.6",
    "lo": "IMP-6.A",
    "skill": "1.B",
    "difficulty": "medium",
    "stem": "Which of the following best explains why older neighborhoods near the CBDs of many U.S. cities have higher housing densities than suburbs built after 1950?",
    "options": {
     "A": "They were built when most people walked or rode streetcars, so homes were close to transit and jobs.",
     "B": "Land near the CBD was cheaper than land at the city's edge, so builders could afford to put up more units.",
     "C": "They were built after zoning laws required large minimum lot sizes in central cities.",
     "D": "They were built after new highways made it easy for residents to drive to jobs downtown.",
     "E": "Federal home loans after 1950 favored apartment buildings in central cities over single-family homes."
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. Before cars were common, residents needed to live within walking distance of work or a streetcar line, so builders placed row houses and apartments close together near transit and jobs.",
     "B": "Incorrect. Land near the CBD is generally the most expensive, which is one reason builders put more units on each lot.",
     "C": "Incorrect. Large minimum lot sizes lower density; they are more typical of suburban zoning.",
     "D": "Incorrect. Most older neighborhoods near the CBD were built before cars and highways were common; highways made it easier to live farther out, which lowered density.",
     "E": "Incorrect. Federal mortgage programs after World War II mainly supported single-family homes in the suburbs."
    },
    "explanation": "Older city neighborhoods were built before most families had cars. People had to walk or take a streetcar to work, so homes were packed close together near jobs and transit lines. After 1950, cars let people spread out into suburbs with bigger yards."
   },
   {
    "id": "U6-E17",
    "n": 17,
    "topic": "6.7",
    "lo": "IMP-6.B",
    "skill": "2.C",
    "difficulty": "medium",
    "stem": "A city extends a new highway, water lines, and sewer lines into farmland at its edge, while older neighborhoods with aging pipes and roads receive little new investment. Which outcome is most likely?",
    "options": {
     "A": "Population density will rise in the older neighborhoods as new homes and businesses shift back toward them.",
     "B": "Farmland at the edge will be better protected, because the new infrastructure makes building there harder.",
     "C": "Commuting distances will shrink, because jobs and housing will both move to the CBD.",
     "D": "Land values at the edge will fall, because the new highway will bring more traffic.",
     "E": "New development will shift to the edge, encouraging sprawl, while older neighborhoods decline."
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. Investment is going to the edge, so new development is more likely to shift away from the older neighborhoods.",
     "B": "Incorrect. Roads, water, and sewer service make land easier and cheaper to develop, so they speed the loss of farmland.",
     "C": "Incorrect. Development at the edge spreads homes farther from older job centers, which tends to lengthen commutes.",
     "D": "Incorrect. New access and utilities generally raise the value of land at the edge.",
     "E": "Correct. The location and quality of infrastructure shape where development happens. New roads and utilities open fringe land to building, encouraging sprawl, while underinvested older neighborhoods can lose residents and businesses."
    },
    "explanation": "Builders go where the roads, water, and sewers are. If the city puts new pipes and roads on farmland at the edge, new homes and stores will go there. Older neighborhoods with worn-out pipes and roads may lose people and businesses."
   },
   {
    "id": "U6-E18",
    "n": 18,
    "topic": "6.8",
    "lo": "IMP-6.C",
    "skill": "1.D",
    "difficulty": "easy",
    "stem": "A city council caps the number of new building permits it will issue each year and requires new developments to show that roads, schools, and water systems can handle them. This approach is best described as",
    "options": {
     "A": "New Urbanism",
     "B": "inclusionary zoning",
     "C": "a slow-growth policy",
     "D": "urban renewal",
     "E": "transportation-oriented development"
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. New Urbanism is a design approach for compact, walkable, mixed-use neighborhoods, not a cap on permits.",
     "B": "Incorrect. Inclusionary zoning requires or encourages affordable units in new housing; it does not limit how much is built.",
     "C": "Correct. Slow-growth policies limit the rate of new development, for example by capping permits or requiring that infrastructure be in place before building.",
     "D": "Incorrect. Urban renewal cleared and rebuilt older neighborhoods; it did not limit new construction.",
     "E": "Incorrect. Transportation-oriented development concentrates housing and jobs near transit stations rather than limiting growth."
    },
    "explanation": "Capping building permits slows down how fast the city grows. That is a slow-growth policy. It gives the city time to make sure roads, schools, and water can keep up."
   },
   {
    "id": "U6-E19",
    "n": 19,
    "topic": "6.8",
    "lo": "IMP-6.D",
    "skill": "2.C",
    "difficulty": "medium",
    "stem": "A city adopts an urban growth boundary. Ten years later, farmland loss at the city's edge has slowed, but the number of households inside the boundary has grown much faster than the number of homes. Which criticism of the policy do these results most directly support?",
    "options": {
     "A": "It may lower land values inside the boundary, because builders are not allowed to use that land.",
     "B": "It may raise housing costs and price out lower-income households, adding to de facto segregation.",
     "C": "It may lower density inside the boundary, because new homes there are built on large lots.",
     "D": "It may increase car dependence, because the boundary separates homes from shops and jobs.",
     "E": "It may harm the city's historic character as older buildings are torn down to make room for new towers."
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. A growth boundary allows building inside it and restricts building outside it; limiting buildable land tends to raise, not lower, land values inside the boundary.",
     "B": "Correct. Households grew much faster than homes, so demand outran supply inside the boundary. Rising housing costs that price out lower-income residents and can add to de facto segregation are a common criticism of growth limits.",
     "C": "Incorrect. Growth boundaries usually encourage more compact, higher-density building inside the boundary; they do not require large lots.",
     "D": "Incorrect. A growth boundary limits outward spread; it does not separate homes from shops and jobs, which is a result of single-use zoning.",
     "E": "Incorrect. Loss of historic character is a criticism of some redevelopment, but these results describe a housing shortage, not the demolition of older buildings."
    },
    "explanation": "The boundary slowed farmland loss, which is its goal. But households grew much faster than the number of homes. When more people want homes than there are homes, prices rise, and families with less money can get pushed out."
   },
   {
    "id": "U6-E20",
    "n": 20,
    "set": "tracts",
    "setLabel": "Questions 20–22 refer to the table below.",
    "topic": "6.9",
    "lo": "IMP-6.E",
    "skill": "3.E",
    "difficulty": "medium",
    "stimulus": {
     "type": "table",
     "title": "SELECTED DATA FOR FOUR CENSUS TRACTS IN CITY M, 2010 AND 2020 (HYPOTHETICAL DATA)",
     "columns": [
      "Census tract",
      "Median household income, 2010 ($)",
      "Median household income, 2020 ($)",
      "Median monthly rent, 2010 ($)",
      "Median monthly rent, 2020 ($)",
      "Adults with a bachelor's degree, 2010 (%)",
      "Adults with a bachelor's degree, 2020 (%)"
     ],
     "rows": [
      [
       "Tract 101",
       "31,000",
       "68,000",
       "650",
       "1,450",
       "14",
       "46"
      ],
      [
       "Tract 102",
       "29,000",
       "30,500",
       "620",
       "700",
       "12",
       "13"
      ],
      [
       "Tract 103",
       "88,000",
       "92,000",
       "1,300",
       "1,420",
       "51",
       "54"
      ],
      [
       "Tract 104",
       "45,000",
       "43,000",
       "800",
       "860",
       "22",
       "21"
      ]
     ],
     "source": "Hypothetical data. All dollar amounts are adjusted for inflation to 2020 dollars. Tract boundaries are the same in both years."
    },
    "stem": "Which tract shows the strongest evidence of gentrification between 2010 and 2020?",
    "options": {
     "A": "Tract 101, because its income, rent, and share of college graduates rose sharply from low levels",
     "B": "Tract 102, because its rent rose while its median income stayed about the same",
     "C": "Tract 103, because it had the highest income and the highest share of college graduates in both years",
     "D": "Tract 104, because its median income fell slightly while its median rent rose",
     "E": "Tracts 101 and 103 equally, because both tracts had median household incomes above $60,000 in 2020"
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. In Tract 101, median income more than doubled ($31,000 to $68,000), median rent more than doubled ($650 to $1,450), and the share of adults with a bachelor's degree rose from 14 to 46 percent, a pattern consistent with higher-income, more-educated newcomers moving into a lower-income area.",
     "B": "Incorrect. Tract 102's rent rose modestly ($620 to $700), but its income and education levels barely changed, so there is little sign of new higher-income residents.",
     "C": "Incorrect. Tract 103 was already high-income in 2010 and changed little; gentrification describes change in a lower-income area.",
     "D": "Incorrect. Tract 104 shows rising rent but no increase in income or education levels, and the table does not show who moved in or out.",
     "E": "Incorrect. Tract 103's 2020 income reflects an area that was already high-income at the beginning of the period, not a rapid change from low starting levels."
    },
    "explanation": "Gentrification is reinvestment in a lower-income neighborhood along with more higher-income residents. Tract 101 shows the strongest signs: income and rent each more than doubled, and college graduates rose from 14% to 46% of adults. These numbers suggest gentrification, but they do not show who moved or whether anyone was pushed out."
   },
   {
    "id": "U6-E21",
    "n": 21,
    "set": "tracts",
    "topic": "6.9",
    "lo": "IMP-6.E",
    "skill": "3.F",
    "difficulty": "hard",
    "stem": "Which additional information would best help a researcher determine whether longtime residents of Tract 101 were displaced?",
    "options": {
     "A": "Estimates of Tract 101's median household income in 2030",
     "B": "The total land area of Tract 101 in square kilometers",
     "C": "The share of adults with a bachelor's degree in Tract 103 in 2010 and in 2020",
     "D": "A map showing the distance from Tract 101 to the CBD and to major job centers",
     "E": "Interviews and surveys that track where earlier residents moved and why"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. A future income estimate would not show what happened to residents who lived in the tract in 2010.",
     "B": "Incorrect. Land area does not change with displacement and says nothing about who moved.",
     "C": "Incorrect. Data for a different tract cannot show whether Tract 101's residents left.",
     "D": "Incorrect. A tract's location may help explain why it changed, but it does not show whether residents were displaced.",
     "E": "Correct. Tract-level medians cannot show whether the same households stayed or left. Surveys that follow earlier residents and qualitative interviews can show where people moved and whether rising costs forced them out."
    },
    "explanation": "The table shows averages for the whole tract, not what happened to each family. To know if people were pushed out, you need to find out where the old residents went and why. Surveys and interviews can tell you that."
   },
   {
    "id": "U6-E22",
    "n": 22,
    "set": "tracts",
    "topic": "6.10",
    "lo": "SPS-6.A",
    "skill": "2.C",
    "difficulty": "medium",
    "stem": "City M wants to help lower-income households stay in Tract 101, where median rent more than doubled, as new apartment buildings are built there. Which policy would most directly address this goal?",
    "options": {
     "A": "Large-lot zoning that limits new housing in the tract to detached single-family homes",
     "B": "An urban growth boundary drawn around the outer edge of the metropolitan area",
     "C": "Inclusionary zoning that requires new buildings to include some affordable units",
     "D": "An urban renewal program that clears older buildings in the tract for new offices",
     "E": "A local food program that opens weekly farmers' markets in the tract"
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. Limiting housing to detached homes on large lots would reduce the number of homes and tend to raise their cost.",
     "B": "Incorrect. A growth boundary limits sprawl at the metropolitan edge; by limiting land supply, it can raise housing costs rather than protect affordability in one tract.",
     "C": "Correct. Inclusionary zoning requires or encourages developers to set aside a share of new units as affordable housing, directly helping lower-income households remain as a neighborhood changes.",
     "D": "Incorrect. Urban renewal that clears older buildings would remove existing housing and displace residents.",
     "E": "Incorrect. Local food movements can improve access to fresh food, but they do not address housing costs."
    },
    "explanation": "This rule says that when builders put up new apartments, some must be priced so that families with less money can afford them. That helps those families stay, even as the area gets more expensive. It is called inclusionary zoning."
   },
   {
    "id": "U6-E23",
    "n": 23,
    "topic": "6.10",
    "lo": "SPS-6.A",
    "skill": "1.B",
    "difficulty": "hard",
    "stem": "Which of the following best explains how redlining in the 1930s contributed to differences among urban neighborhoods in the United States that persist today?",
    "options": {
     "A": "Lending more money in older neighborhoods encouraged their rapid gentrification during the 1940s and 1950s.",
     "B": "Requiring equal lending across neighborhoods narrowed differences in home values over time.",
     "C": "Concentrating federal home loans in central cities kept suburbs from growing after World War II.",
     "D": "Denying loans in areas rated risky, often because of residents' race, held back investment for decades.",
     "E": "Encouraging real estate agents to resell homes quickly created mixed-income neighborhoods that lasted."
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Redlining restricted lending in neighborhoods rated hazardous; it did not increase lending there.",
     "B": "Incorrect. Redlining did the opposite of equal lending, steering credit away from certain neighborhoods and widening gaps in home values.",
     "C": "Incorrect. Federal mortgage programs of the period favored new suburban development, which grew rapidly after World War II.",
     "D": "Correct. Discriminatory neighborhood grading and lending practices limited mortgage access in many Black and immigrant neighborhoods. Restricted credit made buying and repairing homes harder, contributing to lasting differences in investment, property values, and household wealth.",
     "E": "Incorrect. Quickly reselling homes to profit from racial fear describes blockbusting, and it did not create stable mixed-income neighborhoods."
    },
    "explanation": "In redlined neighborhoods, many residents were refused loans or offered worse terms when they tried to buy or fix up homes. That cut chances to own homes and invest, and it helped create wealth gaps that lasted for generations."
   },
   {
    "id": "U6-E24",
    "n": 24,
    "topic": "6.11",
    "lo": "SPS-6.B",
    "skill": "2.C",
    "difficulty": "medium",
    "stem": "A growing city wants to add housing, clean up contaminated land, and limit development on the farmland around it. Which strategy would most directly meet all three goals?",
    "options": {
     "A": "Build new apartment buildings on greenfield sites at the city's edge",
     "B": "Adopt an urban growth boundary and require large-lot zoning inside it",
     "C": "Require inclusionary zoning for new housing built in the city",
     "D": "Redevelop brownfield sites near downtown with new apartment buildings",
     "E": "Create a greenbelt and steer new apartment building to the next town over"
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Greenfield sites are undeveloped land such as farmland, so this adds housing but uses farmland and cleans up nothing.",
     "B": "Incorrect. The boundary limits farmland loss, but large-lot zoning reduces the number of homes, and nothing is cleaned up.",
     "C": "Incorrect. Inclusionary zoning makes some new units affordable; it does not clean up contaminated land or protect farmland.",
     "D": "Correct. Brownfields are former industrial or commercial sites that may be contaminated; cleaning them up and redeveloping them with apartments adds housing, removes pollution, and reuses developed land, reducing pressure on farmland.",
     "E": "Incorrect. A greenbelt protects farmland, but this sends housing to another town and leaves contaminated land as it is."
    },
    "explanation": "Brownfields are old industrial or commercial sites that may be polluted. Cleaning them up and building apartments there does all three things: it adds homes, removes pollution, and reuses land the city already has, so less farmland is needed."
   },
   {
    "id": "U6-E25",
    "n": 25,
    "topic": "6.11",
    "lo": "SPS-6.B",
    "skill": "5.B",
    "difficulty": "medium",
    "stem": "A central city restricts new development outside a growth boundary on land under its own planning authority. The suburban municipalities next to it adopt no similar limits. Which regional outcome is most likely?",
    "options": {
     "A": "Sprawl will slow across the whole metropolitan area, because the boundary marks the outer limit of regional growth.",
     "B": "Development will shift past the boundary into nearby suburbs, so sprawl will continue across the region.",
     "C": "The central city will annex its neighboring suburbs, so one government will control land use across the region.",
     "D": "Housing prices in the central city will fall, because land inside the boundary becomes more plentiful.",
     "E": "Density inside the central city will fall, because builders will avoid the limited land inside the boundary."
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. The boundary applies only to land under the central city's authority; the neighboring suburbs have no limits, so development can continue there.",
     "B": "Correct. Developers may respond to limits in one jurisdiction by building in neighboring municipalities without them, so sprawl can continue at the regional scale. This is why regional planning efforts matter for urban sustainability.",
     "C": "Incorrect. A city usually cannot annex an incorporated neighbor without its consent, and nothing in the scenario suggests it; the many separate local governments are why regional growth is hard to manage.",
     "D": "Incorrect. A growth boundary limits the land available for building, which tends to raise, not lower, housing prices inside it.",
     "E": "Incorrect. Limiting buildable land usually raises land values, which encourages more compact, denser building inside the boundary."
    },
    "explanation": "A growth boundary only works where it applies. If just the central city has one, builders can go to the suburbs next door that have no limits. Sprawl keeps happening in the region. That is why cities and suburbs often need to plan together."
   }
  ]
 }
}

===== SOURCES.md =====

# Unit 6 bank: data sources and checks

Two data stimuli use observed statistics: P06 and E02–E03. Other numerical datasets are hypothetical and labeled
"Hypothetical data". Conceptual model diagrams are simplified redrawings identified by their source lines.
`python3 u6/verify.py` re-derives every number and computed answer (80 checks). `python3 u6/verify.py --live`
also re-downloads the two sources below and compares every stored value (last run Nov 8, 2026: 0 mismatches).

## 1. World Bank urban share: U6-E02 / U6-E03 line chart

- Source: World Bank, World Development Indicators, indicator `SP.URB.TOTL.IN.ZS`, "Urban population (% of total population)".
  The indicator metadata credits UN Population Division, *World Urbanization Prospects*, national definitions of urban.
- URL (API): https://api.worldbank.org/v2/country/CHN;NGA;USA;GBR;IND/indicator/SP.URB.TOTL.IN.ZS?format=json&date=1960:2024&per_page=1000
- Metadata: https://api.worldbank.org/v2/indicator/SP.URB.TOTL.IN.ZS?format=json
- API header `lastupdated`: 2026-10-08. Accessed Nov 8, 2026.
- Verified: the chart's values equal the API values rounded to one decimal.

| Year | United Kingdom | China | Nigeria | India |
|---|---|---|---|---|
| 1960 | 78.6 | 19.7 | 14.2 | 17.9 |
| 1970 | 76.9 | 17.4 | 20.2 | 19.7 |
| 1980 | 78.6 | 19.4 | 27.4 | 23.5 |
| 1990 | 78.1 | 26.2 | 35.2 | 25.6 |
| 2000 | 79.8 | 36.4 | 43.3 | 27.6 |
| 2010 | 81.0 | 49.2 | 51.7 | 30.9 |
| 2020 | 82.9 | 63.5 | 59.8 | 34.1 |

Full-precision values are stored in `u6/verify.py` (`WB`). Note for reviewers: this World Bank release carries the
newer UN urbanization estimates, so some values differ from the older World Urbanization Prospects 2018 figures in
many textbooks (for example, Nigeria 2020 is 59.8 here). No item depends on a textbook figure; every claim is checked
against the values in the chart. The United States was downloaded but not used (its 2020 value, 80.0, dips slightly
below its 2010 value, 80.7, which would distract from the questions).

Claims checked by script: China gained the most percentage points 1980–2020 (+44.1; Nigeria +32.4, India +10.6,
United Kingdom +4.3); China > Nigeria in 1960 and 2020; India +8.5 vs. Nigeria +24.6 for 1990–2020; the United Kingdom
did not double; China < India in 1980.

## 2. U.S. Census Bureau city populations: U6-P06 table

Rows are incorporated places (SUMLEV 162), Texas (STATE 48): Dallas 19000, Plano 58016, McKinney 45744, Frisco 27684.

| Column in table | File | Field | URL |
|---|---|---|---|
| 2000 Census | sub-est2009_48.csv | POPCENSUS_2000 | https://www2.census.gov/programs-surveys/popest/datasets/2000-2009/cities/totals/sub-est2009_48.csv |
| 2010 Census | SUB-EST2020_48.csv | CENSUS2010POP | https://www2.census.gov/programs-surveys/popest/datasets/2010-2020/cities/SUB-EST2020_48.csv |
| July 1, 2024 estimate | sub-est2024_48.csv | POPESTIMATE2024 | https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/cities/totals/sub-est2024_48.csv |

| City | 2000 Census | 2010 Census | July 1, 2024 estimate |
|---|---|---|---|
| Dallas | 1,188,580 | 1,197,816 | 1,326,087 |
| Plano | 222,030 | 259,841 | 293,286 |
| McKinney | 54,369 | 131,117 | 227,526 |
| Frisco | 33,714 | 116,989 | 235,208 |

Accessed Nov 8, 2026. The 2020 Census count was not used: the Census API now requires a key, and the estimates files
carry only the April 2020 estimates base, not the count itself. Claims checked by script: Frisco grew about 7 times
(6.98) and McKinney about 4 times (4.18) from 2000 to 2024; both passed 100,000 by 2010; no city lost population;
Dallas is the largest.

Definition note (boomburb): the item and its explanation use the broader classroom sense of "boomburb": a large,
fast-growing suburban city of more than 100,000 people that is not the largest city of its metro area. Lang and Simmons'
original study (2001) looked for sustained double-digit growth since 1950; Lang and LeFurgy's later book (2007) used 1970
as its starting year ("The starting year in this analysis is 1970, not 1950, as in the original research":
https://www.brookings.edu/wp-content/uploads/2016/07/boomburbs_chapter.pdf, checked Nov 8, 2026). The table covers
2000–2024 and does not establish either study's full historical criterion, and no item claims that Frisco or McKinney
appears on either list.

## Factual claims outside the stimuli

The topics, Learning Objective codes, and Essential Knowledge come from the 2020 AP Human Geography Course and Exam
Description (Unit 6, pp. 108–118). Other facts the items rely on are standard textbook facts, worded to avoid
specifics that could not be checked:

- Burgess concentric zone model (1925, based on Chicago); Hoyt sector model; Harris and Ullman multiple nuclei model;
  galactic city model; bid-rent theory; Griffin–Ford Latin American city model (1980); McGee's Southeast Asian city
  model (port zone as focus); de Blij's sub-Saharan African city model (three CBDs: colonial, traditional market,
  transitional).
- Christaller's central place theory (threshold, range, hexagonal market areas, isotropic plain); the gravity model
  (population product over distance squared); the rank-size rule; primate cities.
- Boomburb (large, fast-growing suburban city of 100,000+ that is not its metro area's main city; see the definition note
  above); edge
  city; exurb; megacity (10 million or more); metacity (20 million+).
- U.S. suburbanization after 1945 (FHA and VA/GI Bill home loans; Federal-Aid Highway Act of 1956); urban interstates
  routed through low-income and predominantly Black neighborhoods; HOLC residential security maps of the 1930s
  (grades A–D, D shaded red); blockbusting.
- Atlantic Seaboard fall line cities (Richmond, Trenton): water power and head of navigation.
- Census tracts usually hold about 1,200–8,000 people (optimum about 4,000).
