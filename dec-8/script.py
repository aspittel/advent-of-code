from collections import deque

with open('input.txt', 'r') as f:
    data = deque()
    for line in f:
        for val in line.split(' '):
            data.append(int(val))


class Tree:
    def __init__(self, data):
        self.n_children = data.popleft()
        self.n_metadata = data.popleft()
        self.children = [Tree(data) for _ in range(self.n_children)]
        self.metadata = [data.popleft() for _ in range(self.n_metadata)]

    def get_total(self):
        return sum(self.metadata) + sum(child.get_total() for child in self.children)

    def get_child_value(self, child):
        if child < len(self.children):
            return self.children[child].get_root_value()
        return 0

    def get_root_value(self):
        if not self.children: return sum(self.metadata)
        total = 0
        for idx in self.metadata:
            total += self.get_child_value(idx - 1) # Index starts at 1 not 0 :(
        return total


tree = Tree(data)
print(tree.get_total())
print(tree.get_root_value())