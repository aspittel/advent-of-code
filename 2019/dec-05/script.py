def get_modes(modes):
    return [int(mode) for mode in [modes[2], modes[1], modes[0], modes[3:]]]


def get_val(mode, increment, idx, data):
    if mode == 0:
        return data[data[idx + increment]]
    return data[idx + increment]

def get_vals(mode1, mode2, idx, data):
    return get_val(mode1, 1, idx, data), get_val(mode2, 2, idx, data)


def add(mode1, mode2, idx, data):
    val1, val2 = get_vals(mode1, mode2, idx, data)
    data[data[idx + 3]] = val1 + val2

def multiply(mode1, mode2, idx, data):
    val1, val2 = get_vals(mode1, mode2, idx, data)
    data[data[idx + 3]] = val1 * val2

def less_than(mode1, mode2, idx, data):
    val1, val2 = get_vals(mode1, mode2, idx, data)
    data[data[idx + 3]] = 1 if val1 < val2 else 0

def equals(mode1, mode2, idx, data):
    val1, val2 = get_vals(mode1, mode2, idx, data)
    data[data[idx + 3]] = 1 if val1 == val2 else 0

def jump_if_true(mode1, mode2, idx, data):
    val1, val2 = get_vals(mode1, mode2, idx, data)
    return val2 if val1 != 0 else idx + 3

def jump_if_false(mode1, mode2, idx, data):
    val1, val2 = get_vals(mode1, mode2, idx, data)
    return val2 if val1 == 0 else idx + 3


def calculate(data, input_val):
    idx = 0
    diagnostic_code = None
    while data[idx] != 99:
        modes = str(data[idx]).zfill(5)
        mode1, mode2, mode3, opcode = get_modes(modes)
        if opcode == 1:
            add(mode1, mode2, idx, data)
            idx += 4
        elif opcode == 2:
            multiply(mode1, mode2, idx, data)
            idx += 4
        elif opcode == 3:
            data[data[idx+1]] = input_val
            idx += 2
        elif opcode == 4:
            diagnostic_code = data[data[idx + 1]]
            idx += 2
        elif opcode == 5:
            idx = jump_if_true(mode1, mode2, idx, data)
        elif opcode == 6:
            idx = jump_if_false(mode1, mode2, idx, data)
        elif opcode == 7:
            less_than(mode1, mode2, idx, data)
            idx += 4
        elif opcode == 8:
            equals(mode1, mode2, idx, data)
            idx += 4
    return diagnostic_code


with open("input.txt") as _file:
    for line in _file:
        input_values = [int(num) for num in line.split(",")]
        print(f"Part 1: {calculate(input_values[:], 1)}")
        print(f"Part 2: {calculate(input_values[:], 5)}")

