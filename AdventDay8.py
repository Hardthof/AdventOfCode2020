from datetime import datetime
import copy

def bt(data):
    #print('depth: ', len(data['hist']), '\n', data)
    if data['stp'] in data['hist']:
        return False

    nd = copy.deepcopy(data) 
    #nd['hist'] = data['hist'].copy()
    nd['hist'].append(nd['stp'])

    if data['cmd'] in ['acc','nop']:
        nd['stp'] = data['stp'] + 1
        if data['cmd'] == 'acc':
            nd['accumulator'] += data['value']
    else:
        nd['stp'] = data['stp'] + data['value']

    if nd['stp'] >= len(seq):
        print('last vlaue is: ', nd['accumulator'])
        return True
  
    nd['cmd'] = seq[nd['stp']][0]
    nd['value'] = seq[nd['stp']][1]

    if bt(nd):
        return True
    elif not data['flip'] and nd['cmd'] in ['jmp','nop']:
        nd['flip'] = True
        nd['cmd'] = 'jmp' if nd['cmd'] == 'nop' else 'nop'
        return bt(nd)

    return False

def execute(data):
    cmd = seq[data['stp']][0]
    v   = seq[data['stp']][1]

    data['hist'].append(data['stp'])
    newStack = -1

    if cmd == 'acc'  or cmd == 'nop':
        newStack = data['stp'] + 1
    else:
        newStack = data['stp'] + v

    if newStack in data['hist']:
        for i in reversed(data['hist']):
            if seq[i][0] != 'nop':
                data['flip'] = i
                return data['accumulator']

    data['stp'] = newStack

    if cmd == 'acc':
        data['accumulator'] += v

    return execute(data)

print('start', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
with open('AdventOfCode/Day8.txt') as f:
    seq = [[line.split(' ')[0],int(line.split(' ')[1])] for line in [line.rstrip('\n') for line in f]]

data = {'accumulator':0, 'stp':0, 'cmd':seq[0][0], 'value':seq[0][1], 'flip' : False, 'hist' : []}
#print(seq)

#execute(data)
print(bt(data))

print('end', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])