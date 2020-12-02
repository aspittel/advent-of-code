with open('input.txt') as file:
    letters = [num.split(": ") for num in file]
    tally = 0
    for policy, password in letters:
        length, letter = policy.split(" ")
        start, stop = length.split("-")
        start, stop = int(start) - 1, int(stop) - 1
        try:
            if (password[start] == letter or password[stop] == letter) and (password[start] != password[stop]):
                tally += 1
                print(password)
        except:
            pass
        

    print(tally)