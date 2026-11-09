# Unit 7 sources

## Real data (verified by script)

All real numbers in the Unit 7 bank come from the **World Bank, World Development Indicators (WDI)**, data year **2023**,
read through the public WDI API on **Nov. 8, 2026** (dataset `lastupdated` = 2026-10-08). The raw API responses are
cached in `u7/wdi/`. `u7/assemble.py` builds the exam table rows directly from those files (no hand-typed values), and
`u7/verify.py` re-derives every value and every claim made about it. `python3 u7/verify.py --refetch` downloads the
four series again and confirms they still match the cache (it matched on Nov. 8, 2026).

| Indicator | Code | API URL used |
|---|---|---|
| GNI per capita, PPP (current international $) | NY.GNP.PCAP.PP.CD | https://api.worldbank.org/v2/country/ETH;IND;MEX;USA;DEU;VNM/indicator/NY.GNP.PCAP.PP.CD?date=2023&format=json&per_page=100 |
| Employment in agriculture (% of total employment) (modeled ILO estimate) | SL.AGR.EMPL.ZS | https://api.worldbank.org/v2/country/ETH;IND;MEX;USA;DEU;VNM/indicator/SL.AGR.EMPL.ZS?date=2023&format=json&per_page=100 |
| Employment in industry (% of total employment) (modeled ILO estimate) | SL.IND.EMPL.ZS | https://api.worldbank.org/v2/country/ETH;IND;MEX;USA;DEU;VNM/indicator/SL.IND.EMPL.ZS?date=2023&format=json&per_page=100 |
| Employment in services (% of total employment) (modeled ILO estimate) | SL.SRV.EMPL.ZS | https://api.worldbank.org/v2/country/ETH;IND;MEX;USA;DEU;VNM/indicator/SL.SRV.EMPL.ZS?date=2023&format=json&per_page=100 |

Human-readable indicator pages: https://data.worldbank.org/indicator/NY.GNP.PCAP.PP.CD ,
https://data.worldbank.org/indicator/SL.AGR.EMPL.ZS , https://data.worldbank.org/indicator/SL.IND.EMPL.ZS ,
https://data.worldbank.org/indicator/SL.SRV.EMPL.ZS

Values as published. Employment shares are displayed to one decimal; the parenthetical values show three decimals of the API value (the cached responses in `u7/wdi/` hold full precision). Rounding is half-up from the full-precision value, so Vietnam's services share of 39.549... displays as 39.5. GNI is shown as published, in whole dollars.

| Country | GNI per capita, PPP | Agriculture % | Industry % | Services % |
|---|---|---|---|---|
| Ethiopia | 3,060 | 62.2 (62.175) | 6.4 (6.361) | 31.5 (31.464) |
| Germany | 74,600 | 1.2 (1.212) | 26.4 (26.396) | 72.4 (72.393) |
| India | 9,710 | 43.5 (43.514) | 25.0 (25.029) | 31.5 (31.457) |
| Mexico | 24,560 | 12.0 (11.965) | 25.0 (25.031) | 63.0 (63.004) |
| Vietnam | 14,260 | 27.0 (26.983) | 33.5 (33.468) | 39.5 (39.549) |
| United States | 81,870 (not shown) | 1.6 (1.570) | 19.3 (not shown) | 79.1 (79.095) |

Where used:
- **U7-P05** (bar chart): agriculture and services shares for Ethiopia, India, Mexico, United States.
- **U7-E09 to E11** (exam Set B table): GNI per capita PPP and all three sector shares for Ethiopia, Germany, India, Mexico, Vietnam.

What `verify.py` checks on these data: the countries sort by GNI as Ethiopia < India < Vietnam < Mexico < Germany; the
agriculture share falls at every step (E09 key); the industry share does not rise steadily (E09 A false); Vietnam has the
largest industry share, 33.5 (E11 stem); Germany's services share (72.4) exceeds its industry share (E09 B, D false);
Ethiopia's and India's services shares are both 31.5 and India's GNI is more than three times Ethiopia's (E09 E);
each row sums to 100 within rounding; the P05 bar values equal the rounded API values; every number quoted in the E09
and E11 rationales appears in the data.

Note: ILO modeled estimates are revised every year, so later WDI releases may show slightly different 2023 values. The
source line on each stimulus gives the data-update date and access date.

## Hypothetical data

Every other stimulus is labeled "Hypothetical data" or "Hypothetical map" (P02, P10, P13, P18, P20, P24, P26/P27,
P32, E04 to E06, E13/E14, E22/E23). Practice items P33 to P39 have no stimulus. `verify.py` re-computes each keyed answer and each data-based distractor from the
stimulus numbers (for example the comparative-advantage ratios in P20, the pay-gap changes in P13, Country L having
the lowest maternal-death and teen-birth rates, the most legislative seats, and the smallest participation gap in E13, the coal-share arithmetic in P32, the rail links on the Weber map used by E06, and the ratios in E19 and E22).

## Course framework

Topic numbers, titles, learning objectives (SPS-7.A to SPS-7.E, PSO-7.A, IMP-7.A), essential knowledge, and skill
codes (1.A to 5.D) follow the AP Human Geography Course and Exam Description (College Board, 2020), Unit 7,
pp. 119–131 (local copy /tmp/ced/hg.pdf).

## Facts stated without a data stimulus

These widely documented facts appear in keys, explanations, or rationales; none is a statistic:
Industrial Revolution begins in Great Britain in the late 1700s and spreads to Western Europe and the United States in the
1800s, then Russia and Japan (Meiji Restoration 1868); the 2008 global financial crisis began in the U.S. housing-loan market and cut orders and jobs at export factories in China; Grameen Bank and Muhammad Yunus, 2006 Nobel Peace Prize;
Mercosur founded 1991 by Argentina, Brazil, Paraguay, and Uruguay; WTO created 1995; China's first special economic
zones (including Shenzhen) created 1980 on the southeast coast; Vietnam's economic opening (Doi Moi) begins 1986;
South Korea a Japanese colony until 1945; UN Sustainable Development Goals adopted 2015 for all member states; HDI
dimensions (life expectancy, schooling, GNI per capita); GII dimensions (maternal mortality and adolescent birth rate;
parliamentary seats and secondary education; labor force participation by sex).
