from datetime import datetime
import re

def isLineValid(l):

    numbers = list(map(int, (re.findall(r"\d+", l)))) 
    index = re.search(":", l).start()
    s =  l[index -1]
    sub = l[index +2 :]
    count = sub.count(s)

    return count <= max(numbers) and count >= min(numbers)

def isLineValidP2(l):

    numbers = list(map(int, (re.findall(r"\d+", l)))) 
    index = re.search(":", l).start()
    s =  l[index -1]
    sub = l[index +2 :]
    sig = [sub[i - 1] for i in numbers]

    return s in sig and sig[0] != sig[1]
    

with open('AdventOfCode/Day2.txt') as f:
    seq = [line.rstrip('\n') for line in f]

    erg = [isLineValid(l) for l in seq]
    print(erg.count(True))

    erg = [isLineValidP2(l) for l in seq]
    print(erg.count(True))