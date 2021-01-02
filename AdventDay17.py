import cProfile
from collections import namedtuple
from itertools import product

class Universe:
    def __init__(self, n, file):
        self.n = n
        self.file = file  
        self.Coordinate = namedtuple('Coordinate', ['dim' + str(s) for s in range(n)], defaults = (0,) * n)
        self.universe = self.populateUniverse(file)
        self.neighbors = set(self.Coordinate(*offset) for offset in product([-1, 0, 1], repeat = n) if offset != (0,) * n)

    # create all non existent neighbors of active cubes
    def expandUniverse(self, universe):
        newUniverse = {}
        for coord in universe:
            if universe[coord]:
                for offset in self.neighbors:
                    newUniverse[self.addCoord(coord, offset)] = False
        return newUniverse

    # count neighbors till a max of [lim]
    def countActiveNeighbours(self, coord, lim=4):
        count = 0
        for offset in self.neighbors:
            if self.universe.get(self.addCoord(coord, offset)): 
                    count += 1
                    if count >= lim:
                        break
        return count

    def transition(self, active, activeNeighbors):
        return activeNeighbors == 3 or (activeNeighbors == 2 and active)

    def cycleUniverse(self):
        newUniverse = self.expandUniverse(self.universe)
        for cube in newUniverse:
            newUniverse[cube] = self.transition(self.universe.get(cube, False), self.countActiveNeighbours(cube))
        self.universe = newUniverse

    def populateUniverse(self, file):
        universe = {}
        with open(file) as f:
            for y,l in enumerate(f.readlines()):
                for x in range(len(l.rstrip('\n'))):
                    universe[self.Coordinate(x,y)] = (l[x] == '#')
        return universe

    def addCoord(self, coord, offset):
        return self.Coordinate(*map(sum, zip(coord, offset)))

    def start(self, n):
        for _ in range(n):
            self.cycleUniverse()
        print(sum(map((True).__eq__, self.universe.values())))

cProfile.run('Universe(n = 3, file = "AdventOfCode/Day17.txt").start(6)')
cProfile.run('Universe(n = 4, file = "AdventOfCode/Day17.txt").start(6)')

