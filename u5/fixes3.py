# Review pass 1 (independent checker agent, Nov 7). Letters are ORIGINAL letters (before answer-letter swaps).
PATCH = {
 # --- longest-option tells ---
 "U5-E13": {"options": {"E": "fresh milk spoiled fast and was costly to ship, so dairies could pay high rents near the city"}, "skill": "1.D"},
 "U5-E11": {"options": {"B": "efficient farms freed workers for factories, while factories made better farm tools"},
            "rationales": {"E": "Incorrect. Some early mills were built in the countryside near water power, but that does not explain the link: farms supplied workers and food to industry, and industry supplied tools to farms."},
            "skill": "1.B"},
 "U5-E16": {"options": {"D": "Women spend more time on household food crops and processing; men, on cash crops."}},
 "U5-E24": {"options": {"C": "A certification system that sets minimum prices and labor standards for producers"}},
 "U5-E19": {"options": {"E": "Mechanization and economies of scale let large farms buy out many smaller ones."}},
 "U5-E08": {"options": {"E": "the merging of open fields and commons into large private farms, pushing many people to cities",
                        "D": "a shift from commercial farming back to subsistence farming on most British farms"},
            "rationales": {"D": "Incorrect. Enclosed farms grew more crops and livestock for sale to growing towns and cities, so farming became more commercial, not less."}},
 "U5-P09": {"options": {"A": "Portuguese traders brought it from the Americas, and it grows well in poor soil and during dry spells."}},
 "U5-P28": {"options": {"E": "The buildup of salts in soil, often from irrigating fields in dry climates"}},
 "U5-P13": {"options": {"C": "The spread of high-yield seeds, chemicals, and irrigation in poorer countries in the mid-1900s"},
            "explanation": "The Green Revolution began in Mexico in the 1940s and spread to Asia in the 1960s. Scientists such as Norman Borlaug bred high-yield varieties (HYVs) of wheat and rice. Farmers in places like Mexico, India, and the Philippines planted these seeds and added chemical fertilizer, pesticides, irrigation, and machines. Harvests grew a lot. Your AP course guide lists high-yield seeds, more chemicals, and mechanized farming."},
 # --- absolutes / grammar tells ---
 "U5-E01": {"options": {
    "A": "Intensive agriculture produces food for the farm family, whereas extensive agriculture produces food for sale.",
    "B": "Intensive agriculture is practiced in developed countries, whereas extensive agriculture is practiced in developing countries.",
    "C": "Intensive agriculture grows crops, whereas extensive agriculture raises livestock.",
    "D": "Intensive agriculture uses many inputs per unit of land, whereas extensive agriculture uses few inputs per unit of land."}},
 "U5-E23": {"options": {
    "B": "GM crops are grown mainly by subsistence farmers rather than on large commercial farms.",
    "C": "GM crops are banned from international trade.",
    "D": "GM crops may reduce biodiversity and make farmers rely on a few seed companies.",
    "E": "GM crops require farmers to stop using chemical fertilizers and pesticides."}},
 "U5-E17": {"options": {"C": "Men control most land and cash income, while women are mainly responsible for feeding the household."}},
 "U5-P34": {"options": {"A": "decline, because most women migrate to the cities along with the men",
                        "C": "shift mainly to factory work in nearby towns"},
            "whyNot": {"A": "Women usually stay and take over more of the farm work; farms are rarely abandoned.",
                       "C": "The farm work still needs doing, and rural regions often have few factory jobs."},
            "explanation": "When men leave to work in cities or other countries, the family still needs food. So women do more of the farm work. They also make more of the farm decisions. This happens in parts of South Asia, Africa south of the Sahara, and Central America. Experts call it the \"feminization of agriculture.\" Women's farm roles change from place to place, depending on the kind of farming."},
 "U5-P36": {"options": {
    "A": "Women do most of the work on mechanized farms, while men do most of the hand labor on subsistence farms.",
    "C": "Women's roles in food production depend mainly on a region's climate rather than on the type of farming.",
    "E": "Mechanized commercial farms employ more women than subsistence farms do, because machines need many operators."},
   "whyNot": {
    "A": "This reverses the pattern: women often do much of the hand labor on subsistence farms, and mechanized farms are more often run by men.",
    "C": "Your AP course guide says roles depend on the type of production, not mainly on climate.",
    "E": "Mechanized farms need far fewer workers of any gender, not more."}},
 "U5-E07": {"options": {"A": "was grown mostly on large commercial plantations for export",
                        "C": "could be stored for several years without spoiling"},
            "rationales": {"C": "Incorrect. Potatoes keep for months, not years; their advantage was high calories per acre in cool, wet climates."}},
 "U5-P05": {"options": {"B": "The U.S. government applied the township and range grid, which produces long, narrow lots.",
                        "D": "Farmers used metes and bounds, which set boundaries along straight north-south lines."}},
 # E25: the original D ("the Public Land Survey System") duplicated A
 "U5-E25": {"options": {"D": "the open-field system"},
            "rationales": {"D": "Incorrect. The open-field system was the medieval European pattern of scattered strips farmed around a village, not a way of describing property lines."}},
 # --- facts and wording ---
 "U5-P02": {"explanation": "All three places have a Mediterranean climate: hot, dry summers and mild, rainy winters. Olive trees and grapevines have deep roots and tough leaves, so they survive the dry summers. Citrus trees need winters without hard frost, and farmers water them in summer. That is why farmers on three different continents grow the same crops."},
 "U5-P27": {"stem": "In 2022, the war in Ukraine blocked grain shipments from Ukraine's Black Sea ports, and bread and flour prices rose in wheat-importing countries such as Egypt and Lebanon. This example best illustrates which concept?",
            "explanation": "Egypt and Lebanon buy a lot of wheat from abroad, much of it from Ukraine and Russia. When the war blocked ships from leaving Ukraine's Black Sea ports, those countries could not get the grain as easily, so prices rose. A conflict in one place hurt food prices in another. Your AP course guide says global food distribution is shaped by political relationships, infrastructure, and patterns of world trade.",
            "skill": "5.B"},
 "U5-E22": {"stem": "Pastoral nomadism is most common in dry grasslands and deserts, such as parts of Central Asia, the Sahel, and the Horn of Africa, because", "skill": "2.B"},
 "U5-E21": {"rationales": {"C": "Incorrect. Irrigated rice covers only small areas of the Sahel, mainly along the Niger and Senegal Rivers; irrigation can cause salinization, but it is not the main driver of desertification there."}, "skill": "2.B"},
 "U5-P23": {"stem": "In von Thünen's model, simplified in the diagram, which land use occupied ring 2, and why?", "skill": "1.B"},
 "U5-P24": {"explanation": "Von Thünen's model depends on transportation cost rising steeply with distance, so perishable foods must be grown close to the market. Refrigeration and fast, cheap shipping break that rule: fresh grapes can travel thousands of miles from Chile and reach stores during the Northern Hemisphere's winter, when local grapes are out of season. Your AP course guide notes that specialty farming regions do not always fit the rings."},
 "U5-E15": {"rationales": {"A": "Incorrect. Every country in the table exports coffee, so these countries do sell agricultural goods abroad."}, "skill": "3.E"},
 "U5-P35": {"options": {"A": "In every country, women make up a larger share of landholders than men do.",
                        "D": "In Country 3, women's share of landholders is larger than their share of farm workers."}},
 "U5-E12": {"stem": "Large estates in tropical regions that grow a single cash crop, such as bananas, sugarcane, or oil palms, mainly for export to distant markets are an example of"},
 "U5-P17": {"options": {"C": "Land near the city costs more, so farmers must earn a lot from each acre to afford it."}},
 # --- readability ---
 "U5-P08": {"explanation": "The Columbian Exchange was a giant swap between the Americas and the rest of the world. It started after Columbus sailed in 1492. Plants, animals, people, and diseases moved both ways. Maize (corn) and potatoes from the Americas became big foods in Europe, Africa, and Asia. Wheat, cattle, and horses went the other way."},
 "U5-P10": {"explanation": "The Second Agricultural Revolution started in Britain in the 1700s, at the same time as the Industrial Revolution. The seed drill planted seeds in neat rows instead of tossing them by hand. Four-field crop rotation (wheat, turnips, barley, clover) kept the soil healthy, so no field had to sit empty. Later came steel plows, reapers, and tractors."},
 "U5-P11": {"explanation": "New tools and methods let each farmer grow much more food. Farms needed fewer workers, so many rural families moved to cities to work in factories. More food also meant better diets and longer lives."},
 # --- skill tags only ---
 "U5-E05": {"skill": "2.C"}, "U5-E10": {"skill": "2.C"}, "U5-P29": {"skill": "1.D"}, "U5-P14": {"skill": "1.D"},
 "U5-P06": {"skill": "4.E"}, "U5-E03": {"skill": "4.E"},
}
# Options listed in table order (College Board style); applied as a reorder after patches.
REORDER = {"U5-P03": ["Farm 1", "Farm 2", "Farm 3", "Farm 4", "Farm 5"],
           "U5-E14": ["Country P", "Country Q", "Country R", "Country S", "Country T"]}
# Extra letter swaps to re-balance after the reorders (P03 key -> B, E14 key -> A).
SWAPS2 = [("U5-P20", "B", "C"), ("U5-E20", "A", "E")]
