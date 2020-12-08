ROW_COUNT = 127
COL_COUNT = 7

def binary_search(li, up, down, top):
    _min = 0
    _max = top
    for seat in li:
        half = (_max + _min) // 2
        if seat == up:
            _max = half
        elif seat == down:
            _min = half + 1
    return _min


with open('input.txt') as seats:
    seat_ids = []
    max_seat = 0
    for line in seats:
        col = binary_search(line[:7], 'F', 'B', ROW_COUNT)
        row = binary_search(line[7:], 'L', 'R', COL_COUNT)
        seat_id = col * 8 + row
        max_seat = max(max_seat, seat_id)
        seat_ids.append(seat_id)
    print("Part 1", max_seat)

    seat_ids = sorted(seat_ids)
    prev = seat_ids[0]
    for seat_id in seat_ids[1:]:
        if prev != seat_id - 1:
            print("Part 2", prev)
            break
        prev += 1
    