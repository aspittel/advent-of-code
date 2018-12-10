import re
from collections import deque

def get_sequence(max, players):
    sequence = deque()
    scores = [0] * players
    for marble in range(0, max + 1):
        if marble % 23 == 0 and marble > 0:
            current_player = marble % players
            sequence.rotate(-7)
            scores[current_player] += marble + sequence.pop()
        else:
            sequence.rotate(2)
            sequence.append(marble)
    return scores


with open('input.txt', 'r') as f:
    for line in f:
        players, last_marble = [int(n) for n in re.findall(r'\d+', line)]
        scores = get_sequence(last_marble, players)
        print(max(scores))
        large_scores = get_sequence(last_marble * 100, players)        
        print(max(large_scores))
