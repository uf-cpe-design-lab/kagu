# Prototype: whole-Cabinet lock and interlock

Throwaway prototype for [Whole-cabinet lock and interlock pick](https://github.com/uf-cpe-design-lab/kagu/issues/12). It loads the chosen layout from `../drawing-sheet` (40" · 600 mm deep · two Drawer columns) and draws four lock arrangements on it schematically:

- **A** two keys, one in each outer side panel
- **B** one key in a centre post, flexible shafts to lockbars on the outer sides
- **C** one key in a centre post, both lockbars in the divider, DIY yoke
- **D** two keys, one in each column's top Drawer front

Click Drawers to open them (the interlock allows one per column), turn the keys, and watch the tip check about the front casters. Hardware dimensions marked TBC wait on CompX drawings.

## Run

```sh
python3 -m http.server -d prototype 8766
# open http://127.0.0.1:8766/cabinet-lock/lock_3d.html  (#A … #D picks a variant)
```
