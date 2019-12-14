from itertools import permutations

def get_permutations(li):
    for permutation in permutations(li):
        yield permutation

def get_modes(modes):
    return [int(mode) for mode in [modes[2], modes[1], modes[0], modes[3:]]]


class Computer:
    def __init__(self, data):
        self.idx = 0
        self.data = data[:]
        self.done = False
        self.output = None
        self.inputs = []

    def get_params(self, mode1, mode2):
        return self.get_param(mode1, 1), self.get_param(mode2, 2)

    def get_param(self, mode, increment):
        if mode == 0:
            return self.data[self.data[self.idx + increment]]
        return self.data[self.idx + increment]

    def add(self, mode1, mode2):
        param1, param2 = self.get_params(mode1, mode2)
        self.data[self.data[self.idx + 3]] = param1 + param2
        self.idx += 4

    def multiply(self, mode1, mode2):
        param1, param2 = self.get_params(mode1, mode2)
        self.data[self.data[self.idx + 3]] = param1 * param2
        self.idx += 4

    def take_input(self):
        self.data[self.data[self.idx + 1]] = self.inputs.pop(0)
        self.idx += 2

    def create_output(self):
        self.output = self.data[self.data[self.idx + 1]]
        self.idx += 2
        return self.output

    def less_than(self, mode1, mode2):
        param1, param2 = self.get_params(mode1, mode2)
        self.data[self.data[self.idx + 3]] = 1 if param1 < param2 else 0
        self.idx += 4

    def equals(self, mode1, mode2):
        param1, param2 = self.get_params(mode1, mode2)
        self.data[self.data[self.idx + 3]] = 1 if param1 == param2 else 0
        self.idx += 4

    def jump_if_true(self, mode1, mode2):
        param1, param2 = self.get_params(mode1, mode2)
        self.idx = param2 if param1 != 0 else self.idx + 3

    def jump_if_false(self, mode1, mode2):
        param1, param2 = self.get_params(mode1, mode2)
        self.idx = param2 if param1 == 0 else self.idx + 3

    def calculate(self, input_val):
        self.inputs.append(input_val)
        modes = {
            1: lambda: self.add(mode1, mode2),
            2: lambda: self.multiply(mode1, mode2),
            3: lambda: self.take_input(),
            5: lambda: self.jump_if_true(mode1, mode2),
            6: lambda: self.jump_if_false(mode1, mode2),
            7: lambda: self.less_than(mode1, mode2),
            8: lambda: self.equals(mode1, mode2)
        }
        while True:
            mode1, mode2, mode3, opcode = get_modes(f"{self.data[self.idx]:05}")
            if opcode in modes:
                modes[opcode]()              
            elif opcode == 4:
                return self.create_output()                
            elif opcode == 99:
                self.done = True
                return self.output


def max_output_signal(input_vals):
    max_output_signal = 0
    for permutation in get_permutations([0, 1, 2, 3, 4]):
        output_signal = 0
        for input_signal in permutation:
            computer = Computer(input_vals)
            computer.inputs.append(input_signal)
            output_signal = computer.calculate(output_signal)
        max_output_signal = max(max_output_signal, output_signal)
    return max_output_signal


def max_output_signal_feedback_loop(input_vals):
    max_output_signal = 0
    for permutation in get_permutations([5, 6, 7, 8, 9]):
        computers = [Computer(input_vals) for _ in range(5)]
        output_signal = 0
        for computer, phase_setting in zip(computers, permutation):
            computer.inputs.append(phase_setting)
        while computers[-1].done == False:
            for computer in computers:
                output_signal = computer.calculate(output_signal)
        max_output_signal = max(output_signal, max_output_signal)
    return max_output_signal
    


with open("input.txt") as _file:
    for line in _file:
        input_vals = [int(num) for num in line.split(",")]
        print(f"Part 1: {max_output_signal(input_vals)}")
        print(f"Part 2: {max_output_signal_feedback_loop(input_vals)}")