class Math:
    def __init__(self, file, sense = False):
        self.tokens = self.parseInput(file)
        self.orderSens = sense

    def parseInput(self, file):
        tokens = []
        for line in open(file):
            tokens.append([char for char in line.rstrip('\n').replace(' ','')])
            for i,e in enumerate(tokens[-1]):
                tokens[-1][i] = int(tokens[-1][i]) if e.isdigit() else tokens[-1][i]
        return tokens

    def findClosingBracket(self, l, index):
        weight = 1
        for i in range(index + 1, len(l)):
            if l[i] == '(':
                weight += 1
            elif l[i] == ')':
                weight -=1
                if(weight == 0):
                    return i
        return -1

    def reduce(self, line):
        while '(' in line:
            start = line.index('(')
            end = self.findClosingBracket(line, start)
            line[start:end + 1] = self.reduce(line[start + 1:end])
        while(len(line) >= 3):
            start,end = self.getNextOperation(line)
            line[start:end] = self.operation(*line[start:end])
        return line[:1]

    def operation(self, v1, op, v2):
        if op == '+': return [v1 + v2]
        else: return [v1*v2]

    def getNextOperation(self, line):
        start = 0
        if self.orderSens:
            if '+' in line:
                start = line.index('+') - 1
            else:
                start = line.index('*') - 1
        end = start + 3
        return start, end

    def sum(self):
        print(sum(self.reduce(l)[0] for l in self.tokens))

if __name__ == '__main__':
    Math("AdventOfCode/Day18.txt").sum()
    Math("AdventOfCode/Day18.txt", sense=True).sum()