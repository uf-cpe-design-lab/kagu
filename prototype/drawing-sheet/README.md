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
