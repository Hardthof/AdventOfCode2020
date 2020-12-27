from datetime import datetime

def bt(data):
    #print('depth: ', len(data['hist']), '\n', data)
    if data['stp'] in data['hist']:
        #print('last vlaue is: ', data['accumulator'])
        return False

    nd = data.copy()
    nd['hist'] = data['hist'].copy()
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

print('start', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
with open('AdventOfCode/Day8.txt') as f:
    seq = [[line.split(' ')[0],int(line.split(' ')[1])] for line in [line.rstrip('\n') for line in f]]

#data = {'accumulator':0, 'stp':0, 'cmd':seq[0][0], 'value':seq[0][1], 'flip' : True, 'hist' : []} #day1
data = {'accumulator':0, 'stp':0, 'cmd':seq[0][0], 'value':seq[0][1], 'flip' : False, 'hist' : []} #day2
bt(data)
print(data)
print('end', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])