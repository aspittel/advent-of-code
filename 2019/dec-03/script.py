from shapely.geometry import LineString

def format_coords(coords):
    return [(val[0], int(val[1:])) for val in coords.split(",")]


def find_lines(paths):
    lines = []
    startX = 0
    startY = 0
    for direction, distance in paths:
        if direction == "R":
            endX = startX + distance
            lines.append(((startX, startY), (endX, startY)))
            startX = endX
        elif direction == "L":
            endX = startX - distance
            lines.append(((startX, startY), (endX, startY)))
            startX = endX
        elif direction == "D":
            endY = startY - distance
            lines.append(((startX, startY), (startX, endY)))
            startY = endY
        elif direction == "U":
            endY = startY + distance
            lines.append(((startX, startY), (startX, endY)))
            startY = endY
    return lines

def find_intersections(wire1, wire2):
    intersections = []
    for line1 in wire1:
        for line2 in wire2:
            line1 = LineString(line1)
            line2 = LineString(line2)
            if line1.intersects(line2):
                intersections.append(line1.intersection(line2))
    return intersections

def find_intersection_steps(wire1, wire2):
    intersections = []
    min_steps = None
    for idx1, line1 in enumerate(wire1):
        for idx2, line2 in enumerate(wire2):
            print(line1, line2)
            line1 = LineString(line1)
            line2 = LineString(line2)
            
            if line1.intersects(line2):
                steps = 0
                moves = wire1[:idx1]
                if moves:
                    moves.append((moves[-1][1], line1.intersection(line2).coords[:][0]))
                for coords in moves:
                    steps += sum((abs(coords[0][0] - coords[1][0]), abs(coords[0][1] - coords[1][1])))
                
                steps2 = 0
                moves2 = wire2[:idx2]
                if moves2:
                    moves2.append((moves2[-1][1], line1.intersection(line2).coords[:][0]))
                for coords in moves2:
                    steps2 += sum((abs(coords[0][0] - coords[1][0]), abs(coords[0][1] - coords[1][1])))
                if not min_steps:
                    min_steps = steps + steps2
                else:
                    min_steps = min((min_steps, steps + steps2))
    return min_steps

with open('input.txt') as _file:
    paths1 = format_coords(_file.readline())
    lines1 = find_lines(paths1)

    paths2 = format_coords(_file.readline())
    lines2 = find_lines(paths2)

manhattan_distances = []
for intersection in find_intersections(lines1, lines2):
    manhattan_distance = sum([abs(coord) for coord in intersection.coords[:][0]])
    if manhattan_distance > 0:
        manhattan_distances.append(manhattan_distance)

# Part 1
print(int(min(manhattan_distances)))

# Part 2
print(int(find_intersection_steps(lines1, lines2)))


