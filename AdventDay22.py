import cProfile
from collections import deque
from itertools import islice

class Decoder:
    def __init__(self, file):
        self.startDeck = self.parseInput(file)
        winner, deck = self.playTheGame(self.createDeckCopy(self.startDeck, len(self.startDeck['Player 1']), len(self.startDeck['Player 2'])))
        print('Part 1:', self.calcScore(deck[winner]))
        winner, deck = self.playTheGame(self.startDeck, True)
        print('Part 2:', self.calcScore(deck[winner]))

    def parseInput(self, file):
        seq = dict(x.split(": ") for x in [l.replace('\n', ' ') for l in open(file, mode='r').read().split('\n\n')])
        for k,v in seq.items():
            seq[k] = deque([int(x) for x in v.split()])
        return seq

    def createDeckCopy(self, deck, p1, p2):
        return {'Player 1' : deque(islice(deck['Player 1'], 0, p1)), 'Player 2' : deque(islice(deck['Player 2'], 0, p2))}

    def calcScore(self, q):
        score = 0
        [score := score + (len(q)-i)*n for i,n in enumerate(q)]
        return score

    def playTheGame(self, deck, recursive = False):
        setsPlayed = set()
        while len(deck['Player 1']) > 0 and len(deck['Player 2']) > 0:
            state = tuple(deck['Player 1']), tuple(deck['Player 2'])
            if state in setsPlayed:
                return 'Player 1', deck 
            setsPlayed.add(state)
            p1 =  deck['Player 1'].popleft()
            p2 =  deck['Player 2'].popleft()
            
            if len(deck['Player 1']) >= p1 and len(deck['Player 2']) >= p2 and recursive:   
                winner, _ = self.playTheGame(self.createDeckCopy(deck, p1, p2), True)
            elif p1 > p2: 
                winner = 'Player 1'
            else: winner = 'Player 2'
            
            if winner == 'Player 1': 
                deck[winner].extend([p1,p2])
            else: 
                deck[winner].extend([p2,p1])

        return winner, deck       

if __name__ == '__main__':
    # cProfile.run('Decoder("AdventOfCode/Day22.txt")')
    Decoder("AdventOfCode/Day22.txt")