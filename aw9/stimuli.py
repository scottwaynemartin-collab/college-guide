# AP World Unit 9 sources. Texts follow the editions saved in aw9/sources/raw/ and documented in
# aw9/sources/*.md. Cuts are marked with ellipses; bracketed words are clarifications.
# Copyright basis (see each .md): works of the U.S. government (speeches and statements of U.S.
# presidents and officials, the Congressional Record, FRUS, CRS reports, FBIS translations and
# transcripts, NASA and U.S. Army photographs); a British Indian government report published in 1920;
# the Universal Declaration of Human Rights (freely reproducible); and open data under CC BY 4.0
# (World Bank World Development Indicators; Global Carbon Budget via Our World in Data).
# No copyrighted post-1930 non-government text is used.
VERSION = "2026-11-08a"

def P(paragraphs, attribution, translation="", footnotes=None, glossary=None, **kw):
    d = {"type": "passage", "paragraphs": paragraphs, "attribution": attribution}
    if translation: d["translation"] = translation
    if footnotes: d["footnotes"] = footnotes
    if glossary: d["glossary"] = glossary
    d.update(kw)
    return d

def item(label, paragraphs, attribution, translation="", footnotes=None, glossary=None):
    d = {"label": label, "paragraphs": paragraphs, "attribution": attribution}
    if translation: d["translation"] = translation
    if footnotes: d["footnotes"] = footnotes
    if glossary: d["glossary"] = glossary
    return d

STIM = {
# ============================== EXAM ==============================
"X1": P([
    "In May 1967 Pakistan harvested 600,000 acres to new high-yielding wheat seed. … In 1967 the new high-yielding wheats were harvested from 700,000 acres in India. This year they will be planted to 6 million acres. … India will harvest more than 95 million tons in food grains this year—again a record crop. …",
    "These and other developments in the field of agriculture contain the makings of a new revolution. It is not a [violent] Red Revolution like that of the Soviets, nor is it a White Revolution like that of the Shah of Iran. I call it the Green Revolution.",
    "This new revolution can be as significant and as beneficial to mankind as the industrial revolution of a century and a half ago. … Good luck—good monsoons—helped bring in the recent record harvests. But hard work, good management, and sound agricultural policies in the developing countries and foreign aid were also very much involved. …",
    "[A new rice variety called] IR-8 has a stiff, strong, short straw. It does not fall over, or lodge, when the plant is heavily fertilized or when it is buffeted by wind and rain. It matures quickly, allowing for two—sometimes three—crops in a single year. …",
    "But the developing nations—their governments, their institutions, and their farmers—cannot sustain the Green Revolution without outside support. They lack the skills to do the necessary adaptive research. They lack the capital to build fertilizer plants. They lack the facilities and the technicians needed to train their people in the new ways. …",
    "To the farmer, the new seeds and fertilizer represent an untried and expensive investment. The high yields of IR-8 depend on a combination of intensive labor and materials which makes it four times as costly to [grow] as ordinary rice."],
    "William S. Gaud, head of the U.S. Agency for International Development (USAID), the government office that ran U.S. foreign aid, speech to the Society for International Development, Washington, D.C., March 8, 1968",
    "Adapted",
    glossary=[{"t": "high-yielding", "d": "producing a large harvest from each acre"},
              {"t": "White Revolution", "d": "a program of land reform and modernization begun by the shah (king) of Iran in 1963"},
              {"t": "monsoons", "d": "the seasonal rains that water most of the farmland of South Asia"},
              {"t": "lodge", "d": "(of a crop) fall over flat, so that the grain is hard to harvest"},
              {"t": "buffeted", "d": "knocked about"},
              {"t": "adaptive research", "d": "testing new seeds to fit them to local soil and weather"},
              {"t": "capital", "d": "money used to build factories and buy machines"}]),

"X2": P([
    "There is ample evidence during the first epidemic of the introduction of infection into a locality from another infected locality. The railway played a prominent part as was inevitable. During the panic caused by the epidemic the trains were filled with emigrants from infected centres, many of them being ill. The Post office also was an important agency in disseminating infection, also very largely through the Railway Postal Service. … Marwari traders, shopkeepers and even doctors, in fact all who travelled by water, road or rail, were potential factors in distributing infection.",
    "There is no method by which the deaths actually due to influenza can be calculated. If it be assumed that the excess in the deaths in 1918 over the mean of the previous 5 years was the result—direct or indirect—of influenza, the figure would come to 7,718,307. This is an overestimate owing to the disturbing factor of other epidemic diseases, such as plague, cholera, malaria and relapsing fever … . Without any claim to accuracy it is suggested that the mortality directly and indirectly due to influenza was in the neighbourhood of … 7,089,694.",
    "When it is remembered that the epidemic struck India suddenly and almost universally it will be realised to what extent the medical organization already thinned by military needs was taxed. … The failure to meet the demand [for doctors] was due to two causes: (a) the necessity for supplying medical officers for the war. A similar need depleted the civil medical practitioners in all countries taking part in the late struggle, (b) the Medical Colleges and Schools in India cannot turn out a sufficient number of medical men to meet the normal demand. …",
    "Rural areas depend for their medical aid on dispensaries, and these dispensaries are, speaking for India as a whole, too widely separated to be of general utility in a wide spread epidemic."],
    "Annual Report of the Sanitary Commissioner with the Government of India for 1918, a yearly report on disease and deaths by the chief public health official of British India, printed in Calcutta, India, in 1920",
    "Adapted",
    glossary=[{"t": "emigrants from infected centres", "d": "here, people fleeing from cities where the disease had broken out"},
              {"t": "disseminating", "d": "spreading"},
              {"t": "Railway Postal Service", "d": "mail carried and sorted on trains"},
              {"t": "Marwari traders", "d": "merchants from Rajasthan in western India who did business all over India"},
              {"t": "excess in the deaths", "d": "the number of deaths above the usual yearly number"},
              {"t": "mortality", "d": "number of deaths"},
              {"t": "taxed", "d": "here, strained; pushed to its limits"},
              {"t": "civil medical practitioners", "d": "doctors who treat ordinary people, not soldiers"},
              {"t": "dispensaries", "d": "small clinics that give out medicine"}]),

"X3": {"type": "bar",
    "title": "Life Expectancy at Birth in Selected Countries, 1970–2023",
    "categories": ["World", "Japan", "China", "Brazil", "India", "South\nAfrica", "Botswana", "Nigeria"],
    "series": [{"name": "1970", "values": [57.9, 71.9, 56.8, 57.3, 48.6, 55.7, 56.4, 40.0]},
               {"name": "1990", "values": [65.1, 78.8, 68.2, 65.9, 58.6, 62.9, 60.1, 45.7]},
               {"name": "2005", "values": [69.1, 82.0, 74.1, 71.8, 64.9, 53.9, 54.4, 49.5]},
               {"name": "2023", "values": [73.3, 84.0, 78.0, 75.8, 72.0, 66.1, 69.2, 54.5]}],
    "yLabel": "Life expectancy (years)",
    "text": "Life expectancy at birth is the number of years a newborn baby would live, on average, if the death rates of the year of its birth stayed the same all through its life. The figures are estimates made by the United Nations Population Division and reported by the World Bank. Estimates for the earlier years rest on incomplete records in some countries.",
    "source": "World Bank, World Development Indicators, \"Life expectancy at birth, total (years)\" (indicator SP.DYN.LE00.IN), from United Nations, World Population Prospects; data updated October 2026; CC BY 4.0"},

"X4": {"type": "image",
    "src": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/NASA-Apollo8-Dec24-Earthrise.jpg/960px-NASA-Apollo8-Dec24-Earthrise.jpg",
    "width": 960, "height": 960,
    "alt": "A color photograph of the Earth, half in shadow, above the gray curved horizon of the Moon, against a black sky.",
    "caption": "The Earth, half lit by the Sun and half in shadow, appears above the gray, cratered horizon of the Moon. White clouds swirl over blue oceans. The rest of the sky is black.",
    "attribution": "William Anders, U.S. astronaut, photograph taken from the Apollo 8 spacecraft while it orbited the Moon, December 24, 1968",
    "credit": "NASA photograph AS08-14-2383. Public domain image via Wikimedia Commons.",
    "description": "A square color photograph. The bottom quarter shows the surface of the Moon: a gray, curving horizon covered with small craters and ridges. Above it is a black sky with no stars. A little to the right of center, the Earth hangs above the horizon. Only part of it is lit, so it looks like a half circle. The lit part is blue, with white swirls of cloud and a patch of brown land near the shadow line."},

"X5": {"type": "pair", "items": [
    item("Source 1", [
        "The year of 1989 will go down in history as the year in which Stalinist communism expired. These developments will entail unpredictable consequences for Europe, but they will also be of a decisive importance to Africa. … The collapse, particularly of the Marxist economic system in Eastern Europe, also served as a warning to those who insist on persisting with it in Africa. …",
        "The steps that have been decided are the following: the prohibition of the African National Congress, the Pan-Africanist Congress, the South African Communist Party, and a number of subsidiary organizations have been rescinded. …",
        "On one matter there must be no doubt: The lifting of the ban on the named organizations does not mean in any way the approval or condonation of terrorism or crimes of violence committed under their banners … .",
        "The agenda is opened, and the overall aims to which we are aspiring should be acceptable to all reasonable South Africans. Among other things, those aims include: a new democratic constitution; universal franchise; no domination, equality before an independent judiciary; the protection of minorities, as well as of individual rights; freedom of religion; a sound economy based on proven economic principles and private enterprise … . I wish to put it plainly that the government has taken a firm decision to release Mr Mandela unconditionally. …",
        "The time for talking has arrived, and whoever still makes excuses does not really wish to talk. Therefore, I repeat my invitation with greater conviction than ever: Walk through the open door, take your place at the negotiating table together with the government and other leaders … ."],
        "F. W. de Klerk, state president of South Africa and leader of the National Party, speech at the opening of Parliament, Cape Town, February 2, 1990",
        "As broadcast by South African radio and recorded by the U.S. Foreign Broadcast Information Service (FBIS), a U.S. government agency; parts of the speech given in Afrikaans were translated by FBIS; adapted",
        glossary=[{"t": "Stalinist communism", "d": "communist rule with a single party, a planned economy, and a powerful secret police, on the model of Joseph Stalin's Soviet Union"},
                  {"t": "African National Congress", "d": "the ANC, the oldest Black political organization in South Africa, banned by the government since 1960"},
                  {"t": "rescinded", "d": "canceled"},
                  {"t": "condonation", "d": "approval; excusing"},
                  {"t": "universal franchise", "d": "the right of all adults to vote"}]),
    item("Source 2", [
        "Today, the majority of South Africans, black and white, recognize that apartheid has no future. It has to be ended by our own decisive mass action in order to build peace and security. …",
        "Our resort to the armed struggle in 1960, with the formation of the military wing of the ANC [African National Congress], Umkonto we Sizwe [Spear of the Nation] … was a purely defensive action against the violence of apartheid. … We have no option but to continue. …",
        "Mr. de Klerk has gone further than any other Nationalist president in taking real steps to normalize the situation. However, there are further steps … that have to be met before negotiation on the basic demands of our people can begin. I reiterate our call for, inter alia, the immediate ending of the state of emergency and the freeing of all, and not only some, political prisoners. …",
        "We call on the international community to continue the campaign to isolate the apartheid regime. To lift sanctions now would be to run the risk of aborting the process toward the complete eradication of apartheid. … Universal suffrage on a common voters' roll in a united democratic and nonracial South Africa is the only way to peace and racial harmony."],
        "Nelson Mandela, leader of the African National Congress (ANC), speech to a crowd in Cape Town on the day he was released after 27 years in prison, February 11, 1990",
        "As broadcast by South African television and recorded by the U.S. Foreign Broadcast Information Service (FBIS); adapted",
        glossary=[{"t": "Nationalist president", "d": "a president from the National Party, which had ruled South Africa since 1948"},
                  {"t": "inter alia", "d": "Latin for \"among other things\""},
                  {"t": "state of emergency", "d": "special rules that let the police ban meetings and hold people in jail without trial"},
                  {"t": "eradication", "d": "complete removal"},
                  {"t": "common voters' roll", "d": "one list of voters for people of all races"}])]},

"X6": P([
    "With the ratification of the North American Free Trade Agreement [NAFTA] by the U.S. House of Representatives today, one more step has been taken for the creation of the world's largest free trade market between sovereign countries. The agreement provides clear and permanent rules for commerce and investment, which will create jobs and opportunities in our country.",
    "In view of this, I wish to say that Mexicans regard the agreement as an additional instrument in our foreign strategy, to be added to the fundamental changes we have already initiated and are consolidating. These changes had been taking place before NAFTA … . We will fully fulfill NAFTA's pledges. In addition, we will not spare efforts to diversify our relations, particularly with Latin America, the EC, and the Pacific Basin. …",
    "I reiterate that we should not expect immediate effects from NAFTA. The agreement was negotiated in such a manner that it will be gradually enacted over the course of 15 years. The neediest sectors will be given time to rejuvenate their competitive capabilities and forge ahead. …",
    "Today's result can be seen not only as the final step toward the approval of the agreement negotiated and signed by the governments of the three countries, but also as a rejection of protectionist propositions—those that promote fear for competition and those that are closed to long-term perceptions and to the future.",
    "On the march toward free trade, voices have been earnestly raised in the three countries. Some people spoke in favor and others against the agreement. Some people tried, with arguments, to shun the greatness of the Mexican people. … In Mexico, the trust and the great character of our people cannot be subjected to any passing of judgment abroad. We know what we are worth and we are working to build our own future."],
    "Carlos Salinas de Gortari, president of Mexico, statement on Mexican television after the U.S. House of Representatives voted to approve NAFTA, Mexico City, November 17, 1993",
    "Translated from Spanish by the U.S. Foreign Broadcast Information Service (FBIS), a U.S. government agency; adapted",
    glossary=[{"t": "ratification", "d": "formal approval of a treaty"},
              {"t": "sovereign", "d": "independent; governing themselves"},
              {"t": "consolidating", "d": "making stronger and more lasting"},
              {"t": "EC", "d": "the European Community, which became part of the new European Union in November 1993"},
              {"t": "Pacific Basin", "d": "the countries around the Pacific Ocean, such as Japan"},
              {"t": "rejuvenate", "d": "make young and strong again"},
              {"t": "protectionist", "d": "favoring taxes or limits on imports to shield a country's own businesses"},
              {"t": "shun", "d": "here, belittle or deny"}]),

"X7": P([
    "… The spread of information networks is forming a new nervous system for our planet. When something happens in Haiti or Hunan, the rest of us learn about it in real time—from real people. And we can respond in real time as well. …",
    "Now, in many respects, information has never been so free. There are more ways to spread more ideas to more people than at any moment in history. And even in authoritarian countries, information networks are helping people discover new facts and making governments more accountable. …",
    "… In the last year, we've seen a spike in threats to the free flow of information. China, Tunisia, and Uzbekistan have stepped up their censorship of the internet. In Vietnam, access to popular social networking sites has suddenly disappeared. …",
    "… Some countries have erected electronic barriers that prevent their people from accessing portions of the world's networks. They've expunged words, names, and phrases from search engine results. … These actions contravene the Universal Declaration on Human Rights, which tells us that all people have the right \"to seek, receive and impart information and ideas through any media and regardless of frontiers.\" With the spread of these restrictive practices, a new information curtain is descending across much of the world. …",
    "… In many cases, the internet, mobile phones, and other connection technologies can do for economic growth what the Green Revolution did for agriculture."],
    "Hillary Rodham Clinton, U.S. secretary of state, \"Remarks on Internet Freedom,\" speech at the Newseum, a museum of journalism, Washington, D.C., January 21, 2010",
    "Adapted",
    glossary=[{"t": "Hunan", "d": "a province in south-central China"},
              {"t": "authoritarian", "d": "ruled by leaders who allow little political freedom"},
              {"t": "accountable", "d": "required to explain their actions to the people"},
              {"t": "censorship", "d": "a government's blocking of speech, writing, or information"},
              {"t": "expunged", "d": "erased"},
              {"t": "contravene", "d": "go against; break"},
              {"t": "impart", "d": "share; pass on"}]),

"X8": {"type": "bar",
    "title": "People Using the Internet in Selected Countries, 2000–2022 (percent of population)",
    "categories": ["United\nStates", "South\nKorea", "Finland", "China", "Brazil", "Mexico", "India", "Nigeria"],
    "series": [{"name": "2000", "values": [43.1, 44.7, 37.2, 1.8, 2.9, 5.1, 0.5, 0.1]},
               {"name": "2010", "values": [71.7, 83.7, 86.9, 34.3, 40.6, 31.1, 7.5, 11.5]},
               {"name": "2022", "values": [92.7, 97.2, 93.0, 75.6, 80.5, 78.6, 55.9, 39.1]}],
    "yLabel": "Percent of population",
    "text": "An internet user is a person who used the internet from any place, on any device, in the past three months. The figures come from national surveys and from estimates by the International Telecommunication Union (ITU), a United Nations agency, and are reported by the World Bank.",
    "source": "World Bank, World Development Indicators, \"Individuals using the Internet (% of population)\" (indicator IT.NET.USER.ZS), from the ITU World Telecommunication/ICT Indicators Database; data updated October 2026; CC BY 4.0"},

# ============================== PRACTICE ==============================
"P1": P([
    "The United States knows that if the fearful trend of atomic military buildup can be reversed, this greatest of destructive forces can be developed into a great boon, for the benefit of all mankind.",
    "The United States knows that peaceful power from atomic energy is no dream of the future. That capability, already proved, is here—now—today. …",
    "I therefore make the following proposals: The Governments principally involved, to the extent permitted by elementary prudence, to begin now and continue to make joint contributions from their stockpiles of normal uranium and fissionable materials to an International Atomic Energy Agency. We would expect that such an agency would be set up under the aegis of the United Nations. …",
    "The more important responsibility of this Atomic Energy Agency would be to devise methods whereby this fissionable material would be allocated to serve the peaceful pursuits of mankind. Experts would be mobilized to apply atomic energy to the needs of agriculture, medicine, and other peaceful activities. A special purpose would be to provide abundant electrical energy in the power-starved areas of the world. Thus the contributing powers would be dedicating some of their strength to serve the needs rather than the fears of mankind. …",
    "Of those \"principally involved\" the Soviet Union must, of course, be one."],
    "Dwight D. Eisenhower, president of the United States, speech to the General Assembly of the United Nations, New York City, December 8, 1953",
    "Adapted",
    glossary=[{"t": "boon", "d": "a blessing; something helpful"},
              {"t": "elementary prudence", "d": "basic caution"},
              {"t": "fissionable materials", "d": "materials, such as some kinds of uranium, whose atoms can be split to release energy"},
              {"t": "under the aegis of", "d": "under the protection and guidance of"},
              {"t": "devise", "d": "plan; invent"}]),

"P2": {"type": "bar",
    "title": "Total Fertility Rate in Selected Countries, 1970 and 2023 (average births per woman)",
    "categories": ["Nigeria", "Bangladesh", "Iran", "Mexico", "India", "China", "Brazil", "United\nStates", "South\nKorea"],
    "series": [{"name": "1970", "values": [6.5, 6.8, 6.8, 6.5, 5.6, 6.1, 4.9, 2.5, 4.5]},
               {"name": "2023", "values": [4.5, 2.2, 1.7, 1.9, 2.0, 1.0, 1.6, 1.6, 0.7]}],
    "yLabel": "Births per woman",
    "text": "The total fertility rate is the average number of children a woman would have in her lifetime if she had children at the rates of that year. A rate of about 2.1 keeps a population the same size over time, not counting migration. The figures are estimates made by the United Nations Population Division and reported by the World Bank. The world average was 4.8 in 1970 and 2.2 in 2023.",
    "source": "World Bank, World Development Indicators, \"Fertility rate, total (births per woman)\" (indicator SP.DYN.TFRT.IN), from United Nations, World Population Prospects; data updated October 2026; CC BY 4.0"},

"P3": {"type": "image",
    "src": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Emergency_hospital_during_Influenza_epidemic%2C_Camp_Funston%2C_Kansas_-_NCP_1603.jpg/960px-Emergency_hospital_during_Influenza_epidemic%2C_Camp_Funston%2C_Kansas_-_NCP_1603.jpg",
    "width": 960, "height": 719,
    "alt": "A black-and-white photograph of a huge wooden hall filled with rows of cots, where sick men lie or sit while workers in white gowns care for them.",
    "caption": "Rows of cots fill a huge wooden hall. Sick men lie or sit on the cots, many wrapped in blankets. Workers in long white gowns care for them, and some of the workers wear cloth masks over their noses and mouths. A man in an army uniform stands in the center aisle.",
    "attribution": "Photograph of an emergency hospital set up at Camp Funston, a U.S. Army training camp in Kansas, during the influenza epidemic, about 1918",
    "credit": "Otis Historical Archives, National Museum of Health and Medicine (U.S. Army), photograph NCP 1603. Public domain image via Wikimedia Commons.",
    "description": "A wide black-and-white photograph taken from one end of a long wooden building with a high roof of crossed beams and hanging light bulbs. Dozens of metal cots stand in rows on both sides of a center aisle and stretch to the far wall. Men lie in the beds under blankets or sit up on them. In the front, a worker in a white gown sits on a cot beside a man lying down. In the middle, another worker in a white gown wears a cloth mask over his nose and mouth. A woman in a white cap sits farther back. A man in a dark army uniform stands in the aisle. Two large fans hang on the far wall."},

"P4": P([
    "Today, on the continent of Africa, nearly 30 million people have the AIDS virus, including 3 million children under the age 15. There are whole countries in Africa where more than one-third of the adult population carries the infection. More than 4 million require immediate drug treatment. Yet across that continent, only 50,000 AIDS victims—only 50,000—are receiving the medicine they need. Because the AIDS diagnosis is considered a death sentence, many do not seek treatment. Almost all who do are turned away. …",
    "AIDS can be prevented. Antiretroviral drugs can extend life for many years. And the cost of those drugs has dropped from $12,000 a year to under $300 a year, which places a tremendous possibility within our grasp. …",
    "… To meet a severe and urgent crisis abroad, tonight I propose the Emergency Plan for AIDS Relief, a work of mercy beyond all current international efforts to help the people of Africa. This comprehensive plan will prevent 7 million new AIDS infections, treat at least 2 million people with life-extending drugs, and provide humane care for millions of people suffering from AIDS and for children orphaned by AIDS. I ask the Congress to commit $15 billion over the next 5 years … to turn the tide against AIDS in the most afflicted nations of Africa and the Caribbean."],
    "George W. Bush, president of the United States, State of the Union address to Congress, Washington, D.C., January 28, 2003",
    "Adapted",
    glossary=[{"t": "AIDS virus", "d": "HIV, the virus that causes AIDS (acquired immunodeficiency syndrome), a disease that destroys the body's defenses against infection"},
              {"t": "antiretroviral drugs", "d": "medicines that keep HIV from multiplying in the body"},
              {"t": "afflicted", "d": "suffering; badly hit"}]),

"P5": P([
    "The great question of the seventies is, shall we surrender to our surroundings, or shall we make our peace with nature and begin to make reparations for the damage we have done to our air, to our land, and to our water?",
    "Restoring nature to its natural state is a cause beyond party and beyond factions. It has become a common cause of all the people of this country. It is a cause of particular concern to young Americans, because they more than we will reap the grim consequences of our failure to act on programs which are needed now if we are to prevent disaster later. …",
    "We still think of air as free. But clean air is not free, and neither is clean water. The price tag on pollution control is high. Through our years of past carelessness we incurred a debt to nature, and now that debt is being called. …",
    "The automobile is our worst polluter of the air. … We can no longer afford to consider air and water common property, free to be abused by anyone without regard to the consequences. …",
    "Now, I realize that the argument is often made that there is a fundamental contradiction between economic growth and the quality of life, so that to have one we must forsake the other. The answer is not to abandon growth, but to redirect it. …"],
    "Richard Nixon, president of the United States, State of the Union address to Congress, Washington, D.C., January 22, 1970",
    "Adapted",
    glossary=[{"t": "reparations", "d": "payments or actions to make up for harm done"},
              {"t": "factions", "d": "groups within a larger group that disagree with one another"},
              {"t": "incurred a debt", "d": "came to owe something"},
              {"t": "common property", "d": "here, things that belong to everyone, so no one takes care of them"},
              {"t": "forsake", "d": "give up"}]),

"P6": {"type": "bar",
    "title": "Carbon Dioxide Emissions from Fossil Fuels and Industry, Selected Countries, 1970–2024 (billions of tonnes per year)",
    "categories": ["China", "United\nStates", "European\nUnion", "India", "Russia", "Japan"],
    "series": [{"name": "1970", "values": [0.8, 4.3, 3.3, 0.2, 1.4, 0.8]},
               {"name": "1990", "values": [2.5, 5.1, 3.9, 0.6, 2.5, 1.2]},
               {"name": "2010", "values": [8.6, 5.7, 3.4, 1.7, 1.6, 1.2]},
               {"name": "2024", "values": [12.3, 4.9, 2.4, 3.2, 1.8, 1.0]}],
    "yLabel": "Billions of tonnes of CO2",
    "text": "The figures count carbon dioxide (CO2) released by burning coal, oil, and natural gas and by making cement and some other products. They do not count emissions from cutting down forests. \"European Union\" means the 27 countries that belonged to it in 2024, counted together for every year shown. \"Russia\" means the land of today's Russia, which was part of the Soviet Union until 1991. A tonne (metric ton) is 1,000 kilograms, about 2,200 pounds.",
    "source": "Global Carbon Project, Global Carbon Budget 2025, as compiled by Our World in Data (owid-co2-data, column \"co2\"); downloaded November 2026; CC BY 4.0"},

"P7": P([
    "These United States are confronted with an economic affliction of great proportions. We suffer from the longest and one of the worst sustained inflations in our national history. … Idle industries have cast workers into unemployment, human misery, and personal indignity. Those who do work are denied a fair return for their labor by a tax system which penalizes successful achievement and keeps us from maintaining full productivity.",
    "But great as our tax burden is, it has not kept pace with public spending. For decades we have piled deficit upon deficit, mortgaging our future and our children's future for the temporary convenience of the present. …",
    "In this present crisis, government is not the solution to our problem; government is the problem. …",
    "… It is time to check and reverse the growth of government, which shows signs of having grown beyond the consent of the governed.",
    "It is my intention to curb the size and influence of the Federal establishment … ."],
    "Ronald Reagan, president of the United States, inaugural address, Washington, D.C., January 20, 1981",
    "Adapted",
    glossary=[{"t": "affliction", "d": "something that causes suffering"},
              {"t": "inflations", "d": "periods when prices keep rising"},
              {"t": "deficit", "d": "the amount by which a government spends more than it collects in taxes in a year"},
              {"t": "curb", "d": "hold back; limit"},
              {"t": "Federal establishment", "d": "the national government in Washington and its agencies"}]),

"P8": P([
    "… There is little doubt that the present Chinese leadership led by Deng Xiaoping is most determined to push forward with a rapid pace of modernization. They consider close trade and economic relations with the United States as essential for this purpose. …",
    "… One senses a still tentative and uncertain coalition of those Chinese leaders committed to the new policy of pushing economic development based on a re-orientation of their economy toward trade with, and investments by, the West. … The change in direction which the leadership has now embarked on is so drastic—and so contrary to the policies and ideology of the past—that no one can say with certainty how long they will persist in this course, particularly when the going gets rough. …",
    "The \"Forever\" bicycle factory I visited in Shanghai illustrates graphically these strengths [China's huge, hard-working labor force], but also the inherent weaknesses. … The flow of materials and the production process is poorly laid out and reveals a lack of any real knowledge of modern manufacturing methods. … Yet, the Chinese turn out 1,700,000 a year from that place. … They do it with a massive application of people—3,900 to be exact … .",
    "In my view, the key element which will determine the success or failure of the Chinese experiment will be the persistence with which the Chinese can pursue a flexible approach in their emerging dealings with the West. If they do indeed carry through their professed intention to shake off important elements of Communist economic dogma, and consent to foreign investment and the direct infusion of foreign management know-how, based on profit incentives, they have a chance to go forward rapidly."],
    "W. Michael Blumenthal, U.S. secretary of the treasury, confidential memorandum to President Jimmy Carter after Blumenthal's visit to China, March 5, 1979",
    "From Foreign Relations of the United States, 1977–1980, vol. 13, China (U.S. Department of State, 2013); adapted",
    glossary=[{"t": "tentative", "d": "not yet settled; unsure"},
              {"t": "coalition", "d": "a group that works together for a shared goal"},
              {"t": "re-orientation", "d": "turning in a new direction"},
              {"t": "professed intention", "d": "stated plan"},
              {"t": "dogma", "d": "beliefs that must not be questioned"},
              {"t": "infusion", "d": "pouring in; adding"},
              {"t": "profit incentives", "d": "rewards for making money"}]),

"P9": {"type": "table",
    "title": "Women in the Labor Force in Selected Countries, 1990 and 2024 (percent of women ages 15 and older)",
    "columns": ["Country", "1990", "2024"],
    "rows": [["World", "51.2", "49.1"],
             ["China", "73.1", "59.4"],
             ["United States", "56.0", "56.6"],
             ["Japan", "50.1", "55.6"],
             ["Brazil", "44.4", "53.6"],
             ["Mexico", "34.0", "47.4"],
             ["Bangladesh", "24.2", "38.7"],
             ["Saudi Arabia", "15.0", "33.3"],
             ["India", "30.3", "32.4"],
             ["Egypt", "22.2", "18.5"]],
    "text": "The labor force is everyone who has a paid job or is looking for one, including people who work on a family farm or in a family business. Unpaid work caring for one's own home and family is not counted. The figures are estimates made by the International Labour Organization (ILO), a United Nations agency, from national surveys, and are reported by the World Bank.",
    "source": "World Bank, World Development Indicators, \"Labor force participation rate, female (% of female population ages 15+) (modeled ILO estimate)\" (indicator SL.TLF.CACT.FE.ZS); data updated October 2026; CC BY 4.0"},

"P10": P([
    "I speak tonight for the dignity of man and the destiny of democracy. …",
    "At times history and fate meet at a single time in a single place to shape a turning point in man's unending search for freedom. So it was at Lexington and Concord. So it was a century ago at Appomattox. So it was last week in Selma, Alabama.",
    "There, long-suffering men and women peacefully protested the denial of their rights as Americans. Many were brutally assaulted. One good man, a man of God, was killed. …",
    "Every device of which human ingenuity is capable has been used to deny this right [to vote]. The Negro* citizen may go to register only to be told that the day is wrong, or the hour is late, or the official in charge is absent. … For the fact is that the only way to pass these barriers is to show a white skin. …",
    "But even if we pass this bill, the battle will not be over. What happened in Selma is part of a far larger movement which reaches into every section and State of America. It is the effort of American Negroes to secure for themselves the full blessings of American life. Their cause must be our cause too. Because it is not just Negroes, but really it is all of us, who must overcome the crippling legacy of bigotry and injustice. And we shall overcome."],
    "Lyndon B. Johnson, president of the United States, televised speech to a joint session of Congress, Washington, D.C., March 15, 1965",
    "Adapted",
    footnotes=[{"mark": "*", "text": "\"Negro\" was a common word for African Americans in the 1960s. It is not used today."}],
    glossary=[{"t": "Lexington and Concord", "d": "the Massachusetts towns where the first battles of the American Revolution were fought in 1775"},
              {"t": "Appomattox", "d": "the Virginia town where the main Confederate army surrendered in 1865, ending the U.S. Civil War"},
              {"t": "ingenuity", "d": "cleverness"},
              {"t": "legacy", "d": "something handed down from the past"},
              {"t": "bigotry", "d": "hatred of or unfairness toward people of another race, religion, or group"}]),

"P11": {"type": "pair", "items": [
    item("Source 1", [
        "… Some say the answer is to try to just hunker down within our borders. That is clearly not an option. No country can escape the global economy, and the greatest, largest, most powerful country in the world cannot escape the global economy. We must lead it in a direction that is consistent with our values, consistent with our interests … . That's really what GATT is all about. …",
        "But no matter what we do, unless we can expand the markets for America's products and services, we will ultimately fail in our economic mission.",
        "Yes, it is true that one of the reasons for stagnant wages in the United States is intense competition in our own markets and in other markets from people who work for wages our folks couldn't live on. That will happen if there is never another trade agreement in the history of the United States. …"],
        "Bill Clinton, president of the United States, remarks at the signing of a law approving a new world trade agreement, Washington, D.C., December 8, 1994",
        "Adapted",
        glossary=[{"t": "hunker down", "d": "stay put and hide from trouble"},
                  {"t": "GATT", "d": "the General Agreement on Tariffs and Trade, a treaty among many countries, first signed in 1947, to lower taxes on trade; the law Clinton signed approved a new round of GATT agreements"},
                  {"t": "stagnant", "d": "not growing; stuck"}]),
    item("Source 2", [
        "I do not believe there is any more pressing issue regarding human rights in the world today than the exploitive and abusive use of child labor, whether it is in manufacturing, mining, textiles, rugmaking, shoes, et cetera. I have a bill pending in the Senate … which basically would cut off the importation into this country of any items that are made by child labor. …",
        "The documentation is irrefutable—millions of children 8 to 14 years of age, bonded labor, working 10 to 12 hours a day 6 to 7 days a week for mere pennies. The facts are clear that as international corporations seek low-wage workers they push down the cost of labor to the lowest level. …",
        "… We do not allow the products of prison labor to come in but we do of children. So we protect criminals but we do not protect the kids. … Again, what is happening is that so many of these products are now produced overseas."],
        "Tom Harkin, U.S. senator from Iowa, speech in the Senate during the debate on the same trade agreement, December 1, 1994",
        "From the Congressional Record, vol. 140, no. 149 (December 1, 1994); adapted",
        glossary=[{"t": "exploitive", "d": "unfairly using people for profit"},
                  {"t": "pending", "d": "waiting to be voted on"},
                  {"t": "irrefutable", "d": "impossible to prove wrong"},
                  {"t": "bonded labor", "d": "work forced on a person to pay off a debt"}])]},

"P12": P([
    "Whereas recognition of the inherent dignity and of the equal and inalienable rights of all members of the human family is the foundation of freedom, justice and peace in the world,",
    "Whereas disregard and contempt for human rights have resulted in barbarous acts which have outraged the conscience of mankind, and the advent of a world in which human beings shall enjoy freedom of speech and belief and freedom from fear and want has been proclaimed as the highest aspiration of the common people, …",
    "Now, therefore, The General Assembly, Proclaims this Universal Declaration of Human Rights as a common standard of achievement for all peoples and all nations … .",
    "Article 1. All human beings are born free and equal in dignity and rights. …",
    "Article 2. Everyone is entitled to all the rights and freedoms set forth in this Declaration, without distinction of any kind, such as race, colour, sex, language, religion, political or other opinion, national or social origin, property, birth or other status. …",
    "Article 21. … The will of the people shall be the basis of the authority of government; this will shall be expressed in periodic and genuine elections which shall be by universal and equal suffrage … .",
    "Article 26. Everyone has the right to education. Education shall be free, at least in the elementary and fundamental stages. …"],
    "Universal Declaration of Human Rights, adopted by the United Nations General Assembly, Paris, December 10, 1948",
    "Adapted",
    glossary=[{"t": "inherent", "d": "part of a person by nature; built in"},
              {"t": "inalienable", "d": "cannot be taken away"},
              {"t": "barbarous", "d": "cruel and savage"},
              {"t": "advent", "d": "arrival"},
              {"t": "aspiration", "d": "hope; goal"},
              {"t": "universal and equal suffrage", "d": "the right of all adults to vote, with each vote counting the same"}]),

"P13": P([
    "The People's Republic of China (PRC) has the world's largest number of Internet users, estimated at 500 million people. Despite government efforts to limit the flow of online news, Chinese Internet users are able to access unprecedented amounts of information, and political activists have utilized the web as a vital communications tool. In recent years, Twitter-like microblogging has surged, resulting in dramatic cases of dissident communication and public comment on sensitive political issues. However, the web has proven to be less of a democratic catalyst in China than many observers had hoped. …",
    "… Blocked websites, social networking sites, and file sharing sites include Radio Free Asia, Voice of America (Chinese language), international human rights websites, many Taiwanese news sites, Facebook, Twitter, and YouTube. … Commonly barred Internet searches and microblog postings include those with direct and indirect or disguised references to Tibet; the Tiananmen suppression of 1989; … democracy; highly charged foreign affairs issues … .",
    "… In order to maintain their business licenses and operate in China, domestic and foreign Internet companies are required to abide by a rough set of guidelines issued by central and local government agencies—and thus encouraged to practice self-censorship. Companies that have learned how to prosper in this environment include Baidu, China's largest search engine, Sina Weibo, which offers a Twitter-like microblogging platform, and Tencent, which provides instant messaging services."],
    "Congressional Research Service, an office of the Library of Congress that writes reports for members of the U.S. Congress, China, Internet Freedom, and U.S. Policy, July 13, 2012",
    "Adapted",
    glossary=[{"t": "unprecedented", "d": "never seen before"},
              {"t": "microblogging", "d": "posting short messages online for others to read and share"},
              {"t": "dissident", "d": "of people who openly oppose their government"},
              {"t": "catalyst", "d": "something that causes or speeds up a change"},
              {"t": "Radio Free Asia, Voice of America", "d": "news services paid for by the U.S. government"},
              {"t": "self-censorship", "d": "holding back or deleting one's own content to avoid punishment"}]),

"P14": P([
    "During the past few days, elements of the Chinese Army have been brutally suppressing popular and peaceful demonstrations in China. There has been widespread and continuing violence, many casualties, and many deaths. …",
    "The demonstrators in Tiananmen Square were advocating basic human rights, including the freedom of expression, freedom of the press, freedom of association. These are goals we support around the world. …",
    "… This is not the time for an emotional response, but for a reasoned, careful action that takes into account both our long-term interests and recognition of a complex internal situation in China. …",
    "… It would be a tragedy for all if China were to pull back to its pre-1972 era of isolation and repression.",
    "… I am ordering the following actions: suspension of all government-to-government sales and commercial exports of weapons, suspension of visits between U.S. and Chinese military leaders, sympathetic review of requests by Chinese students in the United States to extend their stay, and the offer of humanitarian and medical assistance through the Red Cross to those injured during the assault … .",
    "The process of democratization of Communist societies will not be a smooth one, and we must react to setbacks in a way which stimulates rather than stifles progress toward open and representative systems."],
    "George H. W. Bush, president of the United States, opening statement at a news conference, Washington, D.C., June 5, 1989",
    "Adapted",
    glossary=[{"t": "suppressing", "d": "putting down by force"},
              {"t": "casualties", "d": "people killed or injured"},
              {"t": "advocating", "d": "calling for"},
              {"t": "freedom of association", "d": "the right to form and join groups"},
              {"t": "repression", "d": "harsh control that keeps people from speaking or acting freely"},
              {"t": "stifles", "d": "smothers; holds back"}]),

"P15": P([
    "Science and technology have progressed to such a degree that communication through the use of space satellites has become possible. Through this country's leadership, this competence should be developed for global benefit at the earliest practicable time. …",
    "I again invite all nations to participate in a communication satellite system, in the interest of world peace and closer brotherhood among peoples throughout the world. …",
    "Private ownership and operation of the U.S. portion of the system is favored, provided that such ownership and operation meet the following policy requirements: … 2. Make the system global in coverage so as to provide efficient communication service throughout the whole world as soon as technically feasible, including service where individual portions of the coverage are not profitable; 3. Provide opportunities for foreign participation through ownership or otherwise, in the communications satellite system; …",
    "… In addition to its regulatory responsibilities, the U.S. Government will: … 7. Provide technical assistance to newly developing countries in order to help attain an effective global system as soon as practicable; 8. Examine with other countries the most constructive role for the United Nations … in international space communications."],
    "John F. Kennedy, president of the United States, statement on communication satellite policy, Washington, D.C., July 24, 1961",
    "Adapted",
    glossary=[{"t": "competence", "d": "ability"},
              {"t": "practicable", "d": "possible to do"},
              {"t": "technically feasible", "d": "possible with the technology available"},
              {"t": "regulatory", "d": "having to do with making and enforcing rules"}]),

"P16": P([
    "The Charter of the United Nations which you have just signed is a solid structure upon which we can build a better world. History will honor you for it. Between the victory in Europe and the final victory in Japan, in this most destructive of all wars, you have won a victory against war itself. …",
    "If we had had this Charter a few years ago—and above all, the will to use it—millions now dead would be alive. …",
    "The United Nations have also had experience, even while the fighting was still going on, in reaching economic agreements for times of peace. What was done on the subject of relief at Atlantic City, food at Hot Springs, finance at Bretton Woods, aviation at Chicago, was a fair test of what can be done by nations determined to live cooperatively in a world where they cannot live peacefully any other way. …",
    "… Experience has shown how deeply the seeds of war are planted by economic rivalry and by social injustice. … Artificial and uneconomic trade barriers should be removed—to the end that the standard of living of as many people as possible throughout the world may be raised. …",
    "Under this document we have good reason to expect the framing of an international bill of rights, acceptable to all the nations involved. … Unless we can attain those objectives for all men and women everywhere—without regard to race, language or religion—we cannot have permanent peace and security."],
    "Harry S. Truman, president of the United States, speech at the closing session of the conference that wrote the Charter of the United Nations, San Francisco, June 26, 1945",
    "Adapted",
    glossary=[{"t": "Charter", "d": "a founding document that sets out an organization's goals and rules"},
              {"t": "relief", "d": "help, such as food and medicine, for people in need"},
              {"t": "Bretton Woods", "d": "a town in New Hampshire where a 1944 conference planned new international money and banking institutions"},
              {"t": "artificial and uneconomic trade barriers", "d": "taxes and limits on trade that hurt more than they help"}]),
}

# Raw files used by the excerpt checker (not part of the bank). Paths are relative to sources/raw/.
RAWMAP = {
    "X1": ["web/gaud1968_agbioworld_wayback.html"],
    "X2": ["india_sancomm1918_b31492551.txt"],
    "X5.1": ["fbis/jprs-report_fbis-afr-90-023.txt"],
    "X5.2": ["fbis/jprs-report_fbis-afr-90-029.txt"],
    "X6": ["fbis/micro_IA1176907_0649.txt"],
    "X7": ["web/hrc_internet_freedom_2010.html"],
    "P1": ["app/address-before-the-general-assembly-the-united-nations-peaceful-uses-atomic-energy-new.html"],
    "P4": ["app/address-before-joint-session-the-congress-the-state-the-union-23.html"],
    "P5": ["app/annual-message-the-congress-the-state-the-union-2.html"],
    "P7": ["app/inaugural-address-11.html"],
    "P8": ["web/frus1977-80v13_d224.html"],
    "P10": ["app/special-message-the-congress-the-american-promise.html"],
    "P11.1": ["app/remarks-signing-the-uruguay-round-agreements-act.html"],
    "P11.2": ["crec/CREC-1994-12-01-pt1-PgS4.htm"],
    "P12": ["web/udhr_un.html"],
    "P13": ["web/crs_R42601.html"],
    "P14": ["app/the-presidents-news-conference-45.html"],
    "P15": ["app/statement-the-president-communication-satellite-policy.html"],
    "P16": ["app/address-san-francisco-the-closing-session-the-united-nations-conference.html"],
}

STIM = {k: v for k, v in STIM.items() if v is not None}
