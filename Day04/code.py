from collections import Counter

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

names = [l[0:l.rfind('-')] for l in lines]
ids = [int(''.join(filter(str.isdigit, l))) for l in lines]
checksums = [l[len(l)-6:-1] for l in lines]

# part 1
real = []
for i in range(len(names)):
    room = names[i].replace('-', '')
    freqs = Counter(''.join(sorted(room))).most_common(5)
    chksm = ''.join([c for c, v in freqs])
    if chksm == checksums[i]:
        real.append(ids[i])
print("Part 1: {}".format(sum(real)))

# part 2
def shift(s, n):
    res = ''
    for c in s:
        if c == '-':
            res += '-' if n % 2 == 0 else ' '
        else:
            res += chr(ord('a') + (ord(c) - ord('a') + n) % 26)
    return res

for i in range(len(names)):
    rname = shift(names[i], ids[i])
    if 'north' in rname:
        print("Part 2: {}".format(ids[i]))
