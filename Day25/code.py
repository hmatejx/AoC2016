from alive_progress import alive_bar

def setup():
    global program
    with open('input.txt') as f:
        program = [line.strip().split(' ') for line in f.readlines()]

def is_digit(s):
    return s.lstrip('-').isdigit()

def run_code(initial={}):
    output = []
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
            elif cmd[0] == 'out':
                output.append(int(cmd[1] if is_digit(cmd[1]) else registers[cmd[1]]))
                output = output[-10:]
                print(registers, output)
            i += 1
            bar()
    return registers

# Part 1
# setup()
# run_code({'a': 192})
# inspecting the output the code derives a binary representation of a number
# the starting value is 2538. Adding 192 to it results in 2730, which has the required
# binary representaiton: 2730 = 0b101010101010
print("Part 1: {}".format(192))

