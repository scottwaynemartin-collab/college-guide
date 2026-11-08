# Unit 1 question bank: full export for outside review

Unit 1, Thinking Geographically. Version 2026-11-08b.
33 untimed practice questions (instant feedback: a 6th-grade-level explanation plus one "why not" line per wrong option)
and a 25-question timed exam (25 minutes, choices A–E, College Board-style rationales for every option,
10 stimulus questions in 4 sets). Students are 9th graders in AP Human Geography.
All stimulus data are hypothetical; the projection grids in U1-E03/E04 are computed from the Mercator and Gall-Peters formulas.

Everything below is the complete data file the page uses (unit1.json), followed by the sources note (SOURCES.md).

How the stimulus types render (the JSON holds all of their data):
- table: an HTML table with the given columns and rows; `text` and `note` (if any) show under the table, then the source
  line. The table's `description` is not shown on screen. No Unit 1 table uses `note` or `text`.
- bar: grouped vertical bars, one group per category, at most two series, value printed on each bar, legend above;
  `text` shows under the chart (used in U1-P25 and U1-E08). The bar `description` is not shown on screen; screen readers
  get a generated data table.
- schematicMap: an SVG drawn from `canvas` (pixel width and height) and `features` (coordinates in pixels; the
  background is water-colored wherever no land polygon covers it). Land polygons come in three fills (default beige,
  `small` cream, `power` lavender) and are labeled at `labelAt`; markers `baseN` (purple square), `baseS` (teal square),
  and `house` (house icon); `line` is a thin dark polyline (dashed if `dashed`); `shippingLane` is a thicker dashed line;
  `arrow` has an arrowhead at `to`. The legend shows under the map, then the `description` paragraph (visible on
  screen), then the source line.
  - U1-P02 (dot density): cream land fills the canvas except a narrow water-colored river running north–south at about
    x = 470–494. Twenty-two identical purple squares sit in a band just east of the river (x 510–650); four are scattered
    in the west. Legend: "Each square = 10 dairy farms"; "River".
  - U1-P03 (contour map): beige land fills the canvas. Five closed egg-shaped contour lines surround a summit at
    (300, 210). Horizontal gaps between the 120 m and 140 m lines: west 18 px, south 30 px, north 38 px, east 70 px.
    Letters J (west), K (east), L (north), M (south) sit midway between those two lines; N sits at (720, 360), outside the
    100 m line. No scale bar.
  - U1-P14 (floodplain): two lavender floodplain strips flank a water-colored river near x = 425–480; the west strip is
    wide (x ≈ 165–445), the east strip narrow (≈ 455–530). Cream "Higher ground" lies at the far west and east. Eight
    houses and the teal school square are in the west floodplain; three houses on west high ground; four houses and
    the purple hospital square on east high ground.
  - U1-E03/E04 (two grids): two cream panels labeled Map 1 and Map 2 on a water-colored background. Each panel holds a
    340-px-wide grid with 13 evenly spaced vertical meridians (every 30°) and 11 horizontal parallels (every 15°, 75° S
    to 75° N); the equator is dashed. Map 1 parallel gaps from 75° N down to the equator: 38.4, 23.6, 18.0, 15.4, 14.3 px
    (Mercator). Map 2: 10.8, 17.2, 22.4, 26.1, 28.0 px (Gall-Peters). The grids have no latitude labels; the title and
    description give the latitudes.
  - U1-E13 to E15 (commuting): beige land fills the canvas. City M is a lavender polygon at the center (400, 220). Six
    cream boxes labeled "Town A 64%", "Town B 57%", "Town C 41%", "Town D 32%", "Town E 14%", "Town F 8%" sit 14, 18,
    30, 36, 52, and 58 km from City M (6 px = 1 km; scale bar 0–10 km), each with an arrow pointing to City M. A thick
    dashed line encloses City M and Towns A–D only.
- In the exam, a set's stimulus is stored on the first question of the set and shown beside every question in the set.
  Practice questions each carry their own stimulus (no practice sets).

===== unit1.json =====
{
 "unit": 1,
 "title": "Thinking Geographically",
 "examWeighting": "8–10% of the AP Exam multiple-choice section",
 "version": "2026-11-08b",
 "calibration": "Modeled on the format of the College Board 2020 AP Human Geography Practice Exam and the Course and Exam Description (5 answer choices, set-based stimulus questions, skills 1–5). All questions, stimuli, and data are original or compiled from public facts; no College Board items are reproduced.",
 "checked": "Nov 8, 2026: automated checks in u1/assemble.py (answer balance and runs, option-length tells, absolute-word tells, field completeness, LO/skill tags, set structure) and u1/verify.py (every stimulus number, map geometry, and data-based key recomputed by script); independent Claude checker agent (blind answers 58/58, arithmetic and projection-grid geometry recomputed, E13 checked against the OMB 25% commuting standard); fixes applied in v2026-11-08b: P26 rewritten (scale asked by area studied), P23 rewritten, P03 description and stem, E03-E04 neutral source line, label-pair and hedge tells (E22, P32, E10), P05 E, P15 D, E05 key wording, E13 explanation, E19 rationale, E20 D.",
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
   "id": "1.1",
   "name": "Introduction to Maps",
   "lo": "IMP-1.A"
  },
  {
   "id": "1.2",
   "name": "Geographic Data",
   "lo": "IMP-1.B"
  },
  {
   "id": "1.3",
   "name": "The Power of Geographic Data",
   "lo": "IMP-1.C"
  },
  {
   "id": "1.4",
   "name": "Spatial Concepts",
   "lo": "PSO-1.A"
  },
  {
   "id": "1.5",
   "name": "Human–Environmental Interaction",
   "lo": "PSO-1.B"
  },
  {
   "id": "1.6",
   "name": "Scales of Analysis",
   "lo": "PSO-1.C, PSO-1.D"
  },
  {
   "id": "1.7",
   "name": "Regional Analysis",
   "lo": "SPS-1.A"
  }
 ],
 "practice": [
  {
   "id": "U1-P01",
   "topic": "1.1",
   "lo": "IMP-1.A",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following is the best example of a reference map?",
   "options": {
    "A": "A world map shading each country by its average life expectancy",
    "B": "A state highway map showing roads, cities, rivers, and county lines",
    "C": "A map using circles of different sizes to show the population of each large city",
    "D": "A map with lines connecting places that have the same average January temperature",
    "E": "A world map with each country resized in proportion to its number of people"
   },
   "answer": "B",
   "explanation": "A reference map helps you find places. It shows general features like roads, cities, rivers, and borders. A highway map is a classic reference map. Thematic maps are different: each one is made to show one topic, like life expectancy or temperature.",
   "whyNot": {
    "A": "Shading countries by life expectancy shows one topic. That is a thematic map (a choropleth map).",
    "C": "Circles sized by population show one topic. That is a thematic map (a graduated symbol map).",
    "D": "Lines joining places with the same temperature show one topic. That is a thematic map (an isoline map).",
    "E": "Resizing countries by population shows one topic. That is a thematic map (a cartogram)."
   },
   "vocab": [
    "reference map",
    "thematic map"
   ]
  },
  {
   "id": "U1-P02",
   "topic": "1.1",
   "lo": "IMP-1.A",
   "skill": "3.A",
   "difficulty": "easy",
   "stimulus": {
    "type": "schematicMap",
    "title": "DAIRY FARMS IN COUNTY R (HYPOTHETICAL)",
    "canvas": {
     "width": 800,
     "height": 400
    },
    "features": [
     {
      "kind": "land",
      "name": "County R, west of the river",
      "polygon": [
       [
        0,
        0
       ],
       [
        468,
        0
       ],
       [
        474,
        60
       ],
       [
        462,
        130
       ],
       [
        476,
        200
       ],
       [
        466,
        270
       ],
       [
        478,
        340
       ],
       [
        470,
        400
       ],
       [
        0,
        400
       ]
      ],
      "style": "small"
     },
     {
      "kind": "land",
      "name": "County R, east of the river",
      "polygon": [
       [
        484,
        0
       ],
       [
        800,
        0
       ],
       [
        800,
        400
       ],
       [
        486,
        400
       ],
       [
        494,
        340
       ],
       [
        482,
        270
       ],
       [
        492,
        200
       ],
       [
        478,
        130
       ],
       [
        490,
        60
       ]
      ],
      "style": "small"
     },
     {
      "kind": "marker",
      "name": "10 dairy farms",
      "points": [
       [
        625,
        308
       ],
       [
        629,
        253
       ],
       [
        558,
        116
       ],
       [
        557,
        70
       ],
       [
        624,
        177
       ],
       [
        647,
        377
       ],
       [
        520,
        326
       ],
       [
        550,
        341
       ],
       [
        513,
        292
       ],
       [
        526,
        52
       ],
       [
        519,
        119
       ],
       [
        571,
        329
       ],
       [
        517,
        259
       ],
       [
        593,
        247
       ],
       [
        560,
        287
       ],
       [
        585,
        277
       ],
       [
        511,
        361
       ],
       [
        531,
        152
       ],
       [
        590,
        139
       ],
       [
        537,
        227
       ],
       [
        608,
        56
       ],
       [
        630,
        214
       ],
       [
        95,
        85
       ],
       [
        250,
        300
       ],
       [
        165,
        215
       ],
       [
        335,
        120
       ]
      ],
      "symbol": "baseN"
     }
    ],
    "legend": [
     {
      "swatch": "baseN",
      "label": "Each square = 10 dairy farms"
     },
     {
      "swatch": "water",
      "label": "River"
     }
    ],
    "description": "A river runs north to south through the eastern part of County R. Every square is the same size and stands for 10 dairy farms. Twenty-two squares are packed into a band just east of the river; only four squares are scattered across the western part of the county.",
    "source": "Hypothetical data"
   },
   "stem": "The map above is best classified as which type of thematic map?",
   "options": {
    "A": "Choropleth map",
    "B": "Graduated symbol map",
    "C": "Isoline map",
    "D": "Dot density map",
    "E": "Cartogram"
   },
   "answer": "D",
   "explanation": "On a dot density map, every dot (here, a small square) stands for the same number of things. More dots in one spot means more of that thing there. Each square here is 10 dairy farms, so you can see the farms are bunched together (clustered) just east of the river.",
   "whyNot": {
    "A": "A choropleth map shades whole areas, like counties, darker or lighter. This map places symbols instead of shading areas.",
    "B": "A graduated symbol map uses bigger symbols for bigger amounts. Every square here is the same size.",
    "C": "An isoline map draws lines that connect places with equal values, like elevation. There are no lines like that here.",
    "E": "A cartogram changes the size of places to match a number, like population. The county keeps its real shape here."
   },
   "vocab": [
    "dot density map",
    "thematic map",
    "clustering"
   ]
  },
  {
   "id": "U1-P03",
   "topic": "1.1",
   "lo": "IMP-1.A",
   "skill": "3.B",
   "difficulty": "medium",
   "stimulus": {
    "type": "schematicMap",
    "title": "CONTOUR MAP OF HILL Q (HYPOTHETICAL). CONTOUR INTERVAL: 20 METERS",
    "canvas": {
     "width": 800,
     "height": 420
    },
    "features": [
     {
      "kind": "land",
      "name": "",
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
      ]
     },
     {
      "kind": "line",
      "name": "100 m contour line",
      "line": [
       [
        620.0,
        210.0
       ],
       [
        618.8,
        222.4
       ],
       [
        615.1,
        234.7
       ],
       [
        609.1,
        246.8
       ],
       [
        600.7,
        258.6
       ],
       [
        590.0,
        270.0
       ],
       [
        577.1,
        281.0
       ],
       [
        562.1,
        291.4
       ],
       [
        545.1,
        301.3
       ],
       [
        526.3,
        310.4
       ],
       [
        505.7,
        318.8
       ],
       [
        483.5,
        326.3
       ],
       [
        460.0,
        333.0
       ],
       [
        435.2,
        338.7
       ],
       [
        409.4,
        343.4
       ],
       [
        382.8,
        347.2
       ],
       [
        355.6,
        349.8
       ],
       [
        327.9,
        351.5
       ],
       [
        300.0,
        352.0
       ],
       [
        292.0,
        351.5
       ],
       [
        284.0,
        349.8
       ],
       [
        276.2,
        347.2
       ],
       [
        268.5,
        343.4
       ],
       [
        261.1,
        338.7
       ],
       [
        254.0,
        333.0
       ],
       [
        247.2,
        326.3
       ],
       [
        240.9,
        318.8
       ],
       [
        234.9,
        310.4
       ],
       [
        229.5,
        301.3
       ],
       [
        224.6,
        291.4
       ],
       [
        220.3,
        281.0
       ],
       [
        216.6,
        270.0
       ],
       [
        213.5,
        258.6
       ],
       [
        211.1,
        246.8
       ],
       [
        209.4,
        234.7
       ],
       [
        208.4,
        222.4
       ],
       [
        208.0,
        210.0
       ],
       [
        208.4,
        194.6
       ],
       [
        209.4,
        179.3
       ],
       [
        211.1,
        164.2
       ],
       [
        213.5,
        149.5
       ],
       [
        216.6,
        135.2
       ],
       [
        220.3,
        121.5
       ],
       [
        224.6,
        108.5
       ],
       [
        229.5,
        96.2
       ],
       [
        234.9,
        84.8
       ],
       [
        240.9,
        74.4
       ],
       [
        247.2,
        65.0
       ],
       [
        254.0,
        56.7
       ],
       [
        261.1,
        49.6
       ],
       [
        268.5,
        43.7
       ],
       [
        276.2,
        39.0
       ],
       [
        284.0,
        35.7
       ],
       [
        292.0,
        33.7
       ],
       [
        300.0,
        33.0
       ],
       [
        327.9,
        33.7
       ],
       [
        355.6,
        35.7
       ],
       [
        382.8,
        39.0
       ],
       [
        409.4,
        43.7
       ],
       [
        435.2,
        49.6
       ],
       [
        460.0,
        56.7
       ],
       [
        483.5,
        65.0
       ],
       [
        505.7,
        74.4
       ],
       [
        526.3,
        84.8
       ],
       [
        545.1,
        96.2
       ],
       [
        562.1,
        108.5
       ],
       [
        577.1,
        121.5
       ],
       [
        590.0,
        135.2
       ],
       [
        600.7,
        149.5
       ],
       [
        609.1,
        164.2
       ],
       [
        615.1,
        179.3
       ],
       [
        618.8,
        194.6
       ],
       [
        620.0,
        210.0
       ]
      ]
     },
     {
      "kind": "line",
      "name": "120 m contour line",
      "line": [
       [
        550.0,
        210.0
       ],
       [
        549.0,
        219.8
       ],
       [
        546.2,
        229.4
       ],
       [
        541.5,
        239.0
       ],
       [
        534.9,
        248.3
       ],
       [
        526.6,
        257.3
       ],
       [
        516.5,
        266.0
       ],
       [
        504.8,
        274.2
       ],
       [
        491.5,
        282.0
       ],
       [
        476.8,
        289.2
       ],
       [
        460.7,
        295.8
       ],
       [
        443.4,
        301.7
       ],
       [
        425.0,
        307.0
       ],
       [
        405.7,
        311.5
       ],
       [
        385.5,
        315.2
       ],
       [
        364.7,
        318.2
       ],
       [
        343.4,
        320.3
       ],
       [
        321.8,
        321.6
       ],
       [
        300.0,
        322.0
       ],
       [
        293.6,
        321.6
       ],
       [
        287.2,
        320.3
       ],
       [
        280.8,
        318.2
       ],
       [
        274.7,
        315.2
       ],
       [
        268.7,
        311.5
       ],
       [
        263.0,
        307.0
       ],
       [
        257.6,
        301.7
       ],
       [
        252.4,
        295.8
       ],
       [
        247.7,
        289.2
       ],
       [
        243.3,
        282.0
       ],
       [
        239.4,
        274.2
       ],
       [
        235.9,
        266.0
       ],
       [
        232.9,
        257.3
       ],
       [
        230.5,
        248.3
       ],
       [
        228.5,
        239.0
       ],
       [
        227.1,
        229.4
       ],
       [
        226.3,
        219.8
       ],
       [
        226.0,
        210.0
       ],
       [
        226.3,
        197.9
       ],
       [
        227.1,
        185.9
       ],
       [
        228.5,
        174.0
       ],
       [
        230.5,
        162.5
       ],
       [
        232.9,
        151.3
       ],
       [
        235.9,
        140.5
       ],
       [
        239.4,
        130.3
       ],
       [
        243.3,
        120.7
       ],
       [
        247.7,
        111.7
       ],
       [
        252.4,
        103.5
       ],
       [
        257.6,
        96.1
       ],
       [
        263.0,
        89.6
       ],
       [
        268.7,
        84.0
       ],
       [
        274.7,
        79.4
       ],
       [
        280.8,
        75.7
       ],
       [
        287.2,
        73.1
       ],
       [
        293.6,
        71.5
       ],
       [
        300.0,
        71.0
       ],
       [
        321.8,
        71.5
       ],
       [
        343.4,
        73.1
       ],
       [
        364.7,
        75.7
       ],
       [
        385.5,
        79.4
       ],
       [
        405.7,
        84.0
       ],
       [
        425.0,
        89.6
       ],
       [
        443.4,
        96.1
       ],
       [
        460.7,
        103.5
       ],
       [
        476.8,
        111.7
       ],
       [
        491.5,
        120.7
       ],
       [
        504.8,
        130.3
       ],
       [
        516.5,
        140.5
       ],
       [
        526.6,
        151.3
       ],
       [
        534.9,
        162.5
       ],
       [
        541.5,
        174.0
       ],
       [
        546.2,
        185.9
       ],
       [
        549.0,
        197.9
       ],
       [
        550.0,
        210.0
       ]
      ]
     },
     {
      "kind": "line",
      "name": "140 m contour line",
      "line": [
       [
        480.0,
        210.0
       ],
       [
        479.3,
        217.1
       ],
       [
        477.3,
        224.2
       ],
       [
        473.9,
        231.2
       ],
       [
        469.1,
        238.0
       ],
       [
        463.1,
        244.7
       ],
       [
        455.9,
        251.0
       ],
       [
        447.4,
        257.0
       ],
       [
        437.9,
        262.7
       ],
       [
        427.3,
        268.0
       ],
       [
        415.7,
        272.8
       ],
       [
        403.2,
        277.2
       ],
       [
        390.0,
        281.0
       ],
       [
        376.1,
        284.3
       ],
       [
        361.6,
        287.1
       ],
       [
        346.6,
        289.2
       ],
       [
        331.3,
        290.8
       ],
       [
        315.7,
        291.7
       ],
       [
        300.0,
        292.0
       ],
       [
        295.1,
        291.7
       ],
       [
        290.3,
        290.8
       ],
       [
        285.5,
        289.2
       ],
       [
        280.8,
        287.1
       ],
       [
        276.3,
        284.3
       ],
       [
        272.0,
        281.0
       ],
       [
        267.9,
        277.2
       ],
       [
        264.0,
        272.8
       ],
       [
        260.4,
        268.0
       ],
       [
        257.1,
        262.7
       ],
       [
        254.1,
        257.0
       ],
       [
        251.5,
        251.0
       ],
       [
        249.2,
        244.7
       ],
       [
        247.4,
        238.0
       ],
       [
        245.9,
        231.2
       ],
       [
        244.9,
        224.2
       ],
       [
        244.2,
        217.1
       ],
       [
        244.0,
        210.0
       ],
       [
        244.2,
        201.2
       ],
       [
        244.9,
        192.5
       ],
       [
        245.9,
        183.9
       ],
       [
        247.4,
        175.5
       ],
       [
        249.2,
        167.3
       ],
       [
        251.5,
        159.5
       ],
       [
        254.1,
        152.1
       ],
       [
        257.1,
        145.1
       ],
       [
        260.4,
        138.6
       ],
       [
        264.0,
        132.6
       ],
       [
        267.9,
        127.3
       ],
       [
        272.0,
        122.5
       ],
       [
        276.3,
        118.5
       ],
       [
        280.8,
        115.1
       ],
       [
        285.5,
        112.4
       ],
       [
        290.3,
        110.5
       ],
       [
        295.1,
        109.4
       ],
       [
        300.0,
        109.0
       ],
       [
        315.7,
        109.4
       ],
       [
        331.3,
        110.5
       ],
       [
        346.6,
        112.4
       ],
       [
        361.6,
        115.1
       ],
       [
        376.1,
        118.5
       ],
       [
        390.0,
        122.5
       ],
       [
        403.2,
        127.3
       ],
       [
        415.7,
        132.6
       ],
       [
        427.3,
        138.6
       ],
       [
        437.9,
        145.1
       ],
       [
        447.4,
        152.1
       ],
       [
        455.9,
        159.5
       ],
       [
        463.1,
        167.3
       ],
       [
        469.1,
        175.5
       ],
       [
        473.9,
        183.9
       ],
       [
        477.3,
        192.5
       ],
       [
        479.3,
        201.2
       ],
       [
        480.0,
        210.0
       ]
      ]
     },
     {
      "kind": "line",
      "name": "160 m contour line",
      "line": [
       [
        410.0,
        210.0
       ],
       [
        409.6,
        214.5
       ],
       [
        408.3,
        219.0
       ],
       [
        406.3,
        223.5
       ],
       [
        403.4,
        227.8
       ],
       [
        399.7,
        232.0
       ],
       [
        395.3,
        236.0
       ],
       [
        390.1,
        239.8
       ],
       [
        384.3,
        243.4
       ],
       [
        377.8,
        246.8
       ],
       [
        370.7,
        249.8
       ],
       [
        363.1,
        252.6
       ],
       [
        355.0,
        255.0
       ],
       [
        346.5,
        257.1
       ],
       [
        337.6,
        258.9
       ],
       [
        328.5,
        260.2
       ],
       [
        319.1,
        261.2
       ],
       [
        309.6,
        261.8
       ],
       [
        300.0,
        262.0
       ],
       [
        296.7,
        261.8
       ],
       [
        293.4,
        261.2
       ],
       [
        290.2,
        260.2
       ],
       [
        287.0,
        258.9
       ],
       [
        283.9,
        257.1
       ],
       [
        281.0,
        255.0
       ],
       [
        278.2,
        252.6
       ],
       [
        275.6,
        249.8
       ],
       [
        273.1,
        246.8
       ],
       [
        270.9,
        243.4
       ],
       [
        268.9,
        239.8
       ],
       [
        267.1,
        236.0
       ],
       [
        265.6,
        232.0
       ],
       [
        264.3,
        227.8
       ],
       [
        263.3,
        223.5
       ],
       [
        262.6,
        219.0
       ],
       [
        262.1,
        214.5
       ],
       [
        262.0,
        210.0
       ],
       [
        262.1,
        204.5
       ],
       [
        262.6,
        199.1
       ],
       [
        263.3,
        193.7
       ],
       [
        264.3,
        188.5
       ],
       [
        265.6,
        183.4
       ],
       [
        267.1,
        178.5
       ],
       [
        268.9,
        173.9
       ],
       [
        270.9,
        169.5
       ],
       [
        273.1,
        165.5
       ],
       [
        275.6,
        161.7
       ],
       [
        278.2,
        158.4
       ],
       [
        281.0,
        155.4
       ],
       [
        283.9,
        152.9
       ],
       [
        287.0,
        150.8
       ],
       [
        290.2,
        149.1
       ],
       [
        293.4,
        148.0
       ],
       [
        296.7,
        147.2
       ],
       [
        300.0,
        147.0
       ],
       [
        309.6,
        147.2
       ],
       [
        319.1,
        148.0
       ],
       [
        328.5,
        149.1
       ],
       [
        337.6,
        150.8
       ],
       [
        346.5,
        152.9
       ],
       [
        355.0,
        155.4
       ],
       [
        363.1,
        158.4
       ],
       [
        370.7,
        161.7
       ],
       [
        377.8,
        165.5
       ],
       [
        384.3,
        169.5
       ],
       [
        390.1,
        173.9
       ],
       [
        395.3,
        178.5
       ],
       [
        399.7,
        183.4
       ],
       [
        403.4,
        188.5
       ],
       [
        406.3,
        193.7
       ],
       [
        408.3,
        199.1
       ],
       [
        409.6,
        204.5
       ],
       [
        410.0,
        210.0
       ]
      ]
     },
     {
      "kind": "line",
      "name": "180 m contour line",
      "line": [
       [
        340.0,
        210.0
       ],
       [
        339.8,
        211.9
       ],
       [
        339.4,
        213.8
       ],
       [
        338.6,
        215.7
       ],
       [
        337.6,
        217.5
       ],
       [
        336.3,
        219.3
       ],
       [
        334.6,
        221.0
       ],
       [
        332.8,
        222.6
       ],
       [
        330.6,
        224.1
       ],
       [
        328.3,
        225.6
       ],
       [
        325.7,
        226.9
       ],
       [
        322.9,
        228.0
       ],
       [
        320.0,
        229.1
       ],
       [
        316.9,
        229.9
       ],
       [
        313.7,
        230.7
       ],
       [
        310.4,
        231.3
       ],
       [
        306.9,
        231.7
       ],
       [
        303.5,
        231.9
       ],
       [
        300.0,
        232.0
       ],
       [
        298.3,
        231.9
       ],
       [
        296.5,
        231.7
       ],
       [
        294.8,
        231.3
       ],
       [
        293.2,
        230.7
       ],
       [
        291.5,
        229.9
       ],
       [
        290.0,
        229.1
       ],
       [
        288.5,
        228.0
       ],
       [
        287.1,
        226.9
       ],
       [
        285.9,
        225.6
       ],
       [
        284.7,
        224.1
       ],
       [
        283.6,
        222.6
       ],
       [
        282.7,
        221.0
       ],
       [
        281.9,
        219.3
       ],
       [
        281.2,
        217.5
       ],
       [
        280.7,
        215.7
       ],
       [
        280.3,
        213.8
       ],
       [
        280.1,
        211.9
       ],
       [
        280.0,
        210.0
       ],
       [
        280.1,
        207.8
       ],
       [
        280.3,
        205.7
       ],
       [
        280.7,
        203.5
       ],
       [
        281.2,
        201.4
       ],
       [
        281.9,
        199.4
       ],
       [
        282.7,
        197.5
       ],
       [
        283.6,
        195.7
       ],
       [
        284.7,
        193.9
       ],
       [
        285.9,
        192.3
       ],
       [
        287.1,
        190.8
       ],
       [
        288.5,
        189.5
       ],
       [
        290.0,
        188.3
       ],
       [
        291.5,
        187.3
       ],
       [
        293.2,
        186.5
       ],
       [
        294.8,
        185.9
       ],
       [
        296.5,
        185.4
       ],
       [
        298.3,
        185.1
       ],
       [
        300.0,
        185.0
       ],
       [
        303.5,
        185.1
       ],
       [
        306.9,
        185.4
       ],
       [
        310.4,
        185.9
       ],
       [
        313.7,
        186.5
       ],
       [
        316.9,
        187.3
       ],
       [
        320.0,
        188.3
       ],
       [
        322.9,
        189.5
       ],
       [
        325.7,
        190.8
       ],
       [
        328.3,
        192.3
       ],
       [
        330.6,
        193.9
       ],
       [
        332.8,
        195.7
       ],
       [
        334.6,
        197.5
       ],
       [
        336.3,
        199.4
       ],
       [
        337.6,
        201.4
       ],
       [
        338.6,
        203.5
       ],
       [
        339.4,
        205.7
       ],
       [
        339.8,
        207.8
       ],
       [
        340.0,
        210.0
       ]
      ]
     },
     {
      "kind": "land",
      "name": "J",
      "polygon": [
       [
        235.0,
        210
       ],
       [
        235.0,
        210
       ],
       [
        235.0,
        210
       ]
      ],
      "labelAt": [
       235.0,
       209
      ]
     },
     {
      "kind": "land",
      "name": "K",
      "polygon": [
       [
        515.0,
        210
       ],
       [
        515.0,
        210
       ],
       [
        515.0,
        210
       ]
      ],
      "labelAt": [
       515.0,
       209
      ]
     },
     {
      "kind": "land",
      "name": "L",
      "polygon": [
       [
        300,
        90.0
       ],
       [
        300,
        90.0
       ],
       [
        300,
        90.0
       ]
      ],
      "labelAt": [
       300,
       89.0
      ]
     },
     {
      "kind": "land",
      "name": "M",
      "polygon": [
       [
        300,
        307.0
       ],
       [
        300,
        307.0
       ],
       [
        300,
        307.0
       ]
      ],
      "labelAt": [
       300,
       306.0
      ]
     },
     {
      "kind": "land",
      "name": "N",
      "polygon": [
       [
        720,
        360
       ],
       [
        720,
        360
       ],
       [
        720,
        360
       ]
      ],
      "labelAt": [
       720,
       359
      ]
     }
    ],
    "description": "Five closed contour lines circle the top of Hill Q, from 100 meters (outer line) to 180 meters (inner line). Point J is on the west side of the hill, Point K on the east side, Point L on the north side, and Point M on the south side; each sits between the 120-meter and 140-meter lines. Point N is outside the 100-meter line. Near Point J the lines are tightly packed; near Point K they are widely spaced; near Point L they are moderately spaced; near Point M they are fairly close together.",
    "source": "Hypothetical map"
   },
   "stem": "Based on the map, at which labeled point is the land steepest?",
   "options": {
    "A": "Point J",
    "B": "Point K",
    "C": "Point L",
    "D": "Point M",
    "E": "Point N"
   },
   "answer": "A",
   "explanation": "Contour lines are isolines: each line connects places at the same height. When the lines are packed close together, the land climbs a lot in a short distance, so it is steep. At Point J the lines are closest together.",
   "whyNot": {
    "B": "At Point K the lines are far apart, so the land rises slowly. That is a gentle slope.",
    "C": "Point L's lines are closer than at K but farther apart than at J, so it is less steep than J.",
    "D": "Point M's lines are fairly close, but they are not packed as tightly as at J.",
    "E": "Point N is past the lowest contour line, with no lines nearby. The land there is nearly flat."
   },
   "vocab": [
    "isoline",
    "contour line",
    "elevation"
   ]
  },
  {
   "id": "U1-P04",
   "topic": "1.1",
   "lo": "IMP-1.A",
   "skill": "1.B",
   "difficulty": "medium",
   "stem": "On a Mercator projection, Greenland looks about as large as Africa, even though Africa is about 14 times larger. Which of the following best explains this distortion?",
   "options": {
    "A": "The Mercator projection keeps areas accurate, so its distortion is in the shapes of landmasses near the equator.",
    "B": "Greenland's thick ice sheet makes the island look much larger on maps than its land area really is.",
    "C": "The Mercator projection keeps local shapes and directions true but stretches area toward the poles.",
    "D": "The Mercator projection is centered on the North Pole, so places close to the pole are drawn larger.",
    "E": "The Mercator projection keeps true distances from the equator, so places far from it look bigger."
   },
   "answer": "C",
   "explanation": "Mercator made his map in 1569 for sailors. It keeps compass directions and the shapes of small areas correct. To do that, it stretches the map more and more as you move toward the North and South Poles. Greenland is far north, so it gets blown up a lot. Africa sits on the equator, where there is little stretching.",
   "whyNot": {
    "A": "That describes an equal-area map like Gall-Peters. Mercator does the opposite: it keeps local shapes but distorts area.",
    "B": "The problem is the map projection, not the ice. Greenland looks huge on Mercator maps that show only outlines.",
    "D": "A map centered on the North Pole is an azimuthal (polar) map. Mercator is a rectangular map centered on the equator.",
    "E": "Mercator does not keep true distances. Its scale grows toward the poles, which is why far-north places look too big."
   },
   "vocab": [
    "Mercator projection",
    "map projection",
    "distortion"
   ]
  },
  {
   "id": "U1-P05",
   "topic": "1.1",
   "lo": "IMP-1.A",
   "skill": "1.E",
   "difficulty": "hard",
   "stem": "An airline planner wants one map that shows the correct distance and direction from the airline's hub airport to cities around the world. Which map projection would serve this purpose best?",
   "options": {
    "A": "A Mercator projection, which keeps compass bearings constant along straight lines",
    "B": "A Gall-Peters projection, which shows the true relative sizes of the continents",
    "C": "A Robinson projection, which keeps overall distortion low across the map",
    "D": "A Goode's homolosine projection, which interrupts the oceans to reduce distortion of land",
    "E": "An azimuthal equidistant projection, which is drawn outward from a single center point"
   },
   "answer": "E",
   "explanation": "An azimuthal equidistant map is drawn around one center point. A straight line from that center shows the true distance and the true direction to any other place. If the planner puts the hub airport at the center, the planner can measure the route to any city. Distances between two places that are NOT the center are distorted, but the planner only needs routes from the hub.",
   "whyNot": {
    "A": "Mercator keeps compass bearings, which helps sailors, but its distances are badly stretched toward the poles.",
    "B": "Gall-Peters keeps area true, but it distorts distances and shapes, so it cannot measure routes from the hub.",
    "C": "Robinson is a compromise map. It distorts a little of everything, so neither distance nor direction from the hub is exactly right.",
    "D": "Goode's map keeps area true, but cutting the oceans breaks up the very routes the planner needs to measure."
   },
   "vocab": [
    "azimuthal equidistant projection",
    "Mercator projection",
    "Gall-Peters projection",
    "Robinson projection"
   ]
  },
  {
   "id": "U1-P06",
   "topic": "1.1",
   "lo": "IMP-1.A",
   "skill": "3.D",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "NEW BUSINESSES OPENED IN FIVE COUNTIES OF STATE Q, 2025 (HYPOTHETICAL DATA)",
    "columns": [
     "County",
     "Population",
     "New businesses opened"
    ],
    "rows": [
     [
      "Adams",
      "820,000",
      "2,870"
     ],
     [
      "Baker",
      "60,000",
      "480"
     ],
     [
      "Cole",
      "150,000",
      "900"
     ],
     [
      "Dunn",
      "300,000",
      "1,350"
     ],
     [
      "Ellis",
      "45,000",
      "135"
     ]
    ],
    "description": "A table listing the population and the number of new businesses opened in 2025 for five counties: Adams, Baker, Cole, Dunn, and Ellis.",
    "source": "Hypothetical data"
   },
   "stem": "A student wants to make a choropleth map showing where opening a new business was most common relative to the number of residents. Based on the table, which county should be shaded darkest?",
   "options": {
    "A": "Adams County",
    "B": "Baker County",
    "C": "Cole County",
    "D": "Dunn County",
    "E": "Ellis County"
   },
   "answer": "B",
   "explanation": "A choropleth map should shade areas by a rate, not a total. Divide new businesses by population. Baker had 480 new businesses for 60,000 people. That is 8.0 per 1,000 residents, the highest rate. Adams had the most businesses only because it has the most people.",
   "whyNot": {
    "A": "Adams has the biggest total (2,870), but it has 820,000 people. That is only 3.5 per 1,000 residents.",
    "C": "Cole's rate is 6.0 per 1,000 residents. That is second highest, but below Baker's 8.0.",
    "D": "Dunn's rate is 4.5 per 1,000 residents, lower than Baker's.",
    "E": "Ellis is the smallest county, but its rate is only 3.0 per 1,000 residents, the lowest of the five."
   },
   "vocab": [
    "choropleth map",
    "rate",
    "per capita"
   ]
  },
  {
   "id": "U1-P07",
   "topic": "1.1",
   "lo": "IMP-1.A",
   "skill": "3.A",
   "difficulty": "easy",
   "stem": "On a certain world map, India appears much larger than Canada, even though Canada has about three times as much area. The map draws each country's size in proportion to its population. This type of map is called a",
   "options": {
    "A": "cartogram",
    "B": "choropleth map",
    "C": "reference map",
    "D": "dot density map",
    "E": "Mercator projection"
   },
   "answer": "A",
   "explanation": "A cartogram changes the size of each place to match a number, like population, instead of land area. India has far more people than Canada, so India is drawn much bigger. Cartograms give up true shape and area to make one number easy to see.",
   "whyNot": {
    "B": "A choropleth map keeps true country sizes and shades them with colors.",
    "C": "A reference map shows real locations and features like borders and cities. It does not resize countries by population.",
    "D": "A dot density map keeps true sizes and places dots inside each country.",
    "E": "Mercator stretches places near the poles. That would make Canada look bigger, not smaller."
   },
   "vocab": [
    "cartogram",
    "thematic map"
   ]
  },
  {
   "id": "U1-P08",
   "topic": "1.2",
   "lo": "IMP-1.B",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "A city planner uses a computer program to stack map layers showing roads, flood zones, school locations, and population density, and then analyzes how the layers relate to one another. This tool is best described as",
   "options": {
    "A": "remote sensing from satellites",
    "B": "a satellite navigation system such as GPS",
    "C": "a national census of population",
    "D": "a geographic information system",
    "E": "an aerial photograph of the city"
   },
   "answer": "D",
   "explanation": "A geographic information system (GIS) is computer software that stores map data in layers. The planner can stack layers, like roads on top of flood zones, to see how they relate. GIS is the tool for analyzing. GPS and remote sensing are ways of collecting data that often go into a GIS.",
   "whyNot": {
    "A": "Remote sensing collects images or data from far away, such as from satellites. It gathers data but is not the layering tool.",
    "B": "GPS finds a precise location. It collects location data but does not stack and analyze layers.",
    "C": "A census counts people and households. Its data can be one layer in a GIS, but it is not the tool itself.",
    "E": "An aerial photo is one picture. It cannot hold and compare several layers of data."
   },
   "vocab": [
    "geographic information system (GIS)",
    "layer",
    "geospatial technology"
   ]
  },
  {
   "id": "U1-P09",
   "topic": "1.2",
   "lo": "IMP-1.B",
   "skill": "1.D",
   "difficulty": "easy",
   "stem": "Scientists compare images of a mountain glacier taken from satellites in 1990, 2005, and 2020 to measure how much the ice has shrunk. Which method of collecting geographic data are they using?",
   "options": {
    "A": "Field observation",
    "B": "Satellite navigation (GPS)",
    "C": "Remote sensing",
    "D": "A population census",
    "E": "Personal interviews"
   },
   "answer": "C",
   "explanation": "Remote sensing means gathering information about Earth's surface from a distance, usually with satellites, airplanes, or drones. Comparing satellite images from different years shows change over time, like a glacier getting smaller.",
   "whyNot": {
    "A": "Field observation means going to the place and recording what you see in person. These scientists used images taken from space.",
    "B": "GPS satellites send signals that pinpoint a location. They do not take pictures of the glacier.",
    "D": "A census counts people, not ice.",
    "E": "Interviews collect people's words and opinions, not measurements of a glacier's size."
   },
   "vocab": [
    "remote sensing",
    "satellite imagery"
   ]
  },
  {
   "id": "U1-P10",
   "topic": "1.2",
   "lo": "IMP-1.B",
   "skill": "3.A",
   "difficulty": "medium",
   "stem": "A geographer wants to learn how longtime residents feel about the changes a new highway brought to their neighborhood. Which source would provide the most useful information?",
   "options": {
    "A": "Satellite images of the neighborhood before and after the highway was built",
    "B": "GPS data showing the average speed of cars on the highway",
    "C": "Census tables showing the neighborhood's population in each decade",
    "D": "A GIS layer showing property values along the highway",
    "E": "Recorded interviews with people who have lived there for decades"
   },
   "answer": "E",
   "explanation": "Feelings and opinions are qualitative information. The best way to get them is to ask people. Personal interviews are one of the sources of spatial information your AP course guide lists. Images, GPS, census tables, and GIS layers give numbers or pictures, but they cannot tell you how residents feel.",
   "whyNot": {
    "A": "Satellite images show physical changes, like new pavement, but not how people feel about them.",
    "B": "GPS speed data tell how fast cars move, not what residents think.",
    "C": "Census tables count people. They show who lives there, not their opinions.",
    "D": "Property values are numbers. They might hint at change, but they do not record residents' feelings."
   },
   "vocab": [
    "qualitative data",
    "quantitative data",
    "interview"
   ]
  },
  {
   "id": "U1-P11",
   "topic": "1.2",
   "lo": "IMP-1.B",
   "skill": "3.A",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "DATA GATHERED TO PLAN A NEW BUS ROUTE IN CITY P (HYPOTHETICAL)",
    "columns": [
     "Data set",
     "What it contains"
    ],
    "rows": [
     [
      "1",
      "Number of residents age 65 and older in each census tract, from the national census"
     ],
     [
      "2",
      "Notes from interviews with riders waiting at bus stops"
     ],
     [
      "3",
      "Images taken from aircraft and satellites showing where new apartment buildings were built"
     ],
     [
      "4",
      "Position of each city bus, recorded automatically every 30 seconds by a receiver on board"
     ],
     [
      "5",
      "One computer map that overlays data sets 1 through 4 so planners can compare them"
     ]
    ],
    "description": "A table describing five data sets a city collected to plan a new bus route.",
    "source": "Hypothetical data"
   },
   "stem": "Which data set was collected using a satellite navigation system?",
   "options": {
    "A": "Data set 1",
    "B": "Data set 2",
    "C": "Data set 3",
    "D": "Data set 4",
    "E": "Data set 5"
   },
   "answer": "D",
   "explanation": "A satellite navigation system, like GPS, uses signals from satellites to find an exact position. The receiver on each bus records where the bus is every 30 seconds. That is Data set 4.",
   "whyNot": {
    "A": "Data set 1 comes from a census, which counts people where they live.",
    "B": "Data set 2 comes from interviews, a field method that gathers people's words.",
    "C": "Data set 3 comes from remote sensing. Satellites took pictures, but they did not find the position of a receiver.",
    "E": "Data set 5 is a GIS, a tool that layers and analyzes data collected in other ways."
   },
   "vocab": [
    "GPS",
    "satellite navigation system",
    "remote sensing",
    "GIS"
   ]
  },
  {
   "id": "U1-P12",
   "topic": "1.3",
   "lo": "IMP-1.C",
   "skill": "3.D",
   "difficulty": "medium",
   "stimulus": {
    "type": "bar",
    "title": "CHILDREN UNDER AGE 5 BY NEIGHBORHOOD, CITY V, 2010 AND 2020 CENSUS (HYPOTHETICAL DATA)",
    "categories": [
     "Riverside",
     "Oak Hill",
     "Midtown",
     "Westfield",
     "Lakeview"
    ],
    "series": [
     {
      "name": "2010",
      "values": [
       650,
       1200,
       400,
       900,
       700
      ]
     },
     {
      "name": "2020",
      "values": [
       1480,
       1050,
       520,
       1120,
       610
      ]
     }
    ],
    "yLabel": "Children under age 5",
    "yMax": 1600,
    "description": "A grouped bar chart of the number of children under age 5 in five neighborhoods in 2010 and 2020. Riverside: 650 and 1,480. Oak Hill: 1,200 and 1,050. Midtown: 400 and 520. Westfield: 900 and 1,120. Lakeview: 700 and 610.",
    "source": "Hypothetical data"
   },
   "stem": "A school district plans to build one new elementary school where the number of young children is growing fastest. Based on the census data in the chart, which neighborhood is the best location?",
   "options": {
    "A": "Riverside",
    "B": "Oak Hill",
    "C": "Midtown",
    "D": "Westfield",
    "E": "Lakeview"
   },
   "answer": "A",
   "explanation": "Riverside's number of children under 5 more than doubled, from 650 to 1,480. That is the biggest increase and the largest total in 2020. These children will start school soon, so a new school there would serve the most students. This is how census data guide government decisions.",
   "whyNot": {
    "B": "Oak Hill had the most young children in 2010, but its number fell by 2020 (1,200 to 1,050).",
    "C": "Midtown grew a little (400 to 520), but it still has the fewest young children.",
    "D": "Westfield grew (900 to 1,120), but Riverside grew far more and now has more young children.",
    "E": "Lakeview's number of young children fell (700 to 610)."
   },
   "vocab": [
    "census",
    "geospatial data"
   ]
  },
  {
   "id": "U1-P13",
   "topic": "1.3",
   "lo": "IMP-1.C",
   "skill": "2.C",
   "difficulty": "medium",
   "stem": "A coffee company uses GIS to compare traffic counts, the locations of competing shops, and the incomes and ages of residents in each neighborhood before choosing where to open new stores. Which outcome is most likely?",
   "options": {
    "A": "New stores are spaced evenly across the city, one in each neighborhood",
    "B": "New stores open where land is cheapest, whatever the traffic or customers",
    "C": "New stores cluster along busy roads in areas with many likely customers",
    "D": "New stores are placed far from busy roads so customers can avoid traffic",
    "E": "New stores open in the most crowded census tracts, even where few people pass by"
   },
   "answer": "C",
   "explanation": "Businesses use geographic data to decide where to locate. By layering traffic, competitors, and customer information, the company can find spots where lots of likely customers pass by. That usually means stores cluster along busy roads in neighborhoods that match the company's customers.",
   "whyNot": {
    "A": "Spacing stores evenly ignores the data the company collected. Businesses go where customers are, not one per neighborhood.",
    "B": "Cheap land does not help if few customers pass by. The company's data focus on customers and traffic.",
    "D": "Coffee shops depend on passing traffic, so busy roads attract stores instead of pushing them away.",
    "E": "Population matters, but the company also weighs traffic and competitors, so it would not ignore those layers."
   },
   "vocab": [
    "GIS",
    "geospatial data",
    "clustering"
   ]
  },
  {
   "id": "U1-P14",
   "topic": "1.3",
   "lo": "IMP-1.C",
   "skill": "4.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "schematicMap",
    "title": "FLOOD RISK AND BUILDINGS ALONG THE RIVER, COUNTY T (HYPOTHETICAL GIS MAP)",
    "canvas": {
     "width": 800,
     "height": 400
    },
    "features": [
     {
      "kind": "land",
      "name": "Higher ground",
      "polygon": [
       [
        0,
        0
       ],
       [
        170,
        0
       ],
       [
        160,
        100
       ],
       [
        175,
        200
       ],
       [
        165,
        300
       ],
       [
        170,
        400
       ],
       [
        0,
        400
       ]
      ],
      "style": "small",
      "labelAt": [
       80,
       360
      ]
     },
     {
      "kind": "land",
      "name": "100-year floodplain",
      "polygon": [
       [
        170,
        0
       ],
       [
        160,
        100
       ],
       [
        175,
        200
       ],
       [
        165,
        300
       ],
       [
        170,
        400
       ],
       [
        445,
        400
       ],
       [
        430,
        300
       ],
       [
        450,
        200
       ],
       [
        425,
        100
       ],
       [
        440,
        0
       ]
      ],
      "style": "power",
      "labelAt": [
       300,
       360
      ]
     },
     {
      "kind": "land",
      "name": "100-year floodplain (east bank)",
      "polygon": [
       [
        470,
        0
       ],
       [
        455,
        100
       ],
       [
        480,
        200
       ],
       [
        460,
        300
       ],
       [
        475,
        400
       ],
       [
        520,
        400
       ],
       [
        528,
        300
       ],
       [
        515,
        200
       ],
       [
        530,
        100
       ],
       [
        520,
        0
       ]
      ],
      "style": "power"
     },
     {
      "kind": "land",
      "name": "Higher ground",
      "polygon": [
       [
        520,
        0
       ],
       [
        530,
        100
       ],
       [
        515,
        200
       ],
       [
        528,
        300
       ],
       [
        520,
        400
       ],
       [
        800,
        400
       ],
       [
        800,
        0
       ]
      ],
      "style": "small",
      "labelAt": [
       660,
       360
      ]
     },
     {
      "kind": "marker",
      "name": "Home",
      "symbol": "house",
      "points": [
       [
        215,
        60
       ],
       [
        290,
        45
       ],
       [
        370,
        70
       ],
       [
        230,
        140
       ],
       [
        390,
        150
       ],
       [
        220,
        250
       ],
       [
        340,
        260
       ],
       [
        395,
        300
       ],
       [
        40,
        120
       ],
       [
        110,
        220
       ],
       [
        60,
        290
       ],
       [
        600,
        230
       ],
       [
        690,
        250
       ],
       [
        740,
        160
       ],
       [
        620,
        300
       ]
      ]
     },
     {
      "kind": "marker",
      "name": "School",
      "symbol": "baseS",
      "points": [
       [
        300,
        185
       ]
      ]
     },
     {
      "kind": "marker",
      "name": "Hospital",
      "symbol": "baseN",
      "points": [
       [
        660,
        110
       ]
      ]
     }
    ],
    "legend": [
     {
      "swatch": "power",
      "label": "100-year floodplain (1% chance of flooding each year)"
     },
     {
      "swatch": "small",
      "label": "Higher ground"
     },
     {
      "swatch": "water",
      "label": "River"
     },
     {
      "swatch": "house",
      "label": "Home"
     },
     {
      "swatch": "baseS",
      "label": "School"
     },
     {
      "swatch": "baseN",
      "label": "Hospital"
     }
    ],
    "description": "A river runs north to south through the map. The shaded 100-year floodplain lies along both banks and is much wider on the west side. Eight homes and the school are inside the floodplain on the west bank. Three homes stand on higher ground at the far west edge. The hospital and four homes stand on higher ground east of the river, outside the floodplain.",
    "source": "Hypothetical map"
   },
   "stem": "County planners made this map in a GIS by combining a flood-risk layer with the locations of buildings. Which decision is best supported by the map?",
   "options": {
    "A": "Building a levee along the east bank to protect the hospital",
    "B": "Moving the school out of the shaded zone onto higher ground",
    "C": "Placing a new fire station in the shaded zone, near the most homes",
    "D": "Rezoning the shaded zone on the west bank for more new housing",
    "E": "Requiring flood insurance for the homes on higher ground east of the river"
   },
   "answer": "B",
   "explanation": "The shaded zone is where a big flood has a 1 percent chance of happening each year. The school sits inside that zone, so a flood could damage it and put children at risk. Moving it to higher ground outside the zone is the decision the map supports.",
   "whyNot": {
    "A": "The hospital is already on higher ground outside the shaded zone, so a levee there protects the wrong place.",
    "C": "Being close to homes helps, but a fire station inside the flood zone could be cut off or damaged in a flood.",
    "D": "Adding housing in the shaded zone would put more people and buildings at risk.",
    "E": "The homes east of the river are outside the shaded zone, so they face the lowest flood risk on the map."
   },
   "vocab": [
    "floodplain",
    "GIS",
    "layer"
   ]
  },
  {
   "id": "U1-P15",
   "topic": "1.3",
   "lo": "IMP-1.C",
   "skill": "1.D",
   "difficulty": "medium",
   "stem": "After an earthquake, a relief organization compares satellite images taken before and after the disaster to find blocked roads and damaged neighborhoods. How does this geographic data most directly help the organization?",
   "options": {
    "A": "It shows how residents feel about the government's response to the disaster",
    "B": "It predicts when and where the next earthquake in the region will strike",
    "C": "It counts how many people were living in each damaged building",
    "D": "It shows which damaged buildings were built before the city's earthquake building code",
    "E": "It helps decide where to send supplies and which roads trucks can use"
   },
   "answer": "E",
   "explanation": "Comparing 'before' and 'after' satellite images shows what changed: which roads are blocked and which neighborhoods are damaged. Relief groups use that to plan where to send food, water, and medicine and which roads trucks can still use. This is an organization using geographic data to make decisions.",
   "whyNot": {
    "A": "Images show physical damage, not people's opinions. Interviews would be needed for that.",
    "B": "Satellite images show what already happened. They cannot predict when the next earthquake will strike.",
    "C": "Images show buildings, not how many people lived inside. Census data would be needed for that.",
    "D": "Satellite images show damage, not when a building was built or what rules it followed. City records would be needed for that."
   },
   "vocab": [
    "remote sensing",
    "satellite imagery"
   ]
  },
  {
   "id": "U1-P16",
   "topic": "1.4",
   "lo": "PSO-1.A",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following describes the absolute location of a place?",
   "options": {
    "A": "It is at 32.8° N latitude, 96.8° W longitude.",
    "B": "It is about 50 kilometers south of the state capital.",
    "C": "It is on the east bank of the river, across from the old mill.",
    "D": "It is a two-hour drive from the nearest seaport.",
    "E": "It is next to the main highway, halfway between two large cities."
   },
   "answer": "A",
   "explanation": "Absolute location is an exact spot that does not change, usually given with latitude and longitude. Anyone can find 32.8° N, 96.8° W on a globe. The other choices describe where the place is compared to something else. That is relative location.",
   "whyNot": {
    "B": "Distance from the capital compares the place to another place, so it is relative location.",
    "C": "'Across from the old mill' is relative location. You have to know where the mill is.",
    "D": "Driving time to a seaport is relative location, and it can change if roads change.",
    "E": "'Halfway between two cities' is relative location."
   },
   "vocab": [
    "absolute location",
    "relative location",
    "latitude",
    "longitude"
   ]
  },
  {
   "id": "U1-P17",
   "topic": "1.4",
   "lo": "PSO-1.A",
   "skill": "2.C",
   "difficulty": "hard",
   "stimulus": {
    "type": "bar",
    "title": "SHARE OF A GROCERY STORE'S WEEKLY CUSTOMERS, BY DISTANCE FROM HOME TO THE STORE (HYPOTHETICAL DATA)",
    "categories": [
     "Under 1 km",
     "1–2 km",
     "2–3 km",
     "3–4 km",
     "4–5 km"
    ],
    "series": [
     {
      "name": "Share of customers (%)",
      "values": [
       41,
       26,
       16,
       10,
       7
      ]
     }
    ],
    "yLabel": "Percent of weekly customers",
    "yMax": 50,
    "description": "A bar chart. Of the store's weekly customers, 41 percent live less than 1 km away, 26 percent live 1–2 km away, 16 percent live 2–3 km away, 10 percent live 3–4 km away, and 7 percent live 4–5 km away.",
    "source": "Hypothetical data"
   },
   "stem": "The chart shows distance decay. Suppose a new expressway cuts driving times to the store from neighborhoods 3 to 5 kilometers away. Which change in the chart would most likely result?",
   "options": {
    "A": "The share of customers living under 1 km away would rise sharply",
    "B": "The bars would reverse, with the most customers living 4–5 km away",
    "C": "The 3–5 km bars would grow, making the drop-off with distance less steep",
    "D": "The chart would stay the same, because the distance in kilometers would not change",
    "E": "The 3–5 km bars would shrink, because more traffic would slow the trip"
   },
   "answer": "C",
   "explanation": "Distance decay means fewer people interact with a place the farther away they are, mostly because the trip takes more time and money. A faster expressway cuts the travel time from farther neighborhoods, so the store feels 'closer' to them. More people from 3 to 5 km away would shop there, and the drop-off in the chart would become less steep.",
   "whyNot": {
    "A": "The expressway helps farther neighborhoods, not the ones next door, so the nearest group would not jump.",
    "B": "Faster roads weaken distance decay but do not flip it. Nearby people still have the shortest trip.",
    "D": "The distance in kilometers stays the same, but travel time drops. People react to time and cost, so the pattern changes.",
    "E": "The expressway is built to cut driving times, so the trip from 3 to 5 km away gets easier, not harder."
   },
   "vocab": [
    "distance decay",
    "time-space compression",
    "friction of distance"
   ]
  },
  {
   "id": "U1-P18",
   "topic": "1.4",
   "lo": "PSO-1.A",
   "skill": "3.E",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "FASTEST COMMON TRAVEL TIME BETWEEN PORT CITY A AND INLAND CITY B (HYPOTHETICAL DATA)",
    "columns": [
     "Year",
     "Fastest common way to travel",
     "Travel time"
    ],
    "rows": [
     [
      "1820",
      "Horse-drawn coach",
      "12 days"
     ],
     [
      "1880",
      "Steam railroad",
      "30 hours"
     ],
     [
      "1950",
      "Car on a paved highway",
      "9 hours"
     ],
     [
      "2020",
      "Commercial airplane",
      "1.5 hours"
     ]
    ],
    "description": "A table of the fastest common travel time between two cities in four years: 12 days in 1820, 30 hours in 1880, 9 hours in 1950, and 1.5 hours in 2020.",
    "source": "Hypothetical data"
   },
   "stem": "Which concept is best illustrated by the trend in the table?",
   "options": {
    "A": "Distance decay, because the two cities interact less as time passes",
    "B": "Absolute distance, because the distance between the cities has shrunk",
    "C": "Environmental determinism, because terrain controls the travel time",
    "D": "Time-space compression, because new technology shrinks travel time",
    "E": "Flows, because the table counts the travelers moving between the cities"
   },
   "answer": "D",
   "explanation": "Time-space compression means places feel closer together because new technology makes travel and communication faster. The two cities never moved, but the trip shrank from 12 days to 1.5 hours.",
   "whyNot": {
    "A": "Distance decay says interaction drops with distance. Here the trip got easier, which weakens distance decay.",
    "B": "Absolute distance, measured in kilometers, did not change. Only the travel time did.",
    "C": "The terrain stayed the same while the technology changed, so the environment did not control the trend.",
    "E": "The table shows how long the trip takes, not how many people or goods move between the cities."
   },
   "vocab": [
    "time-space compression",
    "absolute distance",
    "relative distance"
   ]
  },
  {
   "id": "U1-P19",
   "topic": "1.4",
   "lo": "PSO-1.A",
   "skill": "1.A",
   "difficulty": "medium",
   "stem": "A geographer describes a town's hilly landscape, its brick houses, the language its residents speak, and its yearly harvest festival. The geographer is describing the town's",
   "options": {
    "A": "absolute location",
    "B": "place",
    "C": "relative location",
    "D": "site",
    "E": "space"
   },
   "answer": "B",
   "explanation": "In geography, place means the mix of physical and human features that makes a location special: its landforms and climate plus its buildings, language, and traditions. This description covers both kinds of features, so it is about place.",
   "whyNot": {
    "A": "Absolute location is an exact position, like latitude and longitude. The description gives no coordinates.",
    "C": "Relative location tells where a town is compared to other places. The description never mentions other places.",
    "D": "Site is the physical setting, like hills and rivers. This description also includes language and a festival, which are human features.",
    "E": "Space is about the area between things and how things are arranged in it, not the special character of one town."
   },
   "vocab": [
    "place",
    "space",
    "site"
   ]
  },
  {
   "id": "U1-P20",
   "topic": "1.4",
   "lo": "PSO-1.A",
   "skill": "2.B",
   "difficulty": "hard",
   "stem": "For centuries, Port Q was a small fishing harbor. After a canal opened nearby, ships traveling between two oceans began passing Port Q, and it grew into a major trading city. Which concept best explains this change?",
   "options": {
    "A": "Its absolute location changed when the canal was dug",
    "B": "Its site changed, because the canal altered the physical land of the harbor",
    "C": "Environmental determinism, since the harbor's natural depth decided its future",
    "D": "Its sense of place, such as its language and customs, began attracting traders",
    "E": "Its relative location improved because it now sat on a busy trade route"
   },
   "answer": "E",
   "explanation": "Relative location is where a place is compared to other places and routes. Port Q never moved, so its latitude and longitude stayed the same. But the canal put Port Q right on a busy shipping route. Its location compared to world trade became much better, and that is why it grew.",
   "whyNot": {
    "A": "Absolute location (latitude and longitude) does not change. The harbor stayed in the same spot.",
    "B": "Site is the physical setting of the harbor itself. The canal was built nearby. What changed was the port's connection to other places.",
    "C": "The harbor's natural setting was the same before and after. A human-built canal made the difference.",
    "D": "Nothing in the story says the town's culture changed. Growth came from ships now passing by."
   },
   "vocab": [
    "relative location",
    "absolute location",
    "site",
    "situation"
   ]
  },
  {
   "id": "U1-P21",
   "topic": "1.5",
   "lo": "PSO-1.B",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following best describes environmental determinism?",
   "options": {
    "A": "The idea that climate and landforms control how human societies develop",
    "B": "The idea that people can choose among several ways to use their environment",
    "C": "The idea that resources should be used so future generations can also meet their needs",
    "D": "The idea that interaction between places declines as the distance between them increases",
    "E": "The idea that new technology makes distant places feel closer together"
   },
   "answer": "A",
   "explanation": "Environmental determinism is an old idea that the physical environment, like climate and landforms, controls what people do and how societies develop. Geographers today reject it. Possibilism replaced it: the environment sets limits, but people make choices.",
   "whyNot": {
    "B": "That is possibilism, the idea that replaced environmental determinism.",
    "C": "That is sustainability.",
    "D": "That is distance decay, a spatial concept.",
    "E": "That is time-space compression."
   },
   "vocab": [
    "environmental determinism",
    "possibilism"
   ]
  },
  {
   "id": "U1-P22",
   "topic": "1.5",
   "lo": "PSO-1.B",
   "skill": "1.B",
   "difficulty": "medium",
   "stem": "In the Netherlands, people built dikes and pumped water out of shallow seas and lakes to create new farmland called polders. Which concept does this best illustrate?",
   "options": {
    "A": "Environmental determinism, because the low, wet land forced the Dutch to become farmers",
    "B": "Environmental determinism, because the sea set the limits of where people could live",
    "C": "Possibilism, because people used technology to work around an environmental limit",
    "D": "Sustainability, because the drained land went back to its natural condition",
    "E": "Distance decay, because the new farmland was created close to growing cities"
   },
   "answer": "C",
   "explanation": "Possibilism says the environment sets limits and offers choices, and people decide what to do using their technology and culture. The Dutch faced low land and water, but they built dikes and pumps to make new farmland. People shaped the result; the environment did not decide it for them.",
   "whyNot": {
    "A": "Determinism says nature controls people. Here people changed nature, which is the opposite.",
    "B": "The sea did limit where people could live at first, but people pushed back that limit. That goes against determinism.",
    "D": "Draining seas and lakes changed the natural environment a lot. The land did not go back to a natural state.",
    "E": "The story is about turning water into land, not about how interaction drops off with distance."
   },
   "vocab": [
    "possibilism",
    "polder",
    "environmental determinism"
   ]
  },
  {
   "id": "U1-P23",
   "topic": "1.5",
   "lo": "PSO-1.B",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "Which of the following correctly pairs a renewable resource with a nonrenewable resource?",
   "options": {
    "A": "Renewable: natural gas; nonrenewable: solar energy",
    "B": "Renewable: wind; nonrenewable: coal",
    "C": "Renewable: oil; nonrenewable: natural gas",
    "D": "Renewable: solar energy; nonrenewable: wind",
    "E": "Renewable: coal; nonrenewable: oil"
   },
   "answer": "B",
   "explanation": "A renewable resource is replaced by nature fast enough to keep using it, like wind and sunlight. Coal, oil, and natural gas are fossil fuels that took millions of years to form, so they are nonrenewable. Only choice B puts both resources in the right group.",
   "whyNot": {
    "A": "Natural gas took millions of years to form, so it is nonrenewable. Sunlight comes back every day, so solar energy is renewable.",
    "C": "Oil is a fossil fuel that took millions of years to form, so it is nonrenewable, not renewable.",
    "D": "Wind keeps blowing, so it is renewable. Both of these resources are renewable.",
    "E": "Coal is a fossil fuel that took millions of years to form, so it is nonrenewable, not renewable."
   },
   "vocab": [
    "natural resources",
    "renewable resource",
    "nonrenewable resource",
    "fossil fuel"
   ]
  },
  {
   "id": "U1-P24",
   "topic": "1.5",
   "lo": "PSO-1.B",
   "skill": "1.E",
   "difficulty": "hard",
   "stem": "Which of the following is the strongest criticism geographers make of environmental determinism?",
   "options": {
    "A": "It gives too much credit to human technology and too little to the physical environment",
    "B": "It focuses on local places and cannot be applied to whole world regions",
    "C": "It is a new idea that has not yet been tested with data from many places",
    "D": "It ignores human choice and was used to rank some societies above others",
    "E": "It overlooks climate, which has little effect on where people live or how they farm"
   },
   "answer": "D",
   "explanation": "Environmental determinism says climate and landforms control how people act. Geographers reject it because people make choices using their culture and technology. It was also used in the past to rank some societies above others, which helped people justify colonialism and racism. That is why possibilism replaced it.",
   "whyNot": {
    "A": "That points the wrong way. Determinism gives too much weight to the environment, not to technology.",
    "B": "Determinists did apply the idea to whole world regions, for example by claiming climate shaped entire civilizations.",
    "C": "Environmental determinism is an old idea. It was popular in the late 1800s and early 1900s and has since been rejected.",
    "E": "Climate does affect people, for example which crops they can grow. The problem is claiming that it controls them."
   },
   "vocab": [
    "environmental determinism",
    "possibilism"
   ]
  },
  {
   "id": "U1-P25",
   "topic": "1.5",
   "lo": "PSO-1.B",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "bar",
    "title": "AVERAGE DEPTH TO GROUNDWATER BELOW A DRY FARMING REGION, 1980–2020 (HYPOTHETICAL DATA)",
    "categories": [
     "1980",
     "1990",
     "2000",
     "2010",
     "2020"
    ],
    "series": [
     {
      "name": "Depth to groundwater (meters below the surface)",
      "values": [
       20,
       28,
       37,
       47,
       58
      ]
     }
    ],
    "yLabel": "Meters below the surface",
    "yMax": 60,
    "text": "Farms in the region water their crops with groundwater pumped from wells. The amount of rain that soaks down to refill the aquifer each year stayed about the same from 1980 to 2020.",
    "description": "A bar chart of the average depth to groundwater: 20 meters below the surface in 1980, 28 in 1990, 37 in 2000, 47 in 2010, and 58 in 2020.",
    "source": "Hypothetical data"
   },
   "stem": "Which conclusion about human–environment interaction is best supported by the chart and the note below it?",
   "options": {
    "A": "The water table is rising, so farmers could pump more each year",
    "B": "The dry climate controls how much water farms use, which supports environmental determinism",
    "C": "Groundwater is a nonrenewable resource, like coal, so pumping it uses it up",
    "D": "The rising depth numbers show that irrigation in the region can continue at its current rate",
    "E": "Farmers are pumping water out faster than rain refills it, which is not sustainable"
   },
   "answer": "E",
   "explanation": "The bars show the water getting deeper below the surface, from 20 meters to 58 meters. That means the water table is dropping. Rain refills the aquifer at about the same rate as before, so the drop comes from farmers pumping water out faster than nature puts it back. Using a resource faster than it renews is not sustainable.",
   "whyNot": {
    "A": "A bigger depth number means the water is farther down. The water table is falling, not rising.",
    "B": "Determinism says nature controls people. Here people's pumping is changing nature.",
    "C": "Unlike coal, groundwater is refilled by rain. The water table drops when pumping is faster than the refill rate.",
    "D": "A water table that drops every decade shows that current pumping cannot go on forever."
   },
   "vocab": [
    "sustainability",
    "aquifer",
    "natural resources",
    "water table"
   ]
  },
  {
   "id": "U1-P26",
   "topic": "1.6",
   "lo": "PSO-1.C",
   "skill": "5.A",
   "difficulty": "easy",
   "stem": "A map shades each of the world's countries by its average life expectancy. At which scale of analysis is this map?",
   "options": {
    "A": "Global, because the area being studied is the entire Earth",
    "B": "Regional, because the countries are grouped into continents",
    "C": "National, because each country's average is shown separately",
    "D": "Local, because life expectancy is recorded for each person",
    "E": "Regional, because nearby countries often have similar values"
   },
   "answer": "A",
   "explanation": "The scale of analysis is the size of the area being studied. This map covers the whole world, so it is global, even though the data are shown country by country. A map of only the countries of South America would be regional. A map of the states of Mexico would be national. A map of one city's neighborhoods would be local.",
   "whyNot": {
    "B": "The map does not group countries into continents or cover just one part of the world. It covers every country.",
    "C": "Each country gets its own color, but the map covers the whole world. A national-scale study looks inside one country, such as state by state.",
    "D": "Life expectancy starts with records of people, but this map shows country averages for the whole world. Local scale covers a city or neighborhood.",
    "E": "Neighboring countries may look alike, but the map still covers the whole world, so its scale is global."
   },
   "vocab": [
    "scale of analysis",
    "global scale"
   ]
  },
  {
   "id": "U1-P27",
   "topic": "1.6",
   "lo": "PSO-1.D",
   "skill": "5.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "UNEMPLOYMENT IN COUNTRY X AND ITS FOUR REGIONS, 2025 (HYPOTHETICAL DATA)",
    "columns": [
     "Area",
     "Labor force (millions)",
     "Unemployment rate (%)"
    ],
    "rows": [
     [
      "Country X (national)",
      "10.0",
      "6.0"
     ],
     [
      "North region",
      "4.0",
      "3.5"
     ],
     [
      "East region",
      "3.0",
      "4.0"
     ],
     [
      "South region",
      "2.0",
      "13.0"
     ],
     [
      "West region",
      "1.0",
      "8.0"
     ]
    ],
    "description": "A table of the labor force and unemployment rate for Country X as a whole and for each of its four regions.",
    "source": "Hypothetical data"
   },
   "stem": "Which conclusion can be drawn from the regional-scale data that could NOT be drawn from the national-scale data alone?",
   "options": {
    "A": "Unemployment in Country X is higher than in its neighboring countries",
    "B": "High unemployment is concentrated in the South, which the national rate hides",
    "C": "Country X's overall unemployment rate is 6.0 percent",
    "D": "Unemployment is spread fairly evenly across Country X's regions",
    "E": "The North has the most unemployed workers because it has the largest labor force"
   },
   "answer": "B",
   "explanation": "The national rate (6.0%) is an average for the whole country. At the regional scale, you can see the South's rate is 13.0%, more than twice the national rate, while the North's is only 3.5%. Changing the scale shows a pattern that the single national number hides.",
   "whyNot": {
    "A": "The table has no data on other countries, so it cannot support a comparison with neighbors.",
    "C": "The 6.0% rate is in the national row, so you would know it without the regional data.",
    "D": "The rates range from 3.5% to 13.0%, so they are far from even.",
    "E": "The North has 4.0 million × 3.5% = 140,000 unemployed. The South has 2.0 million × 13.0% = 260,000. The South has more."
   },
   "vocab": [
    "scale of analysis",
    "regional scale",
    "national scale"
   ]
  },
  {
   "id": "U1-P28",
   "topic": "1.6",
   "lo": "PSO-1.D",
   "skill": "5.B",
   "difficulty": "hard",
   "stem": "World population is still growing. Country Z's population is shrinking. Yet the population of Country Z's capital city is growing quickly. Which statement best explains how these patterns can all be true at once?",
   "options": {
    "A": "The three numbers conflict, so at least one data source is probably inaccurate",
    "B": "The capital grows because world population growth is shared equally among cities",
    "C": "Migration within Country Z could be shifting people from rural areas to the capital",
    "D": "Country Z's shrinking population shows that world population is about to fall",
    "E": "The capital's growth will soon make Country Z's national population grow again"
   },
   "answer": "C",
   "explanation": "Different things can happen at different scales. Worldwide, births still outnumber deaths. Country Z may have few births or many people leaving, so it shrinks. But inside Country Z, many people may be moving from the countryside to the capital for jobs, so the capital grows. Looking at only one scale would miss part of the story.",
   "whyNot": {
    "A": "The numbers do not conflict. Each scale can show a different trend at the same time.",
    "B": "Population growth is not shared out equally. Some places grow while others shrink.",
    "D": "One country shrinking says little about the world total, since many other countries are still growing.",
    "E": "People moving to the capital from elsewhere in Country Z do not add to the national total."
   },
   "vocab": [
    "scale of analysis",
    "rural-to-urban migration"
   ]
  },
  {
   "id": "U1-P29",
   "topic": "1.6",
   "lo": "PSO-1.C",
   "skill": "5.A",
   "difficulty": "medium",
   "stem": "A researcher wants to explain why residents of one city neighborhood must travel much farther than residents of other neighborhoods to reach a full-service grocery store. Which scale of analysis is most appropriate for this study?",
   "options": {
    "A": "Global, because food is traded among countries around the world",
    "B": "Regional, because grocery chains operate across several countries",
    "C": "National, because national laws decide where stores may open",
    "D": "National, because the census collects neighborhood data for the whole country",
    "E": "Local, because the question compares neighborhoods within one city"
   },
   "answer": "E",
   "explanation": "Pick the scale that matches the question. This question compares neighborhoods inside one city, so the local scale fits. Global, regional, or national data would blur the differences between neighborhoods.",
   "whyNot": {
    "A": "World trade affects food prices, but it cannot explain why one neighborhood lacks a store and another has one.",
    "B": "Chains may cross borders, but the question is about differences between neighborhoods in one city.",
    "C": "A national rule would not explain why one neighborhood differs from others in the same city.",
    "D": "The census does collect neighborhood data across the country, but this study compares neighborhoods in one city, which is the local scale."
   },
   "vocab": [
    "local scale",
    "scale of analysis",
    "food desert"
   ]
  },
  {
   "id": "U1-P30",
   "topic": "1.7",
   "lo": "SPS-1.A",
   "skill": "1.A",
   "difficulty": "easy",
   "stem": "An area in which a majority of residents speak French at home is best described as",
   "options": {
    "A": "a functional region, organized around a central node",
    "B": "a perceptual region, based on people's feelings and images",
    "C": "a transition zone, where two regions blend together",
    "D": "a formal region, defined by a shared measurable trait",
    "E": "a cultural hearth, the place where a language began"
   },
   "answer": "D",
   "explanation": "A formal region (also called a uniform region) is an area where people share one or more measurable traits, like a language. You can draw its borders using data, such as census counts of the language people speak at home.",
   "whyNot": {
    "A": "A functional region is tied together by connections to a center, like a city's commuter zone. A shared language is a trait, not a connection.",
    "B": "A perceptual region exists in people's minds, like 'the South.' A language majority can be measured with data.",
    "C": "A transition zone is the fuzzy edge where regions blend. The question describes the region itself, not its edge.",
    "E": "A hearth is where something started. The question is about where French is spoken now, not where it began."
   },
   "vocab": [
    "formal region",
    "uniform region"
   ]
  },
  {
   "id": "U1-P31",
   "topic": "1.7",
   "lo": "SPS-1.A",
   "skill": "1.D",
   "difficulty": "medium",
   "stem": "The area from which a hospital draws most of its patients, centered on the hospital and fading with distance, is best described as a",
   "options": {
    "A": "functional region, because it is organized around flows to a central node",
    "B": "functional region, because its people share the same language and culture",
    "C": "formal region, because its border is drawn on an official government map",
    "D": "perceptual region, because its edges are fuzzy and fade with distance",
    "E": "perceptual region, because patients feel loyal to their hospital"
   },
   "answer": "A",
   "explanation": "A functional (nodal) region is held together by connections to a central point, called the node. Patients travel to the hospital, so the hospital is the node. Its pull is strongest nearby and weaker farther away, which is distance decay at work.",
   "whyNot": {
    "B": "Sharing a language or culture defines a formal region. This region is defined by trips to the hospital.",
    "C": "An official border does not make a region formal; a formal region shares a measurable trait. This area is defined by trips to a center.",
    "D": "Many regions have fuzzy edges. This one is defined by flows to a central node, which makes it functional.",
    "E": "Feelings define perceptual regions, but this area is defined by where patients actually come from."
   },
   "vocab": [
    "functional region",
    "nodal region",
    "node"
   ]
  },
  {
   "id": "U1-P32",
   "topic": "1.7",
   "lo": "SPS-1.A",
   "skill": "3.C",
   "difficulty": "medium",
   "stimulus": {
    "type": "table",
    "title": "SHARE OF RESIDENTS WHO SAY THEY LIVE \"UP NORTH,\" SIX COUNTIES OF STATE K (HYPOTHETICAL SURVEY DATA)",
    "columns": [
     "County",
     "Distance north of the state capital (km)",
     "Residents who say they live \"Up North\" (%)"
    ],
    "rows": [
     [
      "Alder",
      "40",
      "6"
     ],
     [
      "Birch",
      "90",
      "22"
     ],
     [
      "Cedar",
      "140",
      "47"
     ],
     [
      "Dogwood",
      "190",
      "71"
     ],
     [
      "Elm",
      "240",
      "88"
     ],
     [
      "Fir",
      "290",
      "95"
     ]
    ],
    "description": "A table of six counties, from south to north, with the share of residents in each who say they live \"Up North\": Alder 6 percent, Birch 22, Cedar 47, Dogwood 71, Elm 88, and Fir 95.",
    "source": "Hypothetical data"
   },
   "stem": "Which statement about the region called \"Up North\" is best supported by the data?",
   "options": {
    "A": "It is a formal region with a sharp border between Birch and Cedar counties",
    "B": "It is a functional region centered on the state capital",
    "C": "It is a perceptual region whose edge is a gradual transition zone",
    "D": "It is a formal region, because the survey measured residents' answers with numbers",
    "E": "It is a perceptual region that begins sharply at the state capital"
   },
   "answer": "C",
   "explanation": "\"Up North\" is a perceptual (vernacular) region: it exists because of how people see where they live. The share of people who say they live \"Up North\" rises little by little as you go north, from 6% to 95%. There is no single line where it starts, so its edge is a transition zone, and different people would draw it in different places.",
   "whyNot": {
    "A": "The share climbs step by step through all six counties (6, 22, 47, 71, 88, 95), so there is no sharp border between any two of them.",
    "B": "Nothing in the table shows trips or connections to the capital. The region is defined by what people say about where they live.",
    "D": "Putting numbers on people's opinions does not make a region formal. The region is still based on how people see it, so it is perceptual.",
    "E": "Even in Alder, closest to the capital, only 6% say they live \"Up North.\" The share rises slowly, so the region has no sharp start at the capital."
   },
   "vocab": [
    "perceptual region",
    "vernacular region",
    "transition zone"
   ]
  },
  {
   "id": "U1-P33",
   "topic": "1.7",
   "lo": "SPS-1.A",
   "skill": "1.B",
   "difficulty": "hard",
   "stem": "Mexico is often placed in North America, in Latin America, and in a free-trade bloc with the United States and Canada. Which statement best explains why one country can belong to all three regions?",
   "options": {
    "A": "Regions are set by international law, and each country is assigned to several of them",
    "B": "Each region is defined by a different criterion, so regions can overlap",
    "C": "Mexico's borders have shifted, moving it from one region to another over time",
    "D": "Latin America and North America are the same region with two different names",
    "E": "Mexico belongs to whichever region its absolute location places it in"
   },
   "answer": "B",
   "explanation": "Geographers create regions by choosing what ties places together. North America is based on a continent, a physical landmass. Latin America is based on culture, such as languages that came from Spain and Portugal. The trade bloc is based on economic ties. Because each region uses a different trait, the same country can fit in all three. Regions can overlap.",
   "whyNot": {
    "A": "No law assigns countries to regions. Geographers and others draw regions for different purposes.",
    "C": "Mexico belongs to all three regions at the same time today. This is not about borders moving.",
    "D": "North America is a continent. Latin America is a cultural region that also includes most of South America, so they are not the same.",
    "E": "Absolute location (latitude and longitude) cannot tell you a region based on culture or trade."
   },
   "vocab": [
    "region",
    "formal region",
    "overlapping regions"
   ]
  }
 ],
 "exam": {
  "title": "Unit 1 Practice Exam: Thinking Geographically",
  "timeMinutes": 25,
  "questionCount": 25,
  "directions": "Each of the questions or incomplete statements below is followed by five suggested answers or completions. Select the one that is best in each case. Your score is based only on the number of questions answered correctly, so answer every question. Work quickly without losing accuracy, and come back to any question you skipped if time allows.",
  "stimulusCount": 10,
  "questions": [
   {
    "id": "U1-E01",
    "n": 1,
    "topic": "1.1",
    "lo": "IMP-1.A",
    "skill": "3.A",
    "difficulty": "easy",
    "stem": "A geographer wants to map the percentage of residents age 65 or older in each county of a state. Which type of map is best suited to this purpose?",
    "options": {
     "A": "Dot density map",
     "B": "Graduated symbol map",
     "C": "Choropleth map",
     "D": "Isoline map",
     "E": "Cartogram"
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. A dot density map shows counts, with each dot standing for a set number of people or things. It is not well suited to showing a percentage for each county.",
     "B": "Incorrect. A graduated symbol map uses symbols of different sizes, usually to show totals at point locations such as cities, not percentages for whole areas.",
     "C": "Correct. A choropleth map shades predefined areas, such as counties, by a rate or percentage, with darker shades usually showing higher values.",
     "D": "Incorrect. An isoline map connects points of equal value, such as elevation or temperature, that vary continuously across space rather than by county.",
     "E": "Incorrect. A cartogram resizes areas in proportion to a variable, which would distort the counties rather than shade them by percentage."
    },
    "explanation": "Choropleth maps color whole areas, like counties or states, by a rate or percentage. Darker usually means higher. The percent of residents age 65 or older in each county is a perfect fit."
   },
   {
    "id": "U1-E02",
    "n": 2,
    "topic": "1.1",
    "lo": "IMP-1.A",
    "skill": "3.A",
    "difficulty": "medium",
    "stem": "Which type of map would best show the total number of passengers using each of a country's 25 busiest airports?",
    "options": {
     "A": "A graduated symbol map with circles at each airport sized by its total",
     "B": "A choropleth map shading each state by its number of airport passengers",
     "C": "An isoline map connecting airports that have equal numbers of passengers",
     "D": "A reference map showing the location and name of each airport",
     "E": "A dot density map with one dot for each airport in the country"
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. A graduated symbol map places a symbol at each location and scales its size to the quantity, which suits totals at point locations such as airports.",
     "B": "Incorrect. Shading whole states would hide which airports carry the traffic, and choropleth maps are better suited to rates than to raw totals.",
     "C": "Incorrect. Isolines represent a continuous surface such as elevation or temperature; passenger counts at separate airports do not form a continuous surface.",
     "D": "Incorrect. A reference map would show where the airports are but not how many passengers each one handles.",
     "E": "Incorrect. One dot per airport shows only where airports are; it would not show differences in passenger totals."
    },
    "explanation": "Graduated symbol maps put a symbol, usually a circle, at each place and make it bigger for bigger numbers. A big circle means a busy airport, and a small circle means a less busy one."
   },
   {
    "id": "U1-E03",
    "n": 3,
    "set": "grids",
    "topic": "1.1",
    "lo": "IMP-1.A",
    "skill": "4.D",
    "difficulty": "medium",
    "stimulus": {
     "type": "schematicMap",
     "title": "TWO WORLD MAP GRIDS DRAWN AT THE SAME WIDTH: LINES OF LATITUDE EVERY 15° (75° S TO 75° N) AND LONGITUDE EVERY 30°",
     "canvas": {
      "width": 800,
      "height": 410
     },
     "features": [
      {
       "kind": "land",
       "name": "Map 1",
       "polygon": [
        [
         15,
         20
        ],
        [
         395,
         20
        ],
        [
         395,
         395
        ],
        [
         15,
         395
        ]
       ],
       "style": "small",
       "labelAt": [
        205,
        52
       ]
      },
      {
       "kind": "land",
       "name": "Map 2",
       "polygon": [
        [
         405,
         20
        ],
        [
         785,
         20
        ],
        [
         785,
         395
        ],
        [
         405,
         395
        ]
       ],
       "style": "small",
       "labelAt": [
        595,
        52
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 meridian",
       "line": [
        [
         35.0,
         105.3
        ],
        [
         35.0,
         324.7
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 meridian",
       "line": [
        [
         63.3,
         105.3
        ],
        [
         63.3,
         324.7
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 meridian",
       "line": [
        [
         91.7,
         105.3
        ],
        [
         91.7,
         324.7
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 meridian",
       "line": [
        [
         120.0,
         105.3
        ],
        [
         120.0,
         324.7
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 meridian",
       "line": [
        [
         148.3,
         105.3
        ],
        [
         148.3,
         324.7
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 meridian",
       "line": [
        [
         176.7,
         105.3
        ],
        [
         176.7,
         324.7
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 meridian",
       "line": [
        [
         205.0,
         105.3
        ],
        [
         205.0,
         324.7
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 meridian",
       "line": [
        [
         233.3,
         105.3
        ],
        [
         233.3,
         324.7
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 meridian",
       "line": [
        [
         261.7,
         105.3
        ],
        [
         261.7,
         324.7
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 meridian",
       "line": [
        [
         290.0,
         105.3
        ],
        [
         290.0,
         324.7
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 meridian",
       "line": [
        [
         318.3,
         105.3
        ],
        [
         318.3,
         324.7
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 meridian",
       "line": [
        [
         346.7,
         105.3
        ],
        [
         346.7,
         324.7
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 meridian",
       "line": [
        [
         375.0,
         105.3
        ],
        [
         375.0,
         324.7
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 1 parallel",
       "line": [
        [
         35,
         324.7
        ],
        [
         375,
         324.7
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 1 parallel",
       "line": [
        [
         35,
         286.3
        ],
        [
         375,
         286.3
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 1 parallel",
       "line": [
        [
         35,
         262.7
        ],
        [
         375,
         262.7
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 1 parallel",
       "line": [
        [
         35,
         244.7
        ],
        [
         375,
         244.7
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 1 parallel",
       "line": [
        [
         35,
         229.3
        ],
        [
         375,
         229.3
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 1 Equator",
       "line": [
        [
         35,
         215.0
        ],
        [
         375,
         215.0
        ]
       ],
       "dashed": true
      },
      {
       "kind": "line",
       "name": "Map 1 parallel",
       "line": [
        [
         35,
         200.7
        ],
        [
         375,
         200.7
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 1 parallel",
       "line": [
        [
         35,
         185.3
        ],
        [
         375,
         185.3
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 1 parallel",
       "line": [
        [
         35,
         167.3
        ],
        [
         375,
         167.3
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 1 parallel",
       "line": [
        [
         35,
         143.7
        ],
        [
         375,
         143.7
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 1 parallel",
       "line": [
        [
         35,
         105.3
        ],
        [
         375,
         105.3
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 2 meridian",
       "line": [
        [
         425.0,
         110.5
        ],
        [
         425.0,
         319.5
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 2 meridian",
       "line": [
        [
         453.3,
         110.5
        ],
        [
         453.3,
         319.5
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 2 meridian",
       "line": [
        [
         481.7,
         110.5
        ],
        [
         481.7,
         319.5
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 2 meridian",
       "line": [
        [
         510.0,
         110.5
        ],
        [
         510.0,
         319.5
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 2 meridian",
       "line": [
        [
         538.3,
         110.5
        ],
        [
         538.3,
         319.5
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 2 meridian",
       "line": [
        [
         566.7,
         110.5
        ],
        [
         566.7,
         319.5
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 2 meridian",
       "line": [
        [
         595.0,
         110.5
        ],
        [
         595.0,
         319.5
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 2 meridian",
       "line": [
        [
         623.3,
         110.5
        ],
        [
         623.3,
         319.5
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 2 meridian",
       "line": [
        [
         651.7,
         110.5
        ],
        [
         651.7,
         319.5
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 2 meridian",
       "line": [
        [
         680.0,
         110.5
        ],
        [
         680.0,
         319.5
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 2 meridian",
       "line": [
        [
         708.3,
         110.5
        ],
        [
         708.3,
         319.5
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 2 meridian",
       "line": [
        [
         736.7,
         110.5
        ],
        [
         736.7,
         319.5
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 2 meridian",
       "line": [
        [
         765.0,
         110.5
        ],
        [
         765.0,
         319.5
        ]
       ]
      },
      {
       "kind": "line",
       "name": "Map 2 parallel",
       "line": [
        [
         425,
         319.5
        ],
        [
         765,
         319.5
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 2 parallel",
       "line": [
        [
         425,
         308.7
        ],
        [
         765,
         308.7
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 2 parallel",
       "line": [
        [
         425,
         291.5
        ],
        [
         765,
         291.5
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 2 parallel",
       "line": [
        [
         425,
         269.1
        ],
        [
         765,
         269.1
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 2 parallel",
       "line": [
        [
         425,
         243.0
        ],
        [
         765,
         243.0
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 2 Equator",
       "line": [
        [
         425,
         215.0
        ],
        [
         765,
         215.0
        ]
       ],
       "dashed": true
      },
      {
       "kind": "line",
       "name": "Map 2 parallel",
       "line": [
        [
         425,
         187.0
        ],
        [
         765,
         187.0
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 2 parallel",
       "line": [
        [
         425,
         160.9
        ],
        [
         765,
         160.9
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 2 parallel",
       "line": [
        [
         425,
         138.5
        ],
        [
         765,
         138.5
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 2 parallel",
       "line": [
        [
         425,
         121.3
        ],
        [
         765,
         121.3
        ]
       ],
       "dashed": false
      },
      {
       "kind": "line",
       "name": "Map 2 parallel",
       "line": [
        [
         425,
         110.5
        ],
        [
         765,
         110.5
        ]
       ],
       "dashed": false
      }
     ],
     "legend": [
      {
       "swatch": "road",
       "label": "Equator (0°)"
      }
     ],
     "description": "Two rectangular grids of the same width. Each shows the same lines of latitude (every 15 degrees, from 75° S at the bottom to 75° N at the top) and the same lines of longitude (every 30 degrees). On both maps, lines of longitude are straight, parallel, and evenly spaced. On Map 1, the gaps between lines of latitude grow wider toward the poles. On Map 2, the gaps between lines of latitude grow narrower toward the poles.",
     "source": "Grid spacing computed from two standard world map projection formulas"
    },
    "stem": "Which statement best describes how Map 1 differs from Map 2?",
    "options": {
     "A": "Map 1 keeps the areas of high-latitude places accurate, while Map 2 enlarges them",
     "B": "Map 1 is an azimuthal projection centered on a pole, while Map 2 is cylindrical",
     "C": "Map 1 keeps distances true across the map, while Map 2 distorts distances",
     "D": "Map 1 increasingly enlarges areas toward the poles; Map 2 keeps relative areas correct",
     "E": "Map 1 and Map 2 distort area in the same way, since both show the same parallels"
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. This reverses the two maps. On Map 1 the parallels spread farther apart toward the poles while the meridians stay the same distance apart, so high-latitude areas are enlarged.",
     "B": "Incorrect. Both grids are cylindrical: their meridians are straight, parallel, and evenly spaced. An azimuthal polar projection would show meridians radiating from a central pole.",
     "C": "Incorrect. Neither grid keeps distances true across the whole map; on both, every parallel is drawn as long as the equator, so east–west scale grows toward the poles.",
     "D": "Correct. Map 1's spacing between parallels grows toward the poles, as on the Mercator projection, so high-latitude areas are enlarged. Map 2's spacing shrinks toward the poles, offsetting the east–west stretching so that relative areas stay correct, as on equal-area cylindrical projections such as the Gall-Peters.",
     "E": "Incorrect. The grids show the same parallels, but the spacing between them differs, and that spacing determines how area is distorted."
    },
    "explanation": "Look at the gaps between the flat lines. On Map 1 the gaps get bigger near the poles, so places there get stretched taller as well as wider and look too big, like Greenland on a Mercator map. On Map 2 the gaps get smaller near the poles, which squeezes places back down so their areas stay correct, like on a Gall-Peters map."
   },
   {
    "id": "U1-E04",
    "n": 4,
    "set": "grids",
    "topic": "1.1",
    "lo": "IMP-1.A",
    "skill": "4.F",
    "difficulty": "hard",
    "stem": "Which statement best describes a limitation of Map 2?",
    "options": {
     "A": "It enlarges the area of Canada and Russia compared with Brazil and India",
     "B": "It flattens the shapes of high-latitude places, squeezing them north to south",
     "C": "It keeps compass bearings as straight lines, so it is useful mainly for sea navigation",
     "D": "It shows true distances from its center point but distorts areas elsewhere",
     "E": "It is a compromise map with small distortions of area, shape, distance, and direction"
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. That describes Map 1. Map 2's narrowing spacing toward the poles keeps relative areas correct, so Canada and Russia are not enlarged compared with Brazil and India.",
     "B": "Correct. To keep area true, an equal-area cylindrical map shrinks north–south distances toward the poles while east–west distances are stretched, so high-latitude landmasses look flattened. Equal-area maps give up correct shape.",
     "C": "Incorrect. Showing compass bearings as straight lines is the strength of the Mercator projection, the type shown in Map 1, not of an equal-area map.",
     "D": "Incorrect. True distances from a center point are a property of azimuthal equidistant projections, which are built around a center point rather than a rectangular grid.",
     "E": "Incorrect. Compromise projections such as the Robinson spread small distortions across all four properties; Map 2 keeps area exact and gives up correct shape."
    },
    "explanation": "Every map projection gives something up. Map 2 keeps areas correct, but to do that it squishes places near the poles from top to bottom, so their shapes look flat and wide. You can trust Map 2 for comparing sizes, not shapes."
   },
   {
    "id": "U1-E05",
    "n": 5,
    "topic": "1.1",
    "lo": "IMP-1.A",
    "skill": "1.B",
    "difficulty": "medium",
    "stem": "A subway map shows each line as a straight colored path with evenly spaced stations, even though the real tracks curve and the stations are different distances apart. Which statement best explains why the mapmaker drew it this way?",
    "options": {
     "A": "The mapmaker lacked accurate GPS data on the location of each station",
     "B": "Subway maps are reference maps, which require exact distances and shapes",
     "C": "The map is an isoline map that connects stations with equal numbers of riders",
     "D": "Map projections badly distort shape and area on maps of small areas such as a city",
     "E": "All maps are selective, and this one trades true distance for clear connections"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. The simplification is a deliberate design choice; accurate location data are easy to obtain, and the map leaves them out on purpose.",
     "B": "Incorrect. Reference maps help users locate places, but no map shows everything exactly; this map deliberately gives up true distance.",
     "C": "Incorrect. Isoline maps connect points of equal value on a continuous surface; subway lines connect stations along a route.",
     "D": "Incorrect. Projection distortion is very small over an area as small as a city, so it cannot explain straightened lines and evenly spaced stations.",
     "E": "Correct. All maps are selective in the information they show. A transit map gives up accurate distance and shape to make routes, transfers, and the order of stations easy to read."
    },
    "explanation": "Every map leaves things out or changes things on purpose. A subway rider needs to know the order of the stops and where to switch lines, not the exact curve of the tracks. So the mapmaker straightened the lines to make the map easy to use."
   },
   {
    "id": "U1-E06",
    "n": 6,
    "topic": "1.2",
    "lo": "IMP-1.B",
    "skill": "1.D",
    "difficulty": "easy",
    "stem": "A delivery app shows customers exactly where their driver is as the driver moves through the city. The app most directly relies on which geospatial technology to find the driver's position?",
    "options": {
     "A": "A satellite navigation system such as GPS",
     "B": "Remote sensing images taken by satellites",
     "C": "A national census of population and housing",
     "D": "Field interviews with drivers and customers",
     "E": "A choropleth map of the city's neighborhoods"
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. Satellite navigation systems such as the Global Positioning System (GPS) use signals from satellites to calculate a receiver's position, which the app can display in real time.",
     "B": "Incorrect. Remote sensing gathers images or other data about Earth's surface from a distance; it does not track the position of a phone in a moving car.",
     "C": "Incorrect. A census counts people and housing at set times; it cannot locate a moving driver.",
     "D": "Incorrect. Interviews collect qualitative information about people's experiences, not precise real-time positions.",
     "E": "Incorrect. A choropleth map shades areas by a rate or percentage; it does not track the position of anything."
    },
    "explanation": "GPS uses signals from satellites to figure out exactly where a phone or other receiver is. The driver's phone finds its spot with GPS, and the app shows that spot on a map."
   },
   {
    "id": "U1-E07",
    "n": 7,
    "topic": "1.2",
    "lo": "IMP-1.B",
    "skill": "1.A",
    "difficulty": "medium",
    "stem": "A geographer studying a neighborhood's history reads letters written by early settlers, newspaper stories from the 1920s, and a city planning report from 1965. These sources are best described as",
    "options": {
     "A": "geospatial data collected with remote sensing",
     "B": "quantitative data gathered by a national census",
     "C": "written accounts that provide spatial information",
     "D": "layers created with a geographic information system",
     "E": "field data collected with a satellite navigation system"
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. Remote sensing collects data from a distance, such as satellite images, not letters or reports.",
     "B": "Incorrect. Census data are counts of people and housing collected by a government; letters and news stories are written accounts.",
     "C": "Correct. The AP course framework lists written accounts, such as field observations, media reports, travel narratives, policy documents, and personal interviews, as sources of spatial information. Settlers' letters, old newspaper stories, and a planning report fit this category.",
     "D": "Incorrect. A GIS is a tool for storing and analyzing data in layers; the sources themselves are written documents.",
     "E": "Incorrect. Satellite navigation systems such as GPS record precise positions; they do not produce letters or reports."
    },
    "explanation": "Letters, newspaper stories, and government reports are written accounts. Geographers use them to learn what places were like and how people saw them. They are not numbers from a census or pictures from a satellite."
   },
   {
    "id": "U1-E08",
    "n": 8,
    "set": "landcover",
    "topic": "1.2",
    "lo": "IMP-1.B",
    "skill": "3.A",
    "difficulty": "medium",
    "stimulus": {
     "type": "bar",
     "title": "LAND COVER IN RIVER COUNTY, 2005 AND 2025 (HYPOTHETICAL DATA)",
     "categories": [
      "Forest",
      "Cropland",
      "Wetland",
      "Built-up land",
      "Water"
     ],
     "series": [
      {
       "name": "2005",
       "values": [
        34,
        38,
        12,
        10,
        6
       ]
      },
      {
       "name": "2025",
       "values": [
        30,
        31,
        7,
        26,
        6
       ]
      }
     ],
     "yLabel": "Percent of county area",
     "yMax": 40,
     "text": "Built-up land includes buildings, roads, and parking lots.",
     "description": "A grouped bar chart of land cover as a percent of River County's area. Forest: 34 percent in 2005 and 30 percent in 2025. Cropland: 38 and 31. Wetland: 12 and 7. Built-up land: 10 and 26. Water: 6 and 6.",
     "source": "Hypothetical data"
    },
    "stem": "The land-cover data in the chart were most likely gathered by",
    "options": {
     "A": "a satellite navigation system that tracks the position of moving vehicles",
     "B": "remote sensing, using images of the county taken from satellites",
     "C": "a census that asks each household how its land is used",
     "D": "interviews with longtime residents about how the county has changed",
     "E": "a GIS, which creates new land-cover data without outside sources"
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. Satellite navigation systems such as GPS record the positions of receivers; they do not measure how much of a county is forest, cropland, or built-up land.",
     "B": "Correct. Remote sensing gathers information about Earth's surface from a distance. Sorting satellite images into land-cover types is the usual way to measure land cover across a whole county and to compare different years.",
     "C": "Incorrect. A census counts people and housing; it does not measure land cover such as forest or wetland across an entire county.",
     "D": "Incorrect. Interviews provide qualitative information about people's experiences; they cannot produce consistent land-cover percentages for two different years.",
     "E": "Incorrect. A GIS stores, analyzes, and displays data, but the land-cover data must first be collected, usually by remote sensing."
    },
    "explanation": "To measure how much of a whole county is forest, farmland, or city, you need a view from above. Satellites take pictures from space, and computers sort the pictures into land types. That is remote sensing."
   },
   {
    "id": "U1-E09",
    "n": 9,
    "set": "landcover",
    "topic": "1.5",
    "lo": "PSO-1.B",
    "skill": "3.C",
    "difficulty": "medium",
    "stem": "Which conclusion about human–environment interaction is best supported by the chart?",
    "options": {
     "A": "Environmental determinism explains the changes, since nature decided the county's land use",
     "B": "Because cropland shrank, the county's farms are producing less food than in 2005",
     "C": "The loss of wetland was caused by changes in rainfall rather than by human activity",
     "D": "Land use in the county became more sustainable, since the area of water stayed the same",
     "E": "Built-up land grew as natural land covers such as forest and wetland shrank"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. Environmental determinism holds that the physical environment controls human activity. The chart shows people changing the environment, which runs the other way.",
     "B": "Incorrect. The chart shows the area of cropland, not crop output; farms can produce as much or more on less land if yields rise.",
     "C": "Incorrect. The chart gives no rainfall data, and the growth of built-up land points to human activity as a likely cause of land-cover change.",
     "D": "Incorrect. An unchanged water area does not show sustainability, especially when wetland and forest, which provide habitat and can absorb floodwater, declined.",
     "E": "Correct. Built-up land rose from 10 to 26 percent of the county while forest fell from 34 to 30 percent and wetland from 12 to 7 percent, showing people reshaping the environment through land use."
    },
    "explanation": "Built-up land (buildings, roads, and parking lots) went from 10% to 26% of the county. At the same time, forest and wetland got smaller. People changed the land to fit their needs. That is human–environment interaction."
   },
   {
    "id": "U1-E10",
    "n": 10,
    "topic": "1.3",
    "lo": "IMP-1.C",
    "skill": "2.C",
    "difficulty": "medium",
    "stem": "Between two censuses, State A's population grew much faster than the U.S. population as a whole, while State B's population stayed about the same. Based on the new census data, which outcome is most likely?",
    "options": {
     "A": "State A is likely to lose seats in the U.S. Senate, and State B may gain one",
     "B": "Both states keep the same number of House seats, since the number of seats per state is fixed",
     "C": "State A's boundary expands to include part of a neighboring state",
     "D": "State A is likely to gain House seats, and State B may lose one",
     "E": "State B is likely to gain House seats to make up for its slower growth"
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Every state has two senators regardless of population, so census results do not change Senate seats.",
     "B": "Incorrect. The total of 435 House seats is set by law, but how those seats are divided among the states is recalculated after every census.",
     "C": "Incorrect. State boundaries do not change after a census; only the apportionment of House seats does.",
     "D": "Correct. After each census, the 435 House seats are reapportioned according to each state's population. A state growing faster than the country is likely to gain seats, and a state with little growth may lose seats.",
     "E": "Incorrect. Seats follow population; a state that grows slowly compared with the country tends to lose seats, not gain them."
    },
    "explanation": "The 435 House seats are divided up by population after every census. If a state grows faster than the rest of the country, it usually gets more seats. If it does not grow, it can lose a seat to a faster-growing state."
   },
   {
    "id": "U1-E11",
    "n": 11,
    "topic": "1.4",
    "lo": "PSO-1.A",
    "skill": "1.A",
    "difficulty": "easy",
    "stem": "Which of the following statements describes a town's relative location?",
    "options": {
     "A": "The town hall stands at 35.2° N latitude and 97.4° W longitude.",
     "B": "The town lies 60 kilometers upstream from the river's mouth.",
     "C": "The town is home to about 25,000 people.",
     "D": "The town's hilly land and rocky soil limit farming.",
     "E": "The town's name comes from a local word for \"meeting place.\""
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. Latitude and longitude give absolute location, a position that does not depend on other places.",
     "B": "Correct. Relative location describes a place in relation to other places or features, here the river's mouth.",
     "C": "Incorrect. Population size is a characteristic of the place, not a description of where it is.",
     "D": "Incorrect. Hilly land and rocky soil describe the town's site, its physical setting, not its position relative to other places.",
     "E": "Incorrect. A place name, or toponym, can reveal history or culture but does not describe location."
    },
    "explanation": "Relative location tells where a place is compared to something else, like \"60 kilometers upstream from the river's mouth.\" Absolute location uses exact coordinates instead."
   },
   {
    "id": "U1-E12",
    "n": 12,
    "topic": "1.4",
    "lo": "PSO-1.A",
    "skill": "1.B",
    "difficulty": "medium",
    "stem": "Engineers in two countries on opposite sides of the world work on the same design in real time using video calls and shared online files. This situation best illustrates",
    "options": {
     "A": "time-space compression, because technology reduces the effect of distance",
     "B": "distance decay, because the engineers interact less as the distance between them grows",
     "C": "absolute distance, because the two countries are now closer together",
     "D": "a functional region centered on the engineers' main office",
     "E": "a formal region, because the engineers share the same profession"
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. Time-space compression is the reduced importance of distance as transportation and communication technologies speed the movement of people, goods, and information. Real-time collaboration across the world is an example.",
     "B": "Incorrect. Distance decay predicts less interaction with greater distance; here the engineers interact closely despite great distance, which shows distance decay being weakened.",
     "C": "Incorrect. The absolute distance between the countries has not changed; what changed is how much that distance limits interaction.",
     "D": "Incorrect. Nothing in the scenario describes a central office drawing in flows; it describes distance mattering less.",
     "E": "Incorrect. A shared profession could help define a formal region, but the scenario is about technology overcoming distance, not about a region."
    },
    "explanation": "Time-space compression means the world feels smaller because technology lets people connect quickly over long distances. Video calls let engineers on opposite sides of Earth work together as if they were in the same room."
   },
   {
    "id": "U1-E13",
    "n": 13,
    "set": "commute",
    "topic": "1.7",
    "lo": "SPS-1.A",
    "skill": "1.D",
    "difficulty": "medium",
    "stimulus": {
     "type": "schematicMap",
     "title": "DAILY COMMUTING TO CITY M FROM SIX NEARBY TOWNS (HYPOTHETICAL DATA)",
     "canvas": {
      "width": 800,
      "height": 440
     },
     "features": [
      {
       "kind": "land",
       "name": "",
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
         440
        ],
        [
         0,
         440
        ]
       ]
      },
      {
       "kind": "land",
       "name": "Town A 64%",
       "style": "small",
       "labelAt": [
        400.0,
        136.0
       ],
       "polygon": [
        [
         360.0,
         114.0
        ],
        [
         440.0,
         114.0
        ],
        [
         440.0,
         158.0
        ],
        [
         360.0,
         158.0
        ]
       ]
      },
      {
       "kind": "land",
       "name": "Town B 57%",
       "style": "small",
       "labelAt": [
        323.6,
        296.4
       ],
       "polygon": [
        [
         283.6,
         274.4
        ],
        [
         363.6,
         274.4
        ],
        [
         363.6,
         318.4
        ],
        [
         283.6,
         318.4
        ]
       ]
      },
      {
       "kind": "land",
       "name": "Town C 41%",
       "style": "small",
       "labelAt": [
        580.0,
        220.0
       ],
       "polygon": [
        [
         540.0,
         198.0
        ],
        [
         620.0,
         198.0
        ],
        [
         620.0,
         242.0
        ],
        [
         540.0,
         242.0
        ]
       ]
      },
      {
       "kind": "land",
       "name": "Town D 32%",
       "style": "small",
       "labelAt": [
        212.9,
        112.0
       ],
       "polygon": [
        [
         172.9,
         90.0
        ],
        [
         252.9,
         90.0
        ],
        [
         252.9,
         134.0
        ],
        [
         172.9,
         134.0
        ]
       ]
      },
      {
       "kind": "land",
       "name": "Town E 14%",
       "style": "small",
       "labelAt": [
        92.7,
        274.2
       ],
       "polygon": [
        [
         52.7,
         252.2
        ],
        [
         132.7,
         252.2
        ],
        [
         132.7,
         296.2
        ],
        [
         52.7,
         296.2
        ]
       ]
      },
      {
       "kind": "land",
       "name": "Town F 8%",
       "style": "small",
       "labelAt": [
        736.1,
        310.1
       ],
       "polygon": [
        [
         696.1,
         288.1
        ],
        [
         776.1,
         288.1
        ],
        [
         776.1,
         332.1
        ],
        [
         696.1,
         332.1
        ]
       ]
      },
      {
       "kind": "land",
       "name": "City M",
       "style": "power",
       "labelAt": [
        400,
        220
       ],
       "polygon": [
        [
         345,
         196
        ],
        [
         370,
         188
        ],
        [
         440,
         190
        ],
        [
         456,
         212
        ],
        [
         450,
         246
        ],
        [
         405,
         252
        ],
        [
         352,
         244
        ]
       ]
      },
      {
       "kind": "arrow",
       "name": "Commuters from Town A to City M",
       "from": [
        400.0,
        163.0
       ],
       "to": [
        400.0,
        182.0
       ]
      },
      {
       "kind": "arrow",
       "name": "Commuters from Town B to City M",
       "from": [
        349.1,
        270.9
       ],
       "to": [
        363.8,
        256.2
       ]
      },
      {
       "kind": "arrow",
       "name": "Commuters from Town C to City M",
       "from": [
        535.0,
        220.0
       ],
       "to": [
        462.0,
        220.0
       ]
      },
      {
       "kind": "arrow",
       "name": "Commuters from Town D to City M",
       "from": [
        255.3,
        136.5
       ],
       "to": [
        339.4,
        185.0
       ]
      },
      {
       "kind": "arrow",
       "name": "Commuters from Town E to City M",
       "from": [
        137.6,
        266.3
       ],
       "to": [
        338.1,
        230.9
       ]
      },
      {
       "kind": "arrow",
       "name": "Commuters from Town F to City M",
       "from": [
        691.3,
        298.1
       ],
       "to": [
        461.8,
        236.6
       ]
      },
      {
       "kind": "shippingLane",
       "name": "Edge of City M's commuting zone",
       "line": [
        [
         150,
         75
        ],
        [
         470,
         75
        ],
        [
         650,
         160
        ],
        [
         655,
         270
        ],
        [
         560,
         330
        ],
        [
         380,
         345
        ],
        [
         260,
         340
        ],
        [
         170,
         250
        ],
        [
         150,
         150
        ],
        [
         150,
         75
        ]
       ],
       "dashed": true
      },
      {
       "kind": "scaleBar",
       "label": "0 — 10 km",
       "from": [
        30,
        415
       ],
       "to": [
        90,
        415
       ]
      }
     ],
     "legend": [
      {
       "swatch": "power",
       "label": "City M"
      },
      {
       "swatch": "small",
       "label": "Town, with the percent of its workers who commute to City M"
      },
      {
       "swatch": "lane",
       "label": "Dashed line: towns where 25% or more of workers commute to City M"
      }
     ],
     "description": "City M is at the center. Arrows show daily commuting from six towns to jobs in City M. Each town is labeled with the percent of its workers who commute to City M: Town A, 14 km from City M, 64%; Town B, 18 km, 57%; Town C, 30 km, 41%; Town D, 36 km, 32%; Town E, 52 km, 14%; Town F, 58 km, 8%. A dashed line encloses City M and Towns A, B, C, and D.",
     "source": "Hypothetical data"
    },
    "stem": "The area inside the dashed line on the map is best described as which type of region?",
    "options": {
     "A": "A formal region, because the towns share the same government",
     "B": "A perceptual region, because residents feel they belong to City M",
     "C": "A functional region, tied together by daily commuting to City M",
     "D": "A formal region, because it is drawn using a measured percentage",
     "E": "A functional region, because its towns share a uniform climate and landscape"
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. The map gives no information about a shared government; the towns are grouped by their connections to City M.",
     "B": "Incorrect. A perceptual region is based on people's feelings or images of a place; the map shows measured commuting, not feelings.",
     "C": "Correct. A functional (nodal) region is organized around a central node and defined by flows and connections to it. The dashed line encloses the towns most strongly linked to City M by daily commuting.",
     "D": "Incorrect. The 25 percent threshold measures each town's connection to City M. A region defined by flows to a node is functional, even when a number is used to draw its edge.",
     "E": "Incorrect. A shared climate and landscape would define a formal region; this region is defined by commuting to City M, not by a uniform trait."
    },
    "explanation": "A functional region is built around a center, called the node, and is held together by movement to it. Here, workers from the towns travel to jobs in City M every day. The dashed line wraps around the towns most connected to City M. The 25% line is a number, but what it measures is trips to City M. A region held together by trips to a center is functional, not formal."
   },
   {
    "id": "U1-E14",
    "n": 14,
    "set": "commute",
    "topic": "1.4",
    "lo": "PSO-1.A",
    "skill": "3.B",
    "difficulty": "easy",
    "stem": "Which concept best explains the pattern of commuting percentages shown on the map?",
    "options": {
     "A": "Time-space compression, because commuters from distant towns reach City M fastest",
     "B": "Clustering, because the towns are bunched tightly around City M",
     "C": "Relative location, because each town's latitude and longitude set its commuting share",
     "D": "Environmental determinism, because the landscape forces workers to commute",
     "E": "Distance decay, because the share commuting to City M falls as distance increases"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. The farthest towns have the lowest commuting shares, so distance still limits interaction; time-space compression would weaken this pattern.",
     "B": "Incorrect. Clustering describes how features are arranged; the towns lie at different distances from City M, and the key pattern is that commuting shares fall with that distance.",
     "C": "Incorrect. Latitude and longitude describe absolute location. The pattern depends on each town's distance from City M.",
     "D": "Incorrect. The map shows no physical barriers, and commuting is a choice shaped by travel time and cost, not by the landscape alone.",
     "E": "Correct. Distance decay is the decline in interaction between places as the distance between them increases. Towns nearest City M send the largest shares of workers; the farthest towns send the smallest."
    },
    "explanation": "Close towns send lots of workers to City M, and far towns send only a few. The farther away a town is, the smaller the share. That drop-off with distance is distance decay."
   },
   {
    "id": "U1-E15",
    "n": 15,
    "set": "commute",
    "topic": "1.4",
    "lo": "PSO-1.A",
    "skill": "2.C",
    "difficulty": "hard",
    "stem": "Suppose a fast commuter rail line opened between City M and Town F. Which change would most likely follow?",
    "options": {
     "A": "Town F's commuting share would fall, because rail weakens ties to City M",
     "B": "City M's functional region would shrink toward the towns nearest the city",
     "C": "Town F would form its own formal region of rail commuters",
     "D": "Town F's commuting share would rise, which could bring it inside the dashed line",
     "E": "Distance decay would increase, because the trip from Town F would take longer"
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Faster transportation lowers the time cost of travel, which strengthens, not weakens, a town's connection to the central city.",
     "B": "Incorrect. Better transportation tends to extend a functional region outward, not shrink it.",
     "C": "Incorrect. Using the same mode of transportation does not create a formal region; the rail line would tie Town F more closely to City M's functional region.",
     "D": "Correct. A fast rail line would cut travel time, an example of time-space compression that weakens distance decay. More of Town F's workers would likely commute to City M, which could push its share above the 25 percent threshold and extend the functional region.",
     "E": "Incorrect. A fast rail line would shorten the trip, reducing the effect of distance rather than increasing it."
    },
    "explanation": "A fast train makes Town F feel closer to City M because the trip takes less time. More people from Town F would take jobs in City M. If enough of them do, Town F could end up inside City M's commuting region."
   },
   {
    "id": "U1-E16",
    "n": 16,
    "topic": "1.5",
    "lo": "PSO-1.B",
    "skill": "1.C",
    "difficulty": "medium",
    "stem": "Which of the following statements best reflects possibilism rather than environmental determinism?",
    "options": {
     "A": "A dry climate limits farming, but people can choose to irrigate, herd, or trade",
     "B": "A region's climate decides what kind of economy its people will have",
     "C": "Mountain landscapes cause the people who live in them to develop the same customs",
     "D": "Societies near the sea become sea traders because the coast controls their choices",
     "E": "The physical environment has no effect on how people live or what they grow"
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. Possibilism holds that the physical environment sets limits and offers opportunities, but people choose among options based on their culture and technology.",
     "B": "Incorrect. Claiming that climate decides a region's economy is environmental determinism, the view that the environment controls human activity.",
     "C": "Incorrect. Claiming that a landscape causes people to share customs is environmental determinism.",
     "D": "Incorrect. Saying that the coast controls people's choices is environmental determinism; possibilism would say the coast offers options that people may or may not use.",
     "E": "Incorrect. Possibilism does not deny the environment's influence; it treats the environment as setting limits within which people make choices."
    },
    "explanation": "Determinism says nature decides what people do. Possibilism says nature sets limits, but people choose what to do within those limits. A dry place limits farming, but people can still pick irrigation, herding, or trade."
   },
   {
    "id": "U1-E17",
    "n": 17,
    "topic": "1.5",
    "lo": "PSO-1.B",
    "skill": "1.D",
    "difficulty": "easy",
    "stem": "A town that depends on a nearby forest for timber decides to cut no more trees each year than the forest regrows and to replant the areas it harvests. Which concept does this policy best reflect?",
    "options": {
     "A": "Environmental determinism, because the forest controls the town's economy",
     "B": "Sustainability, because it meets today's needs without using up the forest",
     "C": "Nonrenewable resource use, because cut trees cannot be replaced",
     "D": "Distance decay, because the town relies on the forest closest to it",
     "E": "Resource depletion, because the town removes trees from the forest each year"
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. The town made a deliberate choice about how much to harvest; environmental determinism holds that the environment controls human activity.",
     "B": "Correct. Sustainability means using resources to meet present needs without compromising the ability of future generations to meet their own needs. Harvesting no more than regrows, and replanting, keeps the forest productive.",
     "C": "Incorrect. Trees are a renewable resource; they regrow, which is what makes this policy possible.",
     "D": "Incorrect. The forest is nearby, but the policy is about how much to harvest over time, not about how interaction changes with distance.",
     "E": "Incorrect. Harvesting a renewable resource does not deplete it when the harvest stays within the rate of regrowth."
    },
    "explanation": "Sustainability means using what you need now while leaving enough for the future. Cutting only as many trees as grow back, and replanting, means the forest will still be there for people later."
   },
   {
    "id": "U1-E18",
    "n": 18,
    "set": "scales",
    "topic": "1.6",
    "lo": "PSO-1.D",
    "skill": "5.B",
    "difficulty": "medium",
    "stimulus": {
     "type": "table",
     "title": "POPULATION CHANGE IN COUNTRY Y AT THREE SCALES, 2015–2025 (HYPOTHETICAL DATA)",
     "columns": [
      "Area",
      "Population, 2015 (millions)",
      "Population, 2025 (millions)",
      "Change (%)"
     ],
     "rows": [
      [
       "Country Y (national)",
       "20.00",
       "20.40",
       "+2.0"
      ],
      [
       "Province 1",
       "8.00",
       "8.64",
       "+8.0"
      ],
      [
       "Province 2",
       "7.00",
       "6.65",
       "−5.0"
      ],
      [
       "Province 3",
       "5.00",
       "5.11",
       "+2.2"
      ],
      [
       "Province 2: Capital District",
       "2.00",
       "2.12",
       "+6.0"
      ],
      [
       "Province 2: River District",
       "3.00",
       "2.73",
       "−9.0"
      ],
      [
       "Province 2: Hill District",
       "2.00",
       "1.80",
       "−10.0"
      ]
     ],
     "description": "A table of population in 2015 and 2025 for Country Y as a whole, for its three provinces, and for the three districts that make up Province 2.",
     "source": "Hypothetical data"
    },
    "stem": "Which statement is best supported by comparing the national data with the provincial data?",
    "options": {
     "A": "The national growth rate accurately describes the change in each province",
     "B": "Province 3's growth was caused by people moving there from Province 2",
     "C": "Modest national growth hides a population decline in one province",
     "D": "Province 2's decline means Country Y is likely to lose population soon",
     "E": "Province 1 grew fastest because it has the largest land area"
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. Provincial changes range from a gain of 8.0 percent to a loss of 5.0 percent, so the national figure of +2.0 percent does not describe each province.",
     "B": "Incorrect. The table shows population change but not migration flows; it cannot show where Province 3's new residents came from.",
     "C": "Correct. At the national scale Country Y grew by 2.0 percent, but at the provincial scale Province 2 lost 5.0 percent. Changing the scale of analysis reveals variation that the national figure hides.",
     "D": "Incorrect. Growth in Provinces 1 and 3 more than offset Province 2's loss; the data do not show that the national population is about to fall.",
     "E": "Incorrect. The table contains no data on land area, so it cannot support a claim about why Province 1 grew fastest."
    },
    "explanation": "The whole country grew a little (+2.0%). But zoom in to the provinces and you see Province 2 actually lost people (−5.0%). The national number hid that. Changing the scale shows a different pattern."
   },
   {
    "id": "U1-E19",
    "n": 19,
    "set": "scales",
    "topic": "1.6",
    "lo": "PSO-1.D",
    "skill": "5.C",
    "difficulty": "hard",
    "stem": "Which conclusion is best supported by the district-level data for Province 2?",
    "options": {
     "A": "River and Hill districts shrank because they are farthest from Country Y's capital",
     "B": "The Capital District's growth shows that Province 2 as a whole is growing",
     "C": "District data add little, since they show the same pattern as provincial data",
     "D": "The Capital District grew because it has a higher birth rate than other districts",
     "E": "The Capital District grew even though Province 2 as a whole lost people"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. The table gives no information about where the districts are or how far they are from the national capital, so it cannot support this explanation.",
     "B": "Incorrect. Province 2 lost 5.0 percent overall; growth in one district did not offset losses in the other two.",
     "C": "Incorrect. The district data reveal a growing Capital District that the provincial figure of −5.0 percent hides, so they add important information.",
     "D": "Incorrect. The table shows population totals, not birth rates; the growth could come from migration, births, or both.",
     "E": "Correct. The Capital District grew by 6.0 percent while Province 2 as a whole fell by 5.0 percent. Analysis at a finer scale reveals growth within a declining province, a pattern that could reflect people moving from the River and Hill districts to the Capital District."
    },
    "explanation": "Province 2 shrank overall. But zooming in again shows that its Capital District grew by 6%, while the other two districts lost a lot of people. One more change of scale reveals one more hidden pattern."
   },
   {
    "id": "U1-E20",
    "n": 20,
    "set": "scales",
    "topic": "1.3",
    "lo": "IMP-1.C",
    "skill": "3.F",
    "difficulty": "hard",
    "stem": "Country Y's national government will fund new primary schools based on where population is growing. Which approach would most likely lead to the best decisions?",
    "options": {
     "A": "Use the national rate of 2.0 percent and divide new schools equally among provinces",
     "B": "Use provincial data alone, building no new schools anywhere in Province 2",
     "C": "Wait for the next census, since current data do not show where people live",
     "D": "Use district-level data so places like the Capital District are not missed",
     "E": "Use provincial data and build the most schools in Province 2, since it lost the most people"
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. The national rate hides large differences among provinces and districts, so dividing schools equally would send some to places that are shrinking.",
     "B": "Incorrect. Province 2 lost population overall, but its Capital District grew by 6.0 percent; ignoring the whole province would overlook a growing area.",
     "C": "Incorrect. The table already shows where population grew and shrank; waiting would delay decisions without adding needed information.",
     "D": "Correct. Geographic data are used at all scales for government decision-making. Finer-scale data reveal growth that provincial or national figures hide, such as the Capital District's 6.0 percent increase within a shrinking province.",
     "E": "Incorrect. New schools are needed where population is growing; Province 2 lost population overall, and most of its loss came in River and Hill districts."
    },
    "explanation": "The most detailed data show exactly where the number of people is going up. Province 2 shrank overall, but its Capital District grew. If the government looked only at provinces, it would miss that spot. Using smaller-scale data helps put schools where they are needed."
   },
   {
    "id": "U1-E21",
    "n": 21,
    "topic": "1.6",
    "lo": "PSO-1.C",
    "skill": "5.A",
    "difficulty": "easy",
    "stem": "A study compares rates of internet access among the countries of Southeast Asia. At which scale of analysis is this study?",
    "options": {
     "A": "Global, because it compares countries",
     "B": "Regional, because it covers one part of the world",
     "C": "National, because each country reports its own data",
     "D": "Local, because internet access is measured in each household",
     "E": "Global, because the internet connects the whole world"
    },
    "answer": "B",
    "rationales": {
     "A": "Incorrect. Comparing countries does not make a study global; the global scale covers the whole world, while this study covers only Southeast Asia.",
     "B": "Correct. The regional scale refers to a part of the world larger than one country, such as Southeast Asia, or to a large area within a country. Comparing Southeast Asian countries is regional-scale analysis.",
     "C": "Incorrect. The national scale examines patterns within one country; this study compares several countries.",
     "D": "Incorrect. Data may be collected from households, but the scale of analysis is set by the area the study covers: a world region.",
     "E": "Incorrect. The internet is global, but the study covers only one world region."
    },
    "explanation": "Scale of analysis means the size of the area you are studying. Southeast Asia is one part of the world: bigger than one country but smaller than the whole planet. That is the regional scale."
   },
   {
    "id": "U1-E22",
    "n": 22,
    "topic": "1.7",
    "lo": "SPS-1.A",
    "skill": "1.A",
    "difficulty": "medium",
    "stem": "When residents of a state were asked to draw the boundaries of \"the Hill Country\" on a blank map, their drawings overlapped in the middle but differed a lot at the edges. \"The Hill Country\" is best described as",
    "options": {
     "A": "a perceptual region, based on people's ideas about an area",
     "B": "a formal region, based on a single trait such as elevation",
     "C": "a functional region, based on travel to a central city",
     "D": "a perceptual region, based on a boundary set by state law",
     "E": "a functional region, based on shared tourism businesses"
    },
    "answer": "A",
    "rationales": {
     "A": "Correct. Perceptual (vernacular) regions exist in people's minds and reflect shared ideas and feelings about a place. Different people draw their boundaries in different places, so the edges are fuzzy.",
     "B": "Incorrect. A formal region defined by elevation would have boundaries drawn from data, so residents' drawings would not need to differ.",
     "C": "Incorrect. A functional region is defined by connections to a central node, such as commuting to a city; the drawings reflect people's images of an area, not travel patterns.",
     "D": "Incorrect. A boundary set by law would be the same on every map and would not depend on people's ideas; the drawings differ because no official boundary exists.",
     "E": "Incorrect. Tourism businesses could form part of a network, but the region in the question is defined by how residents picture it."
    },
    "explanation": "Perceptual regions live in people's heads. Everyone agrees about the middle, but people draw the edges in different places. That fuzzy, disagree-at-the-edges pattern is the sign of a perceptual region."
   },
   {
    "id": "U1-E23",
    "n": 23,
    "topic": "1.7",
    "lo": "SPS-1.A",
    "skill": "2.A",
    "difficulty": "medium",
    "stem": "On a map of the languages spoken at home in a border area, the share of people who speak Language X falls gradually from 90 percent to 10 percent over about 50 kilometers, with many bilingual towns in between. Which statement best describes the boundary of the Language X region?",
    "options": {
     "A": "It is a sharp line that follows the international border",
     "B": "It is a functional boundary based on travel to one city",
     "C": "It is a perceptual boundary, since the language people speak cannot be measured",
     "D": "It is set by law, so mapmakers place it in the same spot",
     "E": "It is a transition zone where the region blends into its neighbor"
    },
    "answer": "E",
    "rationales": {
     "A": "Incorrect. The share of Language X speakers changes gradually across about 50 kilometers, so there is no single sharp line.",
     "B": "Incorrect. The region is defined by a shared trait, the language people speak, not by flows to a central city.",
     "C": "Incorrect. The language spoken at home can be measured with surveys or census data; this is a formal region based on a measurable trait.",
     "D": "Incorrect. Language regions are not set by law; different mapmakers might draw the edge at different percentages.",
     "E": "Correct. Regional boundaries are often transitional. Here the Language X region fades into its neighbor across a zone of bilingual towns rather than ending at a sharp line."
    },
    "explanation": "Regions often do not have sharp edges. As you travel across this border area, Language X becomes less and less common, and many towns speak two languages. That in-between area is a transition zone."
   },
   {
    "id": "U1-E24",
    "n": 24,
    "topic": "1.7",
    "lo": "SPS-1.A",
    "skill": "1.B",
    "difficulty": "hard",
    "stem": "Maps of \"the Middle East\" made by different governments, news organizations, and textbooks often include different sets of countries. Which statement best explains this?",
    "options": {
     "A": "The Middle East is a formal region with an official boundary that changes each year",
     "B": "The Middle East is a functional region, so its edges move with each day's trade flows",
     "C": "People define regions using different criteria, so boundaries can be contested",
     "D": "The maps use different projections, which change which countries appear in a region",
     "E": "The region has no shared characteristics, so it cannot be mapped consistently"
    },
    "answer": "C",
    "rationales": {
     "A": "Incorrect. There is no official, legally fixed boundary of the Middle East; its extent depends on who is defining it and why.",
     "B": "Incorrect. The Middle East is usually defined by shared cultural, historical, or political ties, not by daily flows to a single central node.",
     "C": "Correct. Regions are defined by people using one or more chosen characteristics. Because organizations use different criteria, such as culture, history, or politics, regional boundaries are often contested and overlapping.",
     "D": "Incorrect. A map projection changes the shape and size of places, not which countries a mapmaker chooses to include in a region.",
     "E": "Incorrect. The countries share characteristics that many people use to define a region; the disagreement is over which countries meet the chosen criteria."
    },
    "explanation": "People make regions by choosing what ties places together, like language, religion, history, or politics. Different groups choose differently, so their maps include different countries. That is why regional boundaries are often argued over and can overlap."
   },
   {
    "id": "U1-E25",
    "n": 25,
    "topic": "1.3",
    "lo": "IMP-1.C",
    "skill": "2.C",
    "difficulty": "medium",
    "stem": "A popular navigation app uses real-time traffic data to send drivers off a jammed highway onto quiet residential streets. Which outcome is the most likely geographic effect of this decision?",
    "options": {
     "A": "The absolute distance between the highway and the neighborhoods will shrink",
     "B": "The residential streets will become a formal region defined by app use",
     "C": "The neighborhoods' relative location will change, since they are now farther from the highway",
     "D": "More cars will use residential streets, and towns may add speed bumps",
     "E": "Fewer people will drive, since the app shows the highway is crowded"
    },
    "answer": "D",
    "rationales": {
     "A": "Incorrect. Absolute distance does not change; rerouting changes travel time and traffic patterns, not the distance between places.",
     "B": "Incorrect. Using the same app does not create a formal region; the likely effect is a change in traffic flows on those streets.",
     "C": "Incorrect. The neighborhoods have not moved and are no farther from the highway; what changes is the amount of traffic passing through them.",
     "D": "Correct. Decisions made with geospatial data have geographic effects. Rerouting many drivers onto local streets increases traffic there, which can lead towns to lower speed limits, add speed bumps, or restrict turns.",
     "E": "Incorrect. The app helps drivers continue their trips by another route; it does not by itself lead people to stop driving."
    },
    "explanation": "When the app sends lots of drivers onto small neighborhood streets, those streets get busy. Towns may then add speed bumps or new rules. A decision made with map data changed what happens on the ground."
   }
  ]
 }
}

===== SOURCES.md =====
# Unit 1 bank: sources and what was verified

All stimulus data in Unit 1 are **hypothetical** (labeled "Hypothetical data" or "Hypothetical map" in each title or
source line). No real-world statistics appear in any table, chart, or map. The real-world facts used in stems,
explanations, and rationales, and the formulas behind the projection-grid stimulus, are listed below.
Every number is rechecked by `u1/verify.py`, which `u1/assemble.py` runs on every build.

| Where | Claim | Source (URL) | What was checked |
|---|---|---|---|
| U1-P04 | Africa is about 14 times larger than Greenland | Greenland 2,166,086 sq km: CIA World Factbook (https://www.indexmundi.com/greenland/area.html, which quotes the Factbook; archived Factbook GL summary https://www.cia.gov/the-world-factbook/about/archives/2021/static/445b5377c20a6bb8caebb11040ac4395/GL-summary.pdf). Africa about 30,365,000 sq km: Encyclopaedia Britannica, "Africa" (https://www.britannica.com/place/Africa) | 30,365,000 / 2,166,086 = 14.02 (script) |
| U1-P07 | Canada has about three times India's area | CIA World Factbook, Country Comparison: Area (mirror: https://start.csail.mit.edu/mirror/cia.gov/library/publications/the-world-factbook/rankorder/2147rank.html): Canada 9,984,670 sq km; India 3,287,263 sq km | 9,984,670 / 3,287,263 = 3.04 (script) |
| U1-E03, E04 stimulus | Map 1 parallels spaced by the Mercator formula, y = R ln tan(π/4 + φ/2) | CRC Concise Encyclopedia of Mathematics, "Mercator Projection" (https://archive.lib.msu.edu/crcmath/math/math/m/m187.htm), formula (2); same as Snyder, *Map Projections: A Working Manual*, USGS PP 1395 (https://pubs.usgs.gov/publication/pp1395) | Gaps between 15° parallels grow toward the poles (14.3 → 38.4 px); gap ratios match the formula (script) |
| U1-E03, E04 stimulus | Map 2 parallels spaced by the cylindrical equal-area formula, x = (λ − λ0) cos φs, y = sin φ / cos φs, with φs = 45° (Gall-Peters) | CRC Concise Encyclopedia of Mathematics, "Cylindrical Equal-Area Projection" (https://archive.lib.msu.edu/crcmath/math/math/c/c910.htm); MathWorks Mapping Toolbox, "Gall Orthographic Projection" (https://au.mathworks.com/help/map/gortho.html): "the standard parallel is by definition fixed at 45º" and "It is equal-area, but distortion of shape increases with distance from the standard parallels" | Gaps shrink toward the poles (28.0 → 10.8 px); band heights are proportional to the difference of sines, i.e., equal-area (script); shapes above 45° are flattened north–south (E04 key) |

## Facts stated without a number (standard course content, no external data)
- Mercator (1569) keeps compass bearings as straight lines and local shapes; area grows toward the poles. Gall-Peters
  is equal-area; Robinson is a compromise projection; Goode's homolosine is an interrupted equal-area projection;
  an azimuthal equidistant map shows true distance and direction from its center only.
- The U.S. census is taken every ten years and is used to reapportion the 435 House seats; every state has two
  senators (E10).
- Dutch polders are land reclaimed with dikes and drainage (P22). Coal is nonrenewable; wind is renewable (P23).
- Sustainability wording follows the common "meet present needs without compromising future generations" definition (E17).
- Environmental determinism was influential in the late 1800s and early 1900s and was used to rank societies (P24).

## Hypothetical stimuli (all arithmetic in `u1/verify.py`)
P02 dot-density map (22 squares east of the river, 4 west); P03 contour map (line spacing west 18 < south 30 <
north 38 < east 70 px; J, K, L, M each between the same two contours); P06 business rates (Baker 8.0 per 1,000 is
highest); P11 bus-route data sets; P12 children under 5 (Riverside has the largest 2020 count, largest absolute and
percent growth); P14 floodplain map (8 homes + school inside the floodplain; hospital and 4 homes on east high
ground); P17 customer shares sum to 100 and fall with distance; P18 travel times fall; P25 groundwater depth rises;
P27 regional unemployment averages to the 6.0% national rate (North 140,000 vs South 260,000 unemployed);
P32 "Up North" shares rise steadily; E08 land cover sums to 100 in both years; E13 commuting map (shares fall with
distance; towns at 25% or more are inside the dashed line, others outside; scale bar = 10 km); E18 provinces sum to
the nation and districts sum to Province 2 in both years, and every % change matches.
