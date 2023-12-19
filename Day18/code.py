from alive_progress import alive_bar

with open('input.txt') as f:
    row = [line.strip() for line in f.readlines()][0]

def tile(lcr):
    return '^' if lcr in ['^^.', '.^^', '^..', '..^'] else '.'

def safe(limit):
    with alive_bar() as bar:
        previous = row
        res = previous.count('.')
        bar()
        for i in range(limit - 1):
            l = '.' + previous + '.'
            next = ''.join([tile(l[j - 1:j + 2]) for j in range(1, len(l) - 1)])
            res += next.count('.')
            previous = next    
            bar()
    return res

# Parts 1 and 2
print("Part 1: {}".format(safe(40)))
print("Part 2: {}".format(safe(400000)))
