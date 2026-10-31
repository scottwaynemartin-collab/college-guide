# Sources: "Why do populations boom?"

Every number on screen comes from one dataset. Nothing is invented, smoothed or projected.

## Data

**World Bank, World Development Indicators (WDI)**

| Indicator | Code | Unit |
|---|---|---|
| Birth rate, crude | `SP.DYN.CBRT.IN` | live births per 1,000 people (mid-year population) |
| Death rate, crude | `SP.DYN.CDRT.IN` | deaths per 1,000 people (mid-year population) |

- Upstream sources, as listed in WDI's own metadata: UN Population Division, *World Population Prospects*; national statistical offices; Eurostat; UN Statistical Division, *Population and Vital Statistics Report*.
- License: CC BY 4.0.
- Retrieved: 31 October 2026, from the Open Numbers mirror of WDI. This is a public GitHub repo that republishes the WDI bulk download as CSV: <https://github.com/open-numbers/ddf--open_numbers--world_development_indicators>, commit `1bd7fac42b3d5012353607bf2464a485557fd049` (18 October 2026). Files used:
  - `datapoints/ddf--datapoints--sp_dyn_cbrt_in--by--geo--time.csv`
  - `datapoints/ddf--datapoints--sp_dyn_cdrt_in--by--geo--time.csv`
- Canonical pages: <https://data.worldbank.org/indicator/SP.DYN.CBRT.IN>, <https://data.worldbank.org/indicator/SP.DYN.CDRT.IN>.
- Countries and years: Niger, Bangladesh, Sweden and Japan, 1960–2024. The extract is in [`data/wdi_cbr_cdr.csv`](data/wdi_cbr_cdr.csv) (260 rows) and is rebuilt by [`scripts/extract_data.py`](scripts/extract_data.py).

> Check before you publish: the sandbox this was built in could not reach data.worldbank.org directly, so the numbers come from the mirror above. They are worth spot-checking against the World Bank site. WDI updates its estimates each year when the UN publishes a new revision, so the latest release may differ slightly.

## Every number that appears on screen

On screen, rates are rounded to one decimal place. The gap (natural increase) is worked out from the rounded figures (rounded births minus rounded deaths), so a student checking the subtraction always gets the number shown.

| Where | Country | Year | Births /1,000 | Deaths /1,000 | Gap /1,000 | Raw WDI values |
|---|---|---|---|---|---|---|
| Niger ledger, start | Niger | 1960 | 57.6 | 27.6 | 30.0 | 57.613 / 27.633 |
| Niger ledger, end; predict start; peak-gap marker | Niger | 2009 | 49.8 | 12.0 | 37.8 | 49.8 / 12.0 |
| Prediction reveal; recap strip | Niger | 2024 | 41.4 | 8.7 | 32.7 | 41.42 / 8.719 |
| Bangladesh ledger, start | Bangladesh | 1980 | 45.2 | 15.4 | 29.8 | 45.165 / 15.449 |
| Bangladesh ledger, end; recap strip | Bangladesh | 2024 | 20.0 | 5.1 | 14.9 | 19.988 / 5.105 |
| "1971: war" note | Bangladesh | 1971 | 47.6 | 39.9 | 7.7 | 47.599 / 39.876 |
| Recap strip | Sweden | 2024 | 9.3 | 8.6 | +0.7 | 9.3 / 8.6 |
| Recap strip | Japan | 2024 | 5.7 | 13.3 | −7.6 | 5.7 / 13.3 |

The live labels next to the lines show the published value for each year as the line is drawn. The lines join the annual points with straight segments.

### Derived figures

- **"% a year"** = gap ÷ 10. A gap of 37.8 per 1,000 is +3.8% a year.
- **"doubles in about 19 years"** (Niger, 2009) = ln 2 ÷ ln(1 + 0.0378) = 18.7 years, rounded to 19. This assumes the 2009 rate holds steady. It is a teaching illustration, not a forecast.
- **The gap is *natural* increase.** It leaves out migration, which is how WDI defines the measure.

## Editorial judgments (not data)

These are our labels and explanations. They are not values from the dataset.

- **Stage boundaries on the charts.** Niger's Stage 2 band starts in **1977**, when its death rate begins a steady decline (27.7 in 1975, 26.7 in 1977, 25.7 in 1980, falling from then on). Bangladesh's Stage 2→3 boundary is at **1980**, when its birth rate begins its sustained fall (45.2 in 1980, 40.7 in 1985, 35.1 in 1990). The "Stage 3 begins" band for Niger starts at **2009**, the year of its largest gap in the series. Real transitions do not have sharp edges, so these are approximate markers.
- **Stage labels in the recap strip** (Niger "Stage 2 → 3", Bangladesh "Stage 3", Sweden "Stage 4", Japan "Stage 5") follow the usual AP Human Geography reading of each country's 2024 rates. Japan's deaths exceed its births, the natural decrease the AP course calls Stage 5.
- **Causes named in captions.** "Vaccines, clean water and health care spread" for falling deaths, and "as more children survive, families choose to have fewer" for falling births, are the standard textbook explanations for Stages 2 and 3. They are not drawn from this dataset and are not a Niger- or Bangladesh-specific causal claim.
- **"1971: war".** The 1971 spike in Bangladesh's death rate is in the WDI data. The label is our attribution to that year's Liberation War.

## Caveats worth teaching

- For countries without full birth and death registration, including Niger and, for most of this period, Bangladesh, WDI's figures are UN Population Division **modeled estimates** built from censuses and surveys, not direct counts. WDI's own metadata notes these "are subject to sampling errors and recall errors."
- Crude rates depend on age structure. Japan's high death rate reflects an old population, not poor health. That is why its deaths can exceed its births even though life expectancy is very high.

## Fonts and design

- Inter (SIL Open Font License) and JetBrains Mono (SIL Open Font License). The renderer uses the copies installed on the system, so no font files are bundled here.
- Palette: paper `#F3ECDF`, ink `#22201C` (13.8:1 on paper), muted `#5E574D` (6.1:1), teal accent `#0B6E73` (5.1:1). All text meets the WCAG AA contrast ratio of 4.5:1.
