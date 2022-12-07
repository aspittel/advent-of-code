from collections import defaultdict

with open('input.txt', 'r') as _file:
    working_directory = ['']
    files = defaultdict(lambda: 0)
    for command in _file:
        command = command.strip().split()
        if command[0] == "$":
            if command[1] == "cd":
                if command[2] == "..":
                    working_directory.pop()
                elif command[2] == "/":
                    working_directory = ['']
                else:
                    working_directory.append(command[2])
        elif command[0] != "dir":
            wd_str = ''
            for dir in working_directory:
                wd_str += dir
                files[wd_str] += int(command[0])

total_size = 0
unused_space = 70000000 - files['']
space_to_free = 30000000 - unused_space

to_del = files['']
for dir, size in files.items():
    if size <= 100000:
        total_size += size
    if size >= space_to_free and size < to_del:
        to_del = size
        
print(total_size)
print(to_del)
