# Plywood stock and saw-only joinery

Research for [#8](https://github.com/uf-cpe-design-lab/kagu/issues/8). It feeds [#16](https://github.com/uf-cpe-design-lab/kagu/issues/16) (order and evaluate plywood samples) and [#10](https://github.com/uf-cpe-design-lab/kagu/issues/10) (Carcass construction and joinery). Researched 2026-11-08. Prices and stock change often, so quote them again before ordering.

## Recommendation

1. **Use an all-birch-core 18 mm panel for the Carcass.** That means Baltic birch BB/BB, or an equivalent like Columbia Europly or a "SuperCore"/Premcore birch-core panel. Avoid 5-ply or softwood-core 3/4" hardwood ply. An all-birch core gives a consistent thickness (13 plies at 18 mm), few core voids, edges that look acceptable once finished, and better screw holding in the panel edge. Confirmat and pocket screws depend on edge holding.
2. **Prefinished or unfinished: let the #16 samples decide, but design the joinery to work with both.** The deciding fact is that **wood glue does not bond reliably to a UV-cured finish.** Titebond says its glues are for bare wood and need substrates "clean of any type of paint, stain, or sealer". Columbia's own FinishLine literature gives no gluing guidance. So, for both options:
   - **Dados and rabbets** locate the parts and carry shear. They are cut on the table saw or with a router.
   - **Confirmat screws (7 x 50 mm)** pull the joints tight. They are drilled with a stepped bit, through a 3D-printed jig with a steel bushing.
   - **Glue is a bonus, not a requirement.** On unfinished stock you glue the rabbets and dados. On prefinished stock you assemble dry, or glue only to surfaces cut after finishing.

   This is how glueless prefinished and melamine casework is built, and it is the strongest of the knock-down connectors in the published tests (see [Joinery](#joinery-comparison-for-this-shop)).
3. **Lean prefinished (UV, two sides) if a sample passes #16.** About 4 Cabinets come to roughly 40 m² (about 450 ft²) of panel face. Finishing that by hand with water-based poly at 3 coats is days of lab labor plus a 21-day cure. A factory UV finish also takes cleaning chemicals better (Columbia UV LabCoat is SEFA 8 spot-test rated). The cost is that you lose glue as a structural backup, and scratches made during the build are hard to repair.
4. **Fall back to unfinished BB/BB Baltic birch** if the prefinished samples are not flat, have edge voids, or are hard to get as full sheets near Gainesville. Then glue every rabbet and dado, and finish with a water-based poly.
5. **Make actual thickness a measured parameter.** Nominal 3/4" stock ranges from about 17.8 to 18.7 mm across the products below. Measure each delivered batch, then set the dado width and the build123d `ply_thickness` from that measurement.

## Plywood comparison

"Actual thickness" is the seller's or the standard's stated value, not one we measured. #16 has to measure it.

| Type | Actual thickness | Sheet size | Core, voids, flatness | Price per sheet (as listed) | Samples / small pieces | Link |
|---|---|---|---|---|---|---|
| **Baltic birch BB/BB 18 mm** (unfinished, imported) | 18 mm (≈0.709"), 13 plies | 5x5 ft (1525 mm) traditional; 4x8 also sold | All-birch, solid single-piece inner plies (WWS). BB face: up to ~6 color-matched patches per face (WWS). No published flatness number found. | Baird Brothers 4x8 BB/BB 13-ply **$91.59**. WWS 25 ft² pre-cut pack **$124** (sale, list $155) shipped free. Rockler 30x30" **$45.99** | Yes, effectively: by-the-piece and pre-cut packs ship (WWS 20x30" **$34.99**; Rockler 30x30"; Makerstock custom cuts at $12 per 50 lb flat-rate shipping) | [WWS pack](https://www.woodworkerssource.com/plywood/34-baltic-birch-plywood-pack-choose-your-size.html), [WWS 20x30](https://www.woodworkerssource.com/shop/product/balrec3420.html), [Baird Bros 4x8](https://www.bairdbrothers.com/mobile/34-Baltic-Birch-Plywood-13-ply-48-x-96-sheet-size-P55184.aspx), [Rockler](https://rockler.com/baltic-birch-plywood-choose-thickness) |
| **Columbia Europly 3/4"** (birch core, domestic face, unfinished) | 3/4" nominal, 13-ply birch | 4x8 (via distributors) | 100% birch core, made by Paged-Morag (Poland). Phenolic core glue, soy face glue. "Europly PLUS" sold as "virtually void free" | Distributor quote (Würth Wood Group, Amerhart etc.) | Not to the public. Ask a distributor for an offcut | [Columbia Europly sheet](https://www.columbiaforestproducts.com/app/uploads/2024/02/2024-121_Europly_Product_r1_HQ.pdf) |
| **US hardwood ply, veneer core** (e.g. Columbia PureBond maple, unfinished) | 23/32" (0.719") nominal. HP-1 sanded tolerance not verified (see note) | 4x8 | Mixed-species veneer core. Ply count varies (Ring's End's prefinished maple is **5-ply**, so thick plies and more core voids). Soy-based NAUF glue | Home Depot stocks PureBond (price not retrieved) | Home Depot 2x2 ft and 2x4 ft "project panels" act as cheap samples | [Columbia PureBond (HD)](https://www.homedepot.com/p/Columbia-Forest-Products-3-4-in-x-4-ft-x-8-ft-PureBond-Prefinished-1S-Maple-Plywood-4360/310617730) |
| **Prefinished UV maple, veneer core** (Columbia UV Wood / LabCoat, Rockshield etc.) | 23/32"–3/4" nominal | 4x8 | Columbia UV Wood: modified acrylate, 1.0–1.5 mil dry film, 100% solids, 0 VOC; LabCoat 2.3–3.5 mil. Core depends on the order (veneer core, MDF, PB) | Ring's End C2 5-ply UV 2 sides **$148**. Rockshield UV2S white maple (DK Hardware) **$225.40**. HD PureBond prefinished **1S** (one side) 4x8 | **Columbia FinishLine sample box, free "to architects, fabricators and other specifiers"** (a university lab can ask). HD prefinished maple 2x2 project panels | [Columbia FinishLine](https://www.columbiaforestproducts.com/product/finishline/), [UV LabCoat](https://www.columbiaforestproducts.com/plywood/uv-labcoat), [Ring's End](https://www.ringsend.com/prefinished-maple-plywood-mapleprefnply), [Rockshield](https://www.dkhardware.com/rockshield-engineered-wood-vx24mawp3wmasp3vuv2-white-maple-3-4-4x8-mvcm-c2-pf2-products-product-8982445.html) |
| **Prefinished UV birch, hardwood multi-ply core** (WWS "SuperCore" / "Premcore Plus" UV2, CANUSA) | 18 mm nominal (WWS gives no measured value) | 4x8 full sheets (**store pickup only**, AZ). Pre-cut packs up to 24x45" **ship free** | "Same number of inner hardwood layers" as Baltic birch, sold as "void-free" (marketing). UV on both faces, C-2 or better, whole-piece face | Premcore Plus UV2 **$89–95**, SuperCore UV2 **$109** (pickup). Pre-cut SuperCore pack from **$48** (sale) | **Yes**: small pre-cut packs ship to the lower 48 and work as samples | [WWS prefinished](https://www.woodworkerssource.com/prefinished-plywood.html), [SuperCore pack](https://www.woodworkerssource.com/34-18mm-prefinished-supercore-white-birch-pre-cut-plywood-pack-choose-your-size.html) |
| **Prefinished UV Baltic birch B/BB** | 18 mm (thinner stock is more common) | 5x5 (cut to size, no full-sheet shipping) | Baltic birch core, UV on 2 sides | Quote. The 3/4" listing was **sold out** when checked | Custom cuts ship ($12 per 50 lb flat rate) | [Makerstock UV BB](https://makerstock.com/products/baltic-birch-plywood-uv-prefinished-b-bb-finished-both-sides-copy) |
| **Prefinished birch, big-box** (Home Depot) | **0.703"** actual (listed) | 4x8 | Unspecified core, prefinished faces | HD price (not retrieved) | Buy one sheet locally | [HD prefinished birch](https://www.homedepot.com/p/Prefinished-Birch-Plywood-Common-3-4-in-x-4-ft-x-8-ft-Actual-0-703-in-x-48-in-x-96-in-971080/203005208) |
| **ApplePly** (States Industries) | Thin 1/16" birch plies | Full sheets go through distributors only. BuyApplePly.com sells cut panels (24x24 up to 32x48) | Highest-grade veneer core, "minimum number of voids", attractive edge. NOVA UV finish available to order (clear, satin to high gloss). No UF resin | BuyApplePly 1" white birch 24x24 **$54.42**. 3/4" full sheets about $100–118 in old forum posts (dated) | Cut panels ship, but the landing page does not show 3/4". Ask States: 800-626-1981 | [States core comparison](https://www.statesind.com/core-comparison/), [BuyApplePly](https://www.buyappleply.com/) |

Notes on the table:

- **HP-1 thickness tolerance is unverified.** ANSI/HPVA HP-1-2024 is the governing standard for US hardwood plywood, but its text is paywalled. Secondary sources disagree: some give 1/64" for sanded panels up to 3/4", and one manufacturer gives ±0.8 mm. Do not design to either figure. Measure instead. GOST 3916.1 governs Baltic birch. A supplier quotes ±0.3 mm only "under special requirements", and an unverified copy of the formula gives roughly +0.7/−0.9 mm at 18 mm.
- **The Baltic birch supply is politically exposed.** The US raised the tariff on Russian birch plywood to 50% in 2022. The EIA reports that product was then rerouted through third countries such as Vietnam. Expect "Baltic birch" from mixed origins at mixed quality, which is another reason to sample before buying the full order.
- **5x5 vs 4x8.** A 5x5 sheet (2.32 m²) holds less than a 4x8 (2.97 m²), and with Carcass panels around 500 x 780 mm it nests worse (see the sheet count below). A 4x8 is heavy (one forum post gives about 115 lb for 4x8 Baltic birch; Amerhart gives about 70 lb for 3/4" veneer core) and is hard to ship without damage. Buy full sheets locally (Home Depot, or a trade distributor such as Würth Wood Group, which lists a Tampa branch in a directory) and use shipped pre-cut packs for samples.

## Prefinished vs unfinished

| | Prefinished (UV, 2 sides) | Unfinished (finish in the lab) |
|---|---|---|
| **Glue adhesion** | Poor on the finish. Titebond: glues are "designed to bond bare wood", substrates must be "clean of any type of paint, stain, or sealer", and Super Titebond says "Do not apply to finished surfaces". Shop reports (WoodWeb) say glue "does not stick to the UV finish" and that joints that do stick fail by peeling the finish off the wood. Scuffing plus melamine glue (Roo Clear, Titebond Melamine) or contact cement helps, but it is anecdotal. **Design rule: glue only raw surfaces cut after finishing (dado walls, panel edges), or don't count on glue at all.** | Glue works everywhere. Glued rabbets and dados are the strongest and most forgiving joints in this shop. |
| **Edge treatment** | The same either way: factory UV covers faces only, so edges are raw. Iron-on edge banding (13/16" wide for 3/4" ply, hot-melt, household iron with no steam) bonds to the raw edge, so prefinishing does not affect it. | All-birch-core edges can be left exposed and finished. Veneer-core edges need banding or solid-wood edging. |
| **Finish quality and durability** | Factory UV acrylate is hard and solvent-wipeable (Columbia supports acetone wipe-down). Columbia **UV LabCoat** passed SEFA 8.1 chemical spot, 8.2 hot water and 8.3 impact tests, which suits a lab. Damage done during the build (clamp marks, glue squeeze-out, scratches) is hard to blend in. | Water-based poly such as General Finishes High Performance: 3 coats minimum, 2+ h between coats, light use after 7–10 days, **full cure 21 days**. Durable, but not lab-chemical grade. Easy to touch up later. |
| **Labor for ~4 Cabinets** | None for faces. Edges only (banding plus a wipe of finish). | Roughly 40 m² (450 ft²) of face area for 4 Cabinets, both faces of every part (estimate below), plus edges. Sanding to 180–220 grit, then 3 coats with scuff-sanding between, needs dust-free rack space and 21 days of cure. Our estimate is 3–6 shop days of finishing for the whole run. You can cut this by finishing only faces that show, and leaving Drawer box interiors raw or prefinished. |
| **Buying** | Fewer sources. Full sheets mostly through trade distributors, with minimums for custom orders (Columbia's mill minimums are 120–240 panels). Retail full sheets: HD (often 1S, one side only), Ring's End, Rockshield. | Widely available. BB/BB ships as pre-cut packs and is stocked by local dealers. |

## Joinery comparison for this shop

The shop has a table saw (with a dado stack), router, drill press, miter saw, and a Prusa XL for printed jigs.

| Joint | Strength | Squareness | Repeatability with printed jigs | Knock-down | Works on prefinished? | Notes |
|---|---|---|---|---|---|---|
| **Dado / rabbet + glue** | High: long-grain glue area plus mechanical shoulder. Best for racking. | Good. The shoulder registers the part, so squareness comes from accurate cuts. | No jig needed. Needs a dado stack or router set to the **measured** ply thickness (undersized "plywood" router bits exist for 23/32" and 18 mm stock). | No | Only partly: the dado walls are raw, but the mating face is finished, so glue mostly bonds the edge to the dado bottom. | The baseline joint for an unfinished Carcass. |
| **Dado / rabbet + Confirmat 7x50** | High. The INNO plywood T-joint study ranked Confirmat Ø7x50 and Ø7x70 among the strongest detachable joints, and the Croatian studies found Confirmat stronger than Minifix. | Good: the rabbet locates the part, the screw pulls it tight. | **Good.** Clamp the joint and drill both parts in one pass with a stepped bit (5 mm pilot in the edge part, larger clearance plus countersink in the face part). A printed jig only has to set the hole position along the face. Use press-fit steel drill bushings, not bare plastic. | Yes, a few times. Threads in plywood edge wear with repeated driving. | **Yes**, it needs no glue. This is how glueless casework is built. | **Recommended for the Carcass** with either stock. Edge distance and spacing to be confirmed from Häfele's technical sheet. |
| **Pocket screws** (Kreg, 1-1/4" coarse #8 for 3/4" stock) | Medium–high in shear. Weaker than a dado against racking. | Fair. Parts can creep while the screw is driven, so clamp. | The Kreg jig itself is repeatable, so printed jigs are not needed. Set it to actual thickness (Kreg says to use actual, not nominal). | Partly | Yes | Fast, but leaves visible holes on one face. Good for face frames and hidden joints, and for Top Interface rails. |
| **Cross dowel / barrel nut + machine screw** | High (ranked with Confirmat in the INNO study) | Good with a rabbet | Good. Two holes (edge and face), both doable on the drill press with a printed V-block or edge jig. | **Yes, repeatedly.** Machine thread into steel. | Yes | Use where a part must come off: a removable back for wiring, Top Interface, Tool Wall panels. |
| **Threaded inserts + machine screws** | Medium. Depends on the insert's grip in ply. | Needs a locating feature | Good (drill press) | Yes, repeatedly | Yes | Attaching hardware: casters, Top Interface, slides. |
| **Minifix / cam lock** (Häfele Minifix 15: 15 mm bore, 24/34 mm from edge, about 14 mm deep in 19 mm stock) | **Lowest** of those tested. The INNO plywood study ranked eccentric connectors last. In 21 mm multi-layer panels, Minifix reached 6.15 N·m against 10.53 N·m for Confirmat (Hrčak). A diagonal-test study in MDF and particleboard found it 2–3x weaker. | Fair | Possible: 15 mm Forstner bore to a precise depth plus an edge pin. Steel drilling guides exist. | Yes, best for frequent knock-down | Yes | Not recommended for a rolling Cabinet with racking loads from the casters. |

A mobile Cabinet takes racking from the casters every time it rolls over a threshold. Whichever corner joint is chosen, the Carcass should get its racking stiffness from a **3/4" (or at least 1/2") back panel captured in rabbets and fastened all round**, plus a bottom stiff enough for the caster plate. This matters more than the choice of corner fastener. It is our engineering judgment, not a sourced figure.

## Estimated sheet count for one Cabinet

These are placeholder dimensions until the Bay and Drawer tickets settle them. The Carcass is 590 W x 500 D x 780 H mm of 18 mm ply, sized for a 12-unit (504 mm) gridfinity Baseplate plus side-mount slides, under a ~915 mm overall height with casters and Top Module. Parts:

- 2 sides
- top and bottom
- a 3/4" back in rabbets
- a bottom doubler for the casters
- full-overlay Drawer fronts
- 6 Drawer boxes in 1/2" stock with 1/4"–1/2" bottoms

The script is at the end of this section. It assumes 80% nesting yield.

| Stock | Area | 4x8 sheets | 5x5 sheets |
|---|---|---|---|
| 3/4" Carcass panels | 2.09 m² | 0.9 | 1.1 (the back doesn't nest well) |
| 3/4" Drawer fronts | 0.46 m² | 0.2 | 0.25 |
| 1/2" Drawer box sides/ends | 1.26 m² | 0.5 | 0.7 |
| Drawer bottoms | 1.45 m² | 0.6 | 0.8 |

Per Cabinet that comes to about **1.1–1.3 sheets of 3/4" in 4x8** (about 1.5–2 sheets of 5x5) plus about **1 sheet of 1/2"/1/4"**. For **4 Cabinets, buy about 6 sheets of 3/4" 4x8 (or 8 of 5x5) and 4–5 sheets of 1/2"**, which includes about 15% spare for test cuts and jig setup. The face area to finish (both faces) is about 10.5 m² (113 ft²) per Cabinet, or about 42 m² for 4.

```python
# research/plywood-joinery.md sheet estimate (mm); placeholder Carcass 590 W x 500 D x 780 H
parts_34 = [(2,780,500),(1,554,500),(1,554,500),(1,590,780),(1,590,500),(1,590,780)]  # sides, top, bottom, back, doubler, fronts
sheet_4x8, sheet_5x5, yield_ = 1.2192*2.4384, 1.525*1.525, 0.8
a = sum(n*w*h for n,w,h in parts_34)/1e6   # 2.55 m2 -> 1.07 4x8 / 1.37 5x5
```

## Sample-evaluation checklist for #16

**Order these samples.** Aim for at least 2 ft x 2 ft each, so flatness means something.

| # | Vendor | Product | How to get the sample | Sheet sizes for the real order |
|---|---|---|---|---|
| S1 | Woodworkers Source (Phoenix, ships to the lower 48) | 3/4" (18 mm) **Prefinished SuperCore** white birch UV2 pre-cut pack | Smallest pack (4 pcs 15x30"), free shipping, from about $48 on sale | 4x8 (pickup only in AZ), so you'd need an equivalent locally |
| S2 | Woodworkers Source | 3/4" **Baltic birch BB/BB** by the piece, 20x30" | $34.99 each, ships | 5x5 / 4x8 locally or Baird Brothers |
| S3 | Columbia Forest Products | **FinishLine sample box** (UV Wood, UV LabCoat) | Free to "specifiers": email or call Columbia (800-637-1609) as the UF CpE design lab | 4x8 via distributor (Würth Wood Group etc.) |
| S4 | Home Depot (local) | Columbia **PureBond prefinished maple** 2x2 project panel, and the 4x8 prefinished birch (0.703") if stocked | Buy in store | 4x8 |
| S5 | Makerstock | **UV prefinished Baltic birch B/BB** custom cut, 18 mm | Custom-cut quote ($12 per 50 lb flat rate). The 3/4" was sold out when checked | 5x5, cut to size only |
| S6 (optional) | States Industries | **ApplePly** 3/4", optionally NOVA UV | Call 800-626-1981 or check BuyApplePly.com | 4x8 via distributor |

**Check each sample for the following.** Record the results in the #16 ticket.

1. **Actual thickness.** Use calipers at at least 4 points ≥100 mm from the edges (the GOST method), and give the mean and the range in mm. Pass if the range is ≤0.3 mm across the sample and the mean is within ±0.4 mm of what the seller claims.
2. **Flatness.** Lay the sample on the table saw top and measure the cup and twist gap with feeler gauges. Re-check after 1 week in the lab, because humidity matters in Gainesville. No published spec was found, so set our own pass mark, for example ≤1 mm over 600 mm.
3. **Core and edge voids.** Rip a fresh edge on each side, then count and measure the voids (a void >3 mm long is a defect). Count the plies, and check that the core is all hardwood with no softwood or filler plies.
4. **Face quality.** Patches, splits, and any sand-through of the face veneer.
5. **Dado fit.** Cut a test dado with the dado stack or router bit you intend to use, and check that the sample slides in snugly by hand.
6. **Edge screw holding.** Drive a Confirmat 7x50 into the edge, using a stepped-bit pilot centered in the edge. Look for splitting or delamination, then do 3 remove-and-redrive cycles and note whether it still holds tight. Repeat with a 1-1/4" coarse pocket screw.
7. **Glue test, prefinished samples only.** Glue three lap joints (50 x 50 mm overlap) to raw scrap and break them by hand or in a vise after 24 h:
   - (a) Titebond on the unscuffed finish
   - (b) Titebond on the finish scuffed with 120 grit
   - (c) melamine glue (Titebond Melamine or Roo Clear) on the scuffed finish

   For each, note whether the joint fails in the wood, in the glue, or by peeling the finish off.
8. **Finish durability, prefinished samples.** Scratch the finish with a screwdriver tip and a fingernail. Wipe it with IPA and with acetone (Columbia says acetone wipe-down is fine). Leave flux remover and solder flux on it for 1 h. Put a hot soldering iron stand near it, but not on it.
9. **Finish feel and sheen.** Compare the samples against the lab's expectations: glare under the lab lights, and how fingerprints show.
10. **Edge banding.** Iron on 13/16" birch banding, trim it, and finish the edge. Separately, finish a bare all-birch edge, and judge whether banding is needed at all.
11. **Full-sheet availability near Gainesville.** For each candidate, write down where you can actually buy about 6 full 3/4" sheets: price, lead time, and delivery or pickup.

## Implications for kagu

- **Parameters:** `ply_thickness` (measured, default 18.0 mm), `back_thickness`, `drawer_stock_thickness`. Dado widths and rabbet depths are derived from these and never hard-coded as 19.05 mm.
- **#10 Carcass construction:** use rabbet and dado joints for location, Confirmat 7x50 to clamp them, and glue only when the stock is unfinished. Capture the back in rabbets, since it is the main racking structure. Use cross dowels or threaded inserts where a part must come off, such as the Top Interface, a wiring access back, or Tool Wall panels.
- **Drilling jigs:** these are 3D-printed bodies with press-fit steel bushings. They register off a panel edge or face and are sized for the Prusa XL. Needed: a Confirmat face jig (drill through the clamped joint with a stepped bit), an edge jig for cross dowels, and a drill-press fence and stop for insert holes. Each jig references the same hole pattern as the CAD model, so every Part Label's holes come from one source.
- **Part Labels:** on prefinished stock, mark them on surfaces cut after finishing or hidden from view, or on removable tape, because marker on a UV finish is hard to remove.
- **Glossary gaps (for `/domain-modeling` later):** "Back panel" and "Drawer front" are used here but are not glossary terms yet. "Drilling jig" also probably deserves an entry, since Part Labels and the hole pattern hang off it.
- **Finish/edge treatment (map "Not yet specified")** is now coupled to the stock choice: prefinished means edge banding or finished bare edges only, and unfinished means water-based poly and 21 days of cure in the schedule.

## Open questions

- Can UF buy on a trade account at a distributor such as Würth Wood Group (directory lists a Tampa branch)? That decides whether Columbia UV LabCoat or Europly full sheets are realistic.
- Does the lab need SEFA-grade chemical resistance (flux, IPA, acetone), or is ordinary UV or poly enough?
- Is the Carcass ever meant to be knocked down (moved through doors, shipped)? If so, use cross dowels rather than Confirmat at the corners.
- The Confirmat edge distance and spacing in 18 mm ply need Häfele's technical sheet. A retailer says 7x50 suits 3/4" stock, but there is no official edge distance.

## Sources

Manufacturers and standards:

- Titebond (Franklin International), FAQs (bare wood only, clean of paint/stain/sealer; clamping times): https://www.titebond.com/resources/use/all/faqs
- Super Titebond product page ("Do not apply to finished surfaces"): https://www.titebond.com/print/product/0c432f73-dd8c-40de-8734-68eaf96f8e71
- Columbia Forest Products, FinishLine (UV Wood/LabCoat film thickness, sheens, acetone wipe, mill minimums, free sample box for specifiers): https://www.columbiaforestproducts.com/product/finishline/
- Columbia UV Wood: https://www.columbiaforestproducts.com/plywood/uv-wood
- Columbia UV LabCoat (SEFA 8.1/8.2/8.3): https://www.columbiaforestproducts.com/plywood/uv-labcoat and https://www.columbiaforestproducts.com/app/uploads/2024/09/UV-Labcoat-Product-Sheet-91624.pdf
- Columbia Europly product sheet (13-ply birch, Paged-Morag, phenolic core): https://www.columbiaforestproducts.com/app/uploads/2024/02/2024-121_Europly_Product_r1_HQ.pdf
- States Industries, core comparison (ApplePly 1/16" birch plies, two-step lamination): https://www.statesind.com/core-comparison/
- States Industries ApplePly brochure: https://www.statesind.com/wp-content/uploads/2022/08/Appleply-States-Industries.pdf
- ANSI/HPVA HP-1-2024 (listing; text not retrieved): https://forestsource.io/resources/document/american-national-standard-for-hardwood-and-decorative-plywood-ansihpva-hp-1-2024
- GOST 3916-96 (unofficial copy, thickness measurement method): https://www.scribd.com/document/534587548/GOST-3916-96
- Kreg screw guide (3/4" stock, 1-1/4" coarse for plywood; use actual thickness): https://learn.kregtool.com/learn/how-to-select-right-pocket-hole-screw/ and https://learn.kregtool.com/learn/why-material-thickness-matters/
- General Finishes High Performance (3 coats min, 2+ h recoat, 21-day cure): https://generalfinishes.com/sites/default/files/documents/files/2019-05/TDS-2019-04-High-Performance-General-Finishes.pdf
- Häfele Minifix 15 drilling (catalogue): https://files.hafele.co.uk/CatalogFiles/www/23C3-44.pdf. Minifix 24/34 drilling guide: https://www.blum.org.uk/collections/hafele/products/drill-guide-minifix-15-34
- Häfele Confirmat 7x50 (5 mm drill hole): https://www.heimwerkertools.com/en/tools/fixing-material/screws/145/haefele-confirmat-counter-head-connector-for-oe-5-mm-drill-hole-steel-with-phillips-pz3-cross-slope-galvanized and stepped bit kit: https://www.mcfeelys.com/7mm-x-50mm-confirmat-cabinet-assembly-screws-starter-kit.html

Joint strength studies:

- "Bending strength of T-shape corner detachable joints of structural elements made of plywood", INNO journal: https://innojs.ltu.bg/index.php/scjournal-inno/article/view/212
- Corner L separable assemblies in storage furniture (Drvna industrija 2021): https://drvnaindustrija.com/archive/volume-2021-issue-1/research-into-corner-l-separable-assemblies-in-storage-furniture/
- Diagonal tension/compression of RTA joints in MDF and particleboard (Minifix 2–3x lower): https://rcastoragev2.blob.core.windows.net/615f9ae52dfb395d80c814d59e0fa60c/PMC8434206.pdf
- Confirmat vs Minifix in multi-layer panels (Hrčak): https://hrcak.srce.hr/252024

Vendors (prices as listed 2026-11-08):

- Woodworkers Source, 3/4" Baltic birch pre-cut pack: https://www.woodworkerssource.com/plywood/34-baltic-birch-plywood-pack-choose-your-size.html. 20x30 piece: https://www.woodworkerssource.com/shop/product/balrec3420.html
- Woodworkers Source, prefinished: https://www.woodworkerssource.com/prefinished-plywood.html. SuperCore UV2 pack: https://www.woodworkerssource.com/34-18mm-prefinished-supercore-white-birch-pre-cut-plywood-pack-choose-your-size.html. Premcore UV2 4x8: https://www.woodworkerssource.com/plywood/premium-white-birch/prefinished-birch-white-plywood-18mm.html
- Baird Brothers, 3/4" Baltic birch 13-ply 4x8: https://www.bairdbrothers.com/mobile/34-Baltic-Birch-Plywood-13-ply-48-x-96-sheet-size-P55184.aspx
- Rockler Baltic birch: https://rockler.com/baltic-birch-plywood-choose-thickness
- Makerstock UV prefinished Baltic birch: https://makerstock.com/products/baltic-birch-plywood-uv-prefinished-b-bb-finished-both-sides-copy and custom cuts: https://makerstock.com/pages/custom-cuts
- Home Depot, Columbia PureBond prefinished 1S maple 4x8: https://www.homedepot.com/p/Columbia-Forest-Products-3-4-in-x-4-ft-x-8-ft-PureBond-Prefinished-1S-Maple-Plywood-4360/310617730. Prefinished birch 0.703": https://www.homedepot.com/p/Prefinished-Birch-Plywood-Common-3-4-in-x-4-ft-x-8-ft-Actual-0-703-in-x-48-in-x-96-in-971080/203005208
- Ring's End prefinished maple: https://www.ringsend.com/prefinished-maple-plywood-mapleprefnply
- Rockshield UV2S maple (DK Hardware): https://www.dkhardware.com/rockshield-engineered-wood-vx24mawp3wmasp3vuv2-white-maple-3-4-4x8-mvcm-c2-pf2-products-product-8982445.html
- Amerhart, Columbia UV2S maple (weight ~70 lb): https://www.amerhart.com/product/columbia-forest-products-rotary-cut-maple-c2-uv2s-medium-gloss-naf-veneer-core
- BuyApplePly: https://www.buyappleply.com/
- Würth Wood Group, 3/4" import birch BB/BB 4x8 listing: https://www.wurthwoodgroup.com/Baltic-Birch-Plywood-4-Import--BBBB--5-Ply-VC/

Trade and supply context:

- EIA, Russian birch report (50% tariff, rerouting): https://eia.org/wp-content/uploads/2022/09/russian-birch-report.pdf
- Wood Central, ongoing Russian plywood imports: https://woodcentral.com.au/four-years-into-ukraine-war-u-s-is-still-hungry-for-russian-plywood/

Anecdotal (forums; used only where no primary source exists):

- WoodWeb, Gluing UV-prefinished plywood: https://woodweb.com/knowledge_base/Gluing_UVPrefinished_Plywood.html
- WoodWeb, Glue for dado joints in prefinished ply: https://woodweb.com/knowledge_base/Glue_for_Dado_Joints_in_Prefinished_Ply.html
- Fine Homebuilding, installing iron-on edging: https://finehomebuilding.com/2005/09/01/installing-iron-on-edging
