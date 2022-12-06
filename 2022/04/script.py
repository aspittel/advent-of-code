count = 0
p2_count = 0
with open('input.txt', 'r') as _file:
    ranges = [line.strip().split(',') for line in _file]
for pair in ranges:
    r_pair = []
    for _range in pair:
        (start, end) = _range.split('-')
        start, end = int(start), int(end)
        r_pair.append((start, end))
    if (r_pair[0][0] >= r_pair[1][0] and r_pair[0][1] <= r_pair[1][1]) or (r_pair[1][0] >= r_pair[0][0] and r_pair[1][1] <= r_pair[0][1]):
        count += 1
    if r_pair[0][0] <= r_pair[1][0] <= r_pair[0][1] or r_pair[1][0] <= r_pair[0][0] <= r_pair[1][1]:
        p2_count += 1
print(count)
print(p2_count)

