# Interlock and whole-cabinet lock options

Research for [#5](https://github.com/uf-cpe-design-lab/kagu/issues/5) on the [wayfinder map #1](https://github.com/uf-cpe-design-lab/kagu/issues/1). Researched 2026-11-08.

## Question

What mechanisms can (a) lock every **Drawer** in the **Cabinet** with one key (or one key per column), and (b) act as an anti-tip interlock so only one Drawer opens at a time? And how can a per-drawer **Viewing Lid** lock on a **Locked Drawer** coexist with the whole-cabinet lock?

Constraints: 3/4" plywood **Carcass**, side-mount ball-bearing slides, mobile on casters, about 915 mm tall. The shop has a table saw, miter saw, router, drill press, hand tools and a Prusa XL, and no CNC.

## TL;DR

- **The interlock and the whole-cabinet lock can be one mechanism.** Every commercial system found works by moving or jamming a single vertical member per drawer column (a lockbar, a rod stack, a block stack or a cable). Opening one Drawer moves that member far enough to block the others, and a key cylinder that holds the member in its blocking position locks them all. This is how Accuride, CompX Timberline, Steelcase and Häfele systems all work (sources below).
- **Provisional pick: a CompX Timberline-style lockbar system on one side of each Bay.** That means a steel lockbar in a routed groove in the Carcass side, drawer clips or wedges on the Drawer box sides inside the normal 1/2" slide gap, and a key cylinder in a 16.5 mm hole. It is cheap (the 24" lockbar sells for about $1.40 to $4.87), it is drawn for wood furniture, the only machining is a router groove and a drilled hole, and it works with ordinary 1/2"-clearance side-mount slides. Its anti-tip wedges (System 350/300) put the interlock on the same bar.
- **Commercial alternative: Accuride 3641/3642 interlock slides plus the 4180-0345-XE gang-lock kit.** This is proven and does both jobs, but it needs 0.89" side space on the interlock side and costs about $80+ per pair, so roughly 10 to 20 times the cost of the lockbar route at kagu's drawer count.
- **Printable route: a stacked-block channel** (the Steelcase US 4,960,309 principle). Printed blocks and pivoting cams sit in a vertical channel whose free space equals one cam thickness, and a key bolt that fills that gap locks everything. It is fully printable and drawable from the patent, but I found **no documented DIY build**, so it is a prototype risk.
- **Viewing Lid locks are a separate, second layer on the Drawer itself.** The Locked Drawer still slides and still takes part in the interlock, so students can pull it out and look in. Only its lid is locked. The cleanest way to key it is the same removable-plug, master-keyable cylinder family (Timberline glass-door or cam locks) with a different key code, plus a staff master key. A real precedent is ClickNetherfield's museum "Access" drawer units: each drawer's glass top locks with two push locks, and a separate cabinet lock stops drawers opening.
- **The geometry catch:** a hinged Viewing Lid can only swing open if its hinge line sits in front of the Drawer fronts above it at full extension. That calls for 1" over-travel slides, or a lid that is shorter than the Drawer box (see Implications).

## Weighed comparison

Build difficulty is for this shop. Cost is per Bay column of about 6 to 8 Drawers unless noted. "Slides" means compatibility with ordinary side-mount ball-bearing slides at 1/2" side clearance.

| # | Mechanism | Interlock | Whole-cabinet lock | Build difficulty | Cost (est.) | Plywood / slides fit | Main failure modes |
|---|---|---|---|---|---|---|---|
| W1 | **Hinged external locking bar** (ABUS/HPC/McMaster file bar, or a DIY aluminum angle with a padlock hasp) | No | Yes (padlock) | Very easy: drill and screw | $20 to $60 per column | Any slides. Needs overlay fronts and about 1" of free edge for the bar to swing | Bar flex lets drawers creep open a little; it snags hands and carts; it is visually crude; the padlock gets lost or left open |
| W2 | **Internal gang lockbar** (CompX Timberline System 150/101/104) | Only with W2+ | Yes (one key) | Easy: router groove plus a 16.5 mm hole | Lockbar about $1.40 to $5 plus clips, pins and cylinder (assumed low tens of $, unverified) | Drawn for 3/4" or 1" wood panels; clips fit inside a 1/2" slide gap (DC-500), with DC-502 and DC-510 for 3/4" and 7/8" gaps | Pins drift out of adjustment; the bar drops when unlocked unless retained (LR-100); racking of the Carcass misaligns pins |
| W2+ | **Lockbar plus anti-tip wedges** (Timberline System 300 with lock, 350 without lock, 400 snapper for 2 to 4 drawers) | Yes | Yes (Sys-300) | Moderate: wedge and pin positions must be marked precisely (TL-200 tool) | As W2 plus wedges and snapper (about $5 to $15, unverified) | Same as W2. Sys-400 needs 1/2" slide clearance and at least 6-1/8" to 7-5/8" between slides | Wrong wedge A/B pattern lets two drawers open; misaligned wedges jam; the snapper wears |
| C1 | **Accuride 3641/3642 interlock slides plus 4180-0345-XE gang-lock kit** | Yes | Yes (customer-supplied cam cylinder, e.g. Timberline type 100) | Easy to install, but rods must be cut to ±0.020" | About $80+ per pair, about $640+ per column of 8, plus the kit | Made "for wood applications"; needs **0.89" side space** on the interlock side; 1" over-travel; 180 lb per pair | Rods cut short add lash; a slide failure takes out the whole column's interlock; few lengths stocked |
| C2 | **Accuride DZ5343/DZ5344** (European interlock slide, DB65050-1 lock kit) | Yes | Optional lock kit | Easy to install | Not priced; distributor item | 19.1 mm slide thickness; up to 100 kg | Same as C1; hard to source in the US |
| C3 | **Häfele / Hettich central locking bar with anti-tilt stop** | Yes (Matrix Box P version) | Yes | Easy, but only with that maker's drawer system | Moderate | **Tied to Häfele's Matrix Box P drawer sides**; not for generic ball-bearing slides | System lock-in; parts are discontinued over time |
| C4 | **item Line 8 telescopic-rail interlock** | Yes | No | Easy, but only with item aluminum frames and rails | Not priced | Not plywood; reference only | System lock-in |
| D1 | **DIY stacked-block channel** (Steelcase US 4,960,309 principle, printed blocks and cams) | Yes | Yes: a key bolt fills the free gap | Moderate to hard: needs a prototype and a printed drilling jig | About $10 to $25 per column (filament, aluminum channel, pins, one cam cylinder) | Mounts on the Carcass side in front of or behind the slides; drawer bracket on the box side within the slide gap | Block stack tolerance: too much free space lets two drawers open, too little jams; printed cams wear or creep; humidity moves plywood |
| D2 | **DIY ball string** (Lakso / ESP, EP 0 286 199) | Yes | Yes: a bolt or spring stop at one end | Moderate: printed actuators plus steel balls in a routed or tube track | About $10 to $25 per column | Same placement as D1 | Ball count and free space are critical; debris jams the string |
| D3 | **DIY cable with slack** (Steelcase US 3,941,441) | Yes | Not inherent (needs an added clamp) | Hard: cable tensioning and adjustment | Low | Side wall | Cable stretch keeps changing the slack budget, so it needs re-tensioning |
| F1 | **Locking front panel or door** (Gerstner-style front lid that stows under the bottom drawer) | No | Yes | Moderate: a panel plus sliding hinge or stow slot | $30 to $80 | Any slides | Panel weight and stowage space; slow for daily use; reduces Tool Wall or face space |

## Mechanism descriptions

Each description covers what the parts are, what moves, and where it mounts, in enough detail to draw.

### W1. Hinged external locking bar

- **Parts:** A 16-gauge steel bar (or aluminum angle) as tall as the drawer column; 2 to 3 hinges or a pin-and-clevis at top and bottom; a lift lever; a padlock hasp at the top.
- **Mounting:** The bar is screwed to the Carcass face or side edge on the hinge side. It sits flush with the outside of the Carcass and needs about 1" free beside it to swing.
- **Motion:** The bar swings 90° on a vertical axis and lies across the edges of the overlay Drawer fronts. The lever lowers to latch it, and the padlock through the top stops the lever being raised. The McMaster style instead slides over a notched pin at the bottom and drops onto a clevis pin at the top.
- **Real examples:** the [Hunker install guide](https://www.hunker.com/13419376/how-to-add-a-lock-to-a-filing-cabinet/) (step-by-step for a commercial file bar), the [ABUS file cabinet locking bar video](https://www.youtube.com/watch?v=0X_HMILR72Q), and the [McMaster locking bars catalog page](https://www.mcmaster.com/locking-bars), which has photos. Commercial bars only cover part of the top and bottom drawers: one buyer saw about half of each on a 3-drawer cabinet. A DIY bar can be sized to the column.
- **Notes:** It is useful as a stopgap or as the lock for an instrument Bay, but it does nothing for anti-tip.

### W2. Internal gang lockbar (CompX Timberline)

Source: [CompX Timberline catalog](https://easykeys.com/PDFS/Timberline_Catalog.pdf), pp. 5 to 13.

- **Parts:**
  - LB-240 steel lockbar (24", cut to length; LB-480 is 48").
  - AP-037 adjustable 3/8" pins, set with a 1/4" hex at each Drawer height.
  - DC-500 drawer locking clips on each Drawer box side (DC-502 and DC-510 for wider slide gaps).
  - LC-1xx lockbar clip, which links the cylinder cam to the bar.
  - LR-100 lockbar retainer.
  - Cylinder body (CB-150 for a side-panel mount; CB-101 in a drawer front; CB-100/104 in a fixed rail) with a removable LP-x00 plug.
- **Mounting:** The lockbar lies in a vertical **groove routed in the inside face of the Carcass side** near the front. The cylinder sits in a 16.5 mm hole, either in the side panel (System 150, "lock hole only machining") or in a front rail or top Drawer front (Systems 100, 101, 104).
- **Motion:** Turning the key cams the bar vertically by its full 1/2" throw. In the locked position ("lockbar up" in the catalog figure), each pin sits in front of the hook of its Drawer's clip, so the Drawer cannot open. In the unlocked position the pins clear the clips. The catalog warns: "Lock bar must be restrained from dropping when in open position."
- **Real examples:** catalog drawings on pp. 5 to 11 (all dimensioned); [LB-240 product photo](https://easykeys.com/products/2276_CompX-Timberline-Lockbar_LB-240); [Würth LAC listing](https://wurthlac.com/product/147675/Timberline-24-Lockbar).
- **Keying:** Any lock plug snaps into any cylinder body. The plugs are master-keyable, with over 500 key changes, and can be rekeyed in the field with the KY-500 tool (catalog pp. 3 to 4). This matters for the Viewing Lid keying plan below.
- **Keyless option:** The CompX "Regulator" gives keyless control of gang-lock systems 100, 101 and 104 (catalog p. 13). This is a natural hook for the future electronic-lock provision.

### W2+. Lockbar with anti-tip wedges (Timberline Systems 300, 350, 400)

Source: Timberline catalog, pp. 14 to 18.

- **System 400** (2 to 4 drawers, no lock): an SN-400 "snapper" on the Carcass side and a DC-400 drawer clip on each Drawer. "When either drawer is pulled open, the drawer clip on that drawer moves the snapper into a locked position, thereby preventing any further drawers from being opened." For 3 to 4 drawers, an SN-410 linkage arm and a lockbar join the snappers. Dimensions: lockbar = X + 1", and pin spacing = X − 1", where X is the distance between snappers. It needs at least 7-5/8" between slides (6-1/8" with the narrow DC-410 clip) and 1/2" slide clearance. Retail: [TLSN400 snapper](https://absupply.net/compx-tlsn400-anti-tip-interlock-system-anti-tip-snapper.aspx).
- **System 350** (no lock) and **300** (with lock): the same LB-240 lockbar, with type A and type B anti-tip wedges ([WD-21A](https://compx.com/?p=546963)) on each Drawer and an SN-300 snapper. "When any drawer is pulled open, the wedges on that drawer move the lockbar into a locked position... only one drawer may ever be open at any one time... even if two drawers are pulled at exactly the same time." That last property depends on the A/B wedge pattern shown on p. 17, and the TL-200 marking tool is "required for proper installation." System 300 adds an AC-200 actuator that is driven through an FS-362 flexible shaft from a lock mounted in a 1" exposed front rail.
- **Why it matters for kagu:** this is the only off-the-shelf pairing I found where the interlock and the one-key lock share a single bar, mount in wood, and stay within the normal 1/2" slide gap.
- **Gap:** The catalog drawings are for lateral files. Before committing, check the per-system application drawings referenced at compx.com/instructions.html (drawings B-100 to C-115) for groove size and setback. I could not retrieve them.

### C1. Accuride 3641/3642 interlock slides with gang lock

Sources: [Accuride 3641X system page](https://www.accuride.com/en-us/products/3641x-heavy-duty-interlock-slide-system), [4180-0345-XE kit sheet (PDF)](https://static.richelieu.com/documents/docsGr/100/855/5/1008555/1395122.pdf), and [US 6,296,332 (Accuride)](https://patents.google.com/patent/US6296332).

- **Parts per Drawer:**
  - One 3641 interlock slide on one side and one 3642 non-locking companion on the other.
  - Adapter rails and mounting hardware. The 3641X kit includes one 3641, one 3642, a connecting rod, two adapter rails and a hardware kit.
  - A 1/4" (6.4 mm) aluminum or steel rod between each pair of adjacent slides, cut to **(slide centerline spacing − 2.00") ± 0.020"**.
- **Motion** (from the patent):
  - Each slide's stationary member has an upper and a lower follower at its front end, with rods linking the upper follower of one slide to the lower follower of the slide above.
  - Extending a Drawer drives a tapered actuator on its moving member, which pushes its upper follower up. That push goes through the rod into the lower follower of the slide above, then into that slide's upper follower, and so on up the stack. Each follower lands in its slide's extension path and blocks it.
  - The open slide also blocks the followers below it from rising. Blocking happens within the first 1/8" of about 1/2" of follower travel.
- **Lock:** The 4180-0345-XE kit adds an interface actuator (Timberline AC610) above the top slide, driven by a customer-supplied eccentric cam cylinder. A Timberline type 100 is named. The cylinder goes in the header rail or in the top Drawer front, and needs a minimum 1/4" stroke to activate the lock. Holding the top of the rod stack in its blocking position locks every Drawer. The rod from the actuator is "X − 1/8"" (X = top slide centerline to actuator bottom).
- **Specs:** 0.89" side space, 1" over-travel, up to 180 lb per pair, and drawers up to 42" wide (Accuride page). One retailer contradicts the 180 lb figure, so check before ordering. Lengths are 14", 16", 18" and 20" at [Harbor City Supply ($80.19 base per pair)](https://www.harborcitysupply.com/accuride-3641-3642-interlocking-drawer-system-two-drawer-kit).
- **Real examples:** product photos on the Accuride page; a [3641 CAD model](https://www.cgtrader.com/free-3d-models/engineering-parts/accuride/model-3641-1-25-4-mm-over-travel-interlock-feature-allows-only-one-drawer-to-open-at-a-time-loads-up-to-180-lbs-82-kg-per-pair-rail-and-pocket-mount); and a video of the sibling [Accuride 5343 interlock slide with optional lock](https://www.youtube.com/watch?v=wSXJFZRK4QA).
- **Related:** Knape & Vogt sells a similar "INTERLOK" anti-tilt line (KV 8400 at the 100 lb class, KV 8800 at the 200 lb class) in its [OEM toolbox guide](https://knapeandvogt.com/sites/default/files/KV_OEM_Toolbox_Guide_FINAL_rev2.pdf).

### C3. Häfele and Hettich central locking bars

- **Häfele Matrix Box P** ([catalog p. 10.56](https://files.hafele.co.uk/CatalogFiles/www/23T10-56.pdf)): a galvanized steel central locking bar hangs in the runner on one side and is sized by height units (1 HE = 64 mm, available in 7.5 HE = 483 mm and 10 HE = 643 mm). A Symo 3000 rotary lock case in the front panel has a lifting pin with 12 or 17 mm travel that lifts the bar. Catalog text: "Central locking system with anti-tilt safety stop: Prevents simultaneous opening of several drawers."
- **Fit:** Only with Häfele's drawer sides, so it is **not a fit for kagu's generic slides**. It is still a good visual reference for the lifting-bar principle: see the [Central Locking Bar functional principle video](https://www.youtube.com/watch?v=xfcH1SqGnYo), the [Hettich drawer locking system assembly video](https://www.youtube.com/watch?v=G6cfoaB8sRI), and the stand-alone [Häfele 237.42.109 vertical lock bar](https://store.homedecorhardware.com/hf-237-42-109.html).

### C4. item Line 8 interlock

- **Mechanism:** A plastic locking element on each Drawer frame lifts its locking clip when the Drawer is pulled. A guide bar running in a vertical Line 8 groove then moves all the other clips into their locked position (see the [item product page](https://www.item24.com/en-us/telescopic-rail-interlock-locking-set-8-73333), which has an animated WebP of the motion, and the [install video](https://www.youtube.com/watch?v=BGM96ztSWpY)).
- **Specs:** rated for 50,000 cycles, 33 g per set.
- **Fit:** It is tied to item extrusion frames and soft-close rails, so it is reference only. It shows that a printed locking element plus a bar in an aluminum-extrusion slot is a production-proven layout, which makes it relevant to D1.

### D1. DIY stacked-block channel (recommended DIY form)

Principle from [Steelcase US 4,960,309](https://patents.google.com/patent/US4960309). The patent figures are the drawable reference.

- **Parts:**
  - A vertical channel. In the patent it is a dovetail channel open toward the Drawers. For kagu it could be a routed dado with a printed or aluminum cover, or a slot-profile aluminum extrusion.
  - A stack of lock blocks ("control blocks"), each with angled cam-follower ends.
  - One pivoting cam actuator per Drawer, hinged in an attachment channel beside the block channel.
  - An L-bracket on each Drawer box side whose leg engages the actuator's control slot.
- **Motion:** Opening a Drawer pivots its actuator so its cam wedges between two adjacent blocks. The blocks above it rise until they hit the closed top of the channel.
- **The slack budget:** channel height = stack height + **one cam thickness**. Once one cam is in, no other cam can enter, so no other Drawer can open. Closing the Drawer pivots the cam back out.
- **Lock:** A key cylinder at the front shifts a lock member into the top of the channel against the top block, which uses up the free gap. Then no Drawer can open, and the lock only engages when all Drawers are closed. That gives one key per column for free.
- **Mounting:** on the Carcass side (or a Bay divider). The patent also shows a rear-center upright variant.
- **Printable parts:** blocks, cams and brackets in PETG, PA or PC; steel dowel pins as cam pivots.
- **Real examples:** This is a production Steelcase lateral-file mechanism, and the patent drawings show every part. **I found no documented DIY or printed build** on Printables, Thingiverse, MakerWorld, Instructables or the woodworking forums I searched. A [LumberJocks "one-at-a-time drawers" thread](https://www.lumberjocks.com/threads/one-at-a-time-drawers.266185/) discusses rocker, wedge and bail approaches and the Timberline wedge kit, but without a finished build.

### D2. DIY ball string

From the [Lakso / Engineered Security Products application EP 0 286 199](https://data.epo.org/publication-server/rest/v1.2/patents/EP0286199NWA1/document.html).

- **Parts:** A vertical track on the inner side wall holds a row of loose balls behind a narrow front slot. Each Drawer has a fixed pin that drives an oscillating actuator on a plate screwed across the track, and each actuator carries an offset ball.
- **Motion:** Opening a Drawer forces its actuator's ball between two balls in the string, which tightens the whole string. No other actuator can then enter. "If several drawers are pulled at once, the string locks before any drawer opens." Springs at one or both ends take up the end load, and chamfered recesses ease the ball back out.
- **For kagu:** Steel balls are cheap and precise, which helps tolerance compared with printed blocks. A lock can work like D1, with a bolt that fills the end gap.

### D3. DIY cable with slack

From [Steelcase US 3,941,441](https://patents.google.com/patent/US3941441A).

- **Parts and motion:** A flexible cable runs in a segmented guide on the inside wall, with one cam per Drawer level. A catch on each Drawer rotates its cam and takes up the cable slack, and the slack is sized to allow exactly one Drawer.
- **Drawbacks:** Tension needs a slotted adjuster, and there is no inherent lock. Cable stretch is a long-term drift risk, so this is listed for completeness only.

### Other prior art worth a look while drawing

- [US 4,429,930 (Nightingale)](https://patents.google.com/patent/US4429930): cams and slide bars in a side channel with over-center crank arms.
- [US 4,372,632 (Sperry)](https://patents.google.com/patent/US4372632): a vertical pegged bar that locks the drawers until a stabilizer leg is deployed. It is an interesting idea for a mobile cabinet: Drawers only unlock when a foot or brake is down.
- [US 6,109,709 (Waterloo)](https://patents.google.com/patent/US6109709): a tool-chest internal locking bar driven by a key cylinder, catching a leg on each Drawer.
- Kennedy chests advertise a "full-height rear locking mechanism" plus an anti-tip system ([listing](https://techno.my/products/kennedy-28-inch-6-drawer-professional-top-chest-red)). I found no Kennedy drawing.

### F1. Locking front panel (Gerstner)

- **Mechanism:** On Gerstner chests, a solid front panel covers every Drawer front and locks to the case. When it is unlocked, it slides on "a sliding hinge so that it may be stowed beneath the bottom drawer" ([Penn Tool, Gerstner 2613](https://www.penntoolco.com/gerstner-2613-pro-series-wood-chests)). Some models add one independently keyed drawer, which is the same layering idea as a Locked Drawer.
- **Videos:** [front lid removal](https://www.youtube.com/watch?v=eEIb7JoC6a4), [kit chest and front lid assembly](https://www.youtube.com/watch?v=AeGQnNF9Dc8), [tubalcain examining a Gerstner](https://www.youtube.com/watch?v=g4CmGu5e6_c).
- **For kagu:** at 915 mm tall, a stowed panel needs a full-width pocket under the bottom Bay. It is also slow for a busy lab. A roll-up or hinged door variant covers the same ground.

## How Viewing Lid locks coexist with the whole-cabinet lock

**Two independent layers.**

1. **The cabinet layer** (W2, W2+, C1 or D1) acts on Drawer *travel*. A Locked Drawer is an ordinary participant: it carries the same drawer clip, wedge or bracket, it is blocked when the cabinet is locked, and it blocks the others when it is open.
2. **The lid layer** acts only on the *Viewing Lid*, which is hinged to the Drawer box. With the cabinet unlocked, a student can pull a Locked Drawer out and see its contents through the lid but cannot reach them. Staff unlock the lid.

The two layers share nothing mechanically, so neither one can jam the other. The only rule is to keep the lid lock's parts out of the side zone where the lockbar or interlock runs.

**Real precedent: ClickNetherfield "Access" museum drawer units** ([product data sheet](https://www.specifiedby.com/clicknetherfield/access-displays-fittings/ClickNetherfield_Access_Technical_PDS.pdf)). Each display drawer runs on heavy-duty slides and has a glass top that is "locked in position with two Abloy OF400 locks". Separately, "the cabinet can also be fitted with a locking system to prevent drawers being opened" (an Abloy CL291 with secondary mechanical locking), and anti-tilt features are an option. Installations include the Hunterian Museum (Royal College of Surgeons, London), the Ashmolean (Oxford), the Ulster Museum and the Manchester Museum. A used [Polstore 10-drawer museum chest](https://shop.unigreenscheme.co.uk/other-lab-equipment/item-16077-nckeb) (with photos) has the same split: "All the drawers have lockable glass covers," with "drawer glass/case keys" kept separate from the "key to lock the drawers."

**Lid lock options**, all buyable in the same Timberline removable-plug family so keying stays in one system:

- **Compression-mount glass-door lock on the acrylic lid** (Timberline Type 350/360, CB-351 or CB-361). It slips onto the lid's edge with no boring and is fully cushioned, for panels 1/4" to 5/16" thick. Its cam turns under a printed or aluminum strike on the inside of the Drawer front (catalog p. 27). Bore-through versions (Type 300/310) need a 7/8" hole centered 7/8" from the edge, which is riskier in acrylic.
- **Cam lock in the Drawer front** (Timberline CB-080 to CB-099 for 90°, or CB-180/190 for 180°, in 3/4" material with a 16.5 mm hole; catalog pp. 22 to 23). The cam swings over the lid's front edge or into a slot in a strike bonded to the lid. The lid needs no hardware, only a stiff front edge.
- **Push lock** (the ClickNetherfield approach with Abloy OF400; Timberline Type 175 is the sliding-door equivalent). A plunger from the Drawer front engages a hole in the lid's frame.
- **Hasp plus small padlock**, the cheapest option, with the weakest look and key control.
- **Future electronic lock** (out of scope, but a provision): a small solenoid latch behind the Drawer front acting on the same strike as the cam lock. Plan wire routing through the Drawer back and a cable carrier.

**Keying plan to decide:** Timberline plugs are master-keyable with 500+ key changes and can be rekeyed in the field (catalog pp. 3 to 4), so one supplier covers:

- Key **A**: the cabinet gang locks, for lab TAs or for opening and closing the room.
- Key **B**: all Viewing Lids, for staff only.
- Key **M**: a staff master that opens both.

Each of the roughly 4 Cabinets could also get its own A code.

## Provisional recommendation

1. **Cabinet lock and interlock: the CompX Timberline lockbar family, one bar per drawer column on one Carcass side.** Use System 300 (lock plus anti-tip wedges) if a 1" front rail is acceptable. Otherwise use System 150 (side-mounted gang lock) for the lock, combined with System 350 wedges for anti-tip; confirm with CompX that 150 and 350 can share one bar. The appeal is that it is cheap, documented for wood, needs only router and drill press machining, stays inside the 1/2" slide gap, is master-keyable, and has a keyless Regulator path for the future electronic lock.
2. **Fallback: Accuride 3641/3642 plus the 4180-0345-XE kit,** if Timberline's anti-tip parts prove hard to buy or too fussy. Budget roughly $80+ per Drawer and 0.89" side space on one side.
3. **DIY option worth a prototype ticket: D1, the stacked-block channel,** printed and housed in an aluminum channel. It is cheap and fully parametric, and the lock is built in. The risk is the tolerance of the slack budget, plus no known DIY precedent.
4. **Viewing Lids:** 1/4" acrylic or polycarbonate, hinged to the Drawer box, locked by a Timberline compression-mount glass-door lock or a drawer-front cam lock, keyed B under a master.
5. **Not recommended as the primary lock:** W1 (external bar) and F1 (front panel). Both are acceptable as a stopgap or for the instrument variant.

## Implications for kagu

- **Lockbar or interlock zone on one Carcass side per Bay.** Reserve a vertical strip on the inside face of the Carcass side (or Bay divider) near the front, running the full height of the Drawer stack. The Timberline lockbar sits in a routed groove there, and its pins and drawer clips cross the slide gap. Exact groove width, depth and setback still have to come from the CompX application drawings, but expect roughly a 1/2" lockbar groove plus about 1" to 1-1/2" of setback. Slides must not cover it, so either set the slides back or note that the bar runs ahead of the slide's front end. Make `lock_side` (L/R) and `lockbar_setback` parameters.
- **Side space stays at the standard 1/2" (12.7 mm) per side** for Timberline or DIY options, because the DC-500 clip fits in that gap. **Choosing Accuride 3641 changes it to 0.89" (22.6 mm) on the interlock side**, so Drawer box width must take per-side slide clearance as a parameter.
- **Slide spacing minimums:** Timberline System 400 needs at least 7-5/8" between slides (6-1/8" with the DC-410 clip). Accuride rods are (spacing − 2"), which implies at least about 2"+ of spacing. Shallow drawers in the electronics-components stack must respect whichever system is chosen.
- **Lock cylinder location:** reserve a 16.5 mm hole at the top front of the lock-side Carcass side (System 150) **or** a 1" exposed front rail above the top Drawer (System 300 and the Accuride header-rail option). The **Top Interface must not cover it**, and a header rail affects the Carcass front frame design.
- **Locked Drawer geometry:**
  - The Viewing Lid's hinge line and swept volume must sit **forward of the Drawer fronts above** at full extension. Either use 1" over-travel slides on Locked Drawers (Accuride 3641-class), or make the lid at least front-thickness plus clearance (about 25 mm) shorter than the Drawer box at the rear, or put Locked Drawers in the top position.
  - The lid adds lid thickness plus clearance above the tallest Bin to the Drawer's pitch.
  - Keep lid-lock hardware at the center of the Drawer front, away from the lockbar side.
- **Electronic-lock provision:** run the future wiring path to the top of the lockbar (where a Regulator-style actuator or solenoid would drive the whole column) and to the Locked Drawer fronts.
- **Mobile use:** an interlock does not stop Drawers rolling open while the Cabinet is pushed. The whole-cabinet lock (or slides with hold-in detents) does. The Sperry patent's idea is worth considering: unlock only when a caster brake or foot is engaged.
- **Tolerances and jigs:** pin, wedge and rod positions need about ±0.5 mm repeatability (Accuride: ±0.020" on rods; Timberline: the TL-200 marking tool). That argues for a 3D-printed drilling and marking jig per Bay, which fits the map's "consistent holes via 3D-printed drilling jigs" note.

## Open questions surfaced

1. **Keying plan:** who holds key A (cabinet) versus key B (Viewing Lids)? Is one master enough across all ~4 Cabinets, or does each Cabinet get its own A code?
2. **Is a 1" front header rail acceptable** in the Carcass front (it enables System 300 and Accuride header mounting)? Or must the lock live in the side panel or the top Drawer front?
3. **One lock per Cabinet or per column?** With more than one drawer column, a central flexible-shaft drive (Timberline System 500 or Accuride's AC600 cable) or one cylinder per column is needed.
4. **Over-travel slides for Locked Drawers only, or everywhere?** This interacts with the slide-selection ticket.
5. **Should the interlock span the whole Cabinet or each column?** Tip risk is a whole-cabinet property. Two columns each allowing one open Drawer may still tip a 915 mm cabinet on casters. A stability check is needed.
6. **Build a D1 prototype** (printed stacked-block channel) as a risk-reduction ticket before committing to Timberline? It would also settle whether printed parts survive 50k cycles.
7. **Get the CompX application drawings** (B-100 to C-115) and confirm that System 150 and System 350 can share one lockbar.

## Sources

Manufacturer documentation

- Accuride 3641X Heavy-Duty Interlock Slide System: https://www.accuride.com/en-us/products/3641x-heavy-duty-interlock-slide-system
- Accuride 4180-0345-XE Gang Locking System Interface Kit (PDF): https://static.richelieu.com/documents/docsGr/100/855/5/1008555/1395122.pdf
- Accuride 3641/3642 two-drawer kit pricing (Harbor City Supply): https://www.harborcitysupply.com/accuride-3641-3642-interlocking-drawer-system-two-drawer-kit
- Accuride 3641 CAD model (cgtrader): https://www.cgtrader.com/free-3d-models/engineering-parts/accuride/model-3641-1-25-4-mm-over-travel-interlock-feature-allows-only-one-drawer-to-open-at-a-time-loads-up-to-180-lbs-82-kg-per-pair-rail-and-pocket-mount
- Accuride DZ5343 specs (Metrol): https://motioncontrol.metrol.com/accuride-dz5343.html
- Knape & Vogt OEM Toolbox Guide (INTERLOK 8400/8800): https://knapeandvogt.com/sites/default/files/KV_OEM_Toolbox_Guide_FINAL_rev2.pdf
- CompX Timberline catalog (gang locks, anti-tip, cam, glass-door and push locks): https://easykeys.com/PDFS/Timberline_Catalog.pdf
- CompX WD-21A anti-tip wedge: https://compx.com/?p=546963
- CompX TLSN400 anti-tip snapper: https://absupply.net/compx-tlsn400-anti-tip-interlock-system-anti-tip-snapper.aspx
- CompX LB-240 lockbar: https://easykeys.com/products/2276_CompX-Timberline-Lockbar_LB-240 and https://wurthlac.com/product/147675/Timberline-24-Lockbar
- Häfele Matrix Box P central locking (catalog p. 10.56): https://files.hafele.co.uk/CatalogFiles/www/23T10-56.pdf
- Häfele 237.42.109 vertical lock bar: https://store.homedecorhardware.com/hf-237-42-109.html
- item Telescopic Rail Interlock Locking Set 8: https://www.item24.com/en-us/telescopic-rail-interlock-locking-set-8-73333
- ClickNetherfield Access drawer units product data sheet: https://www.specifiedby.com/clicknetherfield/access-displays-fittings/ClickNetherfield_Access_Technical_PDS.pdf
- Gerstner 2613 front panel description (Penn Tool): https://www.penntoolco.com/gerstner-2613-pro-series-wood-chests
- McMaster-Carr locking bars: https://www.mcmaster.com/locking-bars

Patents

- US 6,296,332 B1, Accuride, file interlock system: https://patents.google.com/patent/US6296332
- US 4,960,309, Steelcase, drawer lock and interlock (stacked blocks): https://patents.google.com/patent/US4960309
- US 3,941,441, Steelcase, drawer interlock system (cable): https://patents.google.com/patent/US3941441A
- EP 0 286 199 A1, Engineered Security Products (Lakso), ball-string interlock: https://data.epo.org/publication-server/rest/v1.2/patents/EP0286199NWA1/document.html
- US 4,429,930, Nightingale, interlock for drawers: https://patents.google.com/patent/US4429930
- US 4,372,632, Sperry, slide interlock and cabinet stabilizer: https://patents.google.com/patent/US4372632
- US 6,109,709, Waterloo, tool cabinet locking bar: https://patents.google.com/patent/US6109709

Videos and photos of real examples

- Accuride 5343 interlock drawer slide with optional lock: https://www.youtube.com/watch?v=wSXJFZRK4QA
- Central Locking Bar functional principle: https://www.youtube.com/watch?v=xfcH1SqGnYo
- Hettich assembly, locking system for drawers: https://www.youtube.com/watch?v=G6cfoaB8sRI
- item interlock system install: https://www.youtube.com/watch?v=BGM96ztSWpY
- ABUS file cabinet locking bars: https://www.youtube.com/watch?v=0X_HMILR72Q
- Gerstner front lid removal: https://www.youtube.com/watch?v=eEIb7JoC6a4
- Gerstner kit chest and front lid assembly: https://www.youtube.com/watch?v=AeGQnNF9Dc8
- tubalcain, examining the Gerstner tool box: https://www.youtube.com/watch?v=g4CmGu5e6_c
- Polstore museum chest with lockable glass drawer covers (photos): https://shop.unigreenscheme.co.uk/other-lab-equipment/item-16077-nckeb

Build guides and forums

- Hunker, how to add a lock to a filing cabinet: https://www.hunker.com/13419376/how-to-add-a-lock-to-a-filing-cabinet/
- LumberJocks, one-at-a-time drawers: https://www.lumberjocks.com/threads/one-at-a-time-drawers.266185/
- Garage Journal, how to build a cabinet lock system (no photos): https://www.garagejournal.com/forum/threads/how-to-build-a-cabinet-lock-system.326412/
- Kennedy chest listing (rear locking and anti-tip): https://techno.my/products/kennedy-28-inch-6-drawer-professional-top-chest-red

## Caveats

- Prices marked "unverified" are estimates. Only the LB-240 lockbar and the Accuride 3641/3642 kit had prices I could see.
- The LumberJocks thread content came from a search snippet, because the page itself blocked fetching.
- The Accuride 3641 load rating differs between Accuride (180 lb per pair) and one retailer (100 lb).
- No documented DIY or 3D-printed interlock build was found. The DIY rows rest on patent drawings of production mechanisms.
