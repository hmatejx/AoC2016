with open('input.txt') as f:
    lines = [list(l.strip()) for l in f.readlines()]

keypad1 = [['1','2','3'],
           ['4','5','6'],
           ['7','8','9']]
keypad2 = [['*','*','1','*','*'],
           ['*','2','3','4','*'],
           ['5','6','7','8','9'],
           ['*','A','B','C','*'],
           ['*','*','D','*','*']]

x, y = 1, 1
part1 = ''
for line in lines:
    for m in line:
        if m == "U" and y > 0:
            y -= 1
        elif m == "D" and y < 2:
            y += 1
        elif m == "L" and x > 0:
            x -= 1
        elif m == "R" and x < 2:
            x += 1
    part1 += keypad1[y][x]
print(part1)

x, y = 0, 2
part2 = ''
for line in lines:
    for m in line:
        if m == "U" and y > 0 and keypad2[y-1][x] != '*':
            y -= 1
        elif m == "D" and y < 4 and keypad2[y+1][x] != '*':
            y += 1
        elif m == "L" and x > 0 and keypad2[y][x-1] != '*':
            x -= 1
        elif m == "R" and x < 4 and keypad2[y][x+1] != '*':
            x += 1
    part2 += keypad2[y][x]
print(part2)