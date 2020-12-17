rules = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19"""

my_ticket = "11,12,13"

nearby_tickets = """3,9,18
15,1,5
5,14,9"""

nearby_tickets = nearby_tickets.split("\n")
nearby_tickets = [[int(i) for i in n.split(",")] for n in nearby_tickets]

rules = rules.split("\n")
rules = [(rule.split(": ")[1].split(" or ")) for rule in rules]
ranges = set()
for rule in rules:
  for r in rule:
    r = r.split('-')
    ranges.update(range(int(r[0]), int(r[1]) + 1))

invalid_tickets = []

for ticket in nearby_tickets:
  for val in ticket:
    if val not in ranges:
      invalid_tickets.append(val)

print("Part 1", sum(invalid_tickets))