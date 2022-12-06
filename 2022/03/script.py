import string

priorities = 0
with open('input.txt', 'r') as _file:
    for line in _file:
        halfway = len(line)//2
        c1, c2 = line[0:halfway], line[halfway:]
        (letter,) = set(c1).intersection(c2)
        priorities += string.ascii_letters.find(letter) + 1
print(priorities)

priorities = 0
with open('input.txt', 'r') as _file:
    badges = [badge.strip() for badge in _file]
    groups = [badges[x:x+3] for x in range(0, len(badges), 3)]
for group in groups:
    (priority,) = set(group[0].strip()).intersection(group[1]).intersection(group[2])
    priorities += string.ascii_letters.find(priority) + 1
print(priorities)