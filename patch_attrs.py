import pathlib
p = pathlib.Path("src/models/palletizer.py")
lines = p.read_text().split("\n")
vb = pathlib.Path("validate_block.txt").read_text().split("\n")
cb = pathlib.Path("ctor_block.txt").read_text().split("\n")
if vb and vb[-1] == "":
    vb.pop()
if cb and cb[-1] == "":
    cb.pop()
va = next(i for i, l in enumerate(lines) if l.strip() == "# struct_to_dict, check each value, and raise")
lines[va+1:va+1] = vb
ca = next(i for i, l in enumerate(lines) if l.strip() == "# validate_config accepted, store on self.")
lines[ca+1:ca+1] = cb
lines = [l for l in lines if l.strip() not in ("columns, rows, layers = 2, 2, 2", "box_h = BOX_H")]
p.write_text("\n".join(lines))
print("patched attributes")
