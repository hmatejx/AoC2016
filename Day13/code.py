# inputs
magic = 1350
stop_at = (31, 39)
visited = {}

def is_open(x, y):
    res = x*x + 3*x + 2*x*y + y + y*y + magic
    res_bin = bin(res)[2:]
    return res_bin.count('1') % 2 == 0

def flood_fill(start = (1, 1)):
    front = [start + (0, )]
    visited[start] = 0
    while front:
        f = min(front, key=lambda f: f[2])
        front.remove(f)
        i, j, step = f
        for n in (1, 0), (-1, 0), (0, 1), (0, -1):
            new_pos = i + n[0], j + n[1]
            if new_pos == stop_at:
                return step + 1
            if all(ij >= 0 for ij in new_pos) and new_pos not in visited and is_open(*new_pos) :
                visited[new_pos] = step + 1
                front.append((new_pos) + (step + 1, ))
    return -1

# Part 1:
print("Part 1: {}".format(flood_fill()))

# Part 2:
print("Part 2: {}".format(len([v for v in visited.values() if v <= 50])))
