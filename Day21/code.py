from alive_progress import alive_bar
from itertools import permutations

with open('input.txt') as f:
    commands = [line.strip().split() for line in f.readlines()]
    commands = [[cmd[0] + ' ' + cmd[1], *cmd[2:]] for cmd in commands]

def exec(cmd, s):
    if cmd[0] == 'swap position':
        i1, i2 = int(cmd[1]), int(cmd[4])
        i1, i2 = (i1, i2) if i1 < i2 else (i2, i1)
        return s[0:i1] + s[i2] + s[i1 + 1: i2] + s[i1] + s[i2+1:]
    elif cmd[0] == 'swap letter':
        i1, i2 = s.find(cmd[1]), s.find(cmd[4])
        i1, l1, i2, l2 = (i1, s[i1], i2, s[i2]) if i1 < i2 else (i2, s[i2], i1, s[i1])
        return s[0:i1] + l2 + s[i1 + 1: i2] + l1 + s[i2+1:]
    elif cmd[0] == 'rotate left':
        offset = int(cmd[1]) % len(s)
        return s[offset:] + s[:offset]
    elif cmd[0] == 'rotate right':
        offset = len(s) - (int(cmd[1]) % len(s))
        return s[offset:] + s[:offset]
    elif cmd[0] == 'rotate based':
        i = s.find(cmd[5])
        offset = i + (2 if i >= 4 else 1)
        offset = len(s) - (offset % len(s))
        return s[offset:] + s[:offset]       
    elif cmd[0] == 'reverse positions':
        i1, i2 = int(cmd[1]), int(cmd[3])
        return s[:i1] + s[i1:i2 + 1][::-1] + s[i2 + 1:]
    elif cmd[0] == 'move position':
        x, y = int(cmd[1]), int(cmd[4])
        if y > x:   return s[:x] + s[x+1:y+1] + s[x] + s[y+1:]
        elif x > y: return s[:y] + s[x] + s[y:x] + s[x+1:]
    return s

def scramble(s):
    for cmd in commands:
        s = exec(cmd, s)
    return s

# Part 1
s = 'abcdefgh'
print("Part 1: {}".format(scramble(s)))

# Part 2
with alive_bar() as bar:
    for s in [''.join(p) for p in permutations(s)]:
        if scramble(s) == 'fbgdceah':
            break
        bar()
print("Part 2: {}".format(s))
