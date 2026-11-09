# Locking casters and mounting them to plywood

Research for [#7](https://github.com/uf-cpe-design-lab/kagu/issues/7) (map [#1](https://github.com/uf-cpe-design-lab/kagu/issues/1)). Researched November 2026. Prices are list prices seen then and will drift.

## Recommendation

- **Caster:** four **Colson 2 Series 4" × 1-1/4" swivel plate casters with Performa rubber wheels and a Total Lock brake** (part **2.04256.445 BRK5**). Each is rated 300 lb. The mount height is **5-1/8" (130.2 mm)**, the plate is 2-1/2" × 3-5/8", the bolts are 5/16", and Zoro lists them at about $51 each, so about $200 per Cabinet.
- **Why this caster:**
  - Colson recommends polyurethane or Performa rubber wheels on tile.
  - The soft (65A) Performa tread spreads a parked Cabinet's weight over the vinyl composition tile (VCT) better than hard polyurethane does.
  - Total lock stops both the wheel and the swivel, so the work surface does not shift when someone leans on it or uses a mallet.
  - At 300 lb, each caster is rated about 2.7× the worst-case per-caster load.
- **Arrangement:** four swivel casters, all four with total lock. Colson calls this "a most versatile arrangement", suited to the short, sideways moves of a lab Cabinet into a bench position. Locking all four gives the stiffest parked work surface. The fallback is two total-lock swivels plus two rigid casters (Colson 2.04208.445), which tracks straighter but only locks at one end.
- **Mounting:**
  - Put each caster under a vertical Carcass panel (side or partition) at a corner, on a **glued-on 3/4" plywood or hardwood caster pad**. The pad doubles the base to about 1-1/2" where the bolts go.
  - Fasten each caster with **four 5/16-18 bolts into T-nuts**, with the T-nut flange on the *upper* face so that bolt tension pulls the flange into the wood. Through-bolts with fender washers and nylon-insert lock nuts also work.
  - Avoid lag screws into a single 3/4" sheet: there is not enough thread embedment, and they loosen and strip when a caster is replaced.
- **Height:** casters add **130.2 mm** to the Cabinet. For a 915 mm work surface, the Carcass plus the Top Module (plus any pad that sits *below* the Carcass bottom) must total **about 785 mm**. Make `caster_mount_height` a parameter.

## Comparison

All casters below are plate-mount swivels with a brake. "Total lock" stops both wheel and swivel. "Wheel lock" (top lock or tread lock) stops only the wheel, so the swivel still pivots ([ICWM guide](https://og.mhi.org/downloads/industrygroups/icwm/ICWM-Caster-and-Wheel-Guide-101.pdf)).

| Option | Dia × tread | Mount (plate, bolt) | Lock | Wheel material vs VCT | Rating / caster | Overall (mount) height | Price each |
|---|---|---|---|---|---|---|---|
| **Colson 2.04256.445 BRK5** (recommended) | 4" × 1-1/4" | 2-1/2" × 3-5/8", bolts 1-3/4" × 2-13/16"–3-1/16" slotted, 5/16" | Total lock | Performa rubber, 65A, non-marking. Soft, so it is the best fit for long parking on VCT; rolls a little harder than PU | 300 lb | 5-1/8" (130.2 mm) | ~$51 (Zoro) |
| Colson 2.04256.95 BRK5 | 4" × 1-1/4" | same plate | Total lock | HI-TECH polyurethane, 45D. Non-marking, rolls easier, but much harder, which puts more pressure on the tile when parked | 275 lb | 5-1/8" (130.2 mm) | not found; similar class |
| Colson 2.03256.445 BRK5 | 3-1/2" × 1-1/4" | same plate | Total lock | Performa rubber | 250 lb | 4-11/16" (119.1 mm) | ~$40–50 class (not confirmed) |
| Colson 2.05256.445 BRK5 | 5" × 1-1/4" | same plate | Total lock | Performa rubber | 325 lb | 6-3/16" (157.2 mm) | ~$91 (PartsSource) |
| Albion 16XI04202ST | 4" × 2" | 4" × 4-1/2" heavy-duty plate | Total lock | Solid "X-treme" polyurethane, hard. Made in USA | 1,000 lb | 5-5/8" (142.9 mm) | ~$84 (CasterHQ) |
| Rockler #84718 | 4" × 1-1/4" | plate (pattern not published) | Total lock | Polyurethane | 300 lb | not published (measure) | ~$14 (Rockler) |
| Shepherd Hardware PRE40120ZN-TPUB (big-box type) | 4" × 15/16" | plate | Tread (wheel-only) lock | TPU | 150 lb | ~4-3/4" class | low; not recommended |

Notes:

- **Swivel radius:** Colson lists 4-3/4" (120.7 mm) for the 4" total-lock model. The catalog gives 3-7/32" for the same caster without a brake, so the brake pedal enlarges the swivel circle. Keep that circle clear of anything that hangs below the Carcass.
- **Supply chain:** Colson, Shepherd (the caster company), Jarvis and Albion are all brands of the Colson Group. Jarvis targets food service and Albion heavy-duty use, so neither has a better fit than Colson 2 Series at this size. Shepherd Hardware's big-box casters are lighter-duty consumer parts.
- **Country of origin:** Zoro lists the Colson 2.04256.445 BRK5 as made in China. The Albion is US-made.
- **Availability:** all options are stocked in the US by Zoro, Grainger, CasterHQ, Caster Specialists, Access Casters and Rockler.

## Load math

Assume a loaded Cabinet of **150 kg = 331 lb**, the top of the stated 100–150 kg range.

| Step | Value |
|---|---|
| Total load W | 331 lb (1,471 N) |
| Share per caster, **N − 1 rule** (one of four casters can lose contact on an uneven floor, so size for three) | 331 / 3 = **110 lb** |
| × 1.33 safety factor (Norlift, CasterHQ "add about a third") | 147 lb |
| × 2.0 safety factor (a conservative allowance for threshold bumps, elevator gaps, and a Rigol instrument set down hard on the top) | **221 lb** |
| Colson 2.04256.445 BRK5 rating | 300 lb, or **2.7×** the N − 1 load |
| Colson 2.04256.95 BRK5 (PU) rating | 275 lb, or 2.5× |
| Colson 3-1/2" Performa rating | 250 lb, or 2.3× |

Colson's guidance on three-caster loading is to "select casters designed to take the weight load on three casters rather than the usual four" ([Colson, Caster Combination Trucks](https://www.colsongroup.com/resources/caster-college/caster-combination-trucks/)). Colson otherwise says there is "no simple formula" and that heavier loads want larger wheels ([Colson, Select the Best Caster](https://colsongroup.com/select-the-best-caster/)). Even the 3-1/2" casters clear the conservative 221 lb target. The 4" size is chosen for rolling ease and for clearing floor joints and thresholds, not for capacity.

### Floor (VCT) check

- **The floor's limit:** Armstrong Standard Excelon VCT has a static load limit of **125 psi** (ASTM F970, at most 0.005" residual indentation) ([Armstrong spec page](https://dp-assets-new.s3.amazonaws.com/assets/78283934/Standard_Excelon_with_Diamond_10_Technology_Coating_Spec_Page_pdf.pdf)). Armstrong's maintenance guide asks that a caster's contact area be "large enough to distribute the load evenly without damaging the floor" and that the rest be made of non-staining material ([Armstrong VCT maintenance recommendations](https://dp-assets-new.s3.amazonaws.com/assets/77973165/VCT___Bio_Flooring_with_Diamond_10_Technology_Coating_Maintenance_Recommendations_pdf.pdf)).
- **Rough estimate of contact pressure:**
  - Method: Hertz line contact of an elastic wheel on a rigid floor, with the parked Cabinet's weight shared over four casters (83 lb each). The moduli are assumed, not published: about 5 MPa for 65A rubber and about 60 MPa for 45D PU. Treat the results as order of magnitude only.
  - **Performa rubber 4" × 1-1/4": about 80 psi mean, 100 psi peak.** This is under 125 psi.
  - **HI-TECH PU 4" × 1-1/4": about 270 psi mean, 350 psi peak.** This is roughly 2× the static limit, so a Cabinet parked in one spot for months could leave dents.
  - Wider and bigger wheels help only a little (a 4" × 2" PU wheel comes out at about 215 psi). The wheel material is the lever that matters.
- **Conclusion:** use a soft, non-marking rubber tread for a Cabinet that parks in one spot for long periods. Never use phenolic, nylon or cast iron on VCT.

## Swivel / rigid arrangement

Colson's descriptions ([Caster Combination Trucks](https://www.colsongroup.com/resources/caster-college/caster-combination-trucks/)):

- **Four swivel:** "Where a side motion is frequently needed, the four swivel arrangement is excellent… A most versatile arrangement." The ICWM guide agrees: use four swivels where both forward and sideways mobility are essential.
- **Two rigid, two swivel:** "Most practical and inexpensive arrangement for straight and/or long distances." The rigid pair tracks, and the swivel end steers.

For kagu, moves are short and tight: out from a bench, across the lab, and sideways into place. Parking stiffness matters more than tracking. **Recommendation: four total-lock swivels.** It also means one part number in the BOM. Four-swivel Cabinets wander on long straight pushes. If the lab finds that annoying, swap the two casters at the far end for rigid ones (Colson 2.04208.445). The plate and height are the same, so nothing else in the model changes.

**Lock type:** total lock rather than wheel-only lock. With wheel-only lock the swivel can still pivot, so the Cabinet shifts by the swivel offset when someone pushes sideways on the work surface. Total lock stops both motions ([ICWM guide](https://og.mhi.org/downloads/industrygroups/icwm/ICWM-Caster-and-Wheel-Guide-101.pdf); [Colson 2 Series](https://resources.colsongroup.com/pdf/Colson2Series.pdf)).

**Plate vs stem:** use plates. A plate spreads the load over four bolts and a 2-1/2" × 3-5/8" bearing area. Stems need a socket or insert in the wood and concentrate the load at one hole.

## Mounting plate casters to the plywood base

### What actually loads the fasteners

The caster plate bears *upward* against the underside of the base, so the Cabinet's weight goes into the wood in compression, not through the bolts. The bolts see:

- Shear when the Cabinet is pushed, or when a wheel hits a threshold.
- Cyclic loosening from vibration.
- Withdrawal only when the Cabinet is lifted or tipped, and then only the caster's own weight.

So clamp force and resistance to loosening matter more than raw pull-out strength.

### Why not lag screws into 3/4" plywood

- **Formula:** the USDA *Wood Handbook* gives the ultimate withdrawal load of a lag screw as p = 8,100 G^3/2 D^3/4 L (lb, in). It assumes a penetration of about **7D** for full strength, and below that, strength falls "about in proportion to the reduction in penetration" ([Wood Handbook ch. 8, FPL-GTR-282](https://www.cedengineering.com/userfiles/S03-019%20-%20Wood%20as%20An%20Engineering%20Material%20-%20Fastenings%20-%20US.pdf)). The NDS design form is W = 1800 G^3/2 D^3/4 lb per inch of thread penetration, with the tapered tip excluded.
- **Embedment in one sheet:** for a 5/16" lag, 7D = 2.2". A single 3/4" sheet (actually about 0.71") leaves only about 0.5" of usable thread, about 1.6D.
- **Plywood penalty:** the *Wood Handbook* also notes that withdrawal resistance in plywood is 15–30% lower than in solid wood of the same thickness (stated for nails). It says fastener withdrawal resistance per unit length falls as the number of plies rises.
- **Resulting capacity:** about 266 lb/in × 0.5" ≈ 130 lb per screw before adjustments, taking G = 0.50 as an assumption for structural plywood, not a published value. That is enough for static loads. But lags in plywood are reported to work loose under repeated moving loads, and they strip when a caster is removed and refitted.

### Recommended method

1. **Load path:** put each caster directly under a Carcass side panel (or partition) near a corner. The load then goes straight down the panel instead of bending the bottom panel. Corners also give the widest wheelbase against tipping.
2. **Caster pad (blocking):** glue and screw a pad of 3/4" plywood (or a hardwood block) about 1" larger than the plate on each side. That makes the pad about 4-1/2" × 5-5/8". The base at the bolts is then about 1-1/2" thick. Hardwood blocking under 3/4" plywood is the common shop practice for heavy cabinets.
3. **Fasteners (preferred):** four **5/16-18 hex bolts with T-nuts** per caster, which matches Colson's 5/16" bolt size.
   - Drill from below through the plate holes, using a 3D-printed drilling jig with the 1-3/4" × 2-13/16" pattern.
   - Set the T-nut in the *upper* face of the stack (the face away from the caster), so that bolt tension pulls the flange into the wood rather than out of it. Counterbore the flange flush if a Drawer or Bay floor sits above it.
   - Use a lock washer or medium threadlocker on each bolt.
   - Casters can then be replaced from below with a wrench alone, which suits four Cabinets maintained over years.
4. **Alternative:** through-bolt with carriage bolts or hex bolts. Put fender washers on the upper face and nylon-insert lock nuts under the plate, or put carriage-bolt heads on the upper face with the nuts below. This is the strongest option, but the bolt heads or nuts sit on the upper face.
5. **Lag screws:** only acceptable into the doubled 1-1/2" stack, with at least 4D (1-1/4") of thread for a 5/16" lag, and only if casters will never be removed.

Where the pad goes changes the height:

- A pad *inside* the Carcass (on top of the bottom panel) adds no height, but takes up Bay space.
- A pad *below* the bottom panel, or a separate plinth frame, adds its own thickness (about 19 mm) to the total.

## Effect of caster height on total Cabinet height

Total height = caster mount height + (pad or plinth thickness, if below the Carcass) + Carcass height + Top Module thickness.

| Caster | Mount height | Carcass + Top Module budget for 915 mm (pad inside) | With a 19 mm pad below the bottom |
|---|---|---|---|
| Colson 3-1/2" Performa | 119.1 mm | 795.9 mm | 776.9 mm |
| **Colson 4" Performa (rec.)** | **130.2 mm** | **784.8 mm** | **765.8 mm** |
| Albion 4" × 2" | 142.9 mm | 772.1 mm | 753.1 mm |
| Colson 5" Performa | 157.2 mm | 757.8 mm | 738.8 mm |

Moving from 4" to 5" casters costs 27 mm of Carcass (almost 4 gridfinity height units of 7 mm) and raises the center of gravity.

## Implications for kagu

- **Parameters:** add `caster_mount_height = 130.2 mm`, `caster_plate = 63.5 × 92.1 mm` (2-1/2" × 3-5/8"), `caster_bolt_pattern = 44.5 × 71.4 mm` (1-3/4" × 2-13/16"; slotted to 77.8 mm), `caster_bolt = 5/16-18`, and `caster_swivel_radius = 120.7 mm` (4-3/4", with total lock). The height budget for #11 (Cabinet size and Bay layout) is **915 − 130.2 − Top Module thickness** for the Carcass, less any pad below the bottom.
- **Carcass:** the Carcass bottom needs a caster pad at each corner, under a side panel. That interacts with Carcass joinery: whether the bottom is captured between the sides or sits under them.
- **Footprint:** keep each caster's 120.7 mm swivel circle inside the footprint so wheels do not stick out past the sides. A caster inset from the corners gives a smaller tipping base, so set the plates as close to the corners as the swivel circle allows.
- **Brake pedal access:** the total-lock pedals must be reachable by foot. With casters tucked fully under the Carcass, the pedals may sit behind the side panels. This may call for a toe-kick recess or for accepting a pedal that sticks out.
- **BOM per Cabinet:**
  - 4× Colson 2.04256.445 BRK5
  - 16× 5/16-18 hex bolts (length = plate + pad + bottom thickness, minus the T-nut seat)
  - 16× 5/16-18 T-nuts and 16 lock washers
  - 4 caster pads, each with a Part Label
  - About $200 for casters per Cabinet, about $800 for all four Cabinets.
- **Shop:** one 3D-printed drilling jig for the caster bolt pattern, matching the shop's jig-based approach.
- **Floor:** the rubber tread is chosen for VCT. If the lab floor turns out to be sealed concrete or epoxy, the HI-TECH PU version (2.04256.95 BRK5, 275 lb, same height) rolls easier with no other change.

## Open questions surfaced

1. **Lab floor:** confirm the floor type (VCT, sealed concrete, or epoxy) and look for thresholds or elevator gaps on the routes the Cabinets will travel. This decides rubber vs PU tread and whether 4" is enough.
2. **Height target:** is 915 mm the height of the *work surface*, so the Top Module is included? That decides the Carcass height budget.
3. **Caster pad placement:** inside the Carcass (costs Bay space) or below it, or as a plinth (costs height)? This belongs with Carcass joinery.
4. **Brake pedals:** should they stick out past the footprint for foot access, or is a toe-kick acceptable?
5. **Arrangement:** four swivels (recommended) or two swivels plus two rigid. The owner should decide after a push test on the real floor if possible.

## Sources

- Colson Group, *2 Series Top Plate Swivel & Rigid* catalog pages (capacity, load height, swivel radius, plate dimensions): https://www.accesscasters.com/content/PDF/colson-2-series-top-plate.pdf
- Colson Group, *2 Series Quick-Pick Guide* (capacity by wheel; Total Lock "locks the wheel and swivel simultaneously"): https://resources.colsongroup.com/pdf/Colson2Series.pdf
- Colson Group, product page 2.04256.441 BRK5 (mount height 5.125", swivel radius 4.75", bolt pattern 1-3/4" × 2-13/16"–3-1/16", 5/16" bolt, Performa 65A): https://colsongroup.com/2-series-casters-top-plate-swivel-zinc-with-4-x-1-25-grey-on-grey-performa-rubber-flat-wheel-and-total-lock-brake-2-04256-441-brk5
- Colson Group, product page 2.04256.445 BRK5: https://colsongroup.com/2-series-casters-top-plate-swivel-zinc-with-4-x-1-25-grey-on-grey-performa-rubber-flat-wheel-and-total-lock-brake-2-04256-445-brk5
- Colson Group, *HI-TECH polyurethane flyer* (45–55 Shore D): https://colsongroupusa.com/wp-content/uploads/2024/12/Hi-Tech-flyer-R11.pdf
- Colson Group, *Select the Best Caster* (floor-protective wheels for tile; larger wheels roll easier): https://colsongroup.com/select-the-best-caster/
- Colson Group, *Caster Combination Trucks* (swivel/rigid arrangements; three-caster loading): https://www.colsongroup.com/resources/caster-college/caster-combination-trucks/
- Colson Group, *Our Brands* (Shepherd, Jarvis, Albion, Faultless): https://colsongroup.com/our-brands/
- Institute of Caster & Wheel Manufacturers (MHI), *Caster and Wheel Guide 101* (brake definitions; four swivel vs 2+2): https://og.mhi.org/downloads/industrygroups/icwm/ICWM-Caster-and-Wheel-Guide-101.pdf
- Armstrong Flooring, *Standard Excelon Imperial Texture* spec page (static load limit 125 psi, ASTM F970): https://dp-assets-new.s3.amazonaws.com/assets/78283934/Standard_Excelon_with_Diamond_10_Technology_Coating_Spec_Page_pdf.pdf
- Armstrong Flooring, *VCT Maintenance Recommendations* (furniture rests and casters): https://dp-assets-new.s3.amazonaws.com/assets/77973165/VCT___Bio_Flooring_with_Diamond_10_Technology_Coating_Maintenance_Recommendations_pdf.pdf
- USDA Forest Products Laboratory, *Wood Handbook* (FPL-GTR-282), ch. 8 *Fastenings* (lag screw withdrawal; plywood fastening): official copy https://www.fpl.fs.usda.gov/documnts/fplgtr/fplgtr282/chapter_08_fpl_gtr282.pdf (mirror used: https://www.cedengineering.com/userfiles/S03-019%20-%20Wood%20as%20An%20Engineering%20Material%20-%20Fastenings%20-%20US.pdf)
- Engineers Edge, summary of the AWC NDS lag screw withdrawal equation (W = 1800 G^3/2 D^3/4, tip excluded): https://ns1.engineersedge.com/calculators/lag_screw_withdrawal_force__16073.htm
- Norlift, caster load sizing (add 33%): https://www.norlift.adpearance.com/wheels-and-casters/start-here
- CasterHQ, load capacity calculator (N − 1 rule, 1.25–1.33 factor): https://casterhq.com/blogs/caster-guide/caster-load-capacity-calculator
- CasterHQ, Albion 16XI04202ST listing (1,000 lb, 5.63" height, ~$84): https://casterhq.com/products/albion-casters-4-x-2-usa-made-top-total-lock-caster-with-solid-polyurethane-wheel-and-4-x-4-5-plate-heavy-duty-industrial-caster-16xi04202st
- Zoro, Colson 2.04256.445 BRK5 listing (~$50.59, origin China): https://www.zoro.com/colson-4-x-1-14-non-marking-rubber-performa-flat-swivel-caster-top-lock-brake-loads-up-to-300-lb-204256445-brk5/i/G7239724
- Zoro, Shepherd Hardware PRE40120ZN-TPUB (tread lock, 150 lb): https://www.zoro.com/shepherd-hardware-4-x-1516-non-marking-polyurethane-swivel-caster-tread-lock-brake-loads-up-to-150-lb-pre40120zn-tpub/i/G7812098/
- PartsSource, Colson 2.05256.445 BRK5 (~$91.41): https://www.partssource.com/parts/colson/205256445brk5
- Rockler, 4" 300-lb polyurethane total-lock caster #84718 (~$13.99): https://www.rockler.com/4-300-lb-polyurethane-caster-swivel-w-total-lock-brake
- Shop practice on caster mounting in plywood (anecdotal; hardwood backer blocks, through-bolts, lags loosening): https://www.sawdustzone.org/forum/discussions/project-related-discussions/3721-attaching-casters

**Not verified against a primary source:** the specific-gravity value used for plywood fasteners (G = 0.50 for Structural I, 0.42 otherwise, NDS Table 12.3.3B), the elastomer moduli in the floor-pressure estimate, and the Rockler caster's OEM and height.
