"""Printable Cabinet hardware (throwaway prototypes): wall standoff (base + TPU cap) and side D-handle.

Each part is modelled in its mounting frame: +Z points away from the panel it is screwed to,
z = 0 is the panel surface. layout.py places them; running this file writes STLs to out/print/.
"""

from pathlib import Path

from build123d import (Align, Axis, Box, Circle, Cone, Cylinder, Edge, ExportDXF, Plane, Polygon, Polyline, Pos, Rot, Unit,
                       Rectangle, Vector, export_stl, extrude, fillet)

# --- wall standoff --------------------------------------------------------------------------
SO_BASE_D, SO_TOP_D, SO_BASE_H = 50.0, 32.0, 35.0  # truncated cone (PETG/ASA)
SO_CAP_D, SO_CAP_H = 32.0, 15.0  # TPU bumper
SO_SCREW_D, SO_BORE_D, SO_FLOOR = 5.5, 11.0, 6.0  # #10 / M5 screw, counterbore = snap socket
SO_STEM_L, SO_BARB_D = 12.0, 12.0  # cap stem snaps past a barb ring into the counterbore
SNAP = 0.15  # radial interference of the stem in the bore


def standoff_base():
    b = Cone(SO_BASE_D / 2, SO_TOP_D / 2, SO_BASE_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    b -= Cylinder(SO_SCREW_D / 2, SO_BASE_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    b -= Pos(0, 0, SO_FLOOR) * Cylinder(SO_BORE_D / 2, SO_BASE_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    return b


def standoff_cap():
    """TPU cap; z = 0 is where it seats on the base's top face, stem points down (-Z)."""
    c = Cylinder(SO_CAP_D / 2, SO_CAP_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    c = fillet(c.edges().group_by(Axis.Z)[-1], 3.0)
    c += Pos(0, 0, -SO_STEM_L) * Cylinder(SO_BORE_D / 2 - 0.2, SO_STEM_L, align=(Align.CENTER, Align.CENTER, Align.MIN))
    c += Pos(0, 0, -SO_STEM_L) * Cone(SO_BARB_D / 2 + SNAP, SO_BORE_D / 2 - 0.2, 3.0, align=(Align.CENTER, Align.CENTER, Align.MIN))
    return c


def standoff_assembled():
    return [standoff_base(), Pos(0, 0, SO_BASE_H) * standoff_cap()]


# --- side D-handle ---------------------------------------------------------------------------
H_LEN, H_GRIP_D, H_REACH = 300.0, 30.0, 50.0  # post centres, grip diameter, grip centre off the panel
H_POST_D, H_PAD = 26.0, 40.0  # post diameter, square foot on the panel
H_ROD_D = 10.2  # 10 mm aluminium rod through the grip
H_INSERT_D, H_INSERT_L = 8.0, 12.0  # M6 heat-set insert holes in the feet (bolts from inside the Cabinet)


def handle():
    """Grip along X, posts down to z = 0 (panel face)."""
    grip = Pos(0, 0, H_REACH) * Rot(0, 90, 0) * Cylinder(H_GRIP_D / 2, H_LEN + H_POST_D)
    h = grip
    for x in (-H_LEN / 2, H_LEN / 2):
        h += Pos(x, 0, 0) * Cylinder(H_POST_D / 2, H_REACH, align=(Align.CENTER, Align.CENTER, Align.MIN))
        h += Pos(x, 0, 0) * Box(H_PAD, H_PAD, 6, align=(Align.CENTER, Align.CENTER, Align.MIN))
        h -= Pos(x, 0, 0) * Cylinder(H_INSERT_D / 2, H_INSERT_L, align=(Align.CENTER, Align.CENTER, Align.MIN))
    h -= Pos(0, 0, H_REACH) * Rot(0, 90, 0) * Cylinder(H_ROD_D / 2, H_LEN + H_POST_D + 2)
    return h


# --- drawer pull: waterjet-cut, bent aluminium strip, set flush into the front's top edge -------------
import math

P_LEN, P_FLANGE, P_LIP, P_T = 160.0, 16.0, 20.0, 2.0  # 5052-H32, 2 mm; flange/lip are outside (mould-line) lengths
P_BEND, P_R_IN, P_K = 45.0, 2.0, 0.33  # lip turns 45° down; inside bend radius; K-factor for the flat pattern
P_CHAMFER, P_CORNER_R = 8.0, 3.0  # 45° cuts on the lip's outer corners; every outline corner rounded R3
P_HOLE_D, P_HOLE_X = 4.5, 60.0  # 2 countersunk M4 / #8 flat-head screws down into the front's top edge
P_POCKET = (P_LEN + 1.0, P_FLANGE + 0.5, P_T)  # routed recess in the top edge (length, depth in, deep)

_SETBACK = (P_R_IN + P_T) * math.tan(math.radians(P_BEND / 2))
P_FLANGE_FLAT, P_LIP_FLAT = P_FLANGE - _SETBACK, P_LIP - _SETBACK
P_BEND_ALLOW = math.radians(P_BEND) * (P_R_IN + P_K * P_T)


def _flat_outline():
    """Flat blank, x across the pull, y from the flange's back edge (0) to the lip tip."""
    a, c = P_LEN / 2, P_CHAMFER
    top = P_FLANGE_FLAT + P_BEND_ALLOW + P_LIP_FLAT
    return [(-a, 0), (a, 0), (a, top - c), (a - c, top), (-a + c, top), (-a, top - c)], top


def drawer_pull_flat():
    """Waterjet blank: outline with R3 corners and the two screw holes; bend line returned separately."""
    pts, top = _flat_outline()
    blank = Polygon(*pts, align=None)
    blank = fillet(blank.vertices(), P_CORNER_R)
    for x in (-P_HOLE_X, P_HOLE_X):
        blank -= Pos(x, P_FLANGE_FLAT / 2) * Circle(P_HOLE_D / 2)
    y_bend = P_FLANGE_FLAT + P_BEND_ALLOW / 2
    return blank, Edge.make_line((-P_LEN / 2, y_bend), (P_LEN / 2, y_bend))


def drawer_pull():
    """The waterjet blank, bent. Mounting frame: origin on the front's top-front edge, +Z out of the face, +Y up.

    Flange flush on the top edge running back into the front (top surface y = 0), an R2 bend at the
    front edge, then the lip going forward and down at 45°. Built by bending the flat blank itself, so the
    3D part and the DXF always agree.
    """
    blank, _ = drawer_pull_flat()
    a, top = P_LEN / 2 + 1, _flat_outline()[1] + 1
    y_lip = P_FLANGE_FLAT + P_BEND_ALLOW
    flange = blank & Pos(0, P_FLANGE_FLAT / 2 - 0.5) * Rectangle(2 * a, P_FLANGE_FLAT + 1)
    lip = Pos(0, -y_lip) * (blank & Pos(0, (y_lip + top) / 2) * Rectangle(2 * a, top - y_lip))
    th, r_out = math.radians(P_BEND), P_R_IN + P_T
    z_b, cy = -_SETBACK, -P_T - P_R_IN  # bend starts at z_b; centre below the sheet
    part = extrude(Plane(origin=(0, 0, -P_FLANGE), x_dir=(1, 0, 0), z_dir=(0, -1, 0)) * flange, P_T)
    arc = [(z_b + r_out * math.sin(th * k / 12), cy + r_out * math.cos(th * k / 12)) for k in range(13)]
    arc += [(z_b + P_R_IN * math.sin(th * k / 12), cy + P_R_IN * math.cos(th * k / 12)) for k in range(12, -1, -1)]
    side = Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))  # local (x, y) = world (z, y)
    part += extrude(side * Polygon(*arc, align=None), P_LEN / 2, both=True)
    outer_end = Vector(0, cy + r_out * math.cos(th), z_b + r_out * math.sin(th))
    inward = Vector(0, -math.cos(th), -math.sin(th))
    part += extrude(Plane(origin=outer_end, x_dir=(1, 0, 0), z_dir=inward) * lip, P_T)
    for x in (-P_HOLE_X, P_HOLE_X):  # countersinks on the top face
        at = Vector(x, 0, -P_FLANGE + P_FLANGE_FLAT / 2)
        part -= Pos(at) * Rot(90, 0, 0) * Cone(P_HOLE_D, P_HOLE_D / 2, P_HOLE_D / 2, align=(Align.CENTER, Align.CENTER, Align.MAX))
    return part


def drawer_pull_pocket():
    """Material routed out of the drawer front, in the pull's mounting frame (6 mm bit leaves R3 corners)."""
    length, depth, deep = P_POCKET
    return Pos(0, -deep / 2, -depth / 2) * Box(length, deep, depth)


if __name__ == "__main__":
    out = Path(__file__).parent / "out" / "print"
    out.mkdir(parents=True, exist_ok=True)
    blank, bend = drawer_pull_flat()
    dxf = ExportDXF(unit=Unit.MM)
    dxf.add_layer("CUT")
    dxf.add_layer("BEND_45_LIP_DOWN")
    dxf.add_shape(blank, layer="CUT")
    dxf.add_shape(bend, layer="BEND_45_LIP_DOWN")
    dxf.write(str(out / "drawer_pull_flat_5052_2mm_waterjet.dxf"))
    print(f"drawer_pull_flat DXF    {P_LEN:.0f} x {_flat_outline()[1]:.1f} mm waterjet blank, 45° bend (R{P_R_IN:.0f} inside, K={P_K}) centred {P_FLANGE_FLAT + P_BEND_ALLOW / 2:.1f} mm from the flange edge")
    for name, part in [("standoff_base_PETG", standoff_base()), ("standoff_cap_TPU", standoff_cap()), ("handle_300_PETG", handle()), ("drawer_pull_ref", drawer_pull())]:
        bb = part.bounding_box()
        export_stl(part, str(out / f"{name}.stl"))
        print(f"{name:22} {bb.size.X:6.1f} x {bb.size.Y:6.1f} x {bb.size.Z:6.1f} mm")
