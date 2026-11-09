# Review pass 3 (ChatGPT Pro, Nov 8, 2026; u3/chatgpt_review.txt). Applied in assemble.py AFTER the letter
# swaps, so every letter here is a FINAL letter. Dict values on options/whyNot/rationales replace single letters;
# a dict on "stimulus" updates stimulus fields; anything else replaces the field. Facts re-verified before applying
# (see SOURCES.md, "Review pass 3").

PATCH = {
 # ---- #1 P22: C was partly defensible (convergence/divergence are not tied to one scale) ----
 "U3-P22": {
   "options": {"C": "Global media are making the two cultures identical, so the local dance tradition will soon disappear."},
   "whyNot": {"C": "Fans are mixing in steps from their own traditional dance, so the local tradition is being used, not erased. Global and local influences are combining."},
   "explanation": "Streaming connects fans in Country X to a song heard around the world. The fans then mix it with a local dance. Global connections can spread a shared influence, while local communities change it in their own ways. Geographers look at both scales to see the whole story.",
   "difficulty": "medium"},

 # ---- #2 E15: give evidence for national unity; the local division comes from opposition to a minority place of worship ----
 "U3-E15": {
   "stem": "In Country N, most people follow Religion 1, and its shared national festivals strengthen a common identity across regions. In one large city, some residents oppose an immigrant community's plan to build the city's first house of worship for Religion 2. Which statement best describes religion's role in Country N at these two scales?",
   "rationales": {
     "C": "Incorrect. The shared festivals strengthen national identity. A local dispute does not show that religion has become unimportant nationally.",
     "D": "Correct. The shared festivals act as a centripetal force at the national scale. Opposition to the minority community's place of worship creates division at the local scale. A cultural factor can have different effects at different scales.",
     "E": "Incorrect. The scenario describes an immigrant community and gives no evidence that Religion 2 spread from the national capital through hierarchical diffusion."},
   "explanation": "Look at the whole country: shared festivals help people feel connected to their country. That is centripetal. Now zoom in to one city: opposition to a minority group's place of worship is causing conflict. That is centrifugal. Religion can work in different ways at different scales."},

 # ---- #3 E07: the ICAO rule was stated too broadly; test the concept with a plain scenario ----
 "U3-E07": {
   "stem": "A pilot whose first language is Portuguese and an air traffic controller whose first language is Japanese use English to communicate during an international flight. English in this interaction is best described as",
   "skill": "1.D",
   "rationales": {
     "A": "Incorrect. A creole develops in a language-contact setting and is spoken as a first language by a community. This example describes people using an existing language to communicate across language differences.",
     "E": "Incorrect. A pidgin develops for limited communication among groups without a shared language. Aviation English is a specialized use of English, not a separate pidgin language."},
   "explanation": "A lingua franca is a \"bridge\" language that people use when they do not share a first language. The pilot speaks Portuguese and the controller speaks Japanese, but both can use English. In international aviation, English often plays this role."},

 # ---- #4 P20: the indicator measures use, not access or speed ----
 "U3-P20": {
   "options": {"D": "Internet use rose in every country shown, but large gaps in use remained in 2024."},
   "explanation": "Every 2024 bar is taller than its 2005 bar. So internet use went up in every country shown and in the world. But use is still uneven. In 2024, about 95% of people in the United States used the internet. In Nigeria, about 41% did. More internet use can make it easier to share culture across long distances. But this graph does not show how fast messages travel or which cultural traits spread."},

 # ---- #5 E21-E22: age groups in two years are not the same people; no 2023 data point ----
 "U3-E21": {
   "rationales": {"E": "Correct. The share speaking Orvani at home declined in all four age groups. The largest decline was 36 percentage points among people ages 10–19, from 48 percent to 12 percent."},
   "explanation": "Compare each pair of bars. Every age group had a lower share using Orvani at home in 2025. The largest drop was among ages 10–19: 48 minus 12 equals 36 percentage points. The bars compare age groups in two different years, not the same people. They also do not show how well people speak Orvani in other settings."},
 "U3-E22": {
   "difficulty": "medium",
   "rationales": {
     "B": "Incorrect. The channel uses Orvani and can support its continued use. Using a global technology does not, by itself, show cultural convergence.",
     "C": "Incorrect. The information links moving to cities with less use of Orvani, not more, and the chart has no measurement between 1995 and 2025, so it cannot show a reversal after the channel began."},
   "explanation": "Online media can spread widely used languages like English. But they can also help people keep minority languages alive. The channel gives people new chances to use and share Orvani. It can help keep cultures different even when everyone uses the same technology. Geographers call this kind of change cultural divergence."},

 # ---- #6 P31: home-language use, not total loss of culture ----
 "U3-P31": {
   "options": {"A": "The data suggest growing linguistic assimilation alongside continued heritage traditions."},
   "whyNot": {"D": "Speaking Language F at home does not show full assimilation into Country G's culture. It shows that the heritage language is still being used."},
   "explanation": "Read down each column. Fewer people in each generation speak Language F at home. More of them speak Country G's language well. That fits linguistic assimilation, which means shifting toward the main language. But 52% of the grandchildren still celebrate the festival. So the table does not show that the heritage culture is gone."},

 # ---- #7 assimilation and multiculturalism defined less absolutely ----
 "U3-P30": {
   "options": {"D": "Acculturation means adopting some new traits; assimilation means becoming less distinct from the dominant culture."},
   "whyNot": {
     "B": "Religious blending is syncretism. Creolization can produce a new community language through long language contact. Neither one defines acculturation or assimilation.",
     "E": "Multiculturalism means several cultural groups keep their identities within one shared society. It does not require them to stay fully separate."},
   "explanation": "Acculturation means picking up some new traits from another culture while keeping parts of your own. Assimilation means becoming more like the main culture around you. People who assimilate often use some of their old traditions less. These changes can be uneven. A family may switch languages but keep its holiday traditions."},
 "U3-P10": {
   "skill": "1.D",
   "whyNot": {
     "B": "Assimilation means adopting a dominant culture and becoming less culturally distinct. These murals instead celebrate the community's Mexican American heritage.",
     "D": "The stem does not describe an imported art idea being changed. It describes residents giving a public space meaning through their own history and culture."}},
 "U3-P14": {
   "whyNot": {
     "C": "Contagious diffusion describes spread through contact among people or nearby places. The key evidence here is that the restaurant model changes to fit local religious practices.",
     "E": "Assimilation would mean the local population adopting the incoming culture and becoming less distinct. Here the restaurant changes its menu to fit local beliefs."}},
 "U3-P32": {
   "whyNot": {
     "B": "Assimilation means adopting a dominant culture. This example describes two traditions combining into one celebration.",
     "C": "Multiculturalism recognizes several cultural groups and their identities. This question is about traditions blending together, which is syncretism."}},
 "U3-E06": {
   "rationales": {
     "B": "Incorrect. The example emphasizes how an idea was adapted, rather than the movement of people who carried a trait.",
     "C": "Incorrect. Person-to-person spread alone does not describe the central feature here: adapting the idea of writing into a different writing system.",
     "E": "Incorrect. The syllabary supported the use of the Cherokee language rather than its replacement by English."}},
 "U3-E14": {
   "options": {"B": "a centrifugal force weakening national political unity"},
   "rationales": {
     "A": "Incorrect. The festivals and language programs support a distinctive regional culture rather than its replacement by the dominant culture.",
     "B": "Incorrect. Celebrating a regional culture does not by itself weaken national unity; nothing in the stem describes a movement for separation or self-rule."}},

 # ---- #8 religious categories as tendencies, not absolute rules ----
 "U3-P28": {
   "whyNot": {"E": "Staying near the hearth does not explain spread across many cultures. Some ethnic religions have communities far from their hearths, and some universalizing religions stay mostly in one region."},
   "explanation": "Universalizing religions teach that their message is open to people of any background. Winning new believers helps them spread to many cultures. Migration and trade help too. Ethnic religions usually have strong ties to one people, history, and place. They may still accept converts and spread when their followers move."},
 "U3-P24": {
   "stimulus": {
     "title": "HEARTHS, RELIGION TYPES, AND DISTRIBUTION OF FOLLOWERS, 2010",
     "columns": ["Religion", "Hearth", "Type", "Where most followers lived in 2010"],
     "rows": [
       ["Buddhism", "South Asia (northeastern India and southern Nepal)", "Universalizing", "East and Southeast Asia"],
       ["Christianity", "Southwest Asia (the Levant, along the eastern Mediterranean)", "Universalizing", "Every inhabited continent, especially the Americas, Europe, and Africa south of the Sahara"],
       ["Hinduism", "South Asia (northern Indian subcontinent)", "Ethnic", "India and Nepal"],
       ["Islam", "Southwest Asia (Mecca and Medina, Arabian Peninsula)", "Universalizing", "Asia and Africa, from Southeast and South Asia to Southwest Asia and North Africa, and Africa south of the Sahara"],
       ["Judaism", "Southwest Asia (the Levant, along the eastern Mediterranean)", "Ethnic", "Mainly Israel and the United States"]],
     "description": "A table listing five religions, their hearth regions, their classification as universalizing or ethnic, and the main regions where their followers lived in 2010.",
     "source": "Where followers lived in 2010: Pew Research Center, \"The Global Religious Landscape\" (2012). Hearths: Encyclopaedia Britannica articles on each religion. Types: College Board AP Human Geography course guide."},
   "explanation": "Hinduism began in South Asia, and most Hindus in the table live in India and Nepal. So it is the clearest match for an ethnic religion that is still found mostly near its hearth. This is a tendency, not a rule: migration has also created Hindu and Jewish communities far from their hearths."},
 "U3-E16": {
   "explanation": "Religion P does not seek converts, 94% of its followers live in its hearth region, and it reaches the table's 1-million-follower mark in only one region. Together, these facts best fit an ethnic religion that has stayed near its hearth. That does not mean it has no communities anywhere else."},
 "U3-E17": {
   "stem": "Based on Religion R's distribution and its approach to seeking converts, which process most plausibly accounts for its presence outside its hearth region?",
   "rationales": {
     "A": "Incorrect. The table provides no evidence that rulers adopted the religion before their subjects. Migration of existing followers is more consistent with the pattern described.",
     "B": "Incorrect. The table does not describe conversion spreading from neighbor to neighbor. Communities outside the hearth can instead result from followers migrating."}},
 "U3-E20": {
   "explanation": "Buddhism is a universalizing religion. Monks, traders, and rulers carried it from South Asia along trade routes, and many people converted. Hinduism is an ethnic religion, and most Hindus still live in South Asia. Hindu traditions did spread long ago to parts of Southeast Asia, and Hindu communities now live around the world."},

 # ---- #9 creolization described accurately ----
 "U3-E09": {
   "stem": "Haitian Creole developed in the 1600s and 1700s in the French colony of Saint-Domingue (present-day Haiti), among French colonists and enslaved Africans who spoke many different African languages. Much of its vocabulary comes from French, but it has its own grammar. Today it is the first language of most Haitians. The development of Haitian Creole best illustrates",
   "rationales": {
     "A": "Incorrect. The passage describes the emergence of Haitian Creole. It does not establish that another language became extinct.",
     "B": "Correct. Contact among French-speaking colonists and enslaved speakers of different African languages contributed to the emergence of a new language. This is an example of creolization in a colonial setting."},
   "explanation": "Haitian Creole grew out of contact among people who spoke different languages under French colonial rule. It developed its own patterns and rules, and children learned it as their first language. That is creolization."},
 "U3-P17": {
   "stem": "Tok Pisin began in the 1800s as a pidgin, a contact language used on plantations among workers who did not share a first language; much of its vocabulary comes from English. Today it is one of the main languages of Papua New Guinea, and many children grow up speaking it as their first language. This change is best described as",
   "difficulty": "easy",
   "whyNot": {"A": "The language did not disappear. Tok Pisin is still widely used, including as a first language."},
   "explanation": "A pidgin develops so that people who do not share a first language can communicate. One path to a creole is when a contact language becomes the first language of a community and is used in everyday life. That is what happened with Tok Pisin."},
 "U3-P16": {
   "stimulus": {"source": "Wikipedia articles \"Swahili language,\" \"Haitian Creole,\" \"Languages of Senegal,\" \"Languages of Ivory Coast,\" \"Languages of Gabon,\" and \"Basque language\" (accessed November 8, 2026)"},
   "whyNot": {
     "A": "Creolization is the development of a new community language through long language contact. Haitian Creole is an example.",
     "C": "A language isolate has no demonstrated relationship to any other living language. Basque is an example.",
     "D": "A dialect is a regional or social variety of one language, with differences in pronunciation, vocabulary, or grammar."},
   "explanation": "A lingua franca is a language people use to communicate when they have different first languages. Swahili spread through trade and other contact. Today, many people in East Africa use it to communicate across language groups in trade, school, and public life."},
 "U3-P21": {
   "whyNot": {
     "A": "The goal is to keep Icelandic vocabulary Icelandic, not to create a shared trade language for other Nordic countries.",
     "D": "Borrowing or combining words does not by itself create a creole. This example describes making new words inside Icelandic."}},

 # ---- #10 diffusion types are not mutually exclusive; missing evidence is not evidence of absence ----
 "U3-E03": {
   "stem": "The order of adoption shown on the map is most consistent with which type of diffusion?",
   "skill": "3.E",
   "options": {"A": "Contagious diffusion", "B": "Relocation diffusion", "C": "Stimulus diffusion", "D": "Hierarchical diffusion", "E": "Reverse hierarchical diffusion"},
   "rationales": {
     "B": "Incorrect. The map does not show migration. Its clearest pattern is that larger cities adopted the style before smaller places.",
     "D": "Correct. Distant large cities adopted the style before nearby small towns. This sequence fits diffusion down an urban hierarchy better than a spread organized mainly by distance."}},
 "U3-E04": {
   "stem": "Which explanation best accounts for Fenn's adoption date compared with those of Benn and Cora?",
   "rationales": {"B": "Incorrect. The map contains no migration history, so this explanation is not supported by the evidence provided."}},
 "U3-P12": {
   "whyNot": {"A": "Contagious diffusion is spread through contact among people or nearby places. The arrow specifically shows migrants moving and settling across the sea."},
   "explanation": "Relocation diffusion happens when people move and bring their culture with them. The arrow shows merchants who moved from Land A, settled in the port town on Land B, and built a place of worship. Later, other residents may have adopted the religion in other ways, but the move shown by the arrow is relocation diffusion."},
 "U3-P13": {
   "whyNot": {"C": "Adoption follows distance from Ora, not a move from smaller places up to larger ones. Starting in a small village does not by itself make it reverse hierarchical diffusion."}},
 "U3-P15": {
   "stem": "A new style of clothing first became popular among teenagers in several small towns in rural Country P. About two years later it appeared in mid-sized cities, and only after that did stores in the country's largest city, which is also the national capital, begin selling it. This pattern is best described as",
   "whyNot": {
     "C": "The stem gives no evidence that migration carried the style. The evidence is the order of adoption by settlement size.",
     "E": "The stem gives no evidence that communities changed the style as they adopted it."}},

 # ---- #11 E05: make the technology change explicit ----
 "U3-E05": {
   "stem": "Assume that use of streaming services and social media became much more widespread throughout Country R after 2016. If another music style first appeared in Arlo in 2024, its spread, compared with the pattern on the map, would most likely be",
   "difficulty": "medium",
   "explanation": "When almost everyone can stream music, people in small towns can hear a new style at nearly the same time as people in big cities. That can shrink the delays caused by distance and city size. (Hearing a style does not guarantee that people will adopt it.) This is time-space convergence at work."},

 # ---- #13 stems should not restate the evidence ----
 "U3-E11": {
   "stem": "Which statement best explains how the community living on the block shaped its cultural landscape between 1975 and 2005?",
   "skill": "4.E",
   "rationales": {"A": "Correct. Residents established a religious institution, restaurants, and signs that reflected their cultural background and served the local community. These features show how ethnicity can shape the use and appearance of space."}},

 # ---- #14 political effects of language and religion stated conditionally ----
 "U3-P09": {
   "skill": "2.C",
   "options": {
     "A": "Region 2 may favor independence because it does not contain the national capital.",
     "B": "The mountain border may make Language A easier to adopt in Region 3.",
     "C": "Using just Language A in public institutions may strengthen Region 3's shared identity with Region 1.",
     "D": "Excluding Language B from public institutions may strengthen demands for self-rule in Region 3.",
     "E": "Language B may replace Language A as the main language of communication in Regions 1 and 2."},
   "whyNot": {
     "B": "Mountains can make movement and contact harder. The map gives no evidence that this range speeds the spread of Language A.",
     "C": "Leaving Language B out of schools, courts, and TV gives a reason for possible tension, not evidence that the policy builds unity.",
     "E": "The map gives no evidence that Language B is spreading into Regions 1 and 2 or becoming their shared language."},
   "explanation": "A centrifugal force creates pressure that can weaken a country's unity. Most people in Region 3 speak Language B, but schools, courts, and TV use only Language A. Some residents may feel their language is left out and may push for more regional control. The mountains may limit contact, but the map does not show that Region 3 is completely cut off."},
 "U3-P08": {
   "whyNot": {"A": "In this example, shared use of Swahili supports communication and national identity. That is a centripetal role."},
   "explanation": "A centripetal force pulls the people of a country together. More than 100 languages are spoken in Tanzania. The government promoted Swahili as one shared language for public life. It helped people from different language groups talk to each other and feel part of one nation. Language can also be a centrifugal force when it divides people, as in a country split into language regions."},
 "U3-P11": {
   "stem": "In Nigeria, Islam is the main religion in much of the north, while Christianity is the main religion in much of the south. Which of the following best explains how this pattern could act as a centrifugal force at the national scale?",
   "difficulty": "medium",
   "options": {"B": "Regional religious identities may become stronger than identification with the country as a whole."},
   "whyNot": {"D": "Religious diversity does not by itself make countries break apart. Political exclusion, unequal power, and regional divisions affect whether religious differences become divisive."}},

 # ---- #15 P02: Student 4 now clearly uses home culture as the standard; Student 2 avoids a climate explanation ----
 "U3-P02": {
   "stimulus": {"rows": [
      ["Student 1", "People here eat dinner at 10 p.m. That is just wrong. Dinner should be at 6, like it is at home."],
      ["Student 2", "My host family explained how work schedules and family traditions shape their late dinners. I tried to understand the custom in that setting instead of judging it by our dinner time at home."],
      ["Student 3", "So many restaurants here look like the chains back home. Maybe every place is becoming the same."],
      ["Student 4", "Meals should be prepared the way they are at home. Because the local food does not follow our way of cooking, I refused to try it."],
      ["Student 5", "I wrote down the prices of meals here so I can compare them with prices back home."]]},
   "whyNot": {"D": "Student 4 treats the home culture's way of cooking as the correct standard for judging another culture. That is ethnocentrism."},
   "explanation": "Cultural relativism means trying to understand a custom in its own setting. You do not judge it by your own culture's rules. Student 2 learned how work and family traditions shape the late dinners. Then Student 2 tried to understand the custom on those terms. Students 1 and 4 do the opposite. They judge the other culture by home rules. That is ethnocentrism."},

 # ---- #16 P25 feedback limits ----
 "U3-P25": {
   "whyNot": {
     "B": "The two Spanish names shown are in south-central and far western Texas. Five examples cannot show where most Spanish place names are.",
     "E": "The table gives Indigenous, Spanish, and German naming histories. It does not support a claim about most Texas place names or show contagious diffusion of English."}},

 # ---- #17 historical overclaims ----
 "U3-P26": {
   "stem": "Which pairing correctly describes one of the hypotheses proposed for the early spread of the Indo-European language family?",
   "difficulty": "medium",
   "explanation": "Indo-European is the language family with the most speakers today. It includes English, Spanish, Hindi, and Russian. Two well-known ideas link its early spread to people moving. The Anatolian hypothesis ties it to farming, which spread out of Anatolia (in today's Türkiye). The steppe, or Kurgan, hypothesis ties a later spread to herders from the grasslands north of the Black and Caspian Seas. Researchers keep testing both ideas."},
 "U3-P27": {
   "whyNot": {
     "A": "Spread from nearby mainland communities would not explain why Malagasy's closest relatives are languages of Borneo.",
     "C": "Changes in writing do not move a language into a different language family."},
   "explanation": "Relocation diffusion happens when people move and carry their culture to a new place. Malagasy's closest relatives are spoken on Borneo. That points to people who sailed across the Indian Ocean many centuries ago. They brought their language to Madagascar. There it kept changing through contact with other languages."},
 "U3-P29": {
   "skill": "2.B",
   "explanation": "Families from Punjab moved to these cities. They built gurdwaras and kept practicing their faith. When people carry their religion to a new place by moving there, that is relocation diffusion. A universalizing religion like Sikhism can spread by people moving, not only by people converting."},

 # ---- #18 smaller corrections ----
 "U3-P07": {
   "options": {"D": "More new housing located far from both employment centers and public transportation"},
   "whyNot": {
     "C": "More people in paid jobs does not mean fewer adults commute. Commuting needs also depend on where jobs are and how people travel.",
     "D": "Nothing in the trend gives a reason for new housing to be farther from jobs and transit."},
   "explanation": "Changes in gender roles can affect how communities use space. When more parents and caregivers work outside the home, families need childcare close to where they live, work, and travel. So childcare centers near homes, workplaces, and transit are the most likely change among these choices."},
 "U3-P23": {
   "explanation": "When schools, jobs, and online media mostly use the national language or English, young people have fewer chances to use their home language. If they do not pass it on to their children, it may become endangered. Families and community programs can also work to keep it alive."},
 "U3-P19": {"difficulty": "medium"},

 # ---- #19 E08: Timor-Leste restored Portuguese after Indonesian occupation; replace climate distractor ----
 "U3-E08": {
   "options": {
     "B": "The four countries joined an international organization that made Portuguese their shared official language.",
     "D": "Large numbers of Portuguese workers moved to these countries during the last 20 years.",
     "E": "Portugal colonized these places, and each kept or restored Portuguese as an official language."},
   "rationales": {
     "B": "Incorrect. The Community of Portuguese Language Countries, founded in 1996, brought together countries that already used Portuguese; the shared language came first, from colonial rule.",
     "E": "Correct. Portuguese colonial rule spread the language through administration, education, religion, and trade. After independence, these states kept Portuguese as an official language or, in Timor-Leste's case, restored it after a period of Indonesian occupation."},
   "explanation": "These countries are far apart, but all were once ruled by Portugal. That history shaped their later choices of official language. Today Portuguese is official in all four, alongside Tetum in Timor-Leste."},

 # ---- #20 E12, E25: remove echo/paraphrase keys ----
 "U3-E12": {
   "stem": "For several generations, residents of a hot, dry region have built houses with thick walls made from local earth, small windows, and flat roofs. Which explanation best accounts for this combination of features?",
   "options": {
     "A": "Builders copied a colonial power's designs to show loyalty to its rulers.",
     "B": "Builders adapted local materials and building designs to the local climate.",
     "C": "Builders mixed decorative details from several past styles to create something new.",
     "D": "Builders used standard designs promoted by international construction companies.",
     "E": "Builders reused buildings left by earlier groups but gave them new cultural uses."},
   "rationales": {
     "A": "Incorrect. The account gives evidence of local materials and environmental conditions, but none of colonial rule or imported designs.",
     "B": "Correct. Traditional architecture adapts to local conditions. Earthen walls slow the movement of heat, small windows limit the sun's heat, and flat roofs are practical where little rain falls.",
     "C": "Incorrect. Mixing details from past styles describes postmodern architecture; the account emphasizes materials and climate, not style.",
     "D": "Incorrect. The account gives no evidence of international companies or standardized global designs.",
     "E": "Incorrect. The account describes a continuing building tradition, not later groups reusing earlier groups' buildings."},
   "explanation": "People in hot, dry places have long built with what is nearby and designed homes to fit the weather. Thick earth walls slow the heat, small windows block the sun, and flat roofs work because it rarely rains. Geographers call this traditional architecture: building styles adapted to local materials and climate."},
 "U3-E25": {
   "stem": "In 1971, Canada adopted an official national policy of multiculturalism. The policy supports the freedom of immigrants and other groups to keep their languages, religions, and traditions while taking part in Canadian society. Which change in the cultural landscape would this policy most likely encourage?",
   "options": {
     "A": "Signs in heritage languages disappearing from immigrant neighborhoods within a generation",
     "B": "Neighborhoods losing their distinct ethnic businesses, places of worship, and festivals",
     "C": "New houses of worship that blend the country's religions into one shared faith",
     "D": "Cultural centers and festivals of many groups staying visible in shared public spaces",
     "E": "Identical shopping malls and chain stores replacing regional and ethnic differences"},
   "rationales": {
     "A": "Incorrect. Heritage-language signs disappearing would point toward assimilation; the policy supports groups that want to keep their languages.",
     "B": "Incorrect. The policy supports keeping traditions, so it would encourage, not erase, distinct businesses, places of worship, and festivals.",
     "C": "Incorrect. Blending religions into one faith describes syncretism; the policy supports groups' freedom to keep their own religions.",
     "D": "Correct. Multiculturalism supports many cultural groups keeping their traditions within one society, so the landscape would keep showing distinct cultural centers and festivals alongside shared public spaces and institutions.",
     "E": "Incorrect. Look-alike chain landscapes reflect placelessness and cultural convergence, not a policy that supports cultural distinctiveness."},
   "explanation": "Multiculturalism supports people's freedom to keep their traditions while taking part in one shared society. On the landscape, you would see cultural centers, places of worship, and festivals of many groups. You would also see schools, parks, and other public places that everyone shares."},
}

# ---- #12 E18: the old item could be answered from the definition alone; new item uses the table (key stays C) ----
REPLACE = {
 "U3-E18": dict(
   stem="Which of the following comparisons CANNOT be made using the data in the table?",
   difficulty="medium", skill="3.F",
   options={
     "A": "Whether Religion P or Religion R has a higher share of followers living in its hearth region",
     "B": "Whether Religion Q or Religion S reaches the 1-million-follower threshold in more world regions",
     "C": "Whether Religion Q or Religion S has more followers worldwide",
     "D": "Whether Religion Q or Religion T has a higher share of followers living outside its hearth region",
     "E": "Whether Religion P and Religion R differ in whether they seek converts"},
   answer="C",
   rationales={
     "A": "Incorrect. The table gives 94 percent for Religion P and 45 percent for Religion R.",
     "B": "Incorrect. Religion Q reaches the threshold in six regions, compared with five for Religion S.",
     "C": "Correct. Counts of regions above a threshold do not give total followers. Each region can have far more than 1 million followers, and smaller groups may live elsewhere.",
     "D": "Incorrect. Subtracting from 100 gives 79 percent outside Religion Q's hearth region and 30 percent outside Religion T's.",
     "E": "Incorrect. The table states that neither Religion P nor Religion R seeks converts."},
   explanation="The table tells how many regions have at least 1 million followers. It does not tell the total number of followers. One religion could have a few huge communities. Another could have more communities that are just over 1 million. You can read or work out every other comparison from the table."),
}

CALIBRATION = "Original AP-style Unit 3 practice, built on the College Board AP Human Geography Course and Exam Description (Fall 2020, current). The 25-question exam uses five answer choices and the AP multiple-choice pace of about one minute per question, with individual and stimulus-set questions. Difficulty labels are editorial estimates; difficulty and score interpretations have not been equated to an official AP Exam. All questions and stimuli are original or compiled from cited public sources; no College Board items are reproduced."
