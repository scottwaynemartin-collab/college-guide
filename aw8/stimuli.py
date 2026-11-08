# AP World Unit 8 sources. Texts follow the editions saved in aw8/sources/raw/ and documented in
# aw8/sources/*.md. Cuts are marked with ellipses; bracketed words are clarifications.
# Copyright rule for this unit: every text is a work of the U.S. government (speeches and papers of
# U.S. officials, State Department and CIA documents printed in Foreign Relations of the United States
# (FRUS), U.S. government translations of foreign documents, the Pentagon Papers, the 9/11 Commission
# Report, U.S. Census and CIA statistics) or was published by 1930. Images are U.S. Air Force photographs.
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
    "The very existence of the Greek state is today threatened by the terrorist activities of several thousand armed men, led by Communists, who defy the government's authority at a number of points, particularly along the northern boundaries. …",
    "The British Government, which has been helping Greece, can give no further financial or economic aid after March 31. Great Britain finds itself under the necessity of reducing or liquidating its commitments in several parts of the world, including Greece. …",
    "At the present moment in world history nearly every nation must choose between alternative ways of life. The choice is too often not a free one.",
    "One way of life is based upon the will of the majority, and is distinguished by free institutions, representative government, free elections, guarantees of individual liberty, freedom of speech and religion, and freedom from political oppression.",
    "The second way of life is based upon the will of a minority forcibly imposed upon the majority. It relies upon terror and oppression, a controlled press and radio; fixed elections, and the suppression of personal freedoms.",
    "I believe that it must be the policy of the United States to support free peoples who are resisting attempted subjugation by armed minorities or by outside pressures. … I believe that our help should be primarily through economic and financial aid which is essential to economic stability and orderly political processes. …",
    "I therefore ask the Congress to provide authority for assistance to Greece and Turkey in the amount of $400,000,000 for the period ending June 30, 1948."],
    "Harry S. Truman, president of the United States, address to a joint session of the U.S. Congress, March 12, 1947",
    "Adapted",
    glossary=[{"t": "liquidating", "d": "ending; getting rid of"},
              {"t": "commitments", "d": "promises of help and duties a country has taken on"},
              {"t": "institutions", "d": "organized parts of a society, such as courts, parliaments, and newspapers"},
              {"t": "subjugation", "d": "being brought under someone else's control"}]),

"X2": {"type": "pair", "items": [
    item("Source 1", [
        "I understand your concern for the security of the United States, Mr. President, because this is the primary duty of a President. But we too are disturbed about these same questions; I bear these same obligations as Chairman of the Council of Ministers of the U.S.S.R. You have been alarmed by the fact that we have aided Cuba with weapons, in order to strengthen its defense capability—precisely defense capability—because whatever weapons it may possess, Cuba cannot be equated with you since the difference in magnitude is so great, particularly in view of modern means of destruction. Our aim has been and is to help Cuba, and no one can dispute the humanity of our motives, which are oriented toward enabling Cuba to live peacefully and develop in the way its people desire.",
        "You wish to ensure the security of your country, and this is understandable. But Cuba, too, wants the same thing; all countries want to maintain their security. But how are we, the Soviet Union, our Government, to assess your actions which are expressed in the fact that you have surrounded the Soviet Union with military bases; surrounded our allies with military bases; placed military bases literally around our country; and stationed your missile armaments there? … Your missiles are located in Britain, are located in Italy, and are aimed against us. Your missiles are located in Turkey.",
        "You are disturbed over Cuba. You say that this disturbs you because it is 90 miles by sea from the coast of the United States of America. But Turkey adjoins us; our sentries patrol back and forth and see each other. … I therefore make this proposal: We are willing to remove from Cuba the means which you regard as offensive. We are willing to carry this out and to make this pledge in the United Nations. Your representatives will make a declaration to the effect that the United States, for its part, considering the uneasiness and anxiety of the Soviet State, will remove its analogous means from Turkey. …"],
        "Letter from Nikita Khrushchev, leader of the Soviet Union, to President John F. Kennedy of the United States, Moscow, October 27, 1962. The letter was also broadcast on Moscow radio.",
        "Official translation prepared by the U.S. Department of State, printed in Foreign Relations of the United States, 1961–1963, vol. VI (Washington, D.C., 1996); adapted",
        glossary=[{"t": "Chairman of the Council of Ministers", "d": "head of the Soviet government"},
                  {"t": "equated with", "d": "treated as equal to"},
                  {"t": "magnitude", "d": "size"},
                  {"t": "adjoins", "d": "is next to; borders"},
                  {"t": "analogous means", "d": "similar weapons"}]),
    item("Source 2", [
        "I have read your letter of October 26th with great care and welcomed the statement of your desire to seek a prompt solution to the problem. The first thing that needs to be done, however, is for work to cease on offensive missile bases in Cuba and for all weapons systems in Cuba capable of offensive use to be rendered inoperable, under effective United Nations arrangements. …",
        "As I read your letter, the key elements of your proposals—which seem generally acceptable as I understand them—are as follows: 1) You would agree to remove these weapons systems from Cuba under appropriate United Nations observation and supervision; and undertake, with suitable safeguards, to halt the further introduction of such weapons systems into Cuba. 2) We, on our part, would agree … (a) to remove promptly the quarantine measures now in effect and (b) to give assurances against an invasion of Cuba. …",
        "But the first ingredient, let me emphasize, is the cessation of work on missile sites in Cuba and measures to render such weapons inoperable, under effective international guarantees. The continuation of this threat, or a prolonging of this discussion concerning Cuba by linking these problems to the broader questions of European and world security, would surely lead to an intensification of the Cuban crisis and a grave risk to the peace of the world."],
        "Letter from President John F. Kennedy to Nikita Khrushchev, Washington, D.C., October 27, 1962, answering an earlier private letter from Khrushchev dated October 26. The White House released the letter to the press.",
        "Printed in Foreign Relations of the United States, 1961–1963, vol. VI (Washington, D.C., 1996); adapted",
        glossary=[{"t": "rendered inoperable", "d": "made unable to work"},
                  {"t": "quarantine measures", "d": "the U.S. Navy's blockade that stopped ships carrying weapons to Cuba"},
                  {"t": "assurances", "d": "promises"},
                  {"t": "cessation", "d": "stopping"}])]},

"X3": {"type": "image",
    "src": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/C-47s_at_Tempelhof_Airport_Berlin_1948.jpg/960px-C-47s_at_Tempelhof_Airport_Berlin_1948.jpg",
    "width": 960, "height": 767,
    "alt": "A black-and-white photograph of a row of twin-engine propeller cargo planes with star markings on a wide airfield, with trucks loaded with crates backed up to their doors and a long airport building behind.",
    "caption": "Twin-engine cargo planes with U.S. star markings are parked in a row on a wide airfield. Trucks piled with wooden crates are backed up to the open doors of the nearest planes. A very long airport building stands in the background.",
    "attribution": "U.S. Air Force photograph of American cargo planes being unloaded at Tempelhof Airport, in the American sector of Berlin, Germany, 1948–1949",
    "credit": "Public domain image (U.S. Air Force photograph) via Wikimedia Commons.",
    "description": "A black-and-white photograph taken from a high point. In the lower right, a twin-engine propeller cargo plane with a white star on its wing and the number 52 on its nose has its side door open; a truck loaded with wooden crates is backed up to it, and a worker stands in the doorway. Five more planes of the same kind are parked in a diagonal row behind it, with another loaded truck beside one of them. Small groups of people stand at the left. The wide paved airfield stretches to a very long, low airport building with hangar openings across the back of the picture.",
    "glossary": [{"t": "sector", "d": "one of the four zones of Berlin run by the United States, Britain, France, and the Soviet Union after World War II"}]},

"X4": {"type": "bar",
    "title": "Average Yearly Growth of the Economy, Soviet Union, Eastern Europe, and United States, 1961–1985",
    "categories": ["1961–65", "1966–70", "1971–75", "1976–80", "1981–85"],
    "series": [{"name": "Soviet Union", "values": [4.9, 5.1, 3.1, 2.2, 1.8]},
               {"name": "Eastern Europe", "values": [3.9, 3.8, 4.9, 1.9, 1.2]},
               {"name": "United States", "values": [4.8, 2.8, 2.3, 3.3, 3.0]}],
    "yLabel": "Average growth per year (percent)",
    "text": "Each bar shows how fast a country's total output of goods and services grew per year, on average, over five years, after rising prices are taken into account. The figures are estimates made by the U.S. Central Intelligence Agency (CIA). For the Soviet Union and Eastern Europe the CIA measured gross national product (GNP); for the United States it measured gross domestic product (GDP), a very similar measure. \"Eastern Europe\" means Bulgaria, Czechoslovakia, East Germany, Hungary, Poland, and Romania taken together.",
    "source": "U.S. Central Intelligence Agency, Directorate of Intelligence, Handbook of Economic Statistics, 1988 (Washington, D.C., 1988), Table 9"},

"X5": P([
    "In August 1945, the Japanese surrendered to the Allies. The popular forces of Vietnam which, since 1940, had made incessant attacks on the Japanese forces, … went down to conquer the capital-city and the governing rule. … On September 2, 1945, the Democratic Republic of Vietnam was solemnly proclaimed. … The new Republic of Vietnam, thus legally instituted, is in the reconstruction of the world a factor of peace and progress. She is entitled for her safeguard to refer to the most sacred principles of SAN FRANCISCO and ATLANTIC Charters*. She is based on and draws her strength from, the first of SUN YAT SEN's Three Principles and the second, fourth, sixth points of President TRUMAN's twelve-point declaration.",
    "But, on September 23, 1945, the French troops attacked Saigon, starting an invasion which is now in its fifth month. That invasion is menacing North Vietnam … . That aggression, carried on by an experienced and numerous army, fully equipped with the most recent inventions of modern warfare, has brought about the destruction of our towns and villages, the assassination of our civilian population, the starving of a great part of our country. …",
    "First of all, democracy has been established on solid foundations. On January 6 last, general elections were organized with the greatest success. … A new administrative organization has replaced the old mandarinate system. The most unpopular taxes have been abolished. The anti-illiteracy campaign organized along efficient lines, has yielded unexpectedly optimistic results. …",
    "For those reasons, we think it our duty to send this note to the Great Powers—which had led the anti-fascist crusade to final victory … . While waiting with confidence for a positive measure from the Governments of WASHINGTON, MOSCOW, LONDON, and CHUNGKING, we have determined to fight to our last drop of blood against the reestablishment of French imperialism. … We only ask full independence, independence that is so far a fact, and that will enable us to cooperate with the other nations in the building-up of a better world and lasting peace."],
    "Note from the Ministry of Foreign Affairs of the Democratic Republic of Vietnam, the government led by Ho Chi Minh, to the governments of China, the United States, the Soviet Union, and Great Britain, Hanoi, February 18, 1946. Ho Chi Minh handed copies to an American official in Hanoi.",
    "English text as printed in United States–Vietnam Relations, 1945–1967 (the \"Pentagon Papers\"), Part I (Washington, D.C.: U.S. Government Printing Office, 1971); adapted",
    footnotes=[{"mark": "*", "text": "The United Nations Charter, signed at San Francisco in 1945, and the Atlantic Charter of 1941. The \"twelve-point declaration\" was a 1945 speech in which Truman listed twelve aims of American foreign policy."}],
    glossary=[{"t": "incessant", "d": "never stopping"},
              {"t": "solemnly proclaimed", "d": "formally announced"},
              {"t": "instituted", "d": "set up"},
              {"t": "Sun Yat Sen's Three Principles", "d": "nationalism, democracy, and the people's livelihood: the ideas of Sun Yat-sen, founder of the Republic of China"},
              {"t": "mandarinate system", "d": "government by appointed officials called mandarins"},
              {"t": "Chungking", "d": "Chongqing, the wartime capital of China's Nationalist government"}]),

"X6": P([
    "After one year's effort, a great leap forward situation has unfolded. Is this something temporary? Will there be a leap forward every year for the next several years? With a nation like ours, large population, vast area, and resources, and the Soviet Union's experience, it is possible. … I am inclined toward leaping forward.",
    "… When discussing the defects of last year, some people dwell on the defects. With dozens of defects in their mind, they fail to see any achievement at all. It is the question of nine fingers and one finger. … Several hundred millions of laboring people and several millions or tens of millions of cadres cannot be doing only bad things. This I believe. …",
    "… Is agriculture actually placed on a solid foundation? X X* catties of grain, X X piculs of cotton, hemp, oil, large cattle, small domestic fowl—are their quota on a solid foundation? Or are they exaggerations? Can they be fulfilled? One must not resort to false reporting in order to get through. … I am concerned over fertilizers this year. Dropsy in humans is due to lack of meat and vegetables. When the crops get no fertilizer, they also suffer from dropsy. …"],
    "Mao Zedong, chairman of the Chinese Communist Party, speech at a conference of the party's leaders of China's provinces and large cities, February 2, 1959. The speech was not published at the time; it was printed in a collection of Mao's talks during the Cultural Revolution in the late 1960s.",
    "Translated by the U.S. Joint Publications Research Service, Miscellany of Mao Tse-tung Thought (1949–1968), Part I (Arlington, Va., 1974); adapted",
    footnotes=[{"mark": "*", "text": "The Chinese collection printed \"X X\" in place of the figures."}],
    glossary=[{"t": "defects", "d": "faults; mistakes"},
              {"t": "cadres", "d": "Communist Party officials and activists"},
              {"t": "catties, piculs", "d": "Chinese units of weight"},
              {"t": "quota", "d": "an amount that is required to be produced"},
              {"t": "dropsy", "d": "a swelling of the body caused by fluid building up"}]),

"X7": P([
    "[Nkrumah] said that his main preoccupation, now that Ghana is about to attain political independence, is to assure the country's economic independence. History has shown that political and economic independence must proceed pari passu and that the former cannot be effective without the latter. He pointed out that Ghana's economy is primarily agricultural and heavily dependent on cocoa. This means that the health of its economy is directly related to the price of cocoa which has fluctuated widely. … The Prime Minister said that he was concerned about the unhealthy situation created by such heavy reliance on one crop and was therefore anxious to diversify the economy both by general agricultural development and by exploiting the country's mineral resources—particularly bauxite. …",
    "Reverting to the Volta River Project*, he said that the Preparatory Commission's report had shown the project to be eminently sound from an engineering point of view. Unfortunately, however, there is the matter of financing. … This project, he felt, would go far towards realizing Ghana's goal of economic independence. …",
    "Dr. Nkrumah went on to say that Ghana has been aware of the desirability of attracting private investment. While the Government believes that certain economic facilities should properly be state-owned, it nevertheless has taken steps to encourage private investment through measures for tax relief, land tenure, etc. …",
    "The Vice President said that he had read and heard much about the foreign policy which Ghana would follow after independence. He asked whether he would be correct in describing Ghana's policy as \"nationalist\". He said he disliked the term \"neutralist\" … . The Prime Minister said that the Vice President had accurately expressed Ghana's position. Ghana's policy, he said, will be one of non-involvement and non-alignment in the East-West struggle. \"But\", he said, \"Ghana can never be neutral\". It will jealously safeguard its independence and resist all efforts at domination."],
    "Memorandum of a conversation between Kwame Nkrumah, prime minister of Ghana, and Richard Nixon, vice president of the United States, Accra, Ghana, March 4, 1957, prepared by the U.S. side and attached to Nixon's report to President Eisenhower. Ghana, formerly the British colony of the Gold Coast, became independent two days later.",
    "Printed in Foreign Relations of the United States, 1955–1957, vol. XVIII (Washington, D.C., 1989); adapted",
    footnotes=[{"mark": "*", "text": "A plan to build a large dam on the Volta River to make electricity, partly to power a plant that would turn bauxite into aluminum."}],
    glossary=[{"t": "preoccupation", "d": "main concern"},
              {"t": "pari passu", "d": "Latin for \"side by side\"; at the same pace"},
              {"t": "diversify", "d": "add more kinds of products"},
              {"t": "bauxite", "d": "a rock that contains aluminum"},
              {"t": "eminently sound", "d": "very well planned"},
              {"t": "land tenure", "d": "the rules for owning or renting land"}]),

"X8": P([
    "We face a hostile ideology—global in scope, atheistic in character, ruthless in purpose, and insidious in method. Unhappily the danger it poses promises to be of indefinite duration. …",
    "Until the latest of our world conflicts, the United States had no armaments industry. American makers of plowshares could, with time and as required, make swords as well. But now we can no longer risk emergency improvisation of national defense; we have been compelled to create a permanent armaments industry of vast proportions. Added to this, three and a half million men and women are directly engaged in the defense establishment. We annually spend on military security more than the net income of all United States corporations.",
    "This conjunction of an immense military establishment and a large arms industry is new in the American experience. The total influence—economic, political, even spiritual—is felt in every city, every State house, every office of the Federal government. … In the councils of government, we must guard against the acquisition of unwarranted influence, whether sought or unsought, by the military-industrial complex. The potential for the disastrous rise of misplaced power exists and will persist. …",
    "Disarmament, with mutual honor and confidence, is a continuing imperative. … I confess that I lay down my official responsibilities in this field with a definite sense of disappointment."],
    "Dwight D. Eisenhower, president of the United States, farewell address to the nation on radio and television, January 17, 1961, three days before he left office",
    "From Public Papers of the Presidents of the United States: Dwight D. Eisenhower, 1960–61; adapted",
    glossary=[{"t": "ideology", "d": "a set of political ideas and beliefs"},
              {"t": "insidious", "d": "working secretly and slowly to do harm"},
              {"t": "improvisation", "d": "making something up quickly, without planning"},
              {"t": "conjunction", "d": "joining together"},
              {"t": "unwarranted", "d": "not justified"},
              {"t": "imperative", "d": "something that must be done"}]),

# ============================== PRACTICE ==============================
"P1": P([
    "The absolute equality of races,—physical, political and social—is the founding stone of world peace and human advancement. …",
    "The beginning of wisdom in interracial contact is the establishment of political institutions among suppressed peoples. The habit of democracy must be made to encircle the earth. … Local self-government with a minimum of help and oversight can be established tomorrow in Asia, in Africa, in America and in the Isles of the Sea. …",
    "England, with her Pax Britannica, her courts of justice, established commerce and a certain apparent recognition of native law and customs, has nevertheless systematically fostered ignorance among the natives, … has usually declined even to try to train black and brown men in real self-government, to recognize civilized black folks as civilized, or to grant to colored colonies those rights of self-government which it freely gives to white men. …",
    "The Negro* race through its thinking intelligentsia is demanding:",
    "I—The recognition of civilized men as civilized despite their race or color\nII—Local self government for backward groups, deliberately rising as experience and knowledge grow to complete self government under the limitations of a self governed world\n… VI—The ancient common ownership of the land and its natural fruits and defence against the unrestrained greed of invested capital\nVII—The establishment under the League of Nations of an international institution for the study of Negro problems"],
    "Manifesto adopted at the London session of the Second Pan-African Congress, a meeting of leaders from Africa, the Caribbean, the United States, and Europe that also met in Brussels and Paris, 1921",
    "As printed in The Crisis, the magazine of the National Association for the Advancement of Colored People (NAACP), November 1921; adapted",
    footnotes=[{"mark": "*", "text": "\"Negro,\" \"colored,\" and \"backward groups\" were common terms in the 1920s. The Congress used them for Africans and people of African descent and for colonized peoples."}],
    glossary=[{"t": "manifesto", "d": "a public statement of goals"},
              {"t": "Pax Britannica", "d": "Latin for \"British peace\"; the order Britain claimed its empire kept"},
              {"t": "intelligentsia", "d": "educated people who lead a group's thinking"},
              {"t": "invested capital", "d": "money put into businesses to earn profits"}]),

"P2": P([
    "At bottom of Kremlin's neurotic view of world affairs is traditional and instinctive Russian sense of insecurity. … Russian rulers have invariably sensed that their rule was relatively archaic in form, fragile and artificial in its psychological foundation, unable to stand comparison or contact with political systems of Western countries. For this reason they have always feared foreign penetration … . And they have learned to seek security only in patient but deadly struggle for total destruction of rival power, never in compacts and compromises with it. …",
    "(1) Soviet power, unlike that of Hitlerite Germany, is neither schematic nor adventuristic. It does not work by fixed plans. It does not take unnecessary risks. Impervious to logic of reason, and it is highly sensitive to logic of force. For this reason it can easily withdraw—and usually does—when strong resistance is encountered at any point. …",
    "(2) Gauged against Western World as a whole, Soviets are still by far the weaker force. Thus, their success will really depend on degree of cohesion, firmness and vigor which Western World can muster. …",
    "… World communism is like malignant parasite which feeds only on diseased tissue. This is point at which domestic and foreign policies meet. …"],
    "George F. Kennan, a senior American diplomat at the U.S. embassy in Moscow, telegram to the U.S. secretary of state, February 22, 1946, later called the \"Long Telegram.\" Kennan wrote in the short style of a telegram, leaving out small words such as \"the.\"",
    "Printed in Foreign Relations of the United States, 1946, vol. VI (Washington, D.C., 1969); adapted",
    glossary=[{"t": "Kremlin", "d": "the Soviet government (named for its headquarters in Moscow)"},
              {"t": "neurotic", "d": "fearful in a way that is not reasonable"},
              {"t": "archaic", "d": "old-fashioned; out of date"},
              {"t": "compacts", "d": "agreements"},
              {"t": "schematic nor adventuristic", "d": "neither following a fixed plan nor taking wild chances"},
              {"t": "impervious", "d": "not affected by"},
              {"t": "cohesion", "d": "sticking together; unity"},
              {"t": "malignant", "d": "harmful and spreading"}]),

"P3": P([
    "In considering the requirements for the rehabilitation of Europe, the physical loss of life, the visible destruction of cities, factories, mines, and railroads was correctly estimated, but it has become obvious during recent months that this visible destruction was probably less serious than the dislocation of the entire fabric of European economy. …",
    "The truth of the matter is that Europe's requirements for the next three or four years of foreign food and other essential products—principally from America—are so much greater than her present ability to pay that she must have substantial additional help or face economic, social, and political deterioration of a very grave character. …",
    "Our policy is directed not against any country or doctrine but against hunger, poverty, desperation, and chaos. Its purpose should be the revival of a working economy in the world so as to permit the emergence of political and social conditions in which free institutions can exist. … Any government which maneuvers to block the recovery of other countries cannot expect help from us. Furthermore, governments, political parties, or groups which seek to perpetuate human misery in order to profit therefrom politically or otherwise will encounter the opposition of the United States.",
    "… The initiative, I think, must come from Europe. … The program should be a joint one, agreed to by a number, if not all, European nations."],
    "George C. Marshall, U.S. secretary of state, speech at Harvard University, Cambridge, Massachusetts, June 5, 1947",
    "As printed in the Department of State Bulletin, June 15, 1947; adapted",
    glossary=[{"t": "rehabilitation", "d": "restoring to good condition"},
              {"t": "dislocation", "d": "breakdown; being thrown out of place"},
              {"t": "fabric", "d": "here, the whole structure"},
              {"t": "deterioration", "d": "getting worse"},
              {"t": "doctrine", "d": "a set of beliefs"},
              {"t": "perpetuate", "d": "make something continue"}]),

"P4": P([
    "Two complex sets of factors have now basically altered this historical distribution of power. First, the defeat of Germany and Japan and the decline of the British and French Empires have interacted with the development of the United States and the Soviet Union in such a way that power has increasingly gravitated to these two centers. Second, the Soviet Union, unlike previous aspirants to hegemony, is animated by a new fanatic faith, antithetical to our own, and seeks to impose its absolute authority over the rest of the world. …",
    "The assault on free institutions is world-wide now, and in the context of the present polarization of power a defeat of free institutions anywhere is a defeat everywhere. …",
    "As for the policy of \"containment\", it is one which seeks by all means short of war to (1) block further expansion of Soviet power, (2) expose the falsities of Soviet pretensions, (3) induce a retraction of the Kremlin's control and influence and (4) in general, so foster the seeds of destruction within the Soviet system that the Kremlin is brought at least to the point of modifying its behavior to conform to generally accepted international standards. …",
    "Without superior aggregate military strength, in being and readily mobilizable, a policy of \"containment\"—which is in effect a policy of calculated and gradual coercion—is no more than a policy of bluff."],
    "\"United States Objectives and Programs for National Security,\" a secret report by officials of the U.S. State and Defense Departments to the National Security Council, April 1950, known as NSC-68",
    "Printed in Foreign Relations of the United States, 1950, vol. I (Washington, D.C., 1977); adapted",
    glossary=[{"t": "gravitated", "d": "moved toward"},
              {"t": "aspirants to hegemony", "d": "powers that tried to dominate others"},
              {"t": "antithetical", "d": "directly opposed"},
              {"t": "polarization", "d": "division into two opposite sides"},
              {"t": "pretensions", "d": "false claims"},
              {"t": "retraction", "d": "pulling back"},
              {"t": "aggregate", "d": "total"},
              {"t": "mobilizable", "d": "able to be made ready for war"},
              {"t": "coercion", "d": "forcing someone to act by using threats"}]),

"P5": P([
    "Jen Pi-shih. During the past year or two, too many individuals during the agrarian reform have been purged and too many have been incorrectly classified. … The elimination of the feudal classes is a ruthless struggle. The backbone of the Communist movement is the poor peasants and the farm laborers. It is, however, necessary to unite with the middle peasants lest the poor be isolated and the revolution fail. …",
    "It is necessary to eliminate rich peasants and landlords and to confiscate their surplus. It is also necessary to confiscate all property belonging to the landlords. But even landlords vary. Those landlords who voluntarily give up their property should not be subject to the judgment of mass meetings and should be given enough to maintain peasant status. Those who do not give up their property voluntarily should be ruthlessly destroyed. …",
    "Mao Tze-tung. … Party work during the anti-Japanese war was basically correct, but its mistakes must now be corrected. The main objective now must be to increase production by renewed agrarian reform and purification of the Party. … The enemies to be overthrown are imperialism, feudalism, and bureaucratic capitalism. All three can be summed up in Chiang Kai-shek's Kuomintang. The demands of the masses must be satisfied. …"],
    "Summary by the U.S. embassy in Nanjing, China, of speeches by Ren Bishi (Jen Pi-shih), a top leader of the Chinese Communist Party, and by Mao Zedong (Mao Tze-tung), the party's chairman, as broadcast by the Communists' radio station in northern China in April and May 1948; sent by Ambassador John Leighton Stuart to the U.S. secretary of state, June 9, 1948",
    "Printed in Foreign Relations of the United States, 1948, vol. VII (Washington, D.C., 1973); adapted",
    glossary=[{"t": "agrarian reform", "d": "changes in who owns and farms the land"},
              {"t": "purged", "d": "removed or punished as enemies"},
              {"t": "feudal classes", "d": "here, landlords and others who lived off the rents and labor of peasants"},
              {"t": "middle peasants", "d": "peasants who farmed their own land and neither rented much out nor rented much in"},
              {"t": "confiscate", "d": "take away by order of those in power"},
              {"t": "bureaucratic capitalism", "d": "the Communists' name for businesses run by officials and their friends"},
              {"t": "Kuomintang", "d": "the Nationalist Party, led by Chiang Kai-shek"}]),

"P6": P([
    "On June 17, 1952, a comprehensive agrarian reform program became law in Guatemala. Its professed objective is the development of a capitalistic agricultural economy through the abolition of semi-feudal owner-worker relationships, the redistribution of land, and the improvement with state assistance of cultivation methods. The implications of the legislation, however, go beyond agrarian reform inasmuch as its provisions furnish a basis for the strengthening of political and Communist control over the rural population.",
    "Full implementation of the law would free thousands of agrarian workers from a centuries-old dependence upon the privileged landholding class, but would subject the majority, in all probability, to close control by the state. …",
    "Administration forces undoubtedly envisage political benefits from the legislation. They are presumably anxious to break the control of the conservative anti-administration large landholders over the farm labor force in order to organize it behind the government. Advantages to the Communists are likely to be enhanced by the opportunity to extend the influence in farm areas … and through greater opportunities to attack the United Fruit Company. …",
    "… Largest of these enterprises is the United Fruit Company which owns or leases some 450,000 acres possibly subject to expropriation."],
    "Intelligence report by the Office of Intelligence Research, U.S. Department of State, Washington, D.C., March 5, 1953, about a land law passed under Guatemala's elected president, Jacobo Árbenz",
    "Printed in Foreign Relations of the United States, 1952–1954, Guatemala (Washington, D.C., 2003); adapted",
    glossary=[{"t": "professed objective", "d": "stated goal"},
              {"t": "abolition", "d": "ending"},
              {"t": "semi-feudal", "d": "partly like the old system in which peasants worked for landlords in return for the right to farm"},
              {"t": "envisage", "d": "expect"},
              {"t": "United Fruit Company", "d": "a large U.S. company that grew bananas in Central America"},
              {"t": "expropriation", "d": "the taking of private property by a government"}]),

"P7": {"type": "image",
    "src": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Cuban_missiles.jpg/960px-Cuban_missiles.jpg",
    "width": 960, "height": 928,
    "alt": "A black-and-white aerial photograph of cleared, rutted ground among palm trees and fields, with a title box and white labels connected by lines to objects on the ground.",
    "caption": "An aerial photograph of cleared, rutted ground among palm trees and fields. A box at the top reads \"MRBM LAUNCH SITE 2, SAN CRISTOBAL, 1 NOVEMBER 1962.\" Lines drawn on the photograph point to labels that read \"MISSILE-READY TENT,\" \"FORMER LAUNCH POSITIONS,\" \"FUEL TRAILERS,\" and \"FORMER LOCATION OF MISSILE-READY TENTS.\"",
    "attribution": "U.S. military reconnaissance photograph taken from a low-flying plane over San Cristóbal, Cuba, November 1, 1962, with labels added by U.S. intelligence analysts",
    "credit": "Public domain image (U.S. military photograph, U.S. National Archives) via Wikimedia Commons.",
    "description": "A black-and-white photograph taken from a low-flying airplane, looking down at an angle. Tall palm trees and patches of dark trees surround a large area of bare, rutted ground crossed by a straight dirt road. A white title box at the upper left reads \"MRBM LAUNCH SITE 2, SAN CRISTOBAL, 1 NOVEMBER 1962.\" Thin white lines connect small white labels to spots on the ground: a single standing tent (\"MISSILE-READY TENT\"), two bare patches (\"FORMER LAUNCH POSITIONS\"), a group of parked tanker trucks (\"FUEL TRAILERS\"), and two places with only marks left on the ground (\"FORMER LOCATION OF MISSILE-READY TENTS\").",
    "glossary": [{"t": "reconnaissance", "d": "flying over or watching an area to gather military information"},
                 {"t": "MRBM", "d": "medium-range ballistic missile"},
                 {"t": "missile-ready tent", "d": "a tent where missiles were kept ready to be raised for launch"}]},

"P8": P([
    "… I wanted to avoid violence, I want to avoid violence. Non-violence is the first article of my faith. It is also the last article of my creed. …",
    "The first shock came in the shape of the Rowlatt Act, a law designed to rob the people of all real freedom. I felt called upon to lead an intensive agitation against it. Then followed the Punjab horrors beginning with the massacre at Jallianwala Bagh and culminating in crawling orders, public flogging and other indescribable humiliations. …",
    "I came reluctantly to the conclusion that the British connection had made India more helpless than she ever was before, politically and economically. … Before the British advent, India spun and wove in her millions of cottages just the supplement she needed for adding to her meagre agricultural resources. This cottage industry, so vital for India's existence, has been ruined by incredibly heartless and inhuman processes as described by English witnesses. …",
    "In my humble opinion, Non-co-operation with evil is as much a duty as is co-operation with good. But in the past, Non-co-operation has been deliberately expressed in violence to the evil doer. I am endeavouring to show to my countrymen that violent Non-co-operation only multiplies evil and that as evil can only be sustained by violence, withdrawal of support of evil requires complete abstention from violence. Non-violence implies voluntary submission to the penalty for Non-co-operation with evil. I am here, therefore, to invite and submit cheerfully to the highest penalty that can be inflicted upon me for what in law is a deliberate crime and what appears to me to be the highest duty of a citizen."],
    "Mohandas K. Gandhi, statement to the court at his trial for sedition, Ahmedabad, India, March 18, 1922",
    "As printed in Young India, 1919–1922, by Mahatma Gandhi, second edition (Madras: S. Ganesan, 1924); adapted",
    glossary=[{"t": "creed", "d": "set of beliefs"},
              {"t": "agitation", "d": "public campaign of protest"},
              {"t": "crawling orders", "d": "an order by a British general forcing Indians to crawl on their bellies along one street in Amritsar"},
              {"t": "advent", "d": "arrival"},
              {"t": "meagre", "d": "small; not enough"},
              {"t": "abstention", "d": "holding back from"},
              {"t": "sedition", "d": "words or acts that urge people to rebel against a government"}]),

"P9": P([
    "French prestige and influence in North Africa are decreasing at an alarming rate. This is due to a number of causes:",
    "A. The perpetuation of the Algerian war which is poisoning the atmosphere of all of North Africa from Morocco to Libya and is now beginning to reach down into Mauretania in French West Africa.",
    "B. French failure to behave in their relations with Morocco and Tunisia in accordance with the requirements of the independence of those countries. …",
    "C. The growing belief of many in North Africa that France cannot over a long period marshall sufficient strength to win a military victory in North Africa and that they can therefore afford to hold out for a solution of the Algerian problem which will assure either immediate independence or independence within the foreseeable future. …",
    "[Recommendation:] That the United States Government move as rapidly as possible to assure the continued pro-Western orientation and moderate nature of the Governments of North Africa by cementing our own relations with those countries. To this end, the United States should: … Avoid any identification with repressive features of French policies in Algeria … .",
    "… We should be sensitive to the fact that new states will be emerging from among the present dependent territories in Africa. … We must look most carefully at our information output which, I suspect, is by no means as effective as that being disseminated by the Communists."],
    "Richard Nixon, vice president of the United States, report to President Dwight D. Eisenhower on his trip to Africa, February 28–March 21, 1957, dated April 5, 1957",
    "Printed in Foreign Relations of the United States, 1955–1957, vol. XVIII (Washington, D.C., 1989); adapted",
    glossary=[{"t": "prestige", "d": "respect and standing in the eyes of others"},
              {"t": "perpetuation", "d": "continuing"},
              {"t": "marshall", "d": "gather; bring together"},
              {"t": "orientation", "d": "direction; leaning"},
              {"t": "dependent territories", "d": "colonies"},
              {"t": "disseminated", "d": "spread"}]),

"P10": {"type": "pair", "items": [
    item("Source 1", [
        "In Korea the Government forces, which were armed to prevent border raids and to preserve internal security, were attacked by invading forces from North Korea. The Security Council of the United Nations called upon the invading troops to cease hostilities and to withdraw to the 38th parallel. This they have not done, but on the contrary have pressed the attack. … In these circumstances I have ordered United States air and sea forces to give the Korean Government troops cover and support.",
        "The attack upon Korea makes it plain beyond all doubt that communism has passed beyond the use of subversion to conquer independent nations and will now use armed invasion and war. …",
        "I have similarly directed acceleration in the furnishing of military assistance to the forces of France and the Associated States in Indochina and the dispatch of a military mission to provide close working relations with those forces."],
        "Harry S. Truman, president of the United States, statement on the situation in Korea, June 27, 1950",
        "From Public Papers of the Presidents of the United States: Harry S. Truman, 1950; adapted",
        glossary=[{"t": "38th parallel", "d": "the line of latitude dividing North Korea from South Korea"},
                  {"t": "subversion", "d": "secret efforts to weaken or overthrow a government"},
                  {"t": "acceleration", "d": "speeding up"},
                  {"t": "Associated States in Indochina", "d": "Vietnam, Laos, and Cambodia, which were then still tied to France"}]),
    item("Source 2", [
        "I'm speaking of Nicaragua, a Soviet ally on the American mainland only 2 hours' flying time from our own borders. With over a billion dollars in Soviet-bloc aid, the Communist government of Nicaragua has launched a campaign to subvert and topple its democratic neighbors. …",
        "The United States Congress has before it a proposal to help stop this threat. The legislation is an aid package of $100 million for the more than 20,000 freedom fighters struggling to bring democracy to their country and eliminate this Communist menace at its source. …",
        "… But let me make one thing plain: I'm not talking about American troops. They are not needed; they have not been requested. The democratic resistance fighting in Nicaragua is only asking America for the supplies and support to save their own country from communism. …",
        "Forty years ago Republicans and Democrats joined together behind the Truman doctrine. It must be our policy, Harry Truman declared, to support peoples struggling to preserve their freedom."],
        "Ronald Reagan, president of the United States, address to the nation on the situation in Nicaragua, broadcast on radio and television, March 16, 1986",
        "From Public Papers of the Presidents of the United States: Ronald Reagan, 1986; adapted",
        glossary=[{"t": "Soviet-bloc", "d": "the Soviet Union and the countries allied with it"},
                  {"t": "subvert", "d": "weaken or overthrow in secret"},
                  {"t": "freedom fighters", "d": "Reagan's name for the armed groups fighting Nicaragua's government"},
                  {"t": "menace", "d": "threat"}])]},

"P11": {"type": "table",
    "title": "People Living in the United States Who Were Born in Selected Countries, 1960–2000",
    "columns": ["Country of birth", "1960", "1970", "1980", "1990", "2000"],
    "rows": [["Philippines", "104,843", "184,842", "501,440", "912,674", "1,369,070"],
             ["Cuba", "79,150", "439,048", "607,814", "736,971", "872,716"],
             ["Korea", "11,171", "38,711", "289,885", "568,397", "864,125"],
             ["Vietnam", "not available", "not available", "231,120", "543,262", "988,174"]],
    "text": "Figures come from the U.S. census, which is taken every ten years. \"Korea\" includes North and South Korea. The census tables do not give a separate count of people born in Vietnam for 1960 and 1970.",
    "source": "Campbell Gibson and Kay Jung, Historical Census Statistics on the Foreign-Born Population of the United States: 1850 to 2000, Population Division Working Paper No. 81 (Washington, D.C.: U.S. Census Bureau, 2006), Table 3"},

"P12": {"type": "pair", "items": [
    item("Source 1", [
        "Bajpai told me last night that a non-Muslim caravan of 500 moving on October 3 under guard from NWFP toward East Punjab was attacked by Muslims* and that about 400 killed and remainder including women and children wounded. These 500 were part of the concentration of about 50,000 non-Muslims who have during recent weeks fled from West Punjab into NWFP for safety.",
        "Prime Minister through Bajpai makes formal request that US make available ten army transport planes to fly these 50,000 refugees from a concentration point, say at Peshawar, to Amritsar. These refugees are in bad shape, are starving, and in immediate peril. … When news gets out a new outburst against Muslims in Delhi is almost certain and if the 50,000 perish from hunger and/or attack communal war will reach proportions beyond anything yet seen. …"],
        "Telegram from Henry F. Grady, U.S. ambassador to India, to the U.S. secretary of state, New Delhi, October 5, 1947. Grady wrote in the short style of a telegram.",
        "Printed in Foreign Relations of the United States, 1947, vol. III (Washington, D.C., 1972); adapted",
        footnotes=[{"mark": "*", "text": "In 1947 Hindus, Sikhs, and Muslims in the Punjab all carried out attacks on members of other religious communities."}],
        glossary=[{"t": "Bajpai", "d": "Girja Shankar Bajpai, the top official in India's foreign ministry"},
                  {"t": "NWFP", "d": "the North-West Frontier Province, next to the Punjab"},
                  {"t": "Prime Minister", "d": "Jawaharlal Nehru"},
                  {"t": "Peshawar, Amritsar", "d": "cities in the northwest of the former British India"},
                  {"t": "communal", "d": "between religious communities"}]),
    item("Source 2", [
        "1. Although the total number of Palestine refugees and destitute persons now receiving relief is 950,000, it is assumed that the maximum number of bonafide displaced persons who must eventually be repatriated or resettled will not exceed 700,000. …",
        "2. The disposition of the refugees is now a political issue of the highest order between Israel and the Arab States, neither of which will consider it as a refugee problem. …",
        "3. … the Arab states are reluctant to accept refugees for permanent resettlement for political as well as economic reasons. They take the position that Israel, and to a lesser extent the United Nations and the United States, created the problem and are responsible for its solution. … The Israelis, on the other hand, are reluctant to repatriate any large number of refugees because of economic and security considerations, and because of the need for land to carry out their planned Jewish immigration program. The Israelis take the position that the problem was created by the invasion of the Arab states, and must be solved by resettlement."],
        "Paper prepared in the office of George McGhee, the U.S. State Department's coordinator on Palestine refugee matters, attached to his memorandum to the secretary of state, Washington, D.C., April 1949",
        "Printed in Foreign Relations of the United States, 1949, vol. VI (Washington, D.C., 1977); adapted",
        glossary=[{"t": "destitute", "d": "having no money or home"},
                  {"t": "bonafide", "d": "real; genuine"},
                  {"t": "repatriated", "d": "sent back to their homeland"},
                  {"t": "resettled", "d": "given a new permanent home somewhere else"},
                  {"t": "disposition", "d": "what will be done with"}])]},

"P13": P([
    "A decade of conflict in Afghanistan, from 1979 to 1989, gave Islamist extremists a rallying point and training field. A Communist government in Afghanistan gained power in 1978 but was unable to establish enduring control. At the end of 1979, the Soviet government sent in military units to ensure that the country would remain securely under Moscow's influence. The response was an Afghan national resistance movement that defeated Soviet forces.",
    "Young Muslims from around the world flocked to Afghanistan to join as volunteers in what was seen as a \"holy war\"—jihad—against an invader. The largest numbers came from the Middle East. Some were Saudis, and among them was Usama Bin Ladin. …",
    "The international environment for Bin Ladin's efforts was ideal. Saudi Arabia and the United States supplied billions of dollars worth of secret assistance to rebel groups in Afghanistan fighting the Soviet occupation. This assistance was funneled through Pakistan … . But Bin Ladin and his comrades had their own sources of support and training, and they received little or no assistance from the United States.",
    "April 1988 brought victory for the Afghan jihad. Moscow declared it would pull its military forces out of Afghanistan within the next nine months. … Bin Ladin and Azzam* agreed that the organization successfully created for Afghanistan should not be allowed to dissolve. They established what they called a base or foundation (al Qaeda) as a potential general headquarters for future jihad."],
    "National Commission on Terrorist Attacks upon the United States (the \"9/11 Commission\"), a panel created by the U.S. Congress and the president to study the attacks of September 11, 2001, The 9/11 Commission Report, 2004",
    "Washington, D.C.: U.S. Government Printing Office, 2004; adapted",
    footnotes=[{"mark": "*", "text": "Abdullah Azzam, a Palestinian preacher who had recruited Muslim volunteers for the war in Afghanistan."}],
    glossary=[{"t": "Islamist extremists", "d": "people with extreme views who want governments run by their own version of Islamic law"},
              {"t": "enduring", "d": "lasting"},
              {"t": "funneled", "d": "passed along"},
              {"t": "dissolve", "d": "break up; come to an end"}]),

"P14": P([
    "Efforts by the United States to support anti-Communist forces in Chile date back to the late 1950s and reflect the rivalry between the United States and the Soviet Union for influence throughout the Third World. The growing strength of the Chilean left, along with continuing fragmentation by conservative and moderate political forces, became increasing concerns … to the United States, which wanted to avoid the emergence of \"another Cuba\" in the Western Hemisphere.",
    "According to the Church Committee report, in their meeting with CIA Director Richard Helms and Attorney General John Mitchell on 15 September 1970 President Nixon and his National Security Advisor, Henry Kissinger, directed the CIA to prevent Allende from taking power. … In addition to political action, Nixon and Kissinger, according to Helms's notes, ordered steps to \"make the economy scream.\"",
    "These Cold War attitudes persisted into the Pinochet era. After Pinochet came to power, senior policymakers appeared reluctant to criticize human rights violations, taking to task US diplomats urging greater attention to the problem. US military assistance and sales grew significantly during the years of greatest human rights abuses. …",
    "Many of Pinochet's officers were involved in systematic and widespread human rights abuses following Allende's ouster. Some of these were contacts or agents of the CIA or US military."],
    "U.S. Central Intelligence Agency, \"CIA Activities in Chile,\" a report to the U.S. Congress, released September 2000",
    "Adapted; the last paragraph comes from the report's summary of findings, which appears before the other paragraphs",
    glossary=[{"t": "Third World", "d": "a Cold War term for the countries of Asia, Africa, and Latin America that were allied with neither superpower"},
              {"t": "fragmentation", "d": "breaking into small groups"},
              {"t": "Church Committee", "d": "a U.S. Senate committee that investigated the CIA in 1975"},
              {"t": "Allende", "d": "Salvador Allende, a Marxist socialist elected president of Chile in 1970"},
              {"t": "Pinochet", "d": "Augusto Pinochet, Chile's ruler from 1973 to 1990"},
              {"t": "ouster", "d": "removal from power"}]),

"P15": P([
    "Behind me stands a wall that encircles the free sectors of this city, part of a vast system of barriers that divides the entire continent of Europe. …",
    "In the 1950's, Khrushchev predicted: \"We will bury you.\" But in the West today, we see a free world that has achieved a level of prosperity and well-being unprecedented in all human history. In the Communist world, we see failure, technological backwardness, declining standards of health, even want of the most basic kind—too little food. Even today, the Soviet Union still cannot feed itself. …",
    "And now the Soviets themselves may, in a limited way, be coming to understand the importance of freedom. We hear much from Moscow about a new policy of reform and openness. Some political prisoners have been released. Certain foreign news broadcasts are no longer being jammed. … General Secretary Gorbachev, if you seek peace, if you seek prosperity for the Soviet Union and Eastern Europe, if you seek liberalization: Come here to this gate! Mr. Gorbachev, open this gate! Mr. Gorbachev, tear down this wall! …",
    "… And in cooperation with many of our allies, the United States is pursuing the Strategic Defense Initiative—research to base deterrence not on the threat of offensive retaliation, but on defenses that truly defend; on systems, in short, that will not target populations, but shield them."],
    "Ronald Reagan, president of the United States, speech at the Brandenburg Gate, West Berlin, West Germany, June 12, 1987. The speech was broadcast in Western Europe and could also be heard in East Germany.",
    "From Public Papers of the Presidents of the United States: Ronald Reagan, 1987; adapted",
    glossary=[{"t": "unprecedented", "d": "never seen before"},
              {"t": "jammed", "d": "blocked with radio noise so that people cannot hear"},
              {"t": "General Secretary", "d": "the title of the leader of the Soviet Communist Party"},
              {"t": "deterrence", "d": "preventing an attack by making the enemy afraid of what would happen"},
              {"t": "retaliation", "d": "striking back"}]),

"P16": P([
    "Chairman Gorbachev asked whether the President was also undertaking reforms? … The Chairman then said that he had heard that the new President was getting advice from both the right and the left in the United States. Experts on the right were saying that with the Soviet Union so involved in reform, with its economy so weak, with its ethnic strife so severe, the moment had clearly come to create an upheaval and perhaps destroy the country forever. … It was unrealistic for either side to hope or expect that the other could not function at home or abroad. Let us be realistic, and base our policies on realism.",
    "Perestroika is our business, Chairman Gorbachev continued, whether anyone likes it or not. It is what we need. As to the question of whether the Soviet Union would emerge stronger or weaker from current policies, the Chairman said he always replies that if he did not expect his country to be stronger—politically, economically, and socially—he would not have embarked on reforms. …",
    "… Concerning Armenia and Azerbaijan, it is always easy to talk about ethnic problems. They are certainly present. Some Armenians ask for greater autonomy because of an accumulation of problems. …",
    "… the process of perestroika was expanding, and its strong side was that democratization would be introduced in all areas of Soviet life. But demagogic and extremist elements were taking advantage of existing difficulties. …"],
    "Memorandum of a conversation at a lunch of Soviet leader Mikhail Gorbachev with President Ronald Reagan and Vice President George H. W. Bush, who had just been elected president, Governors Island, New York, December 7, 1988, written by U.S. notetakers",
    "Printed in Foreign Relations of the United States, 1981–1988, vol. VI (Washington, D.C., 2016); adapted",
    glossary=[{"t": "Chairman", "d": "Gorbachev's title as head of the Soviet state"},
              {"t": "strife", "d": "conflict"},
              {"t": "upheaval", "d": "a sudden, violent change"},
              {"t": "embarked on", "d": "started"},
              {"t": "autonomy", "d": "self-rule"},
              {"t": "demagogic", "d": "stirring up people's feelings to gain power"}]),
}

# Raw files used by the excerpt checker (not part of the bank).
RAWMAP = {
    "X1": ["avalon_trudoc.txt"],
    "X2.1": ["frus1961-63v06_d66.txt"], "X2.2": ["frus1961-63v06_d67.txt"],
    "X5": ["pp/PP-I.txt"],
    "X6": ["jprs_mao_misc_part1.txt"],
    "X7": ["frus1955-57v18_d129.txt"],
    "X8": ["avalon_eisenhower001.txt"],
    "P1": ["crisis1921-11.txt", "crisis1921-11_b.txt"],
    "P2": ["frus1946v06_d475.txt"],
    "P3": ["dsb1947-06-15.txt"],
    "P4": ["frus1950v01_d85.txt"],
    "P5": ["frus1948v07_d227.txt"],
    "P6": ["guat_d35.txt"],
    "P8": ["youngindia1924_huebsch.txt", "gandhiapostle1923.txt"],
    "P9": ["frus1955-57v18_d19.txt"],
    "P10.1": ["truman_korea.txt"], "P10.2": ["reagan_nicaragua.txt"],
    "P12.1": ["frus1947v03_d112.txt"], "P12.2": ["pal_d608.txt"],
    "P13": ["gpo_911report.txt"],
    "P14": ["hinchey2000_transcript.txt", "hinchey2000.txt"],
    "P15": ["reagan_brandenburg.txt"],
    "P16": ["frus1981-88v06_d181.txt"],
}

STIM = {k: v for k, v in STIM.items() if v is not None}
