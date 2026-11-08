# Wi-Fi Site Survey — Guide

A starter guide for running a basic Wi-Fi site survey. This is a
learning template — adapt the steps to your own organisation's
policy. All locations, access points, and readings below are
fictional.

## The five steps

### 1. Plan

Sketch the floor plan and mark the survey points: one per room or
every 10–15 metres in open space, plus stairwells, lifts, and any
spot people complain about. Note the existing access points and
their channels. Pick a quiet time for the walk-through so the
readings reflect normal use, not a one-off spike.

### 2. Measure

At each point, stand still for a few seconds and record:

- **Signal strength (dBm)** on 2.4 GHz and on 5 GHz — the lower
  (more negative) the number, the weaker the signal.
- **Channel** in use at that point, and whether neighbouring
  networks share it.
- **Nearest access point** (use a label like "AP-1", never a real
  MAC address or real device name in a shared template).
- **Interference** — thick walls, metal shelves, microwaves,
  Bluetooth devices, or a neighbouring network on the same
  channel.
- **Notes** — anything odd, like a reading that changes when a
  door closes.

One row per point in `wifi-site-survey-template.csv`.

### 3. Map

Plot the readings on the floor plan. Colour each point by its
rating (excellent / good / fair / weak / dead zone) so the pattern
is visible at a glance. The diagram in `docs/diagram.png` shows
the idea on a sample floor: green where coverage is good, amber
where it is fair, red where it is a dead zone. Your real map will
look different — this one is only an example.

### 4. Analyse

Look for the patterns, not single readings:

- **Dead zones** — points below -80 dBm. These need a new access
  point or a repositioned one.
- **Weak spots** — points between -70 and -80 dBm. Check what is
  between them and the nearest access point (a lift shaft, a
  metal cabinet, a thick wall).
- **Channel overlap** — two access points on the same channel
  covering the same area will fight each other. On 2.4 GHz, use
  only channels 1, 6, and 11; on 5 GHz, spread across the
  available channels.
- **Band balance** — 5 GHz is faster but reaches less far than
  2.4 GHz. A point that is fine on 2.4 GHz but weak on 5 GHz
  usually just needs an access point closer by.

### 5. Recommend

Write down what changes and why, in plain language:

- "Add one access point in the Sample Meeting Room — both bands
  read below -80 dBm there."
- "Move AP-2 from the corridor into the Sample Store Room — the
  store room is a dead zone and the corridor is already covered."
- "Change AP-3 from channel 6 to channel 11 — it overlaps with
  AP-1 on channel 6."

Keep the recommendation list short and tied to the readings. A
recommendation without a reading behind it is a guess.

## Common mistakes (starter notes)

- Measuring only near the access points — the weak spots are
  always at the edges.
- Taking one reading and treating it as final — walk the point
  twice, at different times if you can.
- Ignoring 2.4 GHz interference from microwaves and Bluetooth.
- Recording a real SSID or password in the survey sheet.
- Placing a new access point where the power and cabling are
  easy, instead of where the dead zone is.

## Adding your own survey points

Add a row to `wifi-site-survey-template.csv` with: point_id,
floor, location, band, signal_dbm, channel, nearest_ap,
interference, rating, and notes. Keep locations fictional in
samples — never commit real floor plans or real network details.

## Sample / Demo notice

All locations and readings here are fictional samples for
learning, labelled "Sample / Demo" in the diagram. This template
does not claim any production use.
