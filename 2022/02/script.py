import string

losses = {2: 3, 3: 1, 1: 2}
wins = {3: 2, 1: 3, 2: 1}

score = 0
with open('input.txt', 'r') as _file:
    for line in _file:
        [elf, me] = line.strip().split(' ')
        elf, me = string.ascii_uppercase.index(elf) + 1, string.ascii_uppercase.index(me) - 22
        score += me
        if elf == me: score += 3
        if wins[me] == elf: score += 6
# Part 1
print(score)

score = 0
with open('input.txt', 'r') as _file:
    for line in _file:
        [elf, me] = line.strip().split(' ')
        elf = string.ascii_uppercase.index(elf) + 1
        if me == 'Y': score += elf + 3
        elif me == 'X': score += wins[elf]
        elif me == 'Z': score += 6 + losses[elf]
# Part 2
print(score)