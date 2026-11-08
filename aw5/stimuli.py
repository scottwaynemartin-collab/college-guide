# AP World Unit 5 sources. Texts follow the public-domain editions saved in aw5/sources/raw/ and
# documented in aw5/sources/*.md. Cuts are marked with ellipses; bracketed words are clarifications.
# OCR slips in the scans were corrected against a second scan where one exists (see the .md files).
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

STIM = {
# ============================== EXAM ==============================
"X1": P([
    "The representatives of the French people, organized in National Assembly, considering that ignorance, forgetfulness or contempt of the rights of man are the sole causes of the public miseries and of the corruption of governments, have resolved to set forth in a solemn declaration the natural, inalienable, and sacred rights of man. … In consequence, the National Assembly recognizes and declares, in the presence and under the auspices of the Supreme Being, the following rights of man and citizen.",
    "1. Men are born and remain free and equal in rights. Social distinctions can be based only upon public utility.",
    "2. The aim of every political association is the preservation of the natural and imprescriptible rights of man. These rights are liberty, property, security, and resistance to oppression.",
    "3. The source of all sovereignty is essentially in the nation; no body, no individual can exercise authority that does not proceed from it in plain terms. …",
    "6. Law is the expression of the general will. All citizens have the right to take part personally or by their representatives in its formation. It must be the same for all, whether it protects or punishes. All citizens being equal in its eyes, are equally eligible to all public dignities, places, and employments, according to their capacities, and without other distinction than that of their virtues and their talents. …",
    "10. No one ought to be disturbed on account of his opinions, even religious, provided their manifestation does not derange the public order established by law. …",
    "16. Any society in which the guarantee of the rights is not secured or the separation of powers not determined has no constitution at all."],
    "Declaration of the Rights of Man and of the Citizen, adopted by the National Assembly of France, August 26, 1789",
    "Translated by Frank Maloy Anderson (1904); adapted",
    glossary=[{"t": "imprescriptible", "d": "cannot be taken away"},
              {"t": "sovereignty", "d": "the highest power to rule"},
              {"t": "public utility", "d": "the good of everyone"},
              {"t": "dignities, places, and employments", "d": "government offices and jobs"},
              {"t": "derange", "d": "disturb"}]),

"X2": P([
    "Citizens, it is not enough to have expelled from your country the barbarians* who have for ages stained it with blood—it is not enough to have curbed the factions which, succeeding each other by turns, sported with a phantom of liberty which France exposed to their eyes. It is become necessary, by a last act of national authority, to ensure for ever the empire of liberty in the country which has given us birth. It is necessary to deprive an inhuman government, which has hitherto held our minds in a state of the most humiliating torpitude, of every hope of being enabled again to enslave us. Finally, it is necessary to live independent, or die. Independence or Death! …",
    "We have dared to be free—let us continue free by ourselves, and for ourselves. … What are the people who have fought us? what people would reap the fruits of our labours? and what a dishonourable absurdity, to conquer to be slaves! …",
    "Let us, at the same time, take care, lest a spirit of proselytism should destroy the work—let our neighbours breathe in peace—let them live peaceably under the shield of those laws which they have framed for themselves; let us beware of becoming revolutionary fire-brands—of creating ourselves the legislators of the Antilles—of considering as a glory the disturbing the tranquility of the neighbouring islands. …",
    "Swear then to live free and independent, and to prefer death to every thing that would lead to replace you under the yoke."],
    "Jean-Jacques Dessalines, general in chief of the army that drove the French out of Saint-Domingue, proclamation declaring the independence of Haiti, Gonaïves, January 1, 1804",
    "English translation printed in Marcus Rainsford, An Historical Account of the Black Empire of Hayti (London, 1805); adapted",
    footnotes=[{"mark": "*", "text": "\"Barbarians\" is the translated term Dessalines uses here for the French colonizers."}],
    glossary=[{"t": "factions", "d": "rival groups"}, {"t": "torpitude", "d": "a dull, numb state (an old form of \"torpor\")"},
              {"t": "proselytism", "d": "trying to win other people over to your cause"},
              {"t": "fire-brands", "d": "troublemakers; people who start fights, the way a burning stick starts a fire"},
              {"t": "the Antilles", "d": "the islands of the Caribbean"}]),

"X3": {"type": "bar",
    "title": "Estimated Shares of World Manufacturing Output, 1750 and 1900",
    "categories": ["China", "India–\nPakistan", "Japan", "Russia", "United\nKingdom", "United\nStates"],
    "series": [{"name": "1750 (percent of world total)", "values": [32.8, 24.5, 3.8, 5.0, 1.9, 0.1]},
               {"name": "1900 (percent of world total)", "values": [6.2, 1.7, 2.4, 8.8, 18.5, 23.6]}],
    "yLabel": "Percent of world manufacturing",
    "text": "The figures are an economic historian's estimates of each country's or region's share of all the manufactured goods made in the world, including goods made by hand. \"India–Pakistan\" is the historian's label for the lands that are now India, Pakistan, and Bangladesh. Only some countries are shown.",
    "source": "Paul Bairoch, \"International Industrialization Levels from 1750 to 1980,\" Journal of European Economic History 11 (1982)"},

"X4": {"type": "pair", "items": [
    item("Source 1", [
        "I have visited many factories, both in Manchester and in the surrounding districts, during a period of several months, entering the spinning rooms, unexpectedly, and often alone, at different times of the day, and I never saw a single instance of corporal chastisement inflicted on a child, nor indeed did I ever see children in ill-humour. They seemed to be always cheerful and alert, taking pleasure in the light play of their muscles,—enjoying the mobility natural to their age. The scene of industry, so far from exciting sad emotions in my mind, was always exhilarating. … The work of these lively elves seemed to resemble a sport, in which habit gave them a pleasing dexterity. … As to exhaustion by the day's work, they evinced no trace of it on emerging from the mill in the evening; for they immediately began to skip about any neighbouring play-ground, and to commence their little amusements with the same alacrity as boys issuing from a school."],
        "Andrew Ure, Scottish chemist and writer on manufacturing, The Philosophy of Manufactures, 1835",
        "Adapted",
        glossary=[{"t": "corporal chastisement", "d": "physical punishment, such as hitting"},
                  {"t": "dexterity", "d": "skill with the hands"}, {"t": "evinced", "d": "showed"},
                  {"t": "alacrity", "d": "cheerful eagerness"}]),
    item("Source 2", [
        "Further, the slavery in which the bourgeoisie holds the proletariat chained, is nowhere more conspicuous than in the factory system. Here ends all freedom in law and in fact. The operative must be in the mill at half-past five in the morning; if he comes a couple of minutes too late, he is fined; if he comes ten minutes too late, he is not let in until breakfast is over, and a quarter of the day's wages is withheld, though he loses only two and one-half hours' work out of twelve. He must eat, drink, and sleep at command. … The despotic bell calls him from his bed, his breakfast, his dinner.",
        "What a time he has of it, too, inside the factory! Here the employer is absolute law-giver; he makes regulations at will, changes and adds to his codex at pleasure, and even, if he inserts the craziest stuff, the courts say to the working-man: \"You were your own master, no one forced you to agree to such a contract if you did not wish to; but now, when you have freely entered into it, you must be bound by it.\""],
        "Friedrich Engels, German writer who worked for his family's cotton firm in Manchester, The Condition of the Working-Class in England in 1844, published in German in 1845",
        "Translated by Florence Kelley Wischnewetzky (1887); adapted",
        glossary=[{"t": "bourgeoisie", "d": "the owners of factories and businesses"},
                  {"t": "proletariat", "d": "industrial workers who earn wages and own no property"},
                  {"t": "operative", "d": "a factory worker"}, {"t": "despotic", "d": "acting like a tyrant"},
                  {"t": "codex", "d": "set of rules"}])]},

"X5": P([
    "With the fall of feudalism and the inauguration of a new regime the Meiji Government effected reforms in old usages, one of the earliest being liberty of trade for the people. … a craftsman being now at liberty to select any profession according to his inclination, provided he kept within the limits of law and order. There was no necessity for him to become a member of a trade-guild or union, or to serve any stated number of years as an apprentice. …",
    "Foreign imports, which had been introduced to a most restricted amount in the centuries preceding the Restoration, now advanced with leaps and bounds. … Especially was this the case in 1872, when intense activity was displayed in the introduction of foreign methods. Model factories for silk reeling, spinning, and cement and brick manufacture were established, such as the Tomioka Silk Filature … An engineering college … on modern lines was established, in which all branches of applied science, such as civil and mechanical engineering, naval architecture, and electrical engineering, were taught.",
    "… The mission sent to the [Vienna] Exhibition [of 1873] consisted of over seventy Government officials, and also a German scientist, Dr. Wagner, as adviser … Some of the most able among the members of the mission were also dispatched to different European countries, to study the various scientific subjects bearing on industry. The result was the introduction of the latest knowledge in all branches, and the importation from abroad of new tools and machines."],
    "Junichiro Suzuki, Japanese writer on industry, \"A Résumé of the History of Japanese Industries,\" in Fifty Years of New Japan, essays by Japanese leaders compiled by Count Ōkuma Shigenobu, former prime minister of Japan",
    "English edition edited by Marcus B. Huish (London, 1909); adapted",
    glossary=[{"t": "inauguration of a new regime", "d": "the start of a new government"},
              {"t": "usages", "d": "customs"}, {"t": "silk reeling", "d": "unwinding silk thread from cocoons"},
              {"t": "filature", "d": "a silk-reeling factory"},
              {"t": "the Restoration", "d": "the Meiji Restoration of 1868, when a new government took power in the emperor's name"}]),

"X6": P([
    "All the world knows that in the first days of the Ottoman Monarchy, the glorious precepts of the Koran and the Laws of the Empire were always honoured. The Empire in consequence increased in strength and greatness. … In the last 150 years a succession of accidents and divers causes have arisen which have brought about a disregard for the sacred code of Laws, … and the former strength and prosperity have changed into weakness and poverty. …",
    "… we deem it right to seek by new institutions to give to the Provinces composing the Ottoman Empire the benefit of a good Administration. These institutions must be principally carried out under 3 heads, which are:—1. The guarantees insuring to our subjects perfect security for life, honour, and fortune. 2. A regular system of assessing and levying Taxes. 3. An equally regular system for the levy of Troops and the duration of their service. …",
    "These Imperial concessions shall extend to all our subjects, of whatever Religion or sect they may be; they shall enjoy them without exception. …",
    "… this Imperial Rescript shall be published at Constantinople, and in all places of our Empire, and shall be officially communicated to all the Ambassadors of the friendly Powers resident at Constantinople, that they may be witnesses to the granting of these Institutions …"],
    "Imperial decree of Gülhane* (Hatt-ı Şerif), issued in the name of the Ottoman sultan Abdülmecid I, Constantinople (Istanbul), November 3, 1839",
    "English translation printed in Edward Hertslet, The Map of Europe by Treaty, vol. 2 (London, 1875); adapted",
    footnotes=[{"mark": "*", "text": "Gülhane (\"Rose House\") was a park beside the sultan's palace in Istanbul, where the decree was first read aloud."}],
    glossary=[{"t": "precepts", "d": "rules or teachings"}, {"t": "divers", "d": "various"},
              {"t": "fortune", "d": "property and wealth"}, {"t": "levy of Troops", "d": "drafting soldiers"},
              {"t": "Rescript", "d": "an official order from a ruler"}]),

"X7": P([
    "As every individual, therefore, endeavours as much as he can, both to employ his capital in the support of domestic industry, and so to direct that industry that its produce may be of the greatest value; every individual necessarily labours to render the annual revenue of the society as great as he can. He generally, indeed, neither intends to promote the public interest, nor knows how much he is promoting it. … he intends only his own gain; and he is in this, as in many other cases, led by an invisible hand to promote an end which was no part of his intention. …",
    "It is the maxim of every prudent master of a family, never to attempt to make at home what it will cost him more to make than to buy. The tailor does not attempt to make his own shoes, but buys them of the shoemaker. … What is prudence in the conduct of every private family, can scarce be folly in that of a great kingdom. If a foreign country can supply us with a commodity cheaper than we ourselves can make it, better buy it of them with some part of the produce of our own industry, employed in a way in which we have some advantage. …",
    "Consumption is the sole end and purpose of all production; and the interest of the producer ought to be attended to, only so far as it may be necessary for promoting that of the consumer. … But in the mercantile system, the interest of the consumer is almost constantly sacrificed to that of the producer."],
    "Adam Smith, Scottish philosopher and economist, An Inquiry into the Nature and Causes of the Wealth of Nations, 1776",
    "Adapted",
    glossary=[{"t": "capital", "d": "money or goods used to start or run a business"},
              {"t": "domestic industry", "d": "businesses inside one's own country"},
              {"t": "annual revenue of the society", "d": "the total wealth a country produces in a year"},
              {"t": "maxim", "d": "a rule of good sense"}, {"t": "prudent", "d": "careful and wise"},
              {"t": "mercantile system", "d": "mercantilism: policies that limit imports so a country sells more than it buys"}]),

"X8": {"type": "image",
    "src": "https://upload.wikimedia.org/wikipedia/commons/c/c8/Dore_London.jpg",
    "width": 650, "height": 550,
    "alt": "An engraving seen through a dark brick railway arch, looking down on long rows of crowded brick houses with small walled yards full of people and hanging laundry, while a steam train crosses a viaduct in the distance.",
    "caption": "A dark brick arch frames the scene. Below, long rows of brick row houses stand close together, each with a tiny walled yard. The yards are crowded with people, and laundry hangs on lines. Chimneys crowd the rooftops. In the distance at the top, a steam train crosses a viaduct held up by arches, and smoke drifts across the sky.",
    "attribution": "Over London—by Rail, wood engraving by Adolphe François Pannemaker, French engraver, after a drawing by Gustave Doré, French artist, from the book London: A Pilgrimage, by Doré and the English journalist Blanchard Jerrold, published in London in 1872",
    "credit": "Public domain image via Wikimedia Commons.",
    "description": "The scene is seen from high up, framed by a dark brick arch. Below, long rows of nearly identical brick houses stretch into the distance. Each house has a small yard closed in by walls. The yards are crowded with women, men, and children, and laundry hangs between them. Dozens of chimneys rise from the roofs. In the distance at the top, a railway viaduct held up by arches crosses the scene, with a train and smoke drifting across the sky.",
    "glossary": [{"t": "viaduct", "d": "a long bridge made of arches that carries a railway over a valley or a crowded area"}]},

# ============================== PRACTICE ==============================
"P1": P([
    "Man is born free; and everywhere he is in chains. One thinks himself the master of others, and still remains a greater slave than they. How did this change come about? I do not know. What can make it legitimate? That question I think I can answer. …",
    "\"The problem is to find a form of association which will defend and protect with the whole common force the person and goods of each associate, and in which each, while uniting himself with all, may still obey himself alone, and remain as free as before.\" This is the fundamental problem of which the Social Contract provides the solution. …",
    "\"Each of us puts his person and all his power in common under the supreme direction of the general will, and, in our corporate capacity, we receive each member as an indivisible part of the whole.\""],
    "Jean-Jacques Rousseau, philosopher born in Geneva who lived mostly in France, The Social Contract, 1762",
    "Translated by G. D. H. Cole (1913); adapted",
    glossary=[{"t": "legitimate", "d": "rightful; fairly and lawfully in power"},
              {"t": "association", "d": "a group that people join together"},
              {"t": "general will", "d": "what the whole people wants for the common good"},
              {"t": "corporate capacity", "d": "acting together as one body"}]),

"P2": {"type": "pair", "items": [
    item("Source 1", [
        "Consider, I address you as a legislator, whether, when men contend for their freedom, and to be allowed to judge for themselves, respecting their own happiness, it be not inconsistent and unjust to subjugate women, even though you firmly believe that you are acting in the manner best calculated to promote their happiness? Who made man the exclusive judge, if woman partake with him the gift of reason?",
        "In this style, argue tyrants of every denomination from the weak king to the weak father of a family; they are all eager to crush reason. … Do you not act a similar part, when you force all women, by denying them civil and political rights, to remain immured in their families groping in the dark?"],
        "Mary Wollstonecraft, English writer, A Vindication of the Rights of Woman, 1792, from the book's dedication to Charles-Maurice de Talleyrand, a French politician and former bishop who had presented a plan for national education to France's revolutionary assembly in 1791",
        "Adapted",
        glossary=[{"t": "contend", "d": "fight or argue"}, {"t": "subjugate", "d": "keep under control by force"},
                  {"t": "partake", "d": "share"}, {"t": "of every denomination", "d": "of every kind"},
                  {"t": "immured", "d": "shut in, as if behind walls"}]),
    item("Source 2", [
        "We hold these truths to be self-evident: that all men and women are created equal; that they are endowed by their Creator with certain inalienable rights; that among these are life, liberty, and the pursuit of happiness; that to secure these rights governments are instituted, deriving their just powers from the consent of the governed. …",
        "The history of mankind is a history of repeated injuries and usurpations on the part of man toward woman, having in direct object the establishment of an absolute tyranny over her. …",
        "He has never permitted her to exercise her inalienable right to the elective franchise.\nHe has compelled her to submit to laws, in the formation of which she had no voice. …\nHe has made her, if married, in the eye of the law, civilly dead.\nHe has taken from her all right in property, even to the wages she earns."],
        "Declaration of Sentiments, approved at the women's rights convention at Seneca Falls, New York, United States, July 1848; written mainly by Elizabeth Cady Stanton",
        "As printed in History of Woman Suffrage, vol. 1 (1881); adapted",
        glossary=[{"t": "inalienable", "d": "cannot be taken away"},
                  {"t": "usurpations", "d": "unfair seizures of power"},
                  {"t": "the elective franchise", "d": "the right to vote"},
                  {"t": "civilly dead", "d": "having no legal rights of her own"}])]},

"P3": P([
    "As we consider the various classes of which the State is composed, we are convinced that the laws of our empire which have wisely provided for the upper and middle classes, and have fixed with precision their rights and obligations, have not reached the same degree of success in relation to the peasants bound to the soil, who, either through ancient laws or custom, have been hereditarily subjected to the authority of the landlords. …",
    "It was to the nobility themselves that, in conformity to their own wishes, we reserved the right of formulating the provisions for the new organization of the peasants. … Our confidence has not been deceived. We have found the nobility … ready to make … the voluntary sacrifices of their rights so far as the personal servitude of the peasants is concerned. …",
    "The peasants now bound to the soil shall, within the term fixed by the law, be vested with the full rights of freemen. The landed proprietors, while they shall retain all the rights of ownership over all the lands now belonging to them, shall transfer to the peasants, in return for a rent fixed by law, the full enjoyment of their cottages, farm buildings, and gardens. Furthermore, in order to assure to the peasants their subsistence and enable them to meet their obligations toward the State, the landlords shall turn over to the peasants a quantity of arable and other land provided for in the regulations above mentioned. In return for these allotments the peasant families shall be required to pay rent to the landlords, as fixed by the provisions of the law."],
    "Tsar Alexander II of Russia, manifesto freeing the serfs, March 1861",
    "Translation printed in James Harvey Robinson and Charles A. Beard, Readings in Modern European History, vol. 2 (1908); adapted",
    glossary=[{"t": "peasants bound to the soil", "d": "serfs: farmers who could not leave the land and owed labor or payments to a landlord"},
              {"t": "hereditarily", "d": "passed down from parents to children"},
              {"t": "in conformity to", "d": "following"},
              {"t": "personal servitude", "d": "the serfs' duty to serve their landlord"},
              {"t": "arable", "d": "good for growing crops"},
              {"t": "subsistence", "d": "enough food and goods to stay alive"},
              {"t": "allotments", "d": "plots of land given out"}]),

"P4": P([
    "… We do not even preserve the vestiges of what once we were; we are not Europeans, we are not Indians, but an intermediate species between the aborigines and the Spaniards—Americans by birth and Europeans in right, we are placed in the dilemma of disputing with the natives our titles of possession and maintaining ourselves in the country where we were born, against the opposition of the invaders. …",
    "The people of America having been held under the triple yoke of ignorance, tyranny and vice, have not been in a position to acquire either knowledge, power or virtue. …",
    "Atrocious, godless slavery covered with its sable mantle the land of Venezuela. … Yea, those who were slaves are now free. … To emphasize the justice, the necessity, the beneficent results of this measure, is superfluous, when you know the history of the Helots, Spartacus* and Haiti; when you know that one can not be free and enslaved at the same time, unless in violation of the laws of nature and the civil and political laws. … I implore of you the confirmation of the absolute freedom of the slaves, as I would beg for my life and the life of the Republic."],
    "Simón Bolívar, leader of the independence wars in northern South America, address to the Congress of Angostura, Venezuela, February 15, 1819",
    "Translated by Francisco Javier Yanes; from the edition printed for the government of Venezuela (1919); adapted",
    footnotes=[{"mark": "*", "text": "The Helots were enslaved farm workers in ancient Sparta; Spartacus led a revolt of enslaved people against ancient Rome."}],
    glossary=[{"t": "vestiges", "d": "traces"}, {"t": "Indians / aborigines / natives", "d": "Bolívar's words for the Indigenous peoples of the Americas"},
              {"t": "titles of possession", "d": "legal claims to own the land"},
              {"t": "the invaders", "d": "here, the Spanish, whom Bolívar treats as outsiders"},
              {"t": "yoke", "d": "a heavy burden, like the wooden bar placed on oxen"},
              {"t": "sable mantle", "d": "black cloak"}, {"t": "superfluous", "d": "not needed"}]),

"P5": P([
    "Young Italy is a brotherhood of Italians who believe in a law of progress and duty, and are convinced that Italy is destined to become one nation. … They join this association with the firm intention of consecrating both thought and action to the great aim of reconstituting Italy as one independent sovereign nation of free men and equals. …",
    "Young Italy is republican and unitarian*—republican, because theoretically every nation is destined, by the law of God and humanity, to form a free and equal community of brothers; and the republican government is the only form of government that insures this future. …",
    "Young Italy is unitarian, because, without unity there is no true nation; because, without unity there is no real strength; and Italy, surrounded as she is by powerful, united, and jealous nations, has need of strength above all things; because federalism, by reducing her to the political impotence of Switzerland, would necessarily place her under the influence of one of the neighboring nations. …"],
    "Giuseppe Mazzini, Italian nationalist, General Instructions for the Members of Young Italy, a secret society he founded in 1831",
    "English translation from Life and Writings of Joseph Mazzini (1864), as printed in Robinson and Beard, Readings in Modern European History, vol. 2 (1908); adapted",
    footnotes=[{"mark": "*", "text": "wanting one central government for all of Italy, not a loose union (federation) of separate states"}],
    glossary=[{"t": "consecrating", "d": "dedicating"}, {"t": "reconstituting", "d": "putting back together"},
              {"t": "sovereign", "d": "ruling itself, free of outside control"},
              {"t": "republican", "d": "favoring a government with no king, run by elected leaders"},
              {"t": "impotence", "d": "weakness"}]),

"P6": P([
    "… if the country is denied representation in the Cortes and an authorized voice to cry out against all kinds of abuses, … if, in short, the system, prolific in results of alienating the good will of the natives, is to continue, … we can assert that in a few years the present state of affairs will have been modified completely—and inevitably. There now exists a factor which was formerly lacking—the spirit of the nation has been aroused, and a common misfortune, a common debasement, has united all the inhabitants of the Islands. A numerous enlightened class now exists within and without the Islands, a class created and continually augmented by the stupidity of certain governing powers, which forces the inhabitants to leave the country, to secure education abroad. …",
    "But routine is a declivity down which many governments slide, and routine says that freedom of the press is dangerous. Let us see what History says: uprisings and revolutions have always occurred in countries tyrannized over, in countries where human thought and the human heart have been forced to remain silent."],
    "José Rizal, Filipino writer and reformer, \"The Philippines a Century Hence,\" essay published in 1889–1890 in La Solidaridad, a newspaper of Filipino reformers in Spain",
    "Translated by Charles E. Derbyshire (1912); adapted",
    glossary=[{"t": "the Cortes", "d": "Spain's parliament"}, {"t": "the natives", "d": "here, the Filipino people (the word Spanish officials used)"}, {"t": "alienating", "d": "turning people against"},
              {"t": "debasement", "d": "being treated as lower or worthless"},
              {"t": "augmented", "d": "made larger"}, {"t": "declivity", "d": "downward slope"}]),

"P7": P([
    "Passing to manufactures, we find here the all-prominent fact to be the substitution of the factory for the domestic system, the consequence of the mechanical discoveries of the time. Four great inventions altered the character of the cotton manufacture; the spinning-jenny, patented by Hargreaves in 1770; the water-frame, invented by Arkwright the year before; Crompton's mule introduced in 1779, and the self-acting mule. … None of these by themselves would have revolutionised the industry. But in 1769 … James Watt took out his patent for the steam-engine. Sixteen years later it was applied to the cotton manufacture. … Meanwhile, the iron industry had been equally revolutionised by the invention of smelting by pit-coal … and by the application … of the steam-engine to blast furnaces. …",
    "A further growth of the factory system took place independent of machinery, and owed its origin to the expansion of trade, an expansion which was itself due to the great advance made at this time in the means of communication. The canal system was being rapidly developed throughout the country. … These improved means of communication caused an extraordinary increase in commerce, and to secure a sufficient supply of goods it became the interest of the merchants to collect weavers around them in great numbers, to get looms together in a workshop. … To these latter [the workers] this system meant a change from independence to dependence."],
    "Arnold Toynbee, English historian*, lectures given at Oxford University in 1880–1881, published as Lectures on the Industrial Revolution in England, 1884",
    "Adapted",
    footnotes=[{"mark": "*", "text": "This Arnold Toynbee (1852–1883) helped make the phrase \"Industrial Revolution\" popular. He was the uncle of a later, better-known historian with the same name."}],
    glossary=[{"t": "domestic system", "d": "the older way of making cloth, in which spinners and weavers worked for merchants who supplied the materials"},
              {"t": "mule", "d": "a spinning machine"}, {"t": "smelting by pit-coal", "d": "using coal (coke) instead of charcoal to melt iron out of its ore"},
              {"t": "blast furnaces", "d": "very hot furnaces for making iron"},
              {"t": "means of communication", "d": "here, ways to move goods, such as roads and canals"}]),

"P8": P([
    "It is, unfortunately, a fact which no well-informed Indian official will ignore, that, in many ways, the sources of national wealth in India have been narrowed under British rule. India in the eighteenth century was a great manufacturing as well as a great agricultural country, and the products of the Indian loom supplied the markets of Asia and of Europe. It is, unfortunately, true that the East Indian Company* and the British Parliament, following the selfish commercial policy of a hundred years ago, discouraged Indian manufacturers in the early years of British rule in order to encourage the rising manufactures of England. Their fixed policy, pursued during the last decades of the eighteenth century and the first decades of the nineteenth, was to make India subservient to the industries of Great Britain, and to make the Indian people grow raw produce only, in order to supply material for the looms and manufactories of Great Britain. … prohibitive tariffs excluded Indian silk and cotton goods from England; English goods were admitted into India free of duty or on payment of a nominal duty.",
    "… millions of Indian artisans lost their earnings; the population of India lost one great source of their wealth. … The invention of the power-loom in Europe completed the decline of the Indian industries."],
    "Romesh Chunder Dutt, Indian historian and former official in the British government of India, The Economic History of India under Early British Rule, 1902",
    "Adapted",
    footnotes=[{"mark": "*", "text": "the British East India Company, which ruled much of India until 1858"}],
    glossary=[{"t": "subservient", "d": "serving someone else's needs"}, {"t": "raw produce", "d": "raw materials, such as raw cotton"},
              {"t": "manufactories", "d": "factories"}, {"t": "prohibitive tariffs", "d": "taxes on imports so high that they stop the trade"},
              {"t": "nominal duty", "d": "a very small tax"}, {"t": "artisans", "d": "skilled hand workers"}]),

"P9": P([
    "A steamer of the old kind, capable of carrying three thousand tons, might sail on a voyage so long that she would be compelled to carry twenty-two hundred tons of coal, leaving room for only eight hundred tons of freight; whereas, at the present time, a steamer with the compound engines and all other modern improvements, can make the same voyage and practically reverse the figures—that is, carry twenty-two hundred tons of freight with a consumption of only eight hundred tons of coal. …",
    "In 1860 6d. (12 cents) per bushel was about the lowest rate charged for any length of time for the transportation of bulk grain from New York to Liverpool. … But for the year 1886 the average rate for the same service was 2½d. (5 cents) per bushel. … In like manner, the cost of the ocean transportation of tea from China and Japan, or sugar from Cuba, or coffee from Brazil, has been greatly reduced by the same causes."],
    "David A. Wells, American economist, Recent Economic Changes, 1889",
    "Adapted",
    glossary=[{"t": "steamer", "d": "a steamship"}, {"t": "freight", "d": "goods carried for sale"},
              {"t": "compound engines", "d": "an improved kind of steam engine that uses its steam more than once"},
              {"t": "6d.", "d": "six pence, British money"}, {"t": "bushel", "d": "a unit for measuring grain (about 60 pounds of wheat)"}]),

"P10": P([
    "… Mohammed Ali, in 1819, was led by the advice of Europeans to attempt the introduction of the manufacturing system. … Being persuaded that, with the aid of certain French and Swiss adventurers, it was possible to render Cairo a second Manchester*, he commenced operations with his usual rapidity. French, Italian, Maltese, and Savoyard manufacturers and artisans were employed. … No expense was spared in procuring every description of machinery from Europe. …",
    "… Mohammed Ali was still desirous of rendering Egypt a manufacturing country. … The cultivation of the cotton-plant already promised to become a fertile source of revenue. He now, therefore, determined to manufacture from the raw material. … On the first introduction of European manufactories into Egypt, the Turks in office, and even the people in general, openly evinced their disapprobation. … The Pasha … despised their representations, which arose out of no superior degree of foresight, but from a puerile aversion to every thing new; and his will necessarily prevailed. …",
    "The fellahs employed in the various manipulations have an extreme dislike to the business; being pressed into the mills, they labour only because they are compelled. … Of the twenty-three or twenty-four cotton-mills existing in Egypt, there is not one which has not, at various periods, been accidentally or designedly set on fire."],
    "James Augustus St. John, British writer who traveled in Egypt in 1832–1833, Egypt and Mohammed Ali; or, Travels in the Valley of the Nile, vol. 2, published in London in 1834",
    "Adapted",
    footnotes=[{"mark": "*", "text": "Manchester, England, was the world's leading center of cotton mills."}],
    glossary=[{"t": "Mohammed Ali / the Pasha", "d": "Muhammad Ali, the Ottoman governor (pasha) who ruled Egypt from 1805 to 1848"},
              {"t": "Savoyard", "d": "from Savoy, a region in the Alps"},
              {"t": "revenue", "d": "money coming in to the government"},
              {"t": "the Turks in office", "d": "Turkish-speaking officials who ran Egypt's government"},
              {"t": "evinced their disapprobation", "d": "showed that they disapproved"},
              {"t": "representations", "d": "complaints or objections"}, {"t": "puerile", "d": "childish"},
              {"t": "fellahs", "d": "Egyptian peasant farmers"}, {"t": "pressed", "d": "forced"}]),

"P11": {"type": "image",
    "src": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/NDL-DC_1312610-Utagawa_Kuniteru-%E4%B8%8A%E5%B7%9E%E5%AF%8C%E5%B2%A1%E8%A3%BD%E7%B3%B8%E5%A0%B4-%E6%98%8E%E6%B2%BB5-cmb.jpg/1280px-NDL-DC_1312610-Utagawa_Kuniteru-%E4%B8%8A%E5%B7%9E%E5%AF%8C%E5%B2%A1%E8%A3%BD%E7%B3%B8%E5%A0%B4-%E6%98%8E%E6%B2%BB5-cmb.jpg",
    "width": 1280, "height": 630,
    "alt": "A wide, brightly colored Japanese woodblock print in three panels showing a large group of long brick buildings with tiled roofs and a tall smokestack, with visitors, riders, and a carriage in the grounds.",
    "caption": "The print shows the Tomioka Silk Mill, northwest of Tokyo, in the year it opened. Long brick buildings with tiled roofs stand around open yards, and a tall smokestack rises in the center. Visitors walk and ride through the grounds, some in kimono and some in Western-style suits and hats. A horse-drawn carriage arrives at lower right. The red label at upper right gives the title.",
    "attribution": "Utagawa Kuniteru II, Japanese artist, Tomioka Silk Mill in Jōshū*, color woodblock print in three panels, published in Tokyo in 1872",
    "credit": "National Diet Library, Japan. Public domain image via Wikimedia Commons. *Jōshū is an old name for the region that is now Gunma Prefecture.",
    "description": "A very wide print made of three sheets side by side. Rows of long, two-story brick buildings with gray tiled roofs and many windows fill most of the picture, arranged around open courtyards. A tall round smokestack stands in the middle. People in the yards wear kimono or Western-style coats and hats; some ride horses, and a horse-drawn carriage enters at the lower right. Mountains rise in the background, and cherry trees bloom at the right edge. Red and yellow labels in the corners give the title, the artist's name, and the publisher.",
    "glossary": [{"t": "silk mill", "d": "a factory where silk thread is unwound (reeled) from cocoons"},
                 {"t": "woodblock print", "d": "a picture printed from carved wooden blocks; cheap prints like this were sold to the public"}]},

"P12": P([
    "The Government rightly encouraged private enterprise, but when those thus encouraged happened to be men of no ability, what good could be expected. Therefore it became a matter of prime importance to have some enterprise set up on a large scale so as to attract men of ability to it, and to this end there was no better means than to start the system of joint-stock companies. … At the same time, if by means of joint-stock companies we can secure the prosperity of production and trade, we may thereby expect to promote the wealth and power of a nation. …",
    "The first law enacted concerning private companies, after careful study of American and European institutions, was the Regulations for National Banks. … Thus the first joint-stock companies after Western models in this country were banks, and next came companies connected with shipping, railways, and insurance, to be followed by degrees by various industrial companies. … in 1873, the First National Bank was established. Hitherto, business in this country had consisted of small transactions, the public being ignorant of the advantages of conducting it on a joint-stock basis."],
    "Shibusawa Eiichi, Japanese finance official who left government in 1873 to lead the First National Bank and found many companies, \"Joint-Stock Enterprise in Japan,\" in Fifty Years of New Japan, compiled by Count Ōkuma Shigenobu",
    "English edition edited by Marcus B. Huish (London, 1909); adapted",
    glossary=[{"t": "private enterprise", "d": "businesses owned by private people, not the government"},
              {"t": "joint-stock companies", "d": "businesses owned by many investors who buy shares"},
              {"t": "hitherto", "d": "until then"}]),

"P13": P([
    "The history of all hitherto existing society is the history of class struggles. … Society as a whole is more and more splitting up into two great hostile camps, into two great classes, directly facing each other: Bourgeoisie and Proletariat. …",
    "Owing to the extensive use of machinery and to division of labour, the work of the proletarians has lost all individual character, and consequently, all charm for the workman. He becomes an appendage of the machine. … Modern industry has converted the little workshop of the patriarchal master into the great factory of the industrial capitalist. Masses of labourers, crowded into the factory, are organised like soldiers. …",
    "… The proletarians have nothing to lose but their chains. They have a world to win.\nWORKING MEN OF ALL COUNTRIES, UNITE!"],
    "Karl Marx and Friedrich Engels, German socialist writers, The Communist Manifesto, 1848",
    "Translated by Samuel Moore (English edition of 1888, edited by Engels); adapted",
    glossary=[{"t": "hitherto existing", "d": "that have existed up to now"},
              {"t": "Bourgeoisie", "d": "the class that owns factories, businesses, and capital"},
              {"t": "Proletariat / proletarians", "d": "industrial workers who own nothing but their ability to work"},
              {"t": "appendage", "d": "a part attached to something larger"},
              {"t": "patriarchal master", "d": "the owner of a small, old-style workshop, who ran it like the head of a family"}]),

"P14": P([
    "There is a class of Chinese who despise foreign methods, and without examining their excellences, contemptuously fling them aside with the remark that they are not specially mentioned in the Six Classics and the Histories of China. But what old method will suit the present day emergency? We challenge all these cavillers to produce an Ever Victorious Army* from the ancient drill, or protect our coast with old Chinese gunboats instead of with armored cruisers. By not adopting foreign methods we block our own way. …",
    "To sum up: Chinese learning is moral. Western learning is practical. Chinese learning concerns itself with moral conduct. Western learning, with the affairs of the world. … If the Chinese heart throbs in unison with the heart of the sages, expressing the truth in irreprovable conduct, in filial piety, brotherly love, honesty, integrity, virtue; if government is loyalty and protection, then let government make use of foreign machinery and the railway from morning to night, and nothing untoward will befall the disciples of Confucius."],
    "Zhang Zhidong, Qing official and governor-general of Hubei and Hunan provinces, Exhortation to Learning, 1898",
    "From the English translation by Samuel I. Woodbridge, published under the title China's Only Hope (1900); adapted",
    footnotes=[{"mark": "*", "text": "an army trained and led by Western officers that helped the Qing defeat the Taiping Rebellion in the 1860s"}],
    glossary=[{"t": "Six Classics", "d": "the ancient books at the heart of Confucian learning"},
              {"t": "cavillers", "d": "people who make petty complaints"},
              {"t": "sages", "d": "wise teachers of the past, especially Confucius"},
              {"t": "irreprovable", "d": "blameless"}, {"t": "filial piety", "d": "respect and duty toward one's parents"},
              {"t": "untoward", "d": "bad or harmful"}]),

"P15": {"type": "pair", "items": [
    item("Source 1", [
        "The boy. I am going fourteen; my sister is eleven. I have worked in Milnes's factory two years. She goes there also. … We go at half past five; give over at half past nine. I am now just come home. We sometimes stay till twelve. We are obliged to work overhours. … I asked to come away one night lately, at eight o'clock, being ill; I was told, if I went I must not come again. I am not well now. …",
        "Mother. I have worked in the same mills myself. … There's many young ones in that hot room. There's six of 'em badly now, with bad eyes and sick headache. … I would prefer their coming home at seven, without additional wages."],
        "Testimony of a family in Lenton, near Nottingham, England, to government commissioners investigating the work of children in factories, 1833",
        "From the Reports of the Factory Commissioners (1833), as printed in Robinson and Beard, Readings in Modern European History, vol. 2 (1908); adapted",
        glossary=[{"t": "going fourteen", "d": "almost fourteen years old"}, {"t": "give over", "d": "stop work"},
                  {"t": "overhours", "d": "overtime"}, {"t": "badly", "d": "sick"}]),
    item("Source 2", [
        "No one would accuse him* of a want of sympathy with the working classes; but this he would tell the House, that if they went on, at the bidding of the working classes, to legislate against the capitalists, they would find a very different feeling engendered among the latter towards the operatives. … [In his own factory] they had a large infant school, together with a reading room and news room, and a school for adults, where the workmen attended after working hours. …",
        "He would warn the House that if they now armed the workmen against the capitalists by fixing by law ten hours, or any other number of hours for the duration of labor, and thus interfered with the established custom of the kingdom, he believed it would be impossible that the feeling which hitherto existed on the part of the manufacturers towards the operatives would continue. …"],
        "John Bright, cotton-mill owner and member of the British Parliament, speech in the House of Commons opposing the Ten Hours Bill, a law to limit the workday of women and young people in textile mills, 1847",
        "From the official record of debates (Hansard), as printed in Robinson and Beard, Readings in Modern European History, vol. 2 (1908); adapted",
        footnotes=[{"mark": "*", "text": "The official record reports the speech in the third person, so \"he\" and \"him\" mean Bright."}],
        glossary=[{"t": "a want of", "d": "a lack of"}, {"t": "the House", "d": "the House of Commons, Britain's elected lawmaking body"},
                  {"t": "engendered", "d": "created"}, {"t": "operatives", "d": "factory workers"},
                  {"t": "infant school", "d": "a school for young children"}])]},

"P16": {"type": "bar",
    "title": "Percentage of the Population Living in Towns and Cities of 10,000 or More People, England and Wales and Scotland, 1801–1891",
    "categories": ["1801", "1851", "1891"],
    "series": [{"name": "England and Wales", "values": [21.3, 39.5, 61.7]},
               {"name": "Scotland", "values": [17.0, 32.2, 49.9]}],
    "yLabel": "Percent of population",
    "text": "The figures were calculated from British census counts, which were taken every ten years. Weber's table uses the label \"England\" for England and Wales.",
    "source": "Adna Ferrin Weber, The Growth of Cities in the Nineteenth Century: A Study in Statistics, 1899, Table XXV(a), p. 59"},
}

# Raw files used by the excerpt checker (not part of the bank).
RAWMAP = {
    "X1": ["anderson1904_constitutionsoth00andeiala.txt", "alt/anderson1908_cu31924026370936.txt"],
    "X2": ["rainsford1805_historicalaccoun00rain.txt", "alt/rainsford1805_historicalaccoun00rain_0.txt"],
    "X4.1": ["ure1835_philosophymanuf01uregoog.txt", "alt/ure_philosophymanuf00uregoog.txt"],
    "X4.2": ["gut_pg17306.txt"],
    "X5": ["okuma1909v1_fiftyyearsofnew01okumuoft.txt"],
    "X6": ["hertslet_mapeuropebytrea09hertgoog.txt", "alt/hertslet1875v2_mapeuropebytrea12hertgoog.txt"],
    "X7": ["gut_pg3300.txt"],
    "P1": ["gut_pg46333.txt"],
    "P2.1": ["gut_pg3420.txt"], "P2.2": ["hws1881v1_historyofwomansu01stan.txt"],
    "P3": ["robinsonbeard1908v2_readingsmodern02robi.txt", "alt/robinsonbeard1908v2_readingsinmoder02beargoog.txt"],
    "P4": ["bolivar_angostura1919_addressofbolivar00boluoft.txt"],
    "P5": ["robinsonbeard1908v2_readingsmodern02robi.txt", "alt/robinsonbeard1908v2_readingsinmoder02beargoog.txt"],
    "P6": ["gut_pg35899.txt"],
    "P7": ["toynbee1887_cu31924102143637.txt", "alt/toynbee1884_lecturesonindus02jowegoog.txt"],
    "P8": ["dutt1902_economichistoryo00dutt.txt", "alt/dutt1906_dliernet236779.txt"],
    "P9": ["wells1889_recenteconchange00welliala.txt", "alt/wells1889_recenteconomicc00wellgoog.txt"],
    "P10": ["stjohn1834_egyptandmohamme01johngoog.txt", "alt/stjohn1834_egyptandmohamme00algoog.txt"],
    "P12": ["okuma1909v1_fiftyyearsofnew01okumuoft.txt"],
    "P13": ["gut_pg61.txt", "alt/marx1898_manifestoofcommu00marx_1.txt"],
    "P14": ["zhang_woodbridge1900_cu31924107178109.txt"],
    "P15.1": ["robinsonbeard1908v2_readingsmodern02robi.txt", "alt/robinsonbeard1908v2_readingsinmoder02beargoog.txt"],
    "P15.2": ["robinsonbeard1908v2_readingsmodern02robi.txt", "alt/robinsonbeard1908v2_readingsinmoder02beargoog.txt"],
}

STIM = {k: v for k, v in STIM.items() if v is not None}
