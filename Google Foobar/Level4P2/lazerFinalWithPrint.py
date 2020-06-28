import math
import copy


# solution inspired from:    
# https://www.physicsclassroom.com/class/refln/Lesson-2/Other-Multiple-Mirror-Systems
# https://www.physicsclassroom.com/class/refln/Lesson-2/Ray-Diagrams-for-Plane-Mirrors
# returns list of all vectors from you_position to gaurd when only shooting up or down (vertically on y)
# get the guard's "position" in  the mirror by reflecting the room. We contiously reflect until max laser distance reached.    
# [0] = x, and [1] = y
#
# Assume from_person is the origin, we then build a 
# 2d matrix around him. First we build the center column (aka YShots)
# in all rows then we fill the columns in the row.

class Game:
    def __init__(self, your_position=None, guard_position=None):
        self.initial_shot = None
        self.distance = None
        self.guard = None 
        self.you = None 
        self.dimensions = None
        self.gaurd_shots = []
        self.gaurd_shot_slopes = []
        self.friendly_fire = []
        self.friendly_fire_slopes = []

        self.hash_gaurd_shots = dict()
        self.hash_friendly_fire = dict()

    def initPersons(self, your_position, guard_position):
        self.you = Game.Person( self.dimensions, your_position)
        self.guard = Game.Person( self.dimensions, guard_position)
        self.initial_shot = self.calc_direct_shot(self.you, self.guard)

    def calc_direct_shot(self, from_person, to_person):
        shot = []
        shot.append( to_person.position[0] - from_person.position[0] )
        shot.append( to_person.position[1] - from_person.position[1] )
        return shot

    def addShot(self, shot, mDict):
        if str(shot.slope) in mDict:
            mDict[str(shot.slope)].append(shot)
        else:
            mDict[str(shot.slope)] = shot

    class Person(object):
        def __init__(self, dimensions, position):
            self.position = position
            self.flipUpDown = None
            self.flipRL = None

            self.flipUpDown = [] # the difference in Y alternates per flip (eg, +4, +2, +4, +2, ... )
            self.flipUpDown.append( (dimensions[1] - self.position[1]) *2 )
            self.flipUpDown.append( self.position[1]*2 )
            
            self.flipRL = []
            self.flipRL.append( (dimensions[0] - self.position[0]) *2 )
            self.flipRL.append( self.position[0]*2 )


    class Shot(object):
        def __init__(self, coords = None):
            self.coords = coords
            self.slope = [None, None]
            self.distance = doPythagorean(self.coords[0], self.coords[1])
            if coords:
                self.calcSlope() #(lambda : self.__width - self.col + self.__height - self.row)()
        def calcSlope(self):
        
            if self.coords[1] == 0:
                self.slope = [float('inf'),float('inf') ]
            else:
                self.slope[0] = float(self.coords[0]) / abs(self.coords[1])
                self.slope[1] = float(self.coords[1]) / abs(self.coords[1])



    # seed_shot is the center
    def buildRow(self, direction, seed_shot, sequence ):
        previous_shot = seed_shot.coords
        nShots = []
        
        if direction == "right" or direction == "up" :
            q = 0
            flipper = sequence
        else:
            q = 1
            flipper = [x*-1 for x in sequence]

        # we cleverly hold one variable constant and build on other variable
        if direction == "up" or direction == "down":
            p = 1
            p2 = 0
        elif direction == "right" or direction == "left":
            p = 0
            p2 = 1

        print "---- BUILDING ROW ----"
        print "    ",direction
        while True: 
            next_shot = [0] * 2 # next_shot = coords to shot gaurd after reflecting the guard's 'position' 
            next_shot[p] = previous_shot[p] + flipper[q % 2] 
            next_shot[p2] = seed_shot.coords[p2]
            print '    next_shot",' ,next_shot
            dist = doPythagorean(next_shot[0], next_shot[1])            
            if dist <= self.distance:
                nShot = Game.Shot(next_shot)
                if direction == "right" or direction == "up":
                    nShots.append( nShot)
                else:
                    nShots.insert(0, nShot)
                previous_shot = next_shot
            else:
                break
            q = q + 1
        return nShots
        
    def createHashShots(self, shotList):
        mDict = dict()
        for shot in shotList:
            if str(shot.slope) in mDict:
                mDict[str(shot.slope)].append(shot)
            else:
                mDict[str(shot.slope)] = [shot]
        return mDict


    #includes 'bad' shots too. (eg hits self, or hits gaurd multiple times)
    def findAllShotsFromAToB(self, from_person, to_person):
        seed_shot = self.calc_direct_shot(from_person, to_person)
        seed_shot = Game.Shot(seed_shot)

        # first build initial list
        print "seed_shot.coords", seed_shot.coords
        
        first = self.buildRow("up", seed_shot ,to_person.flipUpDown)
        second = self.buildRow("down", seed_shot ,to_person.flipUpDown)
        iList = second + [seed_shot] + first

        # second we fill in the list, creating a 2d matrix
        fullShots = self.buildFullList(to_person, iList)
        return fullShots
    
    def buildFullList(self, person, initList):
        fullShots = []
        for i,item in enumerate(initList):
            print
            print i
            shots_init_RowA = self.buildRow("right", item, person.flipRL)
            shots_init_RowB = self.buildRow("left", item, person.flipRL)
            shots_init_Row = shots_init_RowB + [item] + shots_init_RowA 
            fullShots.insert(0,shots_init_Row)
        return fullShots

    def getCorrectShots(self):
        flatShots = []
        for row in self.gaurd_shots:
            for shot in row:
                flatShots.append(shot)
        flatFriendly = []
        for row in self.friendly_fire:
            for shot in row:
                flatFriendly.append(shot)
        
        self.hash_gaurd_shots = self.createHashShots(flatShots)
        self.hash_friendly_fire = self.createHashShots(flatFriendly)
        
        self.removeNonDoubleHASH(self.hash_gaurd_shots)
        self.removeNonFriendlyFireHASH()
        
        return self.hash_gaurd_shots
        
    def removeNonDoubleHASH(self, hashShots):

        removedItems = []
        for key in self.hash_gaurd_shots:
            if len(self.hash_gaurd_shots[key]) > 1:
                minShot = self.hash_gaurd_shots[key][0]
                i = 0
                while True:
                    i = i + 1
                    if i == len(self.hash_gaurd_shots[key]):
                        break
                    if minShot.distance > self.hash_gaurd_shots[key][i].distance:
                        prevMinShot = minShot
                        minShot = self.hash_gaurd_shots[key][i]
                        removedItems.append(prevMinShot)
                        self.hash_gaurd_shots[key].remove(prevMinShot)
                        i = i - 1
                    else:
                        removedItems.append(self.hash_gaurd_shots[key][i])
                        self.hash_gaurd_shots[key].remove(self.hash_gaurd_shots[key][i])
                        i = i - 1
        print "WAM BAM!"
        for rmv in removedItems:
            print rmv.coords       
        return 

    #assumes double shot was previously ran
    def removeNonFriendlyFireHASH(self):
        
        removedItems =[]
        print "\n MAX LEN AT", len(self.hash_friendly_fire)
        for i0, key in enumerate(self.hash_gaurd_shots.keys()):
            print "```````", i0
            if key == '[inf, inf]': #skip friendly fire origin shot
                continue
            if key in self.hash_friendly_fire:
                i = -1
                while True:
                    i = i + 1
                    if i == len(self.hash_friendly_fire[key]):
                        break
                    print "    ff! key:", key, "max lenth", len(self.hash_friendly_fire[key])
                    print "           :", self.hash_friendly_fire[key][i].coords , "vs ", self.hash_gaurd_shots[key][0].coords
                    if self.hash_friendly_fire[key][i].distance < self.hash_gaurd_shots[key][0].distance:
                        f = self.hash_friendly_fire[key][i]
                        s = self.hash_gaurd_shots[key][0]
                        print "    Friendly fire:", f.coords, f.distance, f.slope
                        print "    Gaurd:", s.coords, s.distance, s.slope
                        removedItems.append(self.hash_gaurd_shots[key][0])
                        self.hash_gaurd_shots.pop( key )
                        break
        print "REMVOED FROM FRIENDLY"
        for rmv in removedItems:
            print rmv.coords
        return 


def mlgHashPrint(mDict):
    print "vvvvvvvvvvvvvvvvvv"
    i = 0
    for k in mDict:
        print i
        for shot in mDict[k]:
            print "     ",k,
            print " ----> ", shot.coords, shot.slope
        i += 1
    print "^^^^^^^^^^^^^^^^^"
        

def mlgPrint(shots):
    maxLength = -1
    for r in shots:
        if len(r) > maxLength:
            maxLength = len(r)
    i = 0
    for sRow in shots:
        print
        diff = (maxLength - len(sRow) )/2
        for d in range(diff):
            print "".rjust(10),
        for s in sRow:
            print str(s.coords)[:10].rjust(11),
        i += 1
    print

        
def doPythagorean(a,b):
    return math.sqrt(a*a + b*b)

def solution(dimensions, your_position, guard_position, distance):

    print "guard_position", guard_position
    print "your_position", your_position
        
    game = Game()

    game.dimensions = dimensions
    game.distance = distance
    game.initPersons(your_position, guard_position)
    
    if doPythagorean(game.initial_shot[0], game.initial_shot[1]) > distance:
        print "nothing!"
        return 0
    if game.you.position == game.guard.position:
        return 1
    game.gaurd_shots        = game.findAllShotsFromAToB(game.you, game.guard)
    game.friendly_fire = game.findAllShotsFromAToB(game.you, game.you)
    
    print "--->game.gaurd_shots"
    mlgPrint(game.gaurd_shots)
    
    print 
    print "--->game.friendly_fire"
    mlgPrint(game.friendly_fire)

    correctShots = game.getCorrectShots()
    for i, k in enumerate(correctShots):
      print i, correctShots[k][0].coords

    print len(correctShots)

    
if __name__ == '__main__':
    #solution([3,2], [1,1], [2,1], 4)
    #solution([300,275], [150,150], [185,100], 500)
    #solution([3,3], [1,1],[2,2], 5)
    
    
        
    #solution([2,3],[1,1],[1,2],2)
    
    #solution([4,3], [1,1], [3,2], 1)
    #solution([4,2],[1,1],[3,1],11)

    #solution([5,5],[4,4],[3,3],12)
    #solution([10,10],[4,4],[3,3],5000)

    solution([2,4],[1,1],[1,3],11)
    #solution([2,5],[1,2],[1,4],11)
    
    