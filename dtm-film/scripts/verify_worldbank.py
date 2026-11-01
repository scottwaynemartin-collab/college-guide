#!/usr/bin/env python3
"""Check data/wdi_cbr_cdr.csv against the live World Bank API.

Usage: python3 -I scripts/verify_worldbank.py
Exits non-zero if any value differs or is missing.
"""
import csv, json, pathlib, sys, urllib.request

CSV = pathlib.Path(__file__).resolve().parent.parent / "data" / "wdi_cbr_cdr.csv"
rows = list(csv.DictReader(open(CSV)))
isos = sorted({r["iso3"] for r in rows})
wb = {}
for ind, key in [("SP.DYN.CBRT.IN", "crude_birth_rate_per_1000"), ("SP.DYN.CDRT.IN", "crude_death_rate_per_1000")]:
    url = (f"https://api.worldbank.org/v2/country/{';'.join(isos)}/indicator/{ind}"
           "?format=json&per_page=2000&date=1960:2024")
    meta, data = json.load(urllib.request.urlopen(url, timeout=60))
    print(f"{ind}: World Bank last updated {meta.get('lastupdated')}")
    for d in data:
        wb[(d["countryiso3code"], d["date"], key)] = d["value"]

bad = 0
for r in rows:
    for key in ("crude_birth_rate_per_1000", "crude_death_rate_per_1000"):
        live = wb.get((r["iso3"], r["year"], key))
        if live is None or abs(live - float(r[key])) > 1e-9:
            bad += 1
            print(f"MISMATCH {r['iso3']} {r['year']} {key}: ours {r[key]}, World Bank {live}")
print(f"checked {2 * len(rows)} values: {'all match' if not bad else f'{bad} differ'}")
sys.exit(1 if bad else 0)
