with open("input.txt") as _file:
    nums = [int(line) for line in _file]
    set_nums = set(nums)
    for num in nums:
        for num2 in nums:
            if (2020 - num - num2) in set_nums:
                print(num * (2020-num-num2) * num2)
                break
