import cProfile

class Node:
    def __init__(self, v=None, prv=None, nx=None):
        self.v = v
        self.next = nx
        self.prv = prv

class Decoder:
    def __init__(self):
        # seed = [int(s) for s in list('389125467')] #example
        seed = [int(s) for s in list('583976241')] # puzzle 

        d = self.play(seed.copy(), 100)
        start = d[1].next
        part1 = ''
        while start != d[1]:
            part1 += str(start.v)
            start = start.next
        print(part1)

        m = max(seed)
        seed += range(m + 1, 1000000 + 1)
        q = self.play(seed, 10000000)
        print(q[1].next.v * q[1].next.next.v)    

    def play(self, q, n):   
        minq, maxq = min(q), max(q)       
        d = {}
        for v in q:
            d[v] = Node(v)
        for i,v in enumerate(q):
            d[v].prv = d[q[i-1]]
            if v == q[-1]: d[v].next = d[q[0]]
            else: d[v].next = d[q[i+1]]   
        
        start = d[q[0]]
        for _ in range(n):
            original = start.v
            destination = original - 1
            cutA = start.next
            cutE = cutA.next.next
            if destination < minq: destination = maxq
            while destination == cutA.v or destination == cutA.next.v or destination == cutE.v: 
                destination -= 1
                if destination < minq: destination = maxq

            # Merge cutout pos
            start.next = cutE.next 
            cutE.next.prv = start

            # Fix cut endings
            cutE.next = d[destination].next
            cutA.prv = d[destination]

            # Fix cut new neighbors
            cutA.prv.next = cutA
            cutE.next.pev = cutE        
            start = start.next
        return d

if __name__ == '__main__':
    cProfile.run('Decoder()')
    # Decoder()