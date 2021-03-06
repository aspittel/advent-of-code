def format_coords(coords):
    return [(val[0], int(val[1:])) for val in coords.split(",")]

DIRECTIONS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

def find_points(paths):
    points = {}
    
    x = 0
    y = 0
    steps = 0

    for direction, distance in paths:
        for point in range(distance):
            x_change, y_change = DIRECTIONS[direction]
            x += x_change
            y += y_change
            steps += 1
            points[(x, y)] = steps

    return points


def intersections(points1, points2):
    return set(points1.keys()).intersection(set(points2.keys()))


def manhattan_distances(points):
    return [abs(x) + abs(y) for x, y in points]


def least_steps(intersections, points1, points2):
    return [points1[point] + points2[point] for point in intersections]


with open("input.txt") as _file:
    paths1 = format_coords(_file.readline())
    points1 = find_points(paths1)

    paths2 = format_coords(_file.readline())
    points2 = find_points(paths2)

    intersections = intersections(points1, points2)

    print(f"Part 1: {min(manhattan_distances(intersections))}")

    print(f"Part 1: {min(least_steps(intersections, points1, points2))}")