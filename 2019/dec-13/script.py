def get_modes(modes):
    return [int(mode) for mode in [modes[2], modes[1], modes[0], modes[3:]]]


class Computer:
    def __init__(self, data):
        self.idx = 0
        self.data = data[:] + [0] * 3000
        self.done = False
        self.output = None
        self.inputs = []
        self.relative_base = 0

    def get_params(self, mode1, mode2, mode3):
        return self.get_param(mode1, 1), self.get_param(mode2, 2), self.get_param(mode3, 3)

    def get_param(self, mode, increment):
        if mode == 0:
            return self.data[self.idx + increment]
        elif mode == 1:
            return self.idx + increment
        else:
            return self.relative_base + self.data[self.idx + increment]

    def add(self, mode1, mode2, mode3):
        param1, param2, param3 = self.get_params(mode1, mode2, mode3)
        self.data[param3] = self.data[param1] + self.data[param2]
        self.idx += 4

    def multiply(self, mode1, mode2, mode3):
        param1, param2, param3 = self.get_params(mode1, mode2, mode3)
        self.data[param3] = self.data[param1] * self.data[param2]
        self.idx += 4

    def take_input(self, mode1):
        param1 = self.get_param(mode1, 1)
        self.data[param1] = input_data
        self.idx += 2

    def create_output(self, mode1):
        param1 = self.get_param(mode1, 1)
        self.output = self.data[param1]
        self.idx += 2
        return self.output

    def less_than(self, mode1, mode2, mode3):
        param1, param2, param3 = self.get_params(mode1, mode2, mode3)
        self.data[param3] = 1 if self.data[param1] < self.data[param2] else 0
        self.idx += 4

    def equals(self, mode1, mode2, mode3):
        param1, param2, param3 = self.get_params(mode1, mode2, mode3)
        self.data[param3] = 1 if self.data[param1] == self.data[param2] else 0
        self.idx += 4

    def jump_if_true(self, mode1, mode2, mode3):
        param1, param2, param3 = self.get_params(mode1, mode2, mode3)
        self.idx = self.data[param2] if self.data[param1] != 0 else self.idx + 3

    def jump_if_false(self, mode1, mode2, mode3):
        param1, param2, param3 = self.get_params(mode1, mode2, mode3)
        self.idx = self.data[param2] if self.data[param1] == 0 else self.idx + 3

    def relative_offset(self, mode1):
        param1 = self.get_param(mode1, 1)
        self.relative_base += self.data[param1]
        self.idx += 2

    def calculate(self, input_val=None):
        if input_val is not None: self.inputs.append(input_val)
        modes = {
            1: lambda: self.add(mode1, mode2, mode3),
            2: lambda: self.multiply(mode1, mode2, mode3),
            3: lambda: self.take_input(mode1),
            5: lambda: self.jump_if_true(mode1, mode2, mode3),
            6: lambda: self.jump_if_false(mode1, mode2, mode3),
            7: lambda: self.less_than(mode1, mode2, mode3),
            8: lambda: self.equals(mode1, mode2, mode3),
            9: lambda: self.relative_offset(mode1)
        }
        while True:
            mode1, mode2, mode3, opcode = get_modes(f"{self.data[self.idx]:05}")
            if opcode in modes:
                modes[opcode]()              
            elif opcode == 4:
                return self.create_output(mode1)                
            elif opcode == 99:
                self.done = True
                return self.output


def parse_file():
    with open("input.txt") as _file:
        for line in _file:
            return [int(num) for num in line.split(",")]


def block_count(data):
    computer = Computer(data)
    block_count = 0
    while not computer.done:
        computer.calculate()
        computer.calculate()
        if computer.calculate() == 2:
            block_count += 1
    return block_count


input_data = 0
def move_joystick(paddle, ball):
    global input_data
    if paddle[0] < ball[0]:
        input_data = 1
    elif paddle[0] > ball[0]:
        input_data = -1
    elif paddle[0] == ball[0]:
        input_data = 0


def score(data):
    data[0] = 2
    computer = Computer(data)
    score = 0
    ball = (0, 0)
    paddle = (0, 0)
    while not computer.done:
        move_joystick(paddle, ball)

        x = computer.calculate(0)
        y = computer.calculate()
        tile_id = computer.calculate()

        if x == -1 and y == 0:
            score = tile_id
        else:
            if tile_id == 4:
                ball = (x, y)
            elif tile_id == 3:
                paddle = (x, y)
    return score


input_vals = parse_file() 
print(block_count(input_vals))
print(score(input_vals))