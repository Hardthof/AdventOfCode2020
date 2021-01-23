class Decoder:
    def __init__(self, pDoor, pKey):
        ldoor = self.findLoop(7, pDoor)
        door = self.transform(7, ldoor)
        lkey = self.findLoop(7, pKey)
        key = self.transform(7, lkey)
        print(self.transform(door, lkey))
        print(self.transform(key, ldoor))
    
    def transform(self, subNum, loopSize):
        v = 1
        for _ in range(loopSize):
            v = (v * subNum) % 20201227
        return v

    def findLoop(self, subNum, target):
        v,count = 1,0
        while(v != target):
            v = (v * subNum) % 20201227
            count += 1
        return count

if __name__ == '__main__':
    #Decoder(17807724, 5764801)
    Decoder(6930903, 19716708)

