SERIAL_NUMBER = 1308

def get_power_level(x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += SERIAL_NUMBER
    power_level *= rack_id
    hundreds_digit = int(str(power_level)[-3]) if power_level > 100 else 0
    return hundreds_digit - 5


def gen_grid():
    grid = []
    for x in range(300):
        row = []
        for y in range(300):
            row.append(get_power_level(x+1, y+1))
        grid.append(row)
    return grid

def get_box(grid, row, col, size):
    _sum = 0
    for x in range(0, size):
        for y in range(0, size):
            _sum += grid[row + x][col + y]
    return _sum

def find_max_subgrid(grid):
    max_sum = 0
    coordinates = [0, 0]
    for size in range(3, 300):
        for i in range(300 - size):
            for j in range(300 - size):
                box_sum = get_box(grid, i, j, size)
                if box_sum > max_sum:
                    max_sum = box_sum
                    coordinates = [i + 1, j + 1, size]
        print(coordinates, size, max_sum)
    return coordinates, max_sum

print(find_max_subgrid(gen_grid()))