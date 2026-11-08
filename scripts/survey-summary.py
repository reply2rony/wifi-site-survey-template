#!/usr/bin/env python3
"""Starter learning template: summarise the Wi-Fi site survey.

Usage:
    python3 scripts/survey-summary.py wifi-site-survey-template.csv
    python3 scripts/survey-summary.py wifi-site-survey-template.csv --floor 1
    python3 scripts/survey-summary.py wifi-site-survey-template.csv --band 5ghz

Summarises the CSV by floor and band, and flags dead zones and
weak-signal points. Sample data only; no real company data.
"""
import argparse
import csv
import sys
from collections import Counter


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser(description="Summarise the Wi-Fi site survey.")
    ap.add_argument("csv_file", help="path to wifi-site-survey-template.csv")
    ap.add_argument("--floor", help="filter by floor (e.g. 1)")
    ap.add_argument("--band", help="filter by band (e.g. 5ghz)")
    args = ap.parse_args()

    try:
        rows = load(args.csv_file)
    except FileNotFoundError:
        print(f"File not found: {args.csv_file}")
        sys.exit(1)

    if args.floor:
        rows = [r for r in rows if r.get("floor", "") == args.floor]
    if args.band:
        rows = [r for r in rows if r.get("band", "").lower() == args.band.lower()]

    if not rows:
        print("No matching survey points.")
        sys.exit(0)

    print(f"Survey points: {len(rows)}")
    print()
    print("By rating:")
    for rating, n in Counter(r.get("rating", "") for r in rows).most_common():
        print(f"  {rating}: {n}")
    print()
    print("By floor:")
    for floor, n in Counter(r.get("floor", "") for r in rows).most_common():
        print(f"  floor {floor}: {n}")
    print()
    dead = [r for r in rows if r.get("rating", "").lower() == "dead-zone"]
    weak = [r for r in rows if r.get("rating", "").lower() == "weak"]
    if dead:
        print("Dead zones (below -80 dBm) — need a new or moved access point:")
        for r in dead:
            print(f"  {r['point_id']} ({r['location']}, {r['band']}) — {r['signal_dbm']} dBm, nearest {r['nearest_ap']}")
    else:
        print("No dead zones.")
    print()
    if weak:
        print("Weak points (-70 to -80 dBm) — check what blocks the signal:")
        for r in weak:
            print(f"  {r['point_id']} ({r['location']}, {r['band']}) — {r['signal_dbm']} dBm, {r['interference']}")
    else:
        print("No weak points.")


if __name__ == "__main__":
    main()
