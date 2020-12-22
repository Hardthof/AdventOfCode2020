from datetime import datetime

def expandBagRule(v):
    s = [s.replace(',', '').lstrip() for s in v.split(',')]
    s = {sub.split(' ', 1)[1]:sub.split(' ', 1)[0] for sub in s}
    return s

def visitBag(bags, good, bad, k):

    if 'other bag' in bags[k]:
        bad.append(k)
        return False

    if 'shiny gold bag' in bags[k]:
        good.append(k)
        return True

    if k in good:
        return True

    if k in bad:
        return False

    for bag in bags[k]:
        if visitBag(bags, good, bad, bag):
            good.append(k)
            return True

    bad.append(k)
    return False

print('start', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
with open('AdventOfCode/Day7.txt') as f:
    seq = [line.rstrip('\n').replace('bags', 'bag').replace('.', '') for line in f]

    # get set of possible bags
bags = {s[:s.index("contain")-1] : s[s.index("contain")+8:] for s in seq}
good,bad  = [],[]

for k, v in bags.items():
    if 'shiny gold bag' not in v:
        bags[k] = (expandBagRule(v))

print(bags, sep ='\n')

for k, v in bags.items():
    visitBag(bags, good, bad, k)

# for bag in good:
#     if not any(bag in s for s in seq):
#         print (bag, 'not in bags?')
#     if bag in bad:
#         print('thats odd ', bag)

# for bag in bad:
#     if not any(bag in s for s in seq):
#         print (bag, 'not in bags?')
#     if bag in good:
#         print('thats odd ', bag)

#print(*good, sep= '\n')
print('good: ', len(good), 'bad: ', len(bad), 'all: ', len(bags), 'len seq:', len(seq))
print('end', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])