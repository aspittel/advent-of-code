# def traverse(val, tree):
#     if 'no other' in val:
#         return False
#     if 'shiny gold' in val:
#         return True
#     return any([traverse(tree[i], tree) for i in val])


# with open('input.txt') as _file:
#     tree = {}
#     tally = 0
#     for line in _file:
#         rule = line.replace("bags", "").replace("bag", "").replace(".", "").rstrip().split("  contain ")
#         tree[rule[0]] = [l.lstrip() for l in''.join(letter for letter in rule[1] if letter.isalpha() or letter == " ").rstrip().split("  ")]
#     for value in tree.values():
#         if traverse(value, tree):
#             tally += 1
#     print("Part 1", tally)

def traverse(key, tree):
    print(key)
    if key == 'no other': 
        return 0
    _sum = sum([i for i in tree[key].values()])
    return _sum + sum([tree[key][i] * traverse(i, tree) for i in tree[key]]) 

with open('input.txt') as _file:
    tree = {}
    tally = 0
    for line in _file:
        rule = line.replace("bags", "").replace("bag", "").replace(".", "").rstrip().split("  contain ")
        rules = rule[1].split(", ")
        rule_dict = {}
        for color_rule in rules:
            color = ''.join(letter for letter in color_rule if letter.isalpha() or letter == " ").strip()
            number = int(''.join(num for num in color_rule if num.isdigit())) if 'no' not in color_rule else 0 
            rule_dict[color] = number
        tree[rule[0]] = rule_dict
    print("Part 2", traverse('shiny gold', tree))


       
