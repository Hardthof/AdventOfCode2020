from datetime import datetime
import re    

mem,mem2  = {},{}

with open('AdventOfCode/Day14.txt') as f:
    seq = [line.rstrip('\n') for line in f]

a = (2 ** 36) -1
o = 0
md = ''
for cmd in seq:
    if cmd.startswith('ma'):

        a = (2 ** 36) -1
        o = 0
        md = cmd[-36:]

        for i in range(0, 36): 
            if cmd[-(1+i)] == 'X':
                continue
            elif cmd[-(1+i)] == '1':
                o += 2 ** i
            else: # 0
                a  -= 2 ** i
    else:
        m = (re.findall(r"\d+", cmd))
        mem[m[0]] = (int(m[1]) & a) | o

        adr = [int(m[0]) | int(md.replace('X', '0'),2)]
        for i in range(0, 36): 
            if md[i] == 'X':
                tmp = adr.copy()
                for j in range(len(tmp)):
                    adr[j] |= 2 ** (35 - i)
                    tmp[j] &= ((2 ** 36) -1) - 2 ** (35 -i)
                adr += tmp
        for a in adr:
            mem2[int(a)] = int(m[1])

print(sum(mem.values()))
print(sum(mem2.values()))
