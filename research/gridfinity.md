# Gridfinity spec and ecosystem

Research for [#6](https://github.com/uf-cpe-design-lab/kagu/issues/6) on the [wayfinder map #1](https://github.com/uf-cpe-design-lab/kagu/issues/1).
Researched 2026-11-08. Terms follow `GLOSSARY.md` (Drawer, Baseplate, Bin, Shadow Bin).

## TL;DR

- The grid is **42 mm**, the height unit is **7 mm**, and a Bin is **42·N − 0.5 mm** wide. A thin Baseplate is **42·N mm** and **4.65 mm** tall in Zack Freedman's original models, or **5.0 mm** in gridfinity-rebuilt. The Bin's stacking lip adds **4.4 mm** above 7·h.
- **Drawer interior:** `W = 42·N + 2·c` and `D = 42·M + 2·c`, where `c` is the side clearance, about 0.5–1.0 mm per side for plywood. Any larger slack goes into Baseplate padding or printed spacers.
- **Drawer interior height:** at least `z0 + 7·h + 4.4 + c_top`. `z0` is how high the Bin's bottom sits above the Drawer floor: 0 for a thin Baseplate, and about 6.4–6.75 mm for a thick magnet, weighted or screw-together Baseplate.
- **Prusa XL:** the bed is 360 × 360 mm (Prusa's spec and PrusaSlicer's bed shape agree). The largest one-piece Baseplate is **8 × 8 units (336 × 336 mm)**. Bigger Baseplates are printed as tiles and joined with puzzle connectors (GridFlock), horizontal screws (rebuilt "screw together"), or Refined connector clips. Tiles can also just be butted together and held by the Drawer walls, or screwed to the Drawer floor.
- **Code-CAD:** `Ruudjhuu/gridfinity_build123d` (MIT) is a native build123d library. The geometry is simple enough to keep as constants in kagu's own build123d code. GridFlock or gridfinity-rebuilt can produce the files that actually get printed.
- **Shadow Bins:** Tracefinity (MIT, self-hosted) or Tooltrace (hosted, free tier). Both scale from a sheet of paper and export Gridfinity STLs; Tracefinity also exports SVG outlines.

## 1. Where the "spec" comes from

There is no formal, versioned standard. The geometry is whatever Zack Freedman's original models used. He released them in his video ["Gridfinity: Your Ultimate Modular Workshop is FREE!"](https://www.youtube.com/watch?v=ra_9zU-mnl8) under the MIT license, per [gridfinity.xyz](https://gridfinity.xyz/).

- The [gridfinity.xyz specification page](https://gridfinity.xyz/specification/) and its source repo [gridfinity-unofficial/specification](https://github.com/gridfinity-unofficial/specification) are a draft, marked "Draft / WIP!". They give only the headline numbers: a 42×42×7 mm grid, Bins 41.5 mm square ("0.5mm tolerance"), a 4.75 mm Bin foot, Bin corners "3.75", a 42×42 Baseplate cell with "8.0" corners, a "5mm" Baseplate, 6×2 mm magnets, and M3 screws.
- [Stu142/Gridfinity-Documentation](https://github.com/Stu142/Gridfinity-Documentation) has the most complete dimensioned drawings (FreeCAD, 2023-11-10). Its section header says they show "the specifications of Zack's original models". This document's profile numbers come from the dimension text in its `drawing_svg/*.svg` files.
- [kennetek/gridfinity-rebuilt-openscad](https://github.com/kennetek/gridfinity-rebuilt-openscad) `src/core/standard.scad` and `src/core/gridfinity-baseplate.scad` encode the same profiles, cite gridfinity.xyz, and are the de-facto reference implementation. [GridFlock](https://github.com/yawkat/gridflock) uses its Baseplate cutter.
- Zack's own Printables/Thangs pages could not be fetched (Printables returned HTTP 403). The original-model numbers were cross-checked through Stu142's drawings and the rebuilt source instead of read from Zack's files.

**Implementations disagree slightly.** Zack's Baseplate profile, per Stu142, is 4.65 mm tall. gridfinity-rebuilt adds 0.35 mm of clearance under the profile, so its thin Baseplate is 5.0 mm. [cq-gridfinity](https://github.com/michaelgale/cq-gridfinity) uses a 4.75 mm Baseplate profile (0.7 / 1.8 / 2.25) and a separate `GR_BASE_CLR = 0.25`. All of them interoperate in practice.

## 2. Geometry table

All values are in mm. "Zack" means Zack's original models as drawn by Stu142; "rebuilt" means gridfinity-rebuilt-openscad `main`.

### Grid and outline

| Item | Value | Source |
|---|---|---|
| Grid pitch (X and Y) | 42 | Stu142 `baseplate_total_width`; rebuilt `GRID_DIMENSIONS_MM = [42, 42]` |
| Height unit ("U") | 7 | Stu142 `bin_bottom_profile` ("U1 = 7"); rebuilt `z_snap` |
| Half-grid pitch (optional) | 21 | rebuilt `half_grid` (grid / 2) |
| Bin outer size | 42·N − 0.5 (1U = 41.5; 2U = 83.5; 4U = 167.5) | Stu142 `bin_total_width`; rebuilt `BASE_TOP_DIMENSIONS = [41.5, 41.5]` |
| Bin-to-cell clearance | 0.25 per side (0.5 total) | rebuilt `BASE_GAP_MM`; gridfinity.xyz "0.5mm tolerance" |
| Baseplate outer size | 42·N exactly (before any padding) | Stu142; rebuilt `grid_size * length` |
| Bin outer corner radius | R3.75 (top of foot and wall) | Stu142 `bin_radius`; rebuilt `BASE_TOP_RADIUS = 7.5/2` |
| Bin foot corner radii | R1.6 (vertical band), R0.8 (bottom) | Stu142 `bin_radius`; rebuilt `BASE_BOTTOM_RADIUS` = 3.75 − 2.95 |
| Baseplate cell corner radii | R4 (top), R1.85 (vertical band), R1.15 (bottom of chamfer) | Stu142 `baseplate_radius`; rebuilt `BASEPLATE_OUTER_DIAMETER = 8` |

### Bin foot profile (from the bottom up, outer edge)

| Segment | Zack (Stu142) | rebuilt `BASE_PROFILE` |
|---|---|---|
| 45° chamfer | 0.8 | 0.8 |
| Vertical | 1.8 | 1.8 |
| 45° chamfer | 2.15 | 2.15 |
| **Profile height** | **4.75** | **4.75** |
| Bridge/platform above the profile up to 1U | 2.25 (4.75 + 2.25 = 7) | `BASE_HEIGHT = 7` |
| Inset from the 41.5 outline at the bottom | 2.95 per side (bottom 35.6 wide) | 0.8 + 2.15 |

### Baseplate profile (from the bottom up, per cell)

| Segment | Zack (Stu142) | rebuilt `_BASEPLATE_PROFILE` | cq-gridfinity |
|---|---|---|---|
| Clearance under the profile | 0 | 0.35 (`BASEPLATE_HEIGHT = 5`) | n/a |
| 45° chamfer | 0.7 | 0.7 | 0.7 |
| Vertical | 1.8 | 1.8 | 1.8 |
| 45° chamfer (to a sharp ridge shared with the next cell) | 2.15 | 2.15 | 2.25 |
| **Thin Baseplate height** | **4.65** | **5.0** | 4.75 |
| Opening at the vertical band / bottom of chamfer | 37.7 / 36.3 | same | — |

### Stacking lip (top of Bin wall, from the inner tip up and out)

| Segment | Value | Source |
|---|---|---|
| 45° | 0.7 | Stu142 `bin_sharp_stacking_lip_profile`; rebuilt `STACKING_LIP_LINE` |
| Vertical | 1.8 | same |
| 45° | 1.9 | same |
| **Lip height / depth** | **4.4 / 2.6** | same |
| Bin total height | `7·h + 4.4` (2U = 18.4, 3U = 25.4, 6U = 46.4); `7·h` with no lip | Stu142 `bin_total_height`; rebuilt header comment |

rebuilt rounds the lip tip with a 0.6 mm fillet, so its lip is actually 3.55 mm tall, but it says this "has no impact on stacking height". Design to 4.4.

### Magnets and screws

| Item | Value | Source |
|---|---|---|
| Magnet | 6 mm dia × 2 mm disc | gridfinity.xyz spec; Stu142 |
| Magnet hole (spec) | Ø6.5 × 2.4 deep | Stu142 `bin_radius`, `baseplate_radius`; rebuilt `MAGNET_HOLE_RADIUS = 6.5/2`, depth 2 + 2 layers |
| Press-fit variants | crush ribs to Ø5.9 (rebuilt); "Refined" Ø5.86 × 1.9 (rebuilt); GridFlock Ø5.9 × 2.25 | rebuilt `standard.scad`; GridFlock `gridflock.scad` |
| Hole pattern | 4 per cell, 26 c-c (±13 from the cell centre, 8 from the cell edge, 4.8 from the Bin's bottom edge) | Stu142; rebuilt `d_hole_from_side = 8`, `HOLE_DISTANCE_FROM_BOTTOM_EDGE = 4.8` |
| Bin screw hole | M3, Ø3 × 6 deep from the Bin bottom (includes the magnet pocket); Ø4.2 for M3 heat-set inserts | Stu142 `bin_radius` and README |
| Baseplate mounting holes (rebuilt) | Ø3 + countersink (+2.5 r) or counterbore Ø5.5 × 3 | rebuilt `BASEPLATE_SCREW_*` |
| Screw-together Baseplate (rebuilt) | horizontal Ø3.35 holes, Ø5 head, 1–3 per cell edge ("Defaults work for M3 and 4-40") | rebuilt `gridfinity-rebuilt-baseplate.scad` |
| Refined thumbscrew (optional, centre of cell) | Ø15, 1.5 pitch | rebuilt `BASE_THUMBSCREW_*`; [Gridfinity Refined](https://www.printables.com/model/413761-gridfinity-refined) |

### Baseplate thickness variants (rebuilt; height = 5.0 + extra)

| Style | Extra below the profile | Total | Bin bottom above the Drawer floor (`z0`) |
|---|---|---|---|
| Thin (open frame) | 0 | 5.0 (Zack: 4.65) | 0 (the Bin rests on the Drawer floor) |
| Weighted | `bp_h_bot = 6.4` | 11.4 | 6.4 |
| Skeletonized, magnets, no screw hole | 1 + 2.4 + 3.35 | 11.75 | 6.75 |
| Screw together (/minimal) | 6.75 | 11.75 | 6.75 |
| gridfinity_build123d `BasePlateBlockFull` | `bottom_height = 6.4` | ≈11.4 | ≈6.4 |

**How a Bin seats.** In rebuilt geometry, the 45° faces of the Bin foot and the Baseplate cell line up exactly when the Bin's bottom is level with the bottom of the Baseplate's open cell. On a thin Baseplate, that is the Drawer floor. With Zack's 4.65 mm plate, the Bin bottoms out on the floor and keeps about 0.25 mm of clearance on the chamfers. In both cases, on a thin Baseplate **the Drawer floor carries the Bin's weight and must be flat**. (This follows from the profile coordinates above; no source states it in words.)

## 3. Drawer interior size for N × M units

```
W_int = 42·N + 2·c      (side to side)
D_int = 42·M + 2·c      (front to back)
```

- The Baseplate is exactly 42·N × 42·M, and Bins never overhang it (they are 0.5 smaller).
- `c` is the per-side clearance between the Baseplate and the Drawer wall. cq-gridfinity's `GridfinityDrawerSpacer` uses `GR_TOL = 0.5` total. rebuilt's "Fit to Drawer" (`distancex/y`, `fitx/y`) pads the Baseplate out to whatever interior size you enter: `padding = distance − 42·floor(distance/42)`.
- **Recommendation for kagu (not from any source):** design to `c ≈ 0.5–1.0` per side. Plywood Drawer boxes vary by a millimetre or more, so measure the built Drawer and let the generator's padding or spacers absorb the difference. Use whole units only; an oversized interior wastes at most 41 mm before it can fit another unit.
- The outside corners of the Baseplate are R4, so they clear square Drawer corners or corner glue blocks up to about 1 mm.

Worked examples: 8×8 → 336 + 2c; 8×10 → 336 × 420 (+2c each); 10×12 → 420 × 504 (+2c each).

## 4. Minimum Drawer interior height for an h-unit Bin

```
H_min = z0 + 7·h + 4.4 + c_top
```

- `z0` comes from the thickness table above: 0 for a thin Baseplate, about 6.4–6.75 for a thick one. For other generators, use `z0 = T_baseplate − 5.0` with rebuilt-style plates and `T_baseplate − 4.65` with Zack-style plates.
- Leave out the 4.4 for lipless Bins.
- `c_top` is clearance above the tallest Bin to whatever is above it (the next Drawer's underside or a carcass rail) while the Drawer slides. **Recommendation:** at least 3 mm, more if the slides sag. A Bin does not need lift-out clearance inside the Bay if the Drawer extends fully, because it lifts out once the Drawer is open.
- **Stacked Bins:** each added Bin adds about 7·h. The lip receives the next foot the same way a Baseplate does, so only the top lip counts: `H ≈ z0 + 7·Σh + 4.4 + c_top`. This is inferred from the lip/foot geometry; check it on a real print before depending on it.
- The "Drawer interior height" here is the clear vertical space the Bins need. The Drawer box sides can be lower than that; that is a choice for the Drawer construction ticket.

| h (U) | Bin height `7h + 4.4` | `H_min`, thin Baseplate (`z0 = 0`, `c_top = 3`) | `H_min`, magnet/screw-together (`z0 = 6.75`, `c_top = 3`) |
|---|---|---|---|
| 2 | 18.4 | 21.4 | 28.15 |
| 3 | 25.4 | 28.4 | 35.15 |
| 4 | 32.4 | 35.4 | 42.15 |
| 6 | 46.4 | 49.4 | 56.15 |
| 8 | 60.4 | 63.4 | 70.15 |
| 10 | 74.4 | 77.4 | 84.15 |
| 12 | 88.4 | 91.4 | 98.15 |

## 5. Generator comparison

| Generator | Kind | License | Bins / Baseplates | Drawer fit and splitting | Code-CAD integration |
|---|---|---|---|---|---|
| [Ruudjhuu/gridfinity_build123d](https://github.com/Ruudjhuu/gridfinity_build123d) ([docs](http://gridfinity-build123d.readthedocs.io/)) | Python, **build123d** | MIT | Both. `Bin`, `BaseEqual`, `BasePlate`/`BasePlateEqual` with Frame/Full/Skeleton blocks, `StackingLip`, `GridfinityRefinedConnector` | Not automatic. Compose plates in code | **Native**: returns build123d `BasePartObject`s, so it can sit directly in kagu's assembly. Installed from git (`pip install git+…`); v0.1.0; 99★; last push 2026-02 |
| [moritzmhmk/gridfinity-build123d](https://github.com/moritzmhmk/gridfinity-build123d) | Python, **build123d** | "Other" (unclear) | Bins of arbitrary grid shape, compartments | — | Native build123d; 15★; check the license before use |
| [PaulBone/gfthings](https://github.com/PaulBone/gfthings) | Python, build123d (per its README) | none stated | Several object types | — | build123d-based, but no license means it can't be reused |
| [michaelgale/cq-gridfinity](https://github.com/michaelgale/cq-gridfinity) | Python, **CadQuery** | MIT | `GridfinityBox`, `GridfinityBaseplate`, `GridfinityDrawerSpacer`, rugged box; CLI scripts | **Drawer spacer** generator (`best_fit_to_dim`) | On PyPI (`cqgridfinity`). Both libraries run on OCCT, so geometry can move via STEP. Using both in one Python process needs matching OCP versions (not tested here). 206★; last push 2025-04 |
| [kmeisthax/gridfinity-cadquery](https://github.com/kmeisthax/gridfinity-cadquery) | Python, CadQuery | unclear | Port of Zack's models | — | 38★; inactive since 2024-01 |
| [kennetek/gridfinity-rebuilt-openscad](https://github.com/kennetek/gridfinity-rebuilt-openscad) | OpenSCAD | MIT | Both. Magnets/screws/refined holes, half grid, lite, vase | **Fit to Drawer** padding; screw-together plates | STL via the `openscad` CLI. Useful as the **reference constants**. build123d's `import_stl` gives a mesh face, not BREP, so it is fine for printing but poor for CAD. 2.3k★; last push 2025-08 |
| [ostat/gridfinity_extended_openscad](https://github.com/ostat/gridfinity_extended_openscad) ([site](https://gridfinity-extended.ostat.com/)) | OpenSCAD | **GPL-3.0** (MIT before 2024-12-26, per gridfinity.tools) | Both, with the widest feature set | Yes | STL only; GPL matters only if kagu redistributes derived models. 941★ |
| [yawkat/GridFlock](https://github.com/yawkat/gridflock) ([web](https://gridflock.yawk.at), [Perplexing Labs host](https://gridfinity.perplexinglabs.com/pr/gridflock/0/0)) | OpenSCAD + web | MIT / CC-BY 4.0 dual | Baseplates only | **Splits the plate to `bed_size`**, with intersection or edge puzzle connectors, padding/filler, magnets, click latches, numbered tiles | STL. Uses rebuilt's cutter. **The best fit for printing kagu's multi-tile Baseplates.** 127★; active (2026-11) |
| [Perplexing Labs Gridfinity Generator](https://gridfinity.perplexinglabs.com) | Web | proprietary | Both | Yes | STL download only |
| [GridfinityCreator](https://gridfinity.bouwens.co/) | Web | CC BY-NC-SA 4.0 | Both | — | **STEP** export, which build123d's `import_step` can read |
| [Stu142/FreeCAD-Gridfinity-Workbench](https://github.com/Stu142/FreeCAD-Gridfinity-Workbench) | FreeCAD add-on | LGPL-2.1 | Both | — | FreeCAD (STEP out); 542★ |
| [Le0Michine/FusionGridfinityGenerator](https://github.com/Le0Michine/FusionGridfinityGenerator) | Fusion 360 add-in | unclear | Both | — | Fusion; 1.2k★ |
| Other web tools listed on gridfinity.xyz: [gridfinitygenerator.com](https://gridfinitygenerator.com), [Extrabold.tools](https://extrabold.tools), [Gridfinity Layout Tool](https://gridfinitylayouttool.com), [GridfinityStudio](https://gridfinitystudio.com) | Web | various | — | — | Not evaluated |

**What this means for code-CAD.** kagu models the Drawer and Baseplate, not the Bins (Bins are out of scope on the map). The Baseplate is one profile (0.7 / 1.8 / 2.15 at 45° / vertical / 45°) swept around a rounded square and repeated on a 42 mm grid. That is small enough to write as a kagu module using the constants in §2. `gridfinity_build123d` is the native option if a library is preferred. The files that actually get printed should come from GridFlock (split to the Prusa XL bed) or rebuilt, since those are what the community tests against.

## 6. Shadow Bin photo-to-outline tools

Every tool below follows the same workflow: put the tool on a sheet of paper, take a photo from above, use the paper corners to set the scale, trace the outline with segmentation, offset it by a clearance, then cut it into a Gridfinity Bin.

| Tool | Hosting / license | Scale reference | Outputs | Gridfinity features | Cost | Notes |
|---|---|---|---|---|---|---|
| [Tracefinity](https://github.com/tracefinity/tracefinity) | **Self-hosted Docker, MIT** (739★, active) | A4 / Letter / A3 / Tabloid paper; tools may overhang the sheet; U2-Net finds the paper corners | **STL, 3MF, SVG outlines** | Base profile, magnet holes, stacking lip, cutout clearance; tool library, multi-tool layout per project | Free | Traces locally with IS-Net (no API key). Gemini, fal or Replicate are optional and send the photo off-site. Needs a CPU with AVX. **Fits a lab well:** shared tool library, data stays in the lab |
| [neilyboy/tracefinity](https://github.com/neilyboy/tracefinity) | Self-hosted, no license stated | — | SVG/DXF/STL/3MF/STEP (per its description) | — | — | Small fork-like project, 1★; prefer the upstream above |
| [Tooltrace](https://tooltrace.ai/) | Hosted (finalREV), closed | Letter/A4 paper (per testimonials) | **DXF, SVG, STL** | "Gridfinity mode" plus Kaizen/shadow-box foam | Free: 3 active traces. Pro $8/mo: unlimited | DXF/SVG are also usable for laser-cut or foam Shadow Bins |
| [TraceMate](https://tracematehq.com/) | Hosted, closed | A4/A5/Letter paper | STL | 1×1 to 10×10, 7 mm units, lip, R3.75, optional magnets; clearance 0–5 mm in 0.1 steps | Editor free; 3 free cutout downloads, then €4.99 for 10 or €19 for 50 | |
| [Outline](https://github.com/georgslazdans/outline-app) ([app](https://outline.georgs.lv), listed on [gridfinity.tools](https://gridfinity.tools/)) | Web, **AGPL-3.0** (312★) | not stated | Bins with custom cutouts | Simple Bins too | Free | The author says long-term hosting is uncertain |
| DIY: photo → Inkscape trace → SVG → build123d `import_svg` | Free | Ruler or paper in the photo | Whatever kagu's code makes | Whatever the kagu code models | Free | Most control and fits the code-CAD flow, but needs manual cleanup |

Not evaluated: GridPilot and TraceToForge (they appear in [a vendor comparison](https://tracetoforge.com/blog/tracetoforge-vs-tooltrace-vs-gridpilot/)).

## 7. Prusa XL: largest one-piece Baseplate and multi-piece joining

**The printable area is 360 × 360 × 360 mm.**
- [Prusa's product page](https://www.prusa3d.com/product/original-prusa-xl-semi-assembled-single-toolhead-3d-printer/) gives "360 × 360 × 360 mm (46.7 liters)" and does not say multiple toolheads reduce it.
- PrusaSlicer's official profile ([PrusaSlicer-settings-prusa-fff `PrusaResearch/2.5.14.ini`](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.14.ini), `[printer:*commonXL*]`) sets `bed_shape = 0x0,360x0,360x360,0x360` and `max_print_height = 360`. All XL variants inherit those values.

**The largest one-piece Baseplate is 8 × 8 units = 336 × 336 mm** (`floor(360/42) = 8`).
- That leaves 24 mm on each axis for a skirt or brim.
- An 8 × N tile (N ≤ 8) also fits.
- "Fit to Drawer" padding can grow a tile to almost 360 mm, but that leaves nothing for a skirt or brim.
- Nine units in a line (378 mm) only fit diagonally, so there is no practical benefit.

**Ways to join multi-piece Baseplates:**

| Method | How it works | Source |
|---|---|---|
| Butted tiles held by the Drawer | Separate tiles sit edge to edge, and the Drawer walls (plus padding or spacers) stop them moving. This is what rebuilt "Fit to Drawer" and cq-gridfinity `GridfinityDrawerSpacer` assume | rebuilt, cq-gridfinity |
| Puzzle connectors (auto-split) | GridFlock cuts the full Drawer-size plate into bed-size tiles. Its *intersection puzzle* puts small connectors at cell intersections (fixed SVG shape); its *edge puzzle* has adjustable height and count. A full-height connector "can lead to unconnected pieces if there is no magnet layer". Tiles can be numbered | [GridFlock README](https://github.com/yawkat/gridflock) |
| Screw together | rebuilt `style_plate = 3/4` adds 6.75 mm of thickness with horizontal Ø3.35 holes through the tile edges for M3 or 4-40 screws | rebuilt |
| Refined connector clips | A separate printed clip (about 2.8 mm thick, chamfered) drops into matching sockets on neighbouring tiles. gridfinity_build123d implements it | [gridfinity_build123d `connectors.py`](https://github.com/Ruudjhuu/gridfinity_build123d/blob/main/src/gridfinity_build123d/connectors.py); [Gridfinity Refined](https://www.printables.com/model/413761-gridfinity-refined) |
| Screw tiles to the Drawer floor | rebuilt countersink/counterbore holes (M3) in thick plates; each tile is fixed on its own | rebuilt |

## 8. Implications for kagu

1. **Size Drawers from grid units first.** Choose N × M per Drawer, then `W_int = 42N + 2c` and `D_int = 42M + 2c` with c ≈ 0.5–1. The Drawer outside dimensions, slide clearance, Bay width and Carcass follow from that. The cabinet geometry tickets should take N and M as their parametric inputs.
2. **Width of 8 units or less makes printing easy.** An 8-unit-wide Drawer (336 mm + 2c inside) takes one Prusa XL tile across. Depth then splits into ≤ 8-unit tiles, for example 8 × 12 = 8×8 + 8×4. Split evenly where possible (12 = 6 + 6) so the tiles are interchangeable.
3. **Bay vertical pitch comes from `z0 + 7h + 4.4 + c_top`** plus the Drawer floor thickness and slide/runner clearance. Fixing a small set of Drawer heights in units (for example 3U, 6U, 9U) gives a standard set of Bay pitches.
4. **A thin Baseplate puts all Bin load on the Drawer floor.** The floor must be flat and stiff, for example plywood with no sag across 336+ mm. A thick magnet Baseplate costs about 6.75 mm of height per Drawer and four magnets per cell.
5. **The cabinet rolls, so fix the Baseplates.** Screw or glue the tiles to the Drawer floor, or use GridFlock's puzzle tiles plus Drawer-wall padding, so they don't shift when the Drawer is slammed or the cabinet crosses a threshold. Magnets in Bins and Baseplate also stop Bins rattling out of position; that is a decision to make.
6. **Code-CAD split.** kagu's build123d model should carry the Baseplate as a simple parametric module from §2 (or `gridfinity_build123d`), to visualise Drawers and check clearances. The printed files come from GridFlock or rebuilt with `bed_size = 360×360`. Bins stay with the community generators.
7. **Choose a reference implementation.** Use **gridfinity-rebuilt's constants** (5.0 mm thin plate, 4.75 mm foot, 4.4 mm lip). It is the reference GridFlock builds on, and its values are within 0.35 mm of Zack's.
8. **Shadow Bin workflow.** A self-hosted **Tracefinity** gives the lab a shared tool library, keeps photos on site and exports SVG outlines. **Tooltrace** has the least setup cost and gives DXF/SVG if Shadow Bins ever move to foam or laser-cut inserts.

## 9. Open questions surfaced

- **Glossary tension:** a Drawer "holds one Baseplate", but on the Prusa XL any Drawer bigger than 8 × 8 has a Baseplate made of several printed pieces. Does the glossary need a term for a printed piece (for example *Baseplate Tile*), or does Baseplate mean the assembled grid?
- **Magnets or not?** They help Bins stay put in a rolling Cabinet, but cost height (thin vs. about 11.75 mm plates) and hardware.
- **How are Baseplates fixed in the Drawer** (screws, glue, puzzle + padding)? This depends on Drawer floor construction, which is not yet specified.
- **Standard Drawer heights in U.** The answer sets Bay pitch, so it feeds the Bay/Carcass layout tickets.
- **Stacked-Bin height** (`7·Σh + 4.4`) is inferred, not stated by any source. Check it on a real print if Bins will be stacked in Drawers.

## Sources

- Zack Freedman, "Gridfinity: Your Ultimate Modular Workshop is FREE!" — https://www.youtube.com/watch?v=ra_9zU-mnl8
- gridfinity.xyz home (MIT license note, generator and library links) — https://gridfinity.xyz/ ; source — https://github.com/gridfinity-unofficial/gridfinity-unofficial.github.io
- gridfinity.xyz specification (draft) — https://gridfinity.xyz/specification/ ; https://github.com/gridfinity-unofficial/specification
- Stu142, Gridfinity-Documentation (dimensioned drawings of Zack's original models) — https://github.com/Stu142/Gridfinity-Documentation (files `drawing_svg/baseplate_profile.svg`, `baseplate_total_width.svg`, `baseplate_radius.svg`, `bin_bottom_profile.svg`, `bin_profile_width.svg`, `bin_radius.svg`, `bin_total_width.svg`, `bin_total_height.svg`, `bin_sharp_stacking_lip_profile.svg`)
- gridfinity-rebuilt-openscad — https://github.com/kennetek/gridfinity-rebuilt-openscad (`src/core/standard.scad`, `src/core/gridfinity-baseplate.scad`, `gridfinity-rebuilt-baseplate.scad`, `gridfinity-rebuilt-bins.scad`, `src/core/gridfinity-rebuilt-utility.scad`, `docs/baseplates.md`)
- cq-gridfinity — https://github.com/michaelgale/cq-gridfinity (`cqgridfinity/constants.py`, `cqgridfinity/gf_drawer.py`)
- gridfinity_build123d — https://github.com/Ruudjhuu/gridfinity_build123d (`src/gridfinity_build123d/constants.py`, `baseplate.py`, `bin.py`, `connectors.py`)
- moritzmhmk/gridfinity-build123d — https://github.com/moritzmhmk/gridfinity-build123d
- PaulBone/gfthings — https://github.com/PaulBone/gfthings
- kmeisthax/gridfinity-cadquery — https://github.com/kmeisthax/gridfinity-cadquery
- gridfinity_extended_openscad — https://github.com/ostat/gridfinity_extended_openscad
- GridFlock — https://github.com/yawkat/gridflock (README, `gridflock.scad`, `LICENSE`); generator https://gridflock.yawk.at
- Perplexing Labs generator — https://gridfinity.perplexinglabs.com
- GridfinityCreator — https://gridfinity.bouwens.co/
- FreeCAD Gridfinity Workbench — https://github.com/Stu142/FreeCAD-Gridfinity-Workbench
- Fusion Gridfinity Generator — https://github.com/Le0Michine/FusionGridfinityGenerator
- Gridfinity Refined (grizzie17) — https://www.printables.com/model/413761-gridfinity-refined (not fetched, HTTP 403; referenced through rebuilt and gridfinity_build123d)
- gridfinity.tools (tool index, licenses) — https://gridfinity.tools/
- Tracefinity — https://github.com/tracefinity/tracefinity
- neilyboy/tracefinity — https://github.com/neilyboy/tracefinity
- Tooltrace — https://tooltrace.ai/
- TraceMate — https://tracematehq.com/
- Outline — https://github.com/georgslazdans/outline-app ; https://outline.georgs.lv
- build123d importers (`import_svg`, `import_step`, `import_stl`) — https://github.com/gumyr/build123d/blob/dev/src/build123d/importers.py
- Prusa XL product page (build volume) — https://www.prusa3d.com/product/original-prusa-xl-semi-assembled-single-toolhead-3d-printer/
- PrusaSlicer official XL printer profile (`bed_shape`, `max_print_height`) — https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.14.ini
