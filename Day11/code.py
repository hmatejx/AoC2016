with open('input.txt') as f:
    lines = [line.strip().split(',') for line in f.readlines()]

def display():
    for i in range(3, -1, -1):
        str = "F{} ".format(i + 1)
        str += 'E  ' if elevator == i else '.  '
        for j in range(len(names)):
            str += names[j][0].upper() + 'G ' if generators[j] == i else '.  '
            str += names[j][0].upper() + 'M ' if microchips[j] == i else '.  '
        print(str)

# construct the floors:
types = ('hydrogen', 'lithium', 'strontium', 'ruthenium', 'thulium', 'plutonium', 'curium')
names = []
generators = []
microchips = []
elevator = 0
for floor, line in enumerate(lines):
    for l in line:
        for t in types:
            if t in l and not t + '-compatible' in l:
                generators.append(floor)
                if t not in names:
                    names.append(t)
            if t + '-compatible' in l:
                microchips.append(floor)
                if t not in names:
                    names.append(t)

display()

# Part 1
# Not really a solution - which would require a branch & bound algorithm - but
# because moving up you always take 2 items and moving down you always take 1 item,
# it must take 2*n-3 moves to move n items up 1 floor, and this can be used to
# calculate the total number of optimal moves... (at least for my input)
items = [sum([1 for g in generators if g == f] + [1 for m in microchips if m == f]) for f in range(4)]
moves = 0
for floor in range(3):
    moves += 2*items[floor] - 3
    items[floor + 1] += items[floor]
    items[floor] = 0
print("Part 1: {}".format(moves))

# Part 2
# Just add 4 more items on first floor
items = [sum([1 for g in generators if g == f] + [1 for m in microchips if m == f]) for f in range(4)]
items[0] += 4
moves = 0
for floor in range(3):
    moves += 2*items[floor] - 3
    items[floor + 1] += items[floor]
    items[floor] = 0
print("Part 2: {}".format(moves))
