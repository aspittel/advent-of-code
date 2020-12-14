with open('input.txt') as file:
    n = 0
    e = 0
    facing = 'E'
    directions =['N', 'E', 'S', 'W']
    for move in file:
        direction = move[0]
        coord = int(move[1:])
        if direction == 'R':
            to_move = coord // 90
            idx = (directions.index(facing) + to_move) % len(directions)
            facing = directions[idx]
        if direction == 'L':
            to_move = coord // 90
            idx = (directions.index(facing) - to_move) % len(directions)
            facing = directions[idx]
        if direction == 'F':
            direction = facing
        if direction == 'N':
            n += coord
        if direction == 'S':
            n -= coord
        if direction == 'E':
            e += coord
        if direction == 'W':
            e -= coord
    print(abs(n) + abs(e))