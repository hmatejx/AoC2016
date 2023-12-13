with open('input.txt') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]

def run_code(initial={}):
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    registers.update(initial)
    i = 0
    while i < len(lines):
        cmd = lines[i]
        if   cmd[0] == 'cpy': registers[cmd[2]] = int(cmd[1]) if cmd[1].isdigit() else registers[cmd[1]]
        elif cmd[0] == 'inc': registers[cmd[1]] += 1
        elif cmd[0] == 'dec': registers[cmd[1]] -= 1
        else:
            if (cmd[1].isdigit() and int(cmd[1]) != 0) or registers[cmd[1]] != 0:
                i += int(cmd[2])
                continue
        i += 1
    return registers

# Part 1
res = run_code()
print("Part 1: {}".format(res['a']))

# Part 2
res = run_code({'c': 1})
print("Part 2: {}".format(res['a']))
