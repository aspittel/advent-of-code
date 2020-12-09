def check_valid(num, stack):
    current_sum = 0
    for val in stack:
        if num - val in stack:
            return True


looking_for = 1038347917
with open('input.txt') as file:
    nums = [int(num) for num in file]
    stack = nums[:25]
    for num in nums[25:]:
        if not check_valid(num, stack):
            print("Part 1", num)
            break
        stack.pop(0)
        stack.append(num)

    for idx, num in enumerate(nums):
        vals = [num]
        tracking_sum = 0
        curr_idx = idx
        while tracking_sum < looking_for:
            tracking_sum += nums[curr_idx]
            vals.append(nums[curr_idx])
            curr_idx += 1
        if tracking_sum == looking_for:
            print(vals)
            print("Part 2", max(vals) + min(vals))
            break