# IPF_Shell Prototype — Frozen Snapshot

A **self-contained, frozen copy** of the IPF_Shell forecasting/planning prototype,
captured **exactly as deployed on Parag's GHE Pages site**.

- **Source ref:** `parag-trivedi/IPF_Shell` `origin/main` @ `a9bf6f2`
  (commit: "Grid time-period filter: apply Start/End range to week columns")
- **Snapshot date:** 2026-06-24
- **Purpose:** an insulated prototype that will **not** be affected by any upstream
  changes the team makes to Parag's repo or to the source projects. It has no link
  to the Parag remote.

## What's inside

```
docs/                     ← the complete built static site (this IS the prototype)
  index.html              ← outer shell (Vite build: assets/index-DONjPxRY.js)
  assets/                 ← shell JS/CSS + images
  cp-app/                 ← Commercial Planning grid   (CRA build, minified)
  cp-grid-app/            ← Platform - Grid             (CRA build, minified)
  setup-app/              ← CPM Setup                   (CRA build, minified)
  *.svg / *.html          ← icons + supporting docs
patches/                  ← documentation of every surgical change (see patches/README.md)
```

> The three embedded apps are **minified build output**. They are edited via
> surgical string patches (see `patches/`), not from clean source. This is by design:
> the live prototype only ever existed as this built artifact.

## Features baked into this snapshot

All of the following were already applied to the deployed bundles and are present here:

1. **Type-to-edit** in grid cells (type to enter edit mode + replace value; Enter/Tab/✓ commit, Esc cancels; Enter→cell below, Tab→next cell).
2. **Delta indicators** rendered as up/down **arrow marks** (↑/↓) instead of solid triangles.
3. **Compact week headers + tooltip** — narrow columns show `W1(1/1/26)`, hover shows the full `Week 1 (Jan 1 - Jan 7)` label.
4. **Week time-period filter** — Start/End date range correctly filters week columns (inclusive boundaries).

## NOT included (intentionally)

- **"Measure subsets" rename + behavior change** — deliberately excluded from this
  snapshot. Provided as an optional, not-yet-applied script in
  `patches/measure_subsets.py` to apply later if desired.

## Run locally

```bash
cd docs
python3 -m http.server 4188
# open http://localhost:4188/#/home
```

(For development against an always-fresh copy, use a no-cache static server.)

## Deploy (GitHub Pages)

Push this repo to your own remote and set **Pages → Source → branch `main`, folder `/docs`**.
The site will be served identically to the Parag link, at your own URL.
