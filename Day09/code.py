with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def decompress_v1(line):
    res = ''
    i = 0
    while i < len(line):
        # check if a compression marker starts
        if line[i] == '(':
            j = line.find(')', i + 1)
            cm = line[i + 1:j].split('x')
            # decompress
            s = line[j + 1:j + 1 + int(cm[0])]
            res += s*int(cm[1])
            i = j + len(s) + 1
        else:
            # add character to output
            res += line[i]
            i += 1
    return res

def decompress_v2(s):
    # plain string, no compression markers
    if ')' not in s: return len(s)
    # split the string into parts
    i = 0
    parts = []
    while i < len(s):
        # check if a compression marker starts
        if s[i] == '(':
                j = s.find(')', i + 1)
                cm = s[i + 1:j].split('x')
                length, repeat = int(cm[0]), int(cm[1])
                parts.append([repeat, s[j + 1: j + 1 + length]])
                i = j + 1 + length
        # process the plain string until next compression marker or eos
        else:
            j = s.find('(', i + 1)
            j = j if j != -1 else len(s)
            parts.append([1, s[i:j]])
            i = j
    # recursivelly process parts and calculate the total length
    res = sum(part[0]*decompress_v2(part[1]) for part in parts)
    return(res)

# part 1 & 2
for line in lines:
    print(len(decompress_v1(line)))
    print(decompress_v2(line))
