from datetime import datetime
import re

mem  = {}

with open('AdventOfCode/Day14.txt') as f:
    seq = [line.rstrip('\n') for line in f]

a = (2 ** 36) -1
o = 0
for cmd in seq:
    if cmd.startswith('ma'):
        a = (2 ** 36) - 1
        o = 0

        for i in range(0, 36): 
            #print(cmd[(-(1+i))])
            if cmd[-(1+i)] == 'X':
                continue
            elif cmd[-(1+i)] == '1': 
                o += 2 ** i
            else: # 0
                a -= 2 ** i
    else:
        m = (re.findall(r"\d+", cmd))
        mem[m[0]] = (int(m[1]) & a) | o

print(sum(mem.values()))
