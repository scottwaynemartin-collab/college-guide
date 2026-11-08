# Unit 2 shared stimulus data + every computed answer (rates, ratios, densities, doubling times).
# assemble.py execs this first; p1.py, p2.py and exam.py read these names, and verify(byid) re-checks
# every keyed numeric answer against the stimulus objects that actually ship in unit2.json.

AGES = ["0–4", "5–9", "10–14", "15–19", "20–24", "25–29", "30–34", "35–39", "40–44",
        "45–49", "50–54", "55–59", "60–64", "65–69", "70–74", "75–79", "80+"]


def _pyramid(shares, male_frac):
    """shares: both-sex weights per age group; male_frac: male share of each group.
    Returns (male, female) lists in percent of TOTAL population, 1 decimal, summing to exactly 100.0."""
    tot = sum(shares)
    m = [s / tot * 100 * f for s, f in zip(shares, male_frac)]
    w = [s / tot * 100 * (1 - f) for s, f in zip(shares, male_frac)]
    mr = [round(v, 1) for v in m]; wr = [round(v, 1) for v in w]
    diff = round(100 - sum(mr) - sum(wr), 1)
    # push any rounding remainder into the largest bar so totals are exactly 100.0
    k = max(range(len(mr)), key=lambda i: mr[i])
    mr[k] = round(mr[k] + diff, 1)
    assert abs(sum(mr) + sum(wr) - 100) < 1e-6, sum(mr) + sum(wr)
    return mr, wr


# Country A: expansive (Stage 2-style) — exam set A
PYR_A_M, PYR_A_F = _pyramid(
    [16.0, 14.2, 12.6, 10.9, 9.2, 7.7, 6.4, 5.3, 4.3, 3.5, 2.8, 2.2, 1.7, 1.3, 0.9, 0.6, 0.4],
    [0.506, 0.505, 0.504, 0.503, 0.502, 0.501, 0.5, 0.499, 0.498, 0.497, 0.495, 0.49, 0.485, 0.475, 0.465, 0.455, 0.44])
# Country B: aging / constrictive — exam set B
PYR_B_M, PYR_B_F = _pyramid(
    [3.4, 3.8, 4.1, 4.3, 4.6, 4.9, 5.2, 5.6, 6.2, 7.2, 7.8, 7.4, 6.9, 6.3, 6.0, 5.2, 6.9],
    [0.513, 0.513, 0.512, 0.512, 0.511, 0.51, 0.508, 0.505, 0.502, 0.5, 0.497, 0.493, 0.485, 0.475, 0.46, 0.43, 0.36])
# Country C: low births with a large cohort now aged 55–69 — practice P09
PYR_C_M, PYR_C_F = _pyramid(
    [4.6, 4.9, 5.1, 5.3, 5.5, 5.8, 6.2, 6.4, 6.1, 5.8, 6.4, 8.3, 8.6, 8.0, 5.2, 3.6, 4.2],
    [0.512, 0.512, 0.511, 0.511, 0.51, 0.509, 0.507, 0.505, 0.503, 0.5, 0.497, 0.493, 0.487, 0.478, 0.465, 0.445, 0.38])
# Country G: large in-migration of working-age men — practice P10 (given directly as male/female weights)
_g_m = [2.6, 2.5, 2.2, 2.0, 6.5, 10.2, 10.8, 9.1, 6.8, 4.6, 3.0, 1.7, 0.8, 0.4, 0.2, 0.1, 0.1]
_g_f = [2.5, 2.4, 2.1, 1.8, 2.0, 2.6, 2.8, 2.4, 1.8, 1.3, 0.9, 0.6, 0.4, 0.3, 0.2, 0.1, 0.1]
PYR_G_M, PYR_G_F = _pyramid([a + b for a, b in zip(_g_m, _g_f)], [a / (a + b) for a, b in zip(_g_m, _g_f)])


def pyr_stats(m, f):
    under15 = sum(m[:3]) + sum(f[:3])
    work = sum(m[3:13]) + sum(f[3:13])
    over65 = sum(m[13:]) + sum(f[13:])
    return dict(under15=round(under15, 1), work=round(work, 1), over65=round(over65, 1),
                dep=round((under15 + over65) / work * 100, 1), male=round(sum(m), 1))


# ---- DTM line chart, Country M (exam set C) ----
DTM_M_YEARS = ["1800", "1825", "1850", "1875", "1900", "1925", "1950", "1975", "2000", "2025"]
DTM_M_CBR = [38, 38, 38, 37, 34, 28, 21, 15, 12, 11]
DTM_M_CDR = [36, 35, 29, 23, 18, 14, 11, 10, 9, 9]
# ---- DTM line chart, Country K (practice P18) ----
DTM_K_YEARS = ["1900", "1920", "1940", "1960", "1980", "2000", "2020"]
DTM_K_CBR = [44, 44, 45, 44, 35, 26, 19]
DTM_K_CDR = [38, 33, 26, 18, 11, 8, 7]
# ---- Malthus test, Country N (practice P22): index, 1960 = 100 ----
MAL_YEARS = ["1960", "1970", "1980", "1990", "2000", "2010", "2020"]
MAL_POP = [100, 125, 155, 185, 213, 240, 265]
MAL_FOOD = [100, 135, 180, 230, 285, 340, 395]

# ---- Country Z provinces (practice P04 map) ----
PROV_Z = [  # name, area sq km, population
    ("Coastal Province", 20000, 8_200_000),
    ("River Valley Province", 30000, 5_400_000),
    ("Highland Province", 60000, 2_100_000),
    ("Desert Province", 140000, 420_000)]

# ---- Country T broad age groups (practice P31), millions ----
AGE_T = dict(young=9.6, work=40.0, old=14.4)

# ---- Subnational age structure (practice P11), percent ----
COUNTY_ROWS = [
    ("Country (national total)", [18, 13, 52, 17]),
    ("County U", [11, 38, 41, 10]),
    ("County R", [10, 7, 41, 42]),
    ("County F", [21, 12, 47, 20])]

# ---- Female education vs TFR (practice P27), hypothetical districts ----
EDU_CATS = ["Under 20%", "20–39%", "40–59%", "60–79%", "80% or more"]
EDU_TFR = [5.9, 4.8, 3.6, 2.6, 1.9]

# ---- Distance decay (practice P35), thousands of migrants ----
DIST_CATS = ["Under 50 km", "50–199 km", "200–499 km", "500–999 km", "1,000 km or more"]
DIST_VALS = [42, 24, 12, 6, 4]

# ---------------- REAL DATA (World Bank WDI, accessed Nov 8, 2026; raw JSON saved in u2/data_raw/) ----------------
# P02: 2024 population (SP.POP.TOTL), land area sq km (AG.LND.TOTL.K2), arable land hectares (AG.LND.ARBL.HA)
WB_DENSITY_2024 = {
    "Egypt": (116_538_258, 995_450, 3_274_000),
    "Netherlands": (17_993_485, 33_670, 1_003_000),
    "Japan": (123_975_371, 364_500, 4_023_000),
    "Canada": (41_262_329, 8_788_700, 38_064_000)}
# P13 and E07: 2024 crude birth rate, crude death rate (per 1,000), population growth (annual %)
WB_VITAL_2024 = {
    "Niger": (41.42, 8.719, 3.28101480132484),
    "India": (15.981, 6.587, 0.890706546985984),
    "Canada": (8.9, 7.9, 2.9844051252484),
    "Germany": (8.1, 12.1, 0.274957829184881),
    "Japan": (5.7, 13.3, -0.435651699326323)}
# P40: 2024 personal remittances received, current US$ (BX.TRF.PWKR.CD.DT) and % of GDP (BX.TRF.PWKR.DT.GD.ZS)
WB_REMIT_2024 = {
    "India": (137674533895.686, 3.66076475144487),
    "Mexico": (67908368512, 3.70984785874569),
    "Philippines": (40279405932.4327, 8.72469619181708),
    "Nepal": (11254463372.2778, 25.9924855623944),
    "Tajikistan": (6801890973.46099, 47.1531186167275),
    "Tonga": (255166174.842972, 39.4086189622236)}
# E14: Latin America & Caribbean total fertility rate (SP.DYN.TFRT.IN, aggregate LCN)
WB_LCN_TFR = {"1970": 5.18421280645098, "2020": 1.85875827927084}


def density_rows():
    rows = []
    for c, (pop, land, arable_ha) in WB_DENSITY_2024.items():
        arable = arable_ha / 100  # hectares -> sq km
        rows.append((c, pop, land, arable, pop / land, pop / arable))
    return rows


def rni_pct(cbr, cdr):
    return (cbr - cdr) / 10


def doubling(rni):
    return 70 / rni


# hypothetical text-only calculations
P14 = dict(cbr=31, cdr=7)            # Country Q
E06 = dict(cbr=26, cdr=6)            # Country R
E19 = dict(pop=60_000_000, land=400_000, arable_share=0.15, farmers=24_000_000)  # Country X


def report():
    out = []
    for nm, (m, f) in {"A": (PYR_A_M, PYR_A_F), "B": (PYR_B_M, PYR_B_F), "C": (PYR_C_M, PYR_C_F), "G": (PYR_G_M, PYR_G_F)}.items():
        out.append(f"Pyramid {nm}: {pyr_stats(m, f)}")
    out.append("DTM M gaps " + str([b - d for b, d in zip(DTM_M_CBR, DTM_M_CDR)]))
    out.append("DTM K gaps " + str([b - d for b, d in zip(DTM_K_CBR, DTM_K_CDR)]))
    out.append("Malthus food per person 2020 vs 1960: %.2f" % (MAL_FOOD[-1] / MAL_POP[-1]))
    tz = sum(p for _, _, p in PROV_Z); az = sum(a for _, a, _ in PROV_Z)
    out.append("Country Z: " + ", ".join(f"{n} {p / a:.1f}" for n, a, p in PROV_Z) + f"; national {tz / az:.2f}; coast+valley share of people {(PROV_Z[0][2] + PROV_Z[1][2]) / tz:.3f} on {(PROV_Z[0][1] + PROV_Z[1][1]) / az:.2f} of land")
    t = AGE_T; out.append("Country T dependency ratio %.1f, youth %.1f, old-age %.1f, dependents/total %.1f" % (
        (t['young'] + t['old']) / t['work'] * 100, t['young'] / t['work'] * 100, t['old'] / t['work'] * 100, (t['young'] + t['old']) / (t['young'] + t['work'] + t['old']) * 100))
    for c, pop, land, ar, a, p in density_rows():
        out.append(f"{c}: arithmetic {a:.2f}, physiological {p:.1f}, ratio {p / a:.1f}, arable share {ar / land * 100:.2f}%")
    for c, (b, d, g) in WB_VITAL_2024.items():
        r = rni_pct(b, d)
        out.append(f"{c}: RNI {r:.3f}% growth {g:.3f}% gap {g - r:.3f}" + (f" doubling {doubling(r):.1f}" if r > 0 else ""))
    for c, (usd, pct) in WB_REMIT_2024.items():
        out.append(f"{c}: ${usd / 1e9:.2f}B, {pct:.1f}% of GDP")
    for k, v in (("P14", P14), ("E06", E06)):
        r = rni_pct(v['cbr'], v['cdr']); out.append(f"{k}: RNI {r}% doubling {doubling(r):.2f}")
    x = E19; ar = x['land'] * x['arable_share']
    out.append(f"E19: arithmetic {x['pop'] / x['land']}, arable {ar}, physiological {x['pop'] / ar}, agricultural {x['farmers'] / ar}")
    out.append("LCN TFR 1970->2020: %.2f -> %.2f (%.0f%% drop)" % (WB_LCN_TFR['1970'], WB_LCN_TFR['2020'], (1 - WB_LCN_TFR['2020'] / WB_LCN_TFR['1970']) * 100))
    return out


if __name__ == "__main__":
    print("\n".join(report()))
