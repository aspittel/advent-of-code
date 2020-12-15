moves = {}
turns = 1
with open('input.txt') as file:
    nums = file.readlines()[0]
    nums = [int(n) for n in nums.split(',')]
    move = nums.pop()
    for n in nums:
        moves[n] = turns
        turns += 1

# for the popped move
turns += 1

while turns < 30000001:
    if move in moves:
        last_time = moves[move]
        next_move = turns - 1 - last_time
    else:
        next_move = 0
    moves[move] = turns - 1
    turns += 1
    move = next_move
print(move)
