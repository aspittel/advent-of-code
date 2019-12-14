import re
from itertools import combinations


def greatest_common_denominator(a, b):
    while b:      
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
	return (a * b) / greatest_common_denominator(a, b)


def create_data():
    points = []
    with open("input.txt") as _file:
        for line in _file:
            points.append({"coordinate": [int(n) for n in re.findall(r'-?\d+', line)]})
    for point in points:
        point["velocity"] = [0, 0, 0]
    return points


def check_seen(seen, first_overlap, points, move):
    for idx, coord in enumerate(seen):
        if not first_overlap[idx]:
            coords = ''.join([str(i["coordinate"][idx]) for i in points] + [str(i["velocity"][idx]) for i in points])
            if coords not in seen[idx]:
                seen[idx].add(coords)
            else:
                first_overlap[idx] = move
    return seen, first_overlap


def move_points(points):
    for point in points:
        for idx, (coord, velocity) in enumerate(zip(point["coordinate"], point["velocity"])):
            point["coordinate"][idx] += velocity
    return points


def change_velocity(points):
    point_pairs = combinations(points, 2)
    for point, other_point in point_pairs:
        for idx, coord in enumerate(point["coordinate"]):
            other_coord = other_point["coordinate"][idx]
            if coord > other_coord:
                point["velocity"][idx] -= 1
                other_point["velocity"][idx] += 1
            elif coord < other_coord:
                point["velocity"][idx] += 1
                other_point["velocity"][idx] -= 1
    return points


def calculate_energy(points):
    total_energy = 0
    for point in points:
        x, y, z = point["coordinate"]
        vx, vy, vz = point["velocity"]
        total_energy += (abs(x) + abs(y) + abs(z)) * (abs(vx) + abs(vy) + abs(vz))
    print(f"Part 1: {total_energy}")


def simulate_motion(points):
    seen = [set(), set(), set()]
    first_overlap = [None, None, None]
    move = 0
    while None in first_overlap:
        seen, first_overlap = check_seen(seen, first_overlap, points, move)
        move += 1
        points = change_velocity(points)
        points = move_points(points)
        if move == 1000:
            calculate_energy(points)
    return first_overlap


points = create_data()
first_overlap = simulate_motion(points)

print(f"Part 2: {int(least_common_multiple(least_common_multiple(first_overlap[0], first_overlap[1]), first_overlap[2]))}")
