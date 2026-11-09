# Unit 1: Thinking Geographically — practice-exam bank v2026-11-08d

Exam weighting: 8–10% of the AP Exam multiple-choice section

Calibration: Original AP Human Geography Unit 1 practice aligned to the course framework (Fall 2020 Course and Exam Description). The timed assessment follows the AP multiple-choice format and pacing, with five answer choices and a mix of individual and stimulus-based questions. It is not an official College Board exam, and its difficulty has not been statistically equated to the AP Exam; difficulty labels are editorial estimates not yet calibrated with student-response data. All questions, stimuli, and data are original or compiled from public facts; no College Board items are reproduced.

Checked: Nov 8, 2026: automated checks in u1/assemble.py (answer balance and runs, option-length tells, absolute-word tells, field completeness, LO/skill tags, set structure) and u1/verify.py (every stimulus number, map geometry, and data-based key recomputed by script); independent Claude checker agent (blind answers 58/58, arithmetic and projection-grid geometry recomputed, E13 checked against the OMB 25% commuting standard); fixes applied in v2026-11-08b: P26 rewritten, P23 rewritten, P03 description and stem, E03-E04 neutral source line, label-pair and hedge tells (E22, P32, E10), P05 E, P15 D, E05 key wording, E13 explanation, E19 rationale, E20 D. ChatGPT Pro full review (v2026-11-08b, ~10 min; all arithmetic and projection/map geometry independently confirmed) applied in v2026-11-08c after each claim was checked: P26 and E21 now ask the scale at which data are aggregated; P17, E08, E20 rewritten to need the stimulus or the stated limitation; P03 Point N moved between two contours; P25 title and key narrowed; neutral visible captions on P02, P03, P14, E03-E04 with screen-reader details kept in the SVG description; latitude labels on the E03-E04 grids; evidence-precision fixes to explanations and rationales (P04-P07, P12-P16, P18, P22, P24, P29, P31-P33, E02, E04-E06, E10, E14, E15, E19, E22-E25); skill retags; one-letter-per-five answer pattern removed by reordering (IDs kept); P34-P36 added for pattern reading, field observation, and limits of aggregated data. Final independent Claude blind check of v2026-11-08c: 61/61, no must-fix; geometry and data recomputed; should-fix tells applied in v2026-11-08d (map-dependent distractors in P14 and P34, P36 E, E20 E, E15 B hedge, E25 E, P35 key moved from E to A for the topic 1.2 letter pattern and P36 key moved from C to E to keep practice letters balanced, P13 explanation, "the question" wording in P22, P31, E22).

Topics: 1.1 Introduction to Maps (IMP-1.A); 1.2 Geographic Data (IMP-1.B); 1.3 The Power of Geographic Data (IMP-1.C); 1.4 Spatial Concepts (PSO-1.A); 1.5 Human–Environmental Interaction (PSO-1.B); 1.6 Scales of Analysis (PSO-1.C, PSO-1.D); 1.7 Regional Analysis (SPS-1.A)

## Practice

### U1-P01
Topic 1.1 · IMP-1.A · Skill 1.A · easy

Which of the following is the best example of a reference map?

- **A.** A world map shading each country by its average life expectancy
- **B.** A state highway map showing roads, cities, rivers, and county lines
- **C.** A map using circles of different sizes to show the population of each large city
- **D.** A map with lines connecting places that have the same average January temperature
- **E.** A world map with each country resized in proportion to its number of people

**Answer: B**

Explanation: A reference map helps you find places. It shows general features like roads, cities, rivers, and borders. A highway map is a classic reference map. Thematic maps are different: each one is made to show one topic, like life expectancy or temperature.

- Why not A: Shading countries by life expectancy shows one topic. That is a thematic map (a choropleth map).
- Why not C: Circles sized by population show one topic. That makes it a thematic symbol map (a graduated or proportional symbol map).
- Why not D: Lines joining places with the same temperature show one topic. That is a thematic map (an isoline map).
- Why not E: Resizing countries by population shows one topic. That is a thematic map (a cartogram).

Vocab: reference map, thematic map

### U1-P02
Topic 1.1 · IMP-1.A · Skill 3.A · easy

**Stimulus (schematicMap): DAIRY FARMS IN COUNTY R (HYPOTHETICAL)**

Legend: [baseN] Each square = 10 dairy farms; [water] River

Description: Each square represents 10 dairy farms. Symbol placement shows the approximate distribution of farms. North is at the top.

Source: Hypothetical data

The map above is best classified as which type of thematic map?

- **A.** Choropleth map
- **B.** Graduated symbol map
- **C.** Isoline map
- **D.** Dot density map
- **E.** Cartogram

**Answer: D**

Explanation: On a dot density map, each repeated symbol stands for the same amount. Here, each square stands for 10 dairy farms. More squares in an area mean more farms there. A square does not show the exact spot of one farm. The squares are bunched (clustered) just east of the river.

- Why not A: A choropleth map shades whole areas, like counties, darker or lighter. This map places symbols instead of shading areas.
- Why not B: A graduated symbol map uses bigger symbols for bigger amounts. Every square here is the same size.
- Why not C: An isoline map draws lines that connect places with equal values, like elevation. There are no lines like that here.
- Why not E: A cartogram resizes areas to show a number, like population. This map uses repeated symbols instead.

Vocab: dot density map, thematic map, clustering

### U1-P04
Topic 1.1 · IMP-1.A · Skill 1.B · medium

On a Mercator projection, Greenland looks about as large as Africa, even though Africa is about 14 times as large. Which of the following best explains this distortion?

- **A.** The Mercator projection keeps areas accurate, so its distortion is in the shapes of landmasses near the equator.
- **B.** Mercator is a compromise projection that spreads small distortions evenly across the whole map.
- **C.** The Mercator projection preserves local angles and shapes while enlarging areas more toward the poles.
- **D.** The Mercator projection is centered on the North Pole, so places close to the pole are drawn larger.
- **E.** The Mercator projection keeps true distances from the equator, so places far from it look bigger.

**Answer: C**

Explanation: Mercator made his map in 1569 for sailors. It keeps the shapes of small areas and local angles correct, and a route with one steady compass bearing shows up as a straight line. The price is area: the map stretches more and more toward the North and South Poles. Greenland is far north, so it looks much bigger than it really is. Africa sits on the equator, where there is little stretching.

- Why not A: That describes an equal-area map like Gall-Peters. Mercator does the opposite: it keeps local shapes but distorts area.
- Why not B: That describes a compromise map like the Robinson. Mercator's distortion is not spread evenly; it grows toward the poles.
- Why not D: The usual Mercator map is a rectangle centered on the equator, not on the North Pole. Its stretching grows toward both poles.
- Why not E: Mercator does not keep true distances. Its scale grows toward the poles, which is why far-north places look too big.

Vocab: Mercator projection, map projection, distortion

### U1-P03
Topic 1.1 · IMP-1.A · Skill 3.B · medium

**Stimulus (schematicMap): CONTOUR MAP OF HILL Q (HYPOTHETICAL). CONTOUR INTERVAL: 20 METERS**

Labels on map: J; K; L; M; N

Description: Contours connect points of equal elevation. The contour interval is 20 meters, from 100 meters (outer line) to 180 meters (inner line). North is at the top.

Source: Hypothetical map

Based on the map, at which labeled point is the land steepest?

- **A.** Point J
- **B.** Point K
- **C.** Point L
- **D.** Point M
- **E.** Point N

**Answer: A**

Explanation: Contour lines are isolines: each line connects places at the same height. When the lines are packed close together, the land climbs a lot in a short distance, so it is steep. At Point J the lines are closest together.

- Why not B: At Point K the lines are far apart, so the land rises slowly. That is a gentle slope.
- Why not C: Point L's lines are closer than at K but farther apart than at J, so it is less steep than J.
- Why not D: Point M's lines are fairly close, but they are not packed as tightly as at J.
- Why not E: The lines around Point N are as far apart as the lines at Point K, so the slope there is gentle, not steep like at J.

Vocab: isoline, contour line, elevation

### U1-P07
Topic 1.1 · IMP-1.A · Skill 1.D · easy

On a certain world map, India appears much larger than Canada, even though Canada has about three times as much area. The map draws each country's size in proportion to its population. This type of map is called a

- **A.** cartogram
- **B.** choropleth map
- **C.** reference map
- **D.** dot density map
- **E.** Mercator projection

**Answer: A**

Explanation: A cartogram changes each area's size on the map to show a number, like population. India has far more people than Canada, so a population cartogram draws India much bigger. Depending on the design, a cartogram may also change shapes and where places sit.

- Why not B: A choropleth map uses shading to show values in each area. It does not resize areas to show population.
- Why not C: A reference map shows real locations and features like borders and cities. It does not resize countries by population.
- Why not D: A dot density map uses repeated dots to show amounts. It does not resize countries to show population.
- Why not E: Mercator stretches places near the poles. That would make Canada look bigger, not smaller.

Vocab: cartogram, thematic map

### U1-P05
Topic 1.1 · IMP-1.A · Skill 1.E · hard

An airline planner wants one map that shows the correct distance and direction from the airline's hub airport to cities around the world. Which map projection would serve this purpose best?

- **A.** A Mercator projection, which keeps compass bearings constant along straight lines
- **B.** A Gall-Peters projection, which shows the true relative sizes of the continents
- **C.** A Robinson projection with the hub airport placed near the map's center
- **D.** A Goode's homolosine projection, which interrupts the oceans to reduce distortion of land
- **E.** An azimuthal equidistant projection centered on the hub airport

**Answer: E**

Explanation: An azimuthal equidistant map keeps distance and direction true from its center point. With the hub airport at the center, the planner can measure the distance and direction from the hub to any city. Distances between two places away from the center are generally not true, but the planner only needs routes from the hub.

- Why not A: Mercator keeps compass bearings, which helps sailors, but its distances are badly stretched toward the poles.
- Why not B: Gall-Peters keeps area true, but it distorts distances and shapes, so it cannot measure routes from the hub.
- Why not C: Robinson is a compromise map. Putting the hub near the center does not make distance or direction from the hub exactly right.
- Why not D: Goode's map keeps relative area true, but its cuts and distance distortion make it a poor choice for measuring routes from the hub.

Vocab: azimuthal equidistant projection, Mercator projection, Gall-Peters projection, Robinson projection

### U1-P06
Topic 1.1 · IMP-1.A · Skill 3.D · medium

**Stimulus (table): NEW BUSINESSES OPENED IN FIVE COUNTIES OF STATE Q, 2025 (HYPOTHETICAL DATA)**

| County | Population | New businesses opened |
|---|---|---|
| Adams | 820,000 | 2,870 |
| Baker | 60,000 | 480 |
| Cole | 150,000 | 900 |
| Dunn | 300,000 | 1,350 |
| Ellis | 45,000 | 135 |

Description: A table listing the population and the number of new businesses opened in 2025 for five counties: Adams, Baker, Cole, Dunn, and Ellis.

Source: Hypothetical data

A student wants to make a choropleth map of new business openings relative to population, using darker shading for higher values. Based on the table, which county should be shaded darkest?

- **A.** Adams County
- **B.** Baker County
- **C.** Cole County
- **D.** Dunn County
- **E.** Ellis County

**Answer: B**

Explanation: To compare openings relative to population, divide each county's new businesses by its number of residents. Baker had 480 openings for 60,000 residents. That is 8.0 per 1,000 residents, the highest rate. Adams has the largest total, but its rate is only 3.5 per 1,000.

- Why not A: Adams has the biggest total (2,870), but it has 820,000 people. That is only 3.5 per 1,000 residents.
- Why not C: Cole's rate is 6.0 per 1,000 residents. That is second highest, but below Baker's 8.0.
- Why not D: Dunn's rate is 4.5 per 1,000 residents, lower than Baker's.
- Why not E: Ellis is the smallest county, but its rate is only 3.0 per 1,000 residents, the lowest of the five.

Vocab: choropleth map, rate, per capita

### U1-P34
Topic 1.1 · IMP-1.A · Skill 3.B · easy

**Stimulus (schematicMap): FARMHOUSES IN VALLEY V (HYPOTHETICAL)**

Legend: [house] Farmhouse; [water] River

Description: Each house symbol stands for one farmhouse. A river crosses the valley from west to east. North is at the top.

Source: Hypothetical map

Which of the following best describes the spatial pattern of farmhouses shown on the map?

- **A.** Clustered around one central village
- **B.** Dispersed evenly across the whole valley
- **C.** Concentrated on the north bank of the river
- **D.** Linear, following the course of the river
- **E.** Scattered with no link to physical features

**Answer: D**

Explanation: A linear pattern means things are lined up along something long and narrow, like a river, road, or coast. Here the farmhouses form two lines, one on each bank, and follow the river's bends across the valley.

- Why not A: There is no central village. The houses stretch from one side of the map to the other.
- Why not B: A dispersed pattern spreads things out across the whole area. Here the houses stay close to the river, and the land away from it is empty.
- Why not C: Twelve houses stand on each bank, so they are not concentrated on the north bank.
- Why not E: The houses follow the river closely, so the pattern is clearly linked to a physical feature.

Vocab: linear pattern, clustered, dispersed, spatial pattern

### U1-P08
Topic 1.2 · IMP-1.B · Skill 1.D · easy

A city planner uses a computer program to stack map layers showing roads, flood zones, school locations, and population density, and then analyzes how the layers relate to one another. This tool is best described as

- **A.** remote sensing from satellites
- **B.** a satellite navigation system such as GPS
- **C.** a national census of population
- **D.** a geographic information system
- **E.** an aerial photograph of the city

**Answer: D**

Explanation: A geographic information system (GIS) is computer software that stores map data in layers. The planner can stack layers, like roads on top of flood zones, to see how they relate. GIS is the tool for analyzing. GPS and remote sensing are ways of collecting data that often go into a GIS.

- Why not A: Remote sensing collects images or data from far away, such as from satellites. It gathers data but is not the layering tool.
- Why not B: GPS finds a precise location. It collects location data but does not stack and analyze layers.
- Why not C: A census counts people and households. Its data can be one layer in a GIS, but it is not the tool itself.
- Why not E: An aerial photo is one picture. It cannot hold and compare several layers of data.

Vocab: geographic information system (GIS), layer, geospatial technology

### U1-P09
Topic 1.2 · IMP-1.B · Skill 1.D · easy

Scientists compare images of a mountain glacier taken from satellites in 1990, 2005, and 2020 to measure how much the ice has shrunk. Which method of collecting geographic data are they using?

- **A.** Field observation
- **B.** Satellite navigation (GPS)
- **C.** Remote sensing
- **D.** A population census
- **E.** Personal interviews

**Answer: C**

Explanation: Remote sensing means gathering information about Earth's surface from a distance, usually with satellites, airplanes, or drones. Comparing satellite images from different years shows change over time, like a glacier getting smaller.

- Why not A: Field observation means going to the place and recording what you see in person. These scientists used images taken from space.
- Why not B: GPS satellites send signals that pinpoint a location. They do not take pictures of the glacier.
- Why not D: A census counts people, not ice.
- Why not E: Interviews collect people's words and opinions, not measurements of a glacier's size.

Vocab: remote sensing, satellite imagery

### U1-P11
Topic 1.2 · IMP-1.B · Skill 3.A · medium

**Stimulus (table): DATA GATHERED TO PLAN A NEW BUS ROUTE IN CITY P (HYPOTHETICAL)**

| Data set | What it contains |
|---|---|
| 1 | Number of residents age 65 and older in each census tract, from the national census |
| 2 | Notes from interviews with riders waiting at bus stops |
| 3 | Images taken from aircraft and satellites showing where new apartment buildings were built |
| 4 | Position of each city bus, recorded automatically every 30 seconds by a receiver on board |
| 5 | One computer map that overlays data sets 1 through 4 so planners can compare them |

Description: A table describing five data sets a city collected to plan a new bus route.

Source: Hypothetical data

Which data set was collected using a satellite navigation system?

- **A.** Data set 1
- **B.** Data set 2
- **C.** Data set 3
- **D.** Data set 4
- **E.** Data set 5

**Answer: D**

Explanation: A satellite navigation system, like GPS, uses signals from satellites to estimate a receiver's location. The receiver on each bus can record where the bus is every 30 seconds. That is Data set 4.

- Why not A: Data set 1 comes from a census, which counts people where they live.
- Why not B: Data set 2 comes from interviews, a field method that gathers people's words.
- Why not C: Data set 3 comes from remote sensing. Satellites took pictures, but they did not find the position of a receiver.
- Why not E: Data set 5 is a GIS, a tool that layers and analyzes data collected in other ways.

Vocab: GPS, satellite navigation system, remote sensing, GIS

### U1-P10
Topic 1.2 · IMP-1.B · Skill 1.D · medium

A geographer wants to learn how longtime residents feel about the changes a new highway brought to their neighborhood. Which source would provide the most useful information?

- **A.** Satellite images of the neighborhood before and after the highway was built
- **B.** GPS data showing the average speed of cars on the highway
- **C.** Census tables showing the neighborhood's population in each decade
- **D.** A GIS layer showing property values along the highway
- **E.** Recorded interviews with people who have lived there for decades

**Answer: E**

Explanation: Feelings and opinions are qualitative information. The best way to get them is to ask people. Personal interviews are one of the sources of spatial information your AP course guide lists. Images, GPS, census tables, and GIS layers give numbers or pictures, but they cannot tell you how residents feel.

- Why not A: Satellite images show physical changes, like new pavement, but not how people feel about them.
- Why not B: GPS speed data tell how fast cars move, not what residents think.
- Why not C: Census tables count people. They show who lives there, not their opinions.
- Why not D: Property values are numbers. They might hint at change, but they do not record residents' feelings.

Vocab: qualitative data, quantitative data, interview

### U1-P35
Topic 1.2 · IMP-1.B · Skill 1.D · medium

A geographer wants to find out which ground-floor storefronts on one downtown street are open for business, empty, or being renovated this month. Which method would collect the most accurate information?

- **A.** Walking the street and recording what is in each storefront
- **B.** Reviewing satellite images of the downtown rooftops
- **C.** Tracking delivery trucks on the street with GPS receivers
- **D.** Mapping the street's property values from tax records
- **E.** Counting the street's residents with the most recent national census

**Answer: A**

Explanation: Field observation means going to a place and recording what you see. Walking the street lets the geographer check every storefront this month. Census counts, satellite pictures, GPS tracks, and tax records cannot show whether each store is open, empty, or being fixed up right now.

- Why not B: Rooftop images cannot show whether a store is open, empty, or being renovated inside.
- Why not C: Delivery routes might hint at which stores get goods, but they do not record the condition of every storefront.
- Why not D: Property values do not show whether a store is open, empty, or being renovated right now.
- Why not E: A census counts people where they live, usually once every ten years. It does not record whether each store is open this month.

Vocab: field observation, qualitative data

### U1-P14
Topic 1.3 · IMP-1.C · Skill 4.C · medium

**Stimulus (schematicMap): FLOOD RISK AND BUILDINGS ALONG THE RIVER, COUNTY T (HYPOTHETICAL GIS MAP)**

Labels on map: Higher ground; 100-year floodplain; Higher ground

Legend: [power] Area covered by the 1%-annual-chance flood, often called the 100-year floodplain; [small] Higher ground; [water] River; [house] Home; [baseS] School; [baseN] Hospital

Description: The map combines building locations with the mapped 1%-annual-chance floodplain. North is at the top.

Source: Hypothetical map

County planners made this map in a GIS by combining a flood-risk layer with the locations of buildings. Which decision is best supported by the map?

- **A.** Building a levee along the east bank to protect the hospital
- **B.** Moving the school out of the shaded zone onto higher ground
- **C.** Moving the homes at the far west edge out of the shaded zone
- **D.** Moving the hospital out of the shaded zone onto higher ground
- **E.** Requiring flood insurance for the homes on higher ground east of the river

**Answer: B**

Explanation: The school is inside the mapped floodplain. A flood this big or bigger has a 1 percent chance of happening in any given year. Moving the school to higher ground outside this area would lower its risk from river floods.

- Why not A: The hospital is outside the mapped floodplain, while the school is inside it. The map points to protecting the school first.
- Why not C: The three homes at the far west edge stand on higher ground, outside the shaded floodplain. The school is inside it.
- Why not D: The hospital already stands on higher ground east of the river, outside the shaded floodplain. The school is inside it.
- Why not E: These homes are outside the mapped floodplain. Places outside it can still flood, but the map shows the school at much greater risk.

Vocab: floodplain, GIS, layer

### U1-P13
Topic 1.3 · IMP-1.C · Skill 2.C · medium

A coffee company uses GIS to compare traffic counts, the locations of competing shops, and the incomes and ages of residents in each neighborhood before choosing where to open new stores. Which outcome is most likely?

- **A.** New stores are spaced evenly across the city, one in each neighborhood
- **B.** New stores are concentrated in neighborhoods with the lowest property costs
- **C.** New stores are located where customer traits and access suggest strong demand
- **D.** New stores are placed far from busy roads so customers can avoid traffic
- **E.** New stores are located in the census tracts with the greatest total population

**Answer: C**

Explanation: GIS lets the company layer information about customers, traffic and access, and competing shops. Putting these layers together helps it choose places where many likely customers can easily reach a store. The data do not call for spacing stores evenly or choosing the cheapest land.

- Why not A: Even spacing is not what the data point to. Demand, access, and competition differ from one neighborhood to another.
- Why not B: Cheap property is only one factor. The company is weighing customers, traffic, and competitors together.
- Why not D: Putting stores far from busy routes could make them harder for likely customers to reach.
- Why not E: Population is only one factor. The company also weighs traffic and competitors, so total population alone would not decide.

Vocab: GIS, geospatial data

### U1-P15
Topic 1.3 · IMP-1.C · Skill 1.D · medium

After an earthquake, a relief organization compares satellite images taken before and after the disaster to find blocked roads and damaged neighborhoods. How does this geographic data most directly help the organization?

- **A.** It shows how residents feel about the government's response to the disaster
- **B.** It predicts when and where the next earthquake in the region will strike
- **C.** It counts how many people were living in each damaged building
- **D.** It shows which damaged buildings were built before the city's earthquake building code
- **E.** It helps decide where to send supplies and which roads trucks can use

**Answer: E**

Explanation: Comparing 'before' and 'after' satellite images shows what changed: which roads are blocked and which neighborhoods are damaged. Relief groups use that to plan where to send food, water, and medicine and which roads trucks can still use. This is an organization using geographic data to make decisions.

- Why not A: Images show physical damage, not people's opinions. Interviews would be needed for that.
- Why not B: Satellite images show what already happened. They cannot predict when the next earthquake will strike.
- Why not C: Images alone do not show how many people lived in each building. Occupancy records or checks on the ground would be needed.
- Why not D: Satellite images show damage, not when a building was built or what rules it followed. City records would be needed for that.

Vocab: remote sensing, satellite imagery

### U1-P12
Topic 1.3 · IMP-1.C · Skill 3.D · medium

**Stimulus (bar): CHILDREN UNDER AGE 5 BY NEIGHBORHOOD, CITY V, 2010 AND 2020 CENSUS (HYPOTHETICAL DATA)**

Bar chart (y-axis: Children under age 5; max 1600).

| Category | 2010 | 2020 |
|---|---|---|
| Riverside | 650 | 1480 |
| Oak Hill | 1200 | 1050 |
| Midtown | 400 | 520 |
| Westfield | 900 | 1120 |
| Lakeview | 700 | 610 |

Description: A grouped bar chart of the number of children under age 5 in five neighborhoods in 2010 and 2020. Riverside: 650 and 1,480. Oak Hill: 1,200 and 1,050. Midtown: 400 and 520. Westfield: 900 and 1,120. Lakeview: 700 and 610.

Source: Hypothetical data

A school district plans to build one new elementary school where the number of young children is growing fastest. Based on the census data in the chart, which neighborhood is the best location?

- **A.** Riverside
- **B.** Oak Hill
- **C.** Midtown
- **D.** Westfield
- **E.** Lakeview

**Answer: A**

Explanation: Riverside's number of children under 5 more than doubled, from 650 to 1,480. That is both the biggest increase and the largest total in 2020. If other things are similar, these children point to the fastest-growing need for elementary school seats. This is how census data guide government decisions.

- Why not B: Oak Hill had the most young children in 2010, but its number fell by 2020 (1,200 to 1,050).
- Why not C: Midtown grew a little (400 to 520), but it still has the fewest young children.
- Why not D: Westfield grew (900 to 1,120), but Riverside grew far more and now has more young children.
- Why not E: Lakeview's number of young children fell (700 to 610).

Vocab: census, geospatial data

### U1-P17
Topic 1.4 · PSO-1.A · Skill 3.D · medium

**Stimulus (bar): SHARE OF A GROCERY STORE'S WEEKLY CUSTOMERS, BY DISTANCE FROM HOME TO THE STORE (HYPOTHETICAL DATA)**

Bar chart (y-axis: Percent of weekly customers; max 50).

| Category | Share of customers (%) |
|---|---|
| Under 1 km | 41 |
| 1–2 km | 26 |
| 2–3 km | 16 |
| 3–4 km | 10 |
| 4–5 km | 7 |

Description: A bar chart. Of the store's weekly customers, 41 percent live less than 1 km away, 26 percent live 1–2 km away, 16 percent live 2–3 km away, 10 percent live 3–4 km away, and 7 percent live 4–5 km away.

Source: Hypothetical data

Which pair of neighboring distance groups shows the largest drop in customer share, and which geographic pattern is that drop consistent with?

- **A.** From 1–2 km to 2–3 km; distance decay
- **B.** From 2–3 km to 3–4 km; time-space compression
- **C.** From under 1 km to 1–2 km; distance decay
- **D.** From 3–4 km to 4–5 km; time-space compression
- **E.** From under 1 km to 1–2 km; environmental determinism

**Answer: C**

Explanation: The share drops from 41% in the nearest group to 26% in the next group. That is a drop of 15 percentage points. The other drops are 10, 6, and 3 points. Fewer customers coming from farther away fits distance decay: interaction with a place tends to fall as distance grows. The chart alone cannot show every cause, such as how many people live in each group or where other stores are.

- Why not A: This drop is 10 percentage points (26 to 16), smaller than the 15-point drop between the two nearest groups.
- Why not B: This drop is only 6 points (16 to 10). Also, the chart shows nothing about faster travel or new technology.
- Why not D: This drop is only 3 points (10 to 7). Also, the chart shows nothing about faster travel or new technology.
- Why not E: This is the largest drop, but nothing in the chart shows the physical environment controlling what people do.

Vocab: distance decay, percentage point

### U1-P16
Topic 1.4 · PSO-1.A · Skill 1.A · easy

Which of the following describes the absolute location of a place?

- **A.** It is at 32.8° N latitude, 96.8° W longitude.
- **B.** It is about 50 kilometers south of the state capital.
- **C.** It is on the east bank of the river, across from the old mill.
- **D.** It is a two-hour drive from the nearest seaport.
- **E.** It is next to the main highway, halfway between two large cities.

**Answer: A**

Explanation: Absolute location names a place's exact position, using coordinates like latitude and longitude, or an address. The latitude and longitude in A pin down one spot on Earth. The other choices describe where a place is compared to something else. That is relative location.

- Why not B: Distance from the capital compares the place to another place, so it is relative location.
- Why not C: 'Across from the old mill' is relative location. You have to know where the mill is.
- Why not D: Driving time to a seaport is relative location, and it can change if roads change.
- Why not E: 'Halfway between two cities' is relative location.

Vocab: absolute location, relative location, latitude, longitude

### U1-P19
Topic 1.4 · PSO-1.A · Skill 1.D · medium

A geographer describes a town's hilly landscape, its brick houses, the language its residents speak, and its yearly harvest festival. The geographer is describing the town's

- **A.** absolute location
- **B.** place
- **C.** relative location
- **D.** site
- **E.** space

**Answer: B**

Explanation: In geography, place means the mix of physical and human features that makes a location special: its landforms and climate plus its buildings, language, and traditions. This description covers both kinds of features, so it is about place.

- Why not A: Absolute location is an exact position, like latitude and longitude. The description gives no coordinates.
- Why not C: Relative location tells where a town is compared to other places. The description never mentions other places.
- Why not D: Site is the physical setting, like hills and rivers. This description also includes language and a festival, which are human features.
- Why not E: Space is about the area between things and how things are arranged in it, not the special character of one town.

Vocab: place, space, site

### U1-P20
Topic 1.4 · PSO-1.A · Skill 2.B · hard

For centuries, Port Q was a small fishing harbor. After a canal opened nearby, ships traveling between two oceans began passing Port Q, and it grew into a major trading city. Which concept best explains this change?

- **A.** Its absolute location changed when the canal was dug
- **B.** Its site changed, because the canal altered the physical land of the harbor
- **C.** Environmental determinism, since the harbor's natural depth decided its future
- **D.** Its sense of place, such as its language and customs, began attracting traders
- **E.** Its relative location improved because it now sat on a busy trade route

**Answer: E**

Explanation: Relative location is where a place is compared to other places and routes. Port Q never moved, so its latitude and longitude stayed the same. But the canal put Port Q right on a busy shipping route. Its location compared to world trade became much better, and that is why it grew.

- Why not A: Absolute location (latitude and longitude) does not change. The harbor stayed in the same spot.
- Why not B: Site is the physical setting of the harbor itself. The canal was built nearby. What changed was the port's connection to other places.
- Why not C: The harbor's natural setting was the same before and after. A human-built canal made the difference.
- Why not D: Nothing in the story says the town's culture changed. Growth came from ships now passing by.

Vocab: relative location, absolute location, site, situation

### U1-P18
Topic 1.4 · PSO-1.A · Skill 3.E · medium

**Stimulus (table): FASTEST COMMON TRAVEL TIME BETWEEN PORT CITY A AND INLAND CITY B (HYPOTHETICAL DATA)**

| Year | Fastest common way to travel | Travel time |
|---|---|---|
| 1820 | Horse-drawn coach | 12 days |
| 1880 | Steam railroad | 30 hours |
| 1950 | Car on a paved highway | 9 hours |
| 2020 | Commercial airplane | 1.5 hours |

Description: A table of the fastest common travel time between two cities in four years: 12 days in 1820, 30 hours in 1880, 9 hours in 1950, and 1.5 hours in 2020.

Source: Hypothetical data

Which concept is best illustrated by the trend in the table?

- **A.** Distance decay, because the two cities interact less as time passes
- **B.** Absolute distance, because the distance between the cities has shrunk
- **C.** Environmental determinism, because terrain controls the travel time
- **D.** Time-space compression, because new technology shrinks travel time
- **E.** Flows, because the table counts the travelers moving between the cities

**Answer: D**

Explanation: Time-space compression means places feel closer together because new technology makes travel and communication faster. The two cities never moved, but the trip shrank from 12 days to 1.5 hours.

- Why not A: Distance decay is about how interaction changes with distance. This table gives travel times between the same two cities, not interaction at different distances.
- Why not B: Absolute distance, measured in kilometers, did not change. Only the travel time did.
- Why not C: The table links shorter trips to new transportation technology. It does not show the environment controlling how people live.
- Why not E: The table shows how long the trip takes, not how many people or goods move between the cities.

Vocab: time-space compression, absolute distance, relative distance

### U1-P23
Topic 1.5 · PSO-1.B · Skill 1.A · easy

Which of the following correctly pairs a renewable resource with a nonrenewable resource?

- **A.** Renewable: natural gas; nonrenewable: solar energy
- **B.** Renewable: wind; nonrenewable: coal
- **C.** Renewable: oil; nonrenewable: natural gas
- **D.** Renewable: solar energy; nonrenewable: wind
- **E.** Renewable: coal; nonrenewable: oil

**Answer: B**

Explanation: A renewable resource is replaced by nature fast enough to keep using it, like wind and sunlight. Coal, oil, and natural gas are fossil fuels that took millions of years to form, so they are nonrenewable. Only choice B puts both resources in the right group.

- Why not A: Natural gas took millions of years to form, so it is nonrenewable. Sunlight comes back every day, so solar energy is renewable.
- Why not C: Oil is a fossil fuel that took millions of years to form, so it is nonrenewable, not renewable.
- Why not D: Wind keeps blowing, so it is renewable. Both of these resources are renewable.
- Why not E: Coal is a fossil fuel that took millions of years to form, so it is nonrenewable, not renewable.

Vocab: natural resources, renewable resource, nonrenewable resource, fossil fuel

### U1-P22
Topic 1.5 · PSO-1.B · Skill 1.B · medium

In the Netherlands, people built dikes and pumped water out of shallow seas and lakes to create new farmland called polders. Which concept does this best illustrate?

- **A.** Environmental determinism, because the low, wet land forced the Dutch to become farmers
- **B.** Environmental determinism, because the sea set the limits of where people could live
- **C.** Possibilism, because people used technology to work around an environmental limit
- **D.** Sustainability, because the drained land went back to its natural condition
- **E.** Distance decay, because the new farmland was created close to growing cities

**Answer: C**

Explanation: Possibilism says the environment sets limits and offers choices, and people decide what to do using their technology and culture. The Dutch faced low land and water, but they built dikes and pumps to make new farmland. People shaped the result; the environment did not decide it for them.

- Why not A: The story is about people's decisions and technology changing how low, wet land could be used. It does not show nature forcing one outcome.
- Why not B: The sea did limit land use, but human choices and engineering changed what was possible. That goes against determinism.
- Why not D: Draining seas and lakes changed the wetland and coastal environment. The question does not say whether that change can last over the long term, and the land did not go back to its natural state.
- Why not E: The story is about turning water into land, not about how interaction drops off with distance.

Vocab: possibilism, polder, environmental determinism

### U1-P25
Topic 1.5 · PSO-1.B · Skill 3.C · medium

**Stimulus (bar): DEPTH TO GROUNDWATER IN AN ARID AGRICULTURAL REGION, 1980–2020 (HYPOTHETICAL DATA)**

Bar chart (y-axis: Meters below the surface; max 60).

| Category | Depth to groundwater (meters below the surface) |
|---|---|
| 1980 | 20 |
| 1990 | 28 |
| 2000 | 37 |
| 2010 | 47 |
| 2020 | 58 |

Note under chart: Farms in the region water their crops with groundwater pumped from wells. The amount of rain that soaks down to refill the aquifer each year stayed about the same from 1980 to 2020.

Description: A bar chart of the average depth to groundwater: 20 meters below the surface in 1980, 28 in 1990, 37 in 2000, 47 in 2010, and 58 in 2020.

Source: Hypothetical data

Which conclusion about human–environment interaction is best supported by the chart and the note below it?

- **A.** The water table is rising, so farmers could pump more each year
- **B.** The dry climate controls how much water farms use, which supports environmental determinism
- **C.** Groundwater is a nonrenewable resource, like coal, so pumping it uses it up
- **D.** The rising depth numbers show that irrigation in the region can continue at its current rate
- **E.** The falling water table raises doubts that current groundwater use is sustainable

**Answer: E**

Explanation: The water is farther below the surface every decade. From 1980 to 2020, the water table fell 38 meters (from 20 to 58 meters down). Rain still refills the aquifer at about the same rate, so the water being taken out each year is more than what comes back in. If that keeps going, wells could run dry, so the current use may not be sustainable. The chart does not measure the pumping itself.

- Why not A: A bigger depth number means the water is farther down. The water table is falling, not rising.
- Why not B: Determinism says the environment controls how people live. This example is about how people's water use is changing the environment.
- Why not C: The note says rain refills this aquifer. Some aquifers refill very slowly, but groundwater is not always nonrenewable like coal.
- Why not D: A water table that keeps falling is a warning sign. It does not show that pumping can go on at the same rate.

Vocab: sustainability, aquifer, natural resources, water table

### U1-P24
Topic 1.5 · PSO-1.B · Skill 1.E · hard

Which of the following is the strongest criticism geographers make of environmental determinism?

- **A.** It gives too much credit to human technology and too little to the physical environment
- **B.** It focuses on local places and cannot be applied to whole world regions
- **C.** It was built to explain cities, so it cannot be applied to rural areas
- **D.** It ignores human choice and was used to rank some societies above others
- **E.** It overlooks climate, which has little effect on where people live or how they farm

**Answer: D**

Explanation: Environmental determinism says climate and landforms control how people act. Geographers reject it because people make choices using their culture and technology. It was also used in the past to rank some societies above others, which helped people justify colonialism and racism. That is why possibilism replaced it.

- Why not A: That points the wrong way. Determinism gives too much weight to the environment, not to technology.
- Why not B: Determinists did apply the idea to whole world regions, for example by claiming climate shaped entire civilizations.
- Why not C: Determinists applied the idea to whole societies, rural and urban alike. The real problem is that it ignores human choice.
- Why not E: Climate does affect people, for example which crops they can grow. The problem is claiming that it controls them.

Vocab: environmental determinism, possibilism

### U1-P21
Topic 1.5 · PSO-1.B · Skill 1.A · easy

Which of the following best describes environmental determinism?

- **A.** The idea that climate and landforms control how human societies develop
- **B.** The idea that people can choose among several ways to use their environment
- **C.** The idea that resources should be used so future generations can also meet their needs
- **D.** The idea that interaction between places declines as the distance between them increases
- **E.** The idea that new technology makes distant places feel closer together

**Answer: A**

Explanation: Environmental determinism is an old idea that the physical environment, like climate and landforms, controls what people do and how societies develop. Geographers today reject it. Possibilism replaced it: the environment sets limits, but people make choices.

- Why not B: That is possibilism, the idea that replaced environmental determinism.
- Why not C: That is sustainability.
- Why not D: That is distance decay, a spatial concept.
- Why not E: That is time-space compression.

Vocab: environmental determinism, possibilism

### U1-P28
Topic 1.6 · PSO-1.D · Skill 5.B · hard

World population is still growing. Country Z's population is shrinking. Yet the population of Country Z's capital city is growing quickly. Which statement best explains how these patterns can all be true at once?

- **A.** The three numbers conflict, so at least one data source is probably inaccurate
- **B.** The capital grows because world population growth is shared equally among cities
- **C.** Migration within Country Z could be shifting people from rural areas to the capital
- **D.** Country Z's shrinking population shows that world population is about to fall
- **E.** The capital's growth will soon make Country Z's national population grow again

**Answer: C**

Explanation: Different things can happen at different scales. Worldwide, births still outnumber deaths. Country Z may have few births or many people leaving, so it shrinks. But inside Country Z, many people may be moving from the countryside to the capital for jobs, so the capital grows. Looking at only one scale would miss part of the story.

- Why not A: The numbers do not conflict. Each scale can show a different trend at the same time.
- Why not B: Population growth is not shared out equally. Some places grow while others shrink.
- Why not D: One country shrinking says little about the world total, since many other countries are still growing.
- Why not E: People moving to the capital from elsewhere in Country Z do not add to the national total.

Vocab: scale of analysis, rural-to-urban migration

### U1-P26
Topic 1.6 · PSO-1.C · Skill 5.A · easy

A world map shades each country by that country's average life expectancy. At which scale are the life-expectancy data aggregated (grouped) on this map?

- **A.** National, because each mapped value summarizes one country
- **B.** Regional, because neighboring countries may have similar life expectancies
- **C.** Global, because the display includes countries throughout the world
- **D.** Local, because life expectancy is calculated from records about individuals
- **E.** Regional, because each country belongs to a larger world region

**Answer: A**

Explanation: The map covers the whole world, but each color shows one country's average. So the data are grouped at the national scale. The area a map shows (here, the world) and the level at which its data are grouped (here, countries) are two different things.

- Why not B: Neighboring countries may look alike, but each value on the map still summarizes one country.
- Why not C: Global describes the area the map shows. The map does not combine all countries into one worldwide number.
- Why not D: Records about people were combined into country averages. No individual or neighborhood values are shown.
- Why not E: The map shows a value for each country, not one average for each larger world region.

Vocab: scale of analysis, national scale, aggregated data

### U1-P27
Topic 1.6 · PSO-1.D · Skill 5.C · medium

**Stimulus (table): UNEMPLOYMENT IN COUNTRY X AND ITS FOUR REGIONS, 2025 (HYPOTHETICAL DATA)**

| Area | Labor force (millions) | Unemployment rate (%) |
|---|---|---|
| Country X (national) | 10.0 | 6.0 |
| North region | 4.0 | 3.5 |
| East region | 3.0 | 4.0 |
| South region | 2.0 | 13.0 |
| West region | 1.0 | 8.0 |

Description: A table of the labor force and unemployment rate for Country X as a whole and for each of its four regions.

Source: Hypothetical data

Which conclusion can be drawn from the regional-scale data that could NOT be drawn from the national-scale data alone?

- **A.** Unemployment in Country X is higher than in its neighboring countries
- **B.** High unemployment is concentrated in the South, which the national rate hides
- **C.** Country X's overall unemployment rate is 6.0 percent
- **D.** Unemployment is spread fairly evenly across Country X's regions
- **E.** The North has the most unemployed workers because it has the largest labor force

**Answer: B**

Explanation: The national rate (6.0%) is an average for the whole country. At the regional scale, you can see the South's rate is 13.0%, more than twice the national rate, while the North's is only 3.5%. Changing the scale shows a pattern that the single national number hides.

- Why not A: The table has no data on other countries, so it cannot support a comparison with neighbors.
- Why not C: The 6.0% rate is in the national row, so you would know it without the regional data.
- Why not D: The rates range from 3.5% to 13.0%, so they are far from even.
- Why not E: The North has 4.0 million × 3.5% = 140,000 unemployed. The South has 2.0 million × 13.0% = 260,000. The South has more.

Vocab: scale of analysis, regional scale, national scale

### U1-P29
Topic 1.6 · PSO-1.C · Skill 5.A · medium

A researcher wants to explain why residents of one city neighborhood must travel much farther than residents of other neighborhoods to reach a full-service grocery store. Which scale of analysis is most appropriate for this study?

- **A.** Global, because food is traded among countries around the world
- **B.** Regional, because grocery chains operate across several countries
- **C.** National, because national laws decide where stores may open
- **D.** National, because the census collects neighborhood data for the whole country
- **E.** Local, because the question compares neighborhoods within one city

**Answer: E**

Explanation: Pick the scale that matches the question. This study compares neighborhoods inside one city, so it needs local data on where stores are and how far residents travel. National rules or world food markets might help explain the differences, but they cannot replace the neighborhood-by-neighborhood comparison.

- Why not A: World food markets can affect local conditions, but global data alone would not show the differences between neighborhoods.
- Why not B: Chains may cross borders, but the question is about differences between neighborhoods in one city.
- Why not C: National policies can affect where stores open, but this question needs data that tell neighborhoods within the city apart.
- Why not D: The census does collect neighborhood data across the country, but this study compares neighborhoods in one city, which is the local scale.

Vocab: local scale, scale of analysis, food desert

### U1-P36
Topic 1.6 · PSO-1.D · Skill 3.F · medium

County R's average household income rose by 10 percent from 2015 to 2025. Which statement about this county-level figure is most accurate?

- **A.** It shows that incomes rose in each of the county's neighborhoods
- **B.** It shows that the poorest households gained the most income
- **C.** It cannot show a change for the county, since an average hides the differences
- **D.** It shows that the county's income grew faster than the nation's
- **E.** It cannot show whether incomes rose or fell in each neighborhood

**Answer: E**

Explanation: A county average is one number for the whole county. Some neighborhoods may have gained a lot, and others may have lost. To see those differences, you need data grouped at a finer level, such as neighborhoods. One scale can hide what happens at another.

- Why not A: An average can rise even if some neighborhoods lost income, so it cannot show that each neighborhood gained.
- Why not B: An average does not show which households gained. The gains could have gone mostly to richer households.
- Why not C: The county average does show a change for the county as a whole: a 10 percent rise. What it cannot show is how that change differed from place to place.
- Why not D: The statement gives no national data, so it cannot be compared with the nation.

Vocab: scale of analysis, aggregated data, average

### U1-P32
Topic 1.7 · SPS-1.A · Skill 3.C · medium

**Stimulus (table): SHARE OF RESIDENTS WHO SAY THEY LIVE "UP NORTH," SIX COUNTIES OF STATE K (HYPOTHETICAL SURVEY DATA)**

| County | Distance north of the state capital (km) | Residents who say they live "Up North" (%) |
|---|---|---|
| Alder | 40 | 6 |
| Birch | 90 | 22 |
| Cedar | 140 | 47 |
| Dogwood | 190 | 71 |
| Elm | 240 | 88 |
| Fir | 290 | 95 |

Description: A table of six counties, from south to north, with the share of residents in each who say they live "Up North": Alder 6 percent, Birch 22, Cedar 47, Dogwood 71, Elm 88, and Fir 95.

Source: Hypothetical data

Which statement about the region called "Up North" is best supported by the data?

- **A.** It is a formal region with a sharp border between Birch and Cedar counties
- **B.** It is a functional region centered on the state capital
- **C.** It is a perceptual region whose edge is a gradual transition zone
- **D.** It is a formal region, because the survey measured residents' answers with numbers
- **E.** It is a perceptual region that begins sharply at the state capital

**Answer: C**

Explanation: "Up North" is a perceptual (vernacular) region: it depends on how people see the place where they live. The share who say they live "Up North" rises little by little from county to county, from 6% to 95%, and people in the same county disagree. So there is no one border everyone accepts; the edge is a broad transition zone.

- Why not A: The survey does not show an agreed border between Birch and Cedar. Answers are split inside both counties, and the share keeps rising across several counties.
- Why not B: Nothing in the table shows trips or connections to the capital. The region is defined by what people say about where they live.
- Why not D: Putting numbers on people's opinions does not make a region formal. The region is still based on how people see it, so it is perceptual.
- Why not E: The table does not show a shared border at the capital. Even in Alder, closest to the capital, only 6% say they live "Up North," and the share rises slowly to the north.

Vocab: perceptual region, vernacular region, transition zone

### U1-P33
Topic 1.7 · SPS-1.A · Skill 1.B · hard

Mexico is often placed in North America, in Latin America, and in a free-trade bloc with the United States and Canada. Which statement best explains why one country can belong to all three regions?

- **A.** Regions are set by international law, and each country is assigned to several of them
- **B.** Each region is defined by a different criterion, so regions can overlap
- **C.** Mexico's borders have shifted, moving it from one region to another over time
- **D.** Latin America and North America are the same region with two different names
- **E.** Mexico belongs to whichever region its absolute location places it in

**Answer: B**

Explanation: Geographers define regions by choosing what ties places together. North America is a continent, a physical landmass. Latin America is based on culture and history, such as languages that came from Latin, like Spanish and Portuguese. The trade bloc is based on an economic agreement. Because each region uses a different trait, the same country can fit in all three. Regions can overlap.

- Why not A: Some regions, like trade blocs, are set up by agreements, but no single international rule assigns countries to every kind of region. These three groupings use different criteria.
- Why not C: Mexico belongs to all three regions at the same time today. This is not about borders moving.
- Why not D: North America is a continent. Latin America is a cultural region that also includes most of South America, so they are not the same.
- Why not E: Absolute location (latitude and longitude) cannot tell you a region based on culture or trade.

Vocab: region, formal region, overlapping regions

### U1-P31
Topic 1.7 · SPS-1.A · Skill 1.D · medium

The area from which a hospital draws most of its patients, centered on the hospital and fading with distance, is best described as a

- **A.** functional region, because it is organized around flows to a central node
- **B.** functional region, because its people share the same language and culture
- **C.** formal region, because its border is drawn on an official government map
- **D.** perceptual region, because its edges are fuzzy and fade with distance
- **E.** perceptual region, because patients feel loyal to their hospital

**Answer: A**

Explanation: A functional (nodal) region is held together by connections to a central point, called the node. Patients travel to the hospital, so the hospital is the node. Its pull is strongest nearby and weaker farther away, which is distance decay at work.

- Why not B: Sharing a language or culture defines a formal region. This region is defined by trips to the hospital.
- Why not C: The question defines this area by patients' trips to a hospital, not by a government's official boundary or a shared trait.
- Why not D: Many regions have fuzzy edges. This one is defined by flows to a central node, which makes it functional.
- Why not E: Feelings define perceptual regions, but this area is defined by where patients actually come from.

Vocab: functional region, nodal region, node

### U1-P30
Topic 1.7 · SPS-1.A · Skill 1.D · easy

An area in which a majority of residents speak French at home is best described as

- **A.** a functional region, organized around a central node
- **B.** a perceptual region, based on people's feelings and images
- **C.** a transition zone, where two regions blend together
- **D.** a formal region, defined by a shared measurable trait
- **E.** a cultural hearth, the place where a language began

**Answer: D**

Explanation: A formal region (also called a uniform region) is an area where people share one or more measurable traits, like a language. You can draw its borders using data, such as census counts of the language people speak at home.

- Why not A: A functional region is tied together by connections to a center, like a city's commuter zone. A shared language is a trait, not a connection.
- Why not B: A perceptual region exists in people's minds, like 'the South.' A language majority can be measured with data.
- Why not C: A transition zone is the fuzzy edge where regions blend. The question describes the region itself, not its edge.
- Why not E: A hearth is where something started. The question is about where French is spoken now, not where it began.

Vocab: formal region, uniform region

## Timed exam

Each of the questions or incomplete statements below is followed by five suggested answers or completions. Select the one that is best in each case. Your score is based only on the number of questions answered correctly, so answer every question. Work quickly without losing accuracy, and come back to any question you skipped if time allows.

### U1-E01 (Q1)
Topic 1.1 · IMP-1.A · Skill 3.A · easy

A geographer wants to map the percentage of residents age 65 or older in each county of a state. Which type of map is best suited to this purpose?

- **A.** Dot density map
- **B.** Graduated symbol map
- **C.** Choropleth map
- **D.** Isoline map
- **E.** Cartogram

**Answer: C**

Explanation: Choropleth maps color whole areas, like counties or states, by a rate or percentage. Darker usually means higher. The percent of residents age 65 or older in each county is a perfect fit.

- A: Incorrect. A dot density map shows counts, with each dot standing for a set number of people or things. It is not well suited to showing a percentage for each county.
- B: Incorrect. A graduated symbol map uses symbols of different sizes, usually to show totals at point locations such as cities, not percentages for whole areas.
- C: Correct. A choropleth map shades predefined areas, such as counties, by a rate or percentage, with darker shades usually showing higher values.
- D: Incorrect. An isoline map connects points of equal value, such as elevation or temperature, that vary continuously across space rather than by county.
- E: Incorrect. A cartogram resizes areas in proportion to a variable, which would distort the counties rather than shade them by percentage.

### U1-E06 (Q2)
Topic 1.2 · IMP-1.B · Skill 1.D · easy

A delivery app shows customers their driver's current position as the driver moves through the city. The app most directly relies on which geospatial technology to find the driver's position?

- **A.** A satellite navigation system such as GPS
- **B.** Remote sensing images taken by satellites
- **C.** A national census of population and housing
- **D.** Field interviews with drivers and customers
- **E.** A choropleth map of the city's neighborhoods

**Answer: A**

Explanation: GPS uses signals from satellites to estimate where a phone is. The driver's phone sends that location to the app, which shows it on a map.

- A: Correct. Satellite navigation systems such as the Global Positioning System (GPS) use signals from satellites to calculate a receiver's position, which the app can display in real time.
- B: Incorrect. Remote sensing gathers images or other data about Earth's surface from a distance; it does not track the position of a phone in a moving car.
- C: Incorrect. A census counts people and housing at set times; it cannot locate a moving driver.
- D: Incorrect. Interviews could not continuously estimate the location of a moving phone.
- E: Incorrect. A choropleth map shades areas by a rate or percentage; it does not track the position of anything.

### U1-E03 (Q3)
Topic 1.1 · IMP-1.A · Skill 4.D · medium · set: grids

*Questions 3–4 refer to the two map grids below.*

**Stimulus (schematicMap): TWO WORLD MAP GRIDS DRAWN AT THE SAME WIDTH**

Labels on map: Map 1; Map 2; 75° N; 45° N; 0°; 45° S; 75° S; 75° N; 45° N; 0°; 45° S; 75° S

Legend: [road] Equator (0°)

Description: Both grids show parallels (lines of latitude) at 15° intervals from 75° S to 75° N and meridians (lines of longitude) at 30° intervals. The dashed horizontal line is the equator.

Source: Grid spacing computed from two standard world map projection formulas

Which statement best describes how Map 1 differs from Map 2?

- **A.** Map 1 keeps the areas of high-latitude places accurate, while Map 2 enlarges them
- **B.** Map 1 is an azimuthal projection centered on a pole, while Map 2 is cylindrical
- **C.** Map 1 keeps distances true across the map, while Map 2 distorts distances
- **D.** Map 1 increasingly enlarges areas toward the poles; Map 2 keeps relative areas correct
- **E.** Map 1 and Map 2 distort area in the same way, since both show the same parallels

**Answer: D**

Explanation: Look at the gaps between the flat lines. On Map 1 the gaps get bigger near the poles, so places there get stretched taller as well as wider and look too big, like Greenland on a Mercator map. On Map 2 the gaps get smaller near the poles, which squeezes places back down so their areas stay correct, like on a Gall-Peters map.

- A: Incorrect. This reverses the two maps. On Map 1 the parallels spread farther apart toward the poles while the meridians stay the same distance apart, so high-latitude areas are enlarged.
- B: Incorrect. Both grids are cylindrical: their meridians are straight, parallel, and evenly spaced. An azimuthal polar projection would show meridians radiating from a central pole.
- C: Incorrect. Neither grid keeps distances true across the whole map; on both, every parallel is drawn as long as the equator, so east–west scale grows toward the poles.
- D: Correct. Map 1's spacing between parallels grows toward the poles, as on the Mercator projection, so high-latitude areas are enlarged. Map 2's spacing shrinks toward the poles, offsetting the east–west stretching so that relative areas stay correct, as on equal-area cylindrical projections such as the Gall-Peters.
- E: Incorrect. The grids show the same parallels, but the spacing between them differs, and that spacing determines how area is distorted.

### U1-E04 (Q4)
Topic 1.1 · IMP-1.A · Skill 4.F · hard · set: grids

Which statement best describes a limitation of Map 2?

- **A.** It enlarges the area of Canada and Russia compared with Brazil and India
- **B.** It flattens the shapes of high-latitude places, squeezing them north to south
- **C.** It keeps compass bearings as straight lines, so it is useful mainly for sea navigation
- **D.** It shows true distances from its center point but distorts areas elsewhere
- **E.** It is a compromise map with small distortions of area, shape, distance, and direction

**Answer: B**

Explanation: Every map projection gives something up. Map 2 keeps areas correct, but to do that it squishes places near the poles from top to bottom, so their shapes look flat and wide. You can trust Map 2 for comparing sizes, not shapes.

- A: Incorrect. That describes Map 1. Map 2's narrowing spacing toward the poles keeps relative areas correct, so Canada and Russia are not enlarged compared with Brazil and India.
- B: Correct. To keep area true, an equal-area cylindrical map shrinks north–south distances toward the poles while east–west distances are stretched, so high-latitude landmasses look flattened. Equal-area maps give up correct shape.
- C: Incorrect. Showing compass bearings as straight lines is the strength of the Mercator projection, the type shown in Map 1, not of an equal-area map.
- D: Incorrect. True distances from a center point are a property of azimuthal equidistant projections, which are built around a center point rather than a rectangular grid.
- E: Incorrect. A compromise projection such as the Robinson balances several kinds of distortion without keeping area or shape exactly true; Map 2 keeps relative area true and gives up correct shape.

### U1-E11 (Q5)
Topic 1.4 · PSO-1.A · Skill 1.A · easy

Which of the following statements describes a town's relative location?

- **A.** The town hall stands at 35.2° N latitude and 97.4° W longitude.
- **B.** The town lies 60 kilometers upstream from the river's mouth.
- **C.** The town is home to about 25,000 people.
- **D.** The town's hilly land and rocky soil limit farming.
- **E.** The town's name comes from a local word for "meeting place."

**Answer: B**

Explanation: Relative location tells where a place is compared to something else, like "60 kilometers upstream from the river's mouth." Absolute location uses exact coordinates instead.

- A: Incorrect. Latitude and longitude give absolute location, a position that does not depend on other places.
- B: Correct. Relative location describes a place in relation to other places or features, here the river's mouth.
- C: Incorrect. Population size is a characteristic of the place, not a description of where it is.
- D: Incorrect. Hilly land and rocky soil describe the town's site, its physical setting, not its position relative to other places.
- E: Incorrect. A place name, or toponym, can reveal history or culture but does not describe location.

### U1-E18 (Q6)
Topic 1.6 · PSO-1.D · Skill 5.C · medium · set: scales

*Questions 6–8 refer to the table below.*

**Stimulus (table): POPULATION CHANGE IN COUNTRY Y AT THREE SCALES, 2015–2025 (HYPOTHETICAL DATA)**

| Area | Population, 2015 (millions) | Population, 2025 (millions) | Change (%) |
|---|---|---|---|
| Country Y (national) | 20.00 | 20.40 | +2.0 |
| Province 1 | 8.00 | 8.64 | +8.0 |
| Province 2 | 7.00 | 6.65 | −5.0 |
| Province 3 | 5.00 | 5.11 | +2.2 |
| Province 2: Capital District | 2.00 | 2.12 | +6.0 |
| Province 2: River District | 3.00 | 2.73 | −9.0 |
| Province 2: Hill District | 2.00 | 1.80 | −10.0 |

Description: A table of population in 2015 and 2025 for Country Y as a whole, for its three provinces, and for the three districts that make up Province 2.

Source: Hypothetical data

Which statement is best supported by comparing the national data with the provincial data?

- **A.** The national growth rate accurately describes the change in each province
- **B.** Province 3's growth was caused by people moving there from Province 2
- **C.** Modest national growth hides a population decline in one province
- **D.** Province 2's decline means Country Y is likely to lose population soon
- **E.** Province 1 grew fastest because it has the largest land area

**Answer: C**

Explanation: The whole country grew a little (+2.0%). But zoom in to the provinces and you see Province 2 actually lost people (−5.0%). The national number hid that. Changing the scale shows a different pattern.

- A: Incorrect. Provincial changes range from a gain of 8.0 percent to a loss of 5.0 percent, so the national figure of +2.0 percent does not describe each province.
- B: Incorrect. The table shows population change but not migration flows; it cannot show where Province 3's new residents came from.
- C: Correct. At the national scale Country Y grew by 2.0 percent, but at the provincial scale Province 2 lost 5.0 percent. Changing the scale of analysis reveals variation that the national figure hides.
- D: Incorrect. Growth in Provinces 1 and 3 more than offset Province 2's loss; the data do not show that the national population is about to fall.
- E: Incorrect. The table contains no data on land area, so it cannot support a claim about why Province 1 grew fastest.

### U1-E19 (Q7)
Topic 1.6 · PSO-1.D · Skill 5.C · medium · set: scales

Which conclusion is best supported by the district-level data for Province 2?

- **A.** River and Hill districts shrank because they are farthest from Country Y's capital
- **B.** The Capital District's growth shows that Province 2 as a whole is growing
- **C.** District data add little, since they show the same pattern as provincial data
- **D.** The Capital District grew because it has a higher birth rate than other districts
- **E.** The Capital District grew even though Province 2 as a whole lost people

**Answer: E**

Explanation: Province 2 shrank overall. But zooming in again shows that its Capital District grew by 6%, while the other two districts lost a lot of people. One more change of scale reveals one more hidden pattern.

- A: Incorrect. The table gives no information about where the districts are or how far they are from the national capital, so it cannot support this explanation.
- B: Incorrect. Province 2 lost 5.0 percent overall; growth in one district did not offset losses in the other two.
- C: Incorrect. The district data reveal a growing Capital District that the provincial figure of −5.0 percent hides, so they add important information.
- D: Incorrect. The table gives total population, not births, deaths, or migration, so it cannot identify the cause of growth.
- E: Correct. The Capital District grew by 6.0 percent while Province 2 as a whole declined by 5.0 percent. District-level data reveal variation hidden by the provincial total.

### U1-E20 (Q8)
Topic 1.3 · IMP-1.C · Skill 3.F · hard · set: scales

The government plans to use these population data to decide which districts need new primary schools. Which approach best addresses a limitation of the table?

- **A.** Assume school demand grows by the national rate of 2.0 percent in each district
- **B.** Rule out new schools anywhere in Province 2, since the province lost population
- **C.** Use each district's total population to set how many new classrooms it needs
- **D.** Collect each district's number of school-age children and existing school capacity
- **E.** Collect each district's land area so planners can compare population density

**Answer: D**

Explanation: The table shows where the total number of people grew or shrank. It does not show how many young children live in each district or whether schools there have room. The government needs those district-level facts before deciding where to build.

- A: Incorrect. The national average hides differences among districts and does not measure the number of school-age children.
- B: Incorrect. The Capital District grew by 6.0 percent even though Province 2 declined overall; provincial totals can hide local needs.
- C: Incorrect. Total population does not show how many children need primary school or how much classroom space already exists.
- D: Correct. Geographic data guide government decisions at every scale, but the table shows only total population change. District-level counts of school-age children and existing school capacity are needed to judge where new schools are required.
- E: Incorrect. Land area and density show crowding, not how many school-age children live in each district or whether existing schools have room.

### U1-E02 (Q9)
Topic 1.1 · IMP-1.A · Skill 3.A · medium

Which type of map would best show the total number of passengers using each of a country's 25 busiest airports?

- **A.** A graduated symbol map with airport circles sized by passenger-count range
- **B.** A choropleth map shading each state by its number of airport passengers
- **C.** An isoline map connecting airports that have equal numbers of passengers
- **D.** A reference map showing the location and name of each airport
- **E.** A dot density map with one dot for each airport in the country

**Answer: A**

Explanation: Each airport gets a circle, and the circle's size shows its range of passenger numbers. Bigger circles mean busier airports.

- A: Correct. A graduated symbol map places a symbol at each location and uses bigger symbols for higher value ranges, which suits totals at point locations such as airports. (A proportional symbol map, which scales each circle to its exact value, works the same way.)
- B: Incorrect. Shading whole states would hide which airports carry the traffic, and choropleth maps are better suited to rates than to raw totals.
- C: Incorrect. Isolines represent a continuous surface such as elevation or temperature; passenger counts at separate airports do not form a continuous surface.
- D: Incorrect. A reference map would show where the airports are but not how many passengers each one handles.
- E: Incorrect. One dot per airport shows only where airports are; it would not show differences in passenger totals.

### U1-E22 (Q10)
Topic 1.7 · SPS-1.A · Skill 1.A · medium

When residents of a state were asked to draw the boundaries of "the Hill Country" on a blank map, their drawings overlapped in the middle but differed a lot at the edges. "The Hill Country" is best described as

- **A.** a perceptual region, based on people's ideas about an area
- **B.** a formal region, based on a single trait such as elevation
- **C.** a functional region, based on travel to a central city
- **D.** a perceptual region, based on a boundary set by state law
- **E.** a functional region, based on shared tourism businesses

**Answer: A**

Explanation: People can share a general picture of a region but still draw its edges in different places. Those different mental maps are the sign of a perceptual region.

- A: Correct. Perceptual (vernacular) regions exist in people's minds and reflect shared ideas and feelings about a place. Different people draw their boundaries in different places, so the edges are fuzzy.
- B: Incorrect. The question defines the region through residents' mental maps, not through a set elevation level.
- C: Incorrect. A functional region is defined by connections to a central node, such as commuting to a city; the drawings reflect people's images of an area, not travel patterns.
- D: Incorrect. The question describes residents' perceptions, not an official boundary set by law.
- E: Incorrect. Tourism businesses could form part of a network, but the region in the question is defined by how residents picture it.

### U1-E08 (Q11)
Topic 1.2 · IMP-1.B · Skill 3.A · medium · set: landcover

*Questions 11–12 refer to the graph below.*

**Stimulus (bar): LAND COVER IN RIVER COUNTY, 2005 AND 2025 (HYPOTHETICAL DATA)**

Bar chart (y-axis: Percent of county area; max 40).

| Category | 2005 | 2025 |
|---|---|---|
| Forest | 34 | 30 |
| Cropland | 38 | 31 |
| Wetland | 12 | 7 |
| Built-up land | 10 | 26 |
| Water | 6 | 6 |

Note under chart: Built-up land includes buildings, roads, and parking lots.

Description: A grouped bar chart of land cover as a percent of River County's area. Forest: 34 percent in 2005 and 30 percent in 2025. Cropland: 38 and 31. Wetland: 12 and 7. Built-up land: 10 and 26. Water: 6 and 6.

Source: Hypothetical data

Which method would most directly produce the measurements summarized in the chart?

- **A.** Recording the positions of public buses with satellite navigation receivers
- **B.** Classifying satellite images and calculating each category's share of county area
- **C.** Surveying residents about how satisfied they are with changes in their neighborhoods
- **D.** Collecting census counts of residents and homes in each neighborhood
- **E.** Interviewing farmers about changes in their crop yields and costs

**Answer: B**

Explanation: The chart shows what share of the county is forest, farmland, wetland, buildings, and water in two years. To measure that, you need a view from above. Researchers sort satellite images into land types, measure each type's area, and turn it into a percent of the county. That is remote sensing.

- A: Incorrect. Bus positions from satellite navigation describe movement and location, not the area covered by each type of land.
- B: Correct. Remote sensing gathers information about Earth's surface from a distance. Satellite images can be sorted into land-cover types; measuring each type's area and dividing by the county's total area gives the percentages shown, and repeating this for two years allows comparison.
- C: Incorrect. Residents' satisfaction is qualitative opinion; it does not measure the land area in each category.
- D: Incorrect. Counts of people and homes do not measure forest, cropland, wetland, built-up land, and water as shares of the county's area.
- E: Incorrect. Crop yields and costs describe farm output, not the countywide land-cover percentages shown.

### U1-E09 (Q12)
Topic 1.5 · PSO-1.B · Skill 3.C · medium · set: landcover

Which conclusion about human–environment interaction is best supported by the chart?

- **A.** Environmental determinism explains the changes, since nature decided the county's land use
- **B.** Because cropland shrank, the county's farms are producing less food than in 2005
- **C.** The loss of wetland was caused by changes in rainfall rather than by human activity
- **D.** Land use in the county became more sustainable, since the area of water stayed the same
- **E.** Built-up land grew as natural land covers such as forest and wetland shrank

**Answer: E**

Explanation: Built-up land (buildings, roads, and parking lots) went from 10% to 26% of the county. At the same time, forest and wetland got smaller. People changed the land to fit their needs. That is human–environment interaction.

- A: Incorrect. Environmental determinism holds that the physical environment controls human activity. The chart shows people changing the environment, which runs the other way.
- B: Incorrect. The chart shows the area of cropland, not crop output; farms can produce as much or more on less land if yields rise.
- C: Incorrect. The chart gives no rainfall data, and the growth of built-up land points to human activity as a likely cause of land-cover change.
- D: Incorrect. An unchanged water area does not show sustainability, especially when wetland and forest, which provide habitat and can absorb floodwater, declined.
- E: Correct. Built-up land rose from 10 to 26 percent of the county while forest fell from 34 to 30 percent and wetland from 12 to 7 percent, showing people reshaping the environment through land use.

### U1-E16 (Q13)
Topic 1.5 · PSO-1.B · Skill 1.C · medium

Which of the following statements best reflects possibilism rather than environmental determinism?

- **A.** A dry climate limits farming, but people can choose to irrigate, herd, or trade
- **B.** A region's climate decides what kind of economy its people will have
- **C.** Mountain landscapes cause the people who live in them to develop the same customs
- **D.** Societies near the sea become sea traders because the coast controls their choices
- **E.** The physical environment has no effect on how people live or what they grow

**Answer: A**

Explanation: Determinism says nature decides what people do. Possibilism says nature sets limits, but people choose what to do within those limits. A dry place limits farming, but people can still pick irrigation, herding, or trade.

- A: Correct. Possibilism holds that the physical environment sets limits and offers opportunities, but people choose among options based on their culture and technology.
- B: Incorrect. Claiming that climate decides a region's economy is environmental determinism, the view that the environment controls human activity.
- C: Incorrect. Claiming that a landscape causes people to share customs is environmental determinism.
- D: Incorrect. Saying that the coast controls people's choices is environmental determinism; possibilism would say the coast offers options that people may or may not use.
- E: Incorrect. Possibilism does not deny the environment's influence; it treats the environment as setting limits within which people make choices.

### U1-E07 (Q14)
Topic 1.2 · IMP-1.B · Skill 1.D · medium

A geographer studying a neighborhood's history reads letters written by early settlers, newspaper stories from the 1920s, and a city planning report from 1965. These sources are best described as

- **A.** geospatial data collected with remote sensing
- **B.** quantitative data gathered by a national census
- **C.** written accounts that provide spatial information
- **D.** layers created with a geographic information system
- **E.** field data collected with a satellite navigation system

**Answer: C**

Explanation: Letters, newspaper stories, and government reports are written accounts. Geographers use them to learn what places were like and how people saw them. They are not numbers from a census or pictures from a satellite.

- A: Incorrect. Remote sensing collects data from a distance, such as satellite images, not letters or reports.
- B: Incorrect. Census data are counts of people and housing collected by a government; letters and news stories are written accounts.
- C: Correct. The AP course framework lists written accounts, such as field observations, media reports, travel narratives, policy documents, and personal interviews, as sources of spatial information. Settlers' letters, old newspaper stories, and a planning report fit this category.
- D: Incorrect. A GIS is a tool for storing and analyzing data in layers; the sources themselves are written documents.
- E: Incorrect. Satellite navigation systems such as GPS record precise positions; they do not produce letters or reports.

### U1-E13 (Q15)
Topic 1.7 · SPS-1.A · Skill 1.D · medium · set: commute

*Questions 15–17 refer to the map below.*

**Stimulus (schematicMap): DAILY COMMUTING TO CITY M FROM SIX NEARBY TOWNS (HYPOTHETICAL DATA)**

Labels on map: Town A 64%; Town B 57%; Town C 41%; Town D 32%; Town E 14%; Town F 8%; City M

Legend: [power] City M; [small] Town, with the percent of its workers who commute to City M; [lane] Dashed line: towns where 25% or more of workers commute to City M

Description: City M is at the center. Arrows show daily commuting from six towns to jobs in City M. Each town is labeled with the percent of its workers who commute to City M: Town A, 14 km from City M, 64%; Town B, 18 km, 57%; Town C, 30 km, 41%; Town D, 36 km, 32%; Town E, 52 km, 14%; Town F, 58 km, 8%. A dashed line encloses City M and Towns A, B, C, and D.

Source: Hypothetical data

The area inside the dashed line on the map is best described as which type of region?

- **A.** A formal region, because the towns share the same government
- **B.** A perceptual region, because residents feel they belong to City M
- **C.** A functional region, tied together by daily commuting to City M
- **D.** A formal region, because it is drawn using a measured percentage
- **E.** A functional region, because its towns share a uniform climate and landscape

**Answer: C**

Explanation: A functional region is built around a center, called the node, and is held together by movement to it. Here, workers from the towns travel to jobs in City M every day. The dashed line wraps around the towns most connected to City M. The 25% line is a number, but what it measures is trips to City M. A region held together by trips to a center is functional, not formal.

- A: Incorrect. The map gives no information about a shared government; the towns are grouped by their connections to City M.
- B: Incorrect. A perceptual region is based on people's feelings or images of a place; the map shows measured commuting, not feelings.
- C: Correct. A functional (nodal) region is organized around a central node and defined by flows and connections to it. The dashed line encloses the towns most strongly linked to City M by daily commuting.
- D: Incorrect. The 25 percent threshold measures each town's connection to City M. A region defined by flows to a node is functional, even when a number is used to draw its edge.
- E: Incorrect. A shared climate and landscape would define a formal region; this region is defined by commuting to City M, not by a uniform trait.

### U1-E14 (Q16)
Topic 1.4 · PSO-1.A · Skill 3.E · easy · set: commute

Which concept best explains the pattern of commuting percentages shown on the map?

- **A.** Time-space compression, because commuters from distant towns reach City M fastest
- **B.** Clustering, because the towns are bunched tightly around City M
- **C.** Relative location, because each town's latitude and longitude set its commuting share
- **D.** Environmental determinism, because the landscape forces workers to commute
- **E.** Distance decay, because the share commuting to City M falls as distance increases

**Answer: E**

Explanation: Nearby towns send a bigger share of their workers to City M, and farther towns send a smaller share. (The map shows shares, not the total number of workers.) The share drops as distance grows. That is distance decay.

- A: Incorrect. The map gives distances and commuting shares, not travel times or changes in transportation technology.
- B: Incorrect. Clustering describes how features are arranged; the towns lie at different distances from City M, and the key pattern is that commuting shares fall with that distance.
- C: Incorrect. Latitude and longitude describe absolute location. The pattern depends on each town's distance from City M.
- D: Incorrect. The map shows no physical barriers, and commuting is a choice shaped by travel time and cost, not by the landscape alone.
- E: Correct. Distance decay is the decline in interaction between places as the distance between them increases. Towns nearest City M send the largest shares of workers; the farthest towns send the smallest.

### U1-E15 (Q17)
Topic 1.4 · PSO-1.A · Skill 2.C · medium · set: commute

Suppose a fast commuter rail line opened between City M and Town F. Which change would most likely follow?

- **A.** Town F's commuting share would fall, because rail weakens ties to City M
- **B.** City M's functional region could shrink toward the towns nearest the city
- **C.** Town F would form its own formal region of rail commuters
- **D.** Town F's commuting share would rise, which could bring it inside the dashed line
- **E.** Town F's commuting share would stay the same, since its distance to City M would not change

**Answer: D**

Explanation: A fast train cuts the travel time from Town F to City M. That could lead a bigger share of Town F's workers to take jobs in City M. If the share reaches 25%, Town F would meet this map's rule for being inside the commuting region.

- A: Incorrect. Faster transportation lowers the time cost of travel, which strengthens, not weakens, a town's connection to the central city.
- B: Incorrect. Better transportation tends to extend a functional region outward, not shrink it.
- C: Incorrect. The scenario is about a changing flow to City M; it does not create a separate region defined by a shared, uniform trait.
- D: Correct. A fast rail line would cut travel time, an example of time-space compression that weakens distance decay. More of Town F's workers would likely commute to City M, which could push its share above the 25 percent threshold and extend the functional region.
- E: Incorrect. The distance in kilometers stays the same, but travel time falls, and commuting responds to travel time and cost.

### U1-E24 (Q18)
Topic 1.7 · SPS-1.A · Skill 1.B · hard

Maps of "the Middle East" made by different governments, news organizations, and textbooks often include different sets of countries. Which statement best explains this?

- **A.** The region has one official boundary, but some organizations use outdated maps
- **B.** The region is organized around trade flows to a single central city
- **C.** People define regions using different criteria, so boundaries can be contested
- **D.** The maps use different projections, which change which countries appear in a region
- **E.** The region has no shared characteristics, so it cannot be mapped consistently

**Answer: C**

Explanation: People make regions by choosing what ties places together, like language, religion, history, or politics. Different groups choose differently, so their maps include different countries. That is why regional boundaries are often argued over and can overlap.

- A: Incorrect. There is no single, universally accepted boundary of the Middle East; organizations use different defining criteria.
- B: Incorrect. The region is not defined by flows to one central city; the question is about the different criteria used to choose its countries.
- C: Correct. Regions are defined by people using one or more chosen characteristics. Because organizations use different criteria, such as culture, history, or politics, regional boundaries are often contested and overlapping.
- D: Incorrect. A map projection changes the shape and size of places, not which countries a mapmaker chooses to include in a region.
- E: Incorrect. The countries share characteristics that many people use to define a region; the disagreement is over which countries meet the chosen criteria.

### U1-E05 (Q19)
Topic 1.1 · IMP-1.A · Skill 1.B · medium

A subway map shows each line as a straight colored path with evenly spaced stations, even though the real tracks curve and the stations are different distances apart. Which statement best explains why the mapmaker drew it this way?

- **A.** The mapmaker lacked accurate GPS data on the location of each station
- **B.** Subway maps are reference maps, which require exact distances and shapes
- **C.** The map is an isoline map that connects stations with equal numbers of riders
- **D.** Map projections badly distort shape and area on maps of small areas such as a city
- **E.** All maps are selective, and this one trades true distance for clear connections

**Answer: E**

Explanation: Every map leaves things out or changes things on purpose. A subway rider needs to know the order of the stops and where to switch lines, not the exact curve of the tracks. So the mapmaker straightened the lines to make the map easy to use.

- A: Incorrect. The simplification is a deliberate design choice; accurate location data are easy to obtain, and the map leaves them out on purpose.
- B: Incorrect. Reference maps help users locate places, but no map shows everything exactly; this map deliberately gives up true distance.
- C: Incorrect. Isoline maps connect points of equal value on a continuous surface; subway lines connect stations along a route.
- D: Incorrect. Straightening the routes and spacing the stations evenly are design choices; projection distortion does not explain that pattern.
- E: Correct. All maps are selective in the information they show. A transit map gives up accurate distance and shape to make routes, transfers, and the order of stations easy to read.

### U1-E21 (Q20)
Topic 1.6 · PSO-1.C · Skill 5.A · easy

A study combines national internet-access data to calculate one rate for Southeast Asia as a whole, then compares that rate with rates for other world regions. At which scale are the compared data aggregated (grouped)?

- **A.** Global, because the regions being compared cover much of the world
- **B.** Regional, because each compared value summarizes a world region
- **C.** National, because the original figures came from individual countries
- **D.** Local, because internet access can be measured for individual households
- **E.** Global, because the internet connects places throughout the world

**Answer: B**

Explanation: The researchers make one number for Southeast Asia and compare it with one number for each other world region. So the compared data are regional, even though the original figures came from countries.

- A: Incorrect. Comparing regions from across the world does not make each compared value a worldwide total.
- B: Correct. The study combines country figures into one value for each world region, so the compared data are aggregated at the regional scale.
- C: Incorrect. The original figures came from countries, but the study combines them into regional values before comparing.
- D: Incorrect. Household information was combined into regional rates; individual household values are not compared.
- E: Incorrect. The worldwide reach of the internet does not decide the level at which the data are grouped.

### U1-E10 (Q21)
Topic 1.3 · IMP-1.C · Skill 2.C · medium

Between two censuses, State A's population grew much faster than the U.S. population as a whole, while State B's population stayed about the same. Based on the new census data, which outcome is most likely?

- **A.** State A is likely to lose seats in the U.S. Senate, and State B may gain one
- **B.** Both states keep the same number of House seats, since the number of seats per state is fixed
- **C.** State A's boundary expands to include part of a neighboring state
- **D.** State A may gain House seats, and State B may lose one if its population share falls
- **E.** State B is likely to gain House seats to make up for its slower growth

**Answer: D**

Explanation: The census helps divide the 435 House seats among the states. A state whose share of the U.S. population goes up may gain a seat, and a state whose share goes down may lose one. A state can also keep the same number of seats.

- A: Incorrect. Every state has two senators regardless of population, so census results do not change Senate seats.
- B: Incorrect. The total of 435 House seats is set by law, but how those seats are divided among the states is recalculated after every census.
- C: Incorrect. Census data can change representation and guide redistricting, but they do not redraw state boundaries.
- D: Correct. After each decennial census, the 435 House seats are reapportioned using state populations and a set formula. Growing faster than other states can produce a seat gain, and a falling share can cost a seat, but growth does not guarantee a change.
- E: Incorrect. Seats follow population; a state that grows slowly compared with the country tends to lose seats, not gain them.

### U1-E12 (Q22)
Topic 1.4 · PSO-1.A · Skill 1.D · medium

Engineers in two countries on opposite sides of the world work on the same design in real time using video calls and shared online files. This situation best illustrates

- **A.** time-space compression, because technology reduces the effect of distance
- **B.** distance decay, because the engineers interact less as the distance between them grows
- **C.** absolute distance, because the two countries are now closer together
- **D.** a functional region centered on the engineers' main office
- **E.** a formal region, because the engineers share the same profession

**Answer: A**

Explanation: Time-space compression means the world feels smaller because technology lets people connect quickly over long distances. Video calls let engineers on opposite sides of Earth work together as if they were in the same room.

- A: Correct. Time-space compression is the reduced importance of distance as transportation and communication technologies speed the movement of people, goods, and information. Real-time collaboration across the world is an example.
- B: Incorrect. Distance decay predicts less interaction with greater distance; here the engineers interact closely despite great distance, which shows distance decay being weakened.
- C: Incorrect. The absolute distance between the countries has not changed; what changed is how much that distance limits interaction.
- D: Incorrect. Nothing in the scenario describes a central office drawing in flows; it describes distance mattering less.
- E: Incorrect. A shared profession could help define a formal region, but the scenario is about technology overcoming distance, not about a region.

### U1-E25 (Q23)
Topic 1.3 · IMP-1.C · Skill 2.C · medium

A popular navigation app uses real-time traffic data to send drivers off a jammed highway onto quiet residential streets. Which outcome is the most likely geographic effect of this decision?

- **A.** The absolute distance between the highway and the neighborhoods will shrink
- **B.** The residential streets will become a formal region defined by app use
- **C.** The neighborhoods' relative location will change, since they are now farther from the highway
- **D.** More cars will use residential streets, and towns may add speed bumps
- **E.** Stores along the highway will move to the side streets to follow the traffic

**Answer: D**

Explanation: When the app sends lots of drivers onto small neighborhood streets, those streets get busy. Towns may then add speed bumps or new rules. A decision made with map data changed what happens on the ground.

- A: Incorrect. Absolute distance does not change; rerouting changes travel time and traffic patterns, not the distance between places.
- B: Incorrect. The scenario describes changed traffic flows, not an area defined by a shared, uniform trait.
- C: Incorrect. Rerouting does not move the neighborhoods farther from the highway. Their traffic connections may change, but the claim that they are farther away is unsupported.
- D: Correct. Decisions made with geospatial data have geographic effects. Rerouting many drivers onto local streets increases traffic there, which can lead towns to lower speed limits, add speed bumps, or restrict turns.
- E: Incorrect. A short detour around a traffic jam gives stores no reason to move; the direct, likely effect is more cars on the side streets.

### U1-E23 (Q24)
Topic 1.7 · SPS-1.A · Skill 2.A · medium

On a map of the languages spoken at home in a border area, the share of people who speak Language X falls gradually from 90 percent to 10 percent over about 50 kilometers, with many bilingual towns in between. Which statement best describes the boundary of the Language X region?

- **A.** It is a sharp line that follows the international border
- **B.** It is a functional boundary based on travel to one city
- **C.** It is a perceptual boundary, since the language people speak cannot be measured
- **D.** It is set by law, so mapmakers place it in the same spot
- **E.** It is a transition zone where the region blends into its neighbor

**Answer: E**

Explanation: Regions often do not have sharp edges. As you travel across this border area, Language X becomes less and less common, and many towns speak two languages. That in-between area is a transition zone.

- A: Incorrect. The share of Language X speakers changes gradually across about 50 kilometers, so there is no single sharp line.
- B: Incorrect. The region is defined by a shared trait, the language people speak, not by flows to a central city.
- C: Incorrect. The language spoken at home can be measured with surveys or census data; this is a formal region based on a measurable trait.
- D: Incorrect. The map shows where people use the language, not a legally defined language area; some countries do set language areas by law, but the gradual change in percentages here points to a transition zone.
- E: Correct. Regional boundaries are often transitional. Here the Language X region fades into its neighbor across a zone of bilingual towns rather than ending at a sharp line.

### U1-E17 (Q25)
Topic 1.5 · PSO-1.B · Skill 1.D · easy

A town that depends on a nearby forest for timber decides to cut no more trees each year than the forest regrows and to replant the areas it harvests. Which concept does this policy best reflect?

- **A.** Environmental determinism, because the forest controls the town's economy
- **B.** Sustainability, because it meets today's needs without using up the forest
- **C.** Nonrenewable resource use, because cut trees cannot be replaced
- **D.** Distance decay, because the town relies on the forest closest to it
- **E.** Resource depletion, because the town removes trees from the forest each year

**Answer: B**

Explanation: Sustainability means using what you need now while leaving enough for the future. Cutting only as many trees as grow back, and replanting, means the forest will still be there for people later.

- A: Incorrect. The town made a deliberate choice about how much to harvest; environmental determinism holds that the environment controls human activity.
- B: Correct. Sustainability means using resources to meet present needs without compromising the ability of future generations to meet their own needs. Harvesting no more than regrows, and replanting, keeps the forest productive.
- C: Incorrect. Trees are a renewable resource; they regrow, which is what makes this policy possible.
- D: Incorrect. The forest is nearby, but the policy is about how much to harvest over time, not about how interaction changes with distance.
- E: Incorrect. Harvesting a renewable resource does not deplete it when the harvest stays within the rate of regrowth.

