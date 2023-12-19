with open('input.txt') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]
    disks = [(int(line[3]), int(line[-1][:-1])) for line in lines]

def find_slot(disks):
    time = 0
    while True:
        d = [(disks[i][1] + time + 1 + i) % disks[i][0] for i in range(len(disks))]
        if all(v == 0 for v in d):
            break  
        time += 1
    return time

# Part 1
print("Part 1: {}".format(find_slot(disks)))

# Part 2
print("Part 2: {}".format(find_slot(disks + [(11, 0)])))
