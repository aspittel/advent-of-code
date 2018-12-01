data = open('input.txt', 'r')
total = 0
for line in data:
    total += int(line)
print(total)