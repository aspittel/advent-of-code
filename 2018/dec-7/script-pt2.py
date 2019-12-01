from collections import defaultdict
from string import ascii_uppercase
import re

def clean_input(data):
    relationships = defaultdict(set)
    for line in data:
        _, parent, child = re.findall(r'[A-Z]', line)
        relationships[child].add(parent)
        if parent not in relationships:
            relationships[parent] = set()
    return relationships


def letter_to_number(letter):
    return ascii_uppercase.index(letter) + 61


def find_time(relationships):
    total = 0
    done = []
    N_WORKERS = 5
    enqueued = [None] * N_WORKERS
            
    while len(done) < len(relationships):
        print(enqueued)
        for i, value in enumerate(enqueued):
            if value:
                letter, time = value
                if time == 1:
                    done.append(letter)
                    enqueued[i] = None
                else:
                    enqueued[i][1] -= 1
        for node in relationships:
            letters_enqueued = [i[0] for i in enqueued if i]
            if node not in done and node not in letters_enqueued and relationships[node].issubset(done) and None in enqueued:
                enqueued[enqueued.index(None)] = [node, letter_to_number(node)]
        total += 1
    return total - 1


with open ('input.txt', 'r') as f:
    relationships = clean_input(f)

print(find_time(relationships))
