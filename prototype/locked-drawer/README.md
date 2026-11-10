# Prototype: Locked Drawer and Viewing Lid

Throwaway prototype for [Locked Drawer and Viewing Lid](https://github.com/uf-cpe-design-lab/kagu/issues/13). It loads the chosen layout from `../drawing-sheet` (40" · 600 mm deep · two Drawer columns) and adds a clear Viewing Lid to whichever Drawers you tick as Locked Drawers:

- **A** hinged at the back (printed knuckle hinges, short fixed rear strip)
- **B** drop-in sheet (flush in 6 × 6 mm rabbets; back edge in a grooved rail; lift the front, slide forward, lift out)
- **C** slide-out lid (printed rails on the box sides; slides forward off the Drawer)

and three lid-lock options: **0** no lock yet (a "check out with staff" label, cam-lock hole marked and its space kept), **1** a cam lock in the Drawer front, **2** a compression-mount glass-door lock on the lid edge.

Pull a Locked Drawer out, turn Key B, open the lid. The rail runs the fit checks live: whether the lid clears the fronts above at full extension, whether any Bin row is lost, room behind the front for the lock and an e-lock provision, the pitch each Locked Drawer adds against each column's spare height, and lid sag. The side section draws the active Drawer pulled out.

## Run

```sh
python3 -m http.server -d prototype 8767
# open http://127.0.0.1:8767/locked-drawer/lid_3d.html
```
