from itertools import permutations
from heapq import heappop, heappush

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    points = {}
    p = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j].isdigit():
                points[int(lines[i][j])] = (i, j)
                p += 1

# A*
def distance(a, b):
    visited = set([a])
    front = []
    heappush(front, (0, 0, a))
    neigh = (0, 1), (0, -1), (1, 0), (-1, 0)
    while front:
        _, d, pos = heappop(front)
        if pos == b:
            return d
        for n in neigh:
            new_pos = pos[0] + n[0], pos[1] + n[1]
            if lines[new_pos[0]][new_pos[1]] != '#' and new_pos not in visited:
                h = abs(b[0] - new_pos[0]) + abs(b[1] - new_pos[1])
                heappush(front, (d + h, d + 1, new_pos))
                visited.add(new_pos)

# create graph of distances between the points
graph = {i: {} for i in range(len(points))}
for i in range(len(points)):
    for j in range(len(points)):
        graph[i][j] = 0 if i == j else distance(points[i], points[j])

# Part 1 & 2 aka let's brute force ;)
res1 = res2 = 1000000000
for p in permutations(range(len(points))):
    if p[0] != 0: continue
    d = sum(graph[p[i]][p[i + 1]] for i in range(len(points) - 1))
    res1 = min(res1, d)
    res2 = min(res2, d + graph[p[-1]][p[0]])
print("Part 1: {}".format(res1))
print("Part 2: {}".format(res2))
