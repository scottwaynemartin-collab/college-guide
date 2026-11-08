# Unit 6 bank: data sources and checks

Only two stimuli use real data. Every other stimulus is labeled "Hypothetical data" or "Hypothetical map".
`python3 u6/verify.py` re-derives every number and computed answer (70 checks). `python3 u6/verify.py --live`
also re-downloads the two sources below and compares every stored value (last run Nov 8, 2026: 0 mismatches).

## 1. World Bank urban share: U6-E02 / U6-E03 line chart

- Source: World Bank, World Development Indicators, indicator `SP.URB.TOTL.IN.ZS`, "Urban population (% of total population)".
  The indicator metadata credits UN Population Division, *World Urbanization Prospects*, national definitions of urban.
- URL (API): https://api.worldbank.org/v2/country/CHN;NGA;USA;GBR;IND/indicator/SP.URB.TOTL.IN.ZS?format=json&date=1960:2024&per_page=1000
- Metadata: https://api.worldbank.org/v2/indicator/SP.URB.TOTL.IN.ZS?format=json
- API header `lastupdated`: 2026-10-08. Accessed Nov 8, 2026.
- Verified: the chart's values equal the API values rounded to one decimal.

| Year | United Kingdom | China | Nigeria | India |
|---|---|---|---|---|
| 1960 | 78.6 | 19.7 | 14.2 | 17.9 |
| 1970 | 76.9 | 17.4 | 20.2 | 19.7 |
| 1980 | 78.6 | 19.4 | 27.4 | 23.5 |
| 1990 | 78.1 | 26.2 | 35.2 | 25.6 |
| 2000 | 79.8 | 36.4 | 43.3 | 27.6 |
| 2010 | 81.0 | 49.2 | 51.7 | 30.9 |
| 2020 | 82.9 | 63.5 | 59.8 | 34.1 |

Full-precision values are stored in `u6/verify.py` (`WB`). Note for reviewers: this World Bank release carries the
newer UN urbanization estimates, so some values differ from the older World Urbanization Prospects 2018 figures in
many textbooks (for example, Nigeria 2020 is 59.8 here). No item depends on a textbook figure; every claim is checked
against the values in the chart. The United States was downloaded but not used (its 2020 value, 80.0, dips slightly
below its 2010 value, 80.7, which would distract from the questions).

Claims checked by script: China gained the most percentage points 1980–2020 (+44.1; Nigeria +32.4, India +10.6,
United Kingdom +4.3); China > Nigeria in 1960 and 2020; India +8.5 vs. Nigeria +24.6 for 1990–2020; the United Kingdom
did not double; China < India in 1980.

## 2. U.S. Census Bureau city populations: U6-P06 table

Rows are incorporated places (SUMLEV 162), Texas (STATE 48): Dallas 19000, Plano 58016, McKinney 45744, Frisco 27684.

| Column in table | File | Field | URL |
|---|---|---|---|
| 2000 Census | sub-est2009_48.csv | POPCENSUS_2000 | https://www2.census.gov/programs-surveys/popest/datasets/2000-2009/cities/totals/sub-est2009_48.csv |
| 2010 Census | SUB-EST2020_48.csv | CENSUS2010POP | https://www2.census.gov/programs-surveys/popest/datasets/2010-2020/cities/SUB-EST2020_48.csv |
| July 1, 2024 estimate | sub-est2024_48.csv | POPESTIMATE2024 | https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/cities/totals/sub-est2024_48.csv |

| City | 2000 Census | 2010 Census | July 1, 2024 estimate |
|---|---|---|---|
| Dallas | 1,188,580 | 1,197,816 | 1,326,087 |
| Plano | 222,030 | 259,841 | 293,286 |
| McKinney | 54,369 | 131,117 | 227,526 |
| Frisco | 33,714 | 116,989 | 235,208 |

Accessed Nov 8, 2026. The 2020 Census count was not used: the Census API now requires a key, and the estimates files
carry only the April 2020 estimates base, not the count itself. Claims checked by script: Frisco grew about 7 times
(6.98) and McKinney about 4 times (4.18) from 2000 to 2024; both passed 100,000 by 2010; no city lost population;
Dallas is the largest.

Definition note (boomburb): the item and its explanation use the working definition "large, fast-growing suburban
cities of more than 100,000 people that are not the main city of their metro area" ("often called boomburbs"). Lang and
Simmons' original definition also required double-digit growth in every census from 1970 on. Per the independent check,
McKinney grew only about 7% in the 1970s (1970: 15,193; 1980: 16,249; figures from the check, not re-verified here), so it
would not meet that stricter test. No item claims that either city appears on Lang's original list.

## Factual claims outside the stimuli

The topics, Learning Objective codes, and Essential Knowledge come from the 2020 AP Human Geography Course and Exam
Description (Unit 6, pp. 108–118). Other facts the items rely on are standard textbook facts, worded to avoid
specifics that could not be checked:

- Burgess concentric zone model (1925, based on Chicago); Hoyt sector model; Harris and Ullman multiple nuclei model;
  galactic city model; bid-rent theory; Griffin–Ford Latin American city model (1980); McGee's Southeast Asian city
  model (port zone as focus); de Blij's sub-Saharan African city model (three CBDs: colonial, traditional market,
  transitional).
- Christaller's central place theory (threshold, range, hexagonal market areas, isotropic plain); the gravity model
  (population product over distance squared); the rank-size rule; primate cities.
- Boomburb (large, fast-growing suburban city of 100,000+ that is not its metro area's main city; see the definition note
  above); edge
  city; exurb; megacity (10 million+); metacity (20 million+).
- U.S. suburbanization after 1945 (FHA and VA/GI Bill home loans; Federal-Aid Highway Act of 1956); urban interstates
  routed through low-income and predominantly Black neighborhoods; HOLC residential security maps of the 1930s
  (grades A–D, D shaded red); blockbusting.
- Atlantic Seaboard fall line cities (Richmond, Trenton): water power and head of navigation.
- Census tracts usually hold about 1,200–8,000 people (optimum about 4,000).
