import cProfile
from collections import Counter

s = ['e', 'se', 'sw', 'w', 'nw', 'ne']
neigh = {'e':(-1,0),'se':(0,-1),'sw':(1,-1),'w':(1,0),'nw':(0,1),'ne':(-1,1)}

class Decoder:
    def __init__(self, file):
        self.data, self.color = self.parseInput(file)

        for i in range(100):
            self.cycle()
            print('day', i, ':', Counter(self.color.values())[0])
    
    def parseInput(self, file):       
        seq = [l for l in open(file, mode='r').read().split('\n')]
        d,c = {},{}
        for line in seq:
            d[line] = self.reduce(line)
            if c.get(d[line], True):
                c[d[line]] = 0 # black
            else:
                c[d[line]] = 1 - c[d[line]] #white / flip
        print(sum(1 for num in Counter(d.values()).values() if num % 2 == 1)) # part1
        return d,c

    def getNeighbors(self, t):
        return [tuple([sum(x) for x in zip(a,t)]) for a in neigh.values()]

    def countExistingBlackNeighbors(self, t, limit=3):
        count = 0
        for n in self.getNeighbors(t):
            v = self.color.get(n, 1)
            if v == 0: count += 1
            if v >= limit: break
        return count

    def cycle(self):
        color = self.color.copy()
        for k in self.color:
            for new in self.getNeighbors(k):
                color[new] = color.get(new, 1)

        self.color = color.copy()
        for k,v in self.color.items():
            count = self.countExistingBlackNeighbors(k)
            if v == 0 and (count == 0 or count > 2): color[k] = 1
            elif v == 1 and count == 2: color[k] = 0
        self.color = color

    def reduce(self, line):
        t = [line.count(item) for item in s]
        t[s.index('e')] -= (t[s.index('se')] + t[s.index('ne')])
        t[s.index('w')] -= (t[s.index('sw')] + t[s.index('nw')])
        w = t[s.index('w')] - (t[s.index('e')] + (t[s.index('ne')] - t[s.index('sw')]))
        nw = t[s.index('nw')] - t[s.index('se')] + (t[s.index('ne')] - t[s.index('sw')])
        return (w, nw)

if __name__ == '__main__':
    # cProfile.run('Decoder("AdventOfCode/Day24Example.txt")')
    Decoder("AdventOfCode/Day24.txt")