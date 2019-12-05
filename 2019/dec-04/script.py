def check_ascending(n):
    return "".join(sorted(n)) == n


def check_repeat(n):
    for digit1, digit2 in zip(n, n[1:]):
        if digit1 == digit2:
            return True


def check_two_consecutive_digits(n):
    repeat_count = 0
    for n1, n2 in zip(n, n[1:]):
        if n1 == n2:
            repeat_count += 1
        else:
            if repeat_count == 1:
                return True
            repeat_count = 0
    return repeat_count == 1


p1_count = 0
p2_count = 0

for n in range(134792, 675811):
    n = str(n)
    if check_ascending(n):
        if check_repeat(n):
            p1_count += 1
        if check_two_consecutive_digits(n):
            p2_count += 1

print(f"Part 1: {p1_count}")
print(f"Part 2: {p2_count}")
