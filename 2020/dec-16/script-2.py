rules = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19
"""

my_ticket = [11,12,13]

nearby_tickets = """3,9,18
15,1,5
5,14,9"""

nearby_tickets = nearby_tickets.split("\n")
nearby_tickets = [[int(i) for i in n.split(",")] for n in nearby_tickets]

split_rules = rules.split("\n")
rules = [(rule.split(": ")[1].split(" or ")) for rule in split_rules]
keys = [rule.split(": ")[0] for rule in split_rules]

ranges = []
for rule in rules:
  _range = set()
  for r in rule:
    r = r.split('-')
    _range.update(range(int(r[0]), int(r[1]) + 1))
  ranges.append(_range)

def valid_ticket(ticket, ranges):
  new_ranges = set()
  for r in ranges:
    new_ranges.update(r)
  for val in ticket:
    if val not in new_ranges:
      return False
  return True


def get_possibilities(valid_tickets):
  vals = []
  for i in range(0, len(valid_tickets[0])):
    v = set(t[i] for t in valid_tickets)
    vals.append(v)
  return vals

valid_tickets = []
for ticket in nearby_tickets:
  if valid_ticket(ticket, ranges):
    valid_tickets.append(ticket)

vals = get_possibilities(valid_tickets)

possibilities = []

for t in vals:
  p = []
  for idx, r in enumerate(ranges):
    if t.issubset(r):
      p.append(idx)
  possibilities.append(p)

vals = {}

while len(vals) < len(possibilities):
  for idx, p in enumerate(possibilities):
    if len(p) == 1:
      val = p[0]
      vals[keys[p[0]]] = idx
      for x in possibilities:
        if val in x:
         x.remove(val)

keys = []   
for x in vals:
  if x.startswith("departure"):
    keys.append(vals[x])

prod = 1
for i in keys:
  prod *= my_ticket[i]
print(prod)
