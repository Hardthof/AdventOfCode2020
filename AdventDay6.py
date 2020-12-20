def p1(f):
    seq = [set(l.replace('\n','')) for l in f.read().split('\n\n')]
    sum = 0
    [sum := sum + len(s) for s in seq]
    print(sum)


def p2(f): 
    seq = [(l.replace('\n',' ')) for l in f.read().split('\n\n')]
    sum = 0
    for string in seq:
        sum += len(set.intersection(*[set(s) for s in string.split(' ')]))
    print(sum)

f = open('AdventOfCode/Day6.txt', mode='r')
#p1(f)
p2(f)