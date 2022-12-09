def check_right(height, row, to_check):
    while to_check < len(row):
        if height <= row[to_check]:
            return False
        to_check += 1
    return True


def check_left(height, row, to_check):
    while to_check >= 0:
        if height <= row[to_check]:
            return False
        to_check -= 1
    return True


def check_down(grid, height, to_check, col_idx):
    while to_check < len(grid):
        if height <= grid[to_check][col_idx]: return False
        to_check += 1
    return True


def check_up(grid, height, to_check, col_idx):
    while to_check >= 0:
        if height <= grid[to_check][col_idx]: return False
        to_check -= 1
    return True


def is_visible(grid, row_idx, col_idx):
    height = grid[row_idx][col_idx]
    row = grid[row_idx]
    return (check_right(height, row, col_idx + 1)
            or check_left(height, row, col_idx - 1) or
            check_down(grid, height, row_idx + 1, col_idx) or
            check_up(grid, height, row_idx - 1, col_idx))

with open('input.txt', 'r') as _file:
    grid = []
    for line in _file:
        grid.append([int(n) for n in line.strip()])
    count = 0
    for idx, _ in enumerate(grid):
        for cidx, _ in enumerate(grid):
            if is_visible(grid, idx, cidx):
                count += 1
    print(count)
