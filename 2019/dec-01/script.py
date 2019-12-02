from math import floor

# Part 1
def get_fuel(mass):
    return floor(mass / 3) - 2

# Part 2
def get_fuel_recursive(mass, running_sum=0):
    if mass <= 0: return running_sum
    new_fuel = get_fuel(mass)
    return get_fuel_recursive(new_fuel, running_sum + max(0, new_fuel))


recursive_sum = 0
non_recursive_sum = 0
with open("input.txt") as file:
    for line in file:
        mass = int(line)
        recursive_sum += get_fuel_recursive(mass)
        non_recursive_sum += get_fuel(mass)

print(f"Part 1: {non_recursive_sum}")
print(f"Part 2: {recursive_sum}")
