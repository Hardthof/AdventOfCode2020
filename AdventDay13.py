import numpy as np
import math
from datetime import datetime

inputString = '37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,587,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,x,x,x,23,x,x,x,x,x,29,x,733,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17'
#inputString = '7,13,x,x,59,x,31,19' # 1068781
#inputString = '17,x,13,19' # 3417
#inputString = '67,7,59,61' #first occurs at timestamp 754018.
#inputString = '67,x,7,59,61' #first occurs at timestamp 779210.
#inputString = '67,7,x,59,61' #first occurs at timestamp 1261476.
#inputString = '1789,37,47,1889' #first occurs at timestamp 1202161486. 


def ggt(m,n):
    if (n==0):
        return m
    else:
        return ggt(n, m%n)

def kgv(m,n):
    o = ggt(m,n)
    p = (m * n) / o
    return int(p)

def kgvL(l):
    n = len(l) 
    if n > 2:
        return l # split halve recursive
    if n == 1:
        return l
    
    return kgv(l[0], l[1])

def trueForAll(buses, d, timestamp):
    for bus in buses:
        if not (timestamp + d[bus]) % bus == 0:
            return bus
    return 0

def part1():
    #timeNow = 939
    #buses = [7,13,59,31,19]

    timeNow = 1005526
    buses = [int(s) for s in inputString.split(',') if s.isdigit()]
    #print (buses)

    closest = {}
    for id in buses:
        next = math.ceil(timeNow / id)
        closest[id] = next * id

    minId = min(closest, key=closest.get)
    print(minId, closest[minId])
    print((closest[minId] - timeNow) * minId)

def part2():
    buses = [int(s) for s in inputString.split(',') if s.isdigit()]
    complete = [s for s in inputString.split(',')]
    
    timeOffest = {}
    for item in buses:
        #print(complete.index(str(item)))
        timeOffest[item] = complete.index(str(item))

    busessorted = sorted(buses.copy())
    
    #print(busessorted)
    #print(buses)
    #print(timeOffest)

    multi = max(busessorted)
    calcOffset = timeOffest[multi]
    erg = 0
    l = busessorted[:-1]

    j = 1

    '''
    while(1):
        erg = multi * j - calcOffset
        
        check = trueForAll(l, timeOffest, erg)
        if check == 0:
            break

        if check == 41:
            print(erg, datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
        
        j = j + 1           

    print(erg)
    '''

    time, step = 0, 1
    for bus in buses:
        offset = timeOffest[bus]
        while (time + offset) % bus:
            time += step
        step *= bus

    print(time)

print('start', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
#part1()
part2()
print('end', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

