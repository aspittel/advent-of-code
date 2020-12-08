from collections import Counter

def get_group_count(group):
    group_count = 0
    letter_counts = Counter(group)
    for letter in letter_counts:
        if letter_counts[letter] == group_len:
            group_count += 1
    return group_count


with open('input.txt') as inp:
    group = []
    groups_anyone = []
    groups_everyone = []
    group_len = 0
    for line in inp:
        if line != "\n":
            group_len += 1
            for letter in line.rstrip():
                group.append(letter)
        else:
            groups_everyone.append(get_group_count(group))
            groups_anyone.append(len(set(group)))
            group_len = 0
            group = []

    groups_anyone.append(len(set(group)))
    groups_everyone.append(get_group_count(group))
    
    print("Part 1", sum(groups_anyone))
    print("Part 2", sum(groups_everyone))
