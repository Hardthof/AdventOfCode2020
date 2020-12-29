from datetime import datetime
import cProfile
from collections import deque

def last(li):
    for i in reversed(range(len(li) - 1)):
        if li[i] == li[-1]:
            return len(li) - i - 1
    return 0

def p2(inp, n):
    input = deque(inp, n)
    d = {input[k]:k for k in range(len(input)-1)}
    for i in range(len(input) - 1, n -1):
        s = input[-1]
        if s in d:
            input.append(i - d[s])
        else:
            input.append(0)
        d[s] = i
    return input[-1]
 
input = [18,11,9,0,5,1]
print(p2(input, 2020))
print(p2(input, 30000000))
#cProfile.run('p2(input, 30000000)')