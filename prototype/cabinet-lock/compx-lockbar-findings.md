# CompX Timberline lockbar: groove, multi-column drive, anti-tip and keying facts

Follow-up to [research/interlocks-locks.md](https://github.com/uf-cpe-design-lab/kagu/blob/research/interlocks-locks/research/interlocks-locks.md). Researched 2026-11-10. This file records facts only and makes no design decisions.

## Sources and how they were read

- **[T]** Timberline catalog: https://easykeys.com/PDFS/Timberline_Catalog.pdf. Page numbers below are the printed page numbers.
- **[FL]** CompX Timberline full-line catalog: https://compx.com/resources/timberline_full_line_catalog.pdf. Its p.5 adds lockbar sizing that [T] does not have.
- **[F19]** CompX Timberline Feb 2019 catalog: https://compx.com/resources/compxtimberline_feb2019.pdf (lock plug and keying table, p.2).
- **CompX application drawings.** The live URLs (`compx.com/sheets/timberline_app/<ID>.pdf`, referenced on [T] p.13) now return 404, so I retrieved the drawings from the Wayback Machine. Each one cited below is `https://web.archive.org/web/2010/http://compx.com/sheets/timberline_app/<ID>.pdf`. Snapshot timestamps are 2010-11-03/04, and the F-125, F-130 and F-135 snapshots are from 2023-09-26. The drawing title blocks say "Copyright 2007", and several are marked "Revised 1992/1994".
  - I read: B-100, B-105, B-110, B-115, B-120, B-125, B-127, C-100, C-105, C-110, C-115, C-120, D-100, D-101, D-105, D-110, D-150, D-160, E-300, F-100, F-101, F-105, F-110, F-125, F-130 and F-135.
  - **I could not read F-120 (System 400) or S-100/S-110/S-120.** Their Wayback copies are truncated at 1 MB. B-135, B-140 and B-145 were not fetched, because they cover glass-door locks and the Regulator, which are outside this scope.
- **compx.com product pages** (`compx.com/?p=...`) return HTTP 403 to scripted fetches. Anything attributed to them below comes from search-engine snippets and is marked *(snippet)*.
- **Prices** were read live from easykeys.com on 2026-11-10 unless marked otherwise.

## 1. Groove, pins and clips

**Lockbar groove in the case side.** The same dimensions recur on every front and side gang-lock drawing that uses an LB-240 (B-100, B-105, B-110, B-115, C-100, F-105, F-110):
- Width: **11/16" (+1/32 / −0)**, which is 17.5 mm (+0.8 / −0).
- Depth: **5/32" (+1/32 / −0)**, which is 4.0 mm (+0.8 / −0).
- Setback: the front edge of the groove sits **1-1/4" (31.75 mm) behind the case front edge**.
- Exception: System 104 / B-120, "lockbar 2-1/2" back in case" (32 mm construction), puts the groove front edge 2-1/2" back.
- [T] p.10 (System 150) and p.6/7 show the same values as "11/16" MIN, 5/32" MIN, 1-1/4"".
- F-135 (2022, System 400 filler) repeats 11/16" min × 5/32" min.

**System 150 side-panel lock (C-100, "lock in knee space panels"):**
- 16.5 mm lock hole, centred **3/4" from the front edge**. The drawing also gives 1/2" (±1/32) between the hole and the groove, with the groove front edge at 1-1/4".
- The CB-150 body passes through the panel. **The key face (LP plug) is on the opposite face of the panel from the lockbar, LC-150 clip and drawers**: the key is on the knee-space side and the lockbar is inside the pedestal.
- Lockbar travel is 1/2".
- Drawing note: "Materials 3/4" unless otherwise shown."

**Panel thickness options:**
- CB-150 is for 3/4" material and CB-150-1 for 1" ([T] p.10).
- C-105: a 1" panel needs a lock pocket routed 1-7/8" × 7/8" wide × 1/4" (+1/32) deep, plus the LC-151 flat clip.
- C-110: panels 1-1/8" to 2-1/8" use CB-110 with LC-152.
- C-115: panels 2-1/8" to 3-1/4" use LC-101.
- [T] p.4: "most Timberline locks are designed for mounting in 3/4" or 1" panels."
- **No drawing covers panels thinner than 3/4".** 18 mm is 0.709", which is 1.05 mm thinner than 3/4". *Unverified:* whether CB-150 seats correctly in 18 mm.

**Lockbar length and part number ([FL] p.5):**
- CompX recommends lockbar length = "interior cabinet height minus 1.000"."
- Part numbers by length:

| Part | Length range |
|---|---|
| LB-120 | 6.000" to 17.999" |
| LB-240 | 18.000" to 29.999" |
| LB-360 | 30.000" to 41.999" |
| LB-480 | 42.000" to 53.999" |

- CompX supplies bars cut to length. The retail LB-480 is sold as a 47"/48" stock bar that the buyer cuts.
- B-100 note: the lockbar "must be restrained from dropping"; "a small screw or a drawer locking clip at the bottom end of lockbar may be used". The LR-100 retainer also does this ([T] p.5).
- E-300 (wardrobe lock) uses LB-480 with SP-260 supports at 18" max spacing. That is a different application.

**AP-037 pins:**
- 3/8" pins that install "with a 1/4" hex tool to any position along the length of the lockbar" ([T] p.5, p.12).
- **No hole spacing rule exists for adjustable pins.** Positions are set per drawer.
- For anti-tip systems, the pin goes at the centre of a line squared across from each wedge opening, with the lockbar in the "middle (open) position" (F-100, steps 3 to 5).
- F-101 (wedge/pin locator): install the pin "so that the washer just touches the bottom score line", which "will allow the drawer to sag without falling out of adjustment."
- Fixed-pin custom bars: pins at 0.500" from the bar end (F-125, System 400 linkage bar, ±1/32").

**DC-500 clip:**
- Dimensions: 1-1/4" long × 19/32" tall × 7/16" deep, for 1/2" slide clearance ([T] p.12).
- DC-502 is for 3/4" slides and DC-510 for 7/8".
- **No drawing found gives the DC-500's vertical or fore-aft position relative to the slide.** Illustrations ([T] p.5) show it on the drawer box side, near the front, above the slide. C-120 (CB-270) shows the DC-500 at the drawer-side top and bottom edges.

## 2. System 150 lock and System 350 wedges on one bar

**No CompX statement either way was found.** Relevant facts:
- **Positions differ between the systems.**
  - SN-300 snapper (Systems 350 and 300) has three positions: "UP locked / CENTER unlocked / DWN locked" (F-105).
  - D-100: "open position: middle position on AC-200, lower position on AC-500."
  - System 150 is a two-position 1/2" throw, with "lockbar up" for locked and "lockbar down" for unlocked ([T] p.5, C-100).
- **Two-sidedness.** System 300 uses a gearbox cylinder (CB-500) and an AC-200 actuator on each side. It does not use LC-150.
- **The closest documented hybrid is D-160:** a side gang lock (C-100) whose lockbar motion is carried to other lockbars through AC-500 actuators and an SS-360 square shaft. No wedges are shown on it.
- Whether LC-150 lets the bar travel both up and down from its unlocked position is **undocumented**, so ask CompX (1-800-LOCKBAR, timberlineorders@compx.com).

## 3. System 300: FS-362, AC-200 and cylinder location

- **FS-362** is a "double sided" flexible shaft, made to order ([T] p.18, F-110). It is a **rotary** shaft: its square end "press[es] into the gearbox" of the cylinder, and it is "not removable when the lock is in the locked position" (D-100).
- **Shaft length:**
  - System 300: X − 5/8", where X = the inside width of the case between the sides, with the lock centred (F-110).
  - System 500: X − 1/4", where X = the distance between actuator mounting surfaces ([T] p.11, D-105).
- **Maximum length:**
  - CompX: "produced in lengths 6"–42"" *(snippet, compx.com/?p=761450)*.
  - Easykeys lists dual-sided shafts at up to 18", 18–30", 30–42" ($11.97) and **42–54" ($14.97)**, with the exact length entered in the order notes. Its keywords list FS-121, FS-122, FS-241, FS-242, FS-362 and FS-482 ([easykeys FS](https://easykeys.com/products/1806_Timberline_Flexible_Shaft_FS.aspx)).
  - **Conflict:** 42" (CompX) versus 54" (easykeys).
  - FS-362 works with AC-200, AC-500 and AC-600 *(snippet)*.
- **AC-200** is the System 300 actuator, "one actuator on each side of the furniture wall", used with CB-500 ([easykeys AC-200](https://easykeys.com/products/1542_Timberline_Actuator_AC-200)). Its middle position is open (D-100).
- **Cylinder location:**
  - System 300 uses CB-500 (3/4" material) or CB-500-1 (1"), which "mounts in 1" exposed rail" ([T] p.18).
  - F-110 is titled "lock mounted in top rail". Its 16.5 mm hole sits 1/2" below the top of a 1" rail.
  - **No CompX drawing shows a CB-500 or CB-550 gearbox in a side panel, a top or a drawer front.**
  - Accuride's kit sheet says: "For cabinets requiring a lock cylinder mounted in the center of the cabinet, consult Timberline for their #AC600 actuators and related hardware with flexible steel actuating cable… allows the cabinet to be locked on both sides" ([4180-0345-XE PDF](https://static.richelieu.com/documents/docsGr/100/855/5/1008555/1395122.pdf)).

## 4. Locking two lockbars with one key

| Method | Parts | Cylinder location | Source |
|---|---|---|---|
| **Double lockbar through a partition** | Two LB-241 bars, one in a groove on each face of the partition (11/16" × 5/32" each, 1-1/4" back), joined by a **pass-through lockbar pin** in a 3/8"-wide × 1"-long slot cut through the partition. Pin length = partition thickness (3/4", 1" or 1-1/2"). Pin position is specified on the LB-241 order (shown 1-1/2" from the top end). | CB-100 with LC-100 at the top of the drawer face (or rail) beside the partition, 1-1/4" from it | B-127 |
| Lock in a stile between pedestals | CB-110 with two LC-102 reverse-mount clips through 1/4" × 1-3/4" slots in both panels. Stile 1" min, 1-1/2" max. | Stile face | B-125 |
| **Square-shaft transfer** | AC-500 actuators on each lockbar plus SS-360 square shaft: "the actuators convert the action into a rotating motion of the square shaft, transferring the up and down action between the lockbars." | Driven by a side gang lock (C-100) or a double lockbar (B-127) | D-160 |
| System 500 central | CB-550 gearbox, FS-362 shafts and AC-500 actuators. "Up to four pedestals and a center drawer… using ONE lock mounted on a front exposed rail" (1" min). | Front rail | [T] p.11; D-105, D-110, D-150 |
| System 300 | CB-500, two AC-200 actuators and FS-362 | 1" top rail | [T] p.18; F-110 |
| System 120 double-sided | CB-120, AC-120 drive, AC-125 remote actuator and SS-360-36" square shaft | Drawer front | [T] p.9 |
| Accuride 4180-0345-XE | Interlock-slide gang kit. "Locks mounted on both sides: order 2 kits"; AC600 cable for a centre lock | Header rail or drawer front | Accuride PDF above |

- D-160's two-bay sketch shows a centre partition with a double lockbar (B-127) plus AC-500 square shafts to the outer-side lockbars.
- **No "dual-bank" kit part number was found.** Every method above is assembled from parts.

## 5. Anti-tip wedge rules (Systems 300 and 350)

- **Single-sided limit:** "Lockbar and plastic wedge required on BOTH sides for 3 or 4 drawer units. 2 drawer unit may be single sided" (F-105).
- **The A/B pattern is documented only for 2, 3 and 4 drawers** ([T] p.17; F-100).
  - Left side, top to bottom: A, B, A, B.
  - Right side: A, B, B, A.
  - "Follow pattern of wedge ('A' & 'B') placement on drawers."
  - **No pattern was found for 6 or 7 drawers per column.**
- **Tooling:** [T] p.17 says the TL-200 wedge/pin marking tool is "required for proper installation". F-101 shows the tool procedure. F-100 shows a manual alternative: mark the wedge-opening centre on the case side, then square a line across the lockbars.
- **Minimum drawer pitch or slide spacing for WD-21: not found.** The only stated minimums are for System 400: 7-5/8" between slides, or 6-1/8" with the DC-410 clip ([T] p.14–15).
- **Not found:** WD-21 wedge dimensions, and any statement on slide type, extension or drawer width. F-100 says "drawer suspensions not shown". [T] p.18 says System 300 "locks wide drawers on both sides".
- **Older part numbers:** the drawings call the wedges WD-20A/B (or W-20A/B). The current catalog uses WD-21A/B.
- **Shipping:** the WD-100 wedge lock is needed during shipping. Otherwise "access to lockbar must be provided at bottom of case to allow lockbar to be 'reset' to open position" (F-105).

## 6. Availability and price

Easykeys, 2026-11-10. Unit price, then 2+/5+/10+ price where given.

| Part | Price | Notes |
|---|---|---|
| LB-480 | $7.47 / 6.47 / 5.27 / 4.47 | "Only 8 left"; listed as 47" and cut to size ([link](https://easykeys.com/2375_CompX-Timberline-Lockbar_LB-480.aspx)) |
| LB-240 | $5.47 | |
| AP-037 | $3.97 / 3.47 / 2.77 / 2.17 | |
| DC-500 | $2.97 / 2.47 / 1.97 / 1.47 | |
| LR-100 | $2.97 | |
| LC-150 | $5.47 | |
| AC-200 | $9.97 / 8.47 / 6.97 / 5.47 | 34 in stock |
| AC-500 | $7.47 | |
| WD-21 type A / type B | $3.97 each | Type A "only 5 left" ([link](https://easykeys.com/products/324_Timberline_Anti-Tip_Wedges.aspx)) |
| FS dual-sided 30–42" / 42–54" | $11.97 / $14.97 | Custom length |
| CB-150, CB-100, CB-101 | $9.97 each | CB-150 "only 11 left" |
| CB-500 | $11.97 | |
| LP plug, TA series (nickel) | $5.87 | TB series $14.07 |

Prices are from the [category pages](https://easykeys.com/manufacturer/compx_timberline/file_cabinet_accessories) and [drawer_door_locks](https://easykeys.com/manufacturer/compx_timberline/drawer_door_locks).

- **SN-300:** no retail price found. compx.com says "Contact to Purchase" *(snippet)*.
- **TL-200:** no listing found.
- **Würth LAC:** LB-480 is TMBLB-480 at $2.40 ($1.83 at 200+), and WD-21A is listed with a $0.00 placeholder. Both are *(snippet; site returned 429)*.

## 7. Keying

- **Master-keyed as standard.** Plugs are "Master-Keyed Standard" ([F19] p.2; [T] p.3).
- **Keyed-alike codes:** 100T to 109T (10 codes).
- **Keyed-different kits:** 25 plugs, coded 110T–134T, or 200 codes in the 110TA–209TA and 700TA–799TA ranges ([F19] p.2).
- **Master key:** D101KY, sold as a stock item ([F19] p.7).
- **Plugs and bodies:** "Any lock plug snaps into any cylinder body"; plugs are removed with the D500KY / KY-500 change tool and can be rekeyed in the field ([T] p.4).
- **What this means for the plan:** two plugs with the same KA code (one per column), plus lid-lock plugs on a different code, are all opened by the standard master.
- **Caveats:**
  - The master is a catalog part, not unique to UF.
  - The TB and TC series have separate control keys ([easykeys control keys](https://easykeys.com/manufacturer/compx_timberline/control-keys)).
  - **Unverified:** whether D101KY opens TB/TC plugs, and whether CompX offers custom or restricted master systems.

## Not verified / still open

- Seating of CB-150 in 18 mm ply.
- Whether a 150 and a 350 can share one bar.
- The A/B wedge pattern for more than 4 drawers.
- The WD-21 envelope and minimum pitch.
- The 42" versus 54" FS length limit.
- SN-300 and TL-200 price and availability.
- Scope of the D101KY master.
- F-120 and S-100/110/120 (truncated archives).
- compx.com product pages (403).
