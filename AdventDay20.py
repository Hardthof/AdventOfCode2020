import cProfile
import re
import numpy as np
import numpy.ma as ma
from itertools import permutations

class Tile:
    def __init__(self, data):
        self.data = np.array([list(s) for s in data.lstrip('\n').split('\n')]) == '#'
        self.permutations = [self.rotateRight, self.rotateRight, self.rotateRight, self.flipHorizontal, 
                          self.rotateRight, self.rotateRight, self.rotateRight, self.flipHorizontal]
        self.permutationIndex = 0

    def getData(self): return self.data[1:-1,1:-1]
    def getTop(self): return self.data[0]
    def getBottom(self): return self.data[-1]
    def getRight(self): return self.data[:,-1]
    def getLeft(self): return self.data[:,0]   
    def rotateRight(self): self.data = np.rot90(self.data)
    def flipHorizontal(self): self.data = np.fliplr(self.data)
    def numberOfPossiblePermutations(self): return len(self.permutations)
    def getPossibleEdges(self): 
        return [self.getTop(), self.getRight(), self.getBottom(), self.getLeft(), np.flip(self.getTop()), 
                np.flip(self.getRight()), np.flip(self.getBottom()), np.flip(self.getLeft())]

    def permutate(self): 
        self.permutations[self.permutationIndex]()
        self.permutationIndex = (self.permutationIndex + 1) % self.numberOfPossiblePermutations()

class Mapper:
    def __init__(self, file):
        self.fragments = self.parseInput(file)
        n = int(np.sqrt(len(self.fragments)))
        self.sea = np.zeros(shape=(n*8, n*8), dtype=bool)
        self.corner, self.edges, self.unique = self.findCornerStones()
        self.erg = np.prod(self.corner, dtype=np.ulonglong)
        self.placeFragments(np.zeros(shape=(n,n)), set(self.fragments))
        self.monster = np.array([list(s) for s in '                  # \n#    ##    ##    ###\n #  #  #  #  #  #   '.split('\n')]) == '#'
        print(self.findTheMonstersAndCountThem())
        print(self.erg)
        
    def parseInput(self, file):
        seq = [l for l in open(file, mode='r').read().split('\n\n')]
        return {int(re.search(r'\d+', s).group()):Tile(s.split(':')[1]) for s in seq}

    def fitsNeighbors(self, matrix, node, pos):
        if pos[0] > 0 and matrix[pos[0] - 1, pos[1]] > 0:
            if not np.array_equal(node.getLeft(), self.fragments[matrix[pos[0] - 1, pos[1]]].getRight()):
                return False
        if pos[0] < matrix.shape[0] - 1 and matrix[pos[0] + 1, pos[1]] > 0:
            if not np.array_equal(node.getRight(), self.fragments[matrix[pos[0] + 1, pos[1]]].getLeft()):
                return False
        if pos[1] > 0 and matrix[pos[0], pos[1] - 1] > 0:
            if not np.array_equal(node.getTop(), self.fragments[matrix[pos[0], pos[1] - 1]].getBottom()):
                return False
        if pos[1] < matrix.shape[1] - 1 and matrix[pos[0], pos[1] + 1] > 0:
            if not np.array_equal(node.getBottom(), self.fragments[matrix[pos[0], pos[1] + 1]].getTop()):
                return False
        return True 

    def findCornerStones(self):
        possibleEdges, corner, edge = [],[],[]
        for x in self.fragments.values(): possibleEdges = possibleEdges + x.getPossibleEdges() 
        (unique, counts) = np.unique(possibleEdges, axis=0, return_counts=True)
        unique = unique[counts == 1]
        for k,x in self.fragments.items():
            candidates = np.vstack((x.getPossibleEdges(), unique))
            (candidates, _) = np.unique(candidates, axis=0, return_counts=True)
            if len(candidates) - len(unique) == 4: corner.append(k)
            elif len(candidates) - len(unique) == 6: edge.append(k)
        return corner,edge, unique

    def findTheMonstersAndCountThem(self):
        for _ in range(3):
            self.window_stack()
            self.sea = np.rot90(self.sea)
        self.window_stack()
        self.sea = np.fliplr(self.sea)
        self.window_stack()
        for _ in range(3):
            self.sea = np.rot90(self.sea)
            self.window_stack()

    def window_stack(self):
        print('New Permutation to scan')
        width = self.monster.shape[0]
        height = self.monster.shape[1]
        stack = []                                
        for i in range(0, self.sea.shape[0]-width+1):
            for j in range(0, self.sea.shape[1]-height+1):
                window = self.sea[i:i+width,j:j+height] #.reshape((-1,1))
                stack.append(window)
        for item in stack:
            if np.array_equal(self.monster, np.logical_and(self.monster, item)):
                print(item)

    def checkIfEdgeIsOuter(self, edge):
        return (edge == self.unique).all(axis=1).any() 

    def posCheck(self, node, matrix, x,y):
        X,Y = matrix.shape[0] - 1, matrix.shape[1] - 1
        # if y == 0 and self.checkIfEdgeIsOuter(self.fragments[node].getTop()): return False                  
        # if y == Y and self.checkIfEdgeIsOuter(self.fragments[node].getBottom()): return False 
        # if x == 0 and self.checkIfEdgeIsOuter(self.fragments[node].getLeft()): return False 
        # if x == X and self.checkIfEdgeIsOuter(self.fragments[node].getRight()): return False 
        if  (x == 0 or x == X) and (y == 0 or y == Y): return node in self.corner
        if x == 0 or x == X or y == 0 or y == Y: return node in self.edges
        return not (node in self.edges or node in self.corner)
        
    def placeFragments(self, matrix, unused):
        # borderFirstOrder = [(0.0), (matrix.shape[0]-1, 0), (0,matrix.shape[1]-1), (matrix.shape[0]-1,matrix.shape[1]-1)]
        # borderFirstOrder += [(x,y) for y in [0,matrix.shape[1]-1] for x in range(1, matrix.shape[0]-1)] 
        # borderFirstOrder += [(x,y) for x in [0,matrix.shape[0]-1] for y in range(1, matrix.shape[1]-1)]
        # borderFirstOrder += [(x,y) for y in range(1, matrix.shape[1] - 1) for x in range(1, matrix.shape[0] - 1)]
        # for x,y in borderFirstOrder:
        for x in range(matrix.shape[0]):
            for y in range(matrix.shape[1]):
                if matrix[x,y] == 0.0:
                    for e in unused:
                        if self.posCheck(e, matrix, x,y):
                            for _ in range(self.fragments[e].numberOfPossiblePermutations()):
                                if self.fitsNeighbors(matrix, self.fragments[e], (x,y)):
                                    matrix[x,y] = e
                                    if self.placeFragments(matrix.copy(), unused.difference([e])):
                                        return True  
                                self.fragments[e].permutate()
                if matrix[x,y] == 0.0: return False # could not match anything!                      
        if np.all(matrix):                                      
            self.erg = int(matrix[0,0] * matrix[x,0] * matrix[0,y] * matrix[x,y])
            print(matrix)
            for x in range(matrix.shape[0]):
                for y in range(matrix.shape[1]):
                    self.sea[x*8:x*8+8,y*8:y*8+8] = self.fragments[matrix[x,y]].getData()
            print(matrix)
            print(matrix[0,0], '\n', self.fragments[matrix[0,0]].getData())
            print(matrix[1,0], '\n', self.fragments[matrix[1,0]].getData())
            return True
        return False # Filled in all unused

if __name__ == '__main__':
    # cProfile.run('Mapper("AdventOfCode/Day20.txt")')
    Mapper("AdventOfCode/Day20Example.txt")