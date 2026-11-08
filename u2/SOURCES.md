# Unit 2 bank — sources and verification notes (v2026-11-08b)

All stimuli are hypothetical (labeled "Hypothetical data" / "Hypothetical map") except the three World Bank tables below.
Every rate, ratio, density, share and doubling time in the bank is recomputed by `u2/assemble.py` from `u2/data.py`
(the `VERIFY` block); the build fails if any keyed number or quoted figure drifts. Raw API responses are saved in
`u2/data_raw/` (pulled Nov 8, 2026; WDI `lastupdated` = 2026-10-08).

## Real-data stimuli (World Bank, World Development Indicators)

| Item | Indicators (2024 values) | API query used | What was verified |
|---|---|---|---|
| U2-P02 density table | SP.POP.TOTL, AG.LND.TOTL.K2, AG.LND.ARBL.HA | https://api.worldbank.org/v2/country/EGY;NLD;CAN;JPN/indicator/{code}?format=json&date=2019:2024 | Population, land area and arable land for Egypt, Netherlands, Japan, Canada; arithmetic and physiological densities computed by script (arable ha ÷ 100 = sq km). Arithmetic densities cross-checked against WDI EN.POP.DNST 2024 (Egypt 117.07, Netherlands 534.41, Japan 340.12, Canada 4.69): exact match. Key: Egypt arithmetic 117 < Netherlands 534, physiological 3,560 > 1,794 (ratio 1.98, "about twice"); Egypt arable share 3.29%. |
| U2-P13 vital-rates table | SP.DYN.CBRT.IN, SP.DYN.CDRT.IN, SP.POP.GROW | https://api.worldbank.org/v2/country/NER;IND;CAN;DEU;JPN/indicator/{code}?format=json&date=2021:2024 | Niger 41.42 / 8.719 / 3.28%; India 15.981 / 6.587 / 0.89%; Canada 8.9 / 7.9 / 2.98%; Germany 8.1 / 12.1 / 0.27%; Japan 5.7 / 13.3 / −0.44%. Script confirms Germany is the only country with deaths > births and positive growth (RNI −0.4%, growth +0.3%); Japan's growth is negative; Canada RNI 0.1%. |
| U2-P40 remittances table | BX.TRF.PWKR.CD.DT, BX.TRF.PWKR.DT.GD.ZS | https://api.worldbank.org/v2/country/IND;MEX;PHL;NPL;TJK;TON/indicator/{code}?format=json&date=2021:2024 | India $137.7B / 3.66%; Mexico $67.9B / 3.71%; Philippines $40.3B / 8.72%; Nepal $11.3B / 25.99%; Tajikistan $6.8B / 47.15%; Tonga $0.26B / 39.41%. Script confirms the two largest receivers (India, Mexico) have the two lowest GDP shares. |

## Real figures quoted in stems, keys, or rationales

| Item | Claim | Source checked |
|---|---|---|
| U2-E07 | 2024 crude death rate: Japan about 13, Niger about 9 per 1,000; Japan about 3 in 10 people 65+; Japan life expectancy among the world's highest; Niger IMR much higher than Japan's | WDI SP.DYN.CDRT.IN 2024 (13.3, 8.719); SP.POP.65UP.TO.ZS 2024 (Japan 29.8%, Niger 2.6%); SP.DYN.LE00.IN 2024 (Japan 84.0, Niger 61.4, world 73.5); SP.DYN.IMRT.IN 2024 (Japan 1.8, Niger 65.6) |
| U2-E14 | Latin America & Caribbean TFR about 5.2 (1970) to about 1.9 (2020); infant mortality fell; region urbanized | WDI SP.DYN.TFRT.IN, aggregate LCN (5.18 → 1.86); SP.DYN.IMRT.IN: the LCN aggregate starts in 1990 (44.1 → 14.4 in 2020), and the country series cover 1970–2020 (Brazil 102.2 → 12.8, Mexico 82.0 → 13.4, Peru 127.3 → 12.2, Haiti 168.0 → 43.6 per 1,000; https://api.worldbank.org/v2/country/BRA;MEX;PER;HTI/indicator/SP.DYN.IMRT.IN?format=json&date=1970:2020, saved as data_raw/IMR_LAC_countries.json); SP.URB.TOTL.IN.ZS LCN (56.5% in 1970 → 80.4% in 2020) |
| U2-E24 | Remittances about one-quarter of GDP in Nepal and Honduras in 2024 | WDI BX.TRF.PWKR.DT.GD.ZS 2024 (Nepal 25.99%, Honduras 25.74%) |
| U2-P29 | Women and girls are almost half (about 48%) of international migrants | UN DESA International Migrant Stock 2024, as reported by Dawn, Feb 18, 2025: https://dawn.com/news/1892702/number-of-migrants-doubled-since-1990-un ("just under half (48pc) of all international migrants worldwide were women or girls") |
| U2-P07 | Groundwater pumping makes parts of Mexico City sink, in places tens of centimeters a year | Eos (AGU): https://eos.org/articles/groundwater-pumping-is-causing-mexico-city-to-sink ("groundwater pumping is the main driver of subsidence"; "about 35 centimeters (14 inches) per year"). Elevation ~2,240 m (standard reference). |
| U2-E01 | Most Russians live west of the Urals, on a minority of the land | Wikipedia, European Russia: https://wikiwand.com/en/articles/European_Russia ("about 80% of Russia's total population"; c. 23% of territory). Item wording avoids a precise percentage. |
| U2-E09 | Singapore "Stop at Two" campaign in the 1970s; "Have Three or More (if you can afford it)" announced 1987; fertility below replacement by the late 1970s (about 1.8 in 1977) | Wikipedia, Population planning in Singapore: https://en.wikipedia.org/wiki/Population_planning_in_Singapore. The independent checker confirmed Singapore's TFR was 2.07 in 1975, 2.11 in 1976, 1.82 in 1977, and below 2.1 every year since. |

## Standard-textbook facts (no figures), wording kept conservative

China one-child policy about 1980–2015, two-child 2016, three-child 2021 (P25); Malthus 1798 (P21); Paul Ehrlich, *The Population Bomb*, 1968 (P23);
Esther Boserup's intensification argument (E08); Ravenstein's laws, 1880s, including short-distance moves, step migration, long-distance
migrants heading for centers of commerce and industry, and women more migratory within their home country (P29, P35, P37);
Canada and Australia use points-based immigration systems (P26); Qatar and the UAE have strongly male-skewed working-age pyramids
because of foreign labor (P10 explanation); Alpine transhumance (E20); Soviet-era growth of Siberian cities such as Novosibirsk, oil and gas
mainly in western Siberia, the Urals as low mountains crossed by the Trans-Siberian Railway (E01 rationales).

## Notes for reviewers

- Ravenstein's laws appear in the course framework only under SPS-2.B.2 (Topic 2.8, women). P29 is tagged there. P35 (distance decay) stays at 2.10 / IMP-2.C and is tied to IMP-2.C.2: its explanation treats distance itself as an intervening obstacle (longer moves cost more and people know less about faraway places).
- Practice stimuli are self-contained (no `set`), as in units 4 and 5, because app.js renders practice stimuli from `q.stimulus` only and practice can be filtered by topic.
