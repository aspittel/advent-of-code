memories = {}

def mask_mem(mask, mem):
    to_bin = list("{0:b}".format(mem[1]).zfill(36))
    for m, v in mask:
        to_bin[m] = v
    memories[mem[0]] = int(''.join(to_bin), 2)

def get_mask_idx(mask):
    mask_vals = []
    for idx, val in enumerate(mask):
        if val != 'X':
            mask_vals.append((idx, val))
    return mask_vals

with open('input.txt') as file:
    mask = ''
    mems = []
    for line in file:
        line = line.rstrip()
        if line.startswith('mask'):
            if mask:
                mask = get_mask_idx(mask)
                for mem in mems:
                    mask_mem(mask, mem)
            mask = line.split("mask = ")[1]
            mems = []
        else:
            mem = line.split(" = ")
            mems.append((int(mem[0][4:-1]), int(mem[1])))
    mask = get_mask_idx(mask)
    for mem in mems:
        mask_mem(mask, mem)
print(sum(memories.values()))