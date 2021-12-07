
count3 = 0
count = 0
with open('input.txt', 'r') as _file:
    li = [int(n) for n in _file]
    n = 0
    
    # Part 1
    for i, j in zip(li, li[1:]):
        if j > i:
            count += 1

    # Part 2
    while n < len(li) - 3:
        count1 = li[n] + li[n+1] + li[n+2]
        count2 = li[n+1] + li[n+2] + li[n+3]
        if li[n] + li[n+1] + li[n+2] < li[n+1] + li[n+2] + li[n+3]:
            count3 += 1
        n += 1
        
    print(count, count3)