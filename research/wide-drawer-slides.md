# Slides and anti-racking for ~1.1 m wide Drawers

Research for [#19](https://github.com/uf-cpe-design-lab/kagu/issues/19), part of the wayfinder map [#1](https://github.com/uf-cpe-design-lab/kagu/issues/1). It builds on [`research/drawer-slides.md`](https://github.com/uf-cpe-design-lab/kagu/blob/research/drawer-slides/research/drawer-slides.md) (#4: ½" side-mount slides for Drawers up to about 24") and [`research/interlocks-locks.md`](https://github.com/uf-cpe-design-lab/kagu/blob/research/interlocks-locks/research/interlocks-locks.md) (#5: CompX Timberline lockbar). Neither is repeated here.

**Question:** Which slides and anti-racking measures suit one column of **~1.1 m wide** gridfinity Drawers (about 26 units, 1100–1120 mm inside), about 450–500 mm deep, in a ~1.2 m wide plywood Cabinet? Also covered: load ratings, side clearance, minimum Drawer height, fit with a single Timberline lockbar, price, US availability, and Drawer-bottom stiffness over the span.

**Sources:** manufacturer catalogues, technical sheets, installation instructions and declarations of performance (Accuride, Knape & Vogt, Blum, CompX Timberline, Metsä Wood, UPM), plus one expired patent. They are listed under [Sources](#sources). Some Accuride documents are distributor-hosted copies, and each carries Accuride's own document number. Everything was checked on **2026-11-08**. Prices marked *(snippet)* come from a search-engine snapshot of the retailer page, not a live page load, because accuride.com and several retailers block automated fetches. **(assumption)** marks my own inference or engineering judgment, not a maker's figure.

## Recommendation

1. **No side-mount ball-bearing slide found has a published rating for a Drawer as wide as 1.1 m.** The widest side-mount rating from both Accuride and Knape & Vogt is **42" (1067 mm)**. That covers the Accuride 3600/3657, 3634, 3641, 7950/7957 and 9301E/9308E, and the KV 8810 and 8900. Every ½"-side-space slide in #4 stops at 24–36". A 26-unit Drawer box is about **1117 mm (44.0") outside**, which is 4.7 % over that limit. Only two products are rated wider, and both are **undermount**: the Accuride 3160EC (60", but only 100 lb) and the Blum MOVENTO with its side stabiliser (cabinet width up to 1400 mm, 40–70 kg class).
2. **Recommended: size the Drawer to the 42" class and use ¾"-side-space heavy-duty slides.**
   - **Width:** **25 units** wide with 12 mm (½") Drawer sides. The box comes out at about 1075 mm (42.3"), which is 8 mm over 1067 mm, close enough to treat as at the limit **(assumption)**. Drop to **24 units** (1033 mm, 40.7") if you want to stay strictly inside the published figure.
   - **Slides:** **Accuride 3657** (lever disconnect, hold-in detent, 53.1 mm tall) or the **Accuride 3600** (the same envelope without a disconnect). Accuride rates the family at **200 lb per pair in frequent use and 273 lb in moderate use, tested with 18" slides on a 42" drawer for 75,000 cycles**. Side space is **0.75" +0.030/−0 (19.1 +0.76/−0 mm)**. The **KV 8810** (200 lb class, 42" maximum, 0.765" +0.02/−0.01, hold-in detent, butterfly lever, 53 mm) is a second source.
   - **Heaviest tool Drawers:** step up to the **Accuride 7957**: 350 lb (18" slides on a 42" drawer, 10,000 cycles), 70.8 mm tall.
   - **Side gap:** set it to **19.4 mm per side** for this column. That value sits inside the Accuride 3600/7957 band (19.05–19.81 mm), the KV 8810 band (19.18–19.94 mm) and the KV 8900 band (19.05–19.81 mm).
3. **Add a synchroniser and a centre pull, even within the 42" rating.** Accuride's own guidance is that drawers wider than they are deep rack, and that wide drawers should have "a central pull handle". I found **no off-the-shelf synchroniser for side-mount ball-bearing slides**. The credible DIY option is a **rack-and-pinion synchroniser** (see [Anti-racking](#anti-racking-and-synchronisation)): printed gear racks on the Carcass, and a pinion at each rear corner of the Drawer on one steel shaft that runs behind the Drawer back. Blum's commercial stabiliser uses the same layout, and so does the expired Standard Precision patent US 4,324,439. A crossed-cable anti-rack is the cheaper fallback.
4. **Build the Drawer bottom so it spans front-to-back (about 480 mm), not side-to-side (about 1050 mm).** A 12 mm (½") birch bottom captured and glued on all four edges deflects only **0.4 mm (0.8 mm long-term) under 50 kg of contents**. Supported on the sides alone it would deflect **10 mm (18 mm long-term)**. The 1.1 m span is then carried by the Drawer back and front acting as beams. Keep the back **at least 75 mm tall** (1.1 mm under 50 kg in 12 mm stock) or make it from 18 mm stock. A centre runner from the Carcass is not needed and is not practical (see [Drawer-bottom stiffness](#drawer-bottom-stiffness-over-the-span)).
5. **The undermount route is the alternative if 26 units matters more than load.** Undermount slides leave almost no side gap, so the inside width is about opening − 42 to 44.5 mm and 26 units fit in a ~1137 mm opening. The **Accuride 3160EC** comes with a cable anti-rack, and its 4180-0753-XE stabiliser kit costs $30.97 *(snippet)*. It is rated **100 lb per pair (22" slides in a 60" drawer, 50,000 cycles)**, which covers parts Drawers but not tool Drawers. **Blum MOVENTO** with a ZS7M side stabiliser (rack-and-pinion) reaches 1400 mm, but Blum's own data gives the US 769 model **60 kg dynamic**. Both need drawer sides of 16 mm (⅝") or thinner, a notched back and template drilling, and the Timberline undermount clip DC-515.
6. **The single Timberline lockbar still works.** With ¾" slides, use the **DC-502** drawer clip, which Timberline makes for ¾" slide clearance. Timberline's own wide lateral-file system (System 300) locks **both** sides through a flexible shaft. On kagu, the synchroniser shaft does that job: the unlocked side cannot advance without the locked side **(assumption; prototype it)**. Without a synchroniser, add a second lockbar or accept some racking play on the far side.

## Comparison table

"Side space" is per side. "Max width" is the maker's recommended maximum drawer width. Loads are per pair under the stated test. Unless noted, the box widths below assume 12 mm sides and a 0.5 mm Baseplate clearance per side (interior = 42N + 1 mm; see [Sizing](#gridfinity-sizing-at-this-width)).

| Slide | Mount / side space | Height | Max width | Load / pair (test) | Lengths | Detent / disconnect | Anti-rack provision | Fits 25 u (1075 mm box)? | Fits 26 u (1117 mm box)? | Price (2026-11-08) |
|---|---|---|---|---|---|---|---|---|---|---|
| **Accuride 3657** / 3600 | side, 0.75" +0.030/−0 [19.1 +0.76/−0] | 2.09" [53.1] | 42" [1067] | **200 lb frequent / 273 lb moderate** (pair of 18" slides on a 42" drawer, 75k cycles, per the 3600 sheet); Accuride's 3657 page says "up to 275 lb" | even 12"–28" | hold-in detent; 3657 lever disconnect, 3600 non-disconnect | none | at the limit (+8 mm) | no (+50 mm) | 3600-22: **$110.99/pair** Zoro *(snippet)*; 3657: not found |
| **Accuride 7957** / 7950 | side, 0.75" [19.1] | 2.79" [70.8] | 42" | **350 lb** (pair of 18" slides on a 42" drawer, 10k cycles); 150 lb flat mount | even 12"–36" | hold-in; 7957 handed lever disconnect, 7950 non-disconnect | none | at the limit | no | 22": **$158.38/pair** (Häfele via DK Hardware) to **$199.99/pair** (Rockler) *(snippet)* |
| Accuride 9301E / 9308E | side, 0.75" [19.1] | not stated in the text I could read | 42" | 480 lb frequent at ≤42" (75k); **360 lb mobile only at ≤32"**; 600 lb moderate at ≤24" | 10"–36", 40", 42", 44", 48", 54", 60" | 9301E none, non-disconnect; 9308E lock-in/lock-out | none | at the limit | no | 9301 22": $179.99/pair (Rockler, from #4); 9308E $107.40 each (from #4) |
| Accuride 3634 | side, 0.78" [19.8] | not confirmed | 42" | 200 lb side, 75 lb flat | even 12"–28" | hold-in, lever disconnect; **1" over-travel** | none | at the limit | no | 22": $129.23–190.40/pair *(snippet)* |
| Accuride 3641 + 3642 | side, 0.89" [22.6] | 2.09" [53] | 42" | 180 lb | 14"–28", 17" | hold-in; **built-in interlock**, 1" over-travel | none | at the limit | no | $80.19 base/pair (from #5) |
| **KV 8810** | side, 0.765" +0.02/−0.01 | 2.09" [53] | 42" | 200 lb *class* (KV says pound classes "are not the same as actual load ratings") | even 10"–28" | hold-in detent, butterfly lever | none | at the limit | no | $56.39 Zoro, unclear if per slide or pair *(snippet)*; 20" pair $44.35 Ferguson *(snippet)* |
| KV 8900 | side, 0.75" +0.03/−0 | 3" [76.2] | test drawers up to 42" | **400 lb** (18" slide, 42" drawer, 30k); 300 lb (36" drawer, 75k) | 10"–36", 40"–48", 60" | non-disconnect | none | at the limit | no | 22": $210.99 Zoro, unit unclear *(snippet)* |
| **Accuride 3160EC** + 4180-0753-XE | **undermount**; inside drawer = cabinet − 1¾" [44.5]; sides ½"–⅝" | 1.05" under the drawer, 1.87" overall | **60"** | **100 lb** (22" slides in a 60" drawer, 50k cycles, with carrier strip) | even 12"–28", 15", 21" | Easy-Close; lever disconnect | **cable system included; stabiliser kit required for 41"–60"** | yes | **yes** (opening ≈ 1138) | kit **$30.97** (accuride.com) *(snippet)*; slides: not found |
| Blum MOVENTO 760H (EU) / 769 (US) + ZS7M stabiliser | **undermount**; inside = opening − 42; sides 12–16 mm | runner 28.5 mm under the drawer (from #4) | stabiliser: **cabinet width up to 1400 mm** (EU ZS7M400/600/750MU); US ZS7M686MU 610–1369 mm openings *(secondary)* | 760H: 40 or 70 kg class; 769R5330S: **60 kg dynamic** (Blum data, from #4) | 760H 350–500 mm; ZS7M686MU for slides ≤ 27" | soft-close; locking devices | **rack-and-pinion stabiliser** (shaft = LW − 315 mm, racks = NL + 10 mm) | yes | **yes** (opening ≈ 1135) | 769 21": $44.52–58.50/pair *(snippet)*; ZS7M686MU: not found |
| ½" class (3832E, 4032, KV 8400/8500/8600) | side, ½" | 45–96 mm | 24", 27", 24", 36", 36" | — | — | — | none | **no** | **no** | see #4 |

**Not found:** I found no ball-bearing **side-mount** slide from Accuride, Knape & Vogt or Hettich with a published width above 42". I also found no synchroniser kit for side-mount ball-bearing slides. Hettich's synchronising bars are for its Quadro/Actro and push-to-open systems, and its KA runners stop at 700 mm length with no wide-drawer kit. Industrial telescopic slides (for example Chambrelan or Rollon) were not surveyed.

### Notes behind the table

- **Why 42" is the ceiling.** Accuride's catalogue says "All slide products carry a maximum recommended drawer width" and "wider drawers require a slide with a higher load rating and a cross section designed to withstand lateral stress". KV says that with drawers wider than 24" "the user has more leverage which can cause racking", and recommends "slides designed for the width of the drawer". Across both catalogues, every 42" figure belongs to the ¾"-class heavy-duty slides.
- **The "drawer width ≤ slide length" rule does not apply to this class.** That rule is printed on the light 3832EC/EHDSC sheets. Accuride Europe's knowledge base gives a softer form: slide length "equal to or slightly longer than the drawer width". Yet Accuride rates the 3600, 3640A and 7950 on **18" slides under a 42" drawer**, a width-to-length ratio of 2.33. kagu with 20" slides on a 1075 mm box is **2.12**, and with 22" slides **1.92**, so it is less prone to racking than Accuride's own test geometry **(assumption: ratio as a proxy)**.
- **Load needed.** Tool contents of 30–50 kg, plus a box of about 10 kg (4.1 kg of 12 mm bottom, about 2 kg of sides, front and back, about 1.4 kg of false front, and about 2 kg of printed Baseplate Tiles **(assumption)**), give **40–60 kg (88–132 lb) in total**. The 200 lb class therefore has about 1.5× margin at the frequent-use rating. The 3160EC's 100 lb leaves only about 35 kg for contents.
- **Mobile rating.** Only the 9301E/9308E have been "vibration testing similar to conditions encountered in mobile applications" (Accuride *Slides for Mobile Applications*), and their mobile rating stops at **32"** drawers. No slide has a mobile rating at 42" or more. A lab Cabinet on casters is gentler than a vehicle **(assumption)**, and transit hold-shut comes from the lockbar (#5/#12).
- **Disconnect matters at this size.** A loaded 1.1 m Drawer is awkward to remove. Lever-disconnect slides (3657, 7957, KV 8810) are preferable to non-disconnect ones (3600, 7950, 9301E, KV 8900), and the synchroniser should be designed to unhook as well.

## Anti-racking and synchronisation

Racking happens when one side of the Drawer advances ahead of the other. Accuride Europe: "Drawers wider than they are deep put more stress on the drawer and slides", looser slides make it worse, "stiffer drawers" reduce it, and "We advise, where design restraints allow, that you use a central pull handle on wide drawers." Each option below is weighed for this shop.

| # | Option | How it works | Fit for kagu | Cost (est.) | Risk |
|---|---|---|---|---|---|
| S0 | **Centre pull + stiff box** | Pull force goes in at the middle, and a stiff box resists yaw | Free; do it regardless | $0 | Students still pull from one end |
| S1 | **DIY rack-and-pinion synchroniser** (recommended) | A gear rack on each Carcass side; a pinion at each rear corner of the Drawer, both on one steel shaft behind the Drawer back. One side cannot advance without turning the shaft, which drives the other side the same amount | Printed racks (Prusa XL, ≤ 360 mm segments) and pinions, a 10 mm steel rod, printed bearing blocks. It needs about 25–30 mm of side-gap height above or below the slide | about $10–20 per Drawer **(assumption)** | Printed tooth wear; mesh alignment; noise and dust (both named as known drawbacks in US 8,152,250's background) |
| S2 | **DIY crossed-cable anti-rack** | Two cables, each anchored to the Carcass at the rear on one side and the front on the other. Each passes over pulleys at the Drawer's rear corners, so its length stays constant only while both sides move together | Printed pulleys with 608 bearings, 1/16" stainless cable, turnbuckles | about $15–25 per Drawer **(assumption)** | Stretch needs re-tensioning. Accuride's 3160EC sheet warns: "Too much tension will cause poor movement" |
| S3 | **Commercial undermount kit** (Accuride 3160EC cable + carrier strip; Blum ZS7M rack-and-pinion) | Factory parts | Only with those undermount slides | $30.97 for the Accuride kit *(snippet)* | Undermount load limits (see table) |
| S4 | **Third (centre) slide** | A slide under the Drawer centre on a Carcass rail | Needs a Carcass cross-member under every Drawer. KV warns a side slide "may lose 75 percent or more of its load carrying capacity if mounted flat" | — | Three slides cannot be kept coplanar, so they bind. **Not recommended** |
| S5 | **Second lockbar or Timberline System 300 on both sides** | Locks both sides but does not synchronise them | Only for security, not for smooth running | Timberline parts | No effect on racking in use |

### S1 detail: DIY rack-and-pinion synchroniser

These are drawable from the Blum MOVENTO stabiliser and the Standard Precision patent; the numbers are mine **(assumption)** and need a prototype.

- **Prior art:** US 4,324,439 (Standard Precision, expired) puts "a spur gear ... on the rear of each intermediate member" engaging "a toothed rack on the stationary outer slide member", with "the two gears ... joined by a transverse shaft". Blum's ZS7M kit is the same idea, sold for MOVENTO: "Shaft cutting dimensions: Internal cabinet width (LW) – 315 mm; Gear rack cutting: NL + 10 mm", suitable "for KB 1400 mm".
- **Racks:** One per side, screwed to the Carcass side (or to a liner; see Implications) in the side gap below the slide. Length = slide length + about 10 mm (Blum's NL + 10). Print in PETG or PA-CF in ≤ 360 mm segments with a keyed joint, module **1.5–2**, 20° pressure angle, 10–12 mm face width.
- **Pinions:** 12–14 teeth (about 21–28 mm pitch diameter), with a D-bore on the shaft and a grub screw or a printed clamp.
- **Shaft:** 10 mm steel rod, about 1080 mm long, clipped behind the Drawer back in 3 printed bearing blocks.
  - **Twist check:** Pull 100 N at one extreme end, and the shaft carries about half that, 50 N at an 11 mm pitch radius, so T ≈ 550 N·mm. Twist = T·L/(G·J) = 550 × 1080 / (79,000 × 982) ≈ 0.0077 rad, which is **0.08 mm at the pitch circle**. Printed-gear backlash (about 0.1–0.3 mm) dominates, which is still only about 0.02° of Drawer yaw.
  - **Tooth stress (Lewis, Y ≈ 0.3):** module 1 at 10 mm face gives about 33 MPa, too high for PETG under repeated load. Module 2 at 12 mm face gives about 14 MPa. Hence module 1.5–2.
- **Space:** The pinion and rack need about 25–30 mm of side-gap height outside the slide, so the Drawer side must be at least slide height + about 25 mm (≈ 80 mm with the 53 mm slides). The 19.4 mm side gap takes a 10–12 mm face width.
- **Removal:** Pinions lift off the rack when the Drawer is tilted up at full extension. Alternatively, make the rear bearing blocks hinge.
- **Real examples:** I found **no printed wide-drawer synchroniser** on Printables, Thingiverse or MakerWorld. The closest is the [FuExRaPiLiRa drawer](https://www.printables.com/model/1420195-fuexrapilira-drawer), a printed full-extension rack-and-pinion telescoping drawer. Treat S1 as a prototype item.

### S2 detail: crossed-cable anti-rack

Cable A is anchored at the Carcass left-rear. It runs forward along the left side gap to a pulley at the Drawer's left-rear corner, across behind the Drawer back to a pulley at the right-rear corner, then forward along the right side gap to an anchor at the Carcass right-front. When both sides move by Δ, the left run grows by Δ and the right run shrinks by Δ, so the total is constant. If the left side leads, the cable would have to lengthen, so it resists. Cable B is the mirror image. This is the principle of Accuride's 3160EC "cable system (included)", which the sheet says is enough for drawers of 31"–40"; above 41" Accuride adds the carrier strip. For kagu at about 42", S1 is the stiffer choice **(assumption)**.

## Drawer-bottom stiffness over the span

Bins on a thin Baseplate bear on the Drawer floor (gridfinity research #6), so the floor must stay flat. A sagging Drawer also eats into the clearance (`c_top`) over the Bins in the Drawer below.

**Inputs.** Metsä Wood structural birch plywood DoP, mean values:

| Thickness | Plies | Mean bending E along the face grain (II) | Across (⊥) | In-plane E (II) | Weight |
|---|---|---|---|---|---|
| 12 mm (½") | 9 | **10,719 N/mm²** | 6,781 | 9,333 | 8.2 kg/m² (UPM WISA-Birch) |
| 18 mm (¾") | 13 | **10,048 N/mm²** | 7,452 | 9,148 | 12.2 kg/m² |

Panel shear modulus is 620 N/mm². Long-term deflection uses k_def = 0.8 (EN 1995-1-1 Table 3.2, plywood to EN 636-1 in service class 1, quoted from memory, not re-fetched), so long-term = 1.8 × instantaneous.

The geometry is a box of 1075 mm × about 508 mm, with a floor of about 1052 × 480 mm (0.505 m²). Loads are uniform: **20 kg of contents (0.39 kPa)** for a parts Drawer and **50 kg (0.97 kPa)** for a tool Drawer. Each case is modelled as a simply supported one-way strip, δ = 5qL⁴/384EI. Real edges are partly fixed and real loads are lumpier, so treat the results as ±50 % **(assumption)**.

**Bottom panel (mm, instantaneous / long-term):**

| Bottom supported on | Span | ½" (12 mm), 20 kg | ½", 50 kg | ¾" (18 mm), 20 kg | ¾", 50 kg |
|---|---|---|---|---|---|
| **Sides only** (in side grooves, front and back not carrying it) | 1052 mm, face grain across the span | 4.0 / 7.2 | **10.0 / 18.1** | 1.3 / 2.3 | 3.2 / 5.7 |
| Sides only, face grain the wrong way | 1052 mm | 6.4 / 11.4 | 15.9 / 28.6 | 1.7 / 3.1 | 4.3 / 7.7 |
| Sides + a centre support (rib or runner) | 2 × 526 mm (conservative) | 0.25 / 0.45 | 0.63 / 1.1 | 0.08 / 0.14 | 0.20 / 0.36 |
| **All four edges** (captured in the front and back too), short span governs | 480 mm, face grain front-to-back | 0.17 / 0.31 | **0.43 / 0.78** | 0.05 / 0.10 | 0.14 / 0.25 |

**Drawer back as a beam over 1075 mm** (carrying half the floor load; the front, with its false front, is stiffer). These are bending plus shear deflections, in mm, instantaneous / long-term. They are conservative because they ignore a glued bottom acting as a flange.

| Back height | 12 mm back, 20 kg | 12 mm back, 50 kg | 18 mm back, 20 kg | 18 mm back, 50 kg |
|---|---|---|---|---|
| 55 mm | 1.1 / 2.0 | 2.7 / 4.9 | 0.7 / 1.3 | 1.9 / 3.3 |
| **75 mm** | 0.4 / 0.8 | **1.1 / 2.0** | 0.3 / 0.5 | 0.8 / 1.4 |
| 100 mm | 0.2 / 0.4 | 0.5 / 0.9 | 0.1 / 0.2 | 0.3 / 0.6 |
| 150 mm | 0.07 / 0.12 | 0.17 / 0.30 | 0.04 / 0.08 | 0.11 / 0.20 |

**Reading the numbers:**

- **The span direction matters far more than ½" vs ¾".** If the bottom hangs only from the sides, even ¾" sags 3–6 mm under tools. If it is captured on all four edges, ½" is under 1 mm. So: **½" (12 mm) bottom, face grain front-to-back, in a groove on all four sides, glued to the front and back.** This keeps the Drawer lighter, which matters against the slide rating.
- **A "centre runner" is a stand-in for front/back support.** A front-to-back rib under the middle of the floor, glued to the front and back, halves the side-to-side span and loads the front and back panels. That is the same structure as all-four-edge capture, and is only needed if the bottom cannot be captured in the front and back. A centre runner that bears on the Carcass (S4) is not recommended.
- **The back panel is the weak link in shallow Drawers.** Keep it **≥ 75 mm tall in 12 mm stock** for tool Drawers, or use 18 mm, or let a glued bottom act as an L-beam flange.
- **Clearance.** Allow **c_top ≥ 5 mm** for this column, not the 3 mm suggested in #6. This covers about 2 mm of long-term sag of a loaded Drawer above an empty one, plus slide sag at extension, which Accuride and KV do not publish **(assumption)**.

## Minimum Drawer height, and fit with a single Timberline lockbar

| Constraint | Value | Source |
|---|---|---|
| Slide height on the Drawer side | 53.1 mm (3600/3657, 3641, KV 8810 at 53 mm); 70.8 mm (7950/7957); 76.2 mm (KV 8900) | Accuride, KV |
| Synchroniser rack and pinion (S1) beside the slide | + about 25–30 mm | **(assumption)** |
| Back panel stiffness (tool Drawer, 12 mm stock) | ≥ 75 mm | table above |
| Timberline DC-502 clip (¾" slide clearance) | 19/32" × 1¼" × 21/32", on the Drawer side | Timberline catalogue p. 12 |
| Timberline throw | ½" lockbar throw | Timberline catalogue |

- **Minimum Drawer box height: about 80 mm** with 53 mm slides and S1, or about 75 mm without S1 (back stiffness governs). With the 7957 it is about 100 mm. Bay pitch = box height + vertical running clearance (about 6–10 mm, **assumption**), so the shallowest Bay is about **90 mm**. Bins may stand taller than the Drawer sides, up to the Drawer above minus `c_top` (gridfinity research #6).
- **Interlock and lock:**
  - **Clip:** with ¾" slides, the Timberline clip changes from DC-500 to **DC-502**. With undermount slides it is **DC-515**.
  - **Anti-tip wedges:** I could not confirm that the WD-21A/B wedges (Systems 300/350) are made for a ¾" gap. The catalogue states "1/2" drawer slide clearance required" only for System 400. Check before ordering.
  - **Lockbar:** the 24" LB-240 or 48" LB-480 is cut to the column height. Custom lockbars run 11"–60".
- **One side versus two:** Timberline's own wide lateral-file System 300 "locks wide drawers on both sides" through an FS-362 flexible shaft "(typically X" − 5/8")". kagu's plan is a single lockbar on one side, and S1's shaft makes it hold the far side as well **(assumption)**. If S1 is dropped, either mirror the lockbar on the other side (a second groove plus a flexible shaft) or accept that the far end can rack forward by the slide play before binding (amount not quantified).
- **Locked Drawer / Viewing Lid:** if a Locked Drawer sits in this column, the **Accuride 3634** (1" over-travel, 200 lb at 42") gives the lid hinge clearance that #5 flagged. Its side space is **0.78" (19.8 mm)**, so the gap stays one per-slide parameter.

## Gridfinity sizing at this width

Interior = 42N + 2c with c = 0.5 mm (#6). Box outer = interior + 2 × side thickness. With ¾"-class side-mount slides, Bay = box + 2 × 19.4 mm. With undermount, the opening is set by the maker's deduction.

| Units wide N | Interior | Box, 12 mm sides | Box, 18 mm sides | Within 42" (1067)? | Bay, side-mount ¾" | Opening, 3160EC (−44.5) | Opening, MOVENTO (−42) |
|---|---|---|---|---|---|---|---|
| 24 | 1009 | 1033 (40.7") | 1045 (41.1") | yes | 1072 | 1054 | 1051 |
| **25** | 1051 | **1075 (42.3")** | 1087 (42.8") | at the limit (+8 mm) | **1114** | 1096 | 1093 |
| 26 | 1093 | 1117 (44.0") | 1129 (44.4") | no (+50 mm) | 1156 | **1138** | **1135** |

A 1200 mm Carcass with 18 mm sides has about 1164 mm inside. Two instrument sets side by side need 1118 mm plus clearance (#17).

## Implications for kagu

- **This overturns #4's slide pick for the Drawer column.** #4 picked ½" slides (Accuride 3832E/4032, 13.0 mm gap), but they top out at 24–27" and cannot carry a 1.1 m Drawer. The Drawer column needs **¾"-class, 42"-rated slides with a 19.4 mm side gap**. Keep side space as a per-Bay parameter, as #4 already recommended.
- **Drawer width parameter (#11):** pick 24, 25 or 26 units.
  - **25 (recommended):** 1075 mm box, Bay 1114 mm.
  - **24:** strictly inside the published rating.
  - **26:** only via undermount (lower load) or by running side-mount slides about 5 % past their published width, which needs a loaded prototype test.
- **Carcass (#10, #11):** with 25 units, the Drawer Bay (1114) is narrower than the Carcass interior (about 1140–1164, set by the instruments). The difference of about 13–25 mm per side goes into **liners** on the Carcass sides in the Drawer column. The liners carry the slides, the S1 racks and the routed Timberline groove. That keeps the router work off the main Carcass sides and lets the Bay be trued to the ±0.76 mm side-space tolerance with shims **(assumption)**.
- **Slide length:** 20" (508 mm) gives an interior depth of about 484 mm with 12 mm front and back, or **11 units** (462 + 22 mm spare). 22" (559 mm) gives about 535 mm, or **12 units**. The choice depends on the Bay depth from #3 (≥ 430 mm, about 530 mm with cables) and on the Carcass depth.
- **Drawer box construction (map "Not yet specified"):**
  - 12 mm bottom, face grain front-to-back, in a groove on all four edges, glued to the front and back.
  - Back at least 75 mm tall (or 18 mm stock), and box height about 80 mm or more.
  - **c_top ≥ 5 mm** in this column.
  - Lever-disconnect slides so a loaded Drawer can be removed.
- **Handles (map "Not yet specified"):** use a **centre pull**, or a full-width bar, on every Drawer in this column (Accuride's advice).
- **Lock and interlock (#12):** DC-502 clips. One lockbar is enough if S1 synchronises; otherwise lock both sides as Timberline does in System 300. Check that the WD-21 wedges work at a ¾" gap.
- **Locked Drawer (#13):** if one is in this column, the Accuride 3634 (1" over-travel) is the only 42" slide surveyed with over-travel besides the 3641.
- **Cost per Drawer:** about $111 (3600) to $200 (7957) for slides, plus about $10–25 for S1 or S2. A distributor quote is still needed for the 3657 and for KV 8810 pair pricing.
- **Suggested prototype ticket:** one full-width test Drawer (25 units, 12 mm box, 3657 or 8810 slides, S1 synchroniser). Load it to 50 kg, then measure sag, racking at an end pull, and force to open. Repeat without S1 and with a one-side lock.

## Open questions surfaced

1. **24, 25 or 26 units wide?** (#11) Is 8 mm over the 42" rating acceptable (25), or must it be strictly in-spec (24)? Is 26 units worth either the undermount load cap or a 5 % out-of-spec side-mount with a test?
2. **Is the 200 lb class (3657 / KV 8810) enough, or should tool Drawers get the 7957?** This depends on how heavy the hand-tool Drawers really are. Weigh a representative set of hammers, mallets, saws and clamps in Bins.
3. **S1 (rack-and-pinion) or S2 (cable)?** Either needs a prototype. Does the synchroniser make one lockbar enough (#12)?
4. **Do Timberline WD-21A/B wedges and the System 300/350 parts work with ¾" side clearance?** Ask CompX, or get the application drawings at compx.com/instructions.html.
5. **Unconfirmed prices:** Accuride 3657, 3160EC slides and Blum ZS7M686MU were not found. KV 8810 and 8900 prices are unclear between per slide and per pair.
6. **Slide sag at full extension** is not published by Accuride or KV for these models. Measure it on the prototype, since it feeds `c_top`.

## Sources

All accessed 2026-11-08.

**Accuride**
- Accuride, product catalogue (© 2018), "Specifications at a glance" (maximum drawer widths for every model), 3160EC, 3634, 3641/3640A, 3600 series, 7950/7957, 9301E/9307E/9308E (pp. 8–9, 14, 20–24): https://res.cloudinary.com/amerhart/image/upload/Documents/Product/Accuride_4180_0266_XE_CAT.pdf
- Accuride, *Enhanced 9300 Slide Family* brochure, R1-0417 (2017): https://res.cloudinary.com/amerhart/image/upload/Documents/Product/Accuride_C9301_E10P_BRO.pdf
- Accuride, *Heavy-Duty Slide Options* (3600, 7950/7957, 9300E), distributor-hosted: https://info.heilind.com/hubfs/DB%20Roberts/DBR%20Email/Heavy%20Duty%20Slide%20Options_2.pdf
- Accuride, *Model 3600 technical sheet* (273/200 lb, 0.75" +0.030/−0, test basis), distributor-hosted: https://ahturf.com/content/3600%20Technical%20Sheet.pdf
- Accuride, *Model 3160EC Easy-Close* quick reference and installation, doc. 3700-9565-MK983-N-0217 (2017), Richelieu-hosted: https://static.richelieu.com/documents/docsGr/119/891/0/1198910/1408776.pdf
- Accuride, 4180-0753-XE Wide Drawer Stabilizer Kit page (price via search snippet): https://www.accuride.com/en-us/products/accessories/4180-wide-drawer-stabilizer-kit
- Accuride, 3657 product page ("up to 275 lbs", via search snippet): https://www.accuride.com/en-us/products/drawer-slides/3657-heavy-duty-slide-with-lever-disconnect
- Accuride Europe knowledge base, *Potential problems of using slides on wide and deep drawers, and ball migration and inching issues*: https://help.accuride-europe.com/knowledge/potential-problems-of-using-slides-on-wide-and-deep-drawers-and-ball-migration-and-inching-issues
- Accuride, *Slides for Mobile Applications*, SS-Mobile-Applications-0821 (2021): https://info.heilind.com/hubfs/Slides%20for%20Mobile%20Applications_2.pdf

**Knape & Vogt**
- Knape & Vogt, *Hardware Guide* (© 2026): "How to Choose a Drawer Slide" (p. 3), 8500, 8810, 8900, 8908 and the 900 Series undermount: https://www.knapeandvogt.com/sites/default/files/Hardware-Guide.pdf

**Blum**
- Blum, *MOVENTO* brochure (side stabiliser set ZS7M400/600/750MU, "For KB 1400 mm", "Shaft cutting dimensions: Internal cabinet width (LW) – 315 mm", "Gear rack cutting: NL + 10 mm", SKW = LW − 42, side thickness 12–16 mm, 40/70 kg classes): https://d2.blum.com/services/BEC003/me17392873_ep_dok_bau_$sen_$aof_$v2.pdf
- Blum, online catalogue page, MOVENTO side stabilisation set: https://publications.blum.com/2022/catalogue/en/420/
- ZS7M686MU (US kit) opening range 610–1369 mm and the ≤ 27" slide limit, *secondary* (retailer and manual mirror, not fetched directly): https://www.cabinetparts.com/p/blum-drawer-slides-undermount-drawer-slides-BSZS7M686MU-p9414, https://wurthlac.com/product/120318/Movento-Lateral-Stabilizer-Set-for-763-769
- Blum MOVENTO 769R5330S data sheet (60 kg dynamic), via #4: https://xcart.wurthlac.com/skin/common_files/files/specs/B769R5330S_SpecSheet.pdf

**CompX Timberline**
- CompX Timberline catalogue (DC-500/502/510/515 clips p. 12, custom lockbars, Systems 300/350/400 pp. 14–18): https://easykeys.com/PDFS/Timberline_Catalog.pdf

**Plywood properties**
- Metsä Wood, *Declaration of Performance* MW/PW/411-002/CPR/DOP, structural birch plywood (MUF): mean bending and in-plane moduli, shear modulus, density 680 kg/m³: https://www.metsagroup.com/globalassets/metsa-wood/dop-documents/dop_metsa_wood_birch_plywood_muf_2019-12-2_en.pdf
- UPM, *WISA-Birch Premium* technical fact sheet (plies, thickness tolerances, kg/m²): https://www.specifiedby.com/upm/wisa-birch/UPM_UPM_WISA-Birch-Premium_Technical_Fact-Sheet.pdf

**Patents and examples**
- US 4,324,439, *Anti-rack system for wide drawers and the like* (Standard Precision, 1982, expired): https://patents.google.com/patent/US4324439
- US 8,152,250, *Synchronizing/stabilizing system ... for drawer applications* (background on rack-and-pinion drawbacks): https://patents.google.com/patent/US8152250
- FuExRaPiLiRa printed rack-and-pinion drawer (Printables): https://www.printables.com/model/1420195-fuexrapilira-drawer

**Retail prices (all *snippet* unless noted)**
- Zoro, Accuride C 3600-22D: https://zoro.com/accuride-drawer-slide-side-mount-full-soft-close-pk2-34w-c-3600-22d/i/G1687576
- DK Hardware, Häfele 432.48.956 (Accuride 7950/7957): https://www.dkhardware.com/hafele-43248956-accuride-7950-7957-heavy-duty-side-bottom-mounted-slide-full-extension-150-350-lbs-weight-capacity-product-6604391.html
- Rockler, Accuride 7957: https://rockler.com/accuride-7957-heavy-duty-350-lb-full-extension-drawer-slides-with-lever-disconnect
- DK Hardware, Accuride 3634 22" (T36342G22): https://www.dkhardware.com/accuride-t36342g22-3634-over-travel-ball-bearing-slide-90-kg-200-lb-capacity-product-9106947.html
- DK Hardware, Häfele 422.05.026 (Accuride 3634, 5-pair pack): https://www.dkhardware.com/hafele-42205026-accuride-3634-heavy-duty-side-bottom-mounted-slide-1-overtravel-200-lbs-weight-capacity-23-22-p-product-6604072.html
- Zoro, KV 8810B22: https://www.zoro.com/knape-vogt-22-in-side-mount-heavy-duty-drawer-slides-kv8810b22/i/G408642939/
- Ferguson, KV 8810B 20: https://www.fergusonhome.com/knape-and-vogt-8810b-20/s1804833
- Zoro, KV 8900 B22: https://www.zoro.com/knape-vogt-kv8900-b22-22-in-extra-heavy-duty-500-lb-full-extension-slide-anochrome-kv8900-b22/i/G204084544/
- Ferguson, Blum 769.5330S: https://www.fergusonhome.com/blum-769-5330s/s1626180
