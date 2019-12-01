with open('sample-input.txt', 'r') as f:
    rules = {}
    for idx, line in enumerate(f):
        if idx == 0: 
            state = line.strip()
        elif idx > 1:
            rule = line.strip().split(" => ")
            rules[rule[0]] = rule[1]


def get_score(state, n_change):
    n_change *= -1
    score = 0
    for l in state:
        if l == "#":
            score += n_change
        n_change += 1
    return score


n_change = 0
for _ in range(20): #1000 for large input
    n_change += 4
    state = "...." + state + "...."
    new_state = ""
    for idx, val in enumerate(state):
        left_chunk = state[idx-2:idx]
        right_chunk = state[idx+1:idx+3]
        chunk = left_chunk + val + right_chunk
        if chunk in rules:
            new_state += rules[chunk]
        else:
            new_state += "."
    start = 0
    while new_state[start] == ".":
        start += 1
    n_change -= start
    end = len(new_state) - 1
    while new_state[end] == ".":
        end -= 1
    state = new_state[start:end+1]

# uncomment for pt2
# score = get_score(state, n_change)
# print(((50_000_000_000 - 1000) * 42) + score)

print(get_score(state, n_change))