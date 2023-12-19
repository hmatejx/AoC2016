from alive_progress import alive_bar
from functools import reduce

def setup():
    global program
    with open('input.txt') as f:
        program = [line.strip().split(' ') for line in f.readlines()]

def is_digit(s):
    return s.lstrip('-').isdigit()

def run_code(initial={}):
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    registers.update(initial)
    i = 0
    with alive_bar() as bar:
        while i < len(program):
            cmd = program[i]
            if   cmd[0] == 'cpy' and not is_digit(cmd[2]): registers[cmd[2]] = int(cmd[1]) if is_digit(cmd[1]) else registers[cmd[1]]
            elif cmd[0] == 'inc' and not is_digit(cmd[1]): registers[cmd[1]] += 1
            elif cmd[0] == 'dec' and not is_digit(cmd[1]): registers[cmd[1]] -= 1
            elif cmd[0] == 'jnz':
                if (int(cmd[1]) if is_digit(cmd[1]) else registers[cmd[1]]) != 0: 
                    i += int(cmd[2]) if is_digit(cmd[2]) else registers[cmd[2]]
                    continue
            elif cmd[0] == 'tgl':
                j = i + registers[cmd[1]]
                if j >= 0 and j < len(program):
                    target = program[j]
                    if len(target) == 2:
                        program[j] = ['dec' if target[0] == 'inc' else 'inc', target[1]]
                    else:
                        program[j] = ['cpy' if target[0] == 'jnz' else 'jnz', ] + target[1:]
            i += 1
            bar()
    return registers

def factorial(x):
    return reduce((lambda x, y: x*y), list(range(2, x + 1)))

# Part 1
setup()
res = run_code({'a': 7})
print("Part 1: {}".format(res['a']))

# Part 2
# the program calculates the sum of the  product of two integers given in lines 19 and 20
# and the factorial of the value given in register a at start
print("Part 2: {}".format(int(program[19][1])*int(program[20][1]) + factorial(12)))
