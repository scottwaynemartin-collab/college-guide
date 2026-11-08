# Unit 1 bank: sources and what was verified

All stimulus data in Unit 1 are **hypothetical** (labeled "Hypothetical data" or "Hypothetical map" in each title or
source line). No real-world statistics appear in any table, chart, or map. The real-world facts used in stems,
explanations, and rationales, and the formulas behind the projection-grid stimulus, are listed below.
Every number is rechecked by `u1/verify.py`, which `u1/assemble.py` runs on every build.

| Where | Claim | Source (URL) | What was checked |
|---|---|---|---|
| U1-P04 | Africa is about 14 times larger than Greenland | Greenland 2,166,086 sq km: CIA World Factbook (https://www.indexmundi.com/greenland/area.html, which quotes the Factbook; archived Factbook GL summary https://www.cia.gov/the-world-factbook/about/archives/2021/static/445b5377c20a6bb8caebb11040ac4395/GL-summary.pdf). Africa about 30,365,000 sq km: Encyclopaedia Britannica, "Africa" (https://www.britannica.com/place/Africa) | 30,365,000 / 2,166,086 = 14.02 (script) |
| U1-P07 | Canada has about three times India's area | CIA World Factbook, Country Comparison: Area (mirror: https://start.csail.mit.edu/mirror/cia.gov/library/publications/the-world-factbook/rankorder/2147rank.html): Canada 9,984,670 sq km; India 3,287,263 sq km | 9,984,670 / 3,287,263 = 3.04 (script) |
| U1-E03, E04 stimulus | Map 1 parallels spaced by the Mercator formula, y = R ln tan(π/4 + φ/2) | CRC Concise Encyclopedia of Mathematics, "Mercator Projection" (https://archive.lib.msu.edu/crcmath/math/math/m/m187.htm), formula (2); same as Snyder, *Map Projections: A Working Manual*, USGS PP 1395 (https://pubs.usgs.gov/publication/pp1395) | Gaps between 15° parallels grow toward the poles (14.3 → 38.4 px); gap ratios match the formula (script) |
| U1-E03, E04 stimulus | Map 2 parallels spaced by the cylindrical equal-area formula, x = (λ − λ0) cos φs, y = sin φ / cos φs, with φs = 45° (Gall-Peters) | CRC Concise Encyclopedia of Mathematics, "Cylindrical Equal-Area Projection" (https://archive.lib.msu.edu/crcmath/math/math/c/c910.htm); MathWorks Mapping Toolbox, "Gall Orthographic Projection" (https://au.mathworks.com/help/map/gortho.html): "the standard parallel is by definition fixed at 45º" and "It is equal-area, but distortion of shape increases with distance from the standard parallels" | Gaps shrink toward the poles (28.0 → 10.8 px); band heights are proportional to the difference of sines, i.e., equal-area (script); shapes above 45° are flattened north–south (E04 key) |

## Facts stated without a number (standard course content, no external data)
- Mercator (1569) keeps compass bearings as straight lines and local shapes; area grows toward the poles. Gall-Peters
  is equal-area; Robinson is a compromise projection; Goode's homolosine is an interrupted equal-area projection;
  an azimuthal equidistant map shows true distance and direction from its center only.
- The U.S. census is taken every ten years and is used to reapportion the 435 House seats; every state has two
  senators (E10).
- Dutch polders are land reclaimed with dikes and drainage (P22). Coal is nonrenewable; wind is renewable (P23).
- Sustainability wording follows the common "meet present needs without compromising future generations" definition (E17).
- Environmental determinism was influential in the late 1800s and early 1900s and was used to rank societies (P24).

## Hypothetical stimuli (all arithmetic in `u1/verify.py`)
P02 dot-density map (22 squares east of the river, 4 west); P03 contour map (line spacing west 18 < south 30 <
north 38 < east 70 px; J, K, L, M each between the same two contours); P06 business rates (Baker 8.0 per 1,000 is
highest); P11 bus-route data sets; P12 children under 5 (Riverside has the largest 2020 count, largest absolute and
percent growth); P14 floodplain map (8 homes + school inside the floodplain; hospital and 4 homes on east high
ground); P17 customer shares sum to 100 and fall with distance; P18 travel times fall; P25 groundwater depth rises;
P27 regional unemployment averages to the 6.0% national rate (North 140,000 vs South 260,000 unemployed);
P32 "Up North" shares rise steadily; E08 land cover sums to 100 in both years; E13 commuting map (shares fall with
distance; towns at 25% or more are inside the dashed line, others outside; scale bar = 10 km); E18 provinces sum to
the nation and districts sum to Province 2 in both years, and every % change matches.
