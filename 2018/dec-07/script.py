from collections import defaultdict
import re

def clean_input(data):
    relationships = defaultdict(set)
    for line in data:
        _, parent, child = re.findall(r'[A-Z]', line)
        relationships[child].add(parent)
        if parent not in relationships:
            relationships[parent] = set()
    return relationships


def find_order(relationships):
    done = []
    while len(done) < len(relationships):
        ready = []
        for node in relationships:
            if node not in done and relationships[node].issubset(done):
                ready.append(node)
        done.append(sorted(ready)[0])
    return done


with open ('input.txt', 'r') as f:
    relationships = clean_input(f)

print(''.join(find_order(relationships)))
