with open('input.txt') as f:
    lines = [line.strip().split() for line in f.readlines()]
    commands = []
    for line in lines:
        if line[0] == 'rect':
            ab = line[1].split('x')
            commands.append(['b', int(ab[0]), int(ab[1])])
        elif line[1] == 'row':
            commands.append(['r', int(line[2][2:]), int(line[4])])
        else:
            commands.append(['c', int(line[2][2:]), int(line[4])])

dimx = 50
dimy = 6
screen = [['.']*dimx for i in range(dimy)]

def display():
    print()
    for line in screen:
        print(''.join(line))

def rect(a, b):
    for i in range(b):
        for j in range(a):
            screen[i][j] = '#'

def rotate_row(a, b):
    screen[a] = screen[a][-b:] + screen[a][:-b]

def rotate_col(a, b):
    col = [screen[i][a] for i in range(dimy)]
    col = col[-b:] + col[:-b]
    for i in range(dimy):
        screen[i][a] = col[i]

for cmd in commands:
    a, b = cmd[1], cmd[2]
    if cmd[0] == 'b':
        rect(a, b)
    elif cmd[0] == 'r':
        rotate_row(a, b)
    else:
        rotate_col(a, b)

print("Part 1: {}".format(sum([sum(1 if p == '#' else 0 for p in line) for line in screen])))

display()
