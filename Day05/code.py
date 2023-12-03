from alive_progress import alive_bar
from hashlib import md5

test = 'abc'
input = 'ojvtpuvg'

def crack(s):
    pwd1 = ''
    pwd2 = '________'
    with alive_bar() as bar:
        i = 0
        while len([c for c in pwd2 if c == '_']):
            s = input + str(i)
            res = md5(s.encode()).hexdigest()
            if res[0:5] == '00000':
                if len(pwd1) < 8:
                    pwd1 += res[5]
                idx = int(res[5], 16)
                if idx < 8 and pwd2[idx] == '_':
                    pwd2 = pwd2[:idx] + res[6] + pwd2[idx+1:]
                    print("s: {}, pwd1: {}, pwd2: {}".format(s, pwd1, pwd2))
            i += 1
            bar()
    return pwd1, pwd2

pwd1, pwd2 = crack(input)
print("Part 1: {}".format(pwd1))
print("Part 2: {}".format(pwd2))
