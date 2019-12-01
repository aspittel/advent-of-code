with open('input.txt', 'r') as f:
    boxes = [box.strip() for box in f]

def check_differences(box1, box2):
    difference_idx = -1
    for idx, letter in enumerate(box1):
        if letter != box2[idx]:
            if difference_idx < 0:
                difference_idx = idx
            else:
                return False
    return box1[0:difference_idx] + box1[difference_idx+1:]


def find_one_difference(boxes):
    for idx, box in enumerate(boxes):
        for box2 in boxes[idx+1:]:
            diff = check_differences(box, box2)
            if diff:
                return diff

print(find_one_difference(boxes))