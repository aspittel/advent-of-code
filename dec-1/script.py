with open('input.txt', 'r') as data:
    total = 0
    for line in data:
        total += int(line)
    print(total)

# Could also do print(sum(int(i) for i in open('input.txt', 'r')))