with open('./input.txt', 'r') as f: 
    data = [int(i) for i in f]

def get_first_duplicate_total(data):
    total = 0
    prev_totals = set([0])
    while True:
        for i in data:
            total += i
            if total in prev_totals:
                return total
            prev_totals.add(total)
    return total

print(get_first_duplicate_total(data))