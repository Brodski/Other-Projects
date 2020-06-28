import math
#
# bringing-a-gun-to-a-guard-fight
#
# My solution was inspired from:    
# https://www.physicsclassroom.com/class/refln/Lesson-2/Other-Multiple-Mirror-Systems
# https://www.physicsclassroom.com/class/refln/Lesson-2/Ray-Diagrams-for-Plane-Mirrors
# 
# Get the guard's "position" in  the mirror by reflecting the room. We continuously reflect until max laser distance is reached.    
# The general thought of my code could be displayed in these two examples:
#
# Example 1:
# dimension=[3,5], you=[1,2], gaurd=[1,4]
# The below shows a visual of the room and then the room after reflecting. 
# Room: https://drive.google.com/file/d/1zh75JWxb-KXCyo7ny7WzKVGv4Us5WvRT/view
#
# If we continue to reflect the room we get a final visual:
# Final room: https://drive.google.com/file/d/1sBAvase-WCrj7L2MPUh5rPFbSQsoLmjW/view
#
# Example 2: 
# dimension=[2,4], you=[1,1], gaurd=[1,2]
# A visual of the solution is shown in the link below:
# Final room: https://drive.google.com/file/d/1lGtn6tetQchqk4OB9k7nMHsiRfWmI8Hl/view
#
# And the coordinates of every shot from "you" to "gaurd" below: (includes improper shots)
# coords: https://drive.google.com/file/d/1-IdqVnDG0u7w8yb1sGpkqt0zmUwIhrH_/view
#
#################
##  Process:   ##
#################
#     Assume "you" is the origin, we will build a 2d
#     matrix around "you". First we build the center column
#     then we fill the columns in the row.
#
#
#
#                                      [x,y]                               [x,y]
#                                      [x,y]                               [x,y]                                       [x,y][x,y][x,y]
#                                      [x,y]                               [x,y]                                  [x,y][x,y][x,y][x,y][x,y]
#                                      [x,y]                               [x,y]                                  [x,y][x,y][x,y][x,y][x,y]
#          [x0,y0]   ----->            [x0,y0]    -------> [x,y][x,y][x,y][x0,y0][x,y][x,y][x,y] ---------> [x,y][x,y][x,y][x0,y0][x,y][x,y][x,y]
#                                      [x,y]                               [x,y]                                  [x,y][x,y][x,y][x,y][x,y][x,y]
#                                      [x,y]                               [x,y]                                  [x,y][x,y][x,y][x,y][x,y]
#                                      [x,y]                               [x,y]                                       [x,y][x,y][x,y]
#
#
#

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

            self.flipUpDown = [] # the difference in Y alternates per flip (eg, +7, +2, +7, +2, ... )
            self.flipUpDown.append( (dimensions[1] - self.position[1]) *2 )
            self.flipUpDown.append( self.position[1]*2 )
            
            self.flipRL = []
            self.flipRL.append( (dimensions[0] - self.position[0]) *2 )
            self.flipRL.append( self.position[0]*2 )


    class Shot(object):
        def __init__(self, coords = None):
            self.coords = coords
            self.slope = [None, None]
            dist = doPythagorean(self.coords[0], self.coords[1])
            self.distance = dist
            if coords:
                self.calcSlope() 
                
        def calcSlope(self):
        
            if self.coords[1] == 0:
                self.slope = [float('inf'),float('inf') ]
            else:
                self.slope[0] = float(self.coords[0]) / abs(self.coords[1])
                self.slope[1] = float(self.coords[1]) / abs(self.coords[1])


    # Returns a list of possible shots. seed_shot is the center
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
        while True: 
            next_shot = [0] * 2 # next_shot = coords to shot gaurd after reflecting the guard's 'position' 
            next_shot[p] = previous_shot[p] + flipper[q % 2] 
            next_shot[p2] = seed_shot.coords[p2]
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

    # Returns a 2d matrix.
    # Includes 'bad' shots too. (eg hits self, or hits gaurd multiple times)
    def findAllShotsFromAToB(self, from_person, to_person):
        seed_shot = self.calc_direct_shot(from_person, to_person)
        seed_shot = Game.Shot(seed_shot)

        first = self.buildRow("up", seed_shot ,to_person.flipUpDown)
        second = self.buildRow("down", seed_shot ,to_person.flipUpDown)
        iList = second + [seed_shot] + first

        fullShots = self.buildFullList(to_person, iList)
        return fullShots
    
    def buildFullList(self, person, initList):
        fullShots = []
        for i,item in enumerate(initList):
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
        
        self.removeMultiShots(self.hash_gaurd_shots)
        self.removeFriendlyFire()
        
        return self.hash_gaurd_shots
        
    # Removes shots that hit the gaurd multiple times
    def removeMultiShots(self, hashShots):
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
                        self.hash_gaurd_shots[key].remove(prevMinShot)
                        i = i - 1
                    else:
                        self.hash_gaurd_shots[key].remove(self.hash_gaurd_shots[key][i])
                        i = i - 1
        return 

    def removeFriendlyFire(self):
        for i0, key in enumerate(self.hash_gaurd_shots.keys()):
            if key == '[inf, inf]': #skip friendly fire origin shot
                continue
            if key in self.hash_friendly_fire:
                i = -1
                while True:
                    i = i + 1
                    if i == len(self.hash_friendly_fire[key]):
                        break
                    if self.hash_friendly_fire[key][i].distance < self.hash_gaurd_shots[key][0].distance:
                        self.hash_gaurd_shots.pop( key )
                        break
        return 

def doPythagorean(a,b):
    return math.sqrt(a*a + b*b)

def solution(dimensions, your_position, guard_position, distance):

    game = Game()
    game.dimensions = dimensions
    game.distance = distance
    game.initPersons(your_position, guard_position)
    
    if doPythagorean(game.initial_shot[0], game.initial_shot[1]) > distance:
        return 0
        
    game.gaurd_shots   = game.findAllShotsFromAToB(game.you, game.guard)
    game.friendly_fire = game.findAllShotsFromAToB(game.you, game.you)
    
    correctShots = game.getCorrectShots()
    


    print len(correctShots)
    return len(correctShots)
if __name__ == '__main__':
    #solution([3,2], [1,1], [2,1], 4)
    #solution([300,275], [150,150], [185,100], 500)
    #solution([3,3], [1,1],[2,2], 5)
    
    
        
    # solution([2,3],[1,1],[1,2],2)
    
    # solution([4,3], [1,1], [3,2], 1)
    # solution([4,2],[1,1],[3,1],11)

    # solution([5,5],[4,4],[3,3],12)
    # solution([10,10],[4,4],[3,3],5000)

     #solution([2,4],[1,1],[1,2],11)
    solution([2,5],[1,2],[1,4],11)
    
    