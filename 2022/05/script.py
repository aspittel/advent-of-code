crates = { 
    1: ['P', 'V', 'Z', 'W', 'D', 'T'],
    2: ['D', 'J', 'F', 'V', 'W', 'S', 'L'],
    3: ['H', 'B', 'T', 'V', 'S', 'L', 'M', 'Z'],
    4: ['J', 'S', 'R'],
    5: ['W', 'L', 'M', 'F', 'G', 'B', 'Z', 'C'],
    6: ['B', 'G', 'R', 'Z', 'H', 'V', 'W', 'Q'],
    7: ['N', 'D', 'B', 'C', 'P', 'J', 'V'],
    8: ['Q', 'B', 'T', 'P'],
    9: ['C', 'R', 'Z', 'G', 'H']
}

# crates = {
#     1: ['N', 'Z'],
#     2: ['D', 'C', 'M'],
#     3: ['P']
# }

# with open('input.txt', 'r') as _file:
#     for move in _file:
#         moves = move.strip().split(' ')
#         to_move, start, end = [int(moves[1]), int(moves[3]), int(moves[5])]
#         crates[end] = crates[start][0:to_move][::-1] + crates[end]
#         del crates[start][0:to_move]
# message = ''
# for _, crate in crates.items():
#     message += crate[0]
# print(message)

with open('input.txt', 'r') as _file:
    for move in _file:
        moves = move.strip().split(' ')
        to_move, start, end = [int(moves[1]), int(moves[3]), int(moves[5])]
        crates[end] = crates[start][0:to_move] + crates[end]
        del crates[start][0:to_move]
message = ''
for _, crate in crates.items():
    message += crate[0]
print(message)