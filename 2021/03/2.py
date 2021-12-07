from collections import Counter

gamma_rate = ''
epsilon_rate = ''

def oxygen(grid, col_number):
    col = ""
    for row in grid:
        col += row[col_number]
    return '1' if Counter(col)['1'] >= Counter(col)['0'] else '0'

def co2(grid, col_number):
    col = ""
    for row in grid:
        col += row[col_number]
    return '1' if Counter(col)['0'] > Counter(col)['1'] else '0'

with open('input.txt', 'r') as _file:
    oxyli = [list(n.strip()) for n in _file]
    co2li = oxyli[::]

    for i in range(len(oxyli[0])):
        more_frequent = oxygen(oxyli, i)
        oxyli = [n for n in oxyli if n[i] == more_frequent]
        if len(oxyli) == 1:  o = int(''.join(oxyli[0]), 2)
        
        least_frequent = co2(co2li, i)
        co2li = [n for n in co2li if n[i] == least_frequent]
        if len(co2li) == 1: c = int(''.join(co2li[0]), 2)

print(o * c)
