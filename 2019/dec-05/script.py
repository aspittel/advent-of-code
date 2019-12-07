def get_modes(modes):
    return [int(mode) for mode in [modes[2], modes[1], modes[0], modes[3:]]]


def get_param(mode, increment, idx, data):
    if mode == 0:
        return data[data[idx + increment]]
    return data[idx + increment]

def get_params(mode1, mode2, idx, data):
    return get_param(mode1, 1, idx, data), get_param(mode2, 2, idx, data)


def call_operation(mode1, mode2, idx, data, operation):
    param1, param2 = get_params(mode1, mode2, idx, data)
    return operation(param1, param2), idx + 4

def add(param1, param2):
    return param1 + param2

def multiply(param1, param2):
    return param1 * param2

def less_than(param1, param2):
    return 1 if param1 < param2 else 0

def equals(param1, param2):
    return 1 if param1 == param2 else 0

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
        OPERATIONS = {1: add, 2: multiply, 7: less_than, 8: equals}
        if opcode in OPERATIONS:
            data[data[idx + 3]], idx = call_operation(
                mode1, mode2, idx, data, OPERATIONS[opcode]
            )
        elif opcode == 3:
            data[data[idx + 1]] = input_val
            idx += 2
        elif opcode == 4:
            diagnostic_code = data[data[idx + 1]]
            idx += 2
        elif opcode == 5:
            idx = jump_if_true(mode1, mode2, idx, data)
        elif opcode == 6:
            idx = jump_if_false(mode1, mode2, idx, data)
    return diagnostic_code


with open("input.txt") as _file:
    for line in _file:
        input_vals = [int(num) for num in line.split(",")]
        print(f"Part 1: {calculate(input_vals[:], 1)}")
        print(f"Part 2: {calculate(input_vals[:], 5)}")

