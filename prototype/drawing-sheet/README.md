# Prototype: code-generated shop drawings

Throwaway prototype for [Pick the CAD toolchain and handoff formats](https://github.com/uf-cpe-design-lab/kagu/issues/9). **Placeholder dimensions.** Not the production drafting module, but the pattern it should follow.

`sheet.py` builds a parametric Carcass in build123d and draws a 3-sheet A3 set straight from the model:

1. **Notation & conventions**: every symbol used in the set, drawn by the same helpers.
2. **Carcass assembly**: front/right/top views, exploded view with Part Label balloons, installed-screw marks, cut list, hardware table, assembly sequence.
3. **Part A (side, left)**: inside face with hole ordinates and joint notes, hatched section details of every dado/rabbet (depths dimensioned), machining sequence, proposed Part Label mark.

Output: [`out/carcass_set.pdf`](out/carcass_set.pdf) (vector, selectable text), PNG previews, `carcass.glb` (3D model the QR code is meant to link to).

## Run

Needs the cairo system library (`brew install cairo`, or zerobrew).

```sh
uv venv .venv && uv pip install --python .venv/bin/python -r requirements.txt
DYLD_FALLBACK_LIBRARY_PATH=/opt/zerobrew/lib .venv/bin/python sheet.py   # ~25 s
```

## Lessons for the real `kagu.drafting` module

- Emit **real SVG text**, not build123d `Text` geometry: glyph outlines took ~145 s of a 178 s build; real text is near-instant and selectable in the PDF.
- Dimensions are labelled with true model values (the drawing is scaled).
- Balloons: leader to the point deepest inside the part's cut face; balloon at the nearest spot clear of dimensions, notes and other parts.
- Hidden lines that coincide with visible edges must be filtered out.
- Details are **numbered** so they never collide with letter Part Labels.

## Layout prototype (chosen design)

`layout.py` builds the instrument Cabinet layout: **40" worktop, 600 mm deep, 1200 mm wide, two instrument sets in the low bay, two Drawer columns (13 Drawers, 12 × 12 units, "spaced" fronts)**, sides and back rising 75 mm above the worktop with a rounded front corner, two printed side handles per side, printed wall standoffs, bent aluminium pulls flush in the top edge of each front, and top-edge accessory pockets.

- [`out/layout/layout.pdf`](out/layout/layout.pdf): front + right-side elevation (mm and inches).
- `out/layout/layout_3d.html`: interactive 3D (click a drawer to open it). It fetches the GLB, so serve the folder: `python3 -m http.server -d out/layout 8765` then open `http://127.0.0.1:8765/layout_3d.html`. Only the chosen variant's GLB is committed; run `layout.py` to regenerate the 36"/500 mm/7U variants.
- Side handle: [Simple Handle – 12 Sizes | Handle for M6 Screws](https://www.printables.com/model/1531320-simple-handle-12-sizes-handle-for-m6-screws) by **Emkatech (Mike)**, CC BY-NC 4.0, 180 mm size. Not redistributed here: download it and extract to `../ext-handle/` (path used by `layout.py`).

## Printable / fabrication files (`out/print/`)

| File | What |
|---|---|
| `bin_*.stl`, `baseplate_5x2.stl` | Gridfinity test bins for the drawer plan (made by `gen_bins.py` with [gridfinity_build123d](https://github.com/Ruudjhuu/gridfinity_build123d), which needs **build123d 0.9.1** in its own venv) |
| `standoff_base_PETG.stl`, `standoff_cap_TPU.stl` | Wall standoff: PETG/ASA cone + TPU snap-in cap (`printed_parts.py`) |
| `drawer_pull_flat_5052_2mm_waterjet.dxf` | Drawer pull waterjet blank, 160 × 34.8 mm, 2 mm 5052-H32; layer `CUT` + bend line on its own layer (45°, R2 inside, K = 0.33). Bend a test piece first. |
| `drawer_pull_ref.stl` | Bent pull, for reference / fit checks |
| `handle_300_PETG.stl` | Superseded custom D-handle (kept for reference) |

Pull finish: tumble flat blanks → bend → Scotch-Brite → satin clear (coatings only after bending).
