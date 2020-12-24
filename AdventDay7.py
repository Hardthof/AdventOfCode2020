from datetime import datetime

def expandBagRule(v):
    s = [s.replace(',', '').lstrip() for s in v.split(',')]
    s = {sub.split(' ', 1)[1]:sub.split(' ', 1)[0] for sub in s}
    return s

def find_parents(child):
    for parent in bags:
        contents = bags[parent]
        if child in contents:
            find_parents(parent)
            good.add(parent)
    return

def countBags(child, count):

    if 'other bag' in bags[child]:
        #print(child, bags[child])
        return 1

    for bag in bags[child]:
        #print(bag, bags[child][bag])
        count += countBags(bag, 1) * int(bags[child][bag])

    #print(child, 'contains ', count, ' other bags')
    return count

print('start', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
with open('AdventOfCode/Day7.txt') as f:
    seq = [line.rstrip('\n').replace('bags', 'bag').replace('.', '') for line in f]

    # get set of possible bags
bags = {s[:s.index("contain")-1] : s[s.index("contain")+8:] for s in seq}
good  = set()

for k, v in bags.items():
        bags[k] = (expandBagRule(v))

find_parents('shiny gold bag')
print(countBags('shiny gold bag', 0))

print('good: ', len(good), 'all:', len(seq))
print('end', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])