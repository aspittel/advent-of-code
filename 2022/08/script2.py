def check_right(row, height, to_check):
    visible_trees = 0
    while to_check < len(row):
        visible_trees += 1
        if row[to_check] >= height:
            return visible_trees
        to_check += 1
    return visible_trees


def check_left(row, height, to_check):
    visible_trees = 0
    while to_check >= 0:
        visible_trees += 1
        if row[to_check] >= height:
            return visible_trees
        to_check -= 1
    return visible_trees


def check_down(grid, height, to_check, col_idx):
    visible_trees = 0
    while to_check < len(grid):
        visible_trees += 1
        if grid[to_check][col_idx] >= height:
            return visible_trees
        to_check += 1
    return visible_trees


def check_up(grid, height, to_check, col_idx):
    visible_trees = 0
    while to_check >= 0:
        visible_trees += 1
        if grid[to_check][col_idx] >= height:
            return visible_trees
        to_check -= 1
    return visible_trees


def is_visible(grid, row_idx, col_idx):
    height = grid[row_idx][col_idx]
    row = grid[row_idx]
    return (check_right(row, height, col_idx + 1)
            * check_left(row, height, col_idx - 1) *
            check_down(grid, height, row_idx + 1, col_idx) *
            check_up(grid, height, row_idx - 1, col_idx))


with open('input.txt', 'r') as _file:
    grid = []
    for line in _file:
        grid.append([int(n) for n in line.strip()])
    max_surround = 0
    max_coords = None
    for idx, _ in enumerate(grid):
        for cidx, _ in enumerate(grid):
            surrounds = is_visible(grid, idx, cidx)
            if surrounds > max_surround:
                max_coords = (idx, cidx)
                max_surround = surrounds            
print(max_surround)
print(max_coords)
