import pathlib
p = pathlib.Path("src/models/palletizer.py")
lines = p.read_text().split("\n")
pi = next(i for i, l in enumerate(lines) if l.strip() == "async def pack(self):")
ri = next(i for i in range(pi, len(lines)) if lines[i].strip().startswith("raise NotImplementedError"))
body = [
"        await self.clear_boxes()",
"        self.placed = []",
"        for i in range(self.columns * self.rows * self.layers):",
"            await self.place()",
"        return len(self.placed)",
]
lines[ri:ri+1] = body
ai = next(i for i, l in enumerate(lines) if "self.place()" in l and "return {" in l)
route = [
"        # pack: pack the whole pallet, answer with the count.",
"        if verb == " + chr(34) + "pack" + chr(34) + ":",
"            return {" + chr(34) + "placed" + chr(34) + ": await self.pack()}",
]
lines[ai+1:ai+1] = route
p.write_text("\n".join(lines))
print("patched pack and route")
