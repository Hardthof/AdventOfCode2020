import pandas as pd
import numpy as np
from datetime import datetime

dictOrientation = { 0 : 'N', 90 : 'E', 180: 'S', 270: 'W'}

seq = ['F10', 'N3', 'F7', 'R90', 'F11']
with open('AdventOfCode/Day12.txt') as f:
    seq = [line.rstrip('\n') for line in f]

def splitCommand(s):
     head = s.rstrip('0123456789')
     tail = int(s[len(head):])

     return head, tail

def applyRotation(pos, direction, degree):
    if direction == 'L':
        degree = degree * -1
    pos[2] = (pos[2] + degree) % 360

    return pos

def applyAbsMove(pos, direction, value):
    if direction == 'N':
        pos[1] = pos[1] + value
    if direction == 'S':
        pos[1] = pos[1] - value
    if direction == 'E':
        pos[0] = pos[0] + value
    if direction == 'W':
        pos[0] = pos[0] - value
    
    return pos

def applyRelMove(pos, orientation, value):
    return applyAbsMove(pos, dictOrientation[pos[2]], value)

def moveWaypoint(pos, waypoint, c, v):
    return pos, applyAbsMove(waypoint, c, v)

def rotateWaypoint(pos, waypoint, c, v):

    if c == 'L':
        v = 360 - v

    if v == 90:
        temp = waypoint[0] 
        waypoint[0] = waypoint[1]
        waypoint[1] = temp * (-1)
    if v == 180:
        waypoint[0] = waypoint[0] * (-1)
        waypoint[1] = waypoint[1] * (-1)
    if v == 270:
        temp = waypoint[0] 
        waypoint[0] = waypoint[1] * (-1)
        waypoint[1] = temp

    return pos, waypoint

def movetoWaypoint(pos, waypoint, c, v):
    pos[0] = pos[0] + waypoint[0] * v
    pos[1] = pos[1] + waypoint[1] * v
    return pos, waypoint

def part1():

    applyCommand = {
    **dict.fromkeys(['N','E','S','W'], applyAbsMove), 
    **dict.fromkeys(['L', 'R'], applyRotation),
    'F' : applyRelMove
    }

    orientation = 90
    pos =[0, 0, orientation]

    for s in seq:
        c, v = splitCommand(s) 
        pos = applyCommand[c](pos, c, v)

    print(abs(pos[0]) + abs(pos[1]))

def part2():

    applyCommand = {
    **dict.fromkeys(['N','E','S','W'], moveWaypoint), 
    **dict.fromkeys(['L', 'R'], rotateWaypoint),
    'F' : movetoWaypoint
    }

    waypoint = [10, 1]
    pos =[0, 0]

    for s in seq:
        c, v = splitCommand(s) 
        pos, waypoint = applyCommand[c](pos, waypoint, c, v)
        #print(c,v, pos, waypoint)

    print(abs(pos[0]) + abs(pos[1]))

print('start', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
part1()
part2()
print('end', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])