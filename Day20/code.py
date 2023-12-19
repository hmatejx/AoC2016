with open('input.txt') as f:
    ips = [list(map(int, line.strip().split('-'))) for line in f.readlines()]
    ips.sort(key=lambda x: x[0])
    maxint = 4294967295

# Part 1
candidates = set([min(r) - 1 for r in ips if min(r) > 0])
candidates.update([max(r) + 1 for r in ips])
res1 = maxint
for c in candidates:
    inside = False
    for r in ips:
        if c >= r[0] and c <= r[1]:
            inside = True
            break
    if not inside and c < res1:
        res1 = c
print("Part 1: {}".format(res1))

# Part 2
merged = True
while merged:
    merged = False
    for i in range(len(ips)):
        for j in range(i + 1, len(ips)):
            if ips[i][1] >= ips[j][0] and ips[i][0] <= ips[j][1]:
                ips[i] = [min(ips[i][0], ips[j][0]), max(ips[i][1], ips[j][1])]
                del ips[j]
                merged = True
                break
        else:
            continue
        break
print("Part 2: {}".format(maxint + 1 - sum([r[1] - r[0] + 1 for r in ips])))
