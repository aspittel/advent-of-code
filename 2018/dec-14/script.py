vals = [3, 7]
a_idx, b_idx = 0, 1

INPUT_SCORE = 894501

def get_new_score(a, b):
    return [int(i) for i in str(a + b)]

def increase_idx(idx):
    return (idx + int(vals[idx]) + 1) % len(vals)

# Part 1
for _ in range(10 + INPUT_SCORE):
    vals += get_new_score(vals[a_idx], vals[b_idx])
    a_idx, b_idx = increase_idx(a_idx), increase_idx(b_idx)

print(''.join(str(val) for val in vals)[INPUT_SCORE:INPUT_SCORE+10])


INPUT_SCORE = str(INPUT_SCORE)

# Part 2
while True:
    vals += get_new_score(vals[a_idx], vals[b_idx])
    p1, p2 = ''.join(str(i) for i in vals[-len(INPUT_SCORE):]), ''.join(str(i) for i in vals[-len(INPUT_SCORE) - 1: -1])
    if INPUT_SCORE == p1 or INPUT_SCORE == p2:
        to_s = ''.join(str(i) for i in vals)
        print(to_s.find(INPUT_SCORE))
        break
    a_idx, b_idx = increase_idx(a_idx), increase_idx(b_idx)
