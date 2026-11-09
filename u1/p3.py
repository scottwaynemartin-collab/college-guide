# Unit 1 practice items P34-P36, added Nov 8, 2026 after the ChatGPT Pro review's coverage notes
# (spatial pattern reading, field observation as the best method, limits of aggregated data).
import math
P = []

def river_valley():
    """P34: farmhouses strung along both banks of a river (linear pattern). River centerline y = 180 + 25 sin(x / 90)."""
    c = lambda x: 180 + 25 * math.sin(x / 90)
    xs = list(range(0, 801, 40))
    north = [[0, 0], [800, 0]] + [[x, round(c(x) - 10, 1)] for x in reversed(xs)]
    south = [[x, round(c(x) + 10, 1)] for x in xs] + [[800, 360], [0, 360]]
    homes = [[x, round(c(x) - 28, 1)] for x in range(45, 800, 65)] + [[x, round(c(x) + 28, 1)] for x in range(75, 800, 65)]
    return dict(type="schematicMap",
      title="FARMHOUSES IN VALLEY V (HYPOTHETICAL)",
      canvas=dict(width=800, height=360),
      features=[
        dict(kind="land", name="North side of the valley", polygon=north, style="small"),
        dict(kind="land", name="South side of the valley", polygon=south, style="small"),
        dict(kind="marker", name="Farmhouse", symbol="house", points=homes),
        dict(kind="line", name="For screen readers: Farmhouses stand in two rows, one along each bank of the river, from the west edge of the map to the east edge. No farmhouses stand far from the river.", line=[[0, 0], [0, 0]])],
      legend=[dict(swatch="house", label="Farmhouse"), dict(swatch="water", label="River")],
      description="Each house symbol stands for one farmhouse. A river crosses the valley from west to east. North is at the top.",
      source="Hypothetical map")

P.append(dict(id="U1-P34", topic="1.1", lo="IMP-1.A", skill="3.B", difficulty="easy",
  stimulus=river_valley(),
  stem="Which of the following best describes the spatial pattern of farmhouses shown on the map?",
  options={
    "A": "Clustered around one central village",
    "B": "Dispersed evenly across the whole valley",
    "C": "Concentrated on the north bank of the river",
    "D": "Linear, following the course of the river",
    "E": "Scattered with no link to physical features"},
  answer="D",
  explanation="A linear pattern means things are lined up along something long and narrow, like a river, road, or coast. Here the farmhouses form two lines, one on each bank, and follow the river's bends across the valley.",
  whyNot={
    "A": "There is no central village. The houses stretch from one side of the map to the other.",
    "B": "A dispersed pattern spreads things out across the whole area. Here the houses stay close to the river, and the land away from it is empty.",
    "C": "Twelve houses stand on each bank, so they are not concentrated on the north bank.",
    "E": "The houses follow the river closely, so the pattern is clearly linked to a physical feature."},
  vocab=["linear pattern", "clustered", "dispersed", "spatial pattern"]))

P.append(dict(id="U1-P35", topic="1.2", lo="IMP-1.B", skill="1.D", difficulty="medium",
  stem="A geographer wants to find out which ground-floor storefronts on one downtown street are open for business, empty, or being renovated this month. Which method would collect the most accurate information?",
  options={
    "A": "Walking the street and recording what is in each storefront",
    "B": "Reviewing satellite images of the downtown rooftops",
    "C": "Tracking delivery trucks on the street with GPS receivers",
    "D": "Mapping the street's property values from tax records",
    "E": "Counting the street's residents with the most recent national census"},
  answer="A",
  explanation="Field observation means going to a place and recording what you see. Walking the street lets the geographer check every storefront this month. Census counts, satellite pictures, GPS tracks, and tax records cannot show whether each store is open, empty, or being fixed up right now.",
  whyNot={
    "B": "Rooftop images cannot show whether a store is open, empty, or being renovated inside.",
    "C": "Delivery routes might hint at which stores get goods, but they do not record the condition of every storefront.",
    "D": "Property values do not show whether a store is open, empty, or being renovated right now.",
    "E": "A census counts people where they live, usually once every ten years. It does not record whether each store is open this month."},
  vocab=["field observation", "qualitative data"]))

P.append(dict(id="U1-P36", topic="1.6", lo="PSO-1.D", skill="3.F", difficulty="medium",
  stem="County R's average household income rose by 10 percent from 2015 to 2025. Which statement about this county-level figure is most accurate?",
  options={
    "A": "It shows that incomes rose in each of the county's neighborhoods",
    "B": "It shows that the poorest households gained the most income",
    "C": "It cannot show a change for the county, since an average hides the differences",
    "D": "It shows that the county's income grew faster than the nation's",
    "E": "It cannot show whether incomes rose or fell in each neighborhood"},
  answer="E",
  explanation="A county average is one number for the whole county. Some neighborhoods may have gained a lot, and others may have lost. To see those differences, you need data grouped at a finer level, such as neighborhoods. One scale can hide what happens at another.",
  whyNot={
    "A": "An average can rise even if some neighborhoods lost income, so it cannot show that each neighborhood gained.",
    "B": "An average does not show which households gained. The gains could have gone mostly to richer households.",
    "C": "The county average does show a change for the county as a whole: a 10 percent rise. What it cannot show is how that change differed from place to place.",
    "D": "The statement gives no national data, so it cannot be compared with the nation."},
  vocab=["scale of analysis", "aggregated data", "average"]))
