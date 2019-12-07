def get_modes(modes):
    return [int(mode) for mode in [modes[2], modes[1], modes[0], modes[3:]]]


def get_param(mode, increment, idx, data):
    if mode == 0:
        return data[data[idx + increment]]
    return data[idx + increment]

def get_params(mode1, mode2, idx, data):
    return get_param(mode1, 1, idx, data), get_param(mode2, 2, idx, data)


def add(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    data[data[idx + 3]] = param1 + param2
    return idx + 4

def multiply(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    data[data[idx + 3]] = param1 * param2
    return idx + 4

def less_than(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    data[data[idx + 3]] = 1 if param1 < param2 else 0
    return idx + 4

def equals(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    data[data[idx + 3]] = 1 if param1 == param2 else 0
    return idx + 4

def jump_if_true(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    return param2 if param1 != 0 else idx + 3

def jump_if_false(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    return param2 if param1 == 0 else idx + 3


def calculate(data, input_val):
    idx = 0
    diagnostic_code = None
    while data[idx] != 99:
        mode1, mode2, mode3, opcode = get_modes(f"{data[idx]:05}")
        OPCODES = {
            1: add,
            2: multiply,
            5: jump_if_true,
            6: jump_if_false,
            7: less_than,
            8: equals
        }
        if opcode in OPCODES:
            idx = OPCODES[opcode](mode1, mode2, idx, data)
        elif opcode == 3:
            data[data[idx+1]] = input_val
            idx += 2
        elif opcode == 4:
            diagnostic_code = data[data[idx + 1]]
            idx += 2
    return diagnostic_code


with open("input.txt") as _file:
    for line in _file:
        input_vals = [int(num) for num in line.split(",")]
        print(f"Part 1: {calculate(input_vals[:], 1)}")
        print(f"Part 2: {calculate(input_vals[:], 5)}")

