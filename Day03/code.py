with open('input.txt') as f:
    lines = [[int(e) for e in l.strip().split()] for l in f.readlines()]

# part 1
tri = 0
for line in lines:
    sides = line.copy()
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        tri += 1
print("Part 1: {}".format(tri))

# part 2
tri = 0
for i in range(0, len(lines), 3):
    t1 = [lines[i+j][0] for j in range(3)]
    t2 = [lines[i+j][1] for j in range(3)]
    t3 = [lines[i+j][2] for j in range(3)]
    t1.sort()
    t2.sort()
    t3.sort()
    tri += (t1[0] + t1[1] > t1[2]) + (t2[0] + t2[1] > t2[2]) + (t3[0] + t3[1] > t3[2])
print(tri)
