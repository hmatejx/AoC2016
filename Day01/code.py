with open('input.txt') as f:
    lines = f.readline().split(', ')

orientation = [0, 1]
position = [0, 0]
history = {'0,0': 1}
Part2 = False
for cmd in lines:
    if cmd[0] == 'R':
        ox = orientation[1]
        oy = -orientation[0]
    elif cmd[0] == 'L':
        ox = -orientation[1]
        oy = orientation[0]
    orientation = [ox, oy]
    step = int(cmd[1:])
    for i in range(step):
        position[0] += orientation[0]
        position[1] += orientation[1]
        posstr =  ','.join(str(e) for e in position)
        if not Part2:
            if history.get(posstr):
                print("Part 2: {}".format(sum(position)))
                Part2 = True
            else:
                history[posstr] = 1

# part 1
print("Part 1: {}".format(sum(position)))
