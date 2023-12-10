import re

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def abba(s):
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
            return True
    return False

def ababab(s, h):
    for i in range(len(s) - 2):
        aba = s[i:(i+3)]
        if aba[0] != aba[2] or aba[0] == aba[1]:
            continue
        bab = aba[1] + aba[0] + aba[1]
        if bab in h:
            return True
    return False

# Part 1 & 2
tls = []
ssl = []
for ip in lines:
    # split the strings to supernet and hypernet parts
    supernet = []
    hypernet = []
    seq = ''
    for c in ip:
        if c == '[':
            supernet.append(seq)
            seq = ''
        elif c == ']':
            hypernet.append(seq)
            seq = ''
        else:
            seq += c
    supernet.append(seq)
    # Part 1
    q1 = len([seq for seq in supernet if abba(seq)]) > 0
    q2 = len([seq for seq in hypernet if abba(seq)]) > 0
    tls.append(1 if q1 and not q2 else 0)
    # Part 2
    q3 = 0
    for s in supernet:
        for h in hypernet:
            if ababab(s, h):
                q3 = 1
                break
    ssl.append(q3)
print("Part 1: {}".format(sum(tls)))
print("Part 2: {}".format(sum(ssl)))
