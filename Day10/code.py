with open('input.txt') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]

def give_bot(bot, val):
    if bots[bot]['low'] == -1:
        bots[bot]['low'] = val
    elif bots[bot]['low'] < val:
        bots[bot]['high'] = val
    else:
        bots[bot]['high'] = bots[bot]['low']
        bots[bot]['low'] = val

# get the number of bots
bots = {}
for line in lines:
    if 'bot' in line:
        i = line.index('bot')
        bot = int(line[i + 1])
        bots[bot] = {'low': -1, 'high': -1}

# process all 'value' lines
for line in [l for l in lines if l[0] == 'value']:
    give_bot(int(line[5]), int(line[1]))

# process all 'bot' lines until end condition
target = {'low': 17, 'high': 61}
output = {}
while True:
    for line in [l for l in lines if lines if l[0] == 'bot']:
        # check if bot can proceed
        bot = bots[int(line[1])]
        if bot == target:
            print("Part 1: {}".format(line[1]))
        if bot['low'] > -1 and bot['high'] > -1:
            if line[5] == 'bot':
                give_bot(int(line[6]), bot[line[3]])
                bot[line[3]] = -1
            elif line[5] == 'output':
                output[int(line[6])] = bot[line[3]]
                bot[line[3]] = -1
            if line[10] == 'bot':
                give_bot(int(line[11]), bot[line[8]])
                bot[line[8]] = -1
            elif line[10] == 'output':
                output[int(line[11])] = bot[line[8]]
                bot[line[8]] = -1
    # check if complete
    if max(b['low'] for _, b in bots.items()) == -1:
        break
print("Part 2: {}".format(output[0]*output[1]*output[2]))
