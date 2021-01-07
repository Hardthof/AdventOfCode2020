import cProfile

class Decoder:
    def __init__(self, file):
        self.rules, self.messages, self.alphabet = self.parseInput(file)
        print([self.search(self.rules['0'].split(' '), m) for m in self.messages].count(True))
        self.rules['8'] = '42 | 42 8'
        self.rules['11'] = '42 31 | 42 11 31'
        print([self.search(self.rules['0'].split(' '), m) for m in self.messages].count(True))

    def parseInput(self, file):
        seq = [l for l in open(file, mode='r').read().split('\n\n')]
        rules = dict(x.split(": ") for x in seq[0].split("\n"))
        messages = [l for l in seq[1].rstrip().split('\n')]
        alphabet = {}
        for key,rule in rules.items():
            if '\"' in rule: 
                rules[key] = rule.strip('\"')
                alphabet[key] = rules[key]

        # roughly 40% speed increase
        for item in rules:
            for a in alphabet:
                rules[item] = rules[item].replace(a, alphabet[a])
        return rules,messages,alphabet

    def search(self, rules, target):
        pos = 0
        for i,r in enumerate(rules):
            if not r in self.alphabet.values(): 
                return any(self.search(s.split(' ') + rules[i+1:], target[pos:]) for s in self.rules[r].split(' | '))
            elif target[pos:].startswith(r):
                pos += len(r)
            else: return False
        return pos == len(target) #String ended!

if __name__ == '__main__':
    cProfile.run('Decoder("AdventOfCode/Day19.txt")')