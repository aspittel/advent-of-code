_file = open("input.txt", "r")
word = _file.readline()

MARKER_LENGTH = 14

for char in range(MARKER_LENGTH, len(word)):
    substr = word[char - MARKER_LENGTH:char]
    if len(set(substr)) == MARKER_LENGTH:
        print(substr)
        print(char)
        break

