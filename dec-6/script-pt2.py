from collections import Counter

with open('input.txt', 'r') as f:
    coords = []
    max_x = 0
    max_y = 0
    for line in f:
        line = [int(i) for i in line.strip().split(', ')]
        if line[0] > max_x: max_x = line[0]
        if line[1] > max_y: max_y = line[1]
        coords.append((line[1], line[0],))

n_regions = 0
matrix = [[(0, 0) for i in range(max_x + 2)] for n in range(max_y + 2)]
for r_idx, row in enumerate(matrix):
    for c_idx, col in enumerate(row):
        total_dist = 0
        for idx, (x, y) in enumerate(coords):
            dist = abs(x - r_idx) + abs(y - c_idx)
            total_dist += dist
        if total_dist < 10000:
            n_regions += 1

print(n_regions)