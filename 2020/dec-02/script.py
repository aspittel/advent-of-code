with open('input.txt') as file:
    letters = [num.split(": ") for num in file]
    tally = 0
    tally2 = 0
    for policy, password in letters:
        length, letter = policy.split(" ")
        start, stop = length.split("-")
        start, stop = int(start), int(stop)

        # part 1
        if password.count(letter) >= start and password.count(letter) <= stop:
            tally += 1

        # part 2
        start, stop = start - 1, stop - 1
        try:
            if (password[start] == letter or password[stop] == letter) and (password[start] != password[stop]):
                tally2 += 1
        except:
            pass
        

    print(tally)
    print(tally2)