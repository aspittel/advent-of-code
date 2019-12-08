def get_layer(data, y=1, x=1):
    start = 0
    while start < len(data):
        yield data[start:start + (x * y)]
        start += x * y

def get_pixel(layers, idx):
    for layer in layers:
        if layer[idx] == "1":
            return "1"
        elif layer[idx] == "0":
            return " "


LAYER_HEIGHT = 6
LAYER_WIDTH = 25

with open('input.txt') as _file:
    data = _file.read()
    layers = [layer for layer in get_layer(data, LAYER_HEIGHT, LAYER_WIDTH)]
    least_zeroes = sorted(layers, key=lambda x: x.count("0"))[0]
    print(f'Part 1: {least_zeroes.count("1") * least_zeroes.count("2")}')

    stacked_pixels = ""
    for coordinate in range(LAYER_HEIGHT * LAYER_WIDTH):
        stacked_pixels += get_pixel(layers, coordinate)

    start = 0
    print("Part 2: ")
    for layer in get_layer(stacked_pixels, LAYER_WIDTH):
        print(''.join(layer))


