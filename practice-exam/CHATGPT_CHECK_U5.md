Please review this AP Human Geography Unit 5 (Agriculture and Rural Land-Use) multiple-choice question bank for my students' practice-exam website. Use your highest reasoning.

Context: 36 untimed practice questions (3 per CED topic 5.1–5.12, instant feedback with a 6th-grade-level explanation and one "why not" line per wrong option) and a 25-question timed exam (5 answer choices, College Board style rationales for every option, 10 stimulus-based questions in 4 sets). Modeled on the College Board 2020 AP Human Geography Practice Exam and the 2020 CED. All data marked "hypothetical" is invented on purpose. Students are 9th graders. Stimulus type "rings" draws a von Thünen ring diagram (center city, rings labeled from the inside out); "schematicMap" for U5-P06 draws a river band across the top, twelve long narrow parcels running down from it, a farmhouse at the river end of each, and a dashed road behind the houses.

Check, and report ONLY real problems, most serious first, each with the exact fix (replacement text):
1. Accuracy: any wrong key, factual error, outdated or overstated claim, or a CED mismatch (topic, learning objective, skill tag). Check the CED essential knowledge for 5.1–5.12 (e.g., plantation agriculture is listed as intensive; shifting cultivation, nomadic herding, ranching as extensive; von Thünen ring 2 = forest in the original model).
2. Ambiguity: any question where a second option is defensible, or where the key could be argued against by a strong student.
3. Arithmetic in every table and chart question (percent changes, comparisons in explanations).
4. Distractor quality and test-wiseness tells (grammar cues, absolute words, an option that repeats stem words, length).
5. Wording: explanations and whyNot lines at a 6th–8th grade reading level; rationales in College Board style; nothing condescending.
6. Sensitive content: anything about women in agriculture, Africa, or developing countries that is stereotyped or overgeneralized.
Keep it tight. No praise needed. Use the question IDs.

===== unit5.json =====
{
 "unit": 5,
 "title": "Agriculture and Rural Land-Use Patterns and Processes",
 "examWeighting": "12–17% of the AP Exam multiple-choice section",
 "version": "2026-11-07a",
 "calibration": "Modeled on the format of the College Board 2020 AP Human Geography Practice Exam and the Course and Exam Description (5 answer choices, set-based stimulus questions, skills 1–5). All questions, stimuli, and data are original or compiled from public facts; no College Board items are reproduced.",
 "checked": "Draft v2026-11-07a: automated checks (answer balance, option-length tells, field completeness).",
 "schemaNotes": {
  "stimulus.type": "table | bar | districtMap | schematicMap | rings (rings = von Thünen-style concentric ring diagram: center, rings[].label, outer, description)",
  "practice[].explanation": "6th-grade-level reason the answer is right (show this first)",
  "practice[].whyNot": "one line per wrong option",
  "exam.questions[].rationales": "College Board-style note on every option A–E",
  "exam.questions[].explanation": "6th-grade-level version for the review screen",
  "set": "questions sharing a stimulus carry the same set id; the stimulus object lives on the first question of the set"
 },
 "topics": [
  {
   "id": "5.1",
   "name": "Introduction to Agriculture",
   "lo": "PSO-5.A"
  },
  {
   "id": "5.2",
   "name": "Settlement Patterns and Survey Methods",
   "lo": "PSO-5.B"
  },
  {
   "id": "5.3",
   "name": "Agricultural Origins and Diffusions",
   "lo": "SPS-5.A, SPS-5.B"
  },
  {
   "id": "5.4",
   "name": "The Second Agricultural Revolution",
   "lo": "SPS-5.C"
  },
  {
   "id": "5.5",
   "name": "The Green Revolution",
   "lo": "SPS-5.D"
  },
  {
   "id": "5.6",
   "name": "Agricultural Production Regions",
   "lo": "PSO-5.C"
  },
  {
   "id": "5.7",
   "name": "Spatial Organization of Agriculture",
   "lo": "PSO-5.C"
  },
  {
   "id": "5.8",
   "name": "Von Thünen Model",
   "lo": "PSO-5.D"
  },
  {
   "id": "5.9",
   "name": "The Global System of Agriculture",
   "lo": "PSO-5.E"
  },
  {
   "id": "5.10",
   "name": "Consequences of Agricultural Practices",
   "lo": "IMP-5.A"
  },
  {
   "id": "5.11",
   "name": "Challenges of Contemporary Agriculture",
   "lo": "IMP-5.B"
  },
  {
   "id": "5.12",
   "name": "Women in Agriculture",
   "lo": "IMP-5.C"
  }
 ],
 "practice": [
  {
   "id": "U5-P01",
   "topic": "5.1",
   "lo": "PSO-5.A",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following is an example of extensive agriculture?",
   "options": {
    "A": "Market gardening of lettuce and tomatoes on small plots near a large city",
    "B": "Growing wet rice on small, hand-worked paddies in a densely populated river valley",
    "C": "Raising beef cattle on very large tracts of semiarid grassland",
    "D": "Running a dairy farm that keeps cows in barns and buys most of their feed",
    "E": "Growing sugarcane on a tropical plantation that employs hundreds of workers"
   },
   "answer": "C",
   "explanation": "Extensive agriculture uses a LOT of land but puts in very little work, money, or machinery per acre. Ranching is the classic example: a few cowboys and a herd of cattle spread out over thousands of acres of dry grassland. Shifting cultivation and nomadic herding are the other two extensive types to know.",
   "whyNot": {
    "A": "Market gardening squeezes lots of labor and money into small plots. That is intensive.",
    "B": "Wet-rice paddies take huge amounts of hand labor on small fields. That is intensive.",
    "D": "A barn dairy with bought feed puts lots of capital into a small area. That is intensive.",
    "E": "A plantation puts large numbers of workers and lots of money into the crop. The CED lists plantation agriculture as intensive."
   },
   "vocab": [
    "extensive agriculture",
    "intensive agriculture",
    "ranching"
   ]
  },
  {
   "id": "U5-P02",
   "topic": "5.1",
   "lo": "PSO-5.A",
   "skill": "2.D",
   "difficulty": "easy",
   "stem": "Olives, grapes, and citrus fruits are major crops in southern Spain, central Chile, and coastal California. Which feature of the physical environment best explains this similarity?",
   "options": {
    "A": "All three regions have hot, dry summers and mild, rainy winters.",
    "B": "All three regions receive heavy rainfall in every month of the year.",
    "C": "All three regions have long, cold winters and short growing seasons.",
    "D": "All three regions depend on summer monsoon rains for most of their water.",
    "E": "All three regions sit at high elevations where frost is common in summer."
   },
   "answer": "A",
   "explanation": "These three places share a Mediterranean climate: hot, dry summers and mild, wet winters. Olive trees, grapevines, and citrus trees have deep roots and tough leaves that handle the dry summer, so farmers in all three places grow the same kinds of crops even though they are on different continents.",
   "whyNot": {
    "B": "Rain in every month describes a wet tropical or marine climate, not a Mediterranean one.",
    "C": "Long, cold winters would kill citrus trees. These regions have mild winters.",
    "D": "Monsoon climates (like much of South Asia) get rain in summer. Mediterranean regions are dry in summer.",
    "E": "Summer frost would ruin these crops. All three regions are warm in summer."
   },
   "vocab": [
    "Mediterranean climate",
    "physical environment"
   ]
  },
  {
   "id": "U5-P03",
   "topic": "5.1",
   "lo": "PSO-5.A",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "FIVE FARMS IN ONE COUNTRY (HYPOTHETICAL DATA)",
    "columns": [
     "Farm",
     "Land farmed (hectares)",
     "Labor and capital spent per hectare (dollars)",
     "Value of output per hectare (dollars)",
     "Main product"
    ],
    "rows": [
     [
      "Farm 1",
      "12,000",
      "40",
      "90",
      "Beef cattle on open grassland"
     ],
     [
      "Farm 2",
      "3",
      "9,500",
      "28,000",
      "Vegetables sold in a nearby city"
     ],
     [
      "Farm 3",
      "800",
      "600",
      "1,400",
      "Wheat"
     ],
     [
      "Farm 4",
      "45,000",
      "15",
      "35",
      "Sheep and goats moved seasonally"
     ],
     [
      "Farm 5",
      "20",
      "50",
      "200",
      "Food crops in forest clearings moved every few years"
     ]
    ],
    "source": "Hypothetical data"
   },
   "stem": "Based on the table, which farm best represents intensive agriculture?",
   "options": {
    "A": "Farm 1",
    "B": "Farm 4",
    "C": "Farm 2",
    "D": "Farm 3",
    "E": "Farm 5"
   },
   "answer": "C",
   "explanation": "Intensive farming means putting a LOT of labor and money into a SMALL piece of land to get a high output from every hectare. Farm 2 farms only 3 hectares but spends $9,500 per hectare and earns $28,000 per hectare. That is market gardening, one of the intensive types in the CED.",
   "whyNot": {
    "A": "Farm 1 is ranching: huge land, tiny spending per hectare. That is extensive.",
    "B": "Farm 4 is nomadic herding: the most land and the least spending per hectare. Extensive.",
    "D": "Farm 3 spends more per hectare than the herders, but far less than Farm 2. It is the middle case, not the best example of intensive.",
    "E": "Farm 5 is shifting cultivation, which the CED lists as extensive."
   },
   "vocab": [
    "intensive agriculture",
    "market gardening",
    "shifting cultivation",
    "nomadic herding"
   ]
  },
  {
   "id": "U5-P04",
   "topic": "5.2",
   "lo": "PSO-5.B",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which rural survey method divided land in much of the United States west of the Appalachian Mountains into a grid of six-mile-square townships, each split into 36 sections of one square mile?",
   "options": {
    "A": "Metes and bounds",
    "B": "The long-lot system",
    "C": "The enclosure movement",
    "D": "Township and range",
    "E": "The open-field system"
   },
   "answer": "D",
   "explanation": "Township and range (the Public Land Survey System) started with the Land Ordinance of 1785. Surveyors laid a grid over the land before most settlers arrived, so the Midwest looks like a checkerboard of square fields and straight roads from an airplane.",
   "whyNot": {
    "A": "Metes and bounds uses landmarks like streams and trees, so parcels have irregular shapes.",
    "B": "Long lots are narrow strips running back from a river, used in French areas like Quebec and Louisiana.",
    "C": "Enclosure was the British fencing-in of common land during the Second Agricultural Revolution, not a survey grid.",
    "E": "The open-field system was the medieval European pattern of scattered strips around a village."
   },
   "vocab": [
    "township and range",
    "Public Land Survey System",
    "section"
   ]
  },
  {
   "id": "U5-P05",
   "topic": "5.2",
   "lo": "PSO-5.B",
   "skill": "1.D",
   "difficulty": "medium",
   "stem": "Farmland in parts of Quebec and Louisiana is divided into long, narrow parcels that run back from a river, with farmhouses lined up along the riverbank. Which statement best explains this pattern?",
   "options": {
    "A": "Railroad companies sold land in square sections along their tracks to attract settlers.",
    "B": "The U.S. government applied the township and range grid, which always produces long, narrow lots.",
    "C": "Early settlers clustered their homes in a central village for defense and walked out to fields in all directions.",
    "D": "Farmers used metes and bounds, which required every boundary to run in a straight north-south line.",
    "E": "French settlers used the long-lot system so that each farm had access to the river for water and transportation."
   },
   "answer": "E",
   "explanation": "French colonists wanted every family to reach the river, because the river was their road and their water supply. So they cut the land into long, skinny strips that all touch the water. Homes were built at the river end of each strip, which makes a linear settlement pattern: a line of houses along the river.",
   "whyNot": {
    "B": "Township and range makes squares, not long strips, and it was not used in French Quebec.",
    "C": "That describes a clustered (nucleated) settlement, not houses strung out along a river.",
    "D": "Metes and bounds follows natural landmarks, so its boundaries are irregular, not straight north-south lines.",
    "A": "Railroad land sales followed the township and range grid of squares, mostly in the U.S. West."
   },
   "vocab": [
    "long-lot system",
    "linear settlement"
   ]
  },
  {
   "id": "U5-P06",
   "topic": "5.2",
   "lo": "PSO-5.B",
   "skill": "4.D",
   "difficulty": "medium",
   "stimulus": {
    "type": "schematicMap",
    "title": "RURAL LAND DIVISION ALONG A RIVER (HYPOTHETICAL)",
    "canvas": {
     "width": 800,
     "height": 380
    },
    "features": [
     {
      "kind": "land",
      "name": "",
      "polygon": [
       [
        0,
        70
       ],
       [
        70,
        70
       ],
       [
        70,
        380
       ],
       [
        0,
        380
       ]
      ],
      "style": "small"
     },
     {
      "kind": "land",
      "name": "",
      "polygon": [
       [
        70,
        70
       ],
       [
        130,
        70
       ],
       [
        130,
        380
       ],
       [
        70,
        380
       ]
      ],
      "style": "small"
     },
     {
      "kind": "land",
      "name": "",
      "polygon": [
       [
        130,
        70
       ],
       [
        205,
        70
       ],
       [
        205,
        380
       ],
       [
        130,
        380
       ]
      ],
      "style": "small"
     },
     {
      "kind": "land",
      "name": "",
      "polygon": [
       [
        205,
        70
       ],
       [
        260,
        70
       ],
       [
        260,
        380
       ],
       [
        205,
        380
       ]
      ],
      "style": "small"
     },
     {
      "kind": "land",
      "name": "",
      "polygon": [
       [
        260,
        70
       ],
       [
        330,
        70
       ],
       [
        330,
        380
       ],
       [
        260,
        380
       ]
      ],
      "style": "small"
     },
     {
      "kind": "land",
      "name": "",
      "polygon": [
       [
        330,
        70
       ],
       [
        390,
        70
       ],
       [
        390,
        380
       ],
       [
        330,
        380
       ]
      ],
      "style": "small"
     },
     {
      "kind": "land",
      "name": "",
      "polygon": [
       [
        390,
        70
       ],
       [
        460,
        70
       ],
       [
        460,
        380
       ],
       [
        390,
        380
       ]
      ],
      "style": "small"
     },
     {
      "kind": "land",
      "name": "",
      "polygon": [
       [
        460,
        70
       ],
       [
        520,
        70
       ],
       [
        520,
        380
       ],
       [
        460,
        380
       ]
      ],
      "style": "small"
     },
     {
      "kind": "land",
      "name": "",
      "polygon": [
       [
        520,
        70
       ],
       [
        590,
        70
       ],
       [
        590,
        380
       ],
       [
        520,
        380
       ]
      ],
      "style": "small"
     },
     {
      "kind": "land",
      "name": "",
      "polygon": [
       [
        590,
        70
       ],
       [
        650,
        70
       ],
       [
        650,
        380
       ],
       [
        590,
        380
       ]
      ],
      "style": "small"
     },
     {
      "kind": "land",
      "name": "",
      "polygon": [
       [
        650,
        70
       ],
       [
        725,
        70
       ],
       [
        725,
        380
       ],
       [
        650,
        380
       ]
      ],
      "style": "small"
     },
     {
      "kind": "land",
      "name": "",
      "polygon": [
       [
        725,
        70
       ],
       [
        800,
        70
       ],
       [
        800,
        380
       ],
       [
        725,
        380
       ]
      ],
      "style": "small"
     },
     {
      "kind": "line",
      "name": "Road",
      "line": [
       [
        0,
        100
       ],
       [
        800,
        100
       ]
      ],
      "dashed": true
     },
     {
      "kind": "marker",
      "name": "Farmhouse",
      "points": [
       [
        35,
        85
       ],
       [
        100,
        85
       ],
       [
        167,
        85
       ],
       [
        232,
        85
       ],
       [
        295,
        85
       ],
       [
        360,
        85
       ],
       [
        425,
        85
       ],
       [
        490,
        85
       ],
       [
        555,
        85
       ],
       [
        620,
        85
       ],
       [
        687,
        85
       ],
       [
        762,
        85
       ]
      ],
      "symbol": "house"
     }
    ],
    "legend": [
     {
      "swatch": "water",
      "label": "River"
     },
     {
      "swatch": "small",
      "label": "Farm parcel"
     },
     {
      "swatch": "house",
      "label": "Farmhouse"
     },
     {
      "swatch": "road",
      "label": "Road"
     }
    ],
    "description": "A river runs along the top of the map. Twelve long, narrow farm parcels run from the riverbank toward the bottom of the map. A farmhouse sits at the river end of every parcel, and a road runs parallel to the river just behind the houses.",
    "source": "Hypothetical map"
   },
   "stem": "The map shows a rural landscape. Which combination of survey method and settlement pattern does it best illustrate?",
   "options": {
    "A": "Metes and bounds survey with a clustered settlement pattern",
    "B": "Township and range survey with a dispersed settlement pattern",
    "C": "Township and range survey with a linear settlement pattern",
    "D": "Long-lot survey with a clustered settlement pattern",
    "E": "Long-lot survey with a linear settlement pattern"
   },
   "answer": "E",
   "explanation": "Two things to spot: the SHAPE of the land and WHERE the houses are. The parcels are long, skinny strips that all touch the river, so the survey method is long lot. The houses sit in a row along the river and road, so the settlement pattern is linear. Survey method = how land is divided. Settlement pattern = where people live.",
   "whyNot": {
    "A": "Metes and bounds makes irregular parcels, and the houses here are in a line, not grouped in a village.",
    "B": "Township and range makes square sections with farmhouses spread out. These are long strips with houses in a row.",
    "C": "The houses do form a line, but the parcels are long strips, not township-and-range squares.",
    "D": "The parcels are long lots, but the houses are lined up along the river, not grouped in one village."
   },
   "vocab": [
    "long-lot system",
    "linear settlement",
    "clustered settlement",
    "dispersed settlement"
   ]
  },
  {
   "id": "U5-P07",
   "topic": "5.3",
   "lo": "SPS-5.A",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following regions was an early hearth of plant and animal domestication, where wheat, barley, sheep, and goats were first domesticated?",
   "options": {
    "A": "The Great Plains of North America",
    "B": "The Fertile Crescent of Southwest Asia",
    "C": "The Amazon Basin of South America",
    "D": "The Scandinavian Peninsula of northern Europe",
    "E": "The interior of Australia"
   },
   "answer": "B",
   "explanation": "The Fertile Crescent is an arc of good farmland in Southwest Asia, around the Tigris and Euphrates Rivers and the eastern Mediterranean coast. About 10,000 years ago, people there began planting wheat and barley and taming sheep and goats. The CED also names the Indus River Valley, Southeast Asia, and Central America as early hearths.",
   "whyNot": {
    "A": "Plains peoples farmed in river valleys, but the Great Plains was not a hearth for wheat, barley, sheep, or goats. Those reached the Americas after 1492.",
    "C": "Some Amazonian peoples domesticated crops such as cassava, but not wheat, barley, sheep, or goats.",
    "D": "Farming reached Scandinavia late, by diffusion from the south.",
    "E": "Interior Australia was not a hearth of domestication, and these crops and animals came there with European colonists."
   },
   "vocab": [
    "hearth",
    "domestication",
    "Fertile Crescent"
   ]
  },
  {
   "id": "U5-P08",
   "topic": "5.3",
   "lo": "SPS-5.B",
   "skill": "1.D",
   "difficulty": "medium",
   "stem": "Which of the following is an example of plant diffusion as part of the Columbian Exchange?",
   "options": {
    "A": "Wheat spreading from the Fertile Crescent into Europe thousands of years ago",
    "B": "Rice spreading from southern China into Southeast Asia thousands of years before European voyages",
    "C": "High-yield wheat varieties spreading from Mexico to India in the 1960s",
    "D": "Maize and potatoes spreading from the Americas to Europe, Africa, and Asia after 1492",
    "E": "Genetically modified soybeans spreading across South America in the 2000s"
   },
   "answer": "D",
   "explanation": "The Columbian Exchange was the swap of plants, animals, people, and diseases between the Americas and the rest of the world that began after Columbus's voyages in 1492. Maize (corn) and potatoes from the Americas became major foods in Europe, Africa, and Asia, while wheat, cattle, and horses moved the other way.",
   "whyNot": {
    "A": "That is diffusion from the first agricultural hearths, thousands of years before 1492.",
    "B": "That is ancient diffusion within Asia, not an exchange between the Americas and the rest of the world.",
    "C": "That is the Green Revolution of the 1960s.",
    "E": "GMO soybeans are modern biotechnology, not the Columbian Exchange."
   },
   "vocab": [
    "Columbian Exchange",
    "diffusion"
   ]
  },
  {
   "id": "U5-P09",
   "topic": "5.3",
   "lo": "SPS-5.B",
   "skill": "2.B",
   "difficulty": "hard",
   "stem": "Cassava, a root crop first domesticated in South America, became a staple food across much of tropical Africa after the 1500s. Which statement best explains this?",
   "options": {
    "A": "Cassava was carried to Africa by Portuguese traders as part of the Columbian Exchange and grows well in poor soils and during dry spells.",
    "B": "Cassava was domesticated a second time in the Nile River valley, so African farmers already had it before the 1500s.",
    "C": "Cassava spread to Africa during the Green Revolution, when scientists bred it for irrigated farms.",
    "D": "Cassava requires cold winters to produce roots, so it grew best in the cooler parts of Africa.",
    "E": "Cassava spread to Africa during the Second Agricultural Revolution, when new machines made it easier to plant."
   },
   "answer": "A",
   "explanation": "Portuguese ships brought cassava from Brazil to West and Central Africa in the 1500s. That is the Columbian Exchange. African farmers kept it because it is tough: it grows in poor soil, survives dry spells, and can stay in the ground until people need it. That made it a good protection against hunger.",
   "whyNot": {
    "B": "Cassava was domesticated in South America. Africa got it by diffusion, not by a second domestication.",
    "C": "Cassava arrived in Africa about 400 years before the Green Revolution, which focused on wheat, rice, and maize.",
    "D": "Cassava is a tropical crop. Frost and cold kill it.",
    "E": "The Second Agricultural Revolution happened in Europe in the 1700s and 1800s and was not how cassava reached Africa."
   },
   "vocab": [
    "Columbian Exchange",
    "staple crop"
   ]
  },
  {
   "id": "U5-P10",
   "topic": "5.4",
   "lo": "SPS-5.C",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which pair of innovations is most closely associated with the Second Agricultural Revolution?",
   "options": {
    "A": "Domestication of wheat and the first irrigation canals",
    "B": "High-yield rice varieties and chemical fertilizers in South Asia",
    "C": "Genetically modified seeds and drone crop monitoring",
    "D": "Shifting cultivation and the first use of fire to clear land",
    "E": "The seed drill and four-field crop rotation"
   },
   "answer": "E",
   "explanation": "The Second Agricultural Revolution started in Britain in the 1700s, alongside the Industrial Revolution. The seed drill planted seeds in neat rows instead of tossing them by hand, and four-field crop rotation (wheat, turnips, barley, clover) kept soil fertile without leaving fields empty. Later came steel plows, mechanical reapers, and tractors.",
   "whyNot": {
    "A": "That is the First Agricultural Revolution (the Neolithic Revolution), thousands of years earlier.",
    "B": "That is the Green Revolution of the 1960s and 1970s.",
    "C": "GMOs and drones are modern biotechnology and precision farming.",
    "D": "Shifting cultivation and burning to clear land are ancient practices, not the Second Agricultural Revolution."
   },
   "vocab": [
    "Second Agricultural Revolution",
    "seed drill",
    "crop rotation"
   ]
  },
  {
   "id": "U5-P11",
   "topic": "5.4",
   "lo": "SPS-5.C",
   "skill": "1.D",
   "difficulty": "medium",
   "stem": "Which of the following was a major result of the Second Agricultural Revolution in Britain?",
   "options": {
    "A": "Farms became smaller as common land was divided up among a growing number of peasant families.",
    "B": "Food production fell, causing life expectancy to drop across the country.",
    "C": "Most farmers returned to subsistence farming and stopped selling crops.",
    "D": "The rural population grew rapidly as farms needed more hand labor.",
    "E": "Fewer farmworkers were needed, so many rural people moved to cities to work in factories."
   },
   "answer": "E",
   "explanation": "New tools and methods let each farmer grow much more food. So farms needed fewer workers, and many rural families moved to cities to work in the new factories. The extra food also meant better diets and longer lives. The CED says it led to better diets, longer life expectancies, and more people available to work in factories.",
   "whyNot": {
    "B": "Food production rose, and life expectancy improved.",
    "C": "Farming became more commercial, with more food sold to growing cities.",
    "D": "Machines replaced workers, so the share of people living on farms fell.",
    "A": "Enclosure did the opposite: it combined small plots and common land into larger private farms."
   },
   "vocab": [
    "Second Agricultural Revolution",
    "enclosure",
    "urbanization"
   ]
  },
  {
   "id": "U5-P12",
   "topic": "5.4",
   "lo": "SPS-5.C",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "FARMING AND URBANIZATION IN COUNTRY X, 1750–1900 (HYPOTHETICAL DATA)",
    "columns": [
     "Year",
     "Wheat yield (bushels per acre)",
     "Share of workers in agriculture (%)",
     "Share of people living in cities (%)"
    ],
    "rows": [
     [
      "1750",
      "16",
      "55",
      "20"
     ],
     [
      "1800",
      "21",
      "40",
      "30"
     ],
     [
      "1850",
      "28",
      "22",
      "50"
     ],
     [
      "1900",
      "31",
      "9",
      "75"
     ]
    ],
    "source": "Hypothetical data"
   },
   "stem": "Which conclusion about Country X is best supported by the data in the table?",
   "options": {
    "A": "Falling wheat yields forced farmworkers to leave the countryside.",
    "B": "Rising farm productivity let a shrinking share of workers feed a growing urban population.",
    "C": "The share of people living in cities fell as farms became more productive.",
    "D": "Agriculture employed a larger share of workers in 1900 than in 1750.",
    "E": "Wheat yields rose fastest between 1850 and 1900, the same period when farm employment was rising."
   },
   "answer": "B",
   "explanation": "Read the columns together. Wheat yields go UP (16 to 31). The share of workers on farms goes DOWN (55% to 9%). The share of people in cities goes UP (20% to 75%). So each farmer is producing more, fewer people need to farm, and more people can live and work in cities. That is the Second Agricultural Revolution working alongside the Industrial Revolution.",
   "whyNot": {
    "A": "Yields rose in every period, so they were not falling.",
    "C": "The urban share rose from 20% to 75%.",
    "D": "The farm share of workers fell from 55% to 9%.",
    "E": "Yields grew by only 3 bushels from 1850 to 1900 (the smallest gain), and farm employment was falling."
   },
   "vocab": [
    "Second Agricultural Revolution",
    "productivity",
    "urbanization"
   ]
  },
  {
   "id": "U5-P13",
   "topic": "5.5",
   "lo": "SPS-5.D",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following best describes the Green Revolution?",
   "options": {
    "A": "The movement to replace chemical fertilizers with organic methods on farms in wealthy countries",
    "B": "The first domestication of plants and animals in river valleys of Southwest and South Asia",
    "C": "The return of eroded farmland to native grasses to reduce soil erosion and dust storms",
    "D": "The conversion of tropical forests in developing countries into protected national parks",
    "E": "The spread of high-yield seeds, fertilizers, pesticides, and irrigation in developing countries after the mid-1900s"
   },
   "answer": "E",
   "explanation": "The Green Revolution began in the 1940s through 1960s, when scientists such as Norman Borlaug bred high-yield varieties (HYVs) of wheat and rice. Farmers in places like Mexico, India, and the Philippines planted these seeds and added chemical fertilizer, pesticides, irrigation, and machines. Harvests grew a lot. The CED lists high-yield seeds, more chemicals, and mechanized farming.",
   "whyNot": {
    "A": "That describes organic farming, which uses fewer chemicals. The Green Revolution used more.",
    "B": "That is the First Agricultural Revolution.",
    "D": "\"Green\" here means crops, not parks or conservation.",
    "C": "That describes conservation programs, not the Green Revolution."
   },
   "vocab": [
    "Green Revolution",
    "high-yield varieties (HYVs)"
   ]
  },
  {
   "id": "U5-P14",
   "topic": "5.5",
   "lo": "SPS-5.D",
   "skill": "2.D",
   "difficulty": "medium",
   "stem": "In the Indian state of Punjab, Green Revolution wheat and rice farming raised harvests sharply. Which of the following is a negative environmental consequence of these practices in Punjab?",
   "options": {
    "A": "Rapid expansion of tropical rain forest onto former farmland",
    "B": "A sharp drop in farmers' use of chemical fertilizers and pesticides on wheat and rice",
    "C": "An end to irrigation because the new seeds need no extra water",
    "D": "Falling water tables from heavy groundwater pumping for irrigation",
    "E": "A return to shifting cultivation as farmers moved to new fields"
   },
   "answer": "D",
   "explanation": "High-yield rice and wheat need a lot of water and fertilizer. Punjab farmers pumped so much groundwater from wells that the water table has dropped steadily, and wells must be dug deeper. Heavy fertilizer and pesticide use has also hurt soil and water quality. Those are the environmental costs of the Green Revolution's bigger harvests.",
   "whyNot": {
    "A": "Punjab is not a rain-forest region, and the Green Revolution kept land in crops.",
    "B": "Chemical use went UP, not down.",
    "C": "HYVs need MORE water, so irrigation expanded.",
    "E": "Farming in Punjab became more intensive and permanent, not shifting."
   },
   "vocab": [
    "Green Revolution",
    "irrigation",
    "groundwater depletion"
   ]
  },
  {
   "id": "U5-P15",
   "topic": "5.5",
   "lo": "SPS-5.D",
   "skill": "3.D",
   "difficulty": "medium",
   "stimulus": {
    "type": "bar",
    "title": "AVERAGE CEREAL YIELD IN TWO REGIONS, 1960 AND 1990 (HYPOTHETICAL DATA)",
    "categories": [
     "Region P",
     "Region Q"
    ],
    "series": [
     {
      "name": "1960 (tonnes per hectare)",
      "values": [
       1.0,
       0.8
      ]
     },
     {
      "name": "1990 (tonnes per hectare)",
      "values": [
       2.3,
       1.0
      ]
     }
    ],
    "yLabel": "Tonnes per hectare",
    "yMax": 2.5,
    "text": "Region P grows mostly irrigated wheat and rice. Region Q grows mostly rain-fed sorghum, millet, and cassava, and few farmers can reach irrigation, fertilizer dealers, or paved roads.",
    "source": "Hypothetical data"
   },
   "stem": "Which statement best explains the difference between the two regions shown in the chart?",
   "options": {
    "A": "Region Q's farmers chose to stop using chemical fertilizer, while Region P's farmers began using it for the first time.",
    "B": "Region Q has a colder climate, so it could not grow any cereal crops.",
    "C": "Region P's yields rose because its farmers moved to shifting cultivation.",
    "D": "Region P's population fell, so each farmer had more land to work.",
    "E": "Green Revolution seeds and inputs were designed mainly for irrigated wheat and rice, so Region P gained far more."
   },
   "answer": "E",
   "explanation": "Region P more than doubled its yield (1.0 to 2.3 tonnes per hectare), while Region Q barely changed (0.8 to 1.0). The Green Revolution's high-yield seeds were mostly wheat, rice, and maize, and they work best with irrigation and fertilizer. Region P had those crops and inputs. Region Q's crops and lack of roads and irrigation meant the Green Revolution helped it much less. This is a big reason the Green Revolution had a smaller effect in much of Sub-Saharan Africa than in South Asia.",
   "whyNot": {
    "A": "The text says Region Q's farmers can't easily get fertilizer. Nothing says they chose to stop.",
    "B": "Region Q does grow cereals (sorghum and millet), and the chart shows a yield there.",
    "C": "Shifting cultivation is extensive and low-yield. It would not more than double yields.",
    "D": "Nothing in the chart or text describes Region P's population."
   },
   "vocab": [
    "Green Revolution",
    "high-yield varieties (HYVs)",
    "yield"
   ]
  },
  {
   "id": "U5-P16",
   "topic": "5.6",
   "lo": "PSO-5.C",
   "skill": "1.D",
   "difficulty": "easy",
   "stem": "A large farm in Brazil plants only soybeans every year and sells the entire harvest to export companies. This farm is an example of which agricultural practice?",
   "options": {
    "A": "Subsistence farming",
    "B": "Commercial monocropping",
    "C": "Shifting cultivation",
    "D": "Pastoral nomadism",
    "E": "Mixed crop and livestock farming"
   },
   "answer": "B",
   "explanation": "Commercial farming grows crops to SELL, not to feed the farm family. Monocropping means growing the same single crop on the same land year after year. A huge soybean farm selling everything for export is both. The CED says production regions are defined by whether they are subsistence or commercial, including monocropping or monoculture.",
   "whyNot": {
    "A": "Subsistence farmers grow food mainly to feed their own families. This farm sells everything.",
    "C": "Shifting cultivation moves to new forest clearings every few years. This farm stays put.",
    "D": "Pastoral nomadism is herding animals from place to place, not growing soybeans.",
    "E": "Mixed farming raises crops AND livestock together. This farm grows only one crop."
   },
   "vocab": [
    "commercial agriculture",
    "monocropping",
    "subsistence agriculture"
   ]
  },
  {
   "id": "U5-P17",
   "topic": "5.6",
   "lo": "PSO-5.C",
   "skill": "1.B",
   "difficulty": "medium",
   "stem": "According to bid-rent theory, why is farmland closest to a large city usually farmed more intensively than land farther away?",
   "options": {
    "A": "Soil is always more fertile near cities than in rural areas.",
    "B": "Land near the city costs more, so farmers must earn a high output per acre to afford it.",
    "C": "Governments ban extensive farming within city limits.",
    "D": "Farmers near cities have fewer customers, so they must grow more food.",
    "E": "Transportation costs are higher for land close to the city than for land far away."
   },
   "answer": "B",
   "explanation": "Bid-rent theory says people bid more for land that is close to the market, because being close saves money on transportation. Higher land prices mean a farmer near the city has to squeeze a lot of value out of every acre, like vegetables or dairy. Farther out, land is cheap, so low-value uses that need lots of land, like grazing, make sense. The CED says intensive and extensive practices are decided partly by land costs (bid-rent).",
   "whyNot": {
    "A": "Soil quality is not what the theory is about, and it is not always better near cities.",
    "D": "Farmers near cities have MORE nearby customers, not fewer.",
    "E": "It is the opposite: transportation costs rise as you move AWAY from the city.",
    "C": "Bid-rent is about land prices, not laws."
   },
   "vocab": [
    "bid-rent theory",
    "intensive agriculture",
    "land cost"
   ]
  },
  {
   "id": "U5-P18",
   "topic": "5.6",
   "lo": "PSO-5.C",
   "skill": "3.C",
   "difficulty": "hard",
   "stimulus": {
    "type": "bar",
    "title": "NET RETURN PER HECTARE BY DISTANCE FROM A CITY MARKET (HYPOTHETICAL DATA)",
    "categories": [
     "0–20 km",
     "20–50 km",
     "50–100 km",
     "100–200 km"
    ],
    "series": [
     {
      "name": "Fresh vegetables (dollars per hectare)",
      "values": [
       2400,
       1500,
       400,
       0
      ]
     },
     {
      "name": "Cattle grazing (dollars per hectare)",
      "values": [
       300,
       280,
       260,
       240
      ]
     }
    ],
    "yLabel": "Net return (dollars per hectare)",
    "yMax": 2500,
    "text": "Net return is the money a farmer earns from one hectare after paying for labor, seed, feed, and transporting the product to the city.",
    "source": "Hypothetical data"
   },
   "stem": "Which statement is best supported by the chart?",
   "options": {
    "A": "Cattle grazing earns a higher net return than fresh vegetables at every distance from the city.",
    "B": "Vegetable farming earns its highest net return in the zone farthest from the city market.",
    "C": "Both land uses lose net return at about the same rate as distance from the city increases.",
    "D": "Vegetables earn far more near the city, but their return falls faster with distance than grazing's does.",
    "E": "Distance from the city market has no effect on the net return from either land use."
   },
   "answer": "D",
   "explanation": "Near the city, vegetables earn $2,400 per hectare and cattle only $300. But vegetables are perishable and costly to ship, so their return drops fast: $1,500, then $400, then $0. Cattle grazing barely drops. Beyond about 100 km, grazing wins. That is bid-rent at work: the intensive, high-value use takes the land near the market, and the extensive use takes the land far away.",
   "whyNot": {
    "A": "Vegetables earn more in the first three distance zones.",
    "B": "Vegetables earn the LEAST far from the city ($0 at 100–200 km).",
    "C": "Vegetables fall by $2,400 while grazing falls by only $60. Not the same rate.",
    "E": "Both returns fall with distance, vegetables most of all."
   },
   "vocab": [
    "bid-rent theory",
    "intensive agriculture",
    "extensive agriculture"
   ]
  },
  {
   "id": "U5-P19",
   "topic": "5.7",
   "lo": "PSO-5.C",
   "skill": "1.D",
   "difficulty": "easy",
   "stem": "A single company owns chicken hatcheries and feed mills, signs contracts with farmers to raise its chickens, and runs its own processing plants and delivery trucks. This is an example of",
   "options": {
    "A": "subsistence agriculture",
    "B": "shifting cultivation",
    "C": "vertical integration in agribusiness",
    "D": "the Columbian Exchange",
    "E": "community-supported agriculture"
   },
   "answer": "C",
   "explanation": "Agribusiness means farming run like a big business, with large companies involved at many steps. Vertical integration means one company controls several steps of the chain: here it owns the chicks, the feed, the processing, and the trucks, and farmers raise the birds under contract. The U.S. poultry industry works this way.",
   "whyNot": {
    "A": "Subsistence farmers grow food for their own families, not for a corporation.",
    "B": "Shifting cultivation is clearing and farming forest plots for a few years, then moving on.",
    "D": "The Columbian Exchange was the swap of crops and animals after 1492.",
    "E": "Community-supported agriculture connects local customers directly to a small farm."
   },
   "vocab": [
    "agribusiness",
    "vertical integration",
    "commodity chain"
   ]
  },
  {
   "id": "U5-P20",
   "topic": "5.7",
   "lo": "PSO-5.C",
   "skill": "1.D",
   "difficulty": "medium",
   "stem": "Which development best illustrates technology increasing the carrying capacity of farmland?",
   "options": {
    "A": "Farmers abandon fields after the soil loses its fertility.",
    "B": "Center-pivot irrigation and improved seeds let the same acreage feed more people.",
    "C": "A region converts farmland into new housing subdivisions.",
    "D": "Herders move their animals to new pastures each season.",
    "E": "A farm stops using tractors and other machinery and returns to plowing its fields with animals."
   },
   "answer": "B",
   "explanation": "Carrying capacity is how many people the land can support. If the same acres produce more food, the land can feed more people. Irrigation brings water to dry fields, and better seeds grow bigger harvests. The CED says technology has increased economies of scale in agriculture and the carrying capacity of the land.",
   "whyNot": {
    "A": "Abandoning worn-out fields lowers how many people the land supports.",
    "C": "Turning farms into housing removes farmland. It does not raise its output.",
    "D": "Seasonal herding is a traditional practice, not new technology raising output.",
    "E": "Going back to animal plowing usually lowers output per acre and per worker."
   },
   "vocab": [
    "carrying capacity",
    "economies of scale",
    "center-pivot irrigation"
   ]
  },
  {
   "id": "U5-P21",
   "topic": "5.7",
   "lo": "PSO-5.C",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "FARMS IN COUNTRY Z, 1950–2020 (HYPOTHETICAL DATA)",
    "columns": [
     "Year",
     "Number of farms (millions)",
     "Average farm size (acres)",
     "Total farmland (millions of acres)"
    ],
    "rows": [
     [
      "1950",
      "5.4",
      "215",
      "1,161"
     ],
     [
      "1980",
      "2.4",
      "425",
      "1,020"
     ],
     [
      "2020",
      "2.0",
      "445",
      "890"
     ]
    ],
    "source": "Hypothetical data"
   },
   "stem": "The trend in the table best illustrates which of the following?",
   "options": {
    "A": "Large-scale commercial operations replacing small family farms",
    "B": "A shift from commercial farming to subsistence farming",
    "C": "A rapid increase in the total amount of land being farmed",
    "D": "The breakup of large estates into many small peasant farms owned by individual families",
    "E": "A return to shifting cultivation as farmers move to new land"
   },
   "answer": "A",
   "explanation": "The number of farms fell by more than half (5.4 million to 2.0 million) while the average farm doubled in size (215 to 445 acres). That means small farms were bought up or combined into bigger ones. Big operations can buy machines and supplies in bulk and spread the cost over more acres (economies of scale). The CED says large-scale commercial operations are replacing small family farms.",
   "whyNot": {
    "B": "Bigger farms with fewer owners point to MORE commercial farming, not subsistence.",
    "C": "Total farmland FELL, from 1,161 to 890 million acres.",
    "D": "Farms got bigger and fewer, the opposite of breaking up estates.",
    "E": "Nothing in the table suggests shifting cultivation, and farm counts would not fall that way."
   },
   "vocab": [
    "agribusiness",
    "economies of scale",
    "family farm"
   ]
  },
  {
   "id": "U5-P22",
   "topic": "5.8",
   "lo": "PSO-5.D",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "In von Thünen's model of agricultural land use, which activity is located in the ring closest to the market city?",
   "options": {
    "A": "Market gardening and dairying",
    "B": "Livestock ranching",
    "C": "Grain and field crops",
    "D": "Forestry for firewood and lumber",
    "E": "Unused wilderness"
   },
   "answer": "A",
   "explanation": "Von Thünen said the most perishable and expensive-to-ship products go closest to the city. Fresh vegetables and milk spoil fast, so they were grown right next to the market (in the 1820s, there were no refrigerated trucks). Then came forest, then grain, then ranching, with wilderness beyond.",
   "whyNot": {
    "B": "Ranching is in the outermost farming ring, because it needs lots of cheap land and animals can walk to market.",
    "C": "Grain is in the third ring. It keeps well, so it can travel farther.",
    "D": "Forest is in the second ring, close because wood is heavy and costly to haul.",
    "E": "Wilderness lies beyond all the rings."
   },
   "vocab": [
    "von Thünen model",
    "market gardening",
    "perishable"
   ]
  },
  {
   "id": "U5-P23",
   "topic": "5.8",
   "lo": "PSO-5.D",
   "skill": "5.B",
   "difficulty": "medium",
   "stimulus": {
    "type": "rings",
    "title": "VON THÜNEN'S MODEL OF RURAL LAND USE",
    "center": "Market city",
    "rings": [
     {
      "label": "1"
     },
     {
      "label": "2"
     },
     {
      "label": "3"
     },
     {
      "label": "4"
     }
    ],
    "outer": "Wilderness",
    "description": "Four rings surround a single market city on a flat, uniform plain. Ring 1 touches the city; ring 4 is farthest away. Farmers haul their own goods to the city, so transportation cost rises with distance.",
    "source": "Simplified from von Thünen, The Isolated State (1826)"
   },
   "stem": "In von Thünen's original model, shown in the diagram, which land use occupied ring 2, and why?",
   "options": {
    "A": "Ranching, because cattle can walk to the city on their own",
    "B": "Grain, because wheat spoils quickly and must be sold within a day",
    "C": "Market gardening, because vegetables need the most land per farm",
    "D": "Forestry, because wood for fuel and building was heavy and costly to haul",
    "E": "Dairying, because milk could be stored for months without spoiling"
   },
   "answer": "D",
   "explanation": "This surprises people: von Thünen put FOREST in ring 2, right after the vegetable and dairy ring. In the 1820s, cities burned wood for heat and cooking and built with lumber. Wood is heavy and bulky, so hauling it far by horse cart cost too much. Grain (ring 3) keeps well and is lighter for its value. Ranching (ring 4) needs the most land.",
   "whyNot": {
    "A": "Ranching is the outermost ring (ring 4).",
    "B": "Grain is in ring 3, and it keeps a long time. It does not spoil in a day.",
    "C": "Market gardening is ring 1, and it uses SMALL plots, not the most land.",
    "E": "Dairying is in ring 1 because milk spoils fast."
   },
   "vocab": [
    "von Thünen model",
    "transportation cost"
   ]
  },
  {
   "id": "U5-P24",
   "topic": "5.8",
   "lo": "PSO-5.D",
   "skill": "1.E",
   "difficulty": "hard",
   "stem": "Which observation most challenges the usefulness of von Thünen's model for explaining agricultural land use today?",
   "options": {
    "A": "Dairy farms are still common on the edges of some large metropolitan areas in North America.",
    "B": "Land prices near a large city are usually much higher than land prices far from it.",
    "C": "Refrigerated ships and air freight let fresh grapes from Chile reach stores in North America and Europe.",
    "D": "Cattle ranching is still common in thinly populated areas located far from major cities.",
    "E": "Many farmers still consider transportation cost when they decide which crops to grow."
   },
   "answer": "C",
   "explanation": "Von Thünen's model depends on transportation cost rising steeply with distance, so perishable foods must be grown close to the market. Refrigeration and fast, cheap shipping break that rule: fresh grapes can travel thousands of miles from Chile and still beat local fruit in winter. The CED notes that specialty farming regions do not always fit the rings.",
   "whyNot": {
    "A": "Dairying near cities fits the model.",
    "B": "Higher land prices near the market match bid-rent and the model.",
    "D": "Ranching far from cities fits the outer ring of the model.",
    "E": "That supports the model's main idea, transportation cost."
   },
   "vocab": [
    "von Thünen model",
    "time-space compression",
    "specialty agriculture"
   ]
  },
  {
   "id": "U5-P25",
   "topic": "5.9",
   "lo": "PSO-5.E",
   "skill": "1.B",
   "difficulty": "easy",
   "stem": "Countries whose export earnings depend heavily on one agricultural commodity, such as coffee or cocoa, are especially vulnerable to",
   "options": {
    "A": "falling birth rates",
    "B": "declining tourism and hotel construction in their largest cities",
    "C": "the loss of their official language",
    "D": "sharp drops in the world price of that commodity",
    "E": "an increase in the number of manufacturing jobs"
   },
   "answer": "D",
   "explanation": "If most of a country's money from exports comes from one crop, its whole economy rides on that crop's price. When world cocoa or coffee prices fall, the country earns much less, and farmers, workers, and the government all have less money. The CED says some countries have become highly dependent on one or more export commodities.",
   "whyNot": {
    "A": "Birth rates are not tied to dependence on one crop export.",
    "B": "Tourism is a separate part of the economy.",
    "C": "Language has nothing to do with commodity dependence.",
    "E": "More manufacturing jobs would REDUCE dependence on one crop, not threaten the country."
   },
   "vocab": [
    "commodity dependence",
    "export commodity",
    "global supply chain"
   ]
  },
  {
   "id": "U5-P26",
   "topic": "5.9",
   "lo": "PSO-5.E",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "TRADE PROFILE OF FIVE COUNTRIES (HYPOTHETICAL DATA)",
    "columns": [
     "Country",
     "Top export",
     "Top export's share of export earnings (%)",
     "Share of food supply that is imported (%)"
    ],
    "rows": [
     [
      "Country A",
      "Machinery",
      "18",
      "15"
     ],
     [
      "Country B",
      "Cocoa",
      "45",
      "20"
     ],
     [
      "Country C",
      "Natural gas",
      "60",
      "85"
     ],
     [
      "Country D",
      "Wheat",
      "25",
      "5"
     ],
     [
      "Country E",
      "Electronics",
      "30",
      "40"
     ]
    ],
    "source": "Hypothetical data"
   },
   "stem": "Based on the table, which country's food supply would be most threatened by a sharp rise in world grain prices?",
   "options": {
    "A": "Country A",
    "B": "Country B",
    "C": "Country C",
    "D": "Country D",
    "E": "Country E"
   },
   "answer": "C",
   "explanation": "Look at the last column: how much of each country's food comes from other countries. Country C imports 85% of its food, so when world grain prices jump, it has to pay much more to feed its people. Country D exports wheat and imports only 5% of its food, so it might even gain from higher grain prices. This shows how food links countries together in a global system.",
   "whyNot": {
    "A": "Country A imports only 15% of its food.",
    "B": "Country B depends on cocoa EXPORTS, which is a different risk. It imports only 20% of its food.",
    "D": "Country D is a wheat exporter that imports just 5% of its food.",
    "E": "Country E imports 40% of its food. That is a real risk, but less than Country C's 85%."
   },
   "vocab": [
    "food security",
    "global supply chain",
    "interdependence"
   ]
  },
  {
   "id": "U5-P27",
   "topic": "5.9",
   "lo": "PSO-5.E",
   "skill": "5.D",
   "difficulty": "hard",
   "stem": "In 2022, the war in Ukraine blocked grain shipments from Black Sea ports, and bread and flour prices rose in wheat-importing countries such as Egypt and Lebanon. This example best illustrates which concept?",
   "options": {
    "A": "Global food distribution networks are affected by political relationships and trade routes.",
    "B": "Von Thünen's model predicts where wheat farming will be located within a single country such as Egypt.",
    "C": "The Green Revolution ended wheat imports in North Africa and Southwest Asia.",
    "D": "Subsistence farmers are the main suppliers of wheat to global markets.",
    "E": "Food prices are set only by local weather in the country where food is eaten."
   },
   "answer": "A",
   "explanation": "Egypt and Lebanon buy a lot of wheat from abroad, much of it from Ukraine and Russia. When war blocked the ships leaving Black Sea ports, those countries could not get the grain as easily, so prices rose. A conflict in one place hurt food prices in another. The CED says global food distribution is shaped by political relationships, infrastructure, and patterns of world trade.",
   "whyNot": {
    "B": "Von Thünen explains land use around one market, not a war disrupting global trade.",
    "C": "These countries still import large amounts of wheat. That is why prices rose.",
    "D": "Most wheat on world markets comes from large commercial farms, not subsistence farmers.",
    "E": "Prices rose because of a war in another country, not local weather."
   },
   "vocab": [
    "global supply chain",
    "food security",
    "interdependence"
   ]
  },
  {
   "id": "U5-P28",
   "topic": "5.10",
   "lo": "IMP-5.A",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following best describes soil salinization?",
   "options": {
    "A": "The washing away of topsoil by heavy rain or wind on bare, unplanted fields",
    "B": "The planting of a different crop in a field each year to restore soil nutrients",
    "C": "The clearing of forest land for farming by cutting and then burning the vegetation",
    "D": "The spread of desert-like conditions into dry grasslands after vegetation is lost",
    "E": "The buildup of salts in soil, often from irrigation in dry climates where water evaporates quickly"
   },
   "answer": "E",
   "explanation": "All water carries a little bit of salt. When farmers irrigate in a hot, dry place, the water evaporates and leaves the salt behind. Year after year the salt builds up until crops can't grow well. This has happened in parts of Pakistan, Iraq, Australia, and California's Central Valley.",
   "whyNot": {
    "A": "That is soil erosion.",
    "B": "That is crop rotation, a conservation practice.",
    "C": "That is slash and burn.",
    "D": "That is desertification."
   },
   "vocab": [
    "soil salinization",
    "irrigation"
   ]
  },
  {
   "id": "U5-P29",
   "topic": "5.10",
   "lo": "IMP-5.A",
   "skill": "2.E",
   "difficulty": "medium",
   "stem": "Rice terraces carved into steep hillsides in the Philippines and on the Indonesian island of Bali best illustrate which of the following?",
   "options": {
    "A": "Desertification caused by overgrazing on hillsides",
    "B": "Farmers changing the landscape to create flat fields and control water on steep slopes",
    "C": "Land left as forest because it is too steep to farm",
    "D": "The long-lot survey system dividing land along a river",
    "E": "Shifting cultivation, in which farmers move from one hillside to another every few years as the soil wears out"
   },
   "answer": "B",
   "explanation": "Rice paddies need flat, flooded fields. Farmers on steep mountains built terraces, like giant stairs, so each step holds water and soil. Terraces slow down rain running downhill, which cuts erosion. The CED lists terraces as an agricultural practice that alters the landscape.",
   "whyNot": {
    "A": "Terraces are for crops, and they fight erosion. They are not caused by overgrazing.",
    "C": "The hills ARE farmed. That is the whole point of terraces.",
    "D": "Long lots are strips along rivers in French areas, not hillside steps.",
    "E": "Terraces are permanent. Farmers use the same terraces for generations."
   },
   "vocab": [
    "terrace farming",
    "landscape modification"
   ]
  },
  {
   "id": "U5-P30",
   "topic": "5.10",
   "lo": "IMP-5.A",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "LAND COVER IN A TROPICAL FRONTIER REGION (HYPOTHETICAL DATA)",
    "columns": [
     "Year",
     "Forest (% of region)",
     "Cattle pasture (% of region)",
     "Cropland, mostly soybeans (% of region)"
    ],
    "rows": [
     [
      "1990",
      "82",
      "10",
      "2"
     ],
     [
      "2005",
      "70",
      "19",
      "6"
     ],
     [
      "2020",
      "61",
      "25",
      "11"
     ]
    ],
    "source": "Hypothetical data"
   },
   "stem": "Which conclusion is best supported by the data in the table?",
   "options": {
    "A": "Forest in the region expanded as farmland was abandoned.",
    "B": "Cropland in the region was converted back into forest.",
    "C": "Forest was cleared and replaced mainly by cattle pasture and soybean fields.",
    "D": "Cattle pasture in the region decreased by more than half.",
    "E": "Land cover in the region stayed about the same over the 30 years shown in the table."
   },
   "answer": "C",
   "explanation": "Forest fell from 82% to 61% of the region, a loss of 21 percentage points. Over the same time, pasture rose 15 points and cropland rose 9 points. So the forest was cut down and turned into ranches and soybean farms. This is land cover change, an environmental effect of agriculture listed in the CED, and it matches what has happened in parts of the Amazon.",
   "whyNot": {
    "A": "Forest SHRANK, from 82% to 61%.",
    "B": "Cropland grew, from 2% to 11%.",
    "D": "Pasture more than DOUBLED, from 10% to 25%.",
    "E": "Every row changed by many percentage points."
   },
   "vocab": [
    "deforestation",
    "land cover change"
   ]
  },
  {
   "id": "U5-P31",
   "topic": "5.11",
   "lo": "IMP-5.B",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following best describes a food desert?",
   "options": {
    "A": "An area where residents have limited access to affordable, healthy food such as fresh produce",
    "B": "A dry region where crops can be grown only with the help of large irrigation projects",
    "C": "A farming region that produces much more food than its own population can eat",
    "D": "A large commercial farm that grows only one crop each year for export",
    "E": "Land that has been damaged by overgrazing and gradually turned into desert"
   },
   "answer": "A",
   "explanation": "A food desert has nothing to do with sand. It is a neighborhood, often a low-income city area or an isolated rural area, where there is no full-service grocery store nearby, so people mostly buy food at gas stations or fast-food places. The CED lists food deserts as a challenge to feeding people.",
   "whyNot": {
    "B": "That describes a dry farming region, not a food desert.",
    "C": "That is a food surplus region.",
    "D": "That is monocropping for export.",
    "E": "That is desertification."
   },
   "vocab": [
    "food desert",
    "food insecurity"
   ]
  },
  {
   "id": "U5-P32",
   "topic": "5.11",
   "lo": "IMP-5.B",
   "skill": "1.D",
   "difficulty": "easy",
   "stem": "Families pay a nearby farm at the start of the growing season and then pick up a box of fresh produce from that farm every week. This arrangement is an example of",
   "options": {
    "A": "plantation agriculture",
    "B": "agribusiness vertical integration",
    "C": "pastoral nomadism",
    "D": "community-supported agriculture",
    "E": "the Green Revolution"
   },
   "answer": "D",
   "explanation": "In community-supported agriculture (CSA), customers buy a \"share\" of a local farm's harvest ahead of time. The farmer gets money up front, and the families get fresh, local food each week. It is part of the local-food movement listed in the CED.",
   "whyNot": {
    "A": "Plantations grow cash crops on large estates, usually for export.",
    "B": "Vertical integration is one big company controlling many steps of food production.",
    "C": "Pastoral nomadism is moving herds of animals to find pasture.",
    "E": "The Green Revolution spread high-yield seeds and chemicals in developing countries."
   },
   "vocab": [
    "community-supported agriculture (CSA)",
    "local-food movement"
   ]
  },
  {
   "id": "U5-P33",
   "topic": "5.11",
   "lo": "IMP-5.B",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "THREE COUNTIES NEAR A FAST-GROWING METROPOLITAN AREA (HYPOTHETICAL DATA)",
    "columns": [
     "County",
     "Distance from city center (miles)",
     "Farmland 2000 (acres)",
     "Farmland 2020 (acres)",
     "Population growth 2000–2020 (%)"
    ],
    "rows": [
     [
      "North County",
      "15",
      "220,000",
      "120,000",
      "+140"
     ],
     [
      "West County",
      "35",
      "310,000",
      "250,000",
      "+60"
     ],
     [
      "Far County",
      "70",
      "400,000",
      "395,000",
      "+5"
     ]
    ],
    "source": "Hypothetical data"
   },
   "stem": "The data in the table best illustrate which challenge of contemporary agriculture?",
   "options": {
    "A": "Farmland lost to suburbanization as a metropolitan area expands",
    "B": "Soil salinization caused by heavy irrigation of farmland in the counties nearest the city",
    "C": "Loss of biodiversity from genetically modified crops",
    "D": "Growth of shifting cultivation near large cities",
    "E": "Food deserts forming in remote rural counties"
   },
   "answer": "A",
   "explanation": "The county closest to the city grew the fastest (+140%) and lost the most farmland (100,000 acres, almost half). The far county barely grew and kept almost all its farms. As the city spreads, houses, roads, and shopping centers are built on farmland. The CED lists land lost to suburbanization as a challenge to feeding a growing population.",
   "whyNot": {
    "B": "The table shows nothing about irrigation or salt.",
    "C": "The table shows nothing about crop types or biodiversity.",
    "D": "Shifting cultivation is not practiced in this setting, and farmland is disappearing, not moving.",
    "E": "The table measures farmland and population, not access to grocery stores."
   },
   "vocab": [
    "suburbanization",
    "urban sprawl",
    "farmland loss"
   ]
  },
  {
   "id": "U5-P34",
   "topic": "5.12",
   "lo": "IMP-5.C",
   "skill": "2.B",
   "difficulty": "medium",
   "stem": "In many rural regions where men migrate to cities or other countries for wage work, the role of women in agriculture tends to",
   "options": {
    "A": "disappear, because farms are abandoned when men leave",
    "B": "grow, because women take on more of the farm work and decision-making",
    "C": "shift entirely to factory work in the same rural region",
    "D": "stay exactly the same, because migration by men has little effect on who does farm labor",
    "E": "become limited to large mechanized wheat farms"
   },
   "answer": "B",
   "explanation": "When men leave to earn wages somewhere else, someone still has to grow the family's food. In much of South Asia, Sub-Saharan Africa, and Central America, women pick up more of the farm work and start making more of the farm decisions. Researchers call this the \"feminization of agriculture.\" The CED says women's roles in food production vary from place to place depending on the type of production.",
   "whyNot": {
    "A": "Farms usually keep running, with women doing more of the work.",
    "C": "The farm work still needs doing, and rural regions often have few factory jobs.",
    "D": "Migration changes who does the farm work.",
    "E": "Families affected by this migration are mostly small farms, not large mechanized wheat farms."
   },
   "vocab": [
    "feminization of agriculture",
    "rural-to-urban migration"
   ]
  },
  {
   "id": "U5-P35",
   "topic": "5.12",
   "lo": "IMP-5.C",
   "skill": "3.D",
   "difficulty": "medium",
   "stimulus": {
    "type": "bar",
    "title": "WOMEN'S ROLE IN AGRICULTURE IN FOUR COUNTRIES (HYPOTHETICAL DATA)",
    "categories": [
     "Country 1",
     "Country 2",
     "Country 3",
     "Country 4"
    ],
    "series": [
     {
      "name": "Women as % of agricultural workers",
      "values": [
       48,
       42,
       30,
       25
      ]
     },
     {
      "name": "Women as % of agricultural landholders",
      "values": [
       15,
       12,
       20,
       18
      ]
     }
    ],
    "yLabel": "Percent",
    "yMax": 60,
    "source": "Hypothetical data"
   },
   "stem": "Which conclusion is best supported by the chart?",
   "options": {
    "A": "In every country, women hold a larger share of farmland than men do.",
    "B": "Country 4 has the largest share of women working in agriculture.",
    "C": "In every country, women's share of farm work is greater than their share of landholding.",
    "D": "In Country 3, women hold a larger share of farmland than they do of farm work.",
    "E": "Women make up more than half of agricultural workers in every country."
   },
   "answer": "C",
   "explanation": "Compare the two bars for each country. The first bar (share of workers) is always taller than the second (share of landholders): 48 vs. 15, 42 vs. 12, 30 vs. 20, 25 vs. 18. So women do a big part of the farm work but hold a much smaller part of the land. This gap is real in many countries, and it matters because people without land titles often can't get loans, seed, or fertilizer.",
   "whyNot": {
    "A": "Women hold 12% to 20% of landholdings. Men hold the rest, so men hold more everywhere.",
    "B": "Country 4 has the SMALLEST share (25%). Country 1 has the largest (48%).",
    "D": "In Country 3, women are 30% of workers but only 20% of landholders.",
    "E": "No country reaches 50%. The highest is 48%."
   },
   "vocab": [
    "women in agriculture",
    "land tenure"
   ]
  },
  {
   "id": "U5-P36",
   "topic": "5.12",
   "lo": "IMP-5.C",
   "skill": "2.D",
   "difficulty": "hard",
   "stem": "Which statement best explains why women's roles in food production differ between small-scale subsistence farming regions and highly mechanized commercial farming regions?",
   "options": {
    "A": "Women take no part in food production in commercial farming regions, so the comparison applies only to subsistence regions.",
    "B": "Subsistence farming uses so much heavy machinery that women's hand labor is rarely needed in the fields.",
    "C": "Women's roles in food production depend only on a region's climate, not on the type of farming practiced.",
    "D": "Subsistence farms rely on hand labor, often done by women, while mechanized farms need few workers and are more often run by men.",
    "E": "Mechanized commercial farms always employ more women than subsistence farms do, because machines need many operators."
   },
   "answer": "D",
   "explanation": "On small subsistence farms, growing food takes lots of hand work, and in many regions women do much of the planting, weeding, harvesting, and food processing for the family. On big mechanized farms, machines do most of the work, so far fewer workers are needed, and owners and operators have more often been men. Women's roles change with the TYPE of farming, which is exactly what the CED says.",
   "whyNot": {
    "A": "Women work and run farms and food businesses in commercial regions too. The roles just differ.",
    "B": "Subsistence farming uses very LITTLE machinery and lots of hand labor.",
    "C": "The CED says roles depend on the type of production, not only on climate.",
    "E": "\"Always\" is wrong, and mechanized farms employ far fewer people of any gender."
   },
   "vocab": [
    "women in agriculture",
    "subsistence agriculture",
    "commercial agriculture"
   ]
  }
 ],
 "exam": {
  "title": "Unit 5 Practice Exam: Agriculture and Rural Land-Use Patterns and Processes",
  "timeMinutes": 25,
  "questionCount": 25,
  "directions": "Each of the questions or incomplete statements below is followed by five suggested answers or completions. Select the one that is best in each case. Your score is based only on the number of questions answered correctly, so answer every question. Work quickly without losing accuracy, and come back to any question you skipped if time allows.",
  "stimulusCount": 10,
  "questions": [
   {
    "id": "U5-E01",
    "n": 1,
    "topic": "5.1",
    "lo": "PSO-5.A",
    "skill": "1.A",
    "difficulty": "easy",
    "stem": "Which of the following best describes the difference between intensive and extensive agriculture?",
    "options": {
     "A": "Intensive agriculture is always subsistence farming, whereas extensive agriculture is always commercial farming.",
     "B": "Intensive agriculture is found only in developed countries, whereas extensive agriculture is found only in developing countries.",
     "C": "Intensive agriculture grows only grains, whereas extensive agriculture raises only animals.",
     "D": "Intensive agriculture uses large inputs of labor or capital per unit of land, whereas extensive agriculture uses few inputs spread over large areas.",
     "E": "Intensive agriculture relies on rainfall, whereas extensive agriculture relies on irrigation."
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Both kinds can be subsistence or commercial. Wet-rice farming is intensive subsistence; a large market garden is intensive commercial; nomadic herding is extensive subsistence; ranching is extensive commercial.",
     "B": "Incorrect. Both are found in developed and developing countries, for example ranching in the United States and Argentina and intensive rice farming in Japan and Bangladesh.",
     "C": "Incorrect. The distinction is about inputs per unit of land, not crop versus livestock. Dairying is intensive livestock farming; shifting cultivation is extensive crop farming.",
     "D": "Correct. Intensive agriculture concentrates labor, capital, fertilizer, or machinery on relatively small areas to get high output per unit of land. Extensive agriculture uses relatively few inputs per unit of land over large areas, as in ranching, nomadic herding, and shifting cultivation.",
     "E": "Incorrect. Water source does not define the two categories; many intensive and extensive systems are rain-fed, and some of each are irrigated."
    },
    "explanation": "Intensive = lots of work and money on a small piece of land (vegetable farms, rice paddies, dairies). Extensive = little work and money spread over a huge area (ranching, nomadic herding, shifting cultivation). It is about inputs per acre, not about rich or poor countries or crops versus animals."
   },
   {
    "id": "U5-E02",
    "n": 2,
    "topic": "5.2",
    "lo": "PSO-5.B",
    "skill": "1.A",
    "difficulty": "easy",
    "stem": "A rural settlement pattern in which farm families live together in a village and walk out to fields that surround it is called a",
    "options": {
     "A": "clustered settlement",
     "B": "dispersed settlement",
     "C": "linear settlement",
     "D": "long-lot settlement",
     "E": "township-and-range settlement"
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. Clustered (nucleated) settlements group homes together in a village, with farmland around it. They are common in much of Europe, Asia, and Africa, often for defense, shared water, or community services.",
     "B": "Incorrect. In dispersed settlements, each family lives on its own farm, separated from neighbors, as in much of the U.S. Midwest.",
     "C": "Incorrect. Linear settlements string homes along a river, road, or canal.",
     "D": "Incorrect. Long lot is a survey method that usually produces a linear pattern along a river, not a central village.",
     "E": "Incorrect. Township and range is a survey method; it usually produces a dispersed pattern of isolated farmsteads."
    },
    "explanation": "Clustered = everyone's house is together in a village, and the fields are around the outside. Dispersed = every farmhouse sits alone on its own land. Linear = houses in a line along a river or road."
   },
   {
    "id": "U5-E03",
    "n": 3,
    "set": "vonthunen",
    "topic": "5.8",
    "lo": "PSO-5.D",
    "skill": "4.A",
    "difficulty": "easy",
    "stimulus": {
     "type": "rings",
     "title": "LAND USE AROUND A MARKET CITY ON AN ISOLATED, UNIFORM PLAIN",
     "center": "Market city",
     "rings": [
      {
       "label": "W"
      },
      {
       "label": "X"
      },
      {
       "label": "Y"
      },
      {
       "label": "Z"
      }
     ],
     "outer": "Wilderness",
     "description": "Four rings, labeled W, X, Y, and Z, surround a single market city. Ring W touches the city; ring Z is farthest away. The plain is flat with equal soil everywhere, there are no roads or rivers, and farmers carry their own goods to the city.",
     "source": "Based on the model in von Thünen, The Isolated State (1826)"
    },
    "stem": "According to von Thünen's model, which ring in the diagram would most likely be used for growing grain and other field crops?",
    "options": {
     "A": "Ring W",
     "B": "Ring X",
     "C": "Ring Y",
     "D": "Ring Z",
     "E": "The market city"
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. Ring W, nearest the city, is for perishable, high-value products such as vegetables and milk.",
     "B": "Incorrect. In von Thünen's original model, the second ring is forest for firewood and lumber, which were heavy and costly to haul.",
     "C": "Correct. Grain and field crops occupy the third ring. Grain keeps well and is worth enough to be hauled a moderate distance, but it needs more land than ring W uses.",
     "D": "Incorrect. Ring Z, the outermost farming ring, is for livestock ranching, which needs the most land and the cheapest land.",
     "E": "Incorrect. The city is the market, where farm products are sold, not where field crops are grown."
    },
    "explanation": "Remember the order from the city out: 1) vegetables and dairy, 2) forest, 3) grain, 4) ranching. Ring Y is the third ring, so it is grain."
   },
   {
    "id": "U5-E04",
    "n": 4,
    "set": "vonthunen",
    "topic": "5.8",
    "lo": "PSO-5.D",
    "skill": "1.B",
    "difficulty": "medium",
    "stem": "According to von Thünen's model, which of the following best explains why ring Z is used for livestock ranching?",
    "options": {
     "A": "Ranching produces the most valuable output per hectare of any land use, so ranchers can afford to pay the highest land rent.",
     "B": "Ranching needs very large areas of land, land rent is lowest far from the city, and animals can be walked to market.",
     "C": "Cattle must be kept close to the city because meat spoils within hours.",
     "D": "The soil in ring Z is poorer than the soil in the other rings.",
     "E": "Government rules in the model prohibit ranching near the city."
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. Ranching earns relatively little per hectare, which is why it is pushed to the outer ring where land rent is lowest.",
     "B": "Correct. Ranching needs a lot of land. Far from the market, land rent is low, and livestock can walk to the city instead of being hauled, which lowers transport costs over long distances.",
     "C": "Incorrect. In the model, live animals walk to market, so distance matters less for them, not more.",
     "D": "Incorrect. The model assumes the same soil everywhere on a uniform plain. Differences come from distance to market, not soil.",
     "E": "Incorrect. The model is based on economics (land rent and transport cost), not government rules."
    },
    "explanation": "Ranching takes a LOT of land and does not earn much per acre, so it goes where land is cheapest: far from the city. And cattle can walk themselves to market, so the long trip costs less than hauling heavy crops would."
   },
   {
    "id": "U5-E05",
    "n": 5,
    "set": "vonthunen",
    "topic": "5.8",
    "lo": "PSO-5.D",
    "skill": "5.B",
    "difficulty": "hard",
    "stem": "Suppose a navigable canal were built from the market city straight out through rings W, X, Y, and Z. Based on von Thünen's reasoning, which change would most likely occur?",
    "options": {
     "A": "All four rings would disappear because farmers would move into the city.",
     "B": "The rings would shrink toward the city because transport costs would rise along the canal.",
     "C": "Each ring would stretch outward along the canal because shipping goods by water lowers transport costs.",
     "D": "Ranching would move into ring W because cattle could no longer walk to the market.",
     "E": "The order of the rings would reverse, with ranching located nearest the city and vegetables grown farthest out."
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. A canal would make farming farther from the city more profitable, not end it.",
     "B": "Incorrect. Cheap water transport lowers transport costs, so the rings would extend, not shrink.",
     "C": "Correct. Von Thünen himself showed that a navigable river distorts the rings. Lower transport costs along the waterway let each land use extend farther from the city in a band along the canal, so the circles stretch into elongated shapes.",
     "D": "Incorrect. Cattle could still walk or be shipped; nothing in the change would push ranching onto the highest-rent land.",
     "E": "Incorrect. The canal lowers costs along one line; it does not change which products are most perishable or most valuable per hectare."
    },
    "explanation": "The rings exist because hauling goods costs more the farther you go. A canal makes shipping much cheaper along its route. So farmers along the canal can grow each product farther from the city, and each ring stretches out along the water like a tongue. Von Thünen showed this with a river in his own book."
   },
   {
    "id": "U5-E06",
    "n": 6,
    "topic": "5.3",
    "lo": "SPS-5.A",
    "skill": "1.A",
    "difficulty": "easy",
    "stem": "Which of the following correctly pairs an early hearth of domestication with crops first domesticated there?",
    "options": {
     "A": "Mesoamerica (Central America) — rice and soybeans",
     "B": "Southeast Asia — maize and potatoes",
     "C": "Fertile Crescent — cassava and sweet potatoes",
     "D": "Northern Europe — coffee and cacao",
     "E": "Mesoamerica (Central America) — maize, beans, and squash"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. Rice and soybeans were domesticated in East and Southeast Asia, not Mesoamerica.",
     "B": "Incorrect. Maize comes from Mesoamerica and potatoes from the Andes of South America.",
     "C": "Incorrect. The Fertile Crescent is known for wheat, barley, lentils, sheep, and goats. Cassava and sweet potatoes come from the Americas.",
     "D": "Incorrect. Northern Europe was not an early hearth. Coffee was first cultivated in the Ethiopia-Yemen region, and cacao in the Americas.",
     "E": "Correct. Mesoamerica (Central America and southern Mexico), one of the hearths named in the CED, domesticated maize, beans, and squash, often grown together as the \"three sisters.\""
    },
    "explanation": "Mesoamerica gave the world maize (corn), beans, and squash, often grown together as the \"three sisters.\" The Fertile Crescent gave wheat, barley, sheep, and goats. Southeast and East Asia gave rice."
   },
   {
    "id": "U5-E07",
    "n": 7,
    "topic": "5.3",
    "lo": "SPS-5.B",
    "skill": "2.B",
    "difficulty": "medium",
    "stem": "After the potato arrived in Europe from the Americas, it contributed to population growth in places such as Ireland and northern Europe in the 1700s and 1800s mainly because it",
    "options": {
     "A": "could be grown only on large commercial plantations",
     "B": "produced many calories per acre and grew well in cool, wet climates",
     "C": "required no labor to plant or harvest",
     "D": "was first domesticated in Ireland, so farmers already knew how to grow it",
     "E": "replaced all other foods in the European diet within a few years"
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. Potatoes were grown widely on small family plots, which is one reason they fed so many poor households.",
     "B": "Correct. As part of the Columbian Exchange, the Andean potato reached Europe, where it produced more food energy per acre than grains and thrived in cool, damp climates. More food from small plots supported population growth.",
     "C": "Incorrect. Potatoes still require planting, weeding, and digging.",
     "D": "Incorrect. Potatoes were domesticated in the Andes of South America.",
     "E": "Incorrect. Potatoes became very important, especially in Ireland, but they did not replace all other foods across Europe."
    },
    "explanation": "The potato came from the Andes Mountains in South America through the Columbian Exchange. It grows lots of food on a small patch of ground and likes cool, wet weather, which is exactly what Ireland and northern Europe have. More food meant more families could survive and grow."
   },
   {
    "id": "U5-E08",
    "n": 8,
    "topic": "5.4",
    "lo": "SPS-5.C",
    "skill": "1.D",
    "difficulty": "medium",
    "stem": "The enclosure movement in Britain during the Second Agricultural Revolution most directly resulted in",
    "options": {
     "A": "the division of large estates into many small plots that were given to landless peasant families",
     "B": "the return of large areas of farmland to forest in order to protect wildlife habitat",
     "C": "a decline in national food production as the newly enclosed farms became less efficient",
     "D": "a large increase in the number of people working as hired laborers on British farms",
     "E": "the merging of open fields and common land into larger private farms, pushing many rural people to cities"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. Enclosure did the opposite, combining small strips and common land into larger private holdings.",
     "B": "Incorrect. Enclosed land was used for more efficient crops and pasture, not returned to forest.",
     "C": "Incorrect. Consolidated farms adopted new methods such as crop rotation and selective breeding, and output rose.",
     "D": "Incorrect. Larger, more efficient farms needed fewer laborers per unit of output, and many rural families lost access to common land.",
     "E": "Correct. Enclosure fenced off open fields and common land into larger private farms. More efficient farms needed fewer workers, and families who lost access to the commons moved to growing industrial cities, supplying factory labor."
    },
    "explanation": "Enclosure means landowners fenced in the open fields and shared \"common\" land and made them into bigger private farms. Bigger farms could use new methods and needed fewer workers. Many poor rural families lost the land they had used and moved to cities, where they worked in factories."
   },
   {
    "id": "U5-E09",
    "n": 9,
    "set": "greenrev",
    "topic": "5.5",
    "lo": "SPS-5.D",
    "skill": "3.C",
    "difficulty": "medium",
    "stimulus": {
     "type": "table",
     "title": "WHEAT FARMING IN COUNTRY M, 1960–1990 (HYPOTHETICAL DATA)",
     "columns": [
      "Year",
      "Wheat yield (tonnes per hectare)",
      "Cropland that is irrigated (%)",
      "Fertilizer used (kg per hectare)",
      "Population (millions)"
     ],
     "rows": [
      [
       "1960",
       "0.8",
       "18",
       "3",
       "450"
      ],
      [
       "1975",
       "1.4",
       "25",
       "20",
       "610"
      ],
      [
       "1990",
       "2.3",
       "32",
       "70",
       "850"
      ]
     ],
     "source": "Hypothetical data"
    },
    "stem": "Which conclusion is best supported by the data in the table?",
    "options": {
     "A": "Wheat yields rose as irrigation and fertilizer use increased, consistent with the Green Revolution.",
     "B": "Wheat yields fell as the population grew, just as Thomas Malthus had predicted they would.",
     "C": "Irrigation decreased over time because the new wheat varieties needed much less water.",
     "D": "Fertilizer use stayed about the same from 1960 to 1990 while wheat yields rose.",
     "E": "Population growth stopped soon after wheat yields began to rise in the 1960s."
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. Yield nearly tripled (0.8 to 2.3 tonnes per hectare) while irrigated cropland rose from 18 to 32 percent and fertilizer use rose from 3 to 70 kg per hectare. That combination of inputs and high-yield seeds is the Green Revolution package.",
     "B": "Incorrect. Yields rose in each period; food production outpaced the Malthusian prediction.",
     "C": "Incorrect. The irrigated share rose in each period.",
     "D": "Incorrect. Fertilizer use rose more than twentyfold.",
     "E": "Incorrect. Population kept growing, from 450 to 850 million."
    },
    "explanation": "Every column goes up. Yields almost tripled, more land was irrigated, and fertilizer use jumped from 3 to 70 kilograms per hectare. High-yield seeds plus water plus fertilizer is the Green Revolution recipe."
   },
   {
    "id": "U5-E10",
    "n": 10,
    "set": "greenrev",
    "topic": "5.5",
    "lo": "SPS-5.D",
    "skill": "2.D",
    "difficulty": "hard",
    "stem": "Which of the following is a likely negative consequence of the changes shown in the table?",
    "options": {
     "A": "Lower wheat yields caused by the loss of irrigation",
     "B": "A shortage of fertilizer that forced farmers back to subsistence farming",
     "C": "Falling groundwater levels and water pollution from fertilizer runoff",
     "D": "Rapid growth of forests on abandoned wheat fields",
     "E": "An end to wheat exports because farmers grew only vegetables"
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. The table shows irrigation expanding and yields rising.",
     "B": "Incorrect. Fertilizer use rose sharply; nothing suggests a shortage.",
     "C": "Correct. Expanding irrigation often means heavy pumping of groundwater, lowering water tables, and much heavier fertilizer use can wash into rivers and wells. These environmental costs accompanied the Green Revolution in places such as Punjab.",
     "D": "Incorrect. Fields were farmed more intensively, not abandoned.",
     "E": "Incorrect. The table shows rising wheat yields, not a switch to vegetables."
    },
    "explanation": "More irrigation means pumping more water out of the ground, so water tables fall. Way more fertilizer means some of it washes into rivers and wells and pollutes them. Bigger harvests came with environmental costs."
   },
   {
    "id": "U5-E11",
    "n": 11,
    "topic": "5.4",
    "lo": "SPS-5.C",
    "skill": "2.D",
    "difficulty": "medium",
    "stem": "The Second Agricultural Revolution was closely linked to the Industrial Revolution because",
    "options": {
     "A": "factories replaced farms as the main source of the food eaten in growing industrial cities",
     "B": "efficient farms freed workers for factories, while factory-made tools such as steel plows raised farm output",
     "C": "governments banned the use of machinery on farms in order to protect new factory jobs in cities",
     "D": "industrial cities grew most of their own food on rooftops, so rural farms were no longer needed",
     "E": "the Industrial Revolution began in rural farming areas and only later spread into cities"
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. Food still came from farms; factories processed some of it later.",
     "B": "Correct. The two revolutions reinforced each other. Productive farms needed fewer workers and fed growing cities, supplying labor and food for industry, while industrial products such as steel plows, reapers, and later tractors and fertilizer made farms more productive still.",
     "C": "Incorrect. Farms adopted more machinery, not less.",
     "D": "Incorrect. Cities depended on farms in the countryside for food.",
     "E": "Incorrect. Industrialization was centered in growing cities and mill towns, drawing workers away from rural areas."
    },
    "explanation": "The two revolutions helped each other. Better farming meant fewer farmers could feed everyone, so extra people could work in factories. And factories built new farm tools like steel plows and reapers, which made farms even more productive."
   },
   {
    "id": "U5-E12",
    "n": 12,
    "topic": "5.6",
    "lo": "PSO-5.C",
    "skill": "1.D",
    "difficulty": "medium",
    "stem": "Large estates in tropical regions that grow a single cash crop, such as bananas, sugarcane, or palm oil, mainly for export to distant markets are an example of",
    "options": {
     "A": "shifting cultivation",
     "B": "pastoral nomadism",
     "C": "subsistence agriculture",
     "D": "plantation agriculture",
     "E": "market gardening"
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Shifting cultivation clears small forest plots for a few years of food crops, then moves on; it is mostly subsistence.",
     "B": "Incorrect. Pastoral nomadism is moving herds to find pasture.",
     "C": "Incorrect. Subsistence agriculture grows food mainly for the farm family's own use, not for export.",
     "D": "Correct. Plantations are large commercial estates, often in tropical regions, that specialize in one export crop (monoculture). Many began with colonial investment, and the CED classifies plantation agriculture as intensive.",
     "E": "Incorrect. Market gardening grows a variety of fruits and vegetables for nearby city markets."
    },
    "explanation": "A plantation is a big farm in a warm, tropical place that grows one crop to sell to faraway countries: bananas, sugarcane, coffee, or palm oil. It is commercial (for sale), monoculture (one crop), and intensive (lots of workers and money)."
   },
   {
    "id": "U5-E13",
    "n": 13,
    "topic": "5.6",
    "lo": "PSO-5.C",
    "skill": "2.E",
    "difficulty": "hard",
    "stem": "Dairy farms historically surrounded large cities such as New York and Chicago in zones known as \"milksheds.\" Bid-rent theory best explains this pattern because",
    "options": {
     "A": "dairy cattle need much more grazing land per animal than beef cattle raised on open ranges",
     "B": "milk keeps fresh for months, so it can be shipped very long distances at very low cost",
     "C": "land near large cities was usually much cheaper than land in remote rural areas",
     "D": "city governments required all milk sold in the city to be produced inside city limits",
     "E": "fresh milk spoiled quickly and was costly to ship, so dairying near the market could outbid other land uses"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. Dairying is usually more intensive than ranching, using less land per unit of output.",
     "B": "Incorrect. Fresh milk spoils quickly, which is why it was produced near consumers before modern refrigeration.",
     "C": "Incorrect. Bid-rent theory predicts land is more expensive closer to the market.",
     "D": "Incorrect. The pattern reflects land rent and transport costs, not a law requiring production inside the city.",
     "E": "Correct. Because fresh milk was perishable and expensive to ship, producers close to the city could earn more per acre, so dairying outbid less intensive uses for the high-rent land near the market."
    },
    "explanation": "Fresh milk goes bad fast, and moving it far used to be hard and expensive. So dairy farmers near the city could make more money per acre than, say, grain farmers. That let them pay the high price of land close to the city. That is bid-rent: whoever earns the most from being close wins the close land."
   },
   {
    "id": "U5-E14",
    "n": 14,
    "set": "exports",
    "topic": "5.9",
    "lo": "PSO-5.E",
    "skill": "3.C",
    "difficulty": "medium",
    "stimulus": {
     "type": "table",
     "title": "EXPORT EARNINGS OF FIVE COUNTRIES (HYPOTHETICAL DATA)",
     "columns": [
      "Country",
      "Largest export",
      "Share of export earnings from largest export (%)",
      "Second-largest export",
      "Share from second-largest export (%)"
     ],
     "rows": [
      [
       "Country P",
       "Coffee",
       "62",
       "Bananas",
       "9"
      ],
      [
       "Country Q",
       "Automobiles",
       "14",
       "Coffee",
       "3"
      ],
      [
       "Country R",
       "Copper",
       "48",
       "Coffee",
       "11"
      ],
      [
       "Country S",
       "Coffee",
       "21",
       "Textiles",
       "19"
      ],
      [
       "Country T",
       "Software services",
       "25",
       "Coffee",
       "6"
      ]
     ],
     "source": "Hypothetical data"
    },
    "stem": "Based on the table, which country's export earnings would be most harmed by a 40 percent drop in the world price of coffee?",
    "options": {
     "A": "Country Q",
     "B": "Country R",
     "C": "Country T",
     "D": "Country S",
     "E": "Country P"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. Coffee is only 3 percent of Country Q's export earnings.",
     "B": "Incorrect. Coffee is 11 percent of Country R's earnings; its larger exposure is to copper prices.",
     "C": "Incorrect. Coffee is only 6 percent of Country T's export earnings.",
     "D": "Incorrect. Coffee is Country S's largest export, but at 21 percent its earnings are more diversified than Country P's.",
     "E": "Correct. Coffee provides 62 percent of Country P's export earnings, so a large fall in coffee prices would cut its total export income far more than any other country's."
    },
    "explanation": "Find the country that gets the biggest share of its export money from coffee. Country P gets 62% from coffee, way more than anyone else, so a coffee price crash would hurt it the most."
   },
   {
    "id": "U5-E15",
    "n": 15,
    "set": "exports",
    "topic": "5.9",
    "lo": "PSO-5.E",
    "skill": "5.D",
    "difficulty": "hard",
    "stem": "The table best illustrates which aspect of the global system of agriculture?",
    "options": {
     "A": "Most countries grow all of their own food and have no need to export agricultural goods.",
     "B": "Some countries depend heavily on a few export commodities, tying their economies to world prices.",
     "C": "Commodity prices are set by each producing country's government and do not change.",
     "D": "Coffee is grown mainly in countries with cold winters and sold mostly to tropical countries.",
     "E": "Countries with diversified exports are more affected by changes in a single crop's price."
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. Every country in the table earns money from exports.",
     "B": "Correct. Countries P and R earn about half or more of their export income from a single primary commodity, so global market prices, shaped by consumers and traders in other countries, drive their national income. The CED notes that some countries are highly dependent on one or more export commodities.",
     "C": "Incorrect. Commodity prices are set on world markets and can change sharply.",
     "D": "Incorrect. Coffee is a tropical crop, and the largest consumer markets include the United States and Europe.",
     "E": "Incorrect. Diversified economies, such as Country Q's, are less affected by a single crop's price."
    },
    "explanation": "Some countries make most of their export money from one product, like coffee or copper. The price is set by buyers and traders all over the world, so a price drop somewhere else can hurt that whole country's economy. That is what it means to be part of a global system."
   },
   {
    "id": "U5-E16",
    "n": 16,
    "set": "timeuse",
    "topic": "5.12",
    "lo": "IMP-5.C",
    "skill": "3.D",
    "difficulty": "medium",
    "stimulus": {
     "type": "bar",
     "title": "AVERAGE HOURS PER WEEK SPENT ON FOOD-RELATED WORK, BY SEX, IN A RURAL REGION (HYPOTHETICAL DATA)",
     "categories": [
      "Growing food crops for the household",
      "Growing cash crops for sale",
      "Processing and preparing food",
      "Selling at local markets"
     ],
     "series": [
      {
       "name": "Women (hours per week)",
       "values": [
        18,
        6,
        14,
        6
       ]
      },
      {
       "name": "Men (hours per week)",
       "values": [
        9,
        16,
        2,
        3
       ]
      }
     ],
     "yLabel": "Hours per week",
     "yMax": 20,
     "text": "In this region, most land titles and most bank loans for farming are held by men.",
     "source": "Hypothetical data"
    },
    "stem": "Which conclusion is best supported by the chart?",
    "options": {
     "A": "Men spend more time than women on every one of the four types of food-related work shown.",
     "B": "Women spend more hours per week than men growing cash crops that are sold for income.",
     "C": "Women and men spend about the same number of hours processing and preparing food.",
     "D": "Women spend more time on household food crops and food processing, while men spend more on cash crops.",
     "E": "Neither women nor men in the region spend any time selling food at local markets."
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Women spend more time than men in three of the four categories.",
     "B": "Incorrect. Men spend 16 hours on cash crops; women spend 6.",
     "C": "Incorrect. Women spend 14 hours processing and preparing food; men spend 2.",
     "D": "Correct. Women average 18 hours on household food crops and 14 on processing, compared with 9 and 2 for men, while men average 16 hours on cash crops compared with 6 for women.",
     "E": "Incorrect. Women spend 6 hours and men 3 hours per week selling at local markets."
    },
    "explanation": "Compare the pairs of bars. Women's bars are taller for household food crops (18 vs. 9), processing food (14 vs. 2), and selling (6 vs. 3). Men's bar is taller only for cash crops (16 vs. 6)."
   },
   {
    "id": "U5-E17",
    "n": 17,
    "set": "timeuse",
    "topic": "5.10",
    "lo": "IMP-5.A",
    "skill": "2.B",
    "difficulty": "hard",
    "stem": "Which of the following best explains the pattern shown in the chart?",
    "options": {
     "A": "Women in the region are not allowed to work outdoors.",
     "B": "Cash crops require no labor, so most of the work goes into household food crops.",
     "C": "A gendered division of labor in which men control most land and cash income while women are mainly responsible for household food",
     "D": "Food processing in the region is fully mechanized, so most of women's processing hours are spent operating and repairing machines.",
     "E": "Men in the region have left farming entirely for jobs in distant cities."
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. Women spend more hours than men on field work for household food crops.",
     "B": "Incorrect. Men spend 16 hours per week on cash crops, so they do require labor.",
     "C": "Correct. The chart and note show a common gendered division of labor: men hold most land titles and credit and focus on income-earning cash crops, while women carry most of the work of feeding the household. The CED lists the role of women in agricultural production as a societal effect of agricultural practices.",
     "D": "Incorrect. Nothing in the chart indicates mechanization, and 14 hours per week of processing suggests largely manual work.",
     "E": "Incorrect. Men still spend many hours on farm work, especially cash crops."
    },
    "explanation": "The note says men hold most of the land and loans. That helps explain why men do more of the farming for money (cash crops), while women do more of the farming and cooking that feeds the family. This kind of split is called a gendered division of labor."
   },
   {
    "id": "U5-E18",
    "n": 18,
    "set": "timeuse",
    "topic": "5.12",
    "lo": "IMP-5.C",
    "skill": "3.F",
    "difficulty": "hard",
    "stem": "Which of the following is a limitation of the chart for understanding women's role in agriculture in the region?",
    "options": {
     "A": "It shows hours worked, but not who decides what to grow or who keeps the income.",
     "B": "It compares the work of women and men who live in the same rural region.",
     "C": "It includes several different types of food-related work instead of only one.",
     "D": "It measures the time spent on each type of work in hours per week.",
     "E": "It shows the work of both women and men rather than only one group."
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. Hours worked do not show control over land, decisions, or income. Two groups can work similar hours with very different power over resources, so the chart alone cannot show who benefits from the work.",
     "B": "Incorrect. Comparing women and men in the same region is a strength of the chart, not a limitation.",
     "C": "Incorrect. Including several types of work gives a fuller picture, which is a strength.",
     "D": "Incorrect. Hours per week is a clear, appropriate unit for time use.",
     "E": "Incorrect. Showing both groups allows comparison, which is a strength."
    },
    "explanation": "The chart tells us how many HOURS each group works. It does not tell us who makes the decisions or who gets to keep the money. That missing piece matters a lot for understanding women's role in farming."
   },
   {
    "id": "U5-E19",
    "n": 19,
    "topic": "5.7",
    "lo": "PSO-5.C",
    "skill": "1.D",
    "difficulty": "medium",
    "stem": "Since the mid-1900s, the number of farms in the United States has fallen sharply while the average size of a farm has grown. Which of the following best explains this trend?",
    "options": {
     "A": "Farmers across the country shifted from commercial farming back to subsistence farming.",
     "B": "Government programs divided large farms into many small plots for new farm families.",
     "C": "Shifting cultivation became the main farming method across most of the Midwest.",
     "D": "Most of the nation's farmland was converted back into forest after about 1950.",
     "E": "Mechanization and economies of scale favored large operations, which absorbed many smaller farms."
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. U.S. agriculture became more commercial, not less.",
     "B": "Incorrect. Farms consolidated into fewer, larger units.",
     "C": "Incorrect. Shifting cultivation is not practiced in the U.S. Midwest.",
     "D": "Incorrect. Most farmland stayed in production; the change was in how many operations controlled it.",
     "E": "Correct. Expensive machinery, seed, and chemical inputs are cheaper per acre for large farms (economies of scale). Large commercial operations and agribusinesses expanded while many smaller family farms sold out. The CED says large-scale commercial operations are replacing small family farms."
    },
    "explanation": "Big farms can spread the cost of a $500,000 combine over thousands of acres, so they make more per acre. Small farms can't compete as well and often sell to bigger ones. So there are fewer farms, but each one is bigger."
   },
   {
    "id": "U5-E20",
    "n": 20,
    "topic": "5.7",
    "lo": "PSO-5.C",
    "skill": "1.D",
    "difficulty": "medium",
    "stem": "Coffee beans grown on small farms in Colombia are sold to an exporter, roasted in a plant in New Jersey, packaged, shipped to a distribution center, and sold in a café in Chicago. This sequence best illustrates",
    "options": {
     "A": "a commodity chain linking places of agricultural production and consumption",
     "B": "the von Thünen model of land use in concentric rings around a single market city",
     "C": "subsistence agriculture practiced by the coffee farmers",
     "D": "the Second Agricultural Revolution in Colombia",
     "E": "a food desert in the city of Chicago"
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. A commodity chain is the linked series of steps (growing, buying, processing, packaging, distributing, and selling) that connects a product's producers to its consumers, often across several countries. The CED says complex commodity chains link production and consumption of agricultural products.",
     "B": "Incorrect. Von Thünen's model explains land use around one local market; this example crosses countries and involves processing and distribution steps.",
     "C": "Incorrect. The coffee is grown for sale, not for the farmers' own consumption.",
     "D": "Incorrect. The example describes a modern global supply chain, not the 1700s–1800s agricultural changes in Europe.",
     "E": "Incorrect. A café selling coffee says nothing about residents' access to affordable, healthy food."
    },
    "explanation": "Follow the coffee from farm to cup: grown in Colombia, sold, roasted in New Jersey, packed, shipped, and sold in Chicago. That chain of steps connecting the farmer to the customer is a commodity chain."
   },
   {
    "id": "U5-E21",
    "n": 21,
    "topic": "5.10",
    "lo": "IMP-5.A",
    "skill": "2.E",
    "difficulty": "medium",
    "stem": "In parts of the Sahel region of Africa, which human activity has most contributed to desertification during periods of drought?",
    "options": {
     "A": "Overgrazing and cutting trees and shrubs, which leaves dry soil exposed to wind erosion",
     "B": "Building terraces on steep hillsides in order to grow flooded rice paddies",
     "C": "Converting large areas of desert into irrigated rice paddies along major rivers",
     "D": "Planting long belts of trees across the region to block the dry winds",
     "E": "Rotating crops each season in order to restore nutrients to the soil"
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. When too many animals graze, or trees and shrubs are cut for fuel and farmland, the protective plant cover is lost. During droughts, bare soil dries out and blows away, and the land becomes desert-like. Climate variability plays a large role, but these land uses make the damage worse.",
     "B": "Incorrect. Terracing is a conservation practice that reduces erosion, and the Sahel is not a hillside rice region.",
     "C": "Incorrect. Irrigated paddies are rare in the Sahel; irrigation can cause salinization, but it is not the main driver of Sahel desertification.",
     "D": "Incorrect. Tree belts, such as the Great Green Wall effort, are meant to fight desertification.",
     "E": "Incorrect. Crop rotation protects soil fertility; it does not cause desertification."
    },
    "explanation": "The Sahel is a dry strip of land just south of the Sahara. When animals eat too much of the grass, and people cut down trees and bushes, the soil has nothing to hold it. During a drought the soil dries and blows away, and the land turns more like a desert. That is desertification."
   },
   {
    "id": "U5-E22",
    "n": 22,
    "topic": "5.1",
    "lo": "PSO-5.A",
    "skill": "2.D",
    "difficulty": "medium",
    "stem": "Pastoral nomadism is most common in dry grasslands and deserts, such as parts of Central Asia, the Sahel, and the Arabian Peninsula, because",
    "options": {
     "A": "these regions have some of the most fertile soils in the world for growing grain crops",
     "B": "rainfall is too low and unreliable for most crops, so herders move animals to find water and grass",
     "C": "governments in these regions require most rural families to raise animals instead of crops",
     "D": "these regions are close to large cities whose residents buy fresh milk every day",
     "E": "heavy rainfall throughout the year makes it impossible to keep animals in one place"
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. These regions have thin soils and little rain, which is why crop farming is difficult there.",
     "B": "Correct. Where rain is scarce and unpredictable, growing crops is risky. Herding livestock (camels, goats, sheep, cattle) and moving them with the seasons lets people use sparse grass and water spread across large areas, an extensive practice shaped by the physical environment.",
     "C": "Incorrect. The pattern reflects climate and environment, not government requirements.",
     "D": "Incorrect. Nomadic herders typically live far from large city markets.",
     "E": "Incorrect. These regions are dry; heavy year-round rain is the opposite of their climate."
    },
    "explanation": "In very dry places, crops often fail because there is not enough rain. But animals can eat the scattered grass. So herders move their animals from place to place with the seasons to find grass and water. The dry climate is the reason."
   },
   {
    "id": "U5-E23",
    "n": 23,
    "topic": "5.11",
    "lo": "IMP-5.B",
    "skill": "1.C",
    "difficulty": "medium",
    "stem": "Supporters of genetically modified (GM) crops argue that they can raise yields and resist pests. Which of the following is a concern raised by critics of GM crops?",
    "options": {
     "A": "GM crops always produce smaller harvests than traditional seeds.",
     "B": "GM crops can be grown only by subsistence farmers.",
     "C": "GM crops cannot be sold in any country.",
     "D": "Reduced crop biodiversity and farmers' dependence on seed companies that hold patents",
     "E": "GM crops require farmers to stop using all chemical fertilizers and pesticides on their fields."
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Many GM varieties raise yields or reduce crop losses; critics' concerns center elsewhere.",
     "B": "Incorrect. GM crops are planted mostly on large commercial farms, for example soybeans and maize in the Americas.",
     "C": "Incorrect. GM crops are widely traded, though some countries restrict them.",
     "D": "Correct. Critics worry that planting a few patented varieties over huge areas reduces biodiversity and that farmers must buy new seed from a few large companies each season. The CED lists debates over reduced biodiversity and fertilizer and pesticide use.",
     "E": "Incorrect. Some GM crops are bred to tolerate herbicides, and critics argue this can increase, not end, chemical use."
    },
    "explanation": "Critics say that when farmers everywhere plant the same few GM varieties, there is less variety in crops (less biodiversity). They also worry that farmers have to buy patented seeds from a few big companies every year."
   },
   {
    "id": "U5-E24",
    "n": 24,
    "topic": "5.11",
    "lo": "IMP-5.B",
    "skill": "1.A",
    "difficulty": "easy",
    "stem": "Which of the following best describes the fair trade movement in agriculture?",
    "options": {
     "A": "A trade agreement that removes all tariffs and quotas on goods traded between countries",
     "B": "A government program that pays farmers to leave some of their cropland unplanted",
     "C": "A certification system that sets minimum prices and labor and environmental standards for producers",
     "D": "A plan to replace imported food with food grown in each consumer's own backyard garden",
     "E": "A treaty that requires every country to grow its own coffee instead of importing it"
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. That describes free trade, not fair trade.",
     "B": "Incorrect. That describes some conservation or price-support programs.",
     "C": "Correct. Fair trade certification guarantees producers, such as coffee, cocoa, and banana growers, a minimum price and sets standards for working conditions and environmental practices. The CED lists fair trade among movements influencing food production and consumption.",
     "D": "Incorrect. That is closer to urban farming or the local-food movement.",
     "E": "Incorrect. Coffee grows only in suitable tropical climates; no such treaty exists."
    },
    "explanation": "Fair trade labels (like the one on some coffee and chocolate) promise that the farmers were paid at least a minimum price and that workers were treated fairly. Shoppers pay a little more so more money gets back to the growers."
   },
   {
    "id": "U5-E25",
    "n": 25,
    "topic": "5.2",
    "lo": "PSO-5.B",
    "skill": "1.D",
    "difficulty": "medium",
    "stem": "Property boundaries in parts of the original thirteen U.S. colonies were described using natural features such as streams, large trees, and stones, producing irregularly shaped parcels. This survey method is called",
    "options": {
     "A": "township and range",
     "B": "the long-lot system",
     "C": "the Public Land Survey System",
     "D": "metes and bounds",
     "E": "enclosure"
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Township and range uses a rectangular grid of squares, not natural landmarks.",
     "B": "Incorrect. Long lots are narrow strips running back from a river, used in French settlement areas.",
     "E": "Incorrect. Enclosure is the British consolidation of open fields and common land, not a surveying method.",
     "D": "Correct. Metes and bounds describes boundaries by distances and directions between landmarks such as streams, trees, and stones, producing irregular parcels. It was widely used in the colonial East and came from British practice.",
     "C": "Incorrect. The Public Land Survey System is another name for township and range."
    },
    "explanation": "Metes and bounds uses landmarks to mark property lines: \"from the big oak tree, 200 feet to the creek, then along the creek to the stone wall.\" Because nature is not in straight lines, the parcels have odd, irregular shapes. You see it in the eastern U.S."
   }
  ]
 }
}
