from itertools import product

memories = {}

def mask_mem(maskx, mask1, mem):
    to_bin = list("{0:b}".format(mem[0]).zfill(36))
    for m in mask1:
        to_bin[m] = '1'
    for combo in product([0, 1], repeat=len(maskx)):
        for i, m in enumerate(maskx):
            to_bin[m] = str(combo[i])
        memories[int(''.join(to_bin), 2)] = mem[1]


def get_mask_idx(mask):
    mask_1s = []
    mask_xs = []
    for idx, val in enumerate(mask):
        if val == '1':
            mask_1s.append(idx)
        if val == 'X':
            mask_xs.append(idx)
    return mask_1s, mask_xs


with open('input.txt') as file:
    mask = ''
    mems = []
    for line in file:
        line = line.rstrip()
        if line.startswith('mask'):
            if mask:
                mask1, maskx = get_mask_idx(mask)
                for mem in mems:
                    mask_mem(maskx, mask1, mem)
            mask = line.split("mask = ")[1]
            mems = []
        else:
            mem = line.split(" = ")
            mems.append((int(mem[0][4:-1]), int(mem[1])))
    mask1, maskx = get_mask_idx(mask)
    for mem in mems:
        mask_mem(maskx, mask1, mem)
print(sum(memories.values()))