import re
import math
import time

class CoordinatePlane:
    def __init__(self, values):
        self.values = [Point(*value) for value in values]
    
    def x_vals(self):
        vals = [val.x for val in self.values]
        return min(vals), max(vals)

    def y_vals(self):
        vals = [val.y for val in self.values]
        return min(vals), max(vals)

    def draw(self):
        min_x, max_x = self.x_vals()
        min_y, max_y = self.y_vals()
        if max_x - min_x > 100 or max_y - min_y > 100: return
        grid = [['.' for _ in range(min_x, max_x+1)] for _ in range(min_y, max_y+1)]
        for value in self.values:
            grid[value.y - min_y][value.x - min_x] = 'X'
        for row in grid:
            print(''.join(row))
        time.sleep(2)
        print('\n\n\n')

    def increment(self):
        for value in self.values:
            value.move()


class Point:
    def __init__(self, x, y, x_speed, y_speed):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed


with open('sample-input.txt', 'r') as f:        
    values = []
    for line in f:
        x, y, x_speed, y_speed = [int(n) for n in re.findall(r'[+-]?\d+', line)]
        values.append((x, y, x_speed, y_speed,))
    plane = CoordinatePlane(values)
    speed = 0
    while True:
        print(speed)
        plane.draw()
        plane.increment()
        speed += 1