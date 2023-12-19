input = '01000100010010111'

def tiger(s):
    return s + '0' + s[::-1].replace('1', '2').replace('0', '1').replace('2', '0')

def checksum(str):
    while True:
        res = ''
        for i in range(0, len(str), 2):
            ss = str[i:i+2]
            res += '1' if ss == '00' or ss == '11' else '0'
        if len(res) % 2 == 1:
            return res
        str = res

# Hmm, brute force, there must be a better way

# Part 1
disk = 272
s = input
while len(s) <disk:
    s = tiger(s)
s = s[:disk]
print("Part 1: {}".format(checksum(s)))

disk = 35651584
s = input
while len(s) <disk:
    s = tiger(s)
s = s[:disk]
print("Part 2: {}".format(checksum(s)))
