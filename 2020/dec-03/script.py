import math

right_list = [1, 3, 5, 7, 1]
down_list = [1, 1, 1, 1, 2]

def get_trees_for_slope(right, down, lines):
    x = right
    y = down
    trees = 0
    while y < len(lines):
        if x > len(lines[y]) - 1:
            x = x % len(lines[y])
        if lines[y][x] == '#':
            trees += 1
        x += right
        y += down
    return trees


with open('input.txt') as inp:
    lines = [line for line in inp]
    height = len(lines)
    width = len(lines[0])
    lines = [list(line.rstrip()) for line in lines]

    print("Part 1", get_trees_for_slope(3, 1, lines))

    all_trees = 1
    for (right, down) in zip(right_list, down_list):
        all_trees *= get_trees_for_slope(right, down, lines)
    
    print("Part 2", all_trees)