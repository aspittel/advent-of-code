from collections import Counter

with open('input.txt') as inp:
    groups = []
    group = set()
    for line in inp:
        if line != "\n":
            for letter in line.rstrip():
                group.add(letter)
        else:
            groups.append(len(group))
            group = set()
    groups.append(len(group))
    print("Part 1", sum(groups))

groups = []
group_len = 0
group = []
with open('input.txt') as inp:
    for line in inp:
            if line != "\n":
                group_len += 1
                for letter in line.rstrip():
                    group.append(letter)
            else:
                group_count = 0
                letter_counts = Counter(group)
                for letter in letter_counts:
                    if letter_counts[letter] == group_len:
                        group_count += 1
                groups.append(group_count)
                group_len = 0
                group = []
    group_count = 0
    letter_counts = Counter(group)
    for letter in letter_counts:
        if letter_counts[letter] == group_len:
            group_count += 1
    groups.append(group_count)
    print("Part 2", sum(groups))