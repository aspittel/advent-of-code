def clean_data(_file):
    orbits = {}
    objects = set()

    for line in _file:
        to_orbit, orbiter = line.rstrip().split(")")
        orbits[orbiter] = to_orbit
        objects.add(to_orbit)
        objects.add(orbiter)
    
    return orbits, objects


def get_orbit(current_obj, orbits):
    if current_obj == "COM": return []
    return [orbits[current_obj]] + get_orbit(orbits[current_obj], orbits)


def get_total_orbits(orbits):
    return sum(len(get_orbit(obj, orbits)) for obj in objects)


def path_between(start, end, orbits):
    start_path, end_path = get_orbit(start, orbits), get_orbit(end, orbits)
    # Get the first point that is in both paths
    overlapping_point = [i for i in start_path if i in end_path][0]
    return start_path.index(overlapping_point) + end_path.index(overlapping_point)


with open("input.txt") as _file:
    orbits, objects = clean_data(_file)

print(f"Part 1: {get_total_orbits(orbits)}")
print(f'Part 2: {path_between("YOU", "SAN", orbits)}')
