# Unit 1 practice items P01-P15 (topics 1.1-1.3)
# Stimulus geometry is computed here so every coordinate can be re-checked by u1/verify.py.
import math, random
P = []

# ---------- stimulus builders ----------
def dot_map():
    """P02: dot-density map of dairy farms in hypothetical County R (each square = 10 farms)."""
    west = [[0, 0], [468, 0], [474, 60], [462, 130], [476, 200], [466, 270], [478, 340], [470, 400], [0, 400]]
    east = [[484, 0], [800, 0], [800, 400], [486, 400], [494, 340], [482, 270], [492, 200], [478, 130], [490, 60]]
    rng = random.Random(11)
    pts = []
    def ok(p): return all((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 >= 24 ** 2 for q in pts)
    while len(pts) < 22:                       # dense band just east of the river
        p = [rng.randint(510, 650), rng.randint(22, 378)]
        if ok(p): pts.append(p)
    for p in ([95, 85], [250, 300], [165, 215], [335, 120]):   # a few scattered in the west
        pts.append(p)
    return dict(type="schematicMap",
      title="DAIRY FARMS IN COUNTY R (HYPOTHETICAL)",
      canvas=dict(width=800, height=400),
      features=[
        dict(kind="land", name="County R, west of the river", polygon=west, style="small"),
        dict(kind="land", name="County R, east of the river", polygon=east, style="small"),
        dict(kind="marker", name="10 dairy farms", points=pts, symbol="baseN")],
      legend=[dict(swatch="baseN", label="Each square = 10 dairy farms"), dict(swatch="water", label="River")],
      description="A river runs north to south through the eastern part of County R. Every square is the same size and stands for 10 dairy farms. Twenty-two squares are packed into a band just east of the river; only four squares are scattered across the western part of the county.",
      source="Hypothetical data")

def contour_map():
    """P03: contour (isoline) map of Hill Q. Spacing between lines: west 18 px, south 30, north 38, east 70."""
    cx, cy = 300, 210
    W = [20 + 18 * i for i in range(5)]    # west extents, inner -> outer
    E = [40 + 70 * i for i in range(5)]    # east
    N = [25 + 38 * i for i in range(5)]    # north (up)
    S = [22 + 30 * i for i in range(5)]    # south (down)
    feats = [dict(kind="land", name="", polygon=[[0, 0], [800, 0], [800, 420], [0, 420]])]
    for i in range(4, -1, -1):
        loop = []
        for k in range(73):
            t = 2 * math.pi * k / 72
            c, s = math.cos(t), math.sin(t)
            x = cx + (E[i] if c >= 0 else W[i]) * c
            y = cy + (S[i] if s >= 0 else N[i]) * s
            loop.append([round(x, 1), round(y, 1)])
        feats.append(dict(kind="line", name=f"{180 - 20 * i} m contour line", line=loop))
    # point labels: zero-area land shapes so only the letter shows
    lab = {"J": (cx - (W[2] + W[3]) / 2, cy), "K": (cx + (E[2] + E[3]) / 2, cy),
           "L": (cx, cy - (N[2] + N[3]) / 2), "M": (cx, cy + (S[2] + S[3]) / 2), "N": (720, 360)}
    for name, (x, y) in lab.items():
        x, y = round(x, 1), round(y, 1)
        feats.append(dict(kind="land", name=name, polygon=[[x, y], [x, y], [x, y]], labelAt=[x, y - 1]))
    stim = dict(type="schematicMap",
      title="CONTOUR MAP OF HILL Q (HYPOTHETICAL). CONTOUR INTERVAL: 20 METERS",
      canvas=dict(width=800, height=420),
      features=feats,
      description="Five closed contour lines circle the top of Hill Q, from 100 meters (outer line) to 180 meters (inner line). Point J is on the west side of the hill, Point K on the east side, Point L on the north side, and Point M on the south side; each sits between the 120-meter and 140-meter lines. Point N is outside the 100-meter line. Near Point J the lines are tightly packed; near Point K they are widely spaced; near Point L they are moderately spaced; near Point M they are fairly close together.",
      source="Hypothetical map")
    return stim, dict(cx=cx, cy=cy, W=W, E=E, N=N, S=S, labels=lab)

def floodplain_map():
    """P14: GIS overlay of a 100-year floodplain and buildings (hypothetical)."""
    wf_e = [[440, 0], [425, 100], [450, 200], [430, 300], [445, 400]]          # west floodplain, east edge (= river west bank)
    ef_w = [[470, 0], [455, 100], [480, 200], [460, 300], [475, 400]]          # east floodplain, west edge (= river east bank)
    ef_e = [[520, 0], [530, 100], [515, 200], [528, 300], [520, 400]]          # east floodplain, east edge
    wh_e = [[170, 0], [160, 100], [175, 200], [165, 300], [170, 400]]          # west high ground, east edge
    feats = [
      dict(kind="land", name="Higher ground", polygon=[[0, 0]] + wh_e + [[0, 400]], style="small", labelAt=[80, 360]),
      dict(kind="land", name="100-year floodplain", polygon=wh_e + wf_e[::-1], style="power", labelAt=[300, 360]),
      dict(kind="land", name="100-year floodplain (east bank)", polygon=ef_w + ef_e[::-1], style="power"),
      dict(kind="land", name="Higher ground", polygon=ef_e + [[800, 400], [800, 0]], style="small", labelAt=[660, 360]),
      dict(kind="marker", name="Home", symbol="house",
           points=[[215, 60], [290, 45], [370, 70], [230, 140], [390, 150], [220, 250], [340, 260], [395, 300],
                   [40, 120], [110, 220], [60, 290],
                   [600, 230], [690, 250], [740, 160], [620, 300]]),
      dict(kind="marker", name="School", symbol="baseS", points=[[300, 185]]),
      dict(kind="marker", name="Hospital", symbol="baseN", points=[[660, 110]])]
    return dict(type="schematicMap",
      title="FLOOD RISK AND BUILDINGS ALONG THE RIVER, COUNTY T (HYPOTHETICAL GIS MAP)",
      canvas=dict(width=800, height=400),
      features=feats,
      legend=[dict(swatch="power", label="100-year floodplain (1% chance of flooding each year)"),
              dict(swatch="small", label="Higher ground"), dict(swatch="water", label="River"),
              dict(swatch="house", label="Home"), dict(swatch="baseS", label="School"), dict(swatch="baseN", label="Hospital")],
      description="A river runs north to south through the map. The shaded 100-year floodplain lies along both banks and is much wider on the west side. Eight homes and the school are inside the floodplain on the west bank. Three homes stand on higher ground at the far west edge. The hospital and four homes stand on higher ground east of the river, outside the floodplain.",
      source="Hypothetical map")

CONTOUR, CONTOUR_GEOM = contour_map()

# ---------------- 1.1 Introduction to Maps (IMP-1.A) ----------------
P.append(dict(id="U1-P01", topic="1.1", lo="IMP-1.A", skill="1.A", difficulty="easy",
  stem="Which of the following is the best example of a reference map?",
  options={
    "A": "A world map shading each country by its average life expectancy",
    "B": "A state highway map showing roads, cities, rivers, and county lines",
    "C": "A map using circles of different sizes to show the population of each large city",
    "D": "A map with lines connecting places that have the same average January temperature",
    "E": "A world map with each country resized in proportion to its number of people"},
  answer="B",
  explanation="A reference map helps you find places. It shows general features like roads, cities, rivers, and borders. A highway map is a classic reference map. Thematic maps are different: each one is made to show one topic, like life expectancy or temperature.",
  whyNot={
    "A": "Shading countries by life expectancy shows one topic. That is a thematic map (a choropleth map).",
    "C": "Circles sized by population show one topic. That is a thematic map (a graduated symbol map).",
    "D": "Lines joining places with the same temperature show one topic. That is a thematic map (an isoline map).",
    "E": "Resizing countries by population shows one topic. That is a thematic map (a cartogram)."},
  vocab=["reference map", "thematic map"]))

P.append(dict(id="U1-P02", topic="1.1", lo="IMP-1.A", skill="3.A", difficulty="easy",
  stimulus=dot_map(),
  stem="The map above is best classified as which type of thematic map?",
  options={
    "A": "Choropleth map",
    "B": "Graduated symbol map",
    "C": "Isoline map",
    "D": "Dot density map",
    "E": "Cartogram"},
  answer="D",
  explanation="On a dot density map, every dot (here, a small square) stands for the same number of things. More dots in one spot means more of that thing there. Each square here is 10 dairy farms, so you can see the farms are bunched together (clustered) just east of the river.",
  whyNot={
    "A": "A choropleth map shades whole areas, like counties, darker or lighter. This map places symbols instead of shading areas.",
    "B": "A graduated symbol map uses bigger symbols for bigger amounts. Every square here is the same size.",
    "C": "An isoline map draws lines that connect places with equal values, like elevation. There are no lines like that here.",
    "E": "A cartogram changes the size of places to match a number, like population. The county keeps its real shape here."},
  vocab=["dot density map", "thematic map", "clustering"]))

P.append(dict(id="U1-P03", topic="1.1", lo="IMP-1.A", skill="3.B", difficulty="medium",
  stimulus=CONTOUR,
  stem="Based on the map, at which labeled point is the land steepest?",
  options={"A": "Point J", "B": "Point K", "C": "Point L", "D": "Point M", "E": "Point N"},
  answer="A",
  explanation="Contour lines are isolines: each line connects places at the same height. When the lines are packed close together, the land climbs a lot in a short distance, so it is steep. At Point J the lines are closest together.",
  whyNot={
    "B": "At Point K the lines are far apart, so the land rises slowly. That is a gentle slope.",
    "C": "Point L's lines are closer than at K but farther apart than at J, so it is less steep than J.",
    "D": "Point M's lines are fairly close, but they are not packed as tightly as at J.",
    "E": "Point N is past the lowest contour line, with no lines nearby. The land there is nearly flat."},
  vocab=["isoline", "contour line", "elevation"]))

P.append(dict(id="U1-P04", topic="1.1", lo="IMP-1.A", skill="1.B", difficulty="medium",
  stem="On a Mercator projection, Greenland looks about as large as Africa, even though Africa is about 14 times larger. Which of the following best explains this distortion?",
  options={
    "A": "The Mercator projection keeps areas accurate, so its distortion is in the shapes of landmasses near the equator.",
    "B": "Greenland's thick ice sheet makes the island look much larger on maps than its land area really is.",
    "C": "The Mercator projection keeps local shapes and directions true but stretches area toward the poles.",
    "D": "The Mercator projection is centered on the North Pole, so places close to the pole are drawn larger.",
    "E": "The Mercator projection keeps true distances from the equator, so places far from it look bigger."},
  answer="C",
  explanation="Mercator made his map in 1569 for sailors. It keeps compass directions and the shapes of small areas correct. To do that, it stretches the map more and more as you move toward the North and South Poles. Greenland is far north, so it gets blown up a lot. Africa sits on the equator, where there is little stretching.",
  whyNot={
    "A": "That describes an equal-area map like Gall-Peters. Mercator does the opposite: it keeps local shapes but distorts area.",
    "B": "The problem is the map projection, not the ice. Greenland looks huge on Mercator maps that show only outlines.",
    "D": "A map centered on the North Pole is an azimuthal (polar) map. Mercator is a rectangular map centered on the equator.",
    "E": "Mercator does not keep true distances. Its scale grows toward the poles, which is why far-north places look too big."},
  vocab=["Mercator projection", "map projection", "distortion"]))

P.append(dict(id="U1-P05", topic="1.1", lo="IMP-1.A", skill="1.E", difficulty="hard",
  stem="An airline planner wants one map that shows the correct distance and direction from the airline's hub airport to cities around the world. Which map projection would serve this purpose best?",
  options={
    "A": "A Mercator projection, which keeps compass bearings constant along straight lines",
    "B": "A Gall-Peters projection, which shows the true relative sizes of the continents",
    "C": "A Robinson projection, which keeps overall distortion low across the map",
    "D": "A Goode's homolosine projection, which interrupts the oceans to reduce distortion of land",
    "E": "An azimuthal equidistant projection, which is drawn outward from a single center point"},
  answer="E",
  explanation="An azimuthal equidistant map is drawn around one center point. A straight line from that center shows the true distance and the true direction to any other place. If the planner puts the hub airport at the center, the planner can measure the route to any city. Distances between two places that are NOT the center are distorted, but the planner only needs routes from the hub.",
  whyNot={
    "A": "Mercator keeps compass bearings, which helps sailors, but its distances are badly stretched toward the poles.",
    "B": "Gall-Peters keeps area true, but it distorts distances and shapes, so it cannot measure routes from the hub.",
    "C": "Robinson is a compromise map. It distorts a little of everything, so neither distance nor direction from the hub is exactly right.",
    "D": "Goode's map keeps area true, but cutting the oceans breaks up the very routes the planner needs to measure."},
  vocab=["azimuthal equidistant projection", "Mercator projection", "Gall-Peters projection", "Robinson projection"]))

P.append(dict(id="U1-P06", topic="1.1", lo="IMP-1.A", skill="3.D", difficulty="medium",
  stimulus=dict(type="table",
    title="NEW BUSINESSES OPENED IN FIVE COUNTIES OF STATE Q, 2025 (HYPOTHETICAL DATA)",
    columns=["County", "Population", "New businesses opened"],
    rows=[
      ["Adams", "820,000", "2,870"],
      ["Baker", "60,000", "480"],
      ["Cole", "150,000", "900"],
      ["Dunn", "300,000", "1,350"],
      ["Ellis", "45,000", "135"]],
    description="A table listing the population and the number of new businesses opened in 2025 for five counties: Adams, Baker, Cole, Dunn, and Ellis.",
    source="Hypothetical data"),
  stem="A student wants to make a choropleth map showing where opening a new business was most common relative to the number of residents. Based on the table, which county should be shaded darkest?",
  options={"A": "Adams County", "B": "Baker County", "C": "Cole County", "D": "Dunn County", "E": "Ellis County"},
  answer="B",
  explanation="A choropleth map should shade areas by a rate, not a total. Divide new businesses by population. Baker had 480 new businesses for 60,000 people. That is 8.0 per 1,000 residents, the highest rate. Adams had the most businesses only because it has the most people.",
  whyNot={
    "A": "Adams has the biggest total (2,870), but it has 820,000 people. That is only 3.5 per 1,000 residents.",
    "C": "Cole's rate is 6.0 per 1,000 residents. That is second highest, but below Baker's 8.0.",
    "D": "Dunn's rate is 4.5 per 1,000 residents, lower than Baker's.",
    "E": "Ellis is the smallest county, but its rate is only 3.0 per 1,000 residents, the lowest of the five."},
  vocab=["choropleth map", "rate", "per capita"]))

P.append(dict(id="U1-P07", topic="1.1", lo="IMP-1.A", skill="3.A", difficulty="easy",
  stem="On a certain world map, India appears much larger than Canada, even though Canada has about three times as much area. The map draws each country's size in proportion to its population. This type of map is called a",
  options={
    "A": "cartogram",
    "B": "choropleth map",
    "C": "reference map",
    "D": "dot density map",
    "E": "Mercator projection"},
  answer="A",
  explanation="A cartogram changes the size of each place to match a number, like population, instead of land area. India has far more people than Canada, so India is drawn much bigger. Cartograms give up true shape and area to make one number easy to see.",
  whyNot={
    "B": "A choropleth map keeps true country sizes and shades them with colors.",
    "C": "A reference map shows real locations and features like borders and cities. It does not resize countries by population.",
    "D": "A dot density map keeps true sizes and places dots inside each country.",
    "E": "Mercator stretches places near the poles. That would make Canada look bigger, not smaller."},
  vocab=["cartogram", "thematic map"]))

# ---------------- 1.2 Geographic Data (IMP-1.B) ----------------
P.append(dict(id="U1-P08", topic="1.2", lo="IMP-1.B", skill="1.A", difficulty="easy",
  stem="A city planner uses a computer program to stack map layers showing roads, flood zones, school locations, and population density, and then analyzes how the layers relate to one another. This tool is best described as",
  options={
    "A": "remote sensing from satellites",
    "B": "a satellite navigation system such as GPS",
    "C": "a national census of population",
    "D": "a geographic information system",
    "E": "an aerial photograph of the city"},
  answer="D",
  explanation="A geographic information system (GIS) is computer software that stores map data in layers. The planner can stack layers, like roads on top of flood zones, to see how they relate. GIS is the tool for analyzing. GPS and remote sensing are ways of collecting data that often go into a GIS.",
  whyNot={
    "A": "Remote sensing collects images or data from far away, such as from satellites. It gathers data but is not the layering tool.",
    "B": "GPS finds a precise location. It collects location data but does not stack and analyze layers.",
    "C": "A census counts people and households. Its data can be one layer in a GIS, but it is not the tool itself.",
    "E": "An aerial photo is one picture. It cannot hold and compare several layers of data."},
  vocab=["geographic information system (GIS)", "layer", "geospatial technology"]))

P.append(dict(id="U1-P09", topic="1.2", lo="IMP-1.B", skill="1.D", difficulty="easy",
  stem="Scientists compare images of a mountain glacier taken from satellites in 1990, 2005, and 2020 to measure how much the ice has shrunk. Which method of collecting geographic data are they using?",
  options={
    "A": "Field observation",
    "B": "Satellite navigation (GPS)",
    "C": "Remote sensing",
    "D": "A population census",
    "E": "Personal interviews"},
  answer="C",
  explanation="Remote sensing means gathering information about Earth's surface from a distance, usually with satellites, airplanes, or drones. Comparing satellite images from different years shows change over time, like a glacier getting smaller.",
  whyNot={
    "A": "Field observation means going to the place and recording what you see in person. These scientists used images taken from space.",
    "B": "GPS satellites send signals that pinpoint a location. They do not take pictures of the glacier.",
    "D": "A census counts people, not ice.",
    "E": "Interviews collect people's words and opinions, not measurements of a glacier's size."},
  vocab=["remote sensing", "satellite imagery"]))

P.append(dict(id="U1-P10", topic="1.2", lo="IMP-1.B", skill="3.A", difficulty="medium",
  stem="A geographer wants to learn how longtime residents feel about the changes a new highway brought to their neighborhood. Which source would provide the most useful information?",
  options={
    "A": "Satellite images of the neighborhood before and after the highway was built",
    "B": "GPS data showing the average speed of cars on the highway",
    "C": "Census tables showing the neighborhood's population in each decade",
    "D": "A GIS layer showing property values along the highway",
    "E": "Recorded interviews with people who have lived there for decades"},
  answer="E",
  explanation="Feelings and opinions are qualitative information. The best way to get them is to ask people. Personal interviews are one of the sources of spatial information your AP course guide lists. Images, GPS, census tables, and GIS layers give numbers or pictures, but they cannot tell you how residents feel.",
  whyNot={
    "A": "Satellite images show physical changes, like new pavement, but not how people feel about them.",
    "B": "GPS speed data tell how fast cars move, not what residents think.",
    "C": "Census tables count people. They show who lives there, not their opinions.",
    "D": "Property values are numbers. They might hint at change, but they do not record residents' feelings."},
  vocab=["qualitative data", "quantitative data", "interview"]))

P.append(dict(id="U1-P11", topic="1.2", lo="IMP-1.B", skill="3.A", difficulty="medium",
  stimulus=dict(type="table",
    title="DATA GATHERED TO PLAN A NEW BUS ROUTE IN CITY P (HYPOTHETICAL)",
    columns=["Data set", "What it contains"],
    rows=[
      ["1", "Number of residents age 65 and older in each census tract, from the national census"],
      ["2", "Notes from interviews with riders waiting at bus stops"],
      ["3", "Images taken from aircraft and satellites showing where new apartment buildings were built"],
      ["4", "Position of each city bus, recorded automatically every 30 seconds by a receiver on board"],
      ["5", "One computer map that overlays data sets 1 through 4 so planners can compare them"]],
    description="A table describing five data sets a city collected to plan a new bus route.",
    source="Hypothetical data"),
  stem="Which data set was collected using a satellite navigation system?",
  options={"A": "Data set 1", "B": "Data set 2", "C": "Data set 3", "D": "Data set 4", "E": "Data set 5"},
  answer="D",
  explanation="A satellite navigation system, like GPS, uses signals from satellites to find an exact position. The receiver on each bus records where the bus is every 30 seconds. That is Data set 4.",
  whyNot={
    "A": "Data set 1 comes from a census, which counts people where they live.",
    "B": "Data set 2 comes from interviews, a field method that gathers people's words.",
    "C": "Data set 3 comes from remote sensing. Satellites took pictures, but they did not find the position of a receiver.",
    "E": "Data set 5 is a GIS, a tool that layers and analyzes data collected in other ways."},
  vocab=["GPS", "satellite navigation system", "remote sensing", "GIS"]))

# ---------------- 1.3 The Power of Geographic Data (IMP-1.C) ----------------
P.append(dict(id="U1-P12", topic="1.3", lo="IMP-1.C", skill="3.D", difficulty="medium",
  stimulus=dict(type="bar",
    title="CHILDREN UNDER AGE 5 BY NEIGHBORHOOD, CITY V, 2010 AND 2020 CENSUS (HYPOTHETICAL DATA)",
    categories=["Riverside", "Oak Hill", "Midtown", "Westfield", "Lakeview"],
    series=[dict(name="2010", values=[650, 1200, 400, 900, 700]),
            dict(name="2020", values=[1480, 1050, 520, 1120, 610])],
    yLabel="Children under age 5", yMax=1600,
    description="A grouped bar chart of the number of children under age 5 in five neighborhoods in 2010 and 2020. Riverside: 650 and 1,480. Oak Hill: 1,200 and 1,050. Midtown: 400 and 520. Westfield: 900 and 1,120. Lakeview: 700 and 610.",
    source="Hypothetical data"),
  stem="A school district plans to build one new elementary school where the number of young children is growing fastest. Based on the census data in the chart, which neighborhood is the best location?",
  options={"A": "Riverside", "B": "Oak Hill", "C": "Midtown", "D": "Westfield", "E": "Lakeview"},
  answer="A",
  explanation="Riverside's number of children under 5 more than doubled, from 650 to 1,480. That is the biggest increase and the largest total in 2020. These children will start school soon, so a new school there would serve the most students. This is how census data guide government decisions.",
  whyNot={
    "B": "Oak Hill had the most young children in 2010, but its number fell by 2020 (1,200 to 1,050).",
    "C": "Midtown grew a little (400 to 520), but it still has the fewest young children.",
    "D": "Westfield grew (900 to 1,120), but Riverside grew far more and now has more young children.",
    "E": "Lakeview's number of young children fell (700 to 610)."},
  vocab=["census", "geospatial data"]))

P.append(dict(id="U1-P13", topic="1.3", lo="IMP-1.C", skill="2.C", difficulty="medium",
  stem="A coffee company uses GIS to compare traffic counts, the locations of competing shops, and the incomes and ages of residents in each neighborhood before choosing where to open new stores. Which outcome is most likely?",
  options={
    "A": "New stores are spaced evenly across the city, one in each neighborhood",
    "B": "New stores open where land is cheapest, whatever the traffic or customers",
    "C": "New stores cluster along busy roads in areas with many likely customers",
    "D": "New stores are placed far from busy roads so customers can avoid traffic",
    "E": "New stores open in the most crowded census tracts, even where few people pass by"},
  answer="C",
  explanation="Businesses use geographic data to decide where to locate. By layering traffic, competitors, and customer information, the company can find spots where lots of likely customers pass by. That usually means stores cluster along busy roads in neighborhoods that match the company's customers.",
  whyNot={
    "A": "Spacing stores evenly ignores the data the company collected. Businesses go where customers are, not one per neighborhood.",
    "B": "Cheap land does not help if few customers pass by. The company's data focus on customers and traffic.",
    "D": "Coffee shops depend on passing traffic, so busy roads attract stores instead of pushing them away.",
    "E": "Population matters, but the company also weighs traffic and competitors, so it would not ignore those layers."},
  vocab=["GIS", "geospatial data", "clustering"]))

P.append(dict(id="U1-P14", topic="1.3", lo="IMP-1.C", skill="4.C", difficulty="medium",
  stimulus=floodplain_map(),
  stem="County planners made this map in a GIS by combining a flood-risk layer with the locations of buildings. Which decision is best supported by the map?",
  options={
    "A": "Building a levee along the east bank to protect the hospital",
    "B": "Moving the school out of the shaded zone onto higher ground",
    "C": "Placing a new fire station in the shaded zone, near the most homes",
    "D": "Rezoning the shaded zone on the west bank for more new housing",
    "E": "Requiring flood insurance for the homes on higher ground east of the river"},
  answer="B",
  explanation="The shaded zone is where a big flood has a 1 percent chance of happening each year. The school sits inside that zone, so a flood could damage it and put children at risk. Moving it to higher ground outside the zone is the decision the map supports.",
  whyNot={
    "A": "The hospital is already on higher ground outside the shaded zone, so a levee there protects the wrong place.",
    "C": "Being close to homes helps, but a fire station inside the flood zone could be cut off or damaged in a flood.",
    "D": "Adding housing in the shaded zone would put more people and buildings at risk.",
    "E": "The homes east of the river are outside the shaded zone, so they face the lowest flood risk on the map."},
  vocab=["floodplain", "GIS", "layer"]))

P.append(dict(id="U1-P15", topic="1.3", lo="IMP-1.C", skill="1.D", difficulty="medium",
  stem="After an earthquake, a relief organization compares satellite images taken before and after the disaster to find blocked roads and damaged neighborhoods. How does this geographic data most directly help the organization?",
  options={
    "A": "It shows how residents feel about the government's response to the disaster",
    "B": "It predicts when and where the next earthquake in the region will strike",
    "C": "It counts how many people were living in each damaged building",
    "D": "It shows which damaged buildings were built before the city's earthquake building code",
    "E": "It helps decide where to send supplies and which roads trucks can use"},
  answer="E",
  explanation="Comparing 'before' and 'after' satellite images shows what changed: which roads are blocked and which neighborhoods are damaged. Relief groups use that to plan where to send food, water, and medicine and which roads trucks can still use. This is an organization using geographic data to make decisions.",
  whyNot={
    "A": "Images show physical damage, not people's opinions. Interviews would be needed for that.",
    "B": "Satellite images show what already happened. They cannot predict when the next earthquake will strike.",
    "C": "Images show buildings, not how many people lived inside. Census data would be needed for that.",
    "D": "Satellite images show damage, not when a building was built or what rules it followed. City records would be needed for that."},
  vocab=["remote sensing", "satellite imagery"]))
