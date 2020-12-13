import pandas as pd
import numpy as np
import itertools
import math
from datetime import datetime
import multiprocessing



def split(word): 
    return [char for char in word]  

def getNeighbours(a, t):
    dim = a.shape
    xCoords = [x for x in range(t[0] - 1, t[0] + 1 + 1) if x >= 0 and x < dim[0]]
    yCoords = [y for y in range(t[1] - 1, t[1] + 1 + 1) if y >= 0 and y < dim[1]]
    
    window = {(x,y) for x in xCoords for y in yCoords}
    window.discard(t)
    return window

def seatMe(s, a, d):
    newSeatings = a.copy()
    for seat in s:
        adjacentSeats = [array[coord] for coord in d[seat]]
        #print(seat, adjacentSeats)
        if a[seat] == 'L':
            newSeatings[seat] = '#' if '#' not in adjacentSeats else 'L'
        else:
            newSeatings[seat] = '#' if adjacentSeats.count('#') < 5 else 'L'
    return newSeatings
    
def getQueenMoves(a, s, t):
    watch = set()
    dim = a.shape
    xrange = list(range(0,dim[0]))
    yrange = list(range(0,dim[1]))
    moves = [(x,y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
    moves.remove((0,0))
    
    for move in moves:
        pos = t
        while(1):
            pos = tuple(map(sum, zip(pos, move)))
            if(pos[0] not in xrange or pos[1] not in yrange):
                break
            if(pos in s):
                watch.add(pos)
                break
    
    return watch


print('start', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    
#data = pd.read_fwf('AdventOfCode/Day11Example.txt', header = None)
data = pd.read_fwf('AdventOfCode/Day11.txt', header = None)
data.columns = ["d"]

cols = range(0, len(data['d'].loc[0]))
df = pd.DataFrame(columns=cols)

for index, row in data.iterrows():
    df.loc[index] = split(row['d'])

array = df.to_numpy()  
print('read', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

setSeats = {tuple(coord) for coord in np.argwhere(array == 'L').tolist()}
setFloor = {tuple(coord) for coord in np.argwhere(array == '.').tolist()}

#print(getQueenMoves(array, setSeats, (0,0)))    

print('Preprocessing done.', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
d = {}
for k in setSeats:
    v = getQueenMoves(array, setSeats, k)
    v= v - setFloor
    d[k] = v

print('get queen moves', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

new = np.ones_like(array) 

while(1):
    new = seatMe(setSeats, array, d)
    #print(new, '\n')
    if(np.array_equal(new, array)):
        break
    array = new
    
#print(new, '\n')
print('pplz:', np.count_nonzero(array == '#'))

print('end', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])