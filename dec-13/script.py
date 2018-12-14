from copy import deepcopy

with open('input.txt', 'r') as f:
    grid = []
    for line in f:
        grid.append(list(line.replace('\n', '')))


increments = {
    '<': [-1, 0],
    '>': [1, 0],
    'v': [0, 1],
    '^': [0, -1]
}

intersections = {
    "left": {
        "v": ">",
        "^": "<",
        ">": "^",
        "<": "v"
    },
    "right": {
        "v": "<",
        "^": ">",
        ">": "v",
        "<": "^"
    }
}

curves = {
    "/": {
        "v": "<",
        "^": ">",
        ">": "^",
        "<": "v"
    },
    "\\": {
        "v": ">",
        "^": "<",
        ">": "v",
        "<": "^"
    }
}

directions = ["left", "straight", "right", "straight"]

def change_directions(direction):
    if direction == "left":
        return "straight"
    if direction == "right":
        return "left"
    if direction == "straight":
        return "right"

class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.turn = "left"

    def __repr__(self):
        return 'x={} y={} direction={} turn={}'.format(self.x, self.y, self.direction, self.turn)

    def move_straight(self):
        x_move, y_move = increments[self.direction]
        self.x += x_move
        self.y += y_move

    def intersection(self):
        if self.turn != "straight":
            self.direction = intersections[self.turn][self.direction]
        self.move_straight()
        self.turn = change_directions(self.turn)

    def curve(self, curve):
        self.direction = curves[curve][self.direction]
        self.move_straight()

    def coordinates(self):
        return f'{self.x},{self.y}'

    def move(self):
        move = grid[self.y][self.x]
        if move == "|" or move == "-":
            self.move_straight()
        elif move == "+":
            self.intersection()
        elif move == "/" or move == "\\":
            self.curve(move)
        else:
            print("whatthefuck")


carts = []
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if col in "<>v^":
            carts.append(Cart(x, y, col))


def clean_original(grid):
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == ">" or col == "<":
                grid[x][y] = "-"
            elif col == "^" or col == "v":
                grid[x][y] = "|"
    return grid


def format_grid(grid):
    for cart in carts:
        grid[cart.y][cart.x] = cart.direction
    for row in grid:
        print(''.join(row))


def last_survivor(carts):
    while True:
        seen = set(cart.coordinates() for cart in carts)
        for cart in carts:
            if cart.coordinates() in seen:
                seen.remove(cart.coordinates())
                cart.move()
                if cart.coordinates() in seen:
                    seen.remove(cart.coordinates())
                else:
                    seen.add(cart.coordinates())
        carts = [cart for cart in carts if cart.coordinates() in seen]
        if len(carts) == 1: return carts[0]
    

def get_collision(carts):
    seen = set()
    for cart in carts:
        cart.move()
        if (cart.x, cart.y,) in seen:
            return cart
        seen.add((cart.x, cart.y,))
    return get_collision(carts)

grid = clean_original(grid)
print(get_collision(deepcopy(carts)))
print(last_survivor(carts))
