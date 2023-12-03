from statistics import mode
from collections import Counter

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

nc = len(lines[0])
columns = [[] for _ in range(nc)]
for l in lines:
    for i in range(nc):
        columns[i].append(ord(l[i]) - ord('a'))

part1 = part2 = ''
for c in columns:
    part1 += chr(ord('a') + int(mode(c)))
    part2 += chr(ord('a') + Counter(c).most_common()[-1][0])
print("Part 1: {}".format(part1))
print("Part 2: {}".format(part2))
