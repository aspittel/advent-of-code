from collections import Counter


n_days = 256

with open('input.txt', 'r') as _file:
    for line in _file:
        fish = [int(n) for n in line.split(',')]

fish = dict(Counter(fish))

new_count = {}
while n_days > 0:
    for days, count in fish.items():
        if days != 0:
            if (days - 1) in new_count:
                new_count[days-1] += count
            else:
                new_count[days-1] = count
        else:
            if 6 in new_count: 
                new_count[6] += count
            else:
                new_count[6] = count
            new_count[8] = count
    fish = new_count
    new_count = {}
    n_days -= 1

print(sum(fish.values()))