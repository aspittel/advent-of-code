import string
score = 0

with open('input.txt', 'r') as _file:
    for line in _file:
        [elf, me] = line.strip().split(' ')
        elf, me = string.ascii_uppercase.index(elf) + 1, string.ascii_uppercase.index(me) - 22
        score += me
        if elf == me: score += 3
        if (me == 3 and elf == 2) or (me == 1 and elf == 3) or (me == 2 and elf == 1): 
            score += 6
# Part 1
print(score)

wins = {2: 3, 3: 1, 1: 2}
losses = {3: 2, 1: 3, 2: 1}
score = 0
with open('input.txt', 'r') as _file:
    for line in _file:
        [elf, me] = line.strip().split(' ')
        elf = string.ascii_uppercase.index(elf) + 1
        if me == 'Y': # tie
            score += elf + 3
        if me == 'X': # loss
            score += losses[elf]
        if me == 'Z': # win
            score += 6 + wins[elf]
# Part 2
print(score)