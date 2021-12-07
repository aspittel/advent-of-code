def clean_line(line, char):
    return [int(n) for n in line.split(char) if n]

with open('input.txt', 'r') as _file:
    inputs = [n.strip() for n in _file]

draws = clean_line(inputs[0], ',')
boards = []
board = []

for line in inputs[2:]:
    if line.strip() == '':
        boards.append(board)
        board = []
    else:
        board.append(clean_line(line.strip(), ' '))


def find_bingo(boards, draws):
    for d in draws:
        for board in range(len(boards)):
            for row in range(len(boards[board])):
                for val in range(len(boards[board][row])):
                    if boards[board][row][val] == d:
                        boards[board][row][val] = -1
                    if sum(boards[board][row]) == -5:
                        return d, board
                    total = 0
                    for r in boards[board]:
                        total += r[val]
                    if total == -5: return d, board

while len(boards):
    d, board = find_bingo(boards, draws)
    final_board = boards.pop(board)

_sum = 0
for row in final_board:
    for val in row:
        if val != -1:
            _sum += val

print(_sum * d)
            
