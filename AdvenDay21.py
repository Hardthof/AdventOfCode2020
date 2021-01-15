import cProfile
import re

class Decoder:
    def __init__(self, file):
        self.parseInput(file)

    def parseInput(self, file):
        seq = [l for l in open(file, mode='r').read().replace('\n',' ').replace(',','').replace('(contains',':').replace(')','\n').rstrip().split('\n')]
        # print(seq)

        ingridients,goodstuff,allstuff,uniques = {},set(),[],set()
        for item in seq:
            magic = item.split(' : ')[0].split()
            allergens = item.split(' : ')[1].split()
            goodstuff |= set(magic)
            allstuff += magic
            for a in allergens:
                if a in ingridients:
                    ingridients[a] = ingridients[a].intersection(set(magic))
                else:
                    ingridients[a] = set(magic)
        
        for item in ingridients.values(): goodstuff -= item
        count = 0
        for i in allstuff: 
            if i in goodstuff: count+=1
        print(count)

        count = 1
        while count > 0:
            count = 0
            for k,v in ingridients.items():
                if len(v) > 1:
                    ingridients[k] = v - uniques
                    count += len(v) - len(ingridients[k])
                if len(ingridients[k]) == 1: uniques |= ingridients[k]
        
        erg = ''
        for s in sorted([k for k in ingridients.keys()]): erg = erg + list(ingridients[s])[0] + ','
        print(erg.rstrip(','))

if __name__ == '__main__':
    # cProfile.run('Decoder("AdventOfCode/Day21Example.txt")')
    Decoder("AdventOfCode/Day21.txt")