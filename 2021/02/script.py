horizontal1 = 0
depth1 = 0

horizontal2 = 0
depth2 = 0
aim = 0

with open('input.txt', 'r') as _file:
    li = [n.strip().split(" ") for n in _file]
    li = [(n[0], int(n[1])) for n in li]
    for direction, coord in li:
        if direction == "forward":
            horizontal1 += coord
            horizontal2 += coord
            depth2 += aim * coord
        if direction == "down":
            aim += coord
            depth1 += coord
        if direction == "up":
            aim -= coord 
            depth1 -= coord       

print(horizontal1 * depth1)
print(horizontal2 * depth2)