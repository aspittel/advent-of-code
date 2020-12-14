START_TIME = 939
BUSES = [
    17,
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    41,
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    937,
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    13,
    "x",
    "x",
    "x",
    "x",
    23,
    "x",
    "x",
    "x",
    "x",
    "x",
    29,
    "x",
    397,
    "x",
    "x",
    "x",
    "x",
    "x",
    37,
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    "x",
    19,
]
filtered_buses = [bus for bus in BUSES if bus != "x"]
times = []

for bus in filtered_buses:
    time = START_TIME // bus
    next_time = (time + 1) * bus
    times.append(next_time)

print("Part 1", (min(times) - START_TIME) * filtered_buses[times.index(min(times))])


def extended_euclid(a, b):
    # FROM: https://github.com/TheAlgorithms/Python/blob/master/blockchain/chinese_remainder_theorem.py
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    return (y, x - (a // b) * y)


def chinese_remainder_theorem(num1, rem1, num2, rem2):
    (x, y) = extended_euclid(num1, num2)
    m = num1 * num2
    n = (rem2 * x * num1) + (rem1 * y * num2)
    return (m, (n % m + m) % m)


print(extended_euclid(19, 13))
# Solved first by finding the formulae for the sequences. Then in trying to combine, I found
# the Chinese Remainder Theorem.
# I used: https://pages.mtu.edu/~dcclark/MA4908/dnt/chinese3.html and
start_bus = BUSES[0]
start_idx = 0
for idx, bus in enumerate(BUSES[1:]):
    if bus == "x":
        continue
    start_bus, start_idx = chinese_remainder_theorem(start_bus, start_idx, bus, idx + 1)

print("Part 2", start_bus - start_idx)
