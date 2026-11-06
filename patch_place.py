import pathlib
p = pathlib.Path("src/models/palletizer.py")
lines = p.read_text().split("\n")
pi = next(i for i, l in enumerate(lines) if l.strip() == "async def place(self):")
ki = next(i for i, l in enumerate(lines) if l.strip() == "async def pack(self):")
ri = next(i for i in range(pi, ki) if lines[i].strip().startswith("raise NotImplementedError"))
body = pathlib.Path("place_body.txt").read_text().split("\n")
if body and body[-1] == "":
    body.pop()
lines[ri:ri+1] = body
ai = next(i for i, l in enumerate(lines) if l.strip() == "# return what it returns.")
route = [
"        # place: put one box in the next slot, answer the slot.",
"        if verb == " + chr(34) + "place" + chr(34) + ":",
"            return {" + chr(34) + "slot" + chr(34) + ": await self.place()}",
]
lines[ai+1:ai+1] = route
p.write_text("\n".join(lines))
print("patched place and route")
