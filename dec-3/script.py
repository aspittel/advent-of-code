with open('input.txt', 'r') as f:
    data = []
    for line in f:
        line = line.strip().split('@ ')
        _id = line[0]
        line = line[1].split(': ')
        coordinates = [int(i) for i in line[0].split(',')]
        dimensions = [int(i) for i in line[1].split('x')]
        data.append({'id': _id, 'coordinates': coordinates, 'dimensions': dimensions})

overlaps = set()
filled = set()

def get_overlaps(coordinates, dimensions):
    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            coord = str(x + coordinates[0]) +"," + str(y + coordinates[1])
            if coord in filled:
                overlaps.add(coord)
            else:
                filled.add(coord)

def no_overlaps(coordinates, dimensions):
    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            coord = str(x + coordinates[0]) +"," + str(y + coordinates[1])
            if coord in overlaps: return False
    return True

# Q1
for line in data:
    get_overlaps(line['coordinates'], line['dimensions'])
print(len(overlaps))

# Q2
for line in data:
    if no_overlaps(line['coordinates'], line['dimensions']):
        print(line['id'])
