def getValue(s, c):
    v = 0
    v = [v := v + 2**x for x in range(len(s)) if row[len(s) -1 -x] == c]
    return v

#seq = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
with open('AdventOfCode/Day5.txt') as f:
    seq = [line.rstrip('\n') for line in f]

passes = []
for s in seq:
    row = s[:-3]
    col = s[-3:]

    rowSum, colsum = 0,0
    [rowSum := rowSum + 2**x for x in range(len(row)) if row[len(row) -1 -x] == 'B']  
    [colsum := colsum + 2**x for x in range(len(col)) if col[len(col) -1 -x] == 'R']
    #print(rowSum, colsum, rowSum * 8 + colsum)
    passes.append(rowSum * 8 + colsum)

for i in range(min(passes), max(passes)):
    if i not in passes:
        print(i, max(passes))
        break