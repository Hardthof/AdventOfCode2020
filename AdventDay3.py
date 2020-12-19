from datetime import datetime
import numpy as np

def hitCounter(l, iStep, jStep):
    hits,j = 0,0

    for i in range(0, len(seq), iStep):
        if seq[i][j % len(seq[0])] == '#':
            hits += 1
        j += jStep
    return hits
    
with open('AdventOfCode/Day3.txt') as f:
    seq = [line.rstrip('\n') for line in f]

    moves = [(1,1),(1,3),(1,5),(1,7),(2,1)]
    total = 1
    [total := total * x for x in [hitCounter(seq, a[0], a[1]) for a in moves]]  
    print(total)