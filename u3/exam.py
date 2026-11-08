# Unit 3 exam items E01-E25
E = []
def q(**k): E.append(k)

q(id="U3-E01", n=1, topic="3.1", lo="PSO-3.A", skill="1.A", difficulty="easy",
  stem="Friday-night high school football games, tailgating, marching bands, homecoming mums, and school colors are related traits that together form a",
  options={
    "A": "culture region",
    "B": "cultural hearth",
    "C": "culture complex",
    "D": "culture trait",
    "E": "cultural landscape"},
  answer="C",
  rationales={
    "A": "Incorrect. A culture region is an area in which people share particular culture traits; the stem describes a set of related traits, not an area.",
    "B": "Incorrect. A cultural hearth is the place where a culture trait or culture originated.",
    "C": "Correct. A culture complex is a group of related culture traits that together make up a larger cultural activity, such as the practices connected to high school football.",
    "D": "Incorrect. A culture trait is a single attribute of a culture; the stem lists several related traits that function together.",
    "E": "Incorrect. The cultural landscape is the visible imprint of culture on a place, such as a stadium. Tailgating, bands, and school colors together are better described as a complex of related traits."},
  explanation="One trait is one piece of culture, like wearing school colors. A culture complex is a group of related traits that go together. Football games, tailgating, marching bands, homecoming mums, and school colors all connect to one activity, so together they form a culture complex.")

q(id="U3-E02", n=2, topic="3.1", lo="PSO-3.A", skill="1.D", difficulty="easy",
  stem="A tourist complains that people in the country she is visiting eat with their hands instead of with forks, and she calls the local way of eating uncivilized. Her attitude is an example of",
  options={
    "A": "ethnocentrism",
    "B": "cultural relativism",
    "C": "acculturation",
    "D": "syncretism",
    "E": "cultural convergence"},
  answer="A",
  rationales={
    "A": "Correct. Ethnocentrism is the attitude that one's own culture is superior and the use of one's own cultural standards to judge other cultures.",
    "B": "Incorrect. Cultural relativism is the opposite attitude: evaluating a culture's practices on their own terms rather than by an outside standard.",
    "C": "Incorrect. Acculturation is the adoption of some traits of another culture; the tourist rejects the local practice rather than adopting it.",
    "D": "Incorrect. Syncretism is the blending of traits from different cultures into a new form.",
    "E": "Incorrect. Cultural convergence is the process by which cultures become more alike through contact."},
  explanation="Ethnocentrism means judging another culture by your own culture's rules. It means deciding that your way is better. In many cultures, eating with your hands is normal and polite. Calling it \"uncivilized\" just because it is different from home is ethnocentric.")

# ---- Set A: hierarchical diffusion map, E03-E05 ----
q(id="U3-E03", n=3, set="musicmap", setLabel="Questions 3–5 refer to the map below.",
  topic="3.4", lo="IMP-3.A", skill="3.B", difficulty="medium",
  stimulus=dict(type="schematicMap",
    title="SPREAD OF A NEW MUSIC STYLE IN COUNTRY R, 2010–2016 (HYPOTHETICAL)",
    canvas=dict(width=800, height=420),
    features=[
      dict(kind="land", name="Country R", polygon=[[24, 40], [300, 22], [560, 34], [776, 24], [784, 200], [770, 404], [420, 396], [30, 408], [16, 220]]),
      dict(kind="island", name="Arlo (hearth), 9 million: 2010", center=[170, 230], radius=16),
      dict(kind="island", name="Benn, 4 million: 2011", center=[620, 100], radius=13),
      dict(kind="island", name="Cora, 3 million: 2011", center=[610, 330], radius=12),
      dict(kind="island", name="Dell, 800,000: 2013", center=[660, 220], radius=9),
      dict(kind="island", name="Eskar, 600,000: 2013", center=[360, 340], radius=9),
      dict(kind="island", name="Fenn, 20,000: 2015", center=[190, 110], radius=6),
      dict(kind="island", name="Gale, 15,000: 2016", center=[430, 150], radius=5),
      dict(kind="scaleBar", label="100 kilometers", **{"from": [50, 386], "to": [150, 386]})],
    description="Circles show cities and towns in Country R; larger circles mean more people. Each label gives the place's name, its population, and the year the music style first became popular there. The style began in Arlo, the hearth. Fenn is about 120 kilometers from Arlo; Benn and Cora are each more than 450 kilometers from Arlo.",
    renderNotes="One land polygon for Country R on a water background. City circles (island features) sized by population, each with a one-line label underneath. Scale bar bottom left: 100 px = 100 km.",
    source="Hypothetical map"),
  stem="The pattern shown on the map is best described as",
  options={
    "A": "contagious diffusion",
    "B": "relocation diffusion",
    "C": "stimulus diffusion",
    "D": "hierarchical diffusion",
    "E": "reverse hierarchical diffusion"},
  answer="D",
  rationales={
    "A": "Incorrect. Contagious diffusion would reach the places nearest the hearth first. Fenn, only about 120 kilometers from Arlo, adopted the style in 2015, years after much more distant large cities.",
    "B": "Incorrect. Relocation diffusion occurs when people migrate and carry a trait with them; the map shows adoption in place, in order of city size.",
    "C": "Incorrect. Stimulus diffusion involves an underlying idea spreading while the trait itself is changed; the map gives no evidence that the style changed.",
    "D": "Correct. The style spread from the largest city to other large cities, then to medium-sized cities, and last to small towns, regardless of distance from the hearth. Spread down an urban hierarchy is hierarchical diffusion.",
    "E": "Incorrect. Reverse hierarchical diffusion moves from small places up to larger ones; here the smallest places adopted the style last."},
  explanation="Follow the years. Arlo, the biggest city, had it in 2010. The big cities Benn and Cora got it in 2011. The medium cities Dell and Eskar got it in 2013. The small towns Fenn and Gale got it last, in 2015 and 2016. The style moved down the ladder of city size, not outward by distance. That is hierarchical diffusion.")

q(id="U3-E04", n=4, set="musicmap", topic="3.4", lo="IMP-3.A", skill="3.E", difficulty="medium",
  stem="Fenn is the place closest to Arlo, yet it was one of the last places to adopt the music style. Which of the following best explains this?",
  options={
    "A": "Distance decay means places nearest a hearth tend to be the last to adopt a trait.",
    "B": "New trends often move first between big, well-connected cities, then down to small towns.",
    "C": "The style reached Fenn when people from Arlo moved there, through relocation diffusion.",
    "D": "Fenn's small population places it in a different culture region from the rest of Country R.",
    "E": "Contagious diffusion spreads a trait to the largest places first and the closest places last."},
  answer="B",
  rationales={
    "A": "Incorrect. Distance decay means interaction declines as distance increases, so nearby places usually adopt a trait sooner, not later.",
    "B": "Correct. In hierarchical diffusion, a trait moves first among the largest and most connected places, through media, business, and travel links, and reaches small towns later, even towns close to the hearth.",
    "C": "Incorrect. The map gives no evidence of migration, and relocation diffusion would not explain why a nearby town adopted the style later than distant large cities.",
    "D": "Incorrect. Nothing on the map suggests Fenn belongs to a different culture region; Fenn and Gale, the two smallest places, both adopted the style last, which reflects their size.",
    "E": "Incorrect. This misdefines contagious diffusion, which spreads to the nearest people and places first regardless of size."},
  explanation="Big cities are tied to each other by media companies, concert tours, airports, and lots of travelers. So a new trend jumps from one big city to another first. Small towns get it later, even if they are close by. That is why little Fenn waited until 2015.")

q(id="U3-E05", n=5, set="musicmap", topic="3.6", lo="SPS-3.A", skill="2.C", difficulty="hard",
  stem="Suppose the same music style had first appeared in Arlo in 2024, when nearly everyone in Country R used streaming services and social media. Compared with the map, the spread would most likely have been",
  options={
    "A": "slower, because online media make distance decay stronger",
    "B": "limited mainly to large cities, because small towns lack media companies",
    "C": "about the same, because trends would still move down the urban hierarchy year by year",
    "D": "carried mainly by migrants, making relocation diffusion the main process",
    "E": "faster and less tied to city size, because of time-space convergence"},
  answer="E",
  rationales={
    "A": "Incorrect. Online media weaken the effect of distance on interaction; they do not strengthen distance decay.",
    "B": "Incorrect. Listeners do not need local media companies to stream music; anyone with internet access can hear a new style, wherever they live.",
    "C": "Incorrect. The AP course framework notes that communication technologies such as the internet are reshaping and accelerating interactions among people, so the slow, year-by-year movement down the urban hierarchy shown on the map would be much less likely.",
    "D": "Incorrect. Online sharing spreads a trait without people moving, so relocation diffusion would not become the main process.",
    "E": "Correct. Time-space convergence, the shrinking of the time it takes for people and ideas to travel between places, means people in small towns can hear a new style online at nearly the same time as people in big cities. Adoption would be faster and depend less on the urban hierarchy."},
  explanation="With streaming and social media, a song posted in Arlo can be heard in tiny Fenn the same day. Distance and city size matter much less. That is time-space convergence: new technology makes places feel closer together, so trends spread faster and more evenly.")

q(id="U3-E06", n=6, topic="3.4", lo="IMP-3.A", skill="1.D", difficulty="medium",
  stem="In the early 1800s, Sequoyah, a Cherokee man who did not read English, saw that English speakers could communicate through writing. He then created a new writing system, with a symbol for each syllable of the Cherokee language, which he completed in 1821. This is an example of",
  options={
    "A": "stimulus diffusion",
    "B": "relocation diffusion",
    "C": "contagious diffusion",
    "D": "hierarchical diffusion",
    "E": "assimilation"},
  answer="A",
  rationales={
    "A": "Correct. In stimulus diffusion, an underlying idea spreads, but the trait itself is changed or reinvented by the receiving culture. The idea of writing spread, and Sequoyah created a new system for the Cherokee language rather than adopting English writing.",
    "B": "Incorrect. Relocation diffusion occurs when people migrate and carry culture with them; Sequoyah adapted an idea he encountered rather than receiving a trait carried by migrants.",
    "C": "Incorrect. Contagious diffusion spreads a trait, unchanged, from person to person; here the trait was reinvented.",
    "D": "Incorrect. Hierarchical diffusion moves from people or places of high rank down the hierarchy; the key feature here is the transformation of the idea.",
    "E": "Incorrect. Assimilation would mean giving up Cherokee culture; the syllabary was created to write the Cherokee language."},
  explanation="Stimulus diffusion means the IDEA spreads, but people change it to fit their own culture. Sequoyah got the idea of writing from seeing English, but he made a brand-new writing system for Cherokee.")

q(id="U3-E07", n=7, topic="3.5", lo="SPS-3.A", skill="1.A", difficulty="easy",
  stem="International rules require pilots and air traffic controllers on international flights to be able to communicate in English, even when neither the pilot nor the controller speaks English as a first language. English in this role is best described as",
  options={
    "A": "a creole",
    "B": "a dialect",
    "C": "a lingua franca",
    "D": "a language isolate",
    "E": "a pidgin"},
  answer="C",
  rationales={
    "A": "Incorrect. A creole develops when a pidgin becomes the first language of a community; aviation English did not develop that way.",
    "B": "Incorrect. A dialect is a regional or social variety of a language.",
    "C": "Correct. A lingua franca is a language used for communication among people who do not share a first language. English plays this role in international aviation, as well as in much of international business and science.",
    "D": "Incorrect. A language isolate has no known relationship to other languages, as with Basque; English belongs to the Germanic branch of the Indo-European family.",
    "E": "Incorrect. A pidgin is a simplified mixture of languages created for limited contact; aviation uses standard English with set phrases, not a new mixed language."},
  explanation="A lingua franca is a \"bridge\" language that people use when they do not share a first language. A pilot from Brazil and a controller in Japan can both use English to talk. English is the lingua franca of the skies.")

q(id="U3-E08", n=8, topic="3.5", lo="SPS-3.A", skill="2.B", difficulty="medium",
  stem="Portuguese is an official language in Brazil, Angola, Mozambique, and Timor-Leste, countries on three different continents. Which of the following best explains this pattern?",
  options={
    "A": "Portuguese spread by contagious diffusion from Brazil to Africa and then to Asia.",
    "B": "The four countries share a tropical climate that favored the spread of Portuguese.",
    "C": "Portuguese formed as a pidgin among traders in Africa and later spread to Europe.",
    "D": "Large numbers of Portuguese workers moved to these countries in the last 20 years.",
    "E": "Portugal colonized these places, and its language remained after independence."},
  answer="E",
  rationales={
    "A": "Incorrect. Contagious diffusion spreads to nearby places; these countries are separated by oceans, and Portuguese reached each one by sea from Portugal.",
    "B": "Incorrect. Climate does not determine language; the pattern reflects colonial history, not environmental conditions.",
    "C": "Incorrect. Portuguese is a Romance language that developed in Europe from Latin; it did not begin as an African trade pidgin.",
    "D": "Incorrect. Portuguese has been used in these places for centuries, far longer than recent migration could explain.",
    "E": "Correct. Portugal built a colonial and trading empire beginning in the 1400s and 1500s. Colonial rule spread Portuguese as the language of government, schooling, and trade, and the former colonies kept it as an official language after independence."},
  explanation="These countries are far apart, but they were all once Portuguese colonies. The colonizers made Portuguese the language of government, schools, and business. After independence, Portuguese stayed. Your AP course guide says colonialism and imperialism helped shape the cultural patterns we see today.")

q(id="U3-E09", n=9, topic="3.5", lo="SPS-3.A", skill="1.B", difficulty="medium",
  stem="Haitian Creole developed in the 1600s and 1700s in the French colony of Saint-Domingue (present-day Haiti). Most of its vocabulary comes from French, while much of its grammar reflects West African languages spoken by enslaved Africans brought to the colony. Today it is the native language of most Haitians. The development of Haitian Creole best illustrates",
  options={
    "A": "language extinction caused by the spread of a colonial language",
    "B": "creolization resulting from contact between cultures under colonialism",
    "C": "the diffusion of an Indo-European language by contagious expansion",
    "D": "stimulus diffusion of the idea of writing from West Africa to Europe",
    "E": "the formation of a dialect through isolation from other languages"},
  answer="B",
  rationales={
    "A": "Incorrect. Haitian Creole did not disappear; it became the native language of most Haitians and, since 1987, an official language of Haiti alongside French.",
    "B": "Correct. Creolization is the blending of cultural elements, including languages, into new forms. Under French colonial rule, contact between French and West African languages produced a new language that children learned as their first language.",
    "C": "Incorrect. Haitian Creole formed through intense contact among groups within one colony, not through the gradual spread of French into neighboring areas.",
    "D": "Incorrect. The stem describes a new spoken language forming, not the spread of the idea of writing.",
    "E": "Incorrect. Haitian Creole formed through contact among speakers of different languages, the opposite of isolation."},
  explanation="Creolization happens when cultures come into close contact and mix to make something new. In colonial Haiti, French and West African languages mixed. Children grew up speaking the mix as their first language, and a new language, Haitian Creole, was born.")

# ---- Set D: sequent occupance table, E10-E11 ----
q(id="U3-E10", n=10, set="cityblock", setLabel="Questions 10–11 refer to the table below.",
  topic="3.2", lo="PSO-3.B", skill="4.E", difficulty="medium",
  stimulus=dict(type="table",
    title="CHANGES ON ONE CITY BLOCK IN CITY M, 1880–2025 (HYPOTHETICAL)",
    columns=["Period", "Main group living on the block", "Features added to the landscape"],
    rows=[
      ["1880–1920", "Immigrants from Germany", "Lutheran church with a tall steeple; bakery with a German-language name carved in stone over the door"],
      ["1920–1975", "Families of many backgrounds; many German American families move to the suburbs", "Bakery building becomes a hardware store; the Lutheran congregation shrinks and later moves away"],
      ["1975–2005", "Refugees and immigrants from Vietnam", "Church building bought by a Vietnamese Catholic parish; phở restaurants; shop signs in Vietnamese and English"],
      ["2005–2025", "Immigrants from Mexico and Central America, alongside Vietnamese families", "Taquería in the former bakery building, under the German name still carved over the door; mural of Our Lady of Guadalupe; shop signs in Spanish; the original church steeple still stands"]],
    description="A table showing which group mainly lived on one city block during four periods between 1880 and 2025 and the landscape features added in each period. In the latest period, the German name carved over the old bakery door and the original church steeple are still visible.",
    source="Hypothetical data"),
  stem="The changes shown in the table best illustrate",
  options={
    "A": "placelessness",
    "B": "cultural convergence",
    "C": "stimulus diffusion",
    "D": "sequent occupance",
    "E": "contagious diffusion"},
  answer="D",
  rationales={
    "A": "Incorrect. Placelessness is the loss of uniqueness in a place's landscape; this block has a distinct, layered landscape.",
    "B": "Incorrect. Cultural convergence is cultures becoming more alike through contact; the table shows a series of groups each adding distinct features.",
    "C": "Incorrect. Stimulus diffusion involves an idea spreading and being changed; the table shows successive groups occupying the same place.",
    "D": "Correct. Sequent occupance is the idea that successive societies leave their cultural imprints on a place, each adding to the cultural landscape. German, Vietnamese, and Mexican and Central American residents each added features, and older features such as the steeple and the carved name remain.",
    "E": "Incorrect. Contagious diffusion is the spread of a trait outward to nearby people and places; the table tracks layers of settlement on one block."},
  explanation="Sequent occupance means layers. Different groups live in the same place one after another, and each one adds to the landscape. On this block you can still see the German church steeple and the carved bakery name, along with Vietnamese and Spanish signs from later groups.")

q(id="U3-E11", n=11, set="cityblock", topic="3.2", lo="PSO-3.C", skill="4.C", difficulty="medium",
  stem="The Vietnamese Catholic parish, phở restaurants, and Vietnamese-language signs added between 1975 and 2005 best illustrate which of the following?",
  options={
    "A": "An ethnic neighborhood shaping how space is used, through its own businesses and institutions",
    "B": "Assimilation, because the newcomers gave up their own language and their religion",
    "C": "Syncretism, because the German and Vietnamese religions blended into a new faith",
    "D": "Postmodern architecture, because the newcomers built structures that mix many older styles",
    "E": "Cultural convergence, because the block came to look like city neighborhoods everywhere else"},
  answer="A",
  rationales={
    "A": "Correct. The AP course framework notes that attitudes toward ethnicity, including ethnic neighborhoods, help shape the use of space. The parish, restaurants, and Vietnamese-language signs show a group building institutions and businesses that serve its members and mark the block as its own.",
    "B": "Incorrect. The Vietnamese-language signs and the Vietnamese parish show that residents kept their language and their religious community.",
    "C": "Incorrect. The earlier Lutheran congregation and the later Catholic parish are both Christian, and reusing a church building is not the blending of two religions into a new faith.",
    "D": "Incorrect. The table describes reuse of an existing church and new businesses and signs, not a new architectural style.",
    "E": "Incorrect. The features added are distinctive to one group, which makes the block more distinctive, not more like other places."},
  explanation="When a group settles in one neighborhood, it often builds what it needs: a place of worship, restaurants with familiar food, and signs in its own language. Those choices shape how the space is used and make the block an ethnic neighborhood.")

q(id="U3-E12", n=12, topic="3.2", lo="PSO-3.B", skill="4.E", difficulty="medium",
  stem="In a hot, dry desert region, traditional houses are built from thick mud-brick walls with small windows and flat roofs. These features are best explained as",
  options={
    "A": "evidence of postmodern architecture spreading through globalization",
    "B": "a sign of sequent occupance by several different groups",
    "C": "a result of time-space convergence reducing local differences",
    "D": "evidence that the region's people assimilated into a colonial culture",
    "E": "traditional architecture adapted to the local climate and materials"},
  answer="E",
  rationales={
    "A": "Incorrect. Postmodern architecture is a recent style that mixes elements of past styles; these houses use long-standing local building methods.",
    "B": "Incorrect. Sequent occupance refers to layers left by successive groups; the stem describes one building tradition suited to the environment.",
    "C": "Incorrect. Time-space convergence tends to spread similar building styles across places; these houses reflect local conditions.",
    "D": "Incorrect. Nothing in the stem describes a colonial culture replacing a local one.",
    "E": "Correct. Traditional architecture uses locally available materials and designs suited to local conditions. Thick earthen walls slow the movement of heat into the house, small windows let in less sun, and flat roofs work where little rain falls."},
  explanation="Traditional buildings use what is nearby and fit the weather. In a desert, mud brick is easy to get, thick walls keep out the daytime heat, small windows block the sun, and flat roofs work because it rarely rains. The culture adapted to its physical environment.")

q(id="U3-E13", n=13, topic="3.3", lo="PSO-3.D", skill="2.B", difficulty="medium",
  stem="Belgium includes Flanders in the north, where most people speak Dutch, and Wallonia in the south, where most people speak French. Disputes between the two regions have led Belgium's national government to give the regions more control over their own affairs. In this case, language has acted mainly as",
  options={
    "A": "a centripetal force that unites the two regions",
    "B": "a lingua franca that both regions share",
    "C": "a centrifugal force that divides the state",
    "D": "an example of syncretism between two languages",
    "E": "a result of hierarchical diffusion from Brussels"},
  answer="C",
  rationales={
    "A": "Incorrect. A centripetal force unites a state; here language differences have fueled disputes between regions.",
    "B": "Incorrect. Dutch and French are separate languages that dominate different regions, not one shared language.",
    "C": "Correct. A centrifugal force divides a state. Language differences between Dutch-speaking Flanders and French-speaking Wallonia have fueled political disputes and led to the devolution of power to the regions.",
    "D": "Incorrect. Syncretism is the blending of traits into a new form; Dutch and French remain distinct languages.",
    "E": "Incorrect. The language divide reflects long-standing regional patterns, not diffusion outward from the capital."},
  explanation="Centripetal forces pull a country together. Centrifugal forces push it apart. In Belgium, the north and south mostly speak different languages, and arguments between them led the government to give each region more power. Language here pushes the country apart, so it is a centrifugal force.")

q(id="U3-E14", n=14, topic="3.3", lo="PSO-3.D", skill="1.D", difficulty="medium",
  stem="In parts of southern Louisiana, communities hold festivals featuring Cajun French music and run French immersion programs in public schools. These efforts best illustrate",
  options={
    "A": "assimilation into the dominant national culture",
    "B": "placemaking that builds a regional sense of place",
    "C": "placelessness caused by global popular culture",
    "D": "hierarchical diffusion of French from Paris to Louisiana",
    "E": "a centrifugal force that will divide the United States"},
  answer="B",
  rationales={
    "A": "Incorrect. Assimilation means giving up a group's distinct culture; these efforts keep a distinct culture alive.",
    "B": "Correct. Placemaking is the shaping of places to reflect a community's identity. Festivals and language programs strengthen a distinctive regional identity and residents' attachment to the region, showing how language contributes to a sense of place.",
    "C": "Incorrect. Placelessness is the loss of local uniqueness; these efforts make the region more distinctive.",
    "D": "Incorrect. The stem describes current local efforts to celebrate and teach a regional language, not the original spread of French to Louisiana.",
    "E": "Incorrect. Celebrating a regional culture does not by itself threaten national unity; nothing in the stem suggests a movement to break away."},
  explanation="Placemaking means people shaping their places to show who they are. Cajun music festivals and French classes help the region feel special and different from other places. That builds a strong sense of place.")

q(id="U3-E15", n=15, topic="3.3", lo="PSO-3.D", skill="5.C", difficulty="hard",
  stem="In Country N, almost everyone belongs to Religion 1, which the national government strongly supports. In one large city, however, a growing community of immigrants follows Religion 2, and disputes have arisen over plans to build its first house of worship there. Which statement best describes the role of religion in Country N at different scales?",
  options={
    "A": "Religion is a centrifugal force at the national scale and a centripetal force in the city.",
    "B": "Religion divides the country at both scales, so the state is likely to break apart.",
    "C": "The dispute shows that religion no longer shapes identity at the national scale.",
    "D": "Religion mainly unites the country nationally, but causes tension at the local scale.",
    "E": "Religion 2 spread to the city by hierarchical diffusion from the national capital."},
  answer="D",
  rationales={
    "A": "Incorrect. This reverses the scales: a shared religion unites the country as a whole, and the dispute is local.",
    "B": "Incorrect. The stem describes a dispute in one city; nothing suggests the whole state is dividing.",
    "C": "Incorrect. Nearly everyone in Country N follows Religion 1, which the government supports, so religion still shapes national identity.",
    "D": "Correct. At the national scale, a shared religion acts as a centripetal force. At the local scale, the arrival of a group with a different religion has led to disputes, so religion acts as a centrifugal force there. The role of a cultural factor can differ by scale of analysis.",
    "E": "Incorrect. The stem says the community grew through immigration, which is relocation diffusion, not hierarchical diffusion from the capital."},
  explanation="Scale matters. Look at the whole country: almost everyone shares Religion 1. There, religion pulls people together (centripetal). Now zoom in to one city. There, religious differences are causing arguments (centrifugal). The same thing can work in different ways at different scales.")

# ---- Set B: religions table, E16-E18 ----
q(id="U3-E16", n=16, set="religions", setLabel="Questions 16–18 refer to the table below.",
  topic="3.7", lo="IMP-3.B", skill="3.B", difficulty="easy",
  stimulus=dict(type="table",
    title="FOLLOWERS OF FIVE RELIGIONS, 2025 (HYPOTHETICAL DATA)",
    columns=["Religion", "Hearth region", "Percent of followers living in hearth region", "World regions with at least 1 million followers", "Seeks converts?"],
    rows=[
      ["Religion P", "Region 1", "94", "1", "No"],
      ["Religion Q", "Region 2", "21", "6", "Yes"],
      ["Religion R", "Region 1", "45", "4", "No"],
      ["Religion S", "Region 3", "8", "5", "Yes"],
      ["Religion T", "Region 4", "70", "2", "Yes"]],
    description="A table of five religions showing each religion's hearth region, the percent of its followers who live in that hearth region, the number of world regions with at least 1 million followers, and whether the religion seeks converts.",
    source="Hypothetical data"),
  stem="Which religion in the table shows the pattern most typical of an ethnic religion that has stayed near its hearth?",
  options={"A": "Religion P", "B": "Religion Q", "C": "Religion R", "D": "Religion S", "E": "Religion T"},
  answer="A",
  rationales={
    "A": "Correct. Ethnic religions generally do not seek converts and are usually concentrated near their hearth. Religion P does not seek converts, has 94 percent of its followers in its hearth region, and has at least 1 million followers in only one world region.",
    "B": "Incorrect. Religion Q seeks converts and has at least 1 million followers in six world regions, a pattern typical of a universalizing religion.",
    "C": "Incorrect. Religion R does not seek converts, but more than half of its followers (55 percent) live outside its hearth region, so it has not stayed near its hearth.",
    "D": "Incorrect. Religion S seeks converts and has only 8 percent of its followers in its hearth region.",
    "E": "Incorrect. Religion T is concentrated near its hearth (70 percent), but it seeks converts, a characteristic of universalizing religions."},
  explanation="Ethnic religions usually do not look for new members, so they tend to stay close to home. Religion P does not seek converts, 94% of its followers live in its hearth region, and it has a large following in only one region. That is the classic ethnic pattern.")

q(id="U3-E17", n=17, set="religions", topic="3.7", lo="IMP-3.B", skill="3.E", difficulty="medium",
  stem="Religion R does not seek converts, yet 55 percent of its followers live outside its hearth region. Which process best explains this pattern?",
  options={
    "A": "Hierarchical diffusion, as rulers adopted it and spread it to their subjects",
    "B": "Contagious diffusion, as followers converted their neighbors in nearby regions",
    "C": "Stimulus diffusion, as other religions copied its main beliefs and practices",
    "D": "Expansion diffusion, as missionaries carried it to new continents",
    "E": "Relocation diffusion, as followers moved and carried the religion with them"},
  answer="E",
  rationales={
    "A": "Incorrect. Spreading a religion to subjects through rulers' conversion requires winning new followers, which a religion that does not seek converts generally does not do.",
    "B": "Incorrect. Contagious diffusion through converting neighbors does not fit a religion that does not seek converts.",
    "C": "Incorrect. Stimulus diffusion would change other religions; it would not place Religion R's own followers outside its hearth.",
    "D": "Incorrect. Missionary work is a way of seeking converts, which Religion R does not do.",
    "E": "Correct. Ethnic religions, which generally do not seek converts, spread mainly through relocation diffusion when their followers migrate, whether by choice or by force. Judaism, whose communities spread through many migrations and expulsions over the centuries, is a real-world example."},
  explanation="If a religion does not try to win new members, the main way it can show up far away is if its own followers MOVE there. That is relocation diffusion. Judaism is a real example: over many centuries, Jewish communities moved, or were forced to move, to many parts of the world.")

q(id="U3-E18", n=18, set="religions", topic="3.7", lo="IMP-3.B", skill="3.F", difficulty="hard",
  stem="Which additional information would be most useful for deciding whether Religion S spread mainly through hierarchical diffusion?",
  options={
    "A": "The share of the population in each world region that follows Religion S today",
    "B": "The total number of people who followed Religion S in 2025",
    "C": "Whether rulers and large cities adopted Religion S before smaller places did",
    "D": "The exact location of Religion S's hearth region on a world map",
    "E": "How many world regions have fewer than 1 million followers of Religion S"},
  answer="C",
  rationales={
    "A": "Incorrect. Today's share of followers in each region shows where the religion is now, not the sequence in which it spread.",
    "B": "Incorrect. The total number of followers says nothing about how the religion spread from place to place.",
    "C": "Correct. Hierarchical diffusion moves from people or places of high rank, such as rulers and large cities, down to lower-ranked people and places. Evidence that elites or large cities adopted Religion S before smaller places would show whether that process was at work.",
    "D": "Incorrect. Knowing exactly where the hearth is does not reveal the order or process by which the religion spread.",
    "E": "Incorrect. Counts of followers in other regions describe today's distribution, not the process of diffusion."},
  explanation="The table shows where followers live NOW. To know HOW the religion spread, you need to know the ORDER in which places adopted it. If kings and big cities adopted it first and smaller places later, that is hierarchical diffusion. Today's numbers cannot tell you that.")

q(id="U3-E19", n=19, topic="3.7", lo="IMP-3.B", skill="1.B", difficulty="medium",
  stem="Which of the following best explains why Irish, spoken in western Europe, and Bengali, spoken in South Asia, belong to the same language family?",
  options={
    "A": "British colonial rule spread one language to both Ireland and South Asia.",
    "B": "Both descend from an ancestral language whose speakers spread across Eurasia.",
    "C": "Both borrowed many of the same words recently through the internet and global media.",
    "D": "Both developed in similar climates, which produced similar vocabularies.",
    "E": "Both are creoles that formed when European traders met local populations."},
  answer="B",
  rationales={
    "A": "Incorrect. British rule spread English, but Irish and Bengali are separate languages whose relationship is thousands of years older than British colonialism.",
    "B": "Correct. Irish (Celtic branch) and Bengali (Indo-Iranian branch) both descend from Proto-Indo-European. As speakers of that ancestral language and its descendants spread across Europe and South and Southwest Asia, it split into branches and individual languages.",
    "C": "Incorrect. Language families are defined by shared ancestry, not by recent borrowing of words.",
    "D": "Incorrect. Climate does not produce related languages; relationships come from a common ancestral language.",
    "E": "Incorrect. Neither language is a creole; both are long-established languages with deep histories in their regions."},
  explanation="A language family is like a family tree. Irish and Bengali are very distant cousins. Both come from one very old language, Proto-Indo-European. As its speakers spread out over thousands of years, it split into many branches, like Celtic in the west and Indo-Iranian in the east.")

q(id="U3-E20", n=20, topic="3.7", lo="IMP-3.B", skill="2.D", difficulty="medium",
  stem="Buddhism and Hinduism both began in South Asia. Today most Buddhists live in East and Southeast Asia, while most Hindus still live in South Asia. Which of the following best explains this difference?",
  options={
    "A": "Buddhism is an ethnic religion tied to the peoples of East and Southeast Asia.",
    "B": "Hinduism began more recently than Buddhism, so it has had less time to spread.",
    "C": "The climate of East Asia was better suited to Buddhist practices than South Asia's.",
    "D": "Buddhist missionaries and traders spread it widely; Hinduism is an ethnic religion.",
    "E": "Buddhism spread mainly as large numbers of farmers from South Asia migrated east."},
  answer="D",
  rationales={
    "A": "Incorrect. Buddhism is a universalizing religion; it began in South Asia and spread to East and Southeast Asia.",
    "B": "Incorrect. Hinduism's roots are older than Buddhism, which began about 2,500 years ago.",
    "C": "Incorrect. Climate does not explain the spread of a belief system; the difference reflects how each religion relates to converts.",
    "D": "Correct. Buddhism is a universalizing religion: monks, missionaries, and traders carried it along overland and sea routes to Central, East, and Southeast Asia, and some rulers adopted and promoted it. Hinduism is an ethnic religion that does not generally seek converts, so most Hindus still live near its hearth in South Asia.",
    "E": "Incorrect. Buddhism spread mainly through missionaries, traders, and the support of rulers, not through mass migration of farmers."},
  explanation="Universalizing religions want to share their message with everyone, so they spread far. Buddhist monks traveled with traders along the Silk Roads and sea routes to places like China, Korea, Japan, and Southeast Asia. Hinduism is an ethnic religion that usually does not seek converts, so it mostly stayed in South Asia.")

# ---- Set C: language-loss bar chart, E21-E22 ----
q(id="U3-E21", n=21, set="orvani", setLabel="Questions 21–22 refer to the graph and information below.",
  topic="3.6", lo="SPS-3.A", skill="3.C", difficulty="medium",
  stimulus=dict(type="bar",
    title="SHARE OF PEOPLE WHO SPEAK ORVANI AT HOME, BY AGE GROUP, COUNTRY K, 1995 AND 2025 (HYPOTHETICAL DATA)",
    categories=["Ages 10–19", "Ages 20–39", "Ages 40–59", "Ages 60 and over"],
    series=[dict(name="1995", values=[48, 60, 72, 85]), dict(name="2025", values=[12, 30, 52, 70])],
    yLabel="Percent who speak Orvani at home",
    yMax=100,
    text="Orvani is an Indigenous language spoken mainly in rural areas of Country K. Since 1995, many young people have moved to Country K's cities, where schools and most jobs use the national language and much online content is in English. In 2023, a group of young Orvani speakers launched a popular Orvani-language music channel and video series online.",
    description="Grouped bar chart of the percent of people in each age group who speak Orvani at home in 1995 and 2025. Ages 10–19: 48 and 12. Ages 20–39: 60 and 30. Ages 40–59: 72 and 52. Ages 60 and over: 85 and 70.",
    source="Hypothetical data"),
  stem="Which conclusion is best supported by the graph?",
  options={
    "A": "Orvani use fell more among older people than among younger people.",
    "B": "In 2025, a majority of people ages 20–39 spoke Orvani at home.",
    "C": "Orvani use fell by the same number of percentage points in every age group.",
    "D": "Older people were less likely than younger people to speak Orvani at home in 2025.",
    "E": "Orvani use fell in every age group, and the steepest drop was among the youngest."},
  answer="E",
  rationales={
    "A": "Incorrect. The youngest group fell the most (36 percentage points, from 48 to 12 percent), while people 60 and over fell the least (15 points).",
    "B": "Incorrect. In 2025, 30 percent of people ages 20–39 spoke Orvani at home, less than half.",
    "C": "Incorrect. The declines were 36, 30, 20, and 15 percentage points, so they were not equal.",
    "D": "Incorrect. In 2025, 70 percent of people 60 and over spoke Orvani at home, compared with 12 percent of people ages 10–19.",
    "E": "Correct. Every age group declined, and the 10–19 age group fell the most, by 36 percentage points (from 48 to 12 percent), a sign that the language is not being passed on to younger generations."},
  explanation="Compare each pair of bars. All four groups went down. Ages 10–19 dropped from 48% to 12%, a 36-point fall, the biggest of all. When young people stop speaking a language, it is in danger of dying out.")

q(id="U3-E22", n=22, set="orvani", topic="3.6", lo="SPS-3.A", skill="4.C", difficulty="hard",
  stem="The online Orvani-language music channel described in the information best illustrates which of the following?",
  options={
    "A": "Online media can promote cultural divergence by helping a minority language stay distinct.",
    "B": "Online media spread English worldwide, so the channel is an example of cultural convergence.",
    "C": "Urbanization reversed the decline in Orvani use among young people by 2025.",
    "D": "Relocation diffusion carried Orvani from the cities back out to rural villages.",
    "E": "Assimilation, because young Orvani speakers adopted the national culture online."},
  answer="A",
  rationales={
    "A": "Correct. The AP course framework notes that communication technologies such as the internet can create both cultural convergence and cultural divergence. An Orvani-language channel uses global technology to keep a minority language distinct, an example of cultural divergence.",
    "B": "Incorrect. The channel is in Orvani, not English, so it makes the local culture more distinct rather than more like global culture.",
    "C": "Incorrect. The graph shows Orvani use falling in every age group between 1995 and 2025; nothing shows the decline reversing.",
    "D": "Incorrect. The information describes an online channel, not people moving from cities to villages.",
    "E": "Incorrect. Creating content in their own minority language is the opposite of giving up that language for the national culture."},
  explanation="The internet can work in two directions. It can make cultures more alike, for example by spreading English. But it can also help small cultures survive: young people used it to share music and videos in Orvani. That pushes back against cultural convergence. Geographers call this cultural divergence.")

q(id="U3-E23", n=23, topic="3.6", lo="SPS-3.A", skill="1.A", difficulty="easy",
  stem="In the mid-1800s, before the first lasting telegraph cable crossed the Atlantic Ocean in 1866, news traveled between Europe and North America by ship and took more than a week to arrive. Today, a video posted in London can be watched in New York seconds later. This change best illustrates",
  options={
    "A": "distance decay",
    "B": "stimulus diffusion",
    "C": "time-space convergence",
    "D": "relocation diffusion",
    "E": "hierarchical diffusion"},
  answer="C",
  rationales={
    "A": "Incorrect. Distance decay is the decline in interaction as distance increases; the stem describes the time needed to connect two places shrinking.",
    "B": "Incorrect. Stimulus diffusion is the spread of an idea that is changed by the culture receiving it.",
    "C": "Correct. Time-space convergence is the reduction in the time it takes for people, goods, or information to travel between places because of improvements in transportation and communication technology.",
    "D": "Incorrect. Relocation diffusion involves people moving and carrying culture with them; the video spreads without anyone moving.",
    "E": "Incorrect. Hierarchical diffusion moves from more important people or places to less important ones; the stem is about how fast information travels."},
  explanation="Time-space convergence means places feel closer together because it takes less time to reach them. News that once took more than a week by ship now arrives in seconds. London and New York did not move, but in travel time they got much closer.")

q(id="U3-E24", n=24, topic="3.8", lo="SPS-3.B", skill="1.D", difficulty="medium",
  stem="Santería, a religion that developed in Cuba, honors spirits called orichas that come from the Yoruba religion of West Africa. Enslaved Yoruba people brought this religion to the island. Many orichas are identified with Roman Catholic saints introduced under Spanish colonial rule. Santería best illustrates",
  options={
    "A": "assimilation, because the Yoruba traditions disappeared into Catholicism",
    "B": "syncretism, because elements of two religions blended into a new form",
    "C": "multiculturalism, because the two religions stayed separate side by side",
    "D": "ethnocentrism, because one group judged the other's religion as inferior",
    "E": "contagious diffusion, because Santería spread from Cuba to nearby islands"},
  answer="B",
  rationales={
    "A": "Incorrect. Yoruba traditions did not disappear; they remain central to Santería.",
    "B": "Correct. Syncretism is the blending of elements from different cultures, such as religious beliefs and practices, into a new cultural form. Santería combines Yoruba religious traditions with elements of Roman Catholicism.",
    "C": "Incorrect. Multiculturalism describes distinct cultures coexisting while keeping their identities; in Santería, the traditions merged.",
    "D": "Incorrect. Ethnocentrism is an attitude of judging other cultures by one's own standards; it does not describe the blending of religions.",
    "E": "Incorrect. The stem describes how Santería formed, not how it spread to other places."},
  explanation="Syncretism means blending. Santería took parts of Yoruba religion from West Africa and parts of Catholicism from Spain and merged them into something new. Both traditions are still visible inside it.")

q(id="U3-E25", n=25, topic="3.8", lo="SPS-3.B", skill="2.C", difficulty="medium",
  stem="In 1971, Canada adopted an official national policy of multiculturalism. The policy encourages immigrants and other groups to keep their own languages, religions, and traditions while taking part in Canadian society. Which outcome would this policy most likely encourage?",
  options={
    "A": "Immigrants abandoning their heritage languages within one generation",
    "B": "Neighborhoods losing their distinct ethnic businesses and festivals",
    "C": "The blending of the country's religions into one new national faith",
    "D": "Many groups keeping distinct identities while sharing one society",
    "E": "A single national culture replacing regional and ethnic differences"},
  answer="D",
  rationales={
    "A": "Incorrect. Losing a heritage language within one generation is a sign of assimilation; the policy encourages groups to keep their languages.",
    "B": "Incorrect. The policy supports keeping traditions, so it would encourage, not erase, distinct ethnic businesses and festivals.",
    "C": "Incorrect. That describes syncretism, the blending of religions; the policy supports groups keeping their own religions.",
    "D": "Correct. Multiculturalism is the coexistence of many cultural groups within one society, each keeping its own identity. Canada's policy encourages groups to maintain their languages, religions, and traditions while participating in national life.",
    "E": "Incorrect. A single culture replacing differences describes assimilation or cultural convergence, not multiculturalism."},
  explanation="Multiculturalism means many cultures living together in one country. Each group keeps its own identity. Canada's policy asks groups to keep their languages and traditions while also being Canadian. Think of a salad, where each food stays itself. A soup is different: everything blends.")
