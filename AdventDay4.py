from datetime import datetime
from itertools import compress
import re
import os

def isPresent(d, reqDict):
    if len(d) == len(reqDict):
        return True

    if (len(d) == len(reqDict) - 1) and 'cid' not in d:
        return True

    return False

def isValid(d):

    if int(d['byr']) < 1920 or int(d['byr']) > 2002:
        return False

    if int(d['iyr']) < 2010 or int(d['iyr']) > 2020:
        return False

    if int(d['eyr']) < 2020 or int(d['eyr']) > 2030:
        return False

    if not 'cm' in d['hgt'] and not 'in' in d['hgt']:
        return False

    hgt = int(re.findall(r"\d+", d['hgt'])[0])
    if 'cm' in d['hgt']:
        if(hgt < 150 or hgt > 193):
            return False
    else:
        if(hgt < 59 or hgt > 76):
            return False

    if not bool(re.search(r'#[a-f\d]{6}', d['hcl'])):
        return False

    if d['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if not bool(re.match(r"\d{9}(?!\d)", d['pid'])):
        return False

    return True
    
f = open('AdventOfCode/Day4.txt', mode='r') 
seq = [l.replace('\n',' ') for l in f.read().split('\n\n')]
reqDict = dict.fromkeys(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'], 0)
passList = [dict((k.strip(), v.strip()) for k,v in (item.split(':') for item in s.split(' '))) for s in seq]
present = [isPresent(d, reqDict) for d in passList]
valid = [isValid(d) for d in list(compress(passList, present))]

print('Fields present', present.count(True))
print('present and valid', valid.count(True))