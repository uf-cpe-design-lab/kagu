# Rigol bench instrument dimensions, weights and clearances

Research for [#3](https://github.com/uf-cpe-design-lab/kagu/issues/3), part of the wayfinder map [#1](https://github.com/uf-cpe-design-lab/kagu/issues/1).

**Question:** What are the external dimensions, weights, rear and ventilation clearances, and handle and carry features of one set of the lab's Rigol bench instruments (MSO2302A, DM3068, DG1032Z, DP832A)? What does one set add up to, and must any of them not be stored on its back or side?

**Sources:** Rigol's own datasheets and user guides, downloaded from rigol.com (listed under [Sources](#sources)). Each figure below cites the document and page it came from. Where Rigol publishes nothing, the text says so. Anything that is my inference or a design assumption, not a Rigol figure, is labelled **(assumption)**.

## Answer in brief

- One set weighs **20.8 kg** nominal without packaging (3.9 + 3.2 + 3.2 + 10.5 kg). Allowing for the scope's published ±0.5 kg tolerance, it is up to **21.3 kg**. Half of that is the DP832A.
- The overall envelopes (W × H × D) are **361.6 × 179.6 × 130.8 mm** (MSO2302A), **231.6 × 107.0 × 290.5 mm** (DM3068), **261.5 × 112 × 318.4 mm** (DG1032Z, width includes its handle) and **239 × 157 × 429.5 mm** (DP832A, depth includes the front knobs and terminals).
- The scope is wide and shallow. The other three are narrow and deep. The deepest unit, the DP832A at 429.5 mm, sets the Bay depth. The scope sets the height of any row it sits in (179.6 mm).
- Rigol publishes a numeric ventilation clearance for **only one instrument**: the MSO2000A needs **at least 10 cm beside, above and behind** while it runs. The other three manuals only say to keep the instrument well ventilated.
- Rigol publishes **no rear-cable clearance** and **no storage-orientation rule** (no "do not store on its back or side") for any of the four.

## Model identification

| Lab name | Rigol series | Model in Rigol docs | Note |
|---|---|---|---|
| MSO2302A | MSO/DS2000A | MSO2302A | 300 MHz, 2 analog + 16 digital channels. The datasheet also lists an MSO2302A-S variant (built-in source) with the same body. |
| DM3068 | DM3000 | DM3068 | 6½-digit DMM. |
| DG1032 | DG1000Z | **DG1032Z** | Rigol's DG1000Z model is named DG1032Z. There is also an older, separate DG1000 (non-Z) series. This note assumes the lab's units are DG1032Z. Check the badge on a unit. |
| DP832A | DP800 | DP832A | The DP800 user guide's figures are drawn from the DP832. The datasheet gives the DP832 and DP832A the same dimensions and weight. |

## Per-instrument data

All dimensions are in mm, as W × H × D unless stated. "Overall" means the outermost extent shown in Rigol's dimension drawing.

### MSO2302A (MSO/DS2000A series oscilloscope)

| Item | Value | Source |
|---|---|---|
| Overall size | **361.6 W × 179.6 H × 130.8 D** | Datasheet DSA18105-1110, Physical Characteristics; User Guide fig. 1-1/1-2 (p. 1-3) |
| What the size includes | "Supporting legs and handle folded, knob height included" (datasheet note [4]). The height includes the bottom feet. The depth includes the front knobs. | Datasheet note [4]; User Guide fig. 1-1/1-2 |
| Size with handle raised or legs deployed | **Not published.** | n/a |
| Weight | **3.9 kg ± 0.5 kg** without packaging; 4.5 kg ± 0.5 kg with packaging | Datasheet, Weight (note [5]: standard configuration) |
| Handle | A single carry handle on top that hinges at the rear. "Pull up the handle vertically for easy carrying… When you do not need the handle, press it down." Folded, it lies within the published envelope. | User Guide p. 1-11, item 1 |
| Feet | Folding "supporting legs" under the front that tilt the scope up for viewing. | User Guide p. 1-4, fig. 1-3 |
| Cooling | Fan cooling. Side vent grilles are shown in fig. 1-3. | Datasheet, Cooling Method; User Guide p. 1-4 |
| Ventilation clearance | "When using the oscilloscope in a bench-top or rack setting, provide **at least 10 cm clearance beside, above and behind** the instrument for adequate ventilation." | User Guide p. XI, "Ventilation Requirement"; same text in the Quick Guide |
| Rear-panel items | Handle, LAN, USB Device, fuse, AC power inlet, security lock slot, Trigger Out BNC, Source 1/2 BNCs (‑S variant). | User Guide p. 1-11, fig. 1-11 |
| Rear-cable clearance | **Not published.** | n/a |
| Storage orientation | **Not published.** "Handle with care during transportation to avoid damage to keys, knobs, interfaces, and other parts on the panels." Storage temperature is −40 °C to +70 °C (non-operating). | User Guide p. IV, "Handle with Caution"; Datasheet, Temperature Range |

### DM3068 (DM3000 series 6½-digit multimeter)

| Item | Value | Source |
|---|---|---|
| Overall size | **231.6 W × 107.0 H × 290.5 D** (Rigol writes it H × W × L: 107.0 × 231.6 × 290.5) | Datasheet DSC06100-2024; User Guide p. 1-4 fig. 1-3/1-4 and p. 6-20 |
| What the size includes | Width and height span the corner bumpers. The depth spans from the front-panel terminals to the rear bumpers. The drawing shows the handle hubs standing slightly outside the 231.6 mm width line. | User Guide fig. 1-3/1-4 (read from the drawing) |
| Size with handle | **Not published.** The swing handle extends below the case in the viewing positions and above it in the carrying position. Rigol gives neither extent. | User Guide p. 1-3, fig. 1-2 |
| Weight | **About 3.2 kg** without packaging. Packaged weight is not published. | Datasheet; User Guide p. 6-20, General Specifications |
| Handle | A side-pivoting swing handle. "Grip the handle by both sides and pull outward, then rotate the handle to a desired position." Three viewing positions and one carrying position are shown. | User Guide p. 1-3 |
| Cooling | **Not stated** in the specifications. No fan appears among the 11 rear-panel items. A side vent grille appears in fig. 1-4. The manual's generic safety page still says "inspect the air outlet and the fan regularly". | User Guide p. 1-9, fig. 1-6; p. III |
| Ventilation clearance | **No figure published.** The manual only says "keep the instrument well ventilated". | User Guide p. III |
| Rear-panel items | Current-input fuse, LAN, GPIB, AC power inlet, VM Comp BNC, Ext Trig BNC, USB Device, RS-232, power fuse, voltage selector, power switch. | User Guide p. 1-9, fig. 1-6 |
| Rear-cable clearance | **Not published.** | n/a |
| Rack option | RM-DM3000 kit: 19-inch rack, **3U**, panel 482.6 × 133.35 mm, tray depth 399 mm. The handle must be removed. | User Guide p. 1-19 to 1-24 |
| Storage orientation | **Not published.** Storage temperature is −40 °C to 70 °C. | User Guide p. 6-20, General Specifications |

### DG1032Z (DG1000Z series function/arbitrary waveform generator)

| Item | Value | Source |
|---|---|---|
| Overall size | **261.5 W × 112 H × 318.4 D** | Datasheet DSB09103-1110, Mechanical; User Guide p. 1-4 |
| What the size includes | The 261.5 mm width **includes the handle pivots**. The case is **236 mm** wide without the handle. The 112 mm height spans the corner bumpers. The 318.4 mm depth spans from the front connectors to the rear bumpers. | User Guide p. 1-4, front and side views (236 and 261.5 are both dimensioned) |
| Size with handle swung down | **195 mm** tall overall, with the handle rotated below the case as a stand. | User Guide p. 1-4, front view |
| Size with handle in carry position | **Not published.** | n/a |
| Weight | **3.2 kg** without packaging; **4.5 kg** with packaging | Datasheet, Mechanical |
| Handle | A side-pivoting swing handle: "hold the handle by sides of the instrument and pull it outward, and then rotate the handle to the desired position." Three viewing positions and one move position are shown. | User Guide p. 1-3 |
| Cooling | Fan cooling ("Cooling by fans compulsively"). The side view shows side vents. | Datasheet; User Guide p. 5-7 |
| Ventilation clearance | **No figure published.** "Keep the instrument well ventilated". | User Guide p. III |
| Rear-panel items | CH1 and CH2 Sync/Ext Mod/Trig/FSK BNCs, 10 MHz In/Out BNC, LAN, USB Device, AC power inlet. | User Guide p. 1-11, fig. 1-2 |
| Rear-cable clearance | **Not published.** The rear BNCs are used for sync and triggering, so cables may be fitted there. | n/a |
| Rack option | RM-1-DG1000Z (one unit) and RM-2-DG1000Z (two side by side). Needs a 19-inch rack, **≥ 2U (88 mm)** of height and **≥ 400 mm** of depth. | DG1000Z Rack Mount Kit installation guide, "Space Requirements" |
| Storage orientation | **Not published.** Non-operating temperature is −40 °C to 70 °C. | Datasheet |

> Caution when reading the DG1000Z user guide: on p. 2-110 it says "make sure the vents at both sides and the fan aperture at the rear panel are visible". That sentence is about the **PA1011 power amplifier accessory**, not the DG1000Z itself.

### DP832A (DP800 series triple-output linear DC power supply)

| Item | Value | Source |
|---|---|---|
| Body size (datasheet) | **239 W × 157 H × 418 D** | DP800 Datasheet DSH03108-1110, Mechanical (the same for A and non-A models) |
| Overall depth | **429.5 mm**, including the front-panel knob and output terminals. The 418 mm figure runs from the front bumpers to the rear bumpers. | DP800 User's Guide p. 1-3, fig. 1-2 (both 418 and 429.5 dimensioned) |
| What W and H include | The corner bumpers. | User's Guide fig. 1-1 |
| Weight | **10.5 kg** (DP832A). Packaged weight is not published. | DP800 Datasheet, Mechanical |
| Handle | **None described** in the user's guide. The side view (fig. 1-2) shows a bar fixed along each side, but the guide does not label it. | User's Guide p. 1-3 |
| Feet | Corner bumpers only. No tilt legs are described. | User's Guide fig. 1-1/1-2 |
| Cooling | Fan cooling with intelligent fan-speed control. A **large fan grille fills most of the rear panel**. If the fan stops, the outputs are disabled. | Datasheet; User's Guide p. 1-11, fig. 1-4 (item 9); p. 2-4 |
| Ventilation clearance | **No figure published.** "Keep the instrument well ventilated and inspect the air outlet and the fan regularly". | User's Guide p. III |
| Rear-panel items | LAN (option), USB Device, USB Host, Digital I/O (option), RS-232 (option), voltage selector, AC power inlet, fuse, fan. The DP832/DP832A has no rear output terminals; only the DP811 has them. | User's Guide p. 1-11 to 1-12, Table 1-1 |
| Rear-cable clearance | **Not published.** | n/a |
| Rack option | RM-1-DP800 (one unit) and RM-2-DP800 (two units). Rack dimensions are not given in the user's guide. | User's Guide p. 6-1 (accessories) |
| Storage orientation | **Not published.** Storage temperature is −40 °C to 70 °C. | DP800 Datasheet |

## Totals for one set

### Weight

| Instrument | Weight without packaging (kg) |
|---|---|
| MSO2302A | 3.9 (± 0.5) |
| DM3068 | ~3.2 |
| DG1032Z | 3.2 |
| DP832A | 10.5 |
| **Set** | **20.8 nominal, 21.3 at the scope's upper tolerance** |

Probes, test leads and power cords are extra. Rigol publishes no weight for them.

### Envelope options

These use the overall published extents: MSO 361.6 × 179.6 × 130.8, DM 231.6 × 107.0 × 290.5, DG 261.5 × 112 × 318.4 (with handle), DP 239 × 157 × 429.5. The figures are instrument extents only. Clearances and shelf thickness are not included.

| Layout | W × H × D (mm) | Notes |
|---|---|---|
| **A. One row, side by side** | **1093.7 × 179.6 × 429.5** | The simplest layout, with nothing on top of anything. The width is 1068.2 if the DG's handle is removed. It needs a Bay over 1.1 m wide. |
| **B. Two rows on an intermediate shelf** (lower: DP832A + MSO; upper: DG1032Z + DM3068) | **600.6 × 291.6 × 429.5**, plus the shelf thickness | Lower row 600.6 × 179.6 × 429.5. Upper row 493.1 × 112 × 318.4. The heaviest unit sits low. |
| **C. Column + scope** (DP832A at the bottom with DG1032Z and DM3068 stacked on it, MSO beside) | **623.1 × 376 × 429.5** | Column 261.5 × 376 × 429.5. The DG (236 mm case) and DM (231.6 mm) both sit within the DP's 239 mm top, but the DG's handle hubs overhang by about 11 mm each side. **Rigol publishes nothing about stacking.** Treat this layout as storage-only. |
| D. Everything in one column | 361.6 × 555.6 × 429.5 | Shown for completeness. The scope is only 130.8 mm deep, so nothing can sit on it, and it would have to go at the bottom with the 10.5 kg DP832A on top. Not recommended. |

## Implications for kagu

1. **The Bay depth is set by the DP832A.** It needs at least **430 mm clear inside depth** with the instrument against the back and no cords fitted. If instruments stay cabled while stored, or are run in the Bay, add a rear allowance. **(Assumption: 100 mm, the same as the MSO's published ventilation figure. A straight IEC power plug plus a gentle bend fits in that.)** That gives about **530 mm**. This is a large share of a typical Carcass depth and should feed the Carcass footprint decision.
2. **Decide whether instruments are only stored in the Bay, or also run there.** If they only sit there powered off, ventilation does not apply, and layouts B or C are compact. If any instrument runs in the Bay, the MSO needs 100 mm on each side, above and behind (Rigol's figure). **(Assumption: give the three fan-cooled or vented units the same 100 mm, since Rigol publishes no number for them.)** In that case stacking (layout C) is out.
3. **Minimum Bay openings, excluding clearances.** Add about 10–20 mm a side for hand and lifting room **(assumption)**.
   - Layout A: inside width ≥ 1094 mm, height ≥ 180 mm, depth ≥ 430 mm. This is probably wider than a single Cabinet can be.
   - Layout B: inside width ≥ 601 mm, height ≥ 292 mm plus the intermediate shelf thickness (≈ 19 mm for 3/4" ply, so ≈ 311 mm), depth ≥ 430 mm.
   - Layout C: inside width ≥ 624 mm, height ≥ 376 mm, depth ≥ 430 mm.
4. **Shelf load.** The static load for one set is **≈ 21 kg**, or ≈ 25 kg once probes, leads and cords are added **(assumption: about 4 kg for accessories, which Rigol does not publish)**. The Cabinet rolls, so design each instrument shelf and its supports for at least **2× static, about 50 kg** **(assumption: a dynamic or shock factor for rolling over thresholds; confirm in the Carcass and caster ticket)**. In layout B the lower shelf carries 14.4 kg of instruments, about 70 % of the set. The DP832A alone puts about 10.5 kg on four corner bumpers.
5. **Put the DP832A at the bottom.** It is half the set's mass, so the lowest Bay position keeps the mobile Cabinet's centre of gravity low. It is also a 10.5 kg lift from near the floor, so leave room above it for hands.
6. **Restrain instruments during rolling (assumption).** None of the instruments has non-slip feet or tie-down points described in Rigol's docs. A front lip, a strap or a retaining bar on the shelf would stop them sliding out when the Cabinet moves.
7. **Handles take extra room.** The DG1032Z's handle adds 25.5 mm of width (261.5 vs 236). Swung down, it makes the unit 195 mm tall. The DM3068's handle extents are not published. Measure both units with their handles in the intended storage position before fixing the Bay height and width.
8. **Storage orientation.** Rigol gives **no rule against storing any of these on its back or side**, and no rule permitting it. **(Assumption, recommended):** store all four flat on their feet, in their normal operating orientation. Every unit has its power inlet and connectors on the rear panel. The DP832A's rear is mostly fan grille, so resting it on its back puts 10.5 kg on the rear bumpers next to the grille. The DG1000Z and DM3068 manuals show a vertical "carrying/move position", but that is how you hold the unit by its handle, not how to store it.
9. **The instrument-cabinet variant could use Rigol rack kits.** The DM3068 takes 3U and 399 mm of depth. The DG1000Z needs at least 2U and 400 mm. The DP800 has single and dual kits, with dimensions not published in the guide. The MSO2000A guide lists no rack kit. That could matter if the parametric instrument variant ever moves to 19-inch rails.

## Gaps (not published by Rigol)

- Dimensions with handles raised or swung (MSO handle up, DM3068 handle in any position, DG1032Z handle in carry position).
- Any ventilation clearance figure for the DM3068, DG1032Z or DP832A.
- Rear cable or connector clearance for any of the four.
- Any storage-orientation rule, or stacking permission, for any of the four.
- Packaged weights for the DM3068 and DP832A.
- Fan or airflow direction for any unit.

## Sources

All files were downloaded from rigol.com on 2026-11-08. The page numbers are the manuals' printed page labels.

Product pages (which link to the documents below):
- MSO/DS2000A: https://www.rigol.com/intl/products/oscilloscope/MSO-DS2000A.html
- DM3068: https://www.rigol.com/intl/products/multimeter/DM3068.html
- DG1000Z: https://www.rigol.com/intl/products/function-arbitrary-waveform-generator/DG1000Z.html
- DP800: https://www.rigol.com/intl/products/dc-power-supply/DP800.html

Documents:
- MSO/DS2000A Datasheet (DSA18105-1110, 2025-08): https://www.rigol.com/dam/global/downloads/brochures/en/data-sheet/oscilloscopes/MSODS2000A_Datasheet_EN.pdf
- MSO2000A/DS2000A User Guide (UGA18110-1110, May 2019): https://www.rigol.com/dam/global/downloads/brochures/en/user-manual/oscillosopes/MSODS2000A_UserGuide_EN.pdf
- MSO/DS2000A Quick Guide: https://www.rigol.com/dam/global/downloads/brochures/en/quick-guide/oscilloscopes/MSODS2000A_QuickGuide_EN-CN.pdf
- DM3068 Datasheet (DSC06100-2024): https://www.rigol.com/dam/global/downloads/brochures/en/data-sheet/multimeters/DM3068_DataSheet_EN.pdf
- DM3068 User Guide (UGC06110-1110, Jan 2024): https://www.rigol.com/dam/global/downloads/brochures/en/user-manual/multimeters/DM3068_UserGuide_EN.pdf
- DM3068 Quick Guide: https://www.rigol.com/dam/global/downloads/brochures/en/quick-guide/multimeters/DM3068_QuickGuide_EN.pdf
- DG1000Z Datasheet (DSB09103-1110): https://www.rigol.com/dam/global/downloads/brochures/en/data-sheet/waveform-generators/DG1000Z_DataSheet_EN.pdf
- DG1000Z User's Guide (UGB09109-1110, Oct 2016): https://www.rigol.com/dam/global/downloads/brochures/en/user-manual/waveform-generators/DG1000Z_UserGuide_EN.pdf
- DG1000Z Rack Mount Kit installation guide: https://www.rigol.com/dam/global/downloads/brochures/en/user-manual/waveform-generators/DG1000Z-RackmountKit-EN.pdf
- DP800 Datasheet (DSH03108-1110): https://www.rigol.com/dam/global/downloads/brochures/en/data-sheet/dc-powers/DP800_DataSheet_EN.pdf
- DP800 User's Guide (UGH04109-1110, Jun 2016): https://www.rigol.com/dam/global/downloads/brochures/en/user-manual/dc-powers/DP800_UserGuide_EN.pdf
