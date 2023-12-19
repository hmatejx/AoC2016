from alive_progress import alive_bar
from hashlib import md5

input = 'gdjjyniy'

moves = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
front = [(1, 1, '')]
solutions = []
with alive_bar() as bar:
    while front:
        i, j, path = front.pop(-1)
        # check if we have reached the vault
        if i == 4 and j == 4:
            solutions.append([len(path), path])
            continue
        h = md5((input + path).encode()).hexdigest()[:4]
        next_steps = ['UDLR'[k] for k in range(4) if h[k] > 'a']
        for step in next_steps:
            # skip steps that would lead into a wall
            if step == 'U' and i == 1 or step == 'D' and i == 4 or step == 'L' and j == 1 or step == 'R' and j == 4:
                continue
            front.append((i + moves[step][1], j + moves[step][0], path + step))
        bar()

print("Part 1: {}".format(min(solutions, key=lambda x: x[0])[1]))
print("Part 2: {}".format(max(solutions, key=lambda x: x[0])[0]))
