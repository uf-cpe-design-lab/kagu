# Drawer slide options

Research for [#4](https://github.com/uf-cpe-design-lab/kagu/issues/4), part of the wayfinder map [#1](https://github.com/uf-cpe-design-lab/kagu/issues/1).

**Question:** Which drawer slides suit plywood gridfinity Drawers in a mobile Cabinet? Options are full-extension ball-bearing side-mount slides (Accuride, Knape & Vogt, generic), heavy-duty slides and undermount slides. For each: load rating per pair, lengths (about 450–600 mm), side clearance, slide height and minimum drawer height, lock-in/lock-out or detent for a rolling Cabinet, soft-close, whether an interlock kit exists for the line, price per pair, and US availability.

**Sources:** manufacturer technical sheets, catalogues and product pages (Accuride, Knape & Vogt, Blum, Hettich), listed under [Sources](#sources). Some Accuride sheets are copies hosted by distributors because accuride.com blocks automated downloads. Each copy carries Accuride's own document number and date. Prices were checked on **2026-11-08**. Prices marked *(snippet)* come from a search-engine snapshot of the retailer page, not a live page load, so confirm them before ordering. Anything that is my inference or a design assumption, not a manufacturer figure, is labelled **(assumption)**.

## Recommendation

1. **Use side-mount, full-extension, ball-bearing slides that need ½" (12.7 mm) side space, in every Bay.** Then the Carcass model has one side-gap parameter. Set it to **13.0 mm per side**. That value fits all three tolerance bands: Accuride 3832E/4032 (12.7 +0.8/−0 mm), KV 8400 (12.7 +0.8/−0 mm) and KV 8600 (0.51" +0.01/−0, i.e. 12.95–13.2 mm).
2. **Light and medium Drawers (electronic parts, fasteners): Accuride 3832E, 22" (559 mm).** Rated 100 lb (45 kg) per pair. The slide is 45.7 mm tall and has a hold-in detent. It costs $29.99 per pair at Rockler. The KV 8400 has the same envelope (45.5 mm × 12.7 mm, 100 lb) and is cheaper (about $17 per pair), but Knape & Vogt does not list a hold-in detent for it. That matters on a rolling Cabinet.
3. **Heavy Drawers (hammers, mallets, saws, clamps): Accuride 4032, 22".** It takes the same ½" side space and carries **150 lb (68 kg)** per pair, tested at 75,000 cycles, with a detent-in. Its drawer rail is **96.3 mm tall**, so it only suits Drawers about 100 mm tall or more **(assumption)**. Tool Drawers will be that tall anyway. If a heavy Drawer must be shallow, use the **KV 8600**: 150 lb class (200 lb at 25,000 cycles), 50.4 mm tall, 0.51" clearance, about $29 per pair. Its sheet does not list a hold-in detent.
4. **Do not buy per-slide lock-in slides for every Drawer.** In transit, the whole-cabinet lock from [#5](https://github.com/uf-cpe-design-lab/kagu/issues/5)/[#12](https://github.com/uf-cpe-design-lab/kagu/issues/12) holds Drawers shut, and the hold-in detent covers the rest of the time. Accuride itself says that slides without locking features "may require an added locking device" in vehicles. Accuride's only ½" side-space lock-in/lock-out slide is the **3308** (150 lb, 50.8 mm tall, $105.82 per pair). Its front latch has to reach through a cut-out in the drawer front, so it is a poor fit for many Drawers that students open all day.
5. **Rule out undermount (Blum MOVENTO) and the ¾" side-space heavy locking slides (Accuride 9308E, KV 8908, Accuride 3608)** for general Drawers. Undermount slides need drawer sides of 16 mm (⅝") or thinner, a notched and template-bored drawer back, and an exact inside width of opening − 42 mm. None of them has lock-in or an interlock. The ¾" locking slides are rated 275–600 lb, cost $96–107 *each*, and are 76 mm tall. They make sense only for an instrument tray, if that Bay ever gets a slide-out shelf.
6. **Interlock:** of the slides surveyed, only the **Accuride 3641** has a built-in interlock, and it needs **0.89" (22.6 mm)** side space. Choosing it would change the side-gap parameter for every Bay in the interlocked column. That decision belongs to [#12](https://github.com/uf-cpe-design-lab/kagu/issues/12). The other lines have no slide-specific interlock kit (see the table).

## Comparison table

"Side space" is per side. "Height" is the vertical size of the slide on the drawer side. Loads are per pair under the maker's stated test. Lengths are nominal.

| Slide | Load / pair | Side space | Height | Lengths | Extension | Detent / lock | Soft- or self-close | Interlock kit | Price (checked 2026-11-08) |
|---|---|---|---|---|---|---|---|---|---|
| **Accuride 3832E** (Classic) | 100 lb [45 kg] (18" slide, 16" drawer, 50k cycles, per the 3832EC sheet) | 0.50" +0.031/−0 [12.7 +0.8/−0 mm] | 1.80" [45.7 mm] | even 6"–28" [148–700 mm] | full | **hold-in detent** | none (EC, ESC, EHDSC variants have it) | none | **$29.99** (22"), $26.99 (18"), $29.99 (24") at Rockler |
| Accuride 3832EC (Easy-Close) | 100 lb | same | 45.7 mm; min. drawer height 1⅞" [47.6 mm] | 14"–28" | full | soft-close holds the drawer shut | soft-close | none | $35.33 (22") *(snippet)* |
| Accuride 3832EHDSC (HD self-close) | 100 lb (18" slide, 24" drawer) | same | 45.7 mm | 12"–28" | full | **strong self-close: detent 6–9 lb per slide**; Accuride quotes 17–19 lb to open, for vehicles | self-close (not damped) | none | not found |
| Accuride 3832EDO | 100 lb | same | 45.7 mm | 10"–28" | full | **detent-out** (holds the drawer open) | none | none | not found |
| **Accuride 4032** | **150 lb [68 kg]** (18" slide, 75k cycles) | 0.50" +0.03/−0 | 3.19" slide, **3.79" [96.3 mm] with rail** | 12"–28" [300–700 mm] | full (rail lift-off disconnect) | **detent-in**, positive stop | none | none | not found |
| Accuride 3308 | 150 lb (12") down to 120 lb (28"); 135 lb at 24" | 0.50" +0.015/−0 | 2.00" [50.8 mm] | 12"–28" | full + 1" | **lock-in and lock-out** (front latch, released through a drawer-front cut-out) | none | none | **$105.82** per pair on accuride.com *(snippet)* |
| Accuride 3641 | 180 lb [82 kg] | **0.89" [22.6 mm]** | 2.09" [53 mm] | 14"–28" and 17" | full + 1" | hold-in detent | none | **yes, built in**: front-mounted interlock, cut-to-length aluminium rods, optional gang lock P/N 4180-0345-XE | not found |
| Accuride 9308E (+ 9301E companion) | 360 lb mobile; 600 lb static | 0.75" [19.1 mm] | not stated in catalogue text | even 12"–36", 40", 42", 48", 54", 60" | full, non-disconnect | **lock-in and lock-out**, front latch; EZ-Release cross-handle kit | none | none | **$107.40 each** (9308E); $174.70 for the 9308-E5 pair (one 9308E + one 9301E) *(snippet)*; 9301 alone $179.99 per pair (22") at Rockler |
| Accuride 3608 | 275 lb (stationary) | 0.75" | not stated | not stated | full, non-disconnect | lock-in and lock-out | none | none | $96.44 each (accuride.com) |
| **KV 8400** | 100 lb class (max. drawer 24") | 0.50" +0.03/−0 | 1.79" [45.5 mm] | even 8"–28" | full | **no hold-in listed** | none (8450FM soft-close and 8400RV self-close "for mobile applications" are separate models, same envelope) | none | $17.34 (8400P 22) at Build.com *(snippet)* |
| **KV 8600** | **150 lb class at 50k cycles; 200 lb at 25k** (18" slide) | 0.51" +0.01/−0 | 1.98" [50.4 mm] | even 12"–28" | full | no hold-in listed | none (8650FM is the soft-close version) | none | $28.64 (8600B 22) at Ferguson *(snippet)* |
| KV 8500 | 150 lb class (max. drawer 36") | 0.50" +0.03/−0 | 3.79" [96.3 mm] with rail | 12"–30" | full | **hold-in** | none | none found in the 2026 KV guide | not found |
| KV 8810 | 200 lb class | 0.765" [19.4 mm] | 2.09" [53 mm] | 10"–28" | full | **hold-in detent** | none (8850FM soft-close) | none | not found |
| KV 8908 | 300 lb vehicular; 400 normal; 500 modest | 0.75" [19 mm] | 3" [76.2 mm] | 12"–60" | full, non-disconnect | **automatic lock-in and lock-out**, removable handle | none | none | $172.51 **each** (42") at Würth LAC *(snippet)*; 22" not found |
| Hettich KA 5632 | 100 lb [45 kg] (EN 15338 level 1) | 12.7 mm | 46 mm | 250–700 mm (50 mm steps) | full | "roll-out prevention"; no detent force published | SC (self-close) and Silent System (soft) variants, 90 lb | none for KA; Hettich's Stop Control central lock/anti-tilt is listed for its own drawer systems and "wooden drawers" | no US listing found; about €23 per pair (550 mm) in Germany *(snippet)* |
| Blum MOVENTO 769 (undermount) | **60 kg dynamic** (Blum data for 769R5330S, 533 mm); retailers say 170 lb | n/a. Drawer inside width = opening − 42 mm; sides ≤ 16 mm | bearing height 28.5 mm; bottom recess 13 mm, bottom clearance 16 mm | 457, 533, 610, 686 mm and more | full | none (soft-close pulls shut) | BLUMOTION soft-close | none | about $56.55 per pair (21") + locking devices about $5.26 per pair *(snippet)* |
| Generic 100 lb, 22" (e.g. Home Depot store brands) | "100 lb" (no test conditions given) | usually ½" **(assumption)** | not stated | 10"–28" | full | rarely documented | some soft-close | none | about $13 per pair in a 10-pair box ($129.54) *(snippet)* |

### Notes behind the table

- **Drawer width limits.** Accuride's 3832EC and 3832EHDSC sheets say "drawer width should not exceed slide length". Accuride's catalogue lists the 3832E Classic for drawers "up to 24" [610 mm]". The 3832 family summary page says 16" "(varies by model)". KV 8400: 24" maximum. Accuride 4032: 27". KV 8600: 36". KV 8500: 36". This matters for gridfinity widths (see below).
- **Accuride's fit rule.** "For optimal performance, construct drawer 1-1/16" [27.0 mm] less than cabinet opening." Also: "Slides may not function properly if side space is less than .50" [12.7 mm]" (3832EC and 3832EHDSC sheets).
- **Load rating changes with length.** The 3308 table falls from 150 lb at 12" to 135 lb at 24" and 120 lb at 28". The other sheets state one figure for a reference length, usually an 18" slide.
- **Accuride's mobile note.** Only the 9308E and 9301E "have undergone vibration testing similar to conditions encountered in mobile applications". For other slides, "When using slides without locking features, the application may require an added locking device to prevent drawers from opening due to excessive forces encountered when vehicles are in motion" (Accuride, *Slides for Mobile Applications*, 2021). A lab Cabinet rolled across a floor is far gentler than a vehicle **(assumption)**, but the advice still applies.
- **The CB-Hand kit** adds lock-in (front unit) or lock-in and lock-out (rear unit) to slides with cross-sections of 0.75" or more, such as the 3640A, 7950, 7957 and 9301. It does **not** fit ½" slides (Accuride 2018 catalogue, p. 44).
- **KV hold-in.** In the 2026 Knape & Vogt guide, the 6500, 8500, 8520 and 8810 list "hold-in detent" or "hold-in feature" as features. The 8400 and 8600 do not, so I treat them as having no specified hold-in. Check a sample before choosing them for a rolling Cabinet.
- **Blum MOVENTO** needs drawer sides of 16 mm (⅝"), a 13 mm bottom recess, rear notches, boring with the T65.1600.01 template, and front locking devices (T51.7601). The minimum internal cabinet depth for the 533 mm runner is 590 mm. Retailers quote 170 lb, Würth quotes 135 lb for the 769R, and Blum's own product data says 60 kg dynamic. Blum's figure should govern.
- **Hettich KA** runners need a carcase interior depth of at least nominal length + 4 mm (for example 554 mm for the 550 mm runner). Hettich's US arm sells them, but no US retail price turned up, so supply would be through a distributor such as Würth.

## Implications for kagu

### Side clearance per Drawer

- Use **13.0 mm per side, 26.0 mm in total**, for every ½"-class slide above **(assumption: a single mid-band value)**. Accuride's own rule (opening − 27.0 mm, i.e. 13.5 mm per side) sits at the top edge of the Accuride and KV 8400 bands, but not inside the KV 8600's 12.95–13.2 mm band. 13.0 mm fits all of them.
- **Build tolerance.** The usable band is only 0.25–0.8 mm per side. Bay openings must therefore come out square and parallel. That is a constraint on [#10](https://github.com/uf-cpe-design-lab/kagu/issues/10) (Carcass joinery). Two cheap fixes exist **(assumption)**: shim the cabinet member with a 3D-printed or hardboard spacer, or size the drawer box last, to the measured opening.
- If a column gets the Accuride 3641 interlock, its side space becomes **22.6 mm per side**. If a ¾" locking slide is ever used, it becomes **19.1 mm**. Keep side space as a per-Bay parameter, not a global constant.

### Gridfinity widths and the drawer-width limit

The interior width needed for *N* gridfinity units is 42·*N* mm plus about 1 mm of play **(assumption; exact baseplate tolerances are [#6](https://github.com/uf-cpe-design-lab/kagu/issues/6))**. Drawer box sides add 2·*t*. Bay opening = box + 26.0 mm.

| Units wide | Box outer, ½" sides | Box outer, ¾" sides | Bay opening (½" sides) | Within 24" (3832E Classic, KV 8400)? |
|---|---|---|---|---|
| 10 | 446 mm (17.6") | 459 mm | 472 mm | yes |
| 11 | 488 mm (19.2") | 501 mm | 514 mm | yes |
| 12 | 530 mm (20.9") | 543 mm | 556 mm | yes |
| 13 | 572 mm (22.5") | 585 mm (23.0") | 598 mm | yes, but wider than a 22" slide, so it breaks the 3832EC/EHDSC "width ≤ slide length" rule unless 24" slides are used |
| 14 | 614 mm (24.2") | 627 mm | 640 mm | **no**. Needs an Accuride 4032 (27") or KV 8600 (36") |

Drawers of up to **12 units wide** work with every ½" option. Going wider than 13 units forces the heavier slide line in that Bay.

### Slide length and gridfinity depth

Assume the drawer box is as long as the slide **(assumption; this is the usual full-extension practice. Accuride gives the drawer-member setback but no drawer-length rule)**. Interior depth = slide length − 2·*t*.

| Slide | Interior, ½" box | Gridfinity units deep (spare) | Interior, ¾" box | Units deep (spare) |
|---|---|---|---|---|
| 18" (457 mm) | 432 mm | 10 (12 mm) | 419 mm | **9** (41 mm). 10 units misses by 0.9 mm |
| 20" (508 mm) | 483 mm | 11 (21 mm) | 470 mm | 11 (8 mm) |
| **22" (559 mm)** | 533 mm | **12 (29 mm)** | 521 mm | 12 (17 mm) |
| 24" (610 mm) | 584 mm | **13 (38 mm)** | 572 mm | 13 (26 mm) |
| 550 mm (Hettich) | 525 mm | 12 (21 mm) | 512 mm | 12 (8 mm) |
| 600 mm (Hettich) | 575 mm | 13 (29 mm) | 562 mm | 13 (16 mm) |

- **22" gives 12 units deep** with ½" box material, and leaves room for a printed handle pocket or a label strip. 24" gives 13 units.
- **Carcass depth.** The Carcass interior has to be at least slide length (Hettich: + 4 mm), plus the back panel. The Rigol DP832A's 429.5 mm depth ([#3](https://github.com/uf-cpe-design-lab/kagu/issues/3) research) is already shallower than an 18" slide, so drawer depth, not the instrument Bay, sets the Cabinet depth.
- **Full extension.** These slides travel their full length, so a 22" Drawer exposes all 12 rows. Over-travel (3308, 3641) is not needed. There is no front face frame to clear.

### Minimum Drawer box height

| Slide | Slide height | Minimum drawer side height |
|---|---|---|
| Accuride 3832E/EC/EHDSC | 45.7 mm | **47.6 mm (1⅞")**, as published for the 3832EC |
| KV 8400 | 45.5 mm | about 47–48 mm **(assumption, same as the 3832)** |
| Hettich KA 5632 | 46 mm | about 48 mm **(assumption)** |
| KV 8600 | 50.4 mm | about 52 mm **(assumption)** |
| Accuride 3308 | 50.8 mm | about 52 mm **(assumption)** |
| KV 8908 | 76.2 mm | about 78 mm **(assumption)** |
| Accuride 4032 / KV 8500 | 96.3 mm with rail | about 100 mm **(assumption)** |

- A 47.6 mm drawer side holds a baseplate plus a few 7 mm height units of bins. The exact count depends on baseplate thickness, drawer-bottom thickness and groove position, and the stacking lip. That arithmetic waits on [#6](https://github.com/uf-cpe-design-lab/kagu/issues/6) (gridfinity spec) and the drawer-box construction note on the map. The shallowest practical Drawer is set by the bins, not by the slide.
- **Drawer pitch (assumption).** Each Drawer occupies its box height plus a vertical gap. Blum asks for 7 mm of top clearance. Side-mount slides only need running clearance. The drawer front then overlaps that gap. Bay heights in [#11](https://github.com/uf-cpe-design-lab/kagu/issues/11) should be built up from box height + gap. Do not start from front height.

### Lock-in and lock-out on a rolling Cabinet

- **Lock-in** (Drawers stay shut while the Cabinet moves). Use a hold-in detent slide (3832E, 4032) **plus** the whole-cabinet lock from [#12](https://github.com/uf-cpe-design-lab/kagu/issues/12), engaged before moving. If the lock is ever left off, the **3832EHDSC** is the low-cost hedge: same envelope, 6–9 lb of detent per slide, 17–19 lb to open. The cost is a stiffer pull on every opening. Use it for the top Drawers, where a roll-out would do the most harm, rather than everywhere **(assumption)**.
- **Lock-out** (a Drawer held open). It is not needed for normal use. If a Drawer must stay open on a sloping floor, the **3832EDO** (detent-out, same envelope) is the cheap choice. True positive lock-out slides are 0.75" side space (9307E, 9308E, 3608, KV 8908), or the 3308 at ½".
- **Tip-over.** A ~915 mm Cabinet with several full-extension 150 lb Drawers open at once can tip, even with locking casters ([#7](https://github.com/uf-cpe-design-lab/kagu/issues/7)). That is why [#5](https://github.com/uf-cpe-design-lab/kagu/issues/5)/[#12](https://github.com/uf-cpe-design-lab/kagu/issues/12) need an interlock. The interlock must work with ½"-side-space slides, so it has to be built or bought separately from the slides. The alternative is to accept the 3641's 22.6 mm side space in the interlocked column.

## Open questions surfaced

- **Interlock vs side space:** use the Accuride 3641 (built-in interlock, 22.6 mm side space) or a separate interlock with ½" slides? This is for [#12](https://github.com/uf-cpe-design-lab/kagu/issues/12).
- **Gridfinity width cap:** is 12 units the widest Drawer, so that every ½" slide fits, or does any Bay go to 13–14 units and need the 4032/8600? This is for [#11](https://github.com/uf-cpe-design-lab/kagu/issues/11).
- **Drawer box material thickness** (½" or ¾"). It changes how many units fit deep and wide. This belongs to the drawer-box construction topic on the map's "Not yet specified" list.
- **Hold-in on the KV 8400/8600** is not documented. Test a sample, or use Accuride for every Drawer.
- **Unconfirmed prices:** 3832EHDSC, 4032 and 3641 prices were not found. Get a distributor quote for about 4 Cabinets' worth (the lab has 4 instrument sets).

## Sources

All accessed 2026-11-08.

**Accuride**
- Accuride, *3832EC Technical Sheet*, doc. 3700-9508(1183)-MK114-R7-0523 (2023), distributor-hosted: https://d1ffabcce73sv0.cloudfront.net/113/55/documents/ac_tech+sheet_3832ec_next-gen_v5_0523+2+2.pdf
- Accuride, *3832EHDSC Technical Sheet*: https://ahturf.com/content/3832EHDSC%20Technical%20Sheet.pdf
- Accuride Europe, *3832 telescopic slides* (metric table, 08/22): https://www.albeco.com.pl/pl/katalog/preview/accuride_3832_en.pdf
- Accuride, *Model 3308* technical sheet, doc. 3700-1070(9423)-MK563-R2-0402: https://www.elite.parts/datasheets/8ox5kny1.pdf
- Accuride, 3308 product page (price, features): https://www.accuride.com/en-us/products/drawer-slides/3308-medium-duty-slide-with-latch-disconnect-lock-in-and-lock-out
- Accuride, *4032/4033/4034/4035 Quick Reference*: https://www.accuride.com/media/amasty/amfile/attach/9de415e16f14fe55f9fd6058ae551c38.pdf
- Accuride, product catalogue (© 2018), "Specifications at a glance", 3832E family, 4000 series, 3634, 3641/3640A, 3600/7950, 9300E, CB-Hand: https://res.cloudinary.com/amerhart/image/upload/Documents/Product/Accuride_4180_0266_XE_CAT.pdf
- Accuride, *Slides for Mobile Applications*, SS-Mobile-Applications-0821 (2021): https://info.heilind.com/hubfs/Slides%20for%20Mobile%20Applications_2.pdf
- Accuride, *Enhanced 9300 Slide Family* brochure (2017): https://res.cloudinary.com/amerhart/image/upload/Documents/Product/Accuride_C9308E5_18D_BRO.pdf
- Accuride, 3608 product page (price): https://pwa-dev.accuride.com/en-us-en-us/products/c3608-heavy-duty-handed-slide-with-lock-in-and-lock-out
- Accuride, 9308E and 9308-E5 pages (prices, snippet): https://www.accuride.com/hardware/9308e, https://www.accuride.com/hardware/9308-E5

**Knape & Vogt**
- Knape & Vogt, *Hardware Guide* (© 2026). Slide quick reference, 8400, 8417/8400RV, 8450FM, 6500, 8500, 8520, 8600, 8650FM, 8810, 8850FM, 8900, 8908: https://www.knapeandvogt.com/sites/default/files/Hardware-Guide.pdf
- Knape & Vogt, *8400 Specifications*, OL2806/1119: https://www.knapeandvogt.com/sites/default/files/OL2806_8400_Specs-1119.pdf
- Knape & Vogt, 8908 product page: https://knapeandvogt.com/products/8908-extra-heavy-duty-full-extension-lock-inlock-out-drawer-slide

**Blum**
- Blum, product data for MOVENTO 769R5330S (Julius Blum GmbH data sheet, distributor-hosted): https://xcart.wurthlac.com/skin/common_files/files/specs/B769R5330S_SpecSheet.pdf
- Blum MOVENTO installation and drawer specifications (Richelieu-hosted): https://static.richelieu.com/documents/docsGr/121/081/5/1210815/1684752.pdf

**Hettich**
- Hettich America, *KA ball bearing runners* brochure (04/22): https://web.hettich.com/fileadmin/Company_website/HUS/Media/HUS_KA_Slides_Brochure_0422_update.pdf
- Hettich, *Locking systems* (Stop Control): https://hettich.com/en-ba/products/runner-systems/locking-systems

**Retail prices**
- Rockler, Accuride 3832E (live page): https://www.rockler.com/accuride-3832e-100-lb-full-extension-drawer-slides
- Rockler, Accuride 9301 (live page): https://www.rockler.com/accuride-9301-extra-heavy-duty-600-lb-full-extension-drawer-slides
- Top Cabinet Hardware, 3832EC 22" (snippet): https://topcabinethardware.com/product/ac-3832ec22z-2/
- Build.com, KV 8400P 22 (snippet): https://build.com/knape-and-vogt-kv8400p22/s1086298
- Ferguson, KV 8600B 22 (snippet): https://fergusonhome.com/knape-and-vogt-8600b-22/s1397775
- Würth LAC, KV 8908B 42 (snippet): https://wurthlac.com/product/121195/8908-Lock-In-Lock-Out-Drawer-Slide-with-500lb-Capacity-Full-Extension-Side-Mount-Zinc-42-Polybag
- WW Hardware, Blum 769 (snippet): https://www.wwhardware.com/blum-769-movento-170lb-static-full-extension-slide
- Drawer.com, MOVENTO locking devices (snippet): https://drawer.com/standard-locking-devices-for-763-769-blum-movento-slides
- Home Depot, generic 22" 100 lb 10-pair box (snippet): https://homedepot.com/p/22-in-Black-Full-Extension-Ball-Bearing-Drawer-Slides-10-Pair-PI-4600-22-08x10/313562886
