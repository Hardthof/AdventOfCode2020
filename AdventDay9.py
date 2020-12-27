from datetime import datetime
import collections

def isValid(x, v):
    pre = list(x)
    for i in range(len(pre) - 1):
        for j in range(i + 1, len(pre)):
            if pre[i] + pre[j] == v:
                return True
    return False

def scan(seq, target):
    dq = collections.deque(seq[:0], None)

    for i in range(len(seq)):
        dq.append(seq[i])
        while sum(list(dq)) > target and len(dq) > 2: dq.popleft()        
        v = sum(list(dq))
        if v == target: break

    return list(dq)

print('start', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
with open('AdventOfCode/Day9.txt') as f:
    seq = [int(line.rstrip('\n')) for line in f]

n = 25
x = collections.deque(seq[:n], n)

for i in range(n,len(seq)):
    if isValid(x, seq[i]):
        x.append(seq[i])
    else:
        print(seq[i])
        l = scan(seq, seq[i])
        print(min(l)+ max(l))
        break

print('end', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

