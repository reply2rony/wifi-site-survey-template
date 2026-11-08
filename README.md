# Wi-Fi Site Survey Template — Starter Template

A starter learning template for planning and recording a Wi-Fi site
survey: walk a building, measure signal strength at sample points,
note interference and dead zones, and decide where access points
should go. It is a checklist plus a small tracking CSV, so an IT
team can record each survey point and summarise coverage — with
fictional sample data only. Sample content only — no real company
data, no invented metrics, and no claim of production use.

## What it is

- `docs/survey-guide.md` — the survey workflow and the checklist:
  plan, measure, map, analyse, recommend.
- `wifi-site-survey-template.csv` — the tracking sheet in CSV form,
  so you can copy it, filter it, and add your own survey points.
- `scripts/survey-summary.py` — a starter Python script that
  summarises the CSV by floor and band, and flags dead zones and
  weak-signal points. Labelled a starter learning template; it is
  not a production tool.

## How to use

1. Sketch the floor plan first (or draw a simple grid) and mark the
   survey points you will measure — one row per point in
   `wifi-site-survey-template.csv`.
2. At each point, record the signal strength (dBm) on 2.4 GHz and
   5 GHz, the channel in use, the nearest access point, and any
   interference you notice.
3. Work the checklist in `docs/survey-guide.md` in order — plan,
   measure, map, analyse, recommend.
4. Summarise the sheet from the command line:

```bash
python3 scripts/survey-summary.py wifi-site-survey-template.csv
python3 scripts/survey-summary.py wifi-site-survey-template.csv --floor 1
python3 scripts/survey-summary.py wifi-site-survey-template.csv --band 5ghz
```

## Reading signal strength (starter guide)

| Signal (dBm) | Rating | Meaning |
|--------------|--------|---------|
| -30 to -50   | Excellent | Very strong, close to the access point |
| -50 to -60   | Good | Reliable for most work |
| -60 to -70   | Fair | Usable, but watch for drops |
| -70 to -80   | Weak | Unreliable — consider a new access point |
| Below -80    | Dead zone | Effectively no usable signal |

Ratings above are starter suggestions for a learning template, not a
standard for any real organisation.

## Sample / Demo notice

All locations, access points, and readings in this repo are fictional
samples for learning. The diagram in `docs/diagram.png` is a locally
generated illustration labelled "Sample / Demo" — it is not a
screenshot of a real system, and this template does not claim any
production use.

## License

MIT — see `LICENSE`.
