# AP World Unit 4 sources. Texts follow the public-domain translations saved in aw4/sources/*.md,
# lightly adapted (cuts marked with ellipses, archaic spelling modernized where noted). Keep in sync.
VERSION = "2026-11-07a"

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

# Hamilton (1929) Table A: average annual registered treasure imports (total pesos), by decade.
_HAM = [("1503-1510", 8, 286932.5), ("1511-1520", 10, 437749.9), ("1521-1530", 10, 234521.2), ("1531-1540", 10, 1117624.9),
        ("1541-1550", 10, 2092543.2), ("1551-1560", 10, 3572905.9), ("1561-1570", 10, 5069750.2), ("1571-1580", 10, 5831710.0),
        ("1581-1590", 10, 10641448.5), ("1591-1600", 10, 13922672.6), ("1601-1610", 10, 11161707.0), ("1611-1620", 10, 10928116.1),
        ("1621-1630", 10, 10393041.0), ("1631-1640", 10, 6685091.2), ("1641-1650", 10, 5106869.9), ("1651-1660", 10, 2130976.5)]
def _ham20():
    cats, vals = [], []
    for i in range(0, 16, 2):
        (a, ya, va), (b, yb, vb) = _HAM[i], _HAM[i + 1]
        avg = (va * ya + vb * yb) / (ya + yb)
        cats.append(a[:4] + "–" + b[7:9] if b[5:7] != "16" or a[:2] == b[5:7] else a[:4] + "–" + b[5:9])
        vals.append(round(avg / 1e6, 1))
    return cats, vals
_HC, _HV = _ham20()
# Hamilton's 1929 Table A is uniformly about twice his revised 1934 series (1503-1660 total: 895.6M vs. the standard 447.8M pesos of 450 maravedis).
# Use the 1934 series (American Treasure and the Price Revolution in Spain, p. 34), 20-year annual averages, rounded to 0.1M.
_HV = [0.2, 0.3, 1.4, 2.7, 6.1, 5.5, 4.3, 1.8]
_HC = ["1503–20", "1521–40", "1541–60", "1561–80", "1581–1600", "1601–20", "1621–40", "1641–60"]

STIM = {
# ============================== EXAM ==============================
"X1": P([
    "… [Prince Henry] had also a wish to know the land that lay beyond the isles of Canary and that Cape called Bojador, for up to his time … neither by writings, nor by the memory of man, was known with any certainty the nature of the land beyond that Cape. … And this was the first reason of his action.",
    "The second reason was that if there chanced to be in those lands some population of Christians, or some havens into which it would be possible to sail without peril, many kinds of merchandise might be brought to this realm, which would find a ready market … because no other people of these parts traded with them … and also the products of this realm might be taken there, which traffic would bring great profit to our countrymen.",
    "The third reason was that, as it was said that the power of the Moors in that land of Africa was very much greater than was commonly supposed … the said Lord Infant* exerted himself to cause this to be fully discovered, and to make it known how far the power of those infidels extended.",
    "The fourth reason was because during the one and thirty years that he had warred against the Moors, he had never found a Christian king, nor a lord outside this land, who for the love of our Lord Jesus Christ would aid him in the said war. Therefore he sought to know if there were in those parts any Christian princes … who would aid him against those enemies of the faith.",
    "The fifth reason was his great desire to make increase in the faith of our Lord Jesus Christ and to bring to him all the souls that should be saved."],
    "Gomes Eanes de Zurara, royal chronicler of Portugal, Chronicle of the Discovery and Conquest of Guinea, 1453",
    "Translated by C. Raymond Beazley and Edgar Prestage (1896); adapted",
    footnotes=[{"mark": "*", "text": "Prince Henry of Portugal (1394–1460), son of King João I, who sponsored Portuguese voyages down the West African coast"}],
    glossary=[{"t": "Cape Bojador", "d": "a cape on the northwest coast of Africa that Portuguese ships first sailed past in 1434"},
              {"t": "havens", "d": "safe harbors"}, {"t": "Moors / infidels", "d": "Zurara's words for Muslims of North Africa"},
              {"t": "realm", "d": "kingdom (here, Portugal)"}, {"t": "traffic", "d": "trade"}]),

"X2": {"type": "pair", "items": [
    item("Source 1", [
        "… Of three millions of persons which lived in Hispaniola itself, there is at present but the inconsiderable remnant of scarce three hundred. …",
        "Now the ultimate end and scope that incited the Spaniards to … the desolation of this people was gold only, that thereby growing rich in a short time, they might arrive at once at such degrees and dignities as were in no ways consistent with their persons. …",
        "[The Spaniards] divided among themselves the young men, women, and children … one obtained thirty, another forty, to this man one hundred were given … upon this pretense, and with this condition, that he should see them instructed in the Catholic religion. … They sent the men to the mines to dig and bring away the gold, which is an intolerable labor; but the women they made use of to till the ground. … The men died in mines, hunger-starved and oppressed with labor, and the women perished in the fields … Thus an infinite number of inhabitants that formerly peopled this island … dwindled away to nothing."],
        "Bartolomé de las Casas, Spanish Dominican friar, A Brief Account of the Destruction of the Indies, written 1542 for King Charles I of Spain",
        "From an English translation published in London in 1689 under the title Popery* Truly Displayed in Its Bloody Colours; spelling modernized and adapted",
        footnotes=[{"mark": "*", "text": "\"Popery\" was an insulting word that English Protestants used for the Roman Catholic Church."}],
        glossary=[{"t": "Hispaniola", "d": "the Caribbean island that today holds Haiti and the Dominican Republic"},
                  {"t": "remnant", "d": "a small part that is left"},
                  {"t": "pretense", "d": "a false reason given to cover the real one"}]),
    item("Source 2", [
        "The rapid melting away of the population of the West Indies during the first quarter of a century of the Spanish rule … is the most familiar instance of the kind, through the impassioned descriptions of Las Casas, which were translated into the principal languages of Europe; and, as a consequence, it is generally believed that the Spaniards were cruel and destructive above all other colonists. … That the wars of subjugation were very destructive of life is only too clear; that famine followed war to prolong its ravages is equally certain; that the average Spaniard recklessly and cruelly overworked the Indians there is no doubt.",
        "Nevertheless, there were other and more subtle causes in operation. Diseases were imported by the whites, which were mitigated for them by some degree of acquired immunity, but which raged irresistibly through a population without that defence. Of these new diseases small-pox was one of the most destructive. In the epidemic of small-pox in 1518 the natives, Peter Martyr* reports, died like sheep. … Small-pox appeared in Mexico at the beginning of the conquest … sweeping off in some provinces half the population."],
        "Edward Gaylord Bourne, historian at Yale University, Spain in America, 1450–1580, published in 1904",
        "Adapted",
        footnotes=[{"mark": "*", "text": "Peter Martyr, an Italian scholar at the Spanish court who wrote about the Americas in the early 1500s. Bourne, writing in 1904, uses older terms: \"the whites\" for Europeans and \"natives\" for Indigenous people."}],
        glossary=[{"t": "subjugation", "d": "conquest"}, {"t": "mitigated", "d": "made less severe"},
                  {"t": "acquired immunity", "d": "protection from a disease built up by earlier exposure to it"}])]},

"X3": {"type": "bar",
    "title": "Average Annual Registered Imports of American Gold and Silver into Spain, 1503–1660",
    "categories": _HC,
    "series": [{"name": "Average imports per year (millions of pesos)", "values": _HV}],
    "yLabel": "Millions of pesos per year",
    "text": "Gold and silver are combined by their money value (1 peso = 450 maravedís, a Spanish unit of account). Most of the silver came from mines at Potosí (in the Andes) and Zacatecas (in Mexico).",
    "source": "Calculated from Earl J. Hamilton, American Treasure and the Price Revolution in Spain, 1501–1650 (1934), p. 34; yearly averages for each 20-year period (first period 18 years), rounded"},

"X4": P([
    "1. No Japanese ships shall ever be sent to foreign lands.",
    "2. No Japanese shall be permitted to go abroad, and if there be discovered anyone who has a secret intention to go abroad he shall be put to death. …",
    "3. If any Japanese residing abroad comes back to Japan, even for a short time, he shall be put to death.",
    "4. Rewards are to be given to those who report to the authorities about the Christians: those who give information about the foreign missionaries shall be given 200 to 300 silver coins according to their merits. …",
    "5. Children and grandchildren of the foreign Christian missionaries shall not be permitted to remain in Japan, and anyone secretly giving shelter to such persons shall be put to death. …"],
    "Ordinance issued by the Tokugawa shogunate to the governors of the port of Nagasaki, Japan, 1636",
    "From Takekoshi Yosaburō, The Economic Aspects of the History of the Civilization of Japan (English edition, 1930); adapted",
    glossary=[{"t": "shogunate", "d": "the government of the shogun, Japan's top military ruler (here, the Tokugawa family)"},
              {"t": "ordinance", "d": "an official order or law"}, {"t": "missionaries", "d": "people sent to spread a religion; here, Catholic priests from Portugal and Spain"}]),

"X5": {"type": "image",
    "src": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Casta_painting_all.jpg/960px-Casta_painting_all.jpg",
    "width": 960, "height": 1353,
    "alt": "A painting divided into sixteen panels, each showing a mother, a father, and a child, with a written label under each family.",
    "caption": "Each panel shows a family. The label assigns colonial social categories to the parents and the child. The first three labels in the top row read: \"Spaniard with Indian woman: Mestizo\"; \"Mestizo with Spanish woman: Castizo\"; \"Castizo with Spanish woman: Spaniard.\" Families in the top rows wear fine European-style clothing. Families in the lower rows wear plainer clothes, carry goods or tools, and some are barefoot. The labels use colonial terms: \"Indian\" meant an Indigenous person, and \"Mulatto,\" a term now considered offensive, meant a person of mixed Spanish and African ancestry.",
    "attribution": "Unknown artist, Las Castas (The Castes), oil painting made in New Spain (colonial Mexico), eighteenth century",
    "credit": "Museo Nacional del Virreinato, Tepotzotlán, Mexico. Public domain image via Wikimedia Commons.",
    "description": "Sixteen small family portraits arranged in four rows of four. In each, a man and a woman stand with a child, and a label below names the mixture of Spanish, Indigenous, and African ancestry the painter assigned to each person. The couples in the first row are dressed in rich cloaks, lace, and fine fabrics. Moving down the rows, the clothing becomes simpler, people carry baskets, fruit, or tools, and several figures in the bottom rows are barefoot.",
    "glossary": [{"t": "New Spain", "d": "Spain's colony in Mexico and nearby lands"},
                 {"t": "Mestizo", "d": "a person of mixed Spanish and Indigenous ancestry"},
                 {"t": "Mulatto", "d": "a colonial term for a person of mixed Spanish and African ancestry"}]},

"X6": P([
    "Under the later Hapsburgs*, with the increasing demands of the colonies on the one hand, and the utter ruin of Spanish industry on the other, the dependence of the Seville export commerce upon foreign manufactures was complete. They supplied five sixths of the cargoes of the outbound fleets. …",
    "The most serious and widespread development of contraband trade, however, was in merchandise introduced into the colonies directly from foreign markets. Portuguese, French, Dutch and other interlopers smuggled their cargoes into the West Indies, through the closed port of Buenos Aires, or even to the Pacific shores of Spanish America. The illicit trader was eagerly welcomed by the colonists, for he supplied their needs at reasonable prices. …",
    "A flood of restrictions, a jealous monopoly, on the one hand—on the other, a flourishing contraband trade of outsiders …—such is the story of Spanish-American commerce in the sixteenth and the seventeenth centuries. The Crown of Castile sought to extend Spanish power, and monopolize all the treasure of the Indies, by means of a rigid and complicated commercial system. Yet in the end, it saw the trade of the New World pass into the hands of its rivals … and its riches diverted at their very source."],
    "Clarence H. Haring, American historian, Trade and Navigation between Spain and the Indies in the Time of the Hapsburgs, published in 1918",
    "Adapted",
    footnotes=[{"mark": "*", "text": "the ruling family of Spain from 1516 to 1700; \"later Hapsburgs\" refers to the 1600s"}],
    glossary=[{"t": "contraband", "d": "smuggled goods"}, {"t": "interlopers", "d": "traders who were not allowed to trade there"},
              {"t": "illicit", "d": "illegal"}, {"t": "monopoly", "d": "complete control of a trade by one group"},
              {"t": "outbound fleets", "d": "the yearly convoys of ships sailing from Seville to the Americas"}]),

"X7": P([
    "They said they had been the first in doing good to the English, and the English the first in doing wrong. They said when the English first came, their king's father* was as a great man and the English as a little child. He kept other Indians from wronging the English, and gave them corn and showed them how to plant, and was free to do them any good, and had let them have a hundred times more land than now the king had for his own people. …",
    "Another grievance was if twenty of their honest Indians testified that an Englishman had done them wrong, it was as nothing, and if but one of their worst Indians testified against any Indian or their king when it pleased the English, that was sufficient. Another grievance was when their kings sold land, the English would say it was more than they agreed to. … Now whom the English had owned for king or queen they would disinherit, and make another king that would give or sell them their land, so that now they had no hopes left to keep any land.",
    "Another grievance: the English cattle and horses still increased, so that when they removed thirty miles from where the English had anything to do, they could not keep their corn from being spoiled, they never being used to fence. …"],
    "John Easton, deputy governor of the English colony of Rhode Island, report of a meeting with Metacom (called King Philip by the English), leader of the Wampanoag people, June 1675",
    "Spelling modernized; adapted",
    footnotes=[{"mark": "*", "text": "Massasoit, Metacom's father, who allied with the Plymouth colonists in 1621"}],
    glossary=[{"t": "grievance", "d": "a complaint about unfair treatment"}, {"t": "testified", "d": "spoke as a witness in court"},
              {"t": "disinherit", "d": "remove from power"}, {"t": "owned", "d": "recognized"}, {"t": "removed", "d": "moved"}, {"t": "they never being used to fence", "d": "they had never needed fences"}]),

"X8": P([
    "From what I can recollect of these battles, they appear to have been raids of one little state or district on the other, to obtain prisoners or booty. Perhaps they were incited to this by those traders who brought the European goods I mentioned amongst us. Such a mode of obtaining slaves in Africa is common; and I believe more are procured this way, and by kidnapping, than any other. When a trader wants slaves, he applies to a chief for them, and tempts him with his wares. … Accordingly he falls on his neighbours, and a desperate battle ensues. If he prevails and takes prisoners, he gratifies his avarice by selling them. …",
    "… Those prisoners which were not sold or redeemed we kept as slaves: but how different was their condition from that of the slaves in the West Indies! With us they do no more work than other members of the community, even their masters; their food, clothing and lodging were nearly the same as theirs, (except that they were not permitted to eat with those who were free-born); and there was scarce any other difference between them, than a superior degree of importance which the head of a family possesses in our state. … Some of these slaves have even slaves under them as their own property."],
    "Olaudah Equiano, formerly enslaved African, describing his childhood in West Africa in the 1750s, The Interesting Narrative of the Life of Olaudah Equiano, published in London in 1789",
    "Adapted",
    glossary=[{"t": "booty", "d": "goods taken by force"}, {"t": "incited", "d": "pushed or encouraged"},
              {"t": "procured", "d": "gotten"}, {"t": "redeemed", "d": "freed after a payment (ransomed)"},
              {"t": "West Indies", "d": "the islands of the Caribbean"}]),

# ============================== PRACTICE ==============================
"P1": P([
    "[Vasco da Gama] sent one of the convicts to Calicut, and those with whom he went took him to two Moors from Tunis, who could speak Castilian and Genoese*. The first greeting that he received was in these words: \"May the Devil take thee! What brought you hither?\" They asked what he sought so far away from home, and he told them that we came in search of Christians and of spices. …",
    "On Tuesday the captain got ready the following things to be sent to the king, namely, twelve pieces of striped cloth, four scarlet hoods, six hats, four strings of coral, a case containing six wash-hand basins, a case of sugar, two casks of oil, and two of honey. … [The king's officials] came, and when they saw the present they laughed at it, saying that it was not a thing to offer to a king, that the poorest merchant from Mecca, or any other part of India, gave more, and that if he wanted to make a present it should be in gold. … When they had gone there came certain Moorish merchants, and they all made fun of the present which the captain desired to be sent to the king."],
    "Journal of a member of Vasco da Gama's crew, describing the Portuguese fleet's arrival at Calicut, India, May 1498",
    "Translated by E. G. Ravenstein (1898); adapted",
    footnotes=[{"mark": "*", "text": "Castilian = Spanish; Genoese = the language of the city of Genoa, in present-day Italy"}],
    glossary=[{"t": "Calicut", "d": "a wealthy port city on the southwest coast of India, ruled by a Hindu king"},
              {"t": "Moors", "d": "the journal's word for Muslims"}, {"t": "convicts", "d": "prisoners the Portuguese brought along to do dangerous jobs"}]),

"P2": P([
    "Española is a wonder. … The harbors on the coast, and the number and size and wholesomeness of the rivers, most of them bearing gold, surpass anything that would be believed by one who had not seen them. … In this island there are many spices and extensive mines of gold and other metals. … They have neither iron, nor steel, nor arms, nor are they competent to use them … because they are timid to a surprising degree.",
    "I gave away a thousand good and pretty articles which I had brought with me in order to win their affection, and that they might be led to become Christians, and be well inclined to love and serve their Highnesses* and the whole Spanish nation, and that they might aid us by giving us things of which we stand in need, but which they possess in abundance. …",
    "Their Highnesses may see that I shall give them all the gold they require, if they will give me but a very little assistance; spices also, and cotton, as much as their Highnesses shall command to be shipped … and slaves, as many … as their Highnesses shall command to be shipped. … All Christendom ought to rejoice … for the great exaltation which may come to them in turning so many nations to our holy faith, and also for the temporal benefits which will bring great refreshment and gain, not only to Spain, but to all Christians."],
    "Christopher Columbus, letter written on his return voyage to Luis de Santángel, a royal official who had helped pay for the voyage, February 1493; the letter was printed and spread across Europe that year",
    "Translated by R. H. Major (1870); adapted",
    footnotes=[{"mark": "*", "text": "King Ferdinand and Queen Isabella of Spain"}],
    glossary=[{"t": "Española", "d": "Hispaniola, the Caribbean island today shared by Haiti and the Dominican Republic"},
              {"t": "temporal", "d": "worldly (money and goods, as opposed to religious)"}]),

"P3": {"type": "table",
    "title": "Estimated Indigenous Population of Central Mexico, 1518–1605",
    "columns": ["Year", "Estimated population"],
    "rows": [["1518", "25.2 million"], ["1532", "16.8 million"], ["1548", "6.3 million"], ["1568", "2.65 million"],
             ["1585", "1.9 million"], ["1595", "1.375 million"], ["1605", "1.075 million"]],
    "text": "These are estimates by historians Sherburne F. Cook and Woodrow Borah, based mainly on Spanish tax and tribute records. Some historians think the 1518 figure is too high, but historians agree that the Indigenous population of central Mexico fell catastrophically in the 1500s.",
    "source": "Sherburne F. Cook and Woodrow Borah, studies of the population of central Mexico, 1960s"},

"P4": P([
    "… There is a river on the hither side of which stands a Muslim town named Rander, wherein are very fair houses and open places. It is a very pleasant and wealthy place, for the Muslim inhabitants thereof trade in their own ships with Malacca, Bengal, Tenasserim, Pegu, Martaban and Sumatra, in spices of divers sorts and drugs and silks in great abundance, musk, benzoin, porcelain and many other wares. Those who dwell here have many great and fair vessels, which carry on this trade, and whosoever would have at his disposal things from Malacca and China, let him go to this place, where he will find them in greater perfection than in any other place soever. …",
    "[In Malacca] dwell up to now great wholesale merchants of every kind, both Muslims and Hindus, many of them from Coromandel, men of great estates and owning many great ships which they call junks. They trade everywhere in goods of all kinds. … They go to Tenasserim, Pegu, Bengal, Pulicat, Coromandel, Malabar and Cambay, so much so that this city of Malacca is the richest seaport with the greatest number of wholesale merchants and abundance of shipping and trade that can be found in the whole world."],
    "Duarte Barbosa, Portuguese official who worked in India from about 1500 to 1516, The Book of Duarte Barbosa, completed about 1518",
    "Translated by M. Longworth Dames (1918–1921); place names and terms modernized (\"Moorish\" to Muslim, \"Heathen\" to Hindu); adapted",
    glossary=[{"t": "Rander", "d": "a port in Gujarat, western India"},
              {"t": "Malacca", "d": "a port on the strait between the Malay Peninsula and Sumatra, captured by the Portuguese in 1511"},
              {"t": "Coromandel", "d": "the southeast coast of India"}, {"t": "junks", "d": "large Asian sailing ships"},
              {"t": "wholesale merchants", "d": "merchants who buy and sell goods in very large amounts"}]),

"P5": P([
    "The following day, Xicotencatl, Captain General of this province*, came to see me … with about fifty of its chiefs, praying me … that I would admit them to the royal service of Your Majesty and to my friendship, and would pardon them the past errors, because they had not understood who we were. He said that they had exerted all their forces … to escape being subjected to anyone, since at no time had this province ever been so … on the contrary, they had always lived free and independent, since immemorial times, and had always defended themselves against the great power of Moctezuma, of his father, and grandfather, who held that country subjected, but had never been able to hold them in subjection, though they had them surrounded on all sides, so that no one could go out of the country. He said also that they ate no salt, since there was none in their country, nor were they allowed to go to buy it anywhere else. … They had endured it, and held it as better thus to be free, rather than be subjected to anyone. They had wanted to do the same with me, but seeing clearly that neither their forces nor their tricks could help them, they had decided that, rather than die, … they would become vassals** of Your Highness."],
    "Hernán Cortés, Spanish conquistador, letter to King Charles I of Spain (Holy Roman Emperor Charles V), 1520, describing events of September 1519",
    "Translated by F. A. MacNutt (1908); names modernized; adapted",
    footnotes=[{"mark": "*", "text": "Tlaxcala, an independent state east of Tenochtitlan, the Mexica (Aztec) capital"}, {"mark": "**", "text": "subjects who owe loyalty and service to a ruler"}],
    glossary=[{"t": "Moctezuma", "d": "Moctezuma II, ruler of the Mexica (Aztec) Empire"},
              {"t": "subjected", "d": "ruled by someone else"}, {"t": "immemorial", "d": "so long ago no one remembers"}]),

"P6": P([
    "The force of silver, which draws unto it the desire of all things, has peopled this mountain more than any other place in all these kingdoms. …",
    "At this day the King receives for his fifth* yearly, from the mines of Potosí, a million of silver. … In the fleet in which I came in the year 1587, there were eleven millions transported in the two fleets of Peru and Mexico, whereof two thirds were in that of Peru, and almost one half for the King. I thought good to set this down … to show the power which His heavenly Majesty has given to the Kings of Spain … who (by the especial favor of heaven) have joined the East with the West Indies, environing the whole world with their power.",
    "They labor in these mines in continual darkness … without knowledge of day or night. … They carry up this metal upon their shoulders, by ladders. A man carries ordinarily the weight of two arrobas** of metal upon his shoulders … and so go they up the ladder holding it with both their hands … a fearful thing, and which breeds an amazement to think upon it, so great is the desire of silver, that for the gain thereof men endure any pains."],
    "José de Acosta, Spanish Jesuit priest who lived in Peru from 1572 to 1586, The Natural and Moral History of the Indies, 1590",
    "Translated by Edward Grimston (1604); spelling modernized; adapted",
    footnotes=[{"mark": "*", "text": "the royal fifth: the king's one-fifth share of the silver mined at Potosí at this time"},
               {"mark": "**", "text": "about 50 pounds (23 kilograms)"}],
    glossary=[{"t": "Potosí", "d": "a huge silver mountain and mining city in the Andes (in today's Bolivia)"},
              {"t": "a million / eleven millions", "d": "pesos, Spanish silver coins"},
              {"t": "East and West Indies", "d": "Asia and the Americas"}, {"t": "environing", "d": "surrounding"}]),

"P7": P([
    "… Though formerly ruled by a governor under the King of Kongo, this governor [of Angola**] has, since the king became a Christian, made himself absolute ruler. Having seized all the lands he ruled, and in time conquered some of the surrounding provinces, he is now a great and rich prince, and hardly less powerful than the King of Kongo, to whom he pays tribute or not, according as he chooses.",
    "It came to pass that after Dom João II of Portugal planted the faith of Christ in the Kingdom of Kongo, and the king became a Christian, the Lord of Angola was always friendly towards him, being to some extent a vassal, and their people trading together. He sent tribute every year to the King of Kongo, and trade was carried on at the port of Luanda between the Portuguese and the people of Angola by permission of the King of Kongo. Slaves were bought and exchanged for other merchandise, all being sent to the island of São Tomé*. … Trade becoming successful, they began to send vessels themselves from Lisbon to Angola, and also a governor, Paulo Dias de Novais by name. … To this Paulo Dias, Dom Sebastião, King of Portugal, granted the power of conquering thirty-three leagues of country … where he was to take all he could gain for himself and his heirs."],
    "Filippo Pigafetta, Italian writer, A Report of the Kingdom of Kongo, 1591, based on the accounts of Duarte Lopes, a Portuguese merchant who lived in Kongo in the 1570s and 1580s",
    "Translated by Margarite Hutchinson (1881); names modernized; adapted",
    footnotes=[{"mark": "*", "text": "a Portuguese island colony in the Gulf of Guinea, off the coast of Central Africa"}, {"mark": "**", "text": "here, the kingdom of Ndongo, south of Kongo; the Portuguese named it after its ruler's title, ngola"}],
    glossary=[{"t": "vassal", "d": "a lesser ruler who owes loyalty and payments to a stronger one"},
              {"t": "tribute", "d": "payments made to show loyalty to a more powerful ruler"},
              {"t": "leagues", "d": "an old distance unit; 33 leagues is roughly 100 miles"}]),

"P8": P([
    "Although a kingdom may be enriched by gifts received, or by purchase taken from some other nations, yet these are things uncertain and of small consideration when they happen. The ordinary means therefore to increase our wealth and treasure is by foreign trade, wherein we must ever observe this rule: to sell more to strangers yearly than we consume of theirs in value.",
    "For suppose that when this kingdom is plentifully served with the cloth, lead, tin, iron, fish and other native commodities, we do yearly export the overplus to foreign countries to the value of twenty-two hundred thousand pounds*, by which means we are enabled beyond the seas to buy and bring in foreign wares for our use and consumption to the value of twenty hundred thousand pounds. By this order duly kept in our trading, we may rest assured that the kingdom shall be enriched yearly two hundred thousand pounds, which must be brought to us in so much treasure, because that part of our stock which is not returned to us in wares must necessarily be brought home in treasure."],
    "Thomas Mun, English merchant and director of the English East India Company, England's Treasure by Foreign Trade, written about 1630 and published in 1664",
    "Spelling modernized; adapted",
    footnotes=[{"mark": "*", "text": "pounds sterling, English money"}],
    glossary=[{"t": "purchase", "d": "here, wealth seized from others (loot), not buying"}, {"t": "strangers", "d": "foreigners"}, {"t": "treasure", "d": "gold and silver"}, {"t": "wares", "d": "goods for sale"},
              {"t": "overplus", "d": "the extra goods left after the kingdom's own needs are met"},
              {"t": "stock", "d": "the nation's total wealth"}]),

"P9": P([
    "The Dutch began their career in the East with no idea other than that of buying cheap and selling dear; their ideas and aims were purely commercial. The experience of a few years taught them that in a country like Java they could not deal satisfactorily with individual traders and that they must deal with governments. They were forced, before they knew it, to become politicians, seeking their commercial ends through diplomatic channels, and warriors, upholding the gains that had been given them by treaty. …",
    "The series of instructions to the Governors General … bade the chief executive in Asia never to make war unless forced. … It seems to have been morally impossible for the Dutch officials to obey these directions in the face of all the temptations to break them. Men of vigor, like Governor General Coen*, who did much to shape the Company's military policy in its early period, came to the conclusion that trade and war were inseparable. … Coen wrote to the directors in 1614 \"that trade in Asia must be conducted and maintained under protection and favor of your own weapons, and that the weapons must be supplied from the profits enjoyed by the trade, so that trade cannot be maintained without war or war without trade.\""],
    "Clive Day, historian at Yale University, The Policy and Administration of the Dutch in Java, published in 1904",
    "Coen's letter translated from Dutch by Clive Day; \"India\" changed to \"Asia\" in Day's text and Coen's letter, to match its meaning; adapted",
    footnotes=[{"mark": "*", "text": "Jan Pieterszoon Coen (1587–1629), leader of the Dutch East India Company (VOC) in Asia, who founded the Dutch base at Batavia (today's Jakarta) on Java in 1619"}],
    glossary=[{"t": "bade", "d": "ordered"}, {"t": "the Company", "d": "the Dutch East India Company (VOC), a joint-stock company chartered in 1602"},
              {"t": "Java", "d": "a large island in today's Indonesia"}, {"t": "inseparable", "d": "unable to be pulled apart"}]),

"P10": P([
    "With respect to books which were not written by the sages … which alarm the age, and astonish the common people … these all contain strange teachings which should be rooted out. …",
    "From of old three teachings have been handed down. Besides the teaching of the learned [Confucianism], there are those of Dao and Fo [Daoism and Buddhism]. …",
    "The teaching of the Western Ocean, which honors Tianzhu*, ranks also among those that are corrupt; but because these men understand mathematics, therefore the government employs them: of this you ought to be aware. To walk in these by-roads and deceive the people is what the law will not excuse. …",
    "Soldiers and people! act according to the sacred instructions of the late emperor**; and stop the progress of these strange sects as you would that of floods, fires, robbers, and thieves. Indeed the injury of floods, fires, robbers, and thieves ends with the body; but that of false religions reaches the human heart."],
    "The Yongzheng Emperor of Qing China, Amplified Instructions on the Sacred Edict, 1724, explaining its seventh rule, \"Degrade strange religions, in order to exalt the orthodox [Confucian] teaching\"; these instructions were read aloud to the public twice a month across the empire",
    "Translated by William Milne (1817); names modernized; adapted",
    footnotes=[{"mark": "*", "text": "\"Lord of Heaven,\" the Chinese name for the Christian God; \"the teaching of the Western Ocean\" is Roman Catholic Christianity, brought by Jesuit missionaries"},
               {"mark": "**", "text": "the Kangxi Emperor (ruled 1661–1722), who issued the original Sacred Edict in 1670"}],
    glossary=[{"t": "sages", "d": "wise teachers of the past, especially Confucius"},
              {"t": "sects", "d": "religious groups outside the approved teaching"}, {"t": "by-roads", "d": "side paths; wrong ways"}]),

"P11": P([
    "In the first place, the efforts of the Spaniards to suppress not only the religious beliefs but also the ancient habits and customs of the Indians in other respects, and to make them conform to European methods of living, created friction between the two races*. The Indians, however, continued well grounded in their native religious beliefs and practices, and the Spaniards found it practically impossible to suppress them either by the number of missionaries brought in, or by the severity of the punishments inflicted. In 1675 these \"superstitious practices\" reached such alarming extremes that Governor Treviño determined to stamp them out for good. Having captured forty-seven medicine men, who were alleged to be guilty of sorcery and witchcraft, he hanged three of them … and inflicted severe punishment upon the others, among whom was a certain native named Popé. …",
    "On being released from captivity in 1675, he returned to his pueblo, full of resentment for the Spaniards. He at once began making preparations for a general revolt. … Other influences, such as the belief that the Spaniards could all be driven out of the country, and the almost universal desire to return to their ancient customs, all operated to make the revolt of the Indians general."],
    "Charles W. Hackett, historian, \"The Revolt of the Pueblo Indians of New Mexico in 1680,\" published in 1911, based on Spanish colonial records",
    "Adapted",
    footnotes=[{"mark": "*", "text": "Hackett, writing in 1911, uses \"Indians\" for the Pueblo peoples and \"two races\" for Pueblos and Spaniards. \"Superstitious practices\" was the Spanish officials' label for Pueblo religion."}],
    glossary=[{"t": "pueblo", "d": "a town of the Pueblo peoples of what is now New Mexico"},
              {"t": "medicine men", "d": "Pueblo religious leaders and healers"}, {"t": "general", "d": "widespread; involving nearly everyone"}]),

"P12": P([
    "The Sultan's hall was crowded with people, among whom were several officers of high rank. Besides these there were all the troopers of the Imperial guard … and a large force of Janissaries*; but there was not in all that great assembly a single man who owed his position to anything except his valor and his merit. No distinction is attached to birth among the Turks; the respect to be paid to a man is measured by the position he holds in the public service. … In making his appointments the Sultan pays no regard to any claims on the score of wealth or rank … he considers each case on its own merits, and examines carefully into the character, ability, and disposition of the man whose promotion is in question. It is by merit that men rise in the service. … Those who receive the highest offices from the Sultan are for the most part the sons of shepherds or herdsmen, and so far from being ashamed of their parentage, they actually glory in it. …",
    "This is the reason that they are successful in their undertakings, that they lord it over others, and are daily extending the bounds of their empire. These are not our ideas; with us there is no opening left for merit; birth is the standard for everything; the prestige of birth is the sole key to advancement in the public service."],
    "Ogier Ghiselin de Busbecq, ambassador of the Habsburg ruler Ferdinand I to the court of Ottoman Sultan Suleiman I, private letter written in 1555",
    "Translated by C. T. Forster and F. H. B. Daniell (1881); adapted",
    footnotes=[{"mark": "*", "text": "elite Ottoman infantry soldiers who served the sultan"}],
    glossary=[{"t": "merit", "d": "skill and good work"}, {"t": "prestige of birth", "d": "the respect a person gets for coming from a noble family"},
              {"t": "Turks", "d": "Busbecq's word for the Ottomans"}]),

"P13": P([
    "One of the great gifts which His Majesty the Shahanshah* made at the beginning of this year was the remission of the jizya** throughout India. … In spite of the disapproval of statesmen, and of the great revenue, and of much chatter on the part of the ignorant, this sublime decree was issued. …",
    "When this tax was imposed in former times … the reason for it was that they [earlier rulers], on account of heart-rooted hatred, were set on the contempt and destruction of those of other faiths. … At the present day, when … those who belong to other religions have, like those of one mind and one religion, bound up the waist of devotion and service, and exert themselves for the advancement of the empire, how should they be classed with that old faction [non-Muslims seen as enemies in earlier times] and be the subjects of contempt? Moreover the main cause of levying the tax in old times was the neediness of the rulers. At this day, when there are thousands of treasures in the storehouses of the world-wide government … why should a just and wise mind apply itself to collecting this tax?"],
    "Abu'l-Fazl, adviser and official historian of the Mughal emperor Akbar, the Akbarnama, written in the 1590s, describing a decree of 1564",
    "Translated by Henry Beveridge (1907–1912); adapted",
    footnotes=[{"mark": "*", "text": "\"King of kings,\" a title for Akbar (ruled 1556–1605)"},
               {"mark": "**", "text": "a tax that Islamic states placed on non-Muslim subjects; in Mughal India most of the people who paid it were Hindus"}],
    glossary=[{"t": "remission", "d": "canceling a tax or debt"}, {"t": "bound up the waist of devotion and service", "d": "worked loyally"}, {"t": "decree", "d": "an official order from a ruler"},
              {"t": "revenue", "d": "money the government collects"}]),

"P15": {"type": "image",
    "src": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Nanban-Screens-by-Kano-Naizen-c1600.png/1280px-Nanban-Screens-by-Kano-Naizen-c1600.png",
    "width": 1280, "height": 554,
    "alt": "A wide Japanese folding screen painted on gold showing a large European sailing ship, a crowd of Portuguese merchants with servants carrying goods, and priests in dark robes greeting them near Japanese shops.",
    "caption": "On the left, a large Portuguese carrack (a three-masted ocean-going ship) lies at anchor while small boats bring people and cargo ashore. In the center, Portuguese merchants in tall hats and baggy trousers walk in a procession; attendants, several of them African (servants or enslaved people), carry chests and goods. On the right, Catholic priests in black and gray robes come out to greet them beside Japanese shops and a building used as a church.",
    "attribution": "Kanō Naizen, Japanese painter, Arrival of the Southern Barbarians*, folding screen (ink, color, and gold leaf on paper), c. 1600",
    "credit": "Kobe City Museum, Japan. Public domain image via Wikimedia Commons. *\"Southern Barbarians\" (Nanban) was the Japanese name for the Portuguese and Spanish, who came to Japan from the south.",
    "description": "A very wide painting on a gold background. A dark three-masted European ship with flags sits in the water at left, with sailors in its rigging. Along the beach in the middle, a parade of Portuguese merchants wearing hats and puffed trousers is led by a richly dressed man under a parasol; attendants carry boxes, bundles, and a covered chair, and a white horse is led along. At right, Jesuit priests in black robes and friars in gray meet the arrivals near a row of Japanese shops, while Japanese people look on.",
    "glossary": [{"t": "carrack", "d": "a large sailing ship used by the Portuguese and Spanish for long ocean voyages"},
                 {"t": "Jesuits", "d": "an order of Catholic priests known for missionary work and education"}]},

"P16": {"type": "bar",
    "title": "Estimated Arrivals of Enslaved Africans Carried Directly from Africa, Selected Regions of the Americas",
    "categories": ["Brazil", "British\nCaribbean", "French\nCaribbean", "Spanish\nAmericas", "Dutch\nAmericas", "Mainland\nN. America"],
    "series": [{"name": "1601–1700 (thousands)", "values": [784, 310, 39, 226, 124, 15]},
               {"name": "1701–1800 (thousands)", "values": [1989, 1813, 995, 146, 295, 295]}],
    "yLabel": "Thousands of people",
    "text": "Estimates count people who survived the voyage from Africa and landed in each region. They do not count later voyages between ports in the Americas. Regions follow the database's categories; mainland North America is the area that later became the United States and Canada. The second period extends past 1750.",
    "source": "Trans-Atlantic Slave Trade Database estimates, Slave Voyages (slavevoyages.org), Emory University"},

"P14": {"type": "pair", "items": [
    item("Source 1", [
        "The discovery of America, and that of a passage to the East Indies by the Cape of Good Hope, are the two greatest and most important events recorded in the history of mankind. … By uniting in some measure the most distant parts of the world, by enabling them to relieve one another's wants, to increase one another's enjoyments, and to encourage one another's industry, their general tendency would seem to be beneficial. To the natives, however, both of the East and West Indies, all the commercial benefits which can have resulted from those events have been sunk and lost in the dreadful misfortunes which they have occasioned. These misfortunes, however, seem to have arisen rather from accident than from anything in the nature of those events themselves. At the particular time when these discoveries were made, the superiority of force happened to be so great on the side of the Europeans, that they were enabled to commit with impunity every sort of injustice in those remote countries. …"],
        "Adam Smith, Scottish economist, The Wealth of Nations, 1776",
        "Adapted",
        glossary=[{"t": "East and West Indies", "d": "Asia and the Americas"}, {"t": "with impunity", "d": "without being punished"}]),
    item("Source 2", [
        "The discovery of gold and silver in America, the extirpation, enslavement and entombment in mines of the native population, the beginning of the conquest and looting of the East Indies, the turning of Africa into a [hunting ground for enslaved people], signalled the rosy dawn of the era of capitalist production. … On their heels treads the commercial war of the European nations, with the globe for a theatre. …",
        "These methods [colonies, national debt, taxes, and tariffs] depend in part on brute force, for example, the colonial system. But they all employ the power of the State, the concentrated and organized force of society, to hasten … the process of transformation of the feudal mode of production into the capitalist mode. … Force is the midwife of every old society pregnant with a new one."],
        "Karl Marx, German philosopher and critic of capitalism, Capital, Volume 1, 1867",
        "Translated by Samuel Moore and Edward Aveling (1887); offensive 1887 wording replaced in brackets; adapted",
        glossary=[{"t": "extirpation", "d": "destruction; wiping out"}, {"t": "entombment in mines", "d": "being worked to death in mines"},
                  {"t": "rosy dawn", "d": "Marx is being sarcastic: the \"bright beginning\" was actually violent"},
                  {"t": "capitalist production", "d": "an economy in which private owners invest money to make profit"}, {"t": "feudal mode of production", "d": "an older economy of lords and peasants"}])]},
}

STIM = {k: v for k, v in STIM.items() if v is not None}
