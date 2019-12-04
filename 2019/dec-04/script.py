increasing_numbers = set()

def check_number(n):
    double_digit = False
    n_repeating = 0
    n = str(n)
    for n1, n2 in zip(n, n[1:]):
        if n1 > n2:
            return False
        elif n1 == n2:
            n_repeating += 1
        else:
            if n_repeating == 1:
                double_digit = True
            n_repeating = 0
    # catch a repeat at the end
    if n_repeating == 1:
        double_digit = True
    return double_digit 

good_passwords_count = 0
for n in range(134792, 675810 + 1):
    if check_number(n):
        good_passwords_count += 1
print(good_passwords_count)
