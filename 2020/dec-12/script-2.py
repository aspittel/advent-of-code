def spin(dir, coord, spin):
    directions = ['N', 'E', 'S', 'W']
    to_move = coord // 90
    if spin == 'L': to_move *= -1
    idx = (directions.index(dir) + to_move) % len(directions)
    return directions[idx]


def move_waypoint(_dir, oppdir, unit1, unit2, facing1, facing2):
    if facing1 == _dir:
        unit1 += coord
    elif facing1 == oppdir:
        unit1 -= coord
    elif facing2 == _dir:
        unit2 += coord
    else:
        unit2 -= coord
    return unit1, unit2

with open('input.txt') as file:
    ns = 0
    es = 0
    unit1 = 1
    unit2 = 10
    facing1 = 'N'
    facing2 = 'E'
    directions = ['N', 'E', 'S', 'W']
    for move in file:
        direction = move[0]
        coord = int(move[1:])
        if direction == 'R':
            facing1 = spin(facing1, coord, 'R')
            facing2 = spin(facing2, coord, 'R')
        if direction == 'L':
            facing1 = spin(facing1, coord, 'L')
            facing2 = spin(facing2, coord, 'L')
        if direction == 'F':
            if facing1 in ['N', 'S']:
                if facing1 == 'S':
                    ns -= unit1 * coord
                else:
                    ns += unit1 * coord
                if facing2 == 'E':
                    es += unit2 * coord
                else:
                    es -= unit2 * coord
            else:
                if facing1 == 'E':
                    es += unit1 * coord
                else:
                    es -= unit1 * coord
                if facing2 == 'S':
                    ns -= unit2 * coord
                else:
                    ns += unit2 * coord
        if direction == 'N':
            unit1, unit2 = move_waypoint('N', 'S', unit1, unit2, facing1, facing2)
        if direction == 'S':
            unit1, unit2 = move_waypoint('S', 'N', unit1, unit2, facing1, facing2)
        if direction == 'E':
            unit1, unit2 = move_waypoint('E', 'W', unit1, unit2, facing1, facing2)
        if direction == 'W':
            unit1, unit2 = move_waypoint('W', 'E', unit1, unit2, facing1, facing2)
    print(abs(ns) + abs(es))