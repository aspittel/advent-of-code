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

matrix = [[(0, 0) for i in range(max_x + 2)] for n in range(max_y + 2)]
for idx, (x, y) in enumerate(coords):
    matrix[x][y] = (idx+1, 0,)
    for r_idx, row in enumerate(matrix):
        for c_idx, col in enumerate(row):
            dist = abs(x - r_idx) + abs(y - c_idx)
            if col[0] == 0 or dist < col[1]: 
                matrix[r_idx][c_idx] = (idx+1, dist,)
            elif dist == col[1] and col[0] != idx+1:
                matrix[r_idx][c_idx] = (None, dist,)
        

matrix = [[i[0] for i in sublist] for sublist in matrix]
flipped_matrix = matrix[::-1]
to_filter = set(matrix[0] + matrix[-1] + flipped_matrix[0] + flipped_matrix[-1])
list_matrix = []

for row in matrix:
    for col in row:
        if col not in to_filter:
            list_matrix.append(col)

print(Counter(list_matrix).most_common(1)[0][1])
