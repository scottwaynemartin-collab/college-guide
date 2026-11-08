# Unit 3 practice items P01-P16 (topics 3.1-3.5)
P = []

# ---------------- 3.1 Introduction to Culture (PSO-3.A) ----------------
P.append(dict(id="U3-P01", topic="3.1", lo="PSO-3.A", skill="1.A", difficulty="easy",
  stem="Eating tamales at Christmas, wearing a yukata (a light cotton kimono) to a summer festival in Japan, and building flat-roofed houses in a dry climate are each an example of a",
  options={
    "A": "culture trait",
    "B": "culture region",
    "C": "cultural hearth",
    "D": "culture complex",
    "E": "cultural landscape"},
  answer="A",
  explanation="A culture trait is one single piece of a culture, like a food, a style of clothing, or a type of building. Your AP course guide lists food preferences, architecture, and land use as culture traits. Each example in the question is one trait. When many related traits go together, that bigger group is called a culture complex.",
  whyNot={
    "B": "A culture region is an area where people share many traits. The question lists single traits, not areas.",
    "C": "A cultural hearth is the place where a trait or a culture first started.",
    "D": "A culture complex is a group of related traits that go together. Each example here is just one trait.",
    "E": "The cultural landscape is what culture looks like on the land. A house fits, but eating tamales is not part of the landscape."},
  vocab=["culture trait", "culture complex", "cultural hearth"]))

P.append(dict(id="U3-P02", topic="3.1", lo="PSO-3.A", skill="4.A", difficulty="easy",
  stimulus=dict(type="table",
    title="JOURNAL ENTRIES FROM FIVE STUDENTS ON A SCHOOL TRIP ABROAD (HYPOTHETICAL)",
    columns=["Student", "Journal entry"],
    rows=[
      ["Student 1", "People here eat dinner at 10 p.m. That is just wrong. Dinner should be at 6, like it is at home."],
      ["Student 2", "My host family eats dinner late because the afternoon is so hot that people rest at midday. Once I learned why, the schedule made sense to me."],
      ["Student 3", "So many restaurants here look like the chains back home. Maybe every place is becoming the same."],
      ["Student 4", "I only ate at restaurants that served food from my own country, because the local food seemed strange."],
      ["Student 5", "I wrote down the prices of meals here so I can compare them with prices back home."]],
    description="A table of five short journal entries written by students during a school trip to another country. Each entry describes the student's reaction to something in the local culture.",
    source="Hypothetical data"),
  stem="Which student's journal entry best demonstrates cultural relativism?",
  options={"A": "Student 1", "B": "Student 2", "C": "Student 3", "D": "Student 4", "E": "Student 5"},
  answer="B",
  explanation="Cultural relativism means trying to understand another culture on its own terms instead of judging it by the rules of your own culture. Student 2 learned WHY the family eats late (the hot afternoon) and decided the schedule made sense there. Students 1 and 4 do the opposite. They judge the other culture by home-culture standards, which is ethnocentrism.",
  whyNot={
    "A": "Student 1 judges the other culture by home-culture rules. That is ethnocentrism.",
    "C": "Student 3 notices that places look alike (cultural convergence) but does not try to understand the local culture.",
    "D": "Student 4 avoids local food because it seems strange. Judging it by home standards is ethnocentrism.",
    "E": "Student 5 only compares prices. That is a fact-finding task, not an attitude toward cultural differences."},
  vocab=["cultural relativism", "ethnocentrism"]))

P.append(dict(id="U3-P03", topic="3.1", lo="PSO-3.A", skill="1.A", difficulty="easy",
  stem="Which of the following is the best example of culture, as geographers use the term?",
  options={
    "A": "Eye color that children inherit from their parents",
    "B": "A pencil-tapping habit that one student invented and uses before big tests",
    "C": "The average amount of rain a region receives each year",
    "D": "A festival song that grandparents teach to their grandchildren",
    "E": "Blinking automatically when dust blows toward someone's eyes"},
  answer="D",
  explanation="Culture is the shared practices, technologies, attitudes, and behaviors that a society passes on. The key ideas are SHARED and LEARNED. A festival song is shared by a community, and grandparents teach it to the next generation. That makes it culture.",
  whyNot={
    "A": "Eye color is passed on through genes. Nobody learns it from their society.",
    "B": "One person's private habit is not shared by a group, so it is not culture.",
    "C": "Rainfall is part of the physical environment. It can shape culture, but it is not culture itself.",
    "E": "Blinking is an automatic body reflex. Nobody has to learn it."},
  vocab=["culture"]))

# ---------------- 3.2 Cultural Landscapes (PSO-3.B, PSO-3.C) ----------------
P.append(dict(id="U3-P04", topic="3.2", lo="PSO-3.B", skill="4.E", difficulty="medium",
  stimulus=dict(type="table",
    title="FIELD NOTES FROM FIVE SITES (HYPOTHETICAL)",
    columns=["Site", "What a student observed"],
    rows=[
      ["Site 1", "Glass office towers built in the 2010s, an international hotel, and coffee shops from chains found in many countries"],
      ["Site 2", "A brick church built in the 1920s that is now a mosque; the old stained-glass windows remain, and a new sign in Arabic and English hangs over the door"],
      ["Site 3", "Thick-walled adobe houses with small windows, built by one local family over several generations"],
      ["Site 4", "A row of new houses, all built in the same style by one company in 2022"],
      ["Site 5", "A street where most shop signs, restaurants, and festival banners reflect one immigrant group"]],
    description="A table of field notes describing the buildings and other landscape features a student observed at five different sites.",
    source="Hypothetical data"),
  stem="Which site in the table provides the clearest evidence of sequent occupance?",
  options={"A": "Site 1", "B": "Site 2", "C": "Site 3", "D": "Site 4", "E": "Site 5"},
  answer="B",
  explanation="Sequent occupance means different groups live in a place one after another, and each group leaves its mark on the landscape. At Site 2, a church built by one group is now a mosque used by a later group, and the old windows are still there. You can see two layers of culture in one building.",
  whyNot={
    "A": "Site 1 shows global, look-alike buildings, not layers left by different groups over time.",
    "C": "Site 3 shows traditional architecture built by one group, not a series of different groups.",
    "D": "Site 4 shows new houses from one year and one builder, with no older layer.",
    "E": "Site 5 shows one group's culture on the landscape, but not one group following another."},
  vocab=["sequent occupance", "cultural landscape"]))

P.append(dict(id="U3-P05", topic="3.2", lo="PSO-3.C", skill="2.B", difficulty="easy",
  stem="In 2019, the climb to the top of Uluru, a huge rock formation in central Australia, was permanently closed. The Anangu, the traditional owners of the land, had long asked visitors not to climb Uluru because of its spiritual importance. This change best illustrates how",
  options={
    "A": "tourism tends to replace traditional land uses once a place becomes famous",
    "B": "a dry climate can make some landforms too dangerous for visitors",
    "C": "sequent occupance erases evidence of earlier groups from the landscape",
    "D": "a national government imposed its own religion on an Indigenous group",
    "E": "Indigenous beliefs and land rights can shape how a landscape is used"},
  answer="E",
  explanation="Uluru is a sacred place for the Anangu, the traditional owners of the land. For years they asked visitors not to climb it, and in 2019 the climb was closed for good. A group's beliefs and its rights to its land changed how the place is used. Your AP course guide says indigenous communities and lands help shape the use of space.",
  whyNot={
    "A": "Here the change went the other way: a tourist activity ended out of respect for a traditional belief.",
    "B": "Heat and safety were real concerns, but the stem says the closure came after the traditional owners' long request based on the site's spiritual meaning.",
    "C": "Sequent occupance is about layers left by different groups. Nothing was erased here.",
    "D": "No religion was imposed. The change respected the Anangu's own beliefs."},
  vocab=["indigenous lands", "sacred space", "cultural landscape"]))

P.append(dict(id="U3-P06", topic="3.2", lo="PSO-3.B", skill="1.A", difficulty="easy",
  stem="Some newer office buildings borrow details from many past styles, such as Greek columns, arches, and bright colors, and combine them in playful new ways. These buildings are best described as examples of",
  options={
    "A": "traditional architecture",
    "B": "sequent occupance",
    "C": "postmodern architecture",
    "D": "an ethnic enclave",
    "E": "colonial architecture"},
  answer="C",
  explanation="Postmodern buildings borrow pieces of older styles, like columns or arches, and mix them in new and often playful ways. They were a reaction against plain glass-box skyscrapers. Your AP course guide lists both traditional and postmodern architecture as parts of the cultural landscape.",
  whyNot={
    "A": "Traditional architecture uses local materials and building styles passed down in one place over generations.",
    "B": "Sequent occupance is about layers left by different groups over time. The stem describes a building style.",
    "D": "An ethnic enclave is a neighborhood where one ethnic group is concentrated, not a style of building.",
    "E": "Colonial architecture follows styles brought by a colonial power, such as Spanish missions in the Americas."},
  vocab=["postmodern architecture", "traditional architecture"]))

P.append(dict(id="U3-P07", topic="3.2", lo="PSO-3.C", skill="2.C", difficulty="medium",
  stem="In Country Z, the share of women working in paid jobs rose sharply between 1970 and 2020. Which change in the cultural landscape would most likely go along with this trend?",
  options={
    "A": "More childcare centers near workplaces, transit stops, and neighborhoods",
    "B": "More stores shifting their busiest hours from evenings and weekends to weekday mornings",
    "C": "Fewer roads and parking lots, because fewer adults would commute to jobs",
    "D": "More homes built with large sewing rooms and kitchens for full-time homemakers",
    "E": "Fewer restaurants and take-out shops, because families would cook more meals at home"},
  answer="A",
  explanation="Your AP course guide says attitudes about gender, including women's roles in the workforce, shape how space is used. When more parents of young children work outside the home, families need childcare. So childcare centers open near jobs, transit stops, and homes. That is a change you can see in the landscape.",
  whyNot={
    "B": "With more adults at work on weekdays, busy shopping times tend to move to evenings and weekends, not mornings.",
    "C": "More people working means more commuting, which usually adds roads, parking, and transit.",
    "D": "Rooms built for full-time homemakers fit a time when fewer women worked for pay, not more.",
    "E": "Households where both adults work usually have less time to cook, so demand for restaurants and take-out tends to grow."},
  vocab=["gender roles", "use of space", "cultural landscape"]))

# ---------------- 3.3 Cultural Patterns (PSO-3.D) ----------------
P.append(dict(id="U3-P08", topic="3.3", lo="PSO-3.D", skill="1.D", difficulty="medium",
  stem="After independence in the 1960s, Tanzania's government promoted Swahili as the national language for primary schools and government in a country where more than 100 languages are spoken. Geographers would describe this shared language as",
  options={
    "A": "a centrifugal force, because it divides speakers of different first languages",
    "B": "an example of relocation diffusion, because it spread mainly through migration",
    "C": "an example of language extinction, because local languages are no longer spoken",
    "D": "an example of cultural relativism, because it judges each culture on its own terms",
    "E": "a centripetal force, because it gives many groups a common identity"},
  answer="E",
  explanation="A centripetal force pulls the people of a country together. More than 100 languages are spoken in Tanzania. Giving everyone one shared language for school and government helped people from many groups feel like one nation. Language can also be a centrifugal force when it divides people, as in a country split into language regions.",
  whyNot={
    "A": "A shared national language pulls people together. Language is centrifugal when it divides groups, not when it gives them a common tongue.",
    "B": "The question is about what the shared language does for the country, not about how it spread.",
    "C": "Many Tanzanians still speak their local languages too. Swahili was added as a common language.",
    "D": "Cultural relativism is an attitude toward other cultures, not a language policy."},
  vocab=["centripetal force", "centrifugal force", "national language"]))

P.append(dict(id="U3-P09", topic="3.3", lo="PSO-3.D", skill="4.D", difficulty="medium",
  stimulus=dict(type="schematicMap",
    title="LANGUAGE REGIONS OF COUNTRY V (HYPOTHETICAL)",
    canvas=dict(width=800, height=380),
    features=[
      dict(kind="zone", name="Region 1", polygon=[[30, 40], [290, 30], [300, 350], [40, 345]], labelAt=[165, 150], sublabel="Most people speak Language A. National capital."),
      dict(kind="zone", name="Region 2", polygon=[[290, 30], [520, 40], [510, 340], [300, 350]], labelAt=[405, 150], sublabel="Most people speak Language A."),
      dict(kind="zone", name="Region 3", polygon=[[520, 40], [770, 50], [760, 330], [510, 340]], labelAt=[640, 150], sublabel="Most people speak Language B."),
      dict(kind="line", name="High mountain range", line=[[520, 40], [532, 70], [510, 100], [532, 130], [510, 160], [532, 190], [510, 220], [532, 250], [510, 280], [532, 310], [510, 340]]),
      dict(kind="marker", name="National capital", symbol="baseN", points=[[165, 250]])],
    legend=[dict(swatch="baseN", label="National capital")],
    description="Country V has three regions. Language A is the only official language, and national schools, courts, and television use only Language A. Most people in Regions 1 and 2 speak Language A at home; most people in Region 3 speak Language B. A zigzag line marks a high mountain range along the border between Region 2 and Region 3.",
    renderNotes="Three side-by-side regions on a water background, each in a different light shade, with name and sublabel. Zigzag line between Regions 2 and 3 = mountains. Square marker in Region 1 = capital.",
    source="Hypothetical map"),
  stem="Based on the map and its description, which outcome is most likely?",
  options={
    "A": "Region 2 will push for independence because the capital is in Region 1.",
    "B": "The mountains will speed the spread of Language A into Region 3.",
    "C": "Language will act as a centripetal force that unites Regions 1 and 3.",
    "D": "Language may become a centrifugal force that pulls Region 3 away.",
    "E": "Language B will become the lingua franca of Regions 1 and 2."},
  answer="D",
  explanation="A centrifugal force pulls a country apart. Region 3 is cut off by mountains, and most people there speak Language B. But schools, courts, and TV use only Language A. People in Region 3 may feel left out, so language becomes a centrifugal force. Canada, where many French speakers in Quebec have pushed for more self-rule, is a real example of language dividing a country.",
  whyNot={
    "A": "Region 2 shares Language A with the capital region, so language is not dividing it from the rest of the country.",
    "B": "Mountains are barriers that usually slow diffusion. That is one reason Language B has survived in Region 3.",
    "C": "Region 3 speaks a different language from Region 1, so language divides them instead of uniting them.",
    "E": "Regions 1 and 2 already share Language A, so they have no need for Language B as a common language."},
  vocab=["centrifugal force", "official language", "physical barrier"]))

P.append(dict(id="U3-P10", topic="3.3", lo="PSO-3.D", skill="1.D", difficulty="medium",
  stem="Beginning in the 1970s, residents of Barrio Logan, a largely Mexican American neighborhood in San Diego, California, turned land beneath a highway bridge into Chicano Park and painted murals on the bridge's concrete pillars. The murals show Mexican and Mexican American history and culture. This is best described as",
  options={
    "A": "placelessness caused by the spread of global popular culture",
    "B": "assimilation into a dominant culture",
    "C": "placemaking that strengthens a sense of place",
    "D": "stimulus diffusion of an art style from abroad",
    "E": "ethnocentrism toward other groups"},
  answer="C",
  explanation="Placemaking is when people shape a public space so it reflects who they are. The residents of Barrio Logan turned the space under a highway into a park and painted murals about their history. That gives the neighborhood a strong sense of place: a feeling that the place is special and belongs to its community.",
  whyNot={
    "A": "Placelessness is when places lose their uniqueness and look the same. These murals make the place more unique.",
    "B": "Assimilation means a group gives up its own culture. The murals celebrate it.",
    "D": "The murals were created by local residents about their own history. The key idea is people shaping their own space.",
    "E": "Ethnocentrism is judging other cultures as worse than your own. The murals honor the residents' heritage without putting down other groups."},
  vocab=["placemaking", "sense of place", "placelessness"]))

P.append(dict(id="U3-P11", topic="3.3", lo="PSO-3.D", skill="5.B", difficulty="hard",
  stem="In Nigeria, Islam is the main religion in much of the north, while Christianity is the main religion in much of the south. Which of the following best explains why geographers see this pattern as a possible centrifugal force?",
  options={
    "A": "Islam and Christianity are both ethnic religions, so neither can spread beyond its region.",
    "B": "When religious differences match regional lines, people may identify more with their region.",
    "C": "A shared belief in one God makes the two religions a centripetal force across both regions.",
    "D": "Religious diversity usually leads a state to split into separate countries.",
    "E": "The pattern resulted from hierarchical diffusion, which spreads religions from capital cities outward."},
  answer="B",
  explanation="A centrifugal force divides a country. In Nigeria, the main religion in much of the north is different from the main religion in much of the south. When religion lines up with region, people may feel closer to their region than to the whole country. Arguments about laws, power, or money can then become both regional and religious, which can pull a state apart.",
  whyNot={
    "A": "Islam and Christianity are universalizing religions that have spread around the world.",
    "C": "The question asks why the pattern can divide the country. Religious differences that line up with regions tend to divide, not unite.",
    "D": "Many countries with more than one major religion stay united. Religion becomes a risk mainly when it lines up with other divisions, such as region.",
    "E": "How the religions spread does not explain why the pattern can divide the country today."},
  vocab=["centrifugal force", "universalizing religion", "regionalism"]))

# ---------------- 3.4 Types of Diffusion (IMP-3.A) ----------------
P.append(dict(id="U3-P12", topic="3.4", lo="IMP-3.A", skill="4.E", difficulty="easy",
  stimulus=dict(type="schematicMap",
    title="SPREAD OF RELIGION Q (HYPOTHETICAL)",
    canvas=dict(width=800, height=400),
    features=[
      dict(kind="land", name="Land A", polygon=[[0, 0], [360, 0], [330, 90], [370, 180], [320, 280], [350, 400], [0, 400]], labelAt=[80, 40]),
      dict(kind="land", name="Land B", polygon=[[540, 0], [800, 0], [800, 400], [520, 400], [560, 300], [530, 200], [560, 100]], labelAt=[700, 40]),
      dict(kind="land", name="Area where most people follow Religion Q by 1500", style="power", polygon=[[70, 110], [220, 80], [290, 170], [250, 300], [110, 310], [50, 220]]),
      dict(kind="land", name="Area where most people follow Religion Q by 1500 (port town)", style="power", polygon=[[545, 175], [625, 170], [635, 240], [560, 248], [538, 210]]),
      dict(kind="island", name="Hearth city", center=[165, 185], radius=8),
      dict(kind="island", name="Port town", center=[588, 200], radius=6),
      dict(kind="arrow", name="Merchants from Land A who settled in the port town in the 1300s", **{"from": [330, 196], "to": [540, 202]})],
    legend=[dict(swatch="power", label="Most people follow Religion Q (by 1500)"), dict(swatch="land", label="Other land"), dict(swatch="water", label="Sea")],
    description="Religion Q began in the hearth city on Land A. By 1500 it had spread from the hearth city to the villages and towns around it (shaded area on Land A). The arrow shows merchants from Land A who sailed across the sea in the 1300s, settled in a port town on Land B, and built the first Religion Q house of worship there. By 1500 most people in the port town followed Religion Q.",
    renderNotes="Land A on the left, Land B on the right, sea between. Shaded (power) areas: a large area around the hearth city on Land A and a small area around the port town on Land B's west coast. Arrow across the sea from Land A to the port town.",
    source="Hypothetical map"),
  stem="The arrow on the map best illustrates which type of diffusion?",
  options={
    "A": "Contagious expansion diffusion",
    "B": "Hierarchical expansion diffusion",
    "C": "Relocation diffusion",
    "D": "Stimulus expansion diffusion",
    "E": "Reverse hierarchical diffusion"},
  answer="C",
  explanation="Relocation diffusion happens when people MOVE and carry their culture with them to a new place. The merchants sailed across the sea, settled in the port town, and brought their religion along. The religion did not spread through the places in between. It jumped across the sea with the people who moved.",
  whyNot={
    "A": "Contagious diffusion spreads person to person into nearby places, like the shaded area around the hearth city, not across the sea with migrants.",
    "B": "Hierarchical diffusion moves from powerful people or large places down to smaller ones. The arrow shows people moving.",
    "D": "Stimulus diffusion is when an idea spreads but changes form. Nothing shows the religion being changed.",
    "E": "Reverse hierarchical diffusion starts in small or less powerful places and moves up to larger ones."},
  vocab=["relocation diffusion", "expansion diffusion", "contagious diffusion"]))

P.append(dict(id="U3-P13", topic="3.4", lo="IMP-3.A", skill="3.E", difficulty="medium",
  stimulus=dict(type="table",
    title="YEAR A NEW DANCE STYLE BECAME POPULAR IN EACH PLACE, REGION J (HYPOTHETICAL DATA)",
    columns=["Place", "Population", "Distance from Ora (km)", "Year the dance became popular"],
    rows=[
      ["Ora (hearth village)", "3,000", "0", "2000"],
      ["Town P", "50,000", "20", "2001"],
      ["Village Q", "1,500", "25", "2001"],
      ["City R", "900,000", "120", "2004"],
      ["Village S", "800", "60", "2002"],
      ["Town T", "30,000", "180", "2006"],
      ["Village U", "600", "200", "2007"]],
    description="A table listing seven places in Region J with each place's population, its distance in kilometers from the village of Ora, where a new dance style began, and the year the dance became popular there.",
    source="Hypothetical data"),
  stem="Which type of diffusion is best supported by the data in the table?",
  options={
    "A": "Hierarchical, because the dance reached the largest place first",
    "B": "Relocation, because the dance reached places far from Ora",
    "C": "Reverse hierarchical, because the dance began in a small village",
    "D": "Stimulus, because the dance changed its steps as it moved from place to place",
    "E": "Contagious, because nearby places adopted it first, whatever their size"},
  answer="E",
  explanation="Look at distance and year together. The closer a place is to Ora, the sooner it adopted the dance, no matter how many people live there. Tiny Village Q (25 km away) got it in 2001, three years before huge City R (120 km away). Spreading to nearby places first, like a cold passing from person to person, is contagious diffusion.",
  whyNot={
    "A": "City R, the largest place, did not adopt the dance until 2004, after several small villages.",
    "B": "Relocation needs people to move and carry the trait. A steady spread outward by distance points to contagious expansion instead.",
    "C": "Village U, the smallest place, adopted the dance last, so the dance did not move from small places up to large ones.",
    "D": "The table shows only places, distances, and years. It gives no sign that the dance changed."},
  vocab=["contagious diffusion", "distance decay", "hierarchical diffusion"]))

P.append(dict(id="U3-P14", topic="3.4", lo="IMP-3.A", skill="1.D", difficulty="easy",
  stem="A U.S.-based burger chain opens restaurants in Country X, where most people do not eat beef for religious reasons. The chain keeps its counters, drive-throughs, and fast service but replaces beef burgers with sandwiches made from spiced potatoes and chicken. This best illustrates",
  options={
    "A": "stimulus diffusion",
    "B": "relocation diffusion",
    "C": "contagious diffusion",
    "D": "reverse hierarchical diffusion",
    "E": "assimilation"},
  answer="A",
  explanation="In stimulus diffusion, the basic idea spreads, but the trait changes to fit the new culture. The fast-food idea (counters, drive-throughs, quick service) spread to Country X. The menu changed to fit local beliefs about food. Same idea, new form.",
  whyNot={
    "B": "Relocation diffusion happens when people move and take their culture with them. Here a business idea spreads and is changed to fit local beliefs.",
    "C": "Contagious diffusion spreads a trait, unchanged, from person to person into nearby places.",
    "D": "Reverse hierarchical diffusion moves from small or less powerful places up to larger ones.",
    "E": "Assimilation is when a group gives up its own culture. The chain kept its basic fast-food model."},
  vocab=["stimulus diffusion", "expansion diffusion"]))

P.append(dict(id="U3-P15", topic="3.4", lo="IMP-3.A", skill="2.A", difficulty="medium",
  stem="A new style of clothing first became popular among teenagers in several small towns in rural Country P. About two years later it appeared in mid-sized cities, and only after that did large stores in the capital city begin selling it. This pattern is best described as",
  options={
    "A": "hierarchical diffusion, because the style moved down from the capital",
    "B": "contagious diffusion, because the style spread to the nearest towns first",
    "C": "relocation diffusion, because teenagers moved to cities and took the style",
    "D": "reverse hierarchical diffusion, because it moved up from small towns",
    "E": "stimulus diffusion, because each city changed the style to fit local tastes"},
  answer="D",
  explanation="Reverse hierarchical diffusion starts at the bottom and moves UP. It begins in small towns or with less powerful groups. Then it climbs to bigger places. Here the style began in small towns. Next it reached mid-sized cities. The capital got it last. Your AP course guide names hierarchical diffusion, which usually moves DOWN from big or powerful places. Reverse hierarchical diffusion climbs the same ladder the other way.",
  whyNot={
    "A": "The style moved UP from small towns to the capital, not down from the capital.",
    "B": "The style moved up by size, from small towns to mid-sized cities to the capital. Nothing shows it spreading to nearby places first.",
    "C": "Nothing says teenagers moved. The style spread while people stayed where they were.",
    "E": "Nothing says the style changed. The same style spread from place to place."},
  vocab=["reverse hierarchical diffusion", "hierarchical diffusion"]))

# ---------------- 3.5 Historical Causes of Diffusion (SPS-3.A) ----------------
P.append(dict(id="U3-P16", topic="3.5", lo="SPS-3.A", skill="4.A", difficulty="easy",
  stimulus=dict(type="table",
    title="FOUR LANGUAGES AND THEIR HISTORIES",
    columns=["Language", "Where it is widely used", "History"],
    rows=[
      ["Swahili", "East Africa, including Kenya and Tanzania", "Spread along Indian Ocean coastal trade routes and later inland trade routes; now widely used for trade, schooling, and government among people who speak many different first languages"],
      ["Haitian Creole", "Haiti", "Formed in the French colony of Saint-Domingue from contact between French and West African languages; now the first language of most Haitians"],
      ["French", "Senegal, Côte d'Ivoire, Gabon", "Brought by French colonization; still an official language after independence"],
      ["Basque", "Northern Spain and southwestern France", "Spoken mainly in its home region; not known to be related to any other living language"]],
    description="A table describing four languages, where each is widely used today, and how each spread or developed.",
    source="Compiled from standard references on world languages"),
  stem="The role of Swahili described in the table best illustrates which concept?",
  options={
    "A": "Creolization",
    "B": "Lingua franca",
    "C": "Language isolate",
    "D": "Dialect",
    "E": "Language extinction"},
  answer="B",
  explanation="A lingua franca is a \"bridge\" language. People use it when they do not share a first language. Swahili spread along trade routes. Today, people in East Africa grow up speaking many different languages, but they can all use Swahili to trade, learn, and run the government. Your AP course guide lists lingua franca as one result of the way cultures spread in the past.",
  whyNot={
    "A": "Creolization is when languages mix to form a new first language, as with Haitian Creole in the table.",
    "C": "A language isolate is not related to any other language, like Basque in the table.",
    "D": "A dialect is a regional version of one language, like the different ways English is spoken in Texas and in Boston.",
    "E": "Swahili is growing in use, not disappearing."},
  vocab=["lingua franca", "creolization", "language isolate"]))
