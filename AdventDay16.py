f = open('AdventOfCode/Day6.txt', mode='r')
seq = [set(l.replace('\n','')) for l in f.read().split('\n\n')]

print(seq)