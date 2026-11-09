"""Spike: verify build123d 0.13.0 drawing + Part Label + export claims for
research/code-cad-drawings.md. Throwaway code, not the kagu drafting module.

Run: pip install build123d==0.13.0 pygltflib && python spike.py
Produces out/{carcass.step, carcass.glb, carcass_exploded.glb, C.3mf, spike.svg, spike.dxf}.
"""

from pathlib import Path

from build123d import (
    IN,
    Box,
    Circle,
    Color,
    Compound,
    Draft,
    Edge,
    ExportDXF,
    ExportSVG,
    ExtensionLine,
    LineType,
    Location,
    Mesher,
    NumberDisplay,
    PageSize,
    Pos,
    Sketch,
    TechnicalDrawing,
    Text,
    Unit,
    Vector,
    export_gltf,
    export_step,
    section,
    Plane,
)

OUT = Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)

T = 0.75 * IN  # nominal ply thickness parameter
W, D, H = 18 * IN, 16 * IN, 30 * IN


def panel(label: str, size, loc: Location, explode: Vector) -> Box:
    p = Box(*size)
    p.label = label  # Part Label -> STEP product name / glTF node name
    p.color = Color(0xD8B98A)
    p.location = loc
    p.explode = explode  # custom attribute: exploded offset
    return p


A = panel("A", (T, D, H), Location((-(W - T) / 2, 0, H / 2)), Vector(-150, 0, 0))
B = panel("B", (T, D, H), Location(((W - T) / 2, 0, H / 2)), Vector(150, 0, 0))
C = panel("C", (W - 2 * T, D, T), Location((0, 0, T / 2)), Vector(0, 0, -150))
parts = [A, B, C]

carcass = Compound(label="Carcass", children=parts)
exploded = Compound(
    label="Carcass-exploded",
    children=[p.moved(Location(p.explode)) for p in parts],
)
for src, dst in zip(parts, exploded.children):
    dst.label = src.label

# --- 3D handoff ---------------------------------------------------------
export_step(carcass, OUT / "carcass.step")
export_gltf(carcass, OUT / "carcass.glb", binary=True)
export_gltf(exploded, OUT / "carcass_exploded.glb", binary=True)
m = Mesher()
m.add_shape(C, part_number="C")
m.write(OUT / "C.3mf")

# --- 2D shop drawing ----------------------------------------------------
draft = Draft(
    font_size=3.5,
    unit=Unit.IN,
    number_display=NumberDisplay.FRACTION,
    fractional_precision=32,
    display_units=True,
)
scale = 0.1


def view(shape, viewpoint, up=(0, 0, 1)):
    vis, hid = shape.project_to_viewport(viewpoint, up, look_at=(0, 0, 0))
    return Compound(children=vis).scale(scale), Compound(children=hid).scale(scale)


front_vis, front_hid = view(carcass, (0, -1000, 0))
iso_vis, _ = view(exploded, (1000, -1000, 800))
iso_vis = iso_vis.moved(Location((90, 20)))

# overall width dimension on the front view, measured from projected geometry
bb = front_vis.bounding_box()
dim_w = ExtensionLine(
    border=[(bb.min.X, bb.min.Y), (bb.max.X, bb.min.Y)],
    offset=(0, -10),
    draft=draft,
    label=None,
)
# The dimension measures the *scaled* drawing; relabel with the true size
dim_w_true = ExtensionLine(
    border=[(bb.min.X, bb.min.Y), (bb.max.X, bb.min.Y)],
    offset=(0, -10),
    draft=draft,
    label=draft._number_with_units(W),
)


def balloon(letter: str, anchor_2d: Vector, at_2d: Vector, r=4.0) -> Sketch:
    """Part Label balloon: circle + letter + leader line (no native class exists)."""
    circle = Pos(at_2d.X, at_2d.Y) * (Circle(r) - Circle(r - 0.35))
    text = Pos(at_2d.X, at_2d.Y) * Text(letter, font_size=4.5)
    direction = (anchor_2d - at_2d).normalized()
    leader = Edge.make_line(at_2d + direction * r, anchor_2d)
    return circle + text, leader


balloons = []
leaders = []
for p in exploded.children:
    c = p.center()
    # Project a short edge at the centroid to get its 2D image
    e = Edge.make_line(c, c + Vector(0.01, 0, 0))
    vis, _ = Compound(children=[e]).project_to_viewport((1000, -1000, 800), (0, 0, 1), look_at=(0, 0, 0))
    anchor = vis[0].position_at(0) * scale + Vector(90, 20)
    b, l = balloon(p.label, Vector(anchor.X, anchor.Y), Vector(anchor.X + 15, anchor.Y + 15))
    balloons.append(b)
    leaders.append(l)

border = TechnicalDrawing(
    designed_by="kagu",
    page_size=PageSize.LETTER,
    title="Carcass spike",
    sub_title="Part Labels A-C",
    drawing_number="KAGU-SPIKE-1",
    drawing_scale=1 / scale,
)

svg = ExportSVG(unit=Unit.MM, margin=5)
svg.add_layer("Border")
svg.add_layer("Visible", line_weight=0.5)
svg.add_layer("Hidden", line_color=(99, 99, 99), line_type=LineType.ISO_DOT)
svg.add_layer("Dims", fill_color=(0, 0, 0), line_weight=0.2)
svg.add_layer("Labels", fill_color=(200, 0, 0), line_color=(200, 0, 0))
svg.add_shape(border, layer="Border")
svg.add_shape(front_vis, layer="Visible")
svg.add_shape(front_hid, layer="Hidden")
svg.add_shape(iso_vis, layer="Visible")
svg.add_shape(dim_w_true, layer="Dims")
for b in balloons:
    svg.add_shape(b, layer="Labels")
svg.add_shape(leaders, layer="Labels")
svg.write(OUT / "spike.svg")

dxf = ExportDXF(unit=Unit.MM)
dxf.add_layer("Visible")
dxf.add_layer("Hidden", line_type=LineType.ISO_DASH)
dxf.add_layer("Dims")
dxf.add_shape(front_vis, layer="Visible")
dxf.add_shape(front_hid, layer="Hidden")
dxf.add_shape(dim_w_true, layer="Dims")
dxf.write(OUT / "spike.dxf")

# --- section --------------------------------------------------------------
sec = section(carcass, section_by=Plane.XZ)
print("section faces:", len(sec.faces()))

# --- cut list ----------------------------------------------------------------
print("label,L_in,W_in,T_in")
for p in parts:
    dims = sorted(p.bounding_box().size, reverse=True)
    print(p.label, *[round(d / IN, 3) for d in dims], sep=",")
print("dim_w scaled label:", dim_w.dimension, "true:", draft._number_with_units(W))
