def check_count_in_range(password, letter, start, stop):
    return password.count(letter) >= start and password.count(letter) <= stop


def check_indexes(password, letter, start, stop):
    return (password[start] == letter or password[stop] == letter) and (password[start] != password[stop])

with open('input.txt') as file:
    letters = [num.split(": ") for num in file]
    part1_tally = 0
    part2_tally = 0
    for policy, password in letters:
        length, letter = policy.split(" ")
        start, stop = length.split("-")
        start, stop = int(start), int(stop)

        # part 1
        if check_count_in_range(password, letter, start, stop): part1_tally += 1

        # part 2
        if check_indexes(password, letter, start - 1, stop - 1): part2_tally += 1
        

    print("Part 1", part1_tally)
    print("Part 2", part2_tally)