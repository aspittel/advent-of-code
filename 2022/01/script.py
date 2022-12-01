running_sum = 0
sums = []
with open('input.txt', 'r') as _file:
    for line in _file:
        if line == "\n":
            sums.append(running_sum)
            running_sum = 0
        else:
            running_sum += int(line)
sums.append(running_sum)

# part 1
print(max(sums))

# part 2
print(sum(sorted(sums, reverse=True)[0:3]))
            
