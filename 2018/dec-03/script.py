import re

with open('input.txt', 'r') as f:
    data = []
    for line in f:
        nums = [int(n) for n in re.findall(r'\d+', line)]
        data.append({'id': nums[0], 'coordinates': [nums[1], nums[2]], 'dimensions': [nums[3], nums[4]]})


def get_coordinates(coordinates, dimensions):
    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            yield str(x + coordinates[0]) + "," + str(y + coordinates[1])


def get_overlaps(data):
    overlaps = set()
    filled = set()
    for line in data:
        for coord in get_coordinates(line['coordinates'], line['dimensions']):
            if coord in filled:
                overlaps.add(coord)
            else:
                filled.add(coord)
    return overlaps


def no_overlaps(coordinates, dimensions, overlaps):
    for coord in get_coordinates(coordinates, dimensions):
        if coord in overlaps: 
            return False
    return True

 
def find_no_overlaps(data, overlaps):
    for line in data:
        if no_overlaps(line['coordinates'], line['dimensions'], overlaps):
            return line['id']


overlaps = get_overlaps(data)
# Q1
print(len(overlaps))

# Q2
print(find_no_overlaps(data, overlaps))