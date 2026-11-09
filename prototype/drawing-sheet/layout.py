"""Rough layout sketch for the 2-set instrument Cabinet (throwaway).

Variants: 36"/40" tall × 1/2 drawer columns. Writes a 2×2 front-elevation sheet (PDF/PNG, mm + in)
and an interactive three.js page where drawers (with baseplates and bins) slide open on click.
Placeholder slide/drawer assumptions until the wide-drawer slide research lands.
Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/zerobrew/lib .venv/bin/python layout.py
"""

import base64
import itertools
import json
import os
import struct
import sys
from pathlib import Path
from html import escape as attr_escape
from xml.sax.saxutils import escape

import cairosvg
from build123d import Axis, Box, Color, Compound, Cylinder, Plane, Pos, Rot, export_gltf, fillet, import_step

from printed_parts import SO_BASE_H, SO_CAP_H, drawer_pull, drawer_pull_pocket, standoff_base, standoff_cap

# Side handle: "Simple Handle – 12 Sizes | Handle for M6 Screws" by Emkatech (Printables 1531320), CC BY-NC 4.0.
# STEP frame: feet on y = 0 (+Y away from the panel), length along Z, M6 holes at z = ±90 for the 180 mm size.
SIDE_HANDLE = import_step(str(Path(__file__).parent.parent / "ext-handle" / "STEB-Handle" / "handle-180mm.step"))

OUT = Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)

# --- parameters (mm) -------------------------------------------------------------------
IN = 25.4
W, D, T, TB = 1200.0, 500.0, 18.0, 12.0
CASTER_H, TOP_MODULE = 130.2, 25.0
BAY_CLEAR = 300.0  # one stored set is 279 tall
SET_W = 559.0
GAP, SLIDE, SIDE, BOT = 3.0, 13.0, 12.0, 12.0  # front gap, slide space per side, drawer side, drawer bottom
DRAWER_D = 457.0  # 18" slides
GRID = 42.0
CORNER_R = 50.0  # rounded top-front corner of each side panel (side profile)
LIP = 75.0  # sides and back rise this far above the worktop (fence; back upstand carries a pegboard)
HANDLE_Z, HANDLE_L, STANDOFF = 60.0, 300.0, 50.0  # side handles: below worktop, length, projection
HANDLE_YS = (-150.0, 150.0)  # two handles per side, front and rear, for two-handed steering
BUMPER = 50.0  # rear wall standoffs: projection behind the back
CHOSEN = (40, 600, "spaced")


def pitch(u):
    """Drawer opening height for bins u units tall: bottom 12 + baseplate 5 + bin 7u + lip 4.4 + clearance 4 + gap 3."""
    return BOT + 5 + 7 * u + 4.4 + 4 + GAP


def mm_in(v, digits=1):
    return f'{v:.0f} ({v / IN:.{digits}f}")'


USE = {3: "flat parts", 6: "sensors, boxed boards", 7: "sensors, boxed boards", 10: "stacked boxes, tools"}
MIXES = {  # (height, gap mode) → drawer heights per column, bottom → top
    (36, "spaced"): [[6, 6, 6, 6, 6, 3], [10, 6, 6, 6, 6]],
    (40, "spaced"): [[6] * 7, [10, 10, 6, 6, 6, 6]],
    (36, "7U"): [[6, 6, 6, 6, 6, 3], [10, 7, 7, 7, 6]],
    (40, "7U"): [[6, 6, 6, 6, 6, 7, 7], [10, 10, 7, 7, 7, 7]],
}
MODES = {"spaced": "spare height shared out as taller fronts", "7U": "some 6U drawers become 7U"}
VARIANTS = {(h, d, m): MIXES[(h, m)] for h in (36, 40) for d in (500, 600) for m in MODES}
SLIDE_FOR_DEPTH = {500: 457.0, 600: 559.0}  # 18" / 22" slides


def set_depth(d):
    global D, DRAWER_D, UNITS_D
    D, DRAWER_D = float(d), SLIDE_FOR_DEPTH[d]
    UNITS_D = int((DRAWER_D - 2 * SIDE - 2) // GRID)


def frame(total_in):
    total = total_in * IN
    carcass_h = total - CASTER_H - TOP_MODULE
    z_bay0 = CASTER_H + T
    z_shelf_top = z_bay0 + BAY_CLEAR + T
    z_top_panel = CASTER_H + carcass_h - T
    return dict(total=total, carcass_h=carcass_h, z_bay0=z_bay0, z_shelf_top=z_shelf_top, room=z_top_panel - z_shelf_top)


def column_pitches(height, mix, mode):
    """Opening height per drawer; in "spaced" mode the column's spare height is shared out evenly."""
    p = [pitch(u) for u in mix]
    if mode == "spaced":
        extra = (frame(height)["room"] - sum(p)) / len(p)
        p = [v + extra for v in p]
    return p


def columns(n):
    """x-extents of each drawer column opening (between sides / centre divider)."""
    x0, x1 = -W / 2 + T, W / 2 - T
    return [(x0, x1)] if n == 1 else [(x0, -T / 2), (T / 2, x1)]


def units_across(x0, x1):
    return int((x1 - x0 - 2 * SLIDE - 2 * SIDE - 2) // GRID)


UNITS_D = int((DRAWER_D - 2 * SIDE - 2) // GRID)  # updated per variant by set_depth()

# --- 3D model ----------------------------------------------------------------------------
WOOD, FRONT, INSTR, DARK, TOPC = Color(0xC9A36B), Color(0xE6CFA3), Color(0x4A4F57), Color(0x222222), Color(0x1B1B1B)
BIN_COLORS = [Color(0xD9DDE3), Color(0x6A9FD8), Color(0xF0A040), Color(0xF4F4F0), Color(0x7FBF7F)]
BIN_SIZES = {3: [(2, 1), (1, 1), (2, 2), (1, 2)],
             7: [(3, 2), (1, 1), (2, 1), (2, 2), (1, 1), (3, 2), (2, 1)],
             6: [(3, 2), (1, 1), (2, 1), (2, 2), (1, 1), (3, 2), (2, 1)],  # Pi-box bins (3×2) among sensor bins
             10: [(3, 2), (3, 2), (6, 4), (3, 2), (4, 3)]}  # stacked boxes + Shadow Bins


def box(x0, x1, y0, y1, z0, z1, color, label=""):
    b = Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)
    b.color, b.label = color, label
    return b


def pack(nx, ny, sizes):
    """Shelf-pack bin footprints into an nx × ny grid; returns (ix, iy, w, d)."""
    out, iy, cyc = [], 0, itertools.cycle(sizes)
    while iy < ny:
        ix, row_d = 0, 1
        while ix < nx:
            w, d = next(cyc)
            w, d = min(w, nx - ix), min(d, ny - iy)
            out.append((ix, iy, w, d))
            ix += w
            row_d = max(row_d, d)
        iy += row_d
    return out


def pull_frame(x0, x1, y_front, z_top):
    """Pull mounting frame on the front's top-front edge: +Z out of the face, +Y up."""
    return Plane(origin=((x0 + x1) / 2, y_front, z_top), x_dir=(1, 0, 0), z_dir=(0, -1, 0)).location


def pull_part(x0, x1, y_front, z_top):
    p = pull_frame(x0, x1, y_front, z_top) * drawer_pull()
    p.color, p.label = Color(0xC8CDD3), "pull"
    return p


ACC_LEN, ACC_DEPTH, ACC_DEEP, ACC_IN = 40.0, 16.5, 4.0, 45.0  # accessory pocket in the front's top edge, each end
ACC_INSERT_D, ACC_INSERT_L = 6.0, 10.0  # M4 threaded insert, pointing down into the edge


def front_with_pocket(x0, x1, y0, zb, h):
    f = box(x0 + 2, x1 - 2, y0, y0 + 18, zb, zb + h, FRONT) - pull_frame(x0, x1, y0, zb + h) * drawer_pull_pocket()
    zt = zb + h
    for xc in (x0 + 2 + ACC_IN, x1 - 2 - ACC_IN):  # accessory interface in the top edge, like the pull, each end
        f -= box(xc - ACC_LEN / 2, xc + ACC_LEN / 2, y0 - 1, y0 + ACC_DEPTH, zt - ACC_DEEP, zt + 1, FRONT)
        f -= Pos(xc, y0 + ACC_DEPTH / 2, zt - ACC_DEEP) * Cylinder(ACC_INSERT_D / 2, 2 * ACC_INSERT_L)
    f.color, f.label = FRONT, "front"
    return f


def drawer(name, x0, x1, z, u, opening):
    """Drawer box + baseplate + bins, closed position; front face at y = -D/2."""
    h = opening - GAP
    y0 = -D / 2
    bx0, bx1 = x0 + SLIDE, x1 - SLIDE
    by0, by1 = y0 + 18, y0 + 18 + DRAWER_D
    zb = z + GAP / 2
    side_h = pitch(u) - GAP - 10
    parts = [
        front_with_pocket(x0, x1, y0, zb, h),
        pull_part(x0, x1, y0, zb + h),  # flange flush in the top-edge pocket, lip turns down over the face
        box(bx0, bx0 + SIDE, by0, by1, zb, zb + side_h, WOOD, "side"),
        box(bx1 - SIDE, bx1, by0, by1, zb, zb + side_h, WOOD, "side"),
        box(bx0 + SIDE, bx1 - SIDE, by1 - SIDE, by1, zb, zb + side_h, WOOD, "back"),
        box(bx0 + SIDE, bx1 - SIDE, by0, by1 - SIDE, zb, zb + BOT, WOOD, "bottom"),
    ]
    nx, ny = units_across(x0, x1), UNITS_D
    gx0 = (bx0 + bx1) / 2 - nx * GRID / 2
    gy0 = by0 + 1
    zp = zb + BOT
    parts.append(box(gx0, gx0 + nx * GRID, gy0, gy0 + ny * GRID, zp, zp + 5, Color(0x9AA0A6), "baseplate"))
    for k, (ix, iy, w, d) in enumerate(pack(nx, ny, BIN_SIZES[u])):
        c = DARK if (u >= 10 and w * d >= 12) else BIN_COLORS[(k * 7 + ix) % len(BIN_COLORS)]
        parts.append(box(gx0 + ix * GRID + 0.6, gx0 + (ix + w) * GRID - 0.6, gy0 + iy * GRID + 0.6,
                         gy0 + (iy + d) * GRID - 0.6, zp + 5, zp + 5 + 7 * u, c, "bin"))
    return Compound(children=parts, label=name)


def side_panel(xa, xb, y0, y1, z0, z1, label):
    """Full-height side: rises LIP above the worktop; only the top-front corner is rounded in profile."""
    b = box(xa, xb, y0, y1, z0, z1, WOOD)
    corners = b.edges().filter_by(Axis.X).filter_by(lambda e: e.center().Z > z1 - 1 and e.center().Y < 0)
    b = fillet(corners, CORNER_R)
    b.color, b.label = WOOD, label
    return b


def instrument_set(x0, z0):
    y0 = -D / 2 + 20
    return [box(x0, x0 + 262, y0, y0 + 318, z0, z0 + 112, INSTR, "DG1032Z"),
            box(x0 + 15, x0 + 247, y0, y0 + 291, z0 + 112, z0 + 219, INSTR, "DM3068"),
            box(x0 + 300, x0 + 539, y0, y0 + 430, z0, z0 + 157, INSTR, "DP832A"),
            box(x0 + 330, x0 + 510, y0 + 30, y0 + 392, z0 + 157, z0 + 279, INSTR, "MSO2302A")]


def model(key, height, depth, mode, mixes):
    set_depth(depth)
    f = frame(height)
    x0, x1, y0, y1 = -W / 2, W / 2, -D / 2, D / 2
    zc, ztop = CASTER_H, CASTER_H + f["carcass_h"]
    zl = f["total"] + LIP
    fixed = [side_panel(x0, x0 + T, y0, y1, zc, zl, "A"), side_panel(x1 - T, x1, y0, y1, zc, zl, "B"),
             box(x0 + T, x1 - T, y0, y1 - TB, zc, zc + T, WOOD, "C"),
             box(x0 + T, x1 - T, y0, y1 - TB, f["z_shelf_top"] - T, f["z_shelf_top"], WOOD, "F"),
             box(x0 + T, x1 - T, y0, y1 - TB, ztop - T, ztop, WOOD, "D"),
             box(x0 + T - 9, x1 - T + 9, y1 - TB, y1, zc, zl, WOOD, "E"),
             box(x0 + T, x1 - T, y0, y1 - TB, ztop, ztop + TOP_MODULE, TOPC, "top")]  # stops at the back's face
    if len(mixes) == 2:
        fixed.append(box(-T / 2, T / 2, y0, y1 - TB, f["z_shelf_top"], ztop - T, WOOD, "divider"))
    PETG, TPU = Color(0xA8743F), Color(0x111111)  # wood-coloured PETG/ASA prints, black TPU caps
    zh = f["total"] - HANDLE_Z
    for sx, out in ((x0, -1), (x1, 1)):  # printed side handles, running front-to-back
        for hy in HANDLE_YS:
            placed = Plane(origin=(sx, hy, zh), x_dir=(0, 0, out), z_dir=(0, 1, 0)).location * SIDE_HANDLE
            for solid in placed.solids():  # the STEP carries its own colour per solid; override each one
                solid.color, solid.label = PETG, "handle"
                fixed.append(solid)
    for bx in (x0 + 80, x1 - 80):  # printed wall standoffs: PETG cone + TPU cap, low and high
        for bz in (zc + 60, f["total"] - 120):
            loc = Plane(origin=(bx, y1, bz), x_dir=(1, 0, 0), z_dir=(0, 1, 0)).location
            base, cap = loc * standoff_base(), loc * Pos(0, 0, SO_BASE_H) * standoff_cap()
            base.color, base.label, cap.color, cap.label = PETG, "standoff base", TPU, "standoff cap"
            fixed += [base, cap]
    fixed += instrument_set(x0 + T + 15, f["z_bay0"]) + instrument_set(x0 + T + 15 + SET_W + 15, f["z_bay0"])
    for cx in (x0 + 70, x1 - 70):
        for cy in (y0 + 70, y1 - 70):
            w = Pos(cx, cy, 51) * Rot(90, 0, 0) * Cylinder(51, 32)
            w.color, w.label = DARK, "wheel"
            fixed += [w, box(cx - 46, cx + 46, cy - 32, cy + 32, CASTER_H - 8, CASTER_H, DARK, "plate"),
                      box(cx - 8, cx + 8, cy - 8, cy + 8, 51, CASTER_H - 8, DARK, "fork")]
    drawers = []
    for ci, ((cx0, cx1), mix) in enumerate(zip(columns(len(mixes)), mixes)):
        z = f["z_shelf_top"]
        for i, (u, op) in enumerate(zip(mix, column_pitches(height, mix, mode))):
            drawers.append(drawer(f"drawer-{ci}-{i}", cx0, cx1, z, u, op))
            z += op
    cab = Compound(children=[Compound(children=fixed, label="carcass")] + drawers, label="kagu")
    path = OUT / f"layout_{height}in_{depth}d_{mode}.glb"
    export_gltf(cab, str(path), binary=True)
    return path


# --- 2×2 front-elevation sheet (plain SVG, page mm, y down) ----------------------------------
PAGE_W, PAGE_H = 420.0, 297.0
K = 1 / 10
svg = []


def rect(x, y, w, h, fill="none", stroke="#000", sw=0.3):
    svg.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def line(x0, y0, x1, y1, sw=0.18):
    svg.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="#000" stroke-width="{sw}"/>')


def text(s, x, y, size=2.2, anchor="start", fill="#000", bold=False):
    b = ' font-weight="bold"' if bold else ""
    svg.append(f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" text-anchor="{anchor}" fill="{fill}"{b}>{escape(s)}</text>')


def vdim(x, y_lo, y_hi, label, side=1, size=1.9):
    line(x, y_lo, x, y_hi)
    for yy in (y_lo, y_hi):
        line(x - 1, yy, x + 1, yy)
    if label:
        text(label, x + side * 1.6, (y_lo + y_hi) / 2 + 0.7, size, "start" if side > 0 else "end")


def elevation(key, height, mode, mixes, ox, floor_y):
    f = frame(height)
    px = lambda x: ox + (x + W / 2) * K
    pz = lambda z: floor_y - z * K
    for cx in (-W / 2 + 70, W / 2 - 70):
        svg.append(f'<circle cx="{px(cx):.2f}" cy="{pz(51):.2f}" r="{51 * K:.2f}" fill="#333"/>')
        rect(px(cx) - 4.6, pz(CASTER_H), 9.2, (CASTER_H - 51) * K, "#555", "none")
    line(ox - 8, floor_y, ox + W * K + 8, floor_y, 0.45)
    zc, ztop = CASTER_H, CASTER_H + f["carcass_h"]
    z_fence = f["total"] + LIP
    rect(px(-W / 2 + T), pz(z_fence), (W - 2 * T) * K, LIP * K, "#B8925C", "#000", 0.25)  # back upstand seen behind the top
    for x0 in (-W / 2, W / 2 - T):
        rect(px(x0), pz(z_fence), T * K, (z_fence - zc) * K, "#C9A36B", "#000", 0.25)
    for sx, sgn in ((-W / 2, -1), (W / 2, 1)):
        x_out = px(sx) + sgn * STANDOFF * K
        rect(min(px(sx), x_out), pz(f["total"] - HANDLE_Z) - 1.1, STANDOFF * K, 2.2, "#B8BEC6", "#555", 0.2)
    for z0 in (zc, f["z_shelf_top"] - T, ztop - T):
        rect(px(-W / 2 + T), pz(z0 + T), (W - 2 * T) * K, T * K, "#C9A36B", "#000", 0.25)
    if len(mixes) == 2:
        rect(px(-T / 2), pz(ztop - T), T * K, (ztop - T - f["z_shelf_top"]) * K, "#C9A36B", "#000", 0.25)
    rect(px(-W / 2 + T), pz(ztop + TOP_MODULE), (W - 2 * T) * K, TOP_MODULE * K, "#1B1B1B", "#000", 0.25)
    for sx in (-W / 2 + T + 15, -W / 2 + T + 15 + SET_W + 15):
        for (a, b, zl, zh, lbl) in [(0, 262, 0, 112, "DG"), (15, 247, 112, 219, "DM"), (300, 539, 0, 157, "DP"), (330, 510, 157, 279, "MSO")]:
            rect(px(sx + a), pz(f["z_bay0"] + zh), (b - a) * K, (zh - zl) * K, "#4A4F57", "#222", 0.2)
            text(lbl, px(sx + (a + b) / 2), pz(f["z_bay0"] + (zl + zh) / 2) + 0.7, 1.8, "middle", "#fff")
    count = 0
    for ci, ((cx0, cx1), mix) in enumerate(zip(columns(len(mixes)), mixes)):
        z = f["z_shelf_top"]
        nx = units_across(cx0, cx1)
        for u, op in zip(mix, column_pitches(height, mix, mode)):
            h = op - GAP
            rect(px(cx0 + 2), pz(z + GAP / 2 + h), (cx1 - cx0 - 4) * K, h * K, "#E6CFA3", "#000", 0.25)
            rect(px((cx0 + cx1) / 2 - 40), pz(z + GAP / 2 + h / 2 + 5), 8, 1, "#222", "none")
            text(f"{u}U {USE[u]}", px(cx0 + 12), pz(z + GAP / 2 + h / 2) + 0.7, 1.7)
            text(f"{nx}×10 / {nx}×12", px(cx1 - 12), pz(z + GAP / 2 + h / 2) + 0.7, 1.6, "end")
            side = 1 if ci == len(mixes) - 1 else -1
            xd = px(W / 2) + 4 if side > 0 else px(-W / 2) - 4
            vdim(xd, pz(z), pz(z + op), f'{op:.0f} ({op / IN:.1f}")', side, 1.6)
            z += op
            count += 1
    xl = px(-W / 2) - (26 if len(mixes) == 2 else 6)
    vdim(xl, pz(0), pz(f["total"]), "worktop " + mm_in(f["total"], 0), -1)
    vdim(xl - 3, pz(0), pz(z_fence), "", -1)
    text("fence " + mm_in(z_fence, 1), xl - 4.6, pz(z_fence) + 2.5, 1.9, "end")
    text(f"bay {mm_in(BAY_CLEAR)}", xl + 2, pz(f["z_bay0"] + BAY_CLEAR / 2) + 0.7, 1.7, "start")
    line(px(-W / 2), floor_y + 5, px(W / 2), floor_y + 5)
    text(mm_in(W), px(0), floor_y + 4.2, 2.0, "middle")
    text(f"{key.upper()} — {count} DRAWERS", px(0), pz(f["total"] + LIP) - 9, 3.4, "middle", bold=True)
    widths = " + ".join(f"{units_across(*c)}" for c in columns(len(mixes)))
    text(f"{MODES[mode]} · drawers {widths} units wide × 10 deep (500) / 12 deep (600)", px(0), pz(f["total"] + LIP) - 4.5, 2.0, "middle")


def side_view(height, depth, ox, floor_y):
    """Right-side elevation: front on the left (third-angle), rounded top corners."""
    f = frame(height)
    py = lambda y: ox + (y + depth / 2) * K
    pz = lambda z: floor_y - z * K
    r = CORNER_R * K
    x0, x1, zt, zb = py(-depth / 2), py(depth / 2), pz(f["total"] + LIP), pz(CASTER_H)
    svg.append(f'<path d="M{x0:.2f},{zb:.2f} L{x0:.2f},{zt + r:.2f} A{r:.2f},{r:.2f} 0 0 1 {x0 + r:.2f},{zt:.2f} '
               f'L{x1:.2f},{zt:.2f} L{x1:.2f},{zb:.2f} Z" fill="#C9A36B" stroke="#000" stroke-width="0.3"/>')
    zw = pz(f["total"])
    svg.append(f'<line x1="{x0:.2f}" y1="{zw:.2f}" x2="{x1:.2f}" y2="{zw:.2f}" stroke="#000" stroke-width="0.25" stroke-dasharray="1.2,0.8"/>')
    text("worktop (between the sides)", x0 + 6, zw - 1.2, 1.8)
    hz = pz(f["total"] - HANDLE_Z)
    for hy in HANDLE_YS:
        rect(py(hy - 100), hz - 1.6, 200 * K, 3.2, "#A8743F", "#555", 0.25)
    text("2 printed M6 handles per side, 180 mm centres (Emkatech, CC BY-NC)", py(0), hz + 5, 1.8, "middle")
    for bz in (CASTER_H + 60, f["total"] - 120):
        rect(x1, pz(bz) - 2.5, BUMPER * K, 5, "#111", "none")
    text(f"printed wall standoffs {SO_BASE_H + SO_CAP_H:.0f} ({(SO_BASE_H + SO_CAP_H) / IN:.0f}\"): PETG cone + TPU cap", x1 + BUMPER * K + 1, pz(CASTER_H + 60) - 4, 1.8)
    for cy in (-depth / 2 + 70, depth / 2 - 70):
        svg.append(f'<circle cx="{py(cy):.2f}" cy="{pz(51):.2f}" r="{51 * K:.2f}" fill="#333"/>')
        rect(py(cy) - 3.2, pz(CASTER_H), 6.4, (CASTER_H - 51) * K, "#555", "none")
    line(x0 - 8, floor_y, x1 + 8, floor_y, 0.45)
    line(x0, floor_y + 5, x1, floor_y + 5)
    text(mm_in(depth), (x0 + x1) / 2, floor_y + 4.2, 2.0, "middle")
    vdim(x1 + 14, pz(0), pz(f["total"]), "worktop " + mm_in(f["total"], 0), 1)
    vdim(x1 + 14, pz(f["total"]), zt, f"fence +{LIP:.0f} ({LIP / IN:.0f}\")", 1)
    line(x0 + r * 0.29, zt + r * 0.29, x0 - 6, zt - 6, 0.18)
    text(f"R{CORNER_R:.0f} ({CORNER_R / IN:.1f}\")", x0 - 6.5, zt - 6.5, 1.9, "end")
    text("FRONT", x0 + 2, zb - 2, 1.8)
    text("RIGHT SIDE", (x0 + x1) / 2, zt - 9, 3.4, "middle", bold=True)
    text("BACK", x1 - 2, zb - 2, 1.8, "end")
    text("sides + back rise above the worktop; only the front corner is rounded", (x0 + x1) / 2, zt - 4.5, 2.0, "middle")


rect(10, 10, 400, 277, sw=0.5)
text('KAGU · INSTRUMENT CABINET — CHOSEN LAYOUT: 40" TALL · 600 mm DEEP · SPACED (1:8)', 16, 19, 3.8, bold=True)
text('Two Rigol sets side by side in the low bay; drawers above. Dimensions in mm (inches). Drawer heights in gridfinity units (U = 7 mm).', 16, 24, 2.3)
K = 1 / 8
h, d, m = CHOSEN
elevation(f'{h}" · {m} — front', h, m, MIXES[(h, m)], 62, 244)
side_view(h, d, 262, 244)
K = 1 / 10
glbs = {key: model(key, h, d, m, mixes) for key, mixes in VARIANTS.items() for (h, d, m) in [key]}
notes = [
    "Pitch per drawer = bottom 12 + baseplate 5 + bin 7·U + lip 4.4 + clearance 4 + gap 3:  3U ≈ 49 (1.9\") · 4U ≈ 56 (2.2\") · 6U ≈ 70 (2.8\") · 10U ≈ 98 (3.9\").",
    "6U: sensors (several per bin) and boxed boards one layer deep (3×2 bins, e.g. Raspberry Pi 5 boxes). 10U: boxed boards stacked two high, hand tools in Shadow Bins.",
    "Depth: 500 mm (19.7\") → 18\" slides, drawers 12 × 10 units; 600 mm (23.6\") → 22\" slides, 12 × 12 units (+20%). Drawers 12 units (21\") wide on standard 1/2\" slides.",
]
for i, n in enumerate(notes):
    text(n, 16, 276 + i * 3.6, 1.9)
page = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{PAGE_W}mm" height="{PAGE_H}mm" viewBox="0 0 {PAGE_W} {PAGE_H}" '
        f'font-family="Arial, Helvetica, sans-serif"><rect width="100%" height="100%" fill="#fff"/>' + "\n".join(svg) + "</svg>")
(OUT / "layout.svg").write_text(page)
cairosvg.svg2pdf(url=str(OUT / "layout.svg"), write_to=str(OUT / "layout.pdf"))
cairosvg.svg2png(url=str(OUT / "layout.svg"), write_to=str(OUT / "layout.png"), output_width=2400)


# --- interactive three.js page ----------------------------------------------------------------
def glb_node_names(path):
    data = path.read_bytes()
    n = struct.unpack_from("<I", data, 12)[0]
    return [nd.get("name", "") for nd in json.loads(data[20:20 + n])["nodes"]]


print("glb drawer nodes:", [n for n in glb_node_names(next(iter(glbs.values()))) if n.startswith("drawer")][:4])
pick = dict(zip("hdm", CHOSEN))
sel = lambda name, items: f'<select id="{name}">' + "".join(
    f'<option value="{v}"{" selected" if v == pick[name] else ""}>{attr_escape(t)}</option>' for v, t in items) + "</select>"
opts = (sel("h", [(36, '36" tall'), (40, '40" tall')]) + sel("d", [(500, '500 mm (19.7") deep'), (600, '600 mm (23.6") deep')])
        + sel("m", [(m, f"{m}: {desc}") for m, desc in MODES.items()]))
html = """<!doctype html><html><head><meta charset="utf-8"><title>Kagu layout 3D</title>
<style>body{margin:0;font-family:Arial,sans-serif;background:#eef0f2;overflow:hidden}
header{position:absolute;top:0;left:0;right:0;padding:10px 14px;display:flex;gap:10px;align-items:center;background:#fff;border-bottom:1px solid #ccc;z-index:2}
button,select{padding:5px 10px;border:1px solid #333;background:#fff;cursor:pointer;font-size:14px}#hint{color:#666;font-size:13px}
canvas{display:block}</style>
<script type="importmap">{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"}}</script>
</head><body><header><b>Kagu instrument Cabinet</b>OPTS
<button id="openall">Open all</button><button id="closeall">Close all</button>
<span id="hint">click a drawer to open/close · drag to rotate · scroll to zoom</span></header>
<pre id="err" style="position:absolute;top:56px;left:14px;color:#b00;background:#fff;z-index:3;white-space:pre-wrap;max-width:80vw"></pre>
<script type="module">
import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {RoomEnvironment} from 'three/addons/environments/RoomEnvironment.js';
const showErr = e => { document.getElementById('err').textContent = 'Error: ' + (e && e.stack || e); console.error(e); };
addEventListener('error', e => showErr(e.error || e.message));

const renderer = new THREE.WebGLRenderer({antialias:true}); renderer.setPixelRatio(devicePixelRatio);
renderer.setSize(innerWidth, innerHeight); document.body.appendChild(renderer.domElement);
const scene = new THREE.Scene(); scene.background = new THREE.Color(0xeef0f2);
scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture;  // even light on every side
scene.add(new THREE.HemisphereLight(0xffffff, 0x888888, 0.8));
for (const [x, y, z] of [[2, 4, 3], [-2, 3, -3]]) { const l = new THREE.DirectionalLight(0xffffff, 0.9); l.position.set(x, y, z); scene.add(l); }
const camera = new THREE.PerspectiveCamera(35, innerWidth/innerHeight, 0.001, 100);
const controls = new OrbitControls(camera, renderer.domElement);
let root = null, drawers = [];
const loader = new GLTFLoader();
async function load(){
  const v = id => document.getElementById(id).value;
  const buf = await fetch(`layout_${v('h')}in_${v('d')}d_${v('m')}.glb`).then(r => { if (!r.ok) throw new Error(r.status + ' ' + r.url); return r.arrayBuffer(); }).catch(showErr);
  if (!buf) return;
  if (root) scene.remove(root);
  loader.parse(buf, '', g => { try {
    root = g.scene; scene.add(root); root.updateMatrixWorld(true); drawers = [];
    root.traverse(o => { if (o.name && o.name.startsWith('drawer')) drawers.push(o); });
    for (const o of drawers) {
      // slide direction = from the drawer's centre toward its front panel, in the parent's frame
      // three.js de-duplicates node names on load (front, front_1, ...), so match by prefix
      const box = new THREE.Box3().setFromObject(o), front = o.children.find(m => m.name.startsWith('front'));
      const c = box.getCenter(new THREE.Vector3()), fc = new THREE.Box3().setFromObject(front).getCenter(new THREE.Vector3());
      const dir = fc.clone().sub(c); dir.y = 0; dir.normalize();
      const size = box.getSize(new THREE.Vector3());
      const travel = (Math.abs(dir.x) * size.x + Math.abs(dir.z) * size.z) * 0.96;  // full-extension slides: the whole box clears the Carcass
      const p0 = o.parent.worldToLocal(c.clone()), p1 = o.parent.worldToLocal(c.clone().addScaledVector(dir, travel));
      o.userData = {home: o.position.clone(), step: p1.sub(p0), t: 0, target: 0};
      o.traverse(m => { if (m !== o) m.userData.drawer = o; });
    }
    const box = new THREE.Box3().setFromObject(root), size = box.getSize(new THREE.Vector3()), ctr = box.getCenter(new THREE.Vector3());
    controls.target.copy(ctr); const d = size.length() * 1.2;
    camera.near = d / 1000; camera.far = d * 20;
    camera.position.set(ctr.x + d*0.45, ctr.y + d*0.40, ctr.z + d*0.80); camera.updateProjectionMatrix(); controls.update();
  } catch (e) { showErr(e); } }, showErr);
}
const ray = new THREE.Raycaster(), mouse = new THREE.Vector2(); let down = null;
renderer.domElement.addEventListener('pointerdown', e => down = [e.clientX, e.clientY]);
renderer.domElement.addEventListener('pointerup', e => {
  if (!down || Math.hypot(e.clientX-down[0], e.clientY-down[1]) > 4) return;
  mouse.set(e.clientX/innerWidth*2-1, -e.clientY/innerHeight*2+1); ray.setFromCamera(mouse, camera);
  const hit = ray.intersectObjects(drawers, true)[0];
  if (hit) { let o = hit.object; while (o && !drawers.includes(o)) o = o.parent; if (o) o.userData.target = o.userData.target ? 0 : 1; }
});
for (const id of ['h', 'd', 'm']) document.getElementById(id).onchange = load;
document.getElementById('openall').onclick = () => drawers.forEach(d => d.userData.target = 1);
document.getElementById('closeall').onclick = () => drawers.forEach(d => d.userData.target = 0);
addEventListener('resize', () => { camera.aspect = innerWidth/innerHeight; camera.updateProjectionMatrix(); renderer.setSize(innerWidth, innerHeight); });
(function tick(){ requestAnimationFrame(tick);
  for (const d of drawers) { const u = d.userData; u.t += (u.target - u.t) * 0.12; d.position.copy(u.home).addScaledVector(u.step, u.t); }
  controls.update(); renderer.render(scene, camera); })();
load();
</script></body></html>"""
html = html.replace("OPTS", opts)
(OUT / "layout_3d.html").write_text(html)
for (h, d, m), mixes in VARIANTS.items():
    if d == 500:
        print(h, m, "room", round(frame(h)["room"]), "columns end at", [round(sum(column_pitches(h, mx, m))) for mx in mixes])
sys.stdout.flush()
os._exit(0)
