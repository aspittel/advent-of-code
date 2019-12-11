from math import atan2, sqrt, degrees, pi
from collections import defaultdict

def angle(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    # atan2 will give us different degrees for different
    # distances: https://gamedev.stackexchange.com/questions/14602/what-are-atan-and-atan2-used-for-in-games
    return atan2(y2 - y1, x2 - x1)


def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def get_points(_file):
    points = []
    for y, line in enumerate(_file):
        for x, char in enumerate(line):
            if char == "#":
                points.append((x, y))
    return points


def get_best_location(points):
    visibilities = [(p1, len(set(angle(p1, p2) for p2 in points))) for p1 in points]
    return max(visibilities, key=lambda point: point[1])


def get_visibilities(best_point, points):
    visibilities = defaultdict(list)
    points.remove(best_point)
    for point in points:
        line = degrees(angle(point, best_point))
        visibilities[line].append((point, distance(point, best_point)))
    return visibilities


def sort_by_distance(degrees):
    for degree in degrees.keys():
        degrees[degree].sort(key=lambda point: point[1], reverse=True)


def get_quadrants(angles):
    quadrant1 = sorted([angle for angle in angles.keys() if angle >= 90])
    quadrant2 = sorted([angle for angle in angles.keys() if angle <= -90])
    quadrant3 = sorted([angle for angle in angles.keys() if angle < 0 and angle >= -90])
    quadrant4 = sorted([angle for angle in angles.keys() if angle >= 0 and angle < 90])
    return quadrant1 + quadrant2 + quadrant3 + quadrant4


def order_quadrants(angles, quadrants):
    ordered_visibilities = {}

    for angle in quadrants:
        ordered_visibilities[angle] = visibilities[angle]

    return ordered_visibilities


def vaporize(visibilities, stop_idx):
    pops = 1
    while True:
        for point in ordered_visibilities.keys():
            if ordered_visibilities[point]:
                item = ordered_visibilities[point].pop()
                if pops == stop_idx:
                    return item[0]
                pops += 1


with open("input.txt") as _file:
    points = get_points(_file)


best_point, max_visible = get_best_location(points)
print(f"Part 1: {max_visible}")

visibilities = get_visibilities(best_point, points)
sort_by_distance(visibilities)

quadrants = get_quadrants(visibilities)
ordered_visibilities = order_quadrants(visibilities, quadrants)

x, y = vaporize(ordered_visibilities, 200)
print(f"Part 2: {x * 100 + y}")
