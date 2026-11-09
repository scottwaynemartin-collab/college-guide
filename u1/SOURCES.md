# Unit 1 bank: sources and what was verified

All stimulus data in Unit 1 are **hypothetical** (labeled "Hypothetical data" or "Hypothetical map" in each title or
source line). No real-world statistics appear in any table, chart, or map. The real-world facts used in stems,
explanations, and rationales, and the formulas behind the projection-grid stimulus, are listed below.
Every number is rechecked by `u1/verify.py`, which `u1/assemble.py` runs on every build.

| Where | Claim | Source (URL) | What was checked |
|---|---|---|---|
| U1-P04 | Africa is about 14 times as large as Greenland | Greenland 2,166,086 sq km: CIA, The World Factbook, as quoted by IndexMundi (https://www.indexmundi.com/greenland/area.html; search snippet "Area: total: 2,166,086 sq km"); the archived Factbook "Country Comparison: Area" hosted by MIT (link in the P07 row) is the reviewer-recommended copy. (The cia.gov archive link used earlier now redirects to a notice that the Factbook has ended, so it was dropped.) Africa about 30,365,000 sq km: Encyclopaedia Britannica, "Africa" (https://www.britannica.com/place/Africa) | 30,365,000 / 2,166,086 = 14.02 (script) |
| U1-P07 | Canada has about three times India's area | CIA World Factbook, Country Comparison: Area (mirror: https://start.csail.mit.edu/mirror/cia.gov/library/publications/the-world-factbook/rankorder/2147rank.html): Canada 9,984,670 sq km; India 3,287,263 sq km | 9,984,670 / 3,287,263 = 3.04 (script) |
| U1-E03, E04 stimulus | Original spherical graticules computed from the standard Mercator and cylindrical equal-area equations; coordinates rounded to 0.1 px. Map 1 parallels use the Mercator formula, y = R ln tan(π/4 + φ/2) | CRC Concise Encyclopedia of Mathematics, "Mercator Projection" (https://archive.lib.msu.edu/crcmath/math/math/m/m187.htm), formula (2); same as Snyder, *Map Projections: A Working Manual*, USGS PP 1395 (https://pubs.usgs.gov/publication/pp1395) | Grid width 300 px. Gaps between 15° parallels grow toward the poles (12.6 → 33.9 px); gap ratios match the formula within 1.2% (script) |
| U1-E03, E04 stimulus | Map 2 parallels spaced by the cylindrical equal-area formula, x = (λ − λ0) cos φs, y = sin φ / cos φs, with standard parallels at 45° N and 45° S (Gall-Peters) | CRC Concise Encyclopedia of Mathematics, "Cylindrical Equal-Area Projection" (https://archive.lib.msu.edu/crcmath/math/math/c/c910.htm); MathWorks Mapping Toolbox, "Gall Orthographic Projection" (https://au.mathworks.com/help/map/gortho.html): "the standard parallel is by definition fixed at 45º" and "It is equal-area, but distortion of shape increases with distance from the standard parallels" | Gaps shrink toward the poles (24.7 → 9.5 px); band heights are proportional to the difference of sines, i.e., equal-area (script); shapes above 45° are flattened north–south (E04 key) |

## Facts stated without a number (standard course content, no external data)
- Mercator (1569) keeps compass bearings as straight lines and local shapes; area grows toward the poles. Gall-Peters
  is equal-area; Robinson is a compromise projection; Goode's homolosine is an interrupted equal-area projection;
  an azimuthal equidistant map shows true distance and direction from its center only.
- The U.S. census is taken every ten years and is used to reapportion the 435 House seats by formula; faster growth can,
  but need not, change a state's seats; every state has two senators (E10).
- Some countries set language regions by law (for example, Belgium's Constitution, Article 4, sets its linguistic regions),
  which is why E23's rationale says the map shows language use, not a legal boundary.
- Dutch polders are land reclaimed with dikes and drainage (P22). Coal is nonrenewable; wind is renewable (P23).
- Sustainability wording follows the common "meet present needs without compromising future generations" definition (E17).
- Environmental determinism was influential in the late 1800s and early 1900s and was used to rank societies (P24).

## Hypothetical stimuli (all arithmetic in `u1/verify.py`)
P02 dot-density map (22 squares east of the river, 4 west); P03 contour map (line spacing west 18 < south 30 <
north 38 < east 70 px; J, K, L, M each between the 120 m and 140 m lines; N on the east side between the 100 m and
120 m lines, where spacing is also 70 px); P34 linear settlement map (24 farmhouses, 12 per bank, each 28 px from the
river centerline, spanning the valley); P06 business rates (Baker 8.0 per 1,000 is
highest); P11 bus-route data sets; P12 children under 5 (Riverside has the largest 2020 count, largest absolute and
percent growth); P14 floodplain map (8 homes + school inside the floodplain; hospital and 4 homes on east high
ground); P17 customer shares sum to 100 and fall with distance; P18 travel times fall; P25 groundwater depth rises;
P27 regional unemployment averages to the 6.0% national rate (North 140,000 vs South 260,000 unemployed);
P32 "Up North" shares rise steadily; E08 land cover sums to 100 in both years; E13 commuting map (shares fall with
distance; the hypothetical boundary includes towns whose share of workers commuting to City M is at least 25%, using
the rule selected for this map, and excludes the others; scale bar = 10 km); E18 provinces sum to
the nation and districts sum to Province 2 in both years, and every % change matches.
