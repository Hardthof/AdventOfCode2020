import itertools
import pandas as pd

def p1(nearTicketsRawString):
    unmapableValues = []
    tickets = getTickets(nearTicketsRawString)
    validTickets = tickets.copy()

    for ticket in tickets:
        for value in ticket:
            if not any([isValidRule(value, r) for r in rules]):
                unmapableValues.append(value)
                validTickets.remove(ticket)
    return unmapableValues, pd.DataFrame(validTickets)

def p2(validTickets):
    ruleMapping = rules.copy()

    # Get lists for all columns which fit the rule
    for rule in rules:
        ruleMapping[rule] = []
        for col in validTickets:
            if all(validTickets[col].apply(lambda x: isValidRule(x, rule))):
                ruleMapping[rule].append(col)

    # condens to single possible combination
    uniques = set()
    while any(len(ruleMapping[ruleMap]) > 1 for ruleMap in ruleMapping):
        for r in ruleMapping:
            if len(ruleMapping[r]) == 1:
                uniques.add(ruleMapping[r][0])
            elif len(ruleMapping[r]) > 1:
                ruleMapping[r] = list(set(ruleMapping[r]) - uniques)

    return ruleMapping

def isValidRule(n, r):
    return (n >= rules[r][0][0] and n <= rules[r][0][1]) or (n >= rules[r][1][0] and n <= rules[r][1][1])

def readRules(s):
    r = {r.split(': ')[0]:r.split(': ')[1] for r in s.rstrip('\n').split('\n')}
    for k,v in r.items():
        r[k] = v.split(' ')
        r[k].remove('or')
        for j in range(len(r[k])):
            r[k][j] = tuple(map(int, r[k][j].split('-')))
    return r

def getTickets(s):
    tickets = [t for t in s.rstrip('\n').split('\n')][1:]
    for i in range(len(tickets)):
        tickets[i] = list(map(int, tickets[i].split(',')))
    return tickets

# read file
f = open('AdventOfCode/Day16.txt', mode='r')
seq = [l for l in f.read().split('\n\n')]

# preprocessing 
rules = readRules(seq[0])
myTicket = getTickets(seq[1])[0]

# p1
e, validTickets = p1(seq[2])
print(sum(e)) #erg p1

# p2
ruleMap = p2(validTickets)
erg = 1 
for r in ruleMap:
    if 'departure' in r:
        erg *= myTicket[ruleMap[r][0]]
print(erg)
