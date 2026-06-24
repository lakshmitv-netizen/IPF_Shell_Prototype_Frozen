# Surgical patches

The embedded apps (`cp-app`, `cp-grid-app`, `setup-app`) are minified CRA builds.
Features were added by precise string replacements in `static/js/main.*.js` rather
than rebuilding from source. This folder documents every change so they are
auditable and re-appliable to a fresh upstream build.

Each app's bundle: `docs/<app>/static/js/main.7c479505.js`.

## Already baked into this snapshot (in `cp-app` and `cp-grid-app`)

### 1. Type-to-edit + Tab/Enter navigation
- `td onKeyDown`: type a digit on a selected cell → enter edit mode + replace value.
- caret: place caret at end on type-over (`setSelectionRange`) instead of select-all.
- Tab/Shift+Tab branch → set nav direction left/right and `preventDefault`.
- Enter branch → set nav direction "down".
- `handleSaveCell` → after commit, dispatch a synthetic `Tab`/`ArrowDown` KeyboardEvent
  to move selection using the grid's own navigation.

### 2. Delta indicators: triangles → arrow marks
- Increase (orange): `<polygon points="7,2.35 12.35,11.9 1.65,11.9">`
  → `<path d="M7 12.5V2.2M3 6.5L7 2.2L11 6.5" stroke=... fill="none">`
- Decrease (blue): `<polygon points="7,11.65 1.65,2.1 12.35,2.1">`
  → `<path d="M7 1.5V11.8M3 7.5L7 11.8L11 7.5" stroke=... fill="none">`

### 3. Compact week headers + custom tooltip
- builder: also emit `shortLabel` e.g. `W1(1/1/26)`.
- `visibleTimeHeaders` map: carry through `granularity` and `shortLabel`.
- render: when `granularity==="week"` and column width `< 170px`, show `shortLabel`.
- `<th>`: custom fixed-position tooltip (with nubbin, drop-shadow) on hover showing
  the full week label, replacing the native `title`.

### 4. Week time-period (Start/End) filter
- Week branch in the date-range filter computes each week's actual start/end dates from
  the plan config and keeps only weeks overlapping the selected Start/End range
  (inclusive; dates parsed as local calendar dates).

## NOT applied here — optional, for later

### 5. "Measure subsets" rename + show-all-measures behavior
See `measure_subsets.py`. Two parts:
- Rename: "Measure category" → "Measure subsets", "N Categories Selected" →
  "N Subset(s) Selected", "Select Measure Category" → "Select Measure Subset",
  header-picker + summary strings → "subset" wording.
- Behavior: stop narrowing the measure list to the plan config's curated
  `selectedMeasureIds`; show **all** measures of the selected subset(s) by default.
  Configure-unchecking then hides specific measures.

Run (from repo root) to apply to this snapshot:

```bash
python3 patches/measure_subsets.py
```
