# Unit 3 bank: sources and verification (v2026-11-08d)

All stimulus data are **hypothetical** (labeled "Hypothetical data" / "Hypothetical map") except the items below.
Every number in every stimulus, and every computed claim in stems, keys, explanations, and rationales, is checked
by the DATA CHECKS block in `u3/assemble.py` (it fails the build if any check fails).

## Real data (statistics)

### U3-P20 — Individuals using the Internet (% of population), 2005 and 2024
- Source: World Bank, World Development Indicators, indicator `IT.NET.USER.ZS` (data from the International
  Telecommunication Union, World Telecommunication/ICT Indicators Database). Dataset "lastupdated" 2026-10-08.
- Page: https://data.worldbank.org/indicator/IT.NET.USER.ZS
- API call used (downloaded Nov 8, 2026):
  https://api.worldbank.org/v2/country/WLD;IND;NGA;BRA;USA;CHN;IDN;KEN;MEX;BGD;ETH;JPN/indicator/IT.NET.USER.ZS?format=json&date=2000:2025&per_page=1000
- Raw values (embedded in assemble.py and re-rounded by the check):

  | Country | 2005 raw | 2024 raw | Shown (2005 → 2024) |
  |---|---|---|---|
  | United States | 67.9681015 | 94.69380188 | 68 → 95 |
  | Brazil | 21.022747248827 | 84.46347227 | 21 → 84 |
  | India | 2.388099909 | 64.9434967 | 2 → 65 |
  | Nigeria | 3.54915571796492 | 41.21139908 | 4 → 41 |
  | World | 15.6 | 71.2 | 16 → 71 |

- Verified by script: rounding of every bar; every value rose; Nigeria 2024 < 50; gains US +27 (smallest),
  Brazil +63, India +63; US–India gap 66 → 30 points.
- Note: countries were used instead of World Bank regional aggregates because the World Bank's current regional
  classification moves Afghanistan and Pakistan out of "South Asia," which students would not expect.

## Real facts used in stimulus tables (non-statistical)

### U3-P25 — Texas place names (Handbook of Texas Online, Texas State Historical Association; accessed Nov 8, 2026)
- https://www.tshaonline.org/handbook/entries/nacogdoches-tx — "named for the Nacogdoche Indians, a Caddo group."
- https://www.tshaonline.org/handbook/entries/san-antonio-tx — 1691 Terán de los Ríos expedition "named the San
  Antonio River on June 13, the Feast Day of ... Saint Anthony of Padua."
- https://www.tshaonline.org/handbook/entries/el-paso-tx — Spaniards "named El Paso del Norte (the Pass of the North)."
- https://www.tshaonline.org/handbook/entries/new-braunfels-tx — founded March 21, 1845, by German immigrants
  (Adelsverein); incorporated under the name of Prince Solms's estate in Germany, Braunfels; 30 mi NE of San Antonio,
  45 mi SW of Austin.
- https://www.tshaonline.org/handbook/entries/fredericksburg-tx — first settlers arrived May 8, 1846; Meusebach
  "named Fredericksburg after Prince Frederick of Prussia."

### U3-P24 — Where followers of five religions lived in 2010 (table dated 2010 since review pass 3)
- Pew Research Center, "The Global Religious Landscape" (Dec. 18, 2012; 2010 data):
  https://www.pewresearch.org/religion/2012/12/18/global-religious-landscape-exec/
- Verified: 97% of Hindus live in India, Mauritius, and Nepal; 99% of Buddhists live in the Asia-Pacific region
  (about half in China), so "East and Southeast Asia" for Buddhists; Christians are spread most evenly (Europe 26%,
  Latin America and the Caribbean 24%, sub-Saharan Africa 24%, plus North America); 44% of Jews live in North America
  and 41% in the Middle East and North Africa, "almost all of them in Israel"; 62% of Muslims live in Asia-Pacific,
  about 20% in the Middle East and North Africa, about 16% in sub-Saharan Africa.
- Universalizing/ethnic types follow the AP course framework (Topic 3.7, IMP-3.B.4 and IMP-3.B.5).
- Hearths (source line since v2026-11-08c: "Encyclopaedia Britannica articles on each religion"), checked Nov 8, 2026:
  Britannica "Buddha" (born at Lumbini, "in what is today southern Nepal"); the Buddhism hearth cell reads "northern India and southern Nepal"
  (v2026-11-08d) because the Buddha's main sites (Bodh Gaya, Sarnath, Kushinagar) are on the Ganges Plain, and
  "northeastern India" usually means Assam and its neighbors; Britannica "Hinduism: The history of
  Hinduism" (Vedic religion took shape on the Indian subcontinent; an Indus-valley link is called speculative, so
  the hearth now reads "northern Indian subcontinent" instead of "Indus and Ganges river valleys"); Britannica
  "Christianity: The history of Christianity" (began in 1st-century Jewish Palestine, in Galilee and Jerusalem,
  "as a movement within Judaism," which also supports Judaism's Levant hearth); Britannica "Muhammad" (first
  revelations near Mecca; emigration in 622 to Yathrib, "also known as Medina").
- Pew's 2025 update ("How the Global Religious Landscape Changed From 2010 to 2020") exists; the independent checker
  confirmed the table's statements still hold with the newer data.

### U3-P16 — Four languages and their histories
The source line (since v2026-11-08c) names these articles. Cross-checked against English Wikipedia articles (Nov 8, 2026): "Swahili language" (Bantu language; emerged as a
lingua franca of the East African coast; official in Kenya and Tanzania); "Haitian Creole" (formed in Saint-Domingue
in the 17th–18th centuries; vocabulary largely from French, grammar with West African influence; native language of
the vast majority of Haitians; official with French); "Basque language" ("Europe's only known language isolate,"
spoken in the western Pyrenees in northern Spain and southwestern France); "Languages of Senegal," "Languages of
Ivory Coast," "Languages of Gabon" (French is the official language in each; checked Nov 8, 2026, because several
Sahel states changed French's status in 2023–24). v2026-11-08b replaced the earlier Portuguese row with French so the
table does not repeat U3-E08's key.

## Real facts in stems and explanations (checked; no statistics)

Cross-checked against English Wikipedia (or Wiktionary where noted), Nov 8, 2026, unless marked "standard knowledge":
- U3-P05 Uluru: climb (chain) closed in October 2019; the Anangu are the traditional owners and long asked visitors
  not to climb.
- U3-P08 Tanzania: Swahili is the national language; Ethnologue lists 126 languages in Tanzania ("more than 100").
- U3-P09 explanation: Quebec as a real example of language-based pressure for self-rule (standard knowledge).
- U3-P10 Chicano Park, Barrio Logan, San Diego: land takeover April 22, 1970; murals begun 1973; beneath the
  San Diego–Coronado Bridge.
- U3-P17 Tok Pisin: English-based creole; began as a plantation pidgin in the 1800s; one of PNG's official languages
  and its most widely used language; many children now learn it as a first language.
- U3-P18 / E08 Treaty of Tordesillas, 1494 (Wikipedia); Brazil's independence from Portugal in 1822 (standard
  knowledge); Portuguese official in Brazil, Angola, Mozambique, and Timor-Leste (Timor-Leste: Portuguese and Tetun
  official, Wikipedia "Languages of Timor-Leste").
- U3-P19 Islam in Indonesia: spread through merchants (including from Gujarat, India, and Arabia), adoption by local
  rulers, and Sufism from about the 12th–13th century.
- U3-P21 Icelandic "tölva" (computer): Wiktionary — coined by Sigurður Nordal in 1965 from tala ("number") +
  völva ("prophetess").
- U3-P26 Indo-European homeland: Anatolian hypothesis (Renfrew; spread with agriculture from about 7500–6000 BCE)
  and Kurgan/steppe hypothesis (Gimbutas; Pontic–Caspian steppe, about 4000–3000 BCE). The items say only that
  scholars still debate the two. "Language family with the most speakers": Wikipedia, more than 3.4 billion
  speakers, "by far the most of any language family" (confirmed by the independent checker).
- U3-P27 Malagasy: Austronesian; one of the Barito languages, closest relative Ma'anyan on Borneo; settlement dates
  are uncertain, so the explanation says "many centuries ago."
- U3-P29 Sikhism: Punjab, late 1400s–early 1500s (Guru Nanak, 1469–1539); large Sikh communities in Surrey
  (Wikipedia "Sikhism in Canada": 154,415 Sikhs in Surrey, 2021 Census); Southall (Sri Guru Singh Sabha, London's largest gurdwara) and Yuba City (gurdwara serving 20,000+ Sikhs; one of
  the largest Sikh festivals outside India) were confirmed from Wikipedia by the independent checker.
- U3-P32 Day of the Dead: November 1–2, the dates of All Saints' and All Souls' Days; Wikipedia notes scholarly
  debate over how much comes from Indigenous versus European traditions, so the stem says customs "that many
  scholars trace to Indigenous Mesoamerican traditions."
- U3-E06 Sequoyah: completed the Cherokee syllabary in 1821; described as illiterate (could not read English).
- U3-E07 Aviation English: ICAO recommended English for international aeronautical communications (Annex 10) and
  requires English proficiency for pilots and controllers on international routes (Wikipedia "Aviation English").
- U3-E09 Haitian Creole: see U3-P16 sources; official since the 1987 constitution.
- U3-E13 Belgium: state reforms from 1970 onward turned a unitary state into a federal one with communities and
  regions, driven by Dutch-speaking (Flanders) and French-speaking (Wallonia) disputes.
- U3-E14 Louisiana French: CODOFIL (1968); French immersion programs in many parishes (e.g., Lafayette).
- U3-E23 Transatlantic telegraph: first cable 1858 failed; permanent connection since 1866.
- U3-E24 Santería: developed in Cuba; syncretism of Yoruba religion, Catholicism, and Spiritism; oricha spirits are
  equated with Roman Catholic saints.
- U3-E25 Canada: official national multiculturalism policy in 1971 (the item does not claim Canada was first).
- Standard knowledge, not separately fetched: yukata as a summer kimono (P01); homecoming mums as a Texas
  football tradition (E01); Nigeria's mostly Muslim north and mostly Christian south ("much of," P11); Buddhism's
  spread by missionaries and traders along the Silk Roads and sea routes (E20); Irish (Celtic) and Bengali
  (Indo-Iranian) as Indo-European languages (E19).

## Not used
No photographs (none available); landscapes are described in text (P04 field notes, E10 city-block table, E12 desert
houses). No `pyramid` or `line` stimuli were needed for this unit.

## Review pass 3 (ChatGPT Pro, v2026-11-08c): new or changed facts and how they were checked
- U3-E08 option B: the Community of Portuguese Language Countries (CPLP) was founded in Lisbon on July 17, 1996
  (founders included Angola, Brazil, and Mozambique); Timor-Leste joined in 2002 after independence (Wikipedia
  "Community of Portuguese Language Countries"). Key E now says Portuguese was "kept or restored," because
  Timor-Leste chose Portuguese (with Tetum) after the Indonesian occupation (1975–1999).
- U3-E07: the stem no longer states an ICAO rule (the review noted pilots may use English or the ground station's
  language); it now describes a Portuguese-speaking pilot and a Japanese-speaking controller using English.
- U3-P33: regional soft-drink words. Dictionary.com, "Soda vs. Pop": "Midwesterners and Northwesterners prefer pop;
  Southerners say coke; and Easterners and Southwesterners ask for soda" (https://www.dictionary.com/articles/sodapop).
- U3-P35: women-only rail cars. Wikipedia "Women-only passenger car": Keio introduced late-night women-only cars in
  2000 "in response to complaints about groping"; Tokyo-area rush-hour cars followed in 2005; Mexico City Metro and
  Delhi Metro have women-only cars. The stem gives the harassment reason for Tokyo only.
  Earlier Tokyo women-only cars (1912 students; 1947 overcrowding) had other reasons; the stem (v2026-11-08d) dates
  the harassment-driven cars to the 2000s.
- U3-P34 (scale) and the rewritten U3-E18 use hypothetical data; their numbers are verified in assemble.py
  (P34's national row is the population-weighted mean of the regions: 85.3% and 14.7%, shown as 85 and 15).

## Review history
- v2026-11-08a: first draft; 0 errors / 0 warnings in assemble.py.
- v2026-11-08b: independent Claude blind check (u3/check_report.md): 57/57 keys agreed, all stimulus numbers
  recomputed, World Bank / Pew / Handbook of Texas sources re-fetched, no must-fix. All should-fix items applied.
- v2026-11-08c: ChatGPT Pro full review (u3/chatgpt_review.txt): all keys kept; corrections applied as
  u3/fixes_c.py (final letters, applied after the swaps in assemble.py); P33–P35 added in u3/p3.py.
- v2026-11-08d: final independent Claude blind check (u3/check_report_final.md, 60/60); fixes in u3/fixes_d.py.
