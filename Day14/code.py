import functools
from hashlib import md5
from alive_progress import alive_bar

# inputs
puzzle = 'jlmsuwbz{}'
stop_at = 64

def find_first_triple(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] and s[i] == s[i + 2]:
            return s[i]
    return ''

@functools.cache
def hash(s, stretch=False):
    if not stretch:
        return  md5(s.encode()).hexdigest()
    for i in range(2017):
        s = md5(s.encode()).hexdigest()
    return s

def find_keys(n, stretch=False):
    keys = []
    with alive_bar() as bar:
        i, r = 0, 0
        while r < stop_at:
            k = find_first_triple(hash(puzzle.format(i), stretch))
            if k:
                for s in [puzzle.format(j) for j in range(i + 1, i + 1001)]:
                    if 5*k in hash(s, stretch):
                        keys.append(i)
                        r += 1
                        break
            i += 1
            bar()
    return keys

# Part 1 & 2
print("Part 1: {}".format(find_keys(stop_at)[-1]))
print("Part 2: {}".format(find_keys(stop_at, stretch=True)[-1]))
