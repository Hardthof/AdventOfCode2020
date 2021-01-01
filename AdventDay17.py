import cProfile
from collections import namedtuple
from itertools import product

# create all non existent neighbors of active cubes
def expandUniverse(universe):
    newUniverse = {}
    for coord in universe:
        if universe[coord]:
            for offset in neighbors:
                newUniverse[addCoord(coord, offset)] = False
    return newUniverse

# count neighbors till a max of [lim]
def countActiveNeighbours(universe, coord, lim=4):
    count = 0
    for offset in neighbors:
        if universe.get(addCoord(coord, offset)): 
                count += 1
                if count >= lim:
                    break

    # is there a way to find potential hotspots from active universes?
        # for now limit searchspace to cube minX,minY,minZ - maxX,maxY,maxZ
        # r Trees, geohash, kd tree

    #print(coord, 'has', count, 'active neighbors: ')
    return count

def transition(active, activeNeighbors):
    return activeNeighbors == 3 or (activeNeighbors == 2 and active)

def cycleUniverse(knownUniverse):
    newUniverse = expandUniverse(knownUniverse)
    for cube in newUniverse:
        newUniverse[cube] = transition(knownUniverse.get(cube, False), countActiveNeighbours(knownUniverse, cube))
    return newUniverse

def populateUniverse(file):
    universe = {}
    with open(file) as f:
        for y,l in enumerate(f.readlines()):
            for x in range(len(l.rstrip('\n'))):
                universe[Coordinate(x,y,0)] = (l[x] == '#')
    return universe

def addCoord(coord, offset):
    return Coordinate(*map(sum, zip(coord, offset)))


def start(n):
    u = populateUniverse('AdventOfCode/Day17.txt')

    for _ in range(6):
        u = cycleUniverse(u)

    print(sum(map((True).__eq__, u.values())))

Coordinate = namedtuple('Coordinate',  ['x', 'y', 'z'])
neighbors = set(Coordinate(*offset) for offset in product([-1, 0, 1], repeat = 3) if offset != (0,0,0))
n = 3
cProfile.run('start(n)')

Coordinate = namedtuple('Coordinate',  ['x', 'y', 'z', 'w'], defaults=(None))
neighbors = set(Coordinate(*offset) for offset in product([-1, 0, 1], repeat = 4) if offset != (0,0,0,0))
#cProfile.run('start(n)')

