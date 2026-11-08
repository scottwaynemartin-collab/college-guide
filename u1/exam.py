# Unit 1 exam items E01-E25
import math
E = []
def q(**k): E.append(k)

# ---------- stimulus builders ----------
def projection_grids():
    """Set A: two cylindrical world grids drawn at the same width.
    Map 1 = Mercator spacing  y = R ln tan(pi/4 + phi/2),           R = 340 / (2 pi)
    Map 2 = Gall-Peters spacing  x = R lam cos45,  y = R sin(phi) / cos45,  R = 340 / (2 pi cos45)"""
    lats = [-75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75]
    W, cy = 340, 215
    R1 = W / (2 * math.pi)
    R2 = W / (2 * math.pi * math.cos(math.radians(45)))
    y1 = {p: R1 * math.log(math.tan(math.pi / 4 + math.radians(p) / 2)) for p in lats}
    y2 = {p: R2 * math.sin(math.radians(p)) / math.cos(math.radians(45)) for p in lats}
    feats = [
      dict(kind="land", name="Map 1", polygon=[[15, 20], [395, 20], [395, 395], [15, 395]], style="small", labelAt=[205, 52]),
      dict(kind="land", name="Map 2", polygon=[[405, 20], [785, 20], [785, 395], [405, 395]], style="small", labelAt=[595, 52])]
    geo = {}
    for name, x0, ys in (("Map 1", 35, y1), ("Map 2", 425, y2)):
        top, bot = round(cy - ys[75], 1), round(cy - ys[-75], 1)
        for k in range(13):                                   # meridians every 30 degrees
            x = round(x0 + W * k / 12, 1)
            feats.append(dict(kind="line", name=f"{name} meridian", line=[[x, top], [x, bot]]))
        for p in lats:                                        # parallels every 15 degrees
            y = round(cy - ys[p], 1)
            feats.append(dict(kind="line", name=f"{name} {'Equator' if p == 0 else 'parallel'}",
                              line=[[x0, y], [x0 + W, y]], dashed=(p == 0)))
        geo[name] = {p: round(cy - ys[p], 1) for p in lats}
    stim = dict(type="schematicMap",
      title="TWO WORLD MAP GRIDS DRAWN AT THE SAME WIDTH: LINES OF LATITUDE EVERY 15° (75° S TO 75° N) AND LONGITUDE EVERY 30°",
      canvas=dict(width=800, height=410),
      features=feats,
      legend=[dict(swatch="road", label="Equator (0°)")],
      description="Two rectangular grids of the same width. Each shows the same lines of latitude (every 15 degrees, from 75° S at the bottom to 75° N at the top) and the same lines of longitude (every 30 degrees). On both maps, lines of longitude are straight, parallel, and evenly spaced. On Map 1, the gaps between lines of latitude grow wider toward the poles. On Map 2, the gaps between lines of latitude grow narrower toward the poles.",
      source="Grid spacing computed from two standard world map projection formulas")
    return stim, geo

def commute_map():
    """Set C: functional region of City M. 6 px = 1 km. Towns placed at stated distances from the city center."""
    cx, cy, ppk = 400, 220, 6
    towns = [  # name, km, bearing (deg, 0 = east, counterclockwise, screen y is down), percent commuting to City M
      ("A", 14, 90, 64), ("B", 18, 225, 57), ("C", 30, 0, 41), ("D", 36, 150, 32), ("E", 52, 190, 14), ("F", 58, -15, 8)]
    feats = [dict(kind="land", name="", polygon=[[0, 0], [800, 0], [800, 440], [0, 440]])]
    boxes = {}
    for name, km, deg, pct in towns:
        x = cx + km * ppk * math.cos(math.radians(deg)); y = cy - km * ppk * math.sin(math.radians(deg))
        x, y = round(x, 1), round(y, 1)
        boxes[name] = (x, y, km, pct)
        feats.append(dict(kind="land", name=f"Town {name} {pct}%", style="small", labelAt=[x, y],
                          polygon=[[x - 40, y - 22], [x + 40, y - 22], [x + 40, y + 22], [x - 40, y + 22]]))
    feats.append(dict(kind="land", name="City M", style="power", labelAt=[cx, cy],
                      polygon=[[cx - 55, cy - 24], [cx - 30, cy - 32], [cx + 40, cy - 30], [cx + 56, cy - 8],
                               [cx + 50, cy + 26], [cx + 5, cy + 32], [cx - 48, cy + 24]]))
    def edge(ux, uy, hw, hh):                                  # distance from a box center to its edge along (ux, uy)
        return min(hw / abs(ux) if abs(ux) > 1e-9 else 1e9, hh / abs(uy) if abs(uy) > 1e-9 else 1e9)
    for name, (x, y, km, pct) in boxes.items():               # commuting flows toward City M
        dx, dy = cx - x, cy - y; d = math.hypot(dx, dy); ux, uy = dx / d, dy / d
        s = edge(ux, uy, 40, 22) + 5; e = edge(ux, uy, 56, 32) + 6
        feats.append(dict(kind="arrow", name=f"Commuters from Town {name} to City M",
                          **{"from": [round(x + ux * s, 1), round(y + uy * s, 1)], "to": [round(cx - ux * e, 1), round(cy - uy * e, 1)]}))
    boundary = [[150, 75], [470, 75], [650, 160], [655, 270], [560, 330], [380, 345], [260, 340], [170, 250], [150, 150], [150, 75]]
    feats.append(dict(kind="shippingLane", name="Edge of City M's commuting zone", line=boundary, dashed=True))
    feats.append(dict(kind="scaleBar", label="0 — 10 km", **{"from": [30, 415], "to": [90, 415]}))
    stim = dict(type="schematicMap",
      title="DAILY COMMUTING TO CITY M FROM SIX NEARBY TOWNS (HYPOTHETICAL DATA)",
      canvas=dict(width=800, height=440),
      features=feats,
      legend=[dict(swatch="power", label="City M"), dict(swatch="small", label="Town, with the percent of its workers who commute to City M"),
              dict(swatch="lane", label="Dashed line: towns where 25% or more of workers commute to City M")],
      description="City M is at the center. Arrows show daily commuting from six towns to jobs in City M. Each town is labeled with the percent of its workers who commute to City M: Town A, 14 km from City M, 64%; Town B, 18 km, 57%; Town C, 30 km, 41%; Town D, 36 km, 32%; Town E, 52 km, 14%; Town F, 58 km, 8%. A dashed line encloses City M and Towns A, B, C, and D.",
      source="Hypothetical data")
    return stim, dict(boxes=boxes, boundary=boundary, city=(cx, cy), ppk=ppk)

PROJ, PROJ_GEO = projection_grids()
COMMUTE, COMMUTE_GEO = commute_map()

LANDCOVER = dict(type="bar",
  title="LAND COVER IN RIVER COUNTY, 2005 AND 2025 (HYPOTHETICAL DATA)",
  categories=["Forest", "Cropland", "Wetland", "Built-up land", "Water"],
  series=[dict(name="2005", values=[34, 38, 12, 10, 6]), dict(name="2025", values=[30, 31, 7, 26, 6])],
  yLabel="Percent of county area", yMax=40,
  text="Built-up land includes buildings, roads, and parking lots.",
  description="A grouped bar chart of land cover as a percent of River County's area. Forest: 34 percent in 2005 and 30 percent in 2025. Cropland: 38 and 31. Wetland: 12 and 7. Built-up land: 10 and 26. Water: 6 and 6.",
  source="Hypothetical data")

SCALES = dict(type="table",
  title="POPULATION CHANGE IN COUNTRY Y AT THREE SCALES, 2015–2025 (HYPOTHETICAL DATA)",
  columns=["Area", "Population, 2015 (millions)", "Population, 2025 (millions)", "Change (%)"],
  rows=[
    ["Country Y (national)", "20.00", "20.40", "+2.0"],
    ["Province 1", "8.00", "8.64", "+8.0"],
    ["Province 2", "7.00", "6.65", "−5.0"],
    ["Province 3", "5.00", "5.11", "+2.2"],
    ["Province 2: Capital District", "2.00", "2.12", "+6.0"],
    ["Province 2: River District", "3.00", "2.73", "−9.0"],
    ["Province 2: Hill District", "2.00", "1.80", "−10.0"]],
  description="A table of population in 2015 and 2025 for Country Y as a whole, for its three provinces, and for the three districts that make up Province 2.",
  source="Hypothetical data")

# ---------------- items ----------------
q(id="U1-E01", n=1, topic="1.1", lo="IMP-1.A", skill="3.A", difficulty="easy",
  stem="A geographer wants to map the percentage of residents age 65 or older in each county of a state. Which type of map is best suited to this purpose?",
  options={"A": "Dot density map", "B": "Graduated symbol map", "C": "Choropleth map", "D": "Isoline map", "E": "Cartogram"},
  answer="C",
  rationales={
    "A": "Incorrect. A dot density map shows counts, with each dot standing for a set number of people or things. It is not well suited to showing a percentage for each county.",
    "B": "Incorrect. A graduated symbol map uses symbols of different sizes, usually to show totals at point locations such as cities, not percentages for whole areas.",
    "C": "Correct. A choropleth map shades predefined areas, such as counties, by a rate or percentage, with darker shades usually showing higher values.",
    "D": "Incorrect. An isoline map connects points of equal value, such as elevation or temperature, that vary continuously across space rather than by county.",
    "E": "Incorrect. A cartogram resizes areas in proportion to a variable, which would distort the counties rather than shade them by percentage."},
  explanation="Choropleth maps color whole areas, like counties or states, by a rate or percentage. Darker usually means higher. The percent of residents age 65 or older in each county is a perfect fit.")

q(id="U1-E02", n=2, topic="1.1", lo="IMP-1.A", skill="3.A", difficulty="medium",
  stem="Which type of map would best show the total number of passengers using each of a country's 25 busiest airports?",
  options={
    "A": "A graduated symbol map with circles at each airport sized by its total",
    "B": "A choropleth map shading each state by its number of airport passengers",
    "C": "An isoline map connecting airports that have equal numbers of passengers",
    "D": "A reference map showing the location and name of each airport",
    "E": "A dot density map with one dot for each airport in the country"},
  answer="A",
  rationales={
    "A": "Correct. A graduated symbol map places a symbol at each location and scales its size to the quantity, which suits totals at point locations such as airports.",
    "B": "Incorrect. Shading whole states would hide which airports carry the traffic, and choropleth maps are better suited to rates than to raw totals.",
    "C": "Incorrect. Isolines represent a continuous surface such as elevation or temperature; passenger counts at separate airports do not form a continuous surface.",
    "D": "Incorrect. A reference map would show where the airports are but not how many passengers each one handles.",
    "E": "Incorrect. One dot per airport shows only where airports are; it would not show differences in passenger totals."},
  explanation="Graduated symbol maps put a symbol, usually a circle, at each place and make it bigger for bigger numbers. A big circle means a busy airport, and a small circle means a less busy one.")

# ---- Set A: projection grids, E03-E04 ----
q(id="U1-E03", n=3, set="grids", topic="1.1", lo="IMP-1.A", skill="4.D", difficulty="medium",
  stimulus=PROJ,
  stem="Which statement best describes how Map 1 differs from Map 2?",
  options={
    "A": "Map 1 keeps the areas of high-latitude places accurate, while Map 2 enlarges them",
    "B": "Map 1 is an azimuthal projection centered on a pole, while Map 2 is cylindrical",
    "C": "Map 1 keeps distances true across the map, while Map 2 distorts distances",
    "D": "Map 1 increasingly enlarges areas toward the poles; Map 2 keeps relative areas correct",
    "E": "Map 1 and Map 2 distort area in the same way, since both show the same parallels"},
  answer="D",
  rationales={
    "A": "Incorrect. This reverses the two maps. On Map 1 the parallels spread farther apart toward the poles while the meridians stay the same distance apart, so high-latitude areas are enlarged.",
    "B": "Incorrect. Both grids are cylindrical: their meridians are straight, parallel, and evenly spaced. An azimuthal polar projection would show meridians radiating from a central pole.",
    "C": "Incorrect. Neither grid keeps distances true across the whole map; on both, every parallel is drawn as long as the equator, so east–west scale grows toward the poles.",
    "D": "Correct. Map 1's spacing between parallels grows toward the poles, as on the Mercator projection, so high-latitude areas are enlarged. Map 2's spacing shrinks toward the poles, offsetting the east–west stretching so that relative areas stay correct, as on equal-area cylindrical projections such as the Gall-Peters.",
    "E": "Incorrect. The grids show the same parallels, but the spacing between them differs, and that spacing determines how area is distorted."},
  explanation="Look at the gaps between the flat lines. On Map 1 the gaps get bigger near the poles, so places there get stretched taller as well as wider and look too big, like Greenland on a Mercator map. On Map 2 the gaps get smaller near the poles, which squeezes places back down so their areas stay correct, like on a Gall-Peters map.")

q(id="U1-E04", n=4, set="grids", topic="1.1", lo="IMP-1.A", skill="4.F", difficulty="hard",
  stem="Which statement best describes a limitation of Map 2?",
  options={
    "A": "It enlarges the area of Canada and Russia compared with Brazil and India",
    "B": "It flattens the shapes of high-latitude places, squeezing them north to south",
    "C": "It keeps compass bearings as straight lines, so it is useful mainly for sea navigation",
    "D": "It shows true distances from its center point but distorts areas elsewhere",
    "E": "It is a compromise map with small distortions of area, shape, distance, and direction"},
  answer="B",
  rationales={
    "A": "Incorrect. That describes Map 1. Map 2's narrowing spacing toward the poles keeps relative areas correct, so Canada and Russia are not enlarged compared with Brazil and India.",
    "B": "Correct. To keep area true, an equal-area cylindrical map shrinks north–south distances toward the poles while east–west distances are stretched, so high-latitude landmasses look flattened. Equal-area maps give up correct shape.",
    "C": "Incorrect. Showing compass bearings as straight lines is the strength of the Mercator projection, the type shown in Map 1, not of an equal-area map.",
    "D": "Incorrect. True distances from a center point are a property of azimuthal equidistant projections, which are built around a center point rather than a rectangular grid.",
    "E": "Incorrect. Compromise projections such as the Robinson spread small distortions across all four properties; Map 2 keeps area exact and gives up correct shape."},
  explanation="Every map projection gives something up. Map 2 keeps areas correct, but to do that it squishes places near the poles from top to bottom, so their shapes look flat and wide. You can trust Map 2 for comparing sizes, not shapes.")

q(id="U1-E05", n=5, topic="1.1", lo="IMP-1.A", skill="1.B", difficulty="medium",
  stem="A subway map shows each line as a straight colored path with evenly spaced stations, even though the real tracks curve and the stations are different distances apart. Which statement best explains why the mapmaker drew it this way?",
  options={
    "A": "The mapmaker lacked accurate GPS data on the location of each station",
    "B": "Subway maps are reference maps, which require exact distances and shapes",
    "C": "The map is an isoline map that connects stations with equal numbers of riders",
    "D": "Map projections badly distort shape and area on maps of small areas such as a city",
    "E": "All maps are selective, and this one trades true distance for clear connections"},
  answer="E",
  rationales={
    "A": "Incorrect. The simplification is a deliberate design choice; accurate location data are easy to obtain, and the map leaves them out on purpose.",
    "B": "Incorrect. Reference maps help users locate places, but no map shows everything exactly; this map deliberately gives up true distance.",
    "C": "Incorrect. Isoline maps connect points of equal value on a continuous surface; subway lines connect stations along a route.",
    "D": "Incorrect. Projection distortion is very small over an area as small as a city, so it cannot explain straightened lines and evenly spaced stations.",
    "E": "Correct. All maps are selective in the information they show. A transit map gives up accurate distance and shape to make routes, transfers, and the order of stations easy to read."},
  explanation="Every map leaves things out or changes things on purpose. A subway rider needs to know the order of the stops and where to switch lines, not the exact curve of the tracks. So the mapmaker straightened the lines to make the map easy to use.")

q(id="U1-E06", n=6, topic="1.2", lo="IMP-1.B", skill="1.D", difficulty="easy",
  stem="A delivery app shows customers exactly where their driver is as the driver moves through the city. The app most directly relies on which geospatial technology to find the driver's position?",
  options={
    "A": "A satellite navigation system such as GPS",
    "B": "Remote sensing images taken by satellites",
    "C": "A national census of population and housing",
    "D": "Field interviews with drivers and customers",
    "E": "A choropleth map of the city's neighborhoods"},
  answer="A",
  rationales={
    "A": "Correct. Satellite navigation systems such as the Global Positioning System (GPS) use signals from satellites to calculate a receiver's position, which the app can display in real time.",
    "B": "Incorrect. Remote sensing gathers images or other data about Earth's surface from a distance; it does not track the position of a phone in a moving car.",
    "C": "Incorrect. A census counts people and housing at set times; it cannot locate a moving driver.",
    "D": "Incorrect. Interviews collect qualitative information about people's experiences, not precise real-time positions.",
    "E": "Incorrect. A choropleth map shades areas by a rate or percentage; it does not track the position of anything."},
  explanation="GPS uses signals from satellites to figure out exactly where a phone or other receiver is. The driver's phone finds its spot with GPS, and the app shows that spot on a map.")

q(id="U1-E07", n=7, topic="1.2", lo="IMP-1.B", skill="1.A", difficulty="medium",
  stem="A geographer studying a neighborhood's history reads letters written by early settlers, newspaper stories from the 1920s, and a city planning report from 1965. These sources are best described as",
  options={
    "A": "geospatial data collected with remote sensing",
    "B": "quantitative data gathered by a national census",
    "C": "written accounts that provide spatial information",
    "D": "layers created with a geographic information system",
    "E": "field data collected with a satellite navigation system"},
  answer="C",
  rationales={
    "A": "Incorrect. Remote sensing collects data from a distance, such as satellite images, not letters or reports.",
    "B": "Incorrect. Census data are counts of people and housing collected by a government; letters and news stories are written accounts.",
    "C": "Correct. The AP course framework lists written accounts, such as field observations, media reports, travel narratives, policy documents, and personal interviews, as sources of spatial information. Settlers' letters, old newspaper stories, and a planning report fit this category.",
    "D": "Incorrect. A GIS is a tool for storing and analyzing data in layers; the sources themselves are written documents.",
    "E": "Incorrect. Satellite navigation systems such as GPS record precise positions; they do not produce letters or reports."},
  explanation="Letters, newspaper stories, and government reports are written accounts. Geographers use them to learn what places were like and how people saw them. They are not numbers from a census or pictures from a satellite.")

# ---- Set D: land cover chart, E08-E09 ----
q(id="U1-E08", n=8, set="landcover", topic="1.2", lo="IMP-1.B", skill="3.A", difficulty="medium",
  stimulus=LANDCOVER,
  stem="The land-cover data in the chart were most likely gathered by",
  options={
    "A": "a satellite navigation system that tracks the position of moving vehicles",
    "B": "remote sensing, using images of the county taken from satellites",
    "C": "a census that asks each household how its land is used",
    "D": "interviews with longtime residents about how the county has changed",
    "E": "a GIS, which creates new land-cover data without outside sources"},
  answer="B",
  rationales={
    "A": "Incorrect. Satellite navigation systems such as GPS record the positions of receivers; they do not measure how much of a county is forest, cropland, or built-up land.",
    "B": "Correct. Remote sensing gathers information about Earth's surface from a distance. Sorting satellite images into land-cover types is the usual way to measure land cover across a whole county and to compare different years.",
    "C": "Incorrect. A census counts people and housing; it does not measure land cover such as forest or wetland across an entire county.",
    "D": "Incorrect. Interviews provide qualitative information about people's experiences; they cannot produce consistent land-cover percentages for two different years.",
    "E": "Incorrect. A GIS stores, analyzes, and displays data, but the land-cover data must first be collected, usually by remote sensing."},
  explanation="To measure how much of a whole county is forest, farmland, or city, you need a view from above. Satellites take pictures from space, and computers sort the pictures into land types. That is remote sensing.")

q(id="U1-E09", n=9, set="landcover", topic="1.5", lo="PSO-1.B", skill="3.C", difficulty="medium",
  stem="Which conclusion about human–environment interaction is best supported by the chart?",
  options={
    "A": "Environmental determinism explains the changes, since nature decided the county's land use",
    "B": "Because cropland shrank, the county's farms are producing less food than in 2005",
    "C": "The loss of wetland was caused by changes in rainfall rather than by human activity",
    "D": "Land use in the county became more sustainable, since the area of water stayed the same",
    "E": "Built-up land grew as natural land covers such as forest and wetland shrank"},
  answer="E",
  rationales={
    "A": "Incorrect. Environmental determinism holds that the physical environment controls human activity. The chart shows people changing the environment, which runs the other way.",
    "B": "Incorrect. The chart shows the area of cropland, not crop output; farms can produce as much or more on less land if yields rise.",
    "C": "Incorrect. The chart gives no rainfall data, and the growth of built-up land points to human activity as a likely cause of land-cover change.",
    "D": "Incorrect. An unchanged water area does not show sustainability, especially when wetland and forest, which provide habitat and can absorb floodwater, declined.",
    "E": "Correct. Built-up land rose from 10 to 26 percent of the county while forest fell from 34 to 30 percent and wetland from 12 to 7 percent, showing people reshaping the environment through land use."},
  explanation="Built-up land (buildings, roads, and parking lots) went from 10% to 26% of the county. At the same time, forest and wetland got smaller. People changed the land to fit their needs. That is human–environment interaction.")

q(id="U1-E10", n=10, topic="1.3", lo="IMP-1.C", skill="2.C", difficulty="medium",
  stem="Between two censuses, State A's population grew much faster than the U.S. population as a whole, while State B's population stayed about the same. Based on the new census data, which outcome is most likely?",
  options={
    "A": "State A is likely to lose seats in the U.S. Senate, and State B may gain one",
    "B": "Both states keep the same number of House seats, since the number of seats per state is fixed",
    "C": "State A's boundary expands to include part of a neighboring state",
    "D": "State A is likely to gain House seats, and State B may lose one",
    "E": "State B is likely to gain House seats to make up for its slower growth"},
  answer="D",
  rationales={
    "A": "Incorrect. Every state has two senators regardless of population, so census results do not change Senate seats.",
    "B": "Incorrect. The total of 435 House seats is set by law, but how those seats are divided among the states is recalculated after every census.",
    "C": "Incorrect. State boundaries do not change after a census; only the apportionment of House seats does.",
    "D": "Correct. After each census, the 435 House seats are reapportioned according to each state's population. A state growing faster than the country is likely to gain seats, and a state with little growth may lose seats.",
    "E": "Incorrect. Seats follow population; a state that grows slowly compared with the country tends to lose seats, not gain them."},
  explanation="The 435 House seats are divided up by population after every census. If a state grows faster than the rest of the country, it usually gets more seats. If it does not grow, it can lose a seat to a faster-growing state.")

q(id="U1-E11", n=11, topic="1.4", lo="PSO-1.A", skill="1.A", difficulty="easy",
  stem="Which of the following statements describes a town's relative location?",
  options={
    "A": "The town hall stands at 35.2° N latitude and 97.4° W longitude.",
    "B": "The town lies 60 kilometers upstream from the river's mouth.",
    "C": "The town is home to about 25,000 people.",
    "D": "The town's hilly land and rocky soil limit farming.",
    "E": "The town's name comes from a local word for \"meeting place.\""},
  answer="B",
  rationales={
    "A": "Incorrect. Latitude and longitude give absolute location, a position that does not depend on other places.",
    "B": "Correct. Relative location describes a place in relation to other places or features, here the river's mouth.",
    "C": "Incorrect. Population size is a characteristic of the place, not a description of where it is.",
    "D": "Incorrect. Hilly land and rocky soil describe the town's site, its physical setting, not its position relative to other places.",
    "E": "Incorrect. A place name, or toponym, can reveal history or culture but does not describe location."},
  explanation="Relative location tells where a place is compared to something else, like \"60 kilometers upstream from the river's mouth.\" Absolute location uses exact coordinates instead.")

q(id="U1-E12", n=12, topic="1.4", lo="PSO-1.A", skill="1.B", difficulty="medium",
  stem="Engineers in two countries on opposite sides of the world work on the same design in real time using video calls and shared online files. This situation best illustrates",
  options={
    "A": "time-space compression, because technology reduces the effect of distance",
    "B": "distance decay, because the engineers interact less as the distance between them grows",
    "C": "absolute distance, because the two countries are now closer together",
    "D": "a functional region centered on the engineers' main office",
    "E": "a formal region, because the engineers share the same profession"},
  answer="A",
  rationales={
    "A": "Correct. Time-space compression is the reduced importance of distance as transportation and communication technologies speed the movement of people, goods, and information. Real-time collaboration across the world is an example.",
    "B": "Incorrect. Distance decay predicts less interaction with greater distance; here the engineers interact closely despite great distance, which shows distance decay being weakened.",
    "C": "Incorrect. The absolute distance between the countries has not changed; what changed is how much that distance limits interaction.",
    "D": "Incorrect. Nothing in the scenario describes a central office drawing in flows; it describes distance mattering less.",
    "E": "Incorrect. A shared profession could help define a formal region, but the scenario is about technology overcoming distance, not about a region."},
  explanation="Time-space compression means the world feels smaller because technology lets people connect quickly over long distances. Video calls let engineers on opposite sides of Earth work together as if they were in the same room.")

# ---- Set C: commuting map, E13-E15 ----
q(id="U1-E13", n=13, set="commute", topic="1.7", lo="SPS-1.A", skill="1.D", difficulty="medium",
  stimulus=COMMUTE,
  stem="The area inside the dashed line on the map is best described as which type of region?",
  options={
    "A": "A formal region, because the towns share the same government",
    "B": "A perceptual region, because residents feel they belong to City M",
    "C": "A functional region, tied together by daily commuting to City M",
    "D": "A formal region, because it is drawn using a measured percentage",
    "E": "A functional region, because its towns share a uniform climate and landscape"},
  answer="C",
  rationales={
    "A": "Incorrect. The map gives no information about a shared government; the towns are grouped by their connections to City M.",
    "B": "Incorrect. A perceptual region is based on people's feelings or images of a place; the map shows measured commuting, not feelings.",
    "C": "Correct. A functional (nodal) region is organized around a central node and defined by flows and connections to it. The dashed line encloses the towns most strongly linked to City M by daily commuting.",
    "D": "Incorrect. The 25 percent threshold measures each town's connection to City M. A region defined by flows to a node is functional, even when a number is used to draw its edge.",
    "E": "Incorrect. A shared climate and landscape would define a formal region; this region is defined by commuting to City M, not by a uniform trait."},
  explanation="A functional region is built around a center, called the node, and is held together by movement to it. Here, workers from the towns travel to jobs in City M every day. The dashed line wraps around the towns most connected to City M. The 25% line is a number, but what it measures is trips to City M. A region held together by trips to a center is functional, not formal.")

q(id="U1-E14", n=14, set="commute", topic="1.4", lo="PSO-1.A", skill="3.B", difficulty="easy",
  stem="Which concept best explains the pattern of commuting percentages shown on the map?",
  options={
    "A": "Time-space compression, because commuters from distant towns reach City M fastest",
    "B": "Clustering, because the towns are bunched tightly around City M",
    "C": "Relative location, because each town's latitude and longitude set its commuting share",
    "D": "Environmental determinism, because the landscape forces workers to commute",
    "E": "Distance decay, because the share commuting to City M falls as distance increases"},
  answer="E",
  rationales={
    "A": "Incorrect. The farthest towns have the lowest commuting shares, so distance still limits interaction; time-space compression would weaken this pattern.",
    "B": "Incorrect. Clustering describes how features are arranged; the towns lie at different distances from City M, and the key pattern is that commuting shares fall with that distance.",
    "C": "Incorrect. Latitude and longitude describe absolute location. The pattern depends on each town's distance from City M.",
    "D": "Incorrect. The map shows no physical barriers, and commuting is a choice shaped by travel time and cost, not by the landscape alone.",
    "E": "Correct. Distance decay is the decline in interaction between places as the distance between them increases. Towns nearest City M send the largest shares of workers; the farthest towns send the smallest."},
  explanation="Close towns send lots of workers to City M, and far towns send only a few. The farther away a town is, the smaller the share. That drop-off with distance is distance decay.")

q(id="U1-E15", n=15, set="commute", topic="1.4", lo="PSO-1.A", skill="2.C", difficulty="hard",
  stem="Suppose a fast commuter rail line opened between City M and Town F. Which change would most likely follow?",
  options={
    "A": "Town F's commuting share would fall, because rail weakens ties to City M",
    "B": "City M's functional region would shrink toward the towns nearest the city",
    "C": "Town F would form its own formal region of rail commuters",
    "D": "Town F's commuting share would rise, which could bring it inside the dashed line",
    "E": "Distance decay would increase, because the trip from Town F would take longer"},
  answer="D",
  rationales={
    "A": "Incorrect. Faster transportation lowers the time cost of travel, which strengthens, not weakens, a town's connection to the central city.",
    "B": "Incorrect. Better transportation tends to extend a functional region outward, not shrink it.",
    "C": "Incorrect. Using the same mode of transportation does not create a formal region; the rail line would tie Town F more closely to City M's functional region.",
    "D": "Correct. A fast rail line would cut travel time, an example of time-space compression that weakens distance decay. More of Town F's workers would likely commute to City M, which could push its share above the 25 percent threshold and extend the functional region.",
    "E": "Incorrect. A fast rail line would shorten the trip, reducing the effect of distance rather than increasing it."},
  explanation="A fast train makes Town F feel closer to City M because the trip takes less time. More people from Town F would take jobs in City M. If enough of them do, Town F could end up inside City M's commuting region.")

q(id="U1-E16", n=16, topic="1.5", lo="PSO-1.B", skill="1.C", difficulty="medium",
  stem="Which of the following statements best reflects possibilism rather than environmental determinism?",
  options={
    "A": "A dry climate limits farming, but people can choose to irrigate, herd, or trade",
    "B": "A region's climate decides what kind of economy its people will have",
    "C": "Mountain landscapes cause the people who live in them to develop the same customs",
    "D": "Societies near the sea become sea traders because the coast controls their choices",
    "E": "The physical environment has no effect on how people live or what they grow"},
  answer="A",
  rationales={
    "A": "Correct. Possibilism holds that the physical environment sets limits and offers opportunities, but people choose among options based on their culture and technology.",
    "B": "Incorrect. Claiming that climate decides a region's economy is environmental determinism, the view that the environment controls human activity.",
    "C": "Incorrect. Claiming that a landscape causes people to share customs is environmental determinism.",
    "D": "Incorrect. Saying that the coast controls people's choices is environmental determinism; possibilism would say the coast offers options that people may or may not use.",
    "E": "Incorrect. Possibilism does not deny the environment's influence; it treats the environment as setting limits within which people make choices."},
  explanation="Determinism says nature decides what people do. Possibilism says nature sets limits, but people choose what to do within those limits. A dry place limits farming, but people can still pick irrigation, herding, or trade.")

q(id="U1-E17", n=17, topic="1.5", lo="PSO-1.B", skill="1.D", difficulty="easy",
  stem="A town that depends on a nearby forest for timber decides to cut no more trees each year than the forest regrows and to replant the areas it harvests. Which concept does this policy best reflect?",
  options={
    "A": "Environmental determinism, because the forest controls the town's economy",
    "B": "Sustainability, because it meets today's needs without using up the forest",
    "C": "Nonrenewable resource use, because cut trees cannot be replaced",
    "D": "Distance decay, because the town relies on the forest closest to it",
    "E": "Resource depletion, because the town removes trees from the forest each year"},
  answer="B",
  rationales={
    "A": "Incorrect. The town made a deliberate choice about how much to harvest; environmental determinism holds that the environment controls human activity.",
    "B": "Correct. Sustainability means using resources to meet present needs without compromising the ability of future generations to meet their own needs. Harvesting no more than regrows, and replanting, keeps the forest productive.",
    "C": "Incorrect. Trees are a renewable resource; they regrow, which is what makes this policy possible.",
    "D": "Incorrect. The forest is nearby, but the policy is about how much to harvest over time, not about how interaction changes with distance.",
    "E": "Incorrect. Harvesting a renewable resource does not deplete it when the harvest stays within the rate of regrowth."},
  explanation="Sustainability means using what you need now while leaving enough for the future. Cutting only as many trees as grow back, and replanting, means the forest will still be there for people later.")

# ---- Set B: three-scale table, E18-E20 ----
q(id="U1-E18", n=18, set="scales", topic="1.6", lo="PSO-1.D", skill="5.B", difficulty="medium",
  stimulus=SCALES,
  stem="Which statement is best supported by comparing the national data with the provincial data?",
  options={
    "A": "The national growth rate accurately describes the change in each province",
    "B": "Province 3's growth was caused by people moving there from Province 2",
    "C": "Modest national growth hides a population decline in one province",
    "D": "Province 2's decline means Country Y is likely to lose population soon",
    "E": "Province 1 grew fastest because it has the largest land area"},
  answer="C",
  rationales={
    "A": "Incorrect. Provincial changes range from a gain of 8.0 percent to a loss of 5.0 percent, so the national figure of +2.0 percent does not describe each province.",
    "B": "Incorrect. The table shows population change but not migration flows; it cannot show where Province 3's new residents came from.",
    "C": "Correct. At the national scale Country Y grew by 2.0 percent, but at the provincial scale Province 2 lost 5.0 percent. Changing the scale of analysis reveals variation that the national figure hides.",
    "D": "Incorrect. Growth in Provinces 1 and 3 more than offset Province 2's loss; the data do not show that the national population is about to fall.",
    "E": "Incorrect. The table contains no data on land area, so it cannot support a claim about why Province 1 grew fastest."},
  explanation="The whole country grew a little (+2.0%). But zoom in to the provinces and you see Province 2 actually lost people (−5.0%). The national number hid that. Changing the scale shows a different pattern.")

q(id="U1-E19", n=19, set="scales", topic="1.6", lo="PSO-1.D", skill="5.C", difficulty="hard",
  stem="Which conclusion is best supported by the district-level data for Province 2?",
  options={
    "A": "River and Hill districts shrank because they are farthest from Country Y's capital",
    "B": "The Capital District's growth shows that Province 2 as a whole is growing",
    "C": "District data add little, since they show the same pattern as provincial data",
    "D": "The Capital District grew because it has a higher birth rate than other districts",
    "E": "The Capital District grew even though Province 2 as a whole lost people"},
  answer="E",
  rationales={
    "A": "Incorrect. The table gives no information about where the districts are or how far they are from the national capital, so it cannot support this explanation.",
    "B": "Incorrect. Province 2 lost 5.0 percent overall; growth in one district did not offset losses in the other two.",
    "C": "Incorrect. The district data reveal a growing Capital District that the provincial figure of −5.0 percent hides, so they add important information.",
    "D": "Incorrect. The table shows population totals, not birth rates; the growth could come from migration, births, or both.",
    "E": "Correct. The Capital District grew by 6.0 percent while Province 2 as a whole fell by 5.0 percent. Analysis at a finer scale reveals growth within a declining province, a pattern that could reflect people moving from the River and Hill districts to the Capital District."},
  explanation="Province 2 shrank overall. But zooming in again shows that its Capital District grew by 6%, while the other two districts lost a lot of people. One more change of scale reveals one more hidden pattern.")

q(id="U1-E20", n=20, set="scales", topic="1.3", lo="IMP-1.C", skill="3.F", difficulty="hard",
  stem="Country Y's national government will fund new primary schools based on where population is growing. Which approach would most likely lead to the best decisions?",
  options={
    "A": "Use the national rate of 2.0 percent and divide new schools equally among provinces",
    "B": "Use provincial data alone, building no new schools anywhere in Province 2",
    "C": "Wait for the next census, since current data do not show where people live",
    "D": "Use district-level data so places like the Capital District are not missed",
    "E": "Use provincial data and build the most schools in Province 2, since it lost the most people"},
  answer="D",
  rationales={
    "A": "Incorrect. The national rate hides large differences among provinces and districts, so dividing schools equally would send some to places that are shrinking.",
    "B": "Incorrect. Province 2 lost population overall, but its Capital District grew by 6.0 percent; ignoring the whole province would overlook a growing area.",
    "C": "Incorrect. The table already shows where population grew and shrank; waiting would delay decisions without adding needed information.",
    "D": "Correct. Geographic data are used at all scales for government decision-making. Finer-scale data reveal growth that provincial or national figures hide, such as the Capital District's 6.0 percent increase within a shrinking province.",
    "E": "Incorrect. New schools are needed where population is growing; Province 2 lost population overall, and most of its loss came in River and Hill districts."},
  explanation="The most detailed data show exactly where the number of people is going up. Province 2 shrank overall, but its Capital District grew. If the government looked only at provinces, it would miss that spot. Using smaller-scale data helps put schools where they are needed.")

q(id="U1-E21", n=21, topic="1.6", lo="PSO-1.C", skill="5.A", difficulty="easy",
  stem="A study compares rates of internet access among the countries of Southeast Asia. At which scale of analysis is this study?",
  options={
    "A": "Global, because it compares countries",
    "B": "Regional, because it covers one part of the world",
    "C": "National, because each country reports its own data",
    "D": "Local, because internet access is measured in each household",
    "E": "Global, because the internet connects the whole world"},
  answer="B",
  rationales={
    "A": "Incorrect. Comparing countries does not make a study global; the global scale covers the whole world, while this study covers only Southeast Asia.",
    "B": "Correct. The regional scale refers to a part of the world larger than one country, such as Southeast Asia, or to a large area within a country. Comparing Southeast Asian countries is regional-scale analysis.",
    "C": "Incorrect. The national scale examines patterns within one country; this study compares several countries.",
    "D": "Incorrect. Data may be collected from households, but the scale of analysis is set by the area the study covers: a world region.",
    "E": "Incorrect. The internet is global, but the study covers only one world region."},
  explanation="Scale of analysis means the size of the area you are studying. Southeast Asia is one part of the world: bigger than one country but smaller than the whole planet. That is the regional scale.")

q(id="U1-E22", n=22, topic="1.7", lo="SPS-1.A", skill="1.A", difficulty="medium",
  stem="When residents of a state were asked to draw the boundaries of \"the Hill Country\" on a blank map, their drawings overlapped in the middle but differed a lot at the edges. \"The Hill Country\" is best described as",
  options={
    "A": "a perceptual region, based on people's ideas about an area",
    "B": "a formal region, based on a single trait such as elevation",
    "C": "a functional region, based on travel to a central city",
    "D": "a perceptual region, based on a boundary set by state law",
    "E": "a functional region, based on shared tourism businesses"},
  answer="A",
  rationales={
    "A": "Correct. Perceptual (vernacular) regions exist in people's minds and reflect shared ideas and feelings about a place. Different people draw their boundaries in different places, so the edges are fuzzy.",
    "B": "Incorrect. A formal region defined by elevation would have boundaries drawn from data, so residents' drawings would not need to differ.",
    "C": "Incorrect. A functional region is defined by connections to a central node, such as commuting to a city; the drawings reflect people's images of an area, not travel patterns.",
    "D": "Incorrect. A boundary set by law would be the same on every map and would not depend on people's ideas; the drawings differ because no official boundary exists.",
    "E": "Incorrect. Tourism businesses could form part of a network, but the region in the question is defined by how residents picture it."},
  explanation="Perceptual regions live in people's heads. Everyone agrees about the middle, but people draw the edges in different places. That fuzzy, disagree-at-the-edges pattern is the sign of a perceptual region.")

q(id="U1-E23", n=23, topic="1.7", lo="SPS-1.A", skill="2.A", difficulty="medium",
  stem="On a map of the languages spoken at home in a border area, the share of people who speak Language X falls gradually from 90 percent to 10 percent over about 50 kilometers, with many bilingual towns in between. Which statement best describes the boundary of the Language X region?",
  options={
    "A": "It is a sharp line that follows the international border",
    "B": "It is a functional boundary based on travel to one city",
    "C": "It is a perceptual boundary, since the language people speak cannot be measured",
    "D": "It is set by law, so mapmakers place it in the same spot",
    "E": "It is a transition zone where the region blends into its neighbor"},
  answer="E",
  rationales={
    "A": "Incorrect. The share of Language X speakers changes gradually across about 50 kilometers, so there is no single sharp line.",
    "B": "Incorrect. The region is defined by a shared trait, the language people speak, not by flows to a central city.",
    "C": "Incorrect. The language spoken at home can be measured with surveys or census data; this is a formal region based on a measurable trait.",
    "D": "Incorrect. Language regions are not set by law; different mapmakers might draw the edge at different percentages.",
    "E": "Correct. Regional boundaries are often transitional. Here the Language X region fades into its neighbor across a zone of bilingual towns rather than ending at a sharp line."},
  explanation="Regions often do not have sharp edges. As you travel across this border area, Language X becomes less and less common, and many towns speak two languages. That in-between area is a transition zone.")

q(id="U1-E24", n=24, topic="1.7", lo="SPS-1.A", skill="1.B", difficulty="hard",
  stem="Maps of \"the Middle East\" made by different governments, news organizations, and textbooks often include different sets of countries. Which statement best explains this?",
  options={
    "A": "The Middle East is a formal region with an official boundary that changes each year",
    "B": "The Middle East is a functional region, so its edges move with each day's trade flows",
    "C": "People define regions using different criteria, so boundaries can be contested",
    "D": "The maps use different projections, which change which countries appear in a region",
    "E": "The region has no shared characteristics, so it cannot be mapped consistently"},
  answer="C",
  rationales={
    "A": "Incorrect. There is no official, legally fixed boundary of the Middle East; its extent depends on who is defining it and why.",
    "B": "Incorrect. The Middle East is usually defined by shared cultural, historical, or political ties, not by daily flows to a single central node.",
    "C": "Correct. Regions are defined by people using one or more chosen characteristics. Because organizations use different criteria, such as culture, history, or politics, regional boundaries are often contested and overlapping.",
    "D": "Incorrect. A map projection changes the shape and size of places, not which countries a mapmaker chooses to include in a region.",
    "E": "Incorrect. The countries share characteristics that many people use to define a region; the disagreement is over which countries meet the chosen criteria."},
  explanation="People make regions by choosing what ties places together, like language, religion, history, or politics. Different groups choose differently, so their maps include different countries. That is why regional boundaries are often argued over and can overlap.")

q(id="U1-E25", n=25, topic="1.3", lo="IMP-1.C", skill="2.C", difficulty="medium",
  stem="A popular navigation app uses real-time traffic data to send drivers off a jammed highway onto quiet residential streets. Which outcome is the most likely geographic effect of this decision?",
  options={
    "A": "The absolute distance between the highway and the neighborhoods will shrink",
    "B": "The residential streets will become a formal region defined by app use",
    "C": "The neighborhoods' relative location will change, since they are now farther from the highway",
    "D": "More cars will use residential streets, and towns may add speed bumps",
    "E": "Fewer people will drive, since the app shows the highway is crowded"},
  answer="D",
  rationales={
    "A": "Incorrect. Absolute distance does not change; rerouting changes travel time and traffic patterns, not the distance between places.",
    "B": "Incorrect. Using the same app does not create a formal region; the likely effect is a change in traffic flows on those streets.",
    "C": "Incorrect. The neighborhoods have not moved and are no farther from the highway; what changes is the amount of traffic passing through them.",
    "D": "Correct. Decisions made with geospatial data have geographic effects. Rerouting many drivers onto local streets increases traffic there, which can lead towns to lower speed limits, add speed bumps, or restrict turns.",
    "E": "Incorrect. The app helps drivers continue their trips by another route; it does not by itself lead people to stop driving."},
  explanation="When the app sends lots of drivers onto small neighborhood streets, those streets get busy. Towns may then add speed bumps or new rules. A decision made with map data changed what happens on the ground.")
