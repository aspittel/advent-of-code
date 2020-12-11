from collections import Counter

with open('input.txt') as file:
    voltages = [0] + sorted([int(n) for n in file]) 
    voltages += [voltages[-1] + 3]
    _abs = []
    for v, v1 in zip(voltages, voltages[1:]):
        _abs.append(abs(v - v1))
    print(Counter(_abs))
_sum = 0
        

with open('input.txt') as file:
    voltages = [0] + sorted([int(n) for n in file]) 
    voltages += [voltages[-1] + 3]
    set_voltages = set(voltages)
    finish = voltages[-1]
    diffs = [1, 2, 3]
    curr_len = 0
    done = 0
    val_counts = {0: 1}
    new_val_counts = {}
    while curr_len <= len(voltages):
        for count in val_counts:
            for diff in diffs:
                _sum = diff + count
                if _sum in set_voltages:
                    if _sum in new_val_counts:
                        new_val_counts[_sum] += val_counts[count]
                    else:
                        new_val_counts[_sum] = val_counts[count]
        if finish in new_val_counts: done += new_val_counts[finish] 
        val_counts = new_val_counts
        new_val_counts = {}
        curr_len += 1
    print(done)            
        

        

