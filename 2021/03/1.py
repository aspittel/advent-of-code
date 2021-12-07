from collections import Counter

gamma_rate = ''
epsilon_rate = ''

def most_frequent(grid, col_number):
    col = ""
    for row in grid:
        col += row[col_number]
    return Counter(col).most_common(1)[0][0]


with open('input.txt', 'r') as _file:
    li = [list(n.strip()) for n in _file]
    for i in range(len(li[0])):
        more_frequent = most_frequent(li, i)
        gamma_rate += str(more_frequent)
        epsilon_rate += '0' if more_frequent == '1' else '1'
    
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    print(gamma_rate * epsilon_rate)
