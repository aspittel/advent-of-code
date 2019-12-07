from collections import Counter

with open('input.txt', 'r') as f:
    twice = 0
    thrice = 0
    for line in f:
        counts = Counter(line).values()
        if 2 in counts:
            twice += 1
        if 3 in counts:
            thrice += 1
    print(twice * thrice)
