"""Prototype A3 shop-drawing set for kagu (throwaway; informs the CAD toolchain ticket).

Placeholder Carcass dimensions. Sheet 1 = assembly, sheet 2 = part drawing of side A.
Writes out/carcass_set.pdf (vector), per-sheet SVGs, PNG previews and carcass.glb.
Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/zerobrew/lib .venv/bin/python sheet.py
"""

import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import cairosvg
import qrcode
from build123d import (
    Align,
    Axis,
    Box,
    Circle,
    Compound,
    Cone,
    Cylinder,
    Draft,
    Edge,
    ExportSVG,
    ExtensionLine,
    Keep,
    LineType,
    Location,
    Plane,
    Pos,
    Rectangle,
    Rot,
    FontStyle,
    Text,
    TextAlign,
    Unit,
    Vector,
    Vertex,
    export_gltf,
)
from xml.sax.saxutils import escape

from pypdf import PdfWriter

OUT = Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)

# --- model parameters (placeholder, mm) --------------------------------------------
W, D, H = 600.0, 500.0, 785.0  # Carcass outer
T = 18.0  # 3/4" ply; measured thickness is a parameter
TB = 12.0  # 1/2" back
JD = 6.0  # dado / rabbet depth into the sides
BR = 9.0  # back rabbet depth into the sides
SHELF_Z = 310.0  # top face of the instrument-bay shelf
HOLE_Y = [40.0, 140.0, 240.0, 340.0, 440.0]  # Confirmat positions from the front edge
CF_SHANK, CF_HEAD, CF_PILOT, CF_PILOT_DP = 7.0, 10.0, 5.0, 45.0  # Confirmat 7x50
URL = "https://uf-cpe-design-lab.github.io/kagu/3d/carcass/"

PANEL_W = W - 2 * T + 2 * JD  # C, D, F run into the joints
PANEL_D = D - TB
ROWS_Z = {"C": T / 2, "F": SHELF_Z - T / 2, "D": H - T / 2}  # hole row per joint


def box(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)


def side(sign):
    """Side panel; sign=-1 is A (left), +1 is B (right). Joints are cut from the inside face."""
    outer = sign * W / 2
    inner = sign * (W / 2 - T)
    xo, xi = sorted((outer, inner))
    s = box(xo, xi, -D / 2, D / 2, 0, H)
    cut = lambda depth: sorted((inner, inner + sign * depth))
    x0, x1 = cut(JD)
    s -= box(x0, x1, -D / 2 - 1, D / 2 + 1, -1, T)  # bottom rabbet
    s -= box(x0, x1, -D / 2 - 1, D / 2 + 1, SHELF_Z - T, SHELF_Z)  # shelf dado
    s -= box(x0, x1, -D / 2 - 1, D / 2 + 1, H - T, H + 1)  # top rabbet
    b0, b1 = cut(BR)
    s -= box(b0, b1, D / 2 - TB, D / 2 + 1, -1, H + 1)  # back rabbet
    for z in ROWS_Z.values():
        for yy in HOLE_Y:
            p = Vector(outer, -D / 2 + yy, z)
            rot = Rot(0, -90 * sign, 0)
            s -= Pos(p) * rot * Pos(0, 0, -1) * Cylinder(CF_SHANK / 2, T - JD + 2, align=(Align.CENTER, Align.CENTER, Align.MIN))
            s -= Pos(p) * rot * Pos(0, 0, -0.01) * Cone(CF_HEAD / 2 + 0.01, CF_SHANK / 2, (CF_HEAD - CF_SHANK) / 2 + 0.01, align=(Align.CENTER, Align.CENTER, Align.MIN))
    return s


def shelf_panel(z_top):
    p = box(-PANEL_W / 2, PANEL_W / 2, -D / 2, -D / 2 + PANEL_D, z_top - T, z_top)
    for sign in (-1, 1):
        for yy in HOLE_Y:
            at = Vector(sign * PANEL_W / 2, -D / 2 + yy, z_top - T / 2)
            p -= Pos(at) * Rot(0, -90 * sign, 0) * Pos(0, 0, -0.01) * Cylinder(CF_PILOT / 2, CF_PILOT_DP, align=(Align.CENTER, Align.CENTER, Align.MIN))
    return p


@dataclass
class Part:
    label: str
    name: str
    solid: object
    explode: tuple
    material: str
    size: tuple

    def placed(self, exploded=False):
        s = self.solid.moved(Location(self.explode)) if exploded else self.solid
        s.label = self.label
        return s


parts = [
    Part("A", "Side, left", side(-1), (-170, 0, 0), "18 ply", (H, D, T)),
    Part("B", "Side, right", side(1), (170, 0, 0), "18 ply", (H, D, T)),
    Part("C", "Bottom", shelf_panel(T), (0, 0, -150), "18 ply", (PANEL_W, PANEL_D, T)),
    Part("D", "Top", shelf_panel(H), (0, 0, 170), "18 ply", (PANEL_W, PANEL_D, T)),
    Part("E", "Back", box(-(W / 2 - T + BR), W / 2 - T + BR, D / 2 - TB, D / 2, 0, H), (0, 320, 560), "12 ply", (H, W - 2 * (T - BR), TB)),
    Part("F", "Shelf, instrument bay", shelf_panel(SHELF_Z), (0, -280, 0), "18 ply", (PANEL_W, PANEL_D, T)),
]
assembled = Compound(children=[p.placed() for p in parts])
exploded = Compound(children=[p.placed(True) for p in parts])
export_gltf(assembled, str(OUT / "carcass.glb"), binary=True)

HARDWARE = [
    ("H1", "Confirmat screw 7x50 (Hafele 264.42.193 or eq.)", 3 * 2 * len(HOLE_Y), "Step drill Ø5/Ø7 + csk"),
    ("H2", "Pan-head screw 4x16, back to C/D/F", 18, "Pilot Ø2.5"),
]

# --- sheet machinery ---------------------------------------------------------------------
PAGE_W, PAGE_H, M = 420.0, 297.0, 10.0  # A3 landscape
FONT = 3.0
SCALES = [1, 2, 5, 8, 10, 15, 20, 25]
DRAFT = Draft(font_size=FONT, arrow_length=2.5, line_width=0.18, unit=Unit.MM,
              display_units=False, decimal_precision=0, pad_around_text=1.0, extension_gap=1.5)
RED = (190, 20, 20)


def on_any(edge, edges, tol=0.05):
    mid = Vertex(*edge.position_at(0.5))
    return any(mid.distance_to(e) < tol for e in edges)


def section(solids, plane, crop):
    """Cut each solid by plane (keep the far side) and crop; parts stay separate for hatching."""
    out = []
    for so in solids:
        piece = so.split(plane, keep=Keep.TOP)
        piece = Compound(children=piece) if isinstance(piece, list) else piece
        c = piece & crop
        for q in c if isinstance(c, list) else [c]:
            if q is not None and q.volume > 1e-6:
                q.label = so.label
                out.append(q)
    return Compound(children=out)


def fit_scale(w, h, box_w, box_h, scales=SCALES):
    return next((s for s in scales if w / s <= box_w and h / s <= box_h), scales[-1])


class View:
    """An orthographic/axonometric projection placed on paper at a fixed scale."""

    def __init__(self, sheet, shape, origin, up, look, region, scales=SCALES, hidden=True, anchor="center"):
        self.sheet, self.origin, self.up, self.look = sheet, origin, up, look
        vis, hid = shape.project_to_viewport(origin, up, look_at=look)
        vis = list(vis)
        hid = [h for h in hid if not on_any(h, vis)] if hidden else []
        b = Compound(children=vis).bounding_box()
        rx0, ry0, rx1, ry1 = region
        self.scale = fit_scale(b.size.X, b.size.Y, rx1 - rx0, ry1 - ry0, scales)
        self.k = 1 / self.scale
        w, h = b.size.X * self.k, b.size.Y * self.k
        px = rx0 + (rx1 - rx0 - w) / 2
        py = ry0 + (ry1 - ry0 - h) / 2 if anchor == "center" else ry0
        self.dx, self.dy = px - b.min.X * self.k, py - b.min.Y * self.k
        self.box = (px, py, px + w, py + h)
        self._vis = vis
        sheet.add("visible", self.place(vis))
        sheet.add("hidden", self.place(hid))

    def place(self, edges):
        return [e.scale(self.k).moved(Location((self.dx, self.dy))) for e in edges]

    def pt(self, p3):
        e = Edge.make_line(p3, Vector(p3) + Vector(0.001, 0.001, 0.001))
        vis, hid = Compound(children=[e]).project_to_viewport(self.origin, self.up, look_at=self.look)
        q = (list(vis) + list(hid))[0].position_at(0)
        return Vector(q.X * self.k + self.dx, q.Y * self.k + self.dy)

    def own_edges(self, shape_without):
        """Visible edges that exist only because of the part missing from shape_without."""
        ovis, _ = shape_without.project_to_viewport(self.origin, self.up, look_at=self.look)
        return [e for e in self._vis if not on_any(e, list(ovis))]

    def tag_sections(self, sect, on_plane, r=3.2, gap=6.0):
        """Part Label balloon per sectioned part, leader to the point deepest inside its cut face.
        The balloon goes at the nearest spot around the view that is clear of dimensions,
        notes and earlier balloons."""
        x0, y0, x1, y1 = self.box
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        hx, hy = (x1 - x0) / 2 + gap + r, (y1 - y0) / 2 + gap + r
        near = lambda b: b[2] > x0 - 40 and b[0] < x1 + 40 and b[3] > y0 - 40 and b[1] < y1 + 40
        busy = [(x0, y0, x1, y1)]
        for layer in ("dims", "label"):
            for sh in self.sheet.layers[layer]:
                bb = sh.bounding_box()
                busy.append((bb.min.X - 0.8, bb.min.Y - 0.8, bb.max.X + 0.8, bb.max.Y + 0.8))
        for txt, tx, ty, size, anchor, *_ in self.sheet.texts:
            w = 0.55 * size * len(txt)
            left = {"start": tx, "middle": tx - w / 2, "end": tx - w}[anchor]
            busy.append((left - 0.8, ty - 0.3 * size, left + w + 0.8, ty + size))
        busy = [b for b in busy if near(b)]
        hits = lambda bx, by: sum(bx + r > b[0] and bx - r < b[2] and by + r > b[1] and by - r < b[3] for b in busy)

        def crosses(ax, ay, bx, by, boxes):
            """How many boxes the leader passes through, ignoring any box it starts inside."""
            pts = [(ax + (bx - ax) * i / 20, ay + (by - ay) * i / 20) for i in range(2, 19)]
            inside = lambda b, px, py: b[0] < px < b[2] and b[1] < py < b[3]
            return sum(any(inside(b, px, py) for px, py in pts) for b in boxes if not inside(b, ax, ay))

        cut_boxes = {}  # 2D extent of each part's cut face, so leaders avoid crossing other parts
        for piece in sect.children:
            fs = [f for f in piece.faces() if on_plane(f)]
            if fs:
                ps = [self.pt(v) for f in fs for v in f.vertices()]
                cut_boxes[id(piece)] = (min(q.X for q in ps), min(q.Y for q in ps), max(q.X for q in ps), max(q.Y for q in ps))
        low = y0
        for piece in sect.children:
            faces = [f for f in piece.faces() if on_plane(f)]
            if not faces:
                continue
            f = max(faces, key=lambda f: f.area)
            # the point deepest inside the material, so the dot never lands in a hole or on an edge
            bb, rim = f.bounding_box(), Compound(children=f.edges())
            grid = [bb.min + Vector(bb.size.X * i, bb.size.Y * j, bb.size.Z * k) / 12
                    for i in range(1, 12) for j in range(1, 12) for k in range(1, 12)
                    if (bb.size.X > 1e-6 or i == 1) and (bb.size.Y > 1e-6 or j == 1) and (bb.size.Z > 1e-6 or k == 1)]
            grid = [g for g in grid if f.is_inside(g)] or [f.center()]
            mid = f.center()  # ties (thin strips) resolve toward the middle of the part
            target = max(grid, key=lambda g: (round(Vertex(*g).distance_to(rim), 1), -(g - mid).length))
            a = self.pt(target)
            spots = []
            for deg in range(0, 360, 10):
                v = Vector(1, 0).rotate(Axis.Z, deg)
                for extra in (0, 4, 8):  # step further out if every close spot is taken
                    t = min((hx + extra) / abs(v.X) if abs(v.X) > 1e-6 else 1e9,
                            (hy + extra) / abs(v.Y) if abs(v.Y) > 1e-6 else 1e9)
                    bx, by = cx + v.X * t, cy + v.Y * t
                    others = [b for k, b in cut_boxes.items() if k != id(piece)]
                    cost = (hits(bx, by) * 1000 + crosses(a.X, a.Y, bx, by, others) * 300
                            + crosses(a.X, a.Y, bx, by, busy[1:]) * 60 + Vector(bx - a.X, by - a.Y).length)
                    spots.append((cost, bx, by))
            _, bx, by = min(spots)
            self.sheet.balloon(piece.label, (a.X, a.Y), (bx, by), r=r)
            busy.append((bx - r - 1, by - r - 1, bx + r + 1, by + r + 1))
            low = min(low, by - r)
        return low

    def hatch(self, faces, spacing=2.0, angles=None):
        """45° section hatching on planar cut faces (spacing in paper mm)."""
        for i, f in enumerate(faces):
            ang = (angles or [45, -45])[i % 2]
            n = f.normal_at()
            pl = Plane(origin=f.center(), z_dir=n)
            bb = f.bounding_box()
            r = bb.diagonal
            step = spacing * self.scale
            lines = []
            j = -r
            while j <= r:
                a = pl.from_local_coords((-r, j))
                b = pl.from_local_coords((r, j))
                ln = Edge.make_line(a, b).rotate(Axis(f.center(), n), ang)
                lines.extend(f.intersect(ln) or [])
                j += step
            if lines:
                v, h = Compound(children=lines).project_to_viewport(self.origin, self.up, look_at=self.look)
                self.sheet.add("hatch", self.place(list(v) + list(h)))


class Sheet:
    LAYERS = ["page", "frame", "visible", "hidden", "hatch", "thin", "dims", "text", "label", "qr", "bar", "invert"]

    def __init__(self, number, total, title, subtitle, drawing_no, scale_txt):
        self.layers = {k: [] for k in self.LAYERS}
        self.texts = []  # real SVG text: selectable in the PDF and far faster than glyph outlines
        self.rect(0, 0, PAGE_W, PAGE_H, "page")
        self.rect(M, M, PAGE_W - M, PAGE_H - M, "frame")
        self.title_block(number, total, title, subtitle, drawing_no, scale_txt)

    def add(self, layer, shapes):
        self.layers[layer].extend(shapes if isinstance(shapes, list) else [shapes])

    COLORS = {"text": (0, 0, 0), "label": RED, "invert": (255, 255, 255)}

    def put(self, s, x, y, size, anchor="start", base="baseline", color=(0, 0, 0), bold=False, rotation=0):
        """Place text with its baseline (or centre/top) at (x, y) in page mm."""
        drop = {"baseline": 0.0, "center": 0.36, "top": 0.72}[base] * size
        self.texts.append((s, x, y - drop, size, anchor, color, bold, rotation))

    def text(self, s, x, y, size=FONT, align=(Align.MIN, Align.MIN), layer="text", rotation=0, bold=False):
        anchor = {Align.MIN: "start", Align.CENTER: "middle", Align.MAX: "end"}[align[0]]
        base = {Align.MIN: "baseline", Align.CENTER: "center", Align.MAX: "top"}[align[1]]
        self.put(s, x, y, size, anchor, base, self.COLORS[layer], bold, rotation)

    def rect(self, x0, y0, x1, y1, layer="thin"):
        pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]
        self.add(layer, [Edge.make_line(a, b) for a, b in zip(pts, pts[1:])])

    def line(self, a, b, layer="thin"):
        self.add(layer, Edge.make_line(a, b))

    def dim(self, p0, p1, offset, value):
        self.add("dims", ExtensionLine(border=[p0, p1], offset=offset, draft=DRAFT, label=f"{value:g}"))

    def leader(self, at, to, lines, layer="text", size=2.6):
        """Note with a leader: arrow-dot at `at`, text block starting at `to`."""
        self.line(at, to, "thin")
        self.add("dims", Pos(*at) * Circle(0.5))
        right = to[0] >= at[0]
        self.line(to, (to[0] + (14 if right else -14), to[1]), "thin")
        for i, s in enumerate(lines):
            self.text(s, to[0] + (1 if right else -1), to[1] + 1 - i * (size + 1.2), size,
                      (Align.MIN if right else Align.MAX, Align.MIN), layer)

    def balloon(self, letter, at, center, r=4.2, layer="label"):
        self.add(layer, Pos(*center) * (Circle(r) - Circle(r - 0.35)))
        self.put(letter, *center, r, "middle", "center", RED)
        d = (Vector(*at) - Vector(*center)).normalized()
        self.add(layer, Edge.make_line(Vector(*center) + d * r, at))
        self.add(layer, Pos(*at) * Circle(0.6))

    def steps(self, x0, y1, width, title, items, size=2.7):
        """Numbered instruction panel: dark title bar, step badges, wrapped text with a hanging
        indent. Part Labels, hardware IDs and jig IDs are highlighted in red."""
        key = re.compile(r"^(?:[A-F]|H\d|J\d)$")
        bar_h, lead, indent, gap = 6.5, size * 1.55, 9.0, 1.6
        self.add("bar", Pos(x0 + width / 2, y1 - bar_h / 2) * Rectangle(width, bar_h))
        self.put(title, x0 + 2.5, y1 - bar_h / 2, 3.0, "start", "center", (255, 255, 255), bold=True)
        space = size * 0.45
        y = y1 - bar_h - gap - size
        for n, item in enumerate(items, 1):
            self.add("bar", Pos(x0 + 4, y + size * 0.36) * Circle(2.3))
            self.put(str(n), x0 + 4, y + size * 0.36, 2.6, "middle", "center", (255, 255, 255), bold=True)
            x = x0 + indent
            for word in item.split():
                t = Text(word, size, text_align=(TextAlign.LEFT, TextAlign.BOTTOM))
                w = t.bounding_box().size.X
                if x + w > x0 + width - 2:
                    x, y = x0 + indent, y - lead
                self.put(word, x, y, size, color=RED if key.match(word.strip("(),.;:")) else (0, 0, 0))
                x += w + space
            y -= lead + gap
        y_end = y + lead + gap - size * 0.6
        self.rect(x0, y_end - 1.5, x0 + width, y1)
        return y_end

    def table(self, x0, y1, cols, rows, title, label_col=0, row_h=6.0):
        y0 = y1 - row_h * (len(rows) + 1)
        x1 = x0 + sum(w for _, w in cols)
        self.rect(x0, y0, x1, y1)
        x = x0
        for i, (hdr, w) in enumerate(cols):
            self.text(hdr, x + 1.5, y1 - row_h + 1.8, 2.4)
            for r, row in enumerate(rows):
                v = row[i]
                s = f"{v:g}" if isinstance(v, float) else str(v)
                self.text(s, x + 1.5, y1 - row_h * (r + 2) + 1.8, 2.6, layer="label" if i == label_col or (label_col == -1 and i == 0) else "text")
            x += w
            if x < x1:
                self.line((x, y0), (x, y1))
        for r in range(1, len(rows) + 1):
            self.line((x0, y1 - row_h * r), (x1, y1 - row_h * r))
        self.text(title, x0, y1 + 1.5, 2.6)
        return y0

    def title_block(self, number, total, title, subtitle, drawing_no, scale_txt):
        x0, y1 = 262.0, 44.0
        self.rect(x0, M, PAGE_W - M, y1, "frame")
        q = y1 - M - 4
        qx0 = PAGE_W - M - 2 - q
        self.line((qx0 - 2, M), (qx0 - 2, y1))
        self.line((x0, 27), (qx0 - 2, 27))
        self.line((x0 + 62, M), (x0 + 62, 27))
        self.line((x0 + 92, M), (x0 + 92, 27))
        self.text(title, x0 + 2, 36, 5.0)
        self.text(subtitle, x0 + 2, 29.5, 2.6)
        for (lbl, val), cx in zip([("DRAWING", drawing_no), ("SCALE", scale_txt), ("SHEET", f"{number} / {total}")],
                                  [x0, x0 + 62, x0 + 92]):
            self.text(lbl, cx + 2, 22.5, 2.0)
            self.text(val, cx + 2, 14, 3.4)
        qr = qrcode.QRCode(border=0, box_size=1)
        qr.add_data(URL)
        qr.make()
        mat = qr.get_matrix()
        cell = q / len(mat)
        for r, row in enumerate(mat):
            for c, on in enumerate(row):
                if on:
                    self.add("qr", Pos(qx0 + (c + 0.5) * cell, y1 - 2 - (r + 0.5) * cell) * Rectangle(cell * 1.02, cell * 1.02))
        self.text("3D", qx0 - 4, y1 - 6, 2.4, (Align.MAX, Align.MIN))
        self.text("All dimensions in mm.  Third-angle projection.  PLACEHOLDER DIMENSIONS — prototype sheet.", M + 4, 13, 2.6)

    def export(self, stem):
        svg = ExportSVG(unit=Unit.MM, fit_to_stroke=False)
        svg.add_layer("page", line_color=(255, 255, 255), line_weight=0.01)
        svg.add_layer("frame", line_color=(0, 0, 0), line_weight=0.5)
        svg.add_layer("visible", line_color=(0, 0, 0), line_weight=0.45)
        svg.add_layer("hidden", line_color=(110, 110, 110), line_weight=0.25, line_type=LineType.HIDDEN)
        svg.add_layer("hatch", line_color=(80, 80, 80), line_weight=0.13)
        svg.add_layer("thin", line_color=(0, 0, 0), line_weight=0.2)
        svg.add_layer("dims", fill_color=(0, 0, 0), line_color=None, line_weight=0.01)
        svg.add_layer("text", fill_color=(0, 0, 0), line_color=None, line_weight=0.01)
        svg.add_layer("label", fill_color=RED, line_color=RED, line_weight=0.25)
        svg.add_layer("qr", fill_color=(0, 0, 0), line_color=None, line_weight=0.01)
        svg.add_layer("bar", fill_color=(40, 40, 40), line_color=None, line_weight=0.01)
        svg.add_layer("invert", fill_color=(255, 255, 255), line_color=None, line_weight=0.01)
        for name, shapes in self.layers.items():
            if shapes:
                svg.add_shape(shapes, layer=name)
        path = OUT / f"{stem}.svg"
        svg.write(str(path))
        els = []
        for txt, x, y, size, anchor, (r, g, b), bold, rot in self.texts:
            tr = f' transform="rotate({-rot:g} {x:.3f} {-y:.3f})"' if rot else ""
            weight = ' font-weight="bold"' if bold else ""
            els.append(f'<text x="{x:.3f}" y="{-y:.3f}" font-size="{size:.3f}" text-anchor="{anchor}" '
                       f'fill="rgb({r},{g},{b})"{weight}{tr}>{escape(txt)}</text>')
        body = path.read_text()
        group = '<g font-family="Arial, Helvetica, sans-serif" stroke="none">\n' + "\n".join(els) + "\n</g>\n</svg>"
        path.write_text(body[: body.rindex("</svg>")] + group)
        cairosvg.svg2pdf(url=str(path), write_to=str(OUT / f"{stem}.pdf"))
        cairosvg.svg2png(url=str(path), write_to=str(OUT / f"{stem}.png"), output_width=2400, background_color="white")
        return OUT / f"{stem}.pdf"


# ===== Sheet 1: Carcass assembly ===========================================================
s1 = Sheet(2, 3, "KAGU  ·  CARCASS ASSEMBLY", "Placeholder — prototype drawing set", "KAGU-CAR-001", "1:8")
LOOK = (0, 0, H / 2)
ORTHO_K = 1 / 8
fw, fh, sd = W * ORTHO_K, H * ORTHO_K, D * ORTHO_K
GAP = 22.0
fx0, fy0 = 40.0, 74.0
front = View(s1, assembled, (0, -5000, H / 2), (0, 0, 1), LOOK, (fx0, fy0, fx0 + fw, fy0 + fh), [8], hidden=False)
right = View(s1, assembled, (5000, 0, H / 2), (0, 0, 1), LOOK, (fx0 + fw + GAP, fy0, fx0 + fw + GAP + sd, fy0 + fh), [8], hidden=False)
top = View(s1, assembled, (0, 0, 5000), (0, 1, 0), LOOK, (fx0, fy0 + fh + GAP, fx0 + fw, fy0 + fh + GAP + sd), [8], hidden=False)
for v, name in [(front, "FRONT"), (right, "RIGHT SIDE"), (top, "TOP")]:
    x0, y0, x1, _ = v.box
    s1.text(name, (x0 + x1) / 2, y0 - (16 if v is not top else 5), 3.2, (Align.CENTER, Align.MAX))
x0, y0, x1, y1 = front.box
s1.dim((x0, y0), (x1, y0), 8, W)
s1.dim((x0, y1), (x0, y0), 8, H)
s1.dim((x1, y0), (x1, y0 + SHELF_Z * ORTHO_K), 6, SHELF_Z)
rx0, ry0, rx1, _ = right.box
s1.dim((rx0, ry0), (rx1, ry0), 8, D)
# hardware callout on the right-side view: one Confirmat head on the outer face of B
for z in ROWS_Z.values():
    for yy in HOLE_Y:  # installed Confirmat heads drawn solid on the assembly
        q = right.pt((W / 2, -D / 2 + yy, z))
        s1.add("dims", Pos(q.X, q.Y) * Circle(0.95))
s1.add("dims", Pos(rx1 + 6, ry0 - 13) * Circle(0.95))
s1.text("= H1 installed", rx1 + 8.5, ry0 - 14.2, 2.4)
h = right.pt((W / 2, -D / 2 + HOLE_Y[2], SHELF_Z - T / 2))
s1.leader((h.X, h.Y), (rx1 + 10, h.Y + 18), ["H1  Confirmat 7x50", "5 per joint, both sides"], "label")

# exploded view with Part Label balloons
ISO = (262.0, 128.0, PAGE_W - M - 4, PAGE_H - M - 4)
iso_origin = (1400, -2600, 1900)
iso = View(s1, exploded, iso_origin, (0, 0, 1), LOOK, (ISO[0], ISO[1] + 8, ISO[2], ISO[3]), hidden=False)
ix0, iy0, ix1, iy1 = iso.box
s1.text(f"EXPLODED VIEW  (1:{iso.scale})", (ISO[0] + ISO[2]) / 2, ISO[1] + 2, 3.2, (Align.CENTER, Align.MIN))
cx, cy = (ix0 + ix1) / 2, (iy0 + iy1) / 2
hx, hy = (ix1 - ix0) / 2 + 9, (iy1 - iy0) / 2 + 9
for p in parts:
    own = iso.own_edges(Compound(children=[q.placed(True) for q in parts if q is not p]))
    a = max(own, key=lambda e: e.length).position_at(0.5)
    a = Vector(a.X * iso.k + iso.dx, a.Y * iso.k + iso.dy)
    v = Vector(a.X - cx, a.Y - cy)
    v = v.normalized() if v.length > 1e-6 else Vector(1, 0)
    t = min(hx / abs(v.X) if abs(v.X) > 1e-6 else 1e9, hy / abs(v.Y) if abs(v.Y) > 1e-6 else 1e9)
    s1.balloon(p.label, (a.X, a.Y), (cx + v.X * t, cy + v.Y * t))

cut_rows = [(p.label, p.name, "1", *sorted(p.size, reverse=True), p.material) for p in parts]
cols = [("LBL", 10), ("PART", 46), ("QTY", 10), ("L", 16), ("W", 16), ("T", 12), ("MATERIAL", 38)]
s1.table(262.0, 124.0, cols, cut_rows, "CUT LIST  (mm, L = grain direction)")
hw_cols = [("ID", 10), ("HARDWARE", 82), ("QTY", 12), ("DRILL", 44)]
s1.table(262.0, 72.0, hw_cols, HARDWARE, "HARDWARE")
s1.steps(M + 4, 54, 165, "ASSEMBLY SEQUENCE", [
    "Machine dados, rabbets and Ø7 holes in A and B (sheet 3), drilling with jig J1.",
    "Drill Ø5 x 45 pilots in both ends of C, D and F with jig J2.",
    "Stand A on its front edge. Seat C, F and D in their joints and drive H1.",
    "Lower B onto C, F and D; drive H1. Check both diagonals are equal.",
    "Slide E down the back rabbets and fix it to C, D and F with H2.",
])

# ===== Sheet 2: Part A (side, left) =========================================================
s2 = Sheet(3, 3, "KAGU  ·  PART A — SIDE, LEFT", "18 ply · qty 1 (B is mirror image)", "KAGU-CAR-002", "1:5")
A = parts[0].placed()
LOOK_A = (-W / 2 + T / 2, 0, H / 2)
inside = View(s2, A, (5000, 0, H / 2), (0, 0, 1), LOOK_A, (66, 50, 182, 275), [5])
x0, y0, x1, y1 = inside.box
s2.text("INSIDE FACE  (1:5)", (x0 + x1) / 2, y0 - 22, 3.2, (Align.CENTER, Align.MAX))
front_pt = lambda yy, z: inside.pt((-W / 2 + T, -D / 2 + yy, z))
s2.dim((x0, y1), (x0, y0), 10, H)
s2.dim((x0, y0), (x1, y0), 16, D)
s2.dim(tuple(front_pt(D, SHELF_Z))[:2], tuple(front_pt(D, 0))[:2], -8, SHELF_Z)
# ordinate positions of the Confirmat holes, measured from the front edge
base_y = y0 - 6
f0 = front_pt(0, 0)
for yy in [0.0] + HOLE_Y:
    p = front_pt(yy, 0)
    s2.line((p.X, y0 - 1.5), (p.X, base_y))
    s2.text(f"{yy:g}", p.X, base_y - 0.8, 2.4, (Align.CENTER, Align.MAX), rotation=0)
s2.text("FRONT EDGE", f0.X - 5, base_y - 0.8, 2.2, (Align.MAX, Align.MAX))
# feature notes
s2.leader(tuple(front_pt(470, SHELF_Z - T / 2))[:2], (x1 + 14, y0 + 0.62 * (y1 - y0)),
          ["SHELF DADO 18 W x 6 D", "THRU, for F  (DETAIL 1)"])
s2.leader(tuple(front_pt(470, H - T / 2))[:2], (x1 + 14, y1 - 6), ["TOP RABBET 18 W x 6 D", "THRU, for D  (DETAIL 2)"])
s2.leader(tuple(front_pt(470, T / 2))[:2], (x1 + 14, y0 + 14), ["BOTTOM RABBET 18 W x 6 D", "THRU, for C  (DETAIL 3)"])
s2.leader(tuple(front_pt(D - TB / 2, 560))[:2], (x1 + 14, y0 + 0.8 * (y1 - y0)), ["BACK RABBET 12 W x 9 D", "full height, for E  (DETAIL 4)"])
s2.leader(tuple(front_pt(HOLE_Y[0], SHELF_Z - T / 2))[:2], (x0 - 18, y0 + 0.3 * (y1 - y0)),
          ["15x Ø7 THRU", "CSK Ø10 x 90° far side", "centred in each joint", "(H1 Confirmat)"])
# Part Label mark (proposed): letter + UP/FRONT triangle on the inside face, front-bottom corner
pl = front_pt(60, 70)
s2.text("A", pl.X, pl.Y, 5.0, (Align.CENTER, Align.CENTER), "label")
s2.text("▲", pl.X - 6, pl.Y, 3.2, (Align.CENTER, Align.CENTER), "label")
s2.leader((pl.X - 6, pl.Y - 2), (x0 - 18, y0 + 0.12 * (y1 - y0)), ["PART LABEL (proposed)", "letter + ▲ = UP", "inside face,", "front-bottom corner"], "label")
# detail callout circle on the inside face around the shelf joint at the third hole
dc = front_pt(HOLE_Y[2], SHELF_Z - T / 2)
s2.add("thin", Pos(dc.X, dc.Y) * (Circle(9) - Circle(8.8)))
s2.text("1", dc.X + 9.5, dc.Y + 6.5, 3.4)
for letter, (yy, z) in {"2": (HOLE_Y[3], H - T / 2), "3": (HOLE_Y[3], T / 2), "4": (D - TB / 2, 560.0)}.items():
    c = front_pt(yy, z)
    s2.add("thin", Pos(c.X, c.Y) * (Circle(7) - Circle(6.8)))
    s2.text(letter, c.X + 7.5, c.Y + 5, 3.4)

# Detail B: section through the shelf joint at a hole row, viewed from the front
y_cut = -D / 2 + HOLE_Y[2]
cut_plane = Plane(origin=(0, y_cut, 0), z_dir=(0, 1, 0))
crop = box(-W / 2 - 0.5, -W / 2 + 85, y_cut - 1, D / 2 + 1, SHELF_Z - 55, SHELF_Z + 32)
sect = section([parts[0].placed(), parts[5].placed()], cut_plane, crop)
detail = View(s2, sect, (-W / 2 + 40, -5000, SHELF_Z), (0, 0, 1), (-W / 2 + 40, 0, SHELF_Z), (256, 186, 330, 268), [2], hidden=False)
cut_faces = [f for f in sect.faces() if abs(f.center().Y - y_cut) < 1e-3]
detail.hatch(cut_faces, spacing=1.6)
dx0, dy0, dx1, dy1 = detail.box
dp = lambda x, z: detail.pt((x, y_cut, z))
s2.dim(tuple(dp(-W / 2 + T - JD, SHELF_Z - T))[:2], tuple(dp(-W / 2 + T, SHELF_Z - T))[:2], 10, JD)
s2.dim(tuple(dp(-W / 2, SHELF_Z - 55))[:2], tuple(dp(-W / 2 + T, SHELF_Z - 55))[:2], 7, T)  # below the cut end
s2.dim(tuple(dp(-W / 2, SHELF_Z - T))[:2], tuple(dp(-W / 2, SHELF_Z))[:2], -6, T)
s2.leader(tuple(dp(-W / 2 + 3, SHELF_Z - T / 2 + CF_SHANK / 2))[:2], (dx0 + 2, dy1 + 4), ["Ø7 THRU, CSK Ø10 x 90°"])
s2.leader(tuple(dp(-W / 2 + T - JD + 25, SHELF_Z - T / 2 - CF_PILOT / 2))[:2], (dx1 - 18, dy0 - 4), ["Ø5 x 45 DP pilot in F (J2)"])
low = detail.tag_sections(sect, lambda f: abs(f.center().Y - y_cut) < 1e-3)
s2.text("DETAIL 1 — SHELF DADO  (1:2)", (dx0 + dx1) / 2, min(dy0 - 12, low - 4), 3.2, (Align.CENTER, Align.MAX))

# Detail C: plan section at the back rabbet with E in place
z_cut = 560.0
plan_plane = Plane(origin=(0, 0, z_cut), z_dir=(0, 0, -1))
crop_c = box(-W / 2 - 0.5, -W / 2 + 55, D / 2 - 45, D / 2 + 0.5, 0, z_cut + 1)
sect_c = section([parts[0].placed(), parts[4].placed()], plan_plane, crop_c)
detail_c = View(s2, sect_c, (-W / 2 + 25, D / 2 - 20, 5000), (0, 1, 0), (-W / 2 + 25, D / 2 - 20, z_cut), (340, 96, 406, 160), [2], hidden=False)
detail_c.hatch([f for f in sect_c.faces() if abs(f.center().Z - z_cut) < 1e-3], spacing=1.6)
cx0, cy0, cx1, cy1 = detail_c.box
cp = lambda x, y: detail_c.pt((x, y, z_cut))
s2.dim(tuple(cp(-W / 2 + T - BR, D / 2))[:2], tuple(cp(-W / 2 + T, D / 2))[:2], -6, BR)
s2.dim(tuple(cp(-W / 2 + T, D / 2 - TB))[:2], tuple(cp(-W / 2 + T, D / 2))[:2], 14, TB)
s2.text("BACK →", cx1 + 3, cy1 - 3, 2.4, (Align.MIN, Align.MAX))
low = detail_c.tag_sections(sect_c, lambda f: abs(f.center().Z - z_cut) < 1e-3)
s2.text("DETAIL 4 — BACK RABBET, PLAN  (1:2)", (cx0 + cx1) / 2, min(cy0 - 12, low - 4), 3.2, (Align.CENTER, Align.MAX))



def rabbet_detail(letter, title, panel, z_lo, z_hi, z_joint_lo, region):
    """Section through a rabbet joint at a hole row, viewed from the front, with width and depth."""
    sec = section([parts[0].placed(), panel.placed()], cut_plane, box(-W / 2 - 0.5, -W / 2 + 60, y_cut - 1, D / 2 + 1, z_lo, z_hi))
    v = View(s2, sec, (-W / 2 + 30, -5000, (z_lo + z_hi) / 2), (0, 0, 1), (-W / 2 + 30, 0, (z_lo + z_hi) / 2), region, [2], hidden=False)
    v.hatch([f for f in sec.faces() if abs(f.center().Y - y_cut) < 1e-3], spacing=1.6)
    p = lambda x, z: tuple(v.pt((x, y_cut, z)))[:2]
    inner = -W / 2 + T
    z_far = z_joint_lo if z_joint_lo > z_lo else z_joint_lo + T  # edge of the rabbet away from the panel end
    s2.dim(p(inner - JD, z_far), p(inner, z_far), 6 if z_joint_lo > z_lo else -6, JD)
    s2.dim(p(-W / 2, z_joint_lo), p(-W / 2, z_joint_lo + T), -6 if z_joint_lo > z_lo else 6, T)
    low = v.tag_sections(sec, lambda f: abs(f.center().Y - y_cut) < 1e-3)
    x0, y0, x1, y1 = v.box
    s2.text(title, (x0 + x1) / 2, min(y0 - 10, low - 4), 3.2, (Align.CENTER, Align.MAX))


rabbet_detail("D", "DETAIL 2 — TOP RABBET  (1:2)", parts[3], H - 40, H + 0.5, H - T, (346, 196, 406, 268))
rabbet_detail("E", "DETAIL 3 — BOTTOM RABBET  (1:2)", parts[2], -0.5, 40, 0.0, (262, 96, 326, 160))
s2.table(262.0, 66.0, hw_cols, HARDWARE[:1], "HARDWARE (this part)")
s2.steps(M + 4, 52, 165, "MACHINING SEQUENCE", [
    "Rip and crosscut to 785 x 500. Mark the Part Label A on the inside face (front-bottom corner).",
    "Cut the top and bottom rabbets and the shelf dado: dado stack 18 wide, 6 deep (details 1, 2, 3).",
    "Cut the back rabbet 12 x 9 along the rear edge, full height (detail 4).",
    "Drill the 15 holes from the inside face with jig J1, which registers in the dado and rabbets; countersink from the outside face.",
])


# ===== Sheet 1: notation and conventions ======================================================
s0 = Sheet(1, 3, "KAGU  ·  NOTATION & CONVENTIONS", "Read this sheet first — applies to every sheet", "KAGU-GEN-000", "—")


def heading(sh, x, y, title, width=118):
    sh.add("bar", Pos(x + width / 2, y - 3.25) * Rectangle(width, 6.5))
    sh.put(title, x + 2.5, y - 3.25, 3.0, "start", "center", (255, 255, 255), bold=True)
    return y - 12


def entry(sh, x, y, lines, size=2.6):
    for i, ln in enumerate(lines):
        sh.text(ln, x, y - i * (size + 1.3), size, (Align.MIN, Align.CENTER) if i == 0 else (Align.MIN, Align.CENTER),
                layer="text")
    return y - max(len(lines), 1) * (size + 1.3) - 4


def hatch_rect(sh, x0, y0, w, h, spacing=1.6):
    f = Pos(x0 + w / 2, y0 + h / 2) * Rectangle(w, h)
    f = f.faces()[0]
    j = -w - h
    while j < w + h:
        ln = Edge.make_line((x0 + j, y0), (x0 + j + h * 3, y0 + h * 3))
        sh.add("hatch", f.intersect(ln) or [])
        j += spacing
    sh.rect(x0, y0, x0 + w, y0 + h, "visible")


# column 1: lines and dimensions
X1, SX = 20.0, 58.0  # sample column, description column
y = heading(s0, X1 - 4, 278, "LINES")
for layer, desc in [("visible", ["Visible edge"]), ("hidden", ["Hidden edge", "(behind a surface)"]),
                    ("thin", ["Thin line: extension, leader,", "table and detail circle"])]:
    s0.line((X1, y), (X1 + 30, y), layer)
    y = entry(s0, SX, y, desc)
hatch_rect(s0, X1, y - 4, 30, 8)
y = entry(s0, SX, y, ["Section: material cut through", "by a section view; hatch angle", "alternates between parts"]) - 2
y = heading(s0, X1 - 4, y, "DIMENSIONS & NOTES")
s0.dim((X1, y - 4), (X1 + 30, y - 4), 2, 100)
y = entry(s0, SX, y, ["Dimension in mm. The number is", "the TRUE size, whatever the scale"]) - 2
s0.leader((X1 + 2, y - 3), (X1 + 12, y + 1), ["Note"])
y = entry(s0, SX, y, ["Note with leader: the dot sits", "on the feature it describes"])
s0.line((X1, y + 1), (X1, y - 4))
s0.line((X1 + 15, y + 1), (X1 + 15, y - 4))
s0.text("0", X1, y - 5, 2.4, (Align.CENTER, Align.MAX))
s0.text("40", X1 + 15, y - 5, 2.4, (Align.CENTER, Align.MAX))
y = entry(s0, SX, y, ["Ordinate positions: measured", "from the 0 edge named beside it"]) - 2
y = heading(s0, X1 - 4, y, "SCALE & UNITS")
y = entry(s0, X1, y, ["All dimensions in millimetres (mm).",
                       "1:5 = the drawing is 1/5 of real size. Each view states its scale.",
                       "Do not measure the paper - always build from the dimensions."])

# column 2: identifiers
X2, SX2 = 150.0, 176.0
y = heading(s0, X2 - 4, 278, "IDENTIFIERS  (red = an ID you can look up)")
s0.balloon("A", (X2 + 14, y - 3), (X2 + 4, y))
y = entry(s0, SX2, y, ["Part Label balloon. Same letter in the", "CUT LIST and marked on the real part"])
s0.text("A", X2 + 6, y, 5.0, (Align.CENTER, Align.CENTER), "label")
s0.text("▲", X2 + 1, y, 3.2, (Align.CENTER, Align.CENTER), "label")
y = entry(s0, SX2, y, ["Part Label mark, written on the part's", "inside face. The ▲ points UP"])
s0.text("H1", X2 + 4, y, 3.4, (Align.CENTER, Align.CENTER), "label")
y = entry(s0, SX2, y, ["Hardware ID - see the HARDWARE table", "(H1 = Confirmat 7x50, H2 = back screw)"])
s0.add("dims", Pos(X2 + 4, y) * Circle(0.95))
y = entry(s0, SX2, y, ["Filled dot (assembly sheets):", "a screw installed at this point"])
s0.add("visible", Pos(X2 + 4, y) * Circle(1.0).edges())
s0.add("visible", Pos(X2 + 4, y) * Circle(1.6).edges())
y = entry(s0, SX2, y, ["Open circles (part sheets): a hole to", "drill; its size is in the hole note"])
s0.text("J1", X2 + 4, y, 3.4, (Align.CENTER, Align.CENTER), "label")
y = entry(s0, SX2, y, ["Jig ID - a 3D-printed drilling or", "marking jig (separate print files)"])
s0.add("thin", Pos(X2 + 4, y) * (Circle(4) - Circle(3.8)))
s0.text("1", X2 + 8.5, y + 3, 3.0)
y = entry(s0, SX2, y, ["Detail circle: this area is drawn larger", "as DETAIL 1 on the same sheet"])
s0.add("bar", Pos(X2 + 4, y) * Circle(2.3))
s0.put("1", X2 + 4, y, 2.6, "middle", "center", (255, 255, 255), bold=True)
y = entry(s0, SX2, y, ["Step badge: do the SEQUENCE steps", "in order; IDs in a step are red"])
s0.add("qr", Pos(X2 + 4, y - 1) * Rectangle(6, 6))
s0.add("invert", Pos(X2 + 4, y - 1) * Rectangle(3, 3))
y = entry(s0, SX2, y, ["QR code (title block): opens the", "interactive 3D model of that assembly"])

# column 3: notation table, projection, terms
X3 = 280.0
y = heading(s0, X3 - 4, 278, "HOLE & SIZE NOTATION", 134)
rows = [("Ø", "diameter", "Ø7 = 7 mm hole"), ("THRU", "all the way through", "Ø7 THRU"),
        ("DP", "depth of a hole", "Ø5 x 45 DP"), ("CSK", "countersink (cone)", "CSK Ø10 x 90°"),
        ("W x D", "width x depth of a cut", "dado 18 W x 6 D"), ("L / W / T", "length (grain) / width / thick.", "cut list"),
        ("QTY", "quantity", ""), ("or eq.", "or an equivalent part", "")]
y_end = s0.table(X3 - 4, y + 2, [("SYMBOL", 18), ("MEANING", 64), ("EXAMPLE", 52)], rows, "", label_col=-1)
y = heading(s0, X3 - 4, y_end - 4, "PROJECTION", 134)
# third-angle symbol: frustum side view (left) and end view (right)
sx, sy = X3, y - 8
s0.add("visible", [Edge.make_line(a, b) for a, b in zip(
    [(sx, sy - 5), (sx + 14, sy - 3), (sx + 14, sy + 3), (sx, sy + 5)],
    [(sx + 14, sy - 3), (sx + 14, sy + 3), (sx, sy + 5), (sx, sy - 5)])])
s0.add("visible", Pos(sx + 24, sy) * Circle(5).edges())
s0.add("visible", Pos(sx + 24, sy) * Circle(3).edges())
for (bx, by, lbl) in [(X3 + 50, sy - 9, "FRONT"), (X3 + 50, sy + 3, "TOP"), (X3 + 74, sy - 9, "RIGHT")]:
    s0.rect(bx, by, bx + 20, by + 10)
    s0.text(lbl, bx + 10, by + 5, 2.3, (Align.CENTER, Align.CENTER))
y = entry(s0, X3, sy - 16, ["Third-angle projection: each view sits on the side it is seen from",
                             "(TOP above FRONT, RIGHT SIDE to the right of FRONT)."])
y = heading(s0, X3 - 4, y + 1, "TERMS", 134)
for term, desc in [("Dado", "groove cut across a panel that another panel seats in"),
                   ("Rabbet", "step cut along a panel edge"),
                   ("Confirmat", "one-piece cabinet screw; needs a stepped Ø5/Ø7 hole"),
                   ("Pilot hole", "small hole the screw threads into"),
                   ("Countersink", "cone at the hole mouth so the head sits flush"),
                   ("Inside face", "the face that ends up inside the Cabinet")]:
    s0.text(term, X3, y, 2.6, (Align.MIN, Align.CENTER), "label")
    s0.text(desc, X3 + 22, y, 2.6, (Align.MIN, Align.CENTER))
    y -= 5.2

writer = PdfWriter()
for pdf in [s0.export("sheet1_notation"), s1.export("sheet2_assembly"), s2.export("sheet3_part_A")]:
    writer.append(str(pdf))
writer.write(str(OUT / "carcass_set.pdf"))
print("ok; iso 1:%s" % iso.scale)

# OCCT objects take minutes to free one-by-one at interpreter shutdown; the files are written, so skip it.
sys.stdout.flush()
os._exit(0)
