def get_layer(x, y, data):
    start = 0
    while start < len(data):
        yield data[start:start + (x * y)]
        start += x * y


LAYER_HEIGHT = 6
LAYER_WIDTH = 25

with open('input.txt') as _file:
    data = _file.read()
    layers = [layer for layer in get_layer(LAYER_HEIGHT, LAYER_WIDTH, data)]
    least_zeroes = sorted(layers, key=lambda x: x.count("0"))[0]
    print(f'Part 1: {least_zeroes.count("1") * least_zeroes.count("2")}')

    stacked_pixels = ""
    for coordinate in range(LAYER_HEIGHT * LAYER_WIDTH):
        done = False
        starting_idx = 0
        while not done:
            if layers[starting_idx][coordinate] == "2":
                starting_idx += 1
            else:
                done = True
                stacked_pixels += " " if layers[starting_idx][coordinate] == "0" else "1"

    start = 0
    print("Part 2: ")
    print(''.join(layer) for layer in get_layer(LAYER_WIDTH, 1, stacked_pixels))
    # while start < len(stacked_pixels):
    #     print(stacked_pixels[start:start + LAYER_WIDTH])
    #     start += 25


