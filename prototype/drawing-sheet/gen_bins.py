"""Printable gridfinity test bins for the kagu drawer plan (gridfinity_build123d).

Run: .venv-bins/bin/python gen_bins.py   → out/print/*.stl
"""

from pathlib import Path

from build123d import export_stl
from gridfinity_build123d import BaseEqual, BasePlateEqual, Bin, CompartmentsEqual, StackingLip

OUT = Path(__file__).parent / "out" / "print"
OUT.mkdir(parents=True, exist_ok=True)

BINS = [  # (name, grid x, grid y, height units, what it is for)
    ("bin_3x2_6U_pi-box", 3, 2, 6, "one Raspberry Pi 5 box (4 x 3 x 1.25 in)"),
    ("bin_3x2_10U_pi-box-stack", 3, 2, 10, "two Pi 5 boxes stacked (4 x 3 x 2.5 in)"),
    ("bin_1x1_6U_sensor", 1, 1, 6, "small sensors"),
    ("bin_2x1_6U_sensor", 2, 1, 6, "sensors, several per bin"),
    ("bin_2x2_6U_sensor", 2, 2, 6, "larger sensor modules"),
    ("bin_2x1_3U_flat", 2, 1, 3, "flat parts"),
]

for name, x, y, u, use in BINS:
    # one open compartment hollows the bin; without it the library returns a solid block
    part = Bin(BaseEqual(grid_x=x, grid_y=y), height_in_units=u, compartments=CompartmentsEqual(), lip=StackingLip())
    bb = part.bounding_box()
    export_stl(part, str(OUT / f"{name}.stl"))
    print(f"{name:28} {bb.size.X:6.1f} x {bb.size.Y:6.1f} x {bb.size.Z:5.1f} mm  vol {part.volume / bb.size.X / bb.size.Y / bb.size.Z:4.0%} of box   {use}")

plate = BasePlateEqual(size_x=5, size_y=2)
bb = plate.bounding_box()
export_stl(plate, str(OUT / "baseplate_5x2.stl"))
print(f"{'baseplate_5x2':28} {bb.size.X:6.1f} x {bb.size.Y:6.1f} x {bb.size.Z:5.1f} mm   holds a 3x2 + 2x2 side by side")
