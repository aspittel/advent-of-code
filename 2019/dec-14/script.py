chemicals = {}

with open("input.txt") as _file:
    for line in _file:
        inp, out = line.strip().split(" => ")
        inp_vals = [i.split(", ") for i in inp]
        out_vals = [o.split(" ") for o in out]
        chemicals[out] = inp

print(chemicals)