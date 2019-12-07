with open('input.txt', 'r') as f:
    text = ''
    for line in f:
        text += line.strip()

def react(text):
    stack = []
    for letter in text:
        last = stack[-1] if stack else None
        if letter != last and (last == letter.upper() or last == letter.lower()):
            stack.pop()
        else:
            stack.append(letter)
    return len(stack)

# A1
print(react(text))

# A2
possibilities = set(text.lower())
print(min(react(text.replace(p, '').replace(p.upper(), '')) for p in possibilities))
