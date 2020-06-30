
import math 

# @1 --> 1
# @2 --> x1^2/2 + x2/2
# @3 --> x1^3/6 + (x1 x2)/2 + x3/3
# @4 --> x1^4/24 + (x1^2 x2)/4 + x2^2/8 + (x1 x3)/3 + x4/4
# @5 --> x1^5/120 + (x1^3 x2)/12 + (x1 x2^2)/8 + (x1^2 x3)/6 + (x2 x3)/6 + (x1 x4)/4 + x5/5
# @6 --> x1^6/720 + (x1^4 x2)/48 + (x1^2 x2^2)/16 + x2^3/48 + (x1^3 x3)/18 + ( x1 x2 x3)/6 + x3^2/18 + (x1^2 x4)/8 + (x2 x4)/8 + (x1 x5)/5 + x6/6
# @7 --> x1^7/5040 + (x1^5 x2)/240 + (x1^3 x2^2)/48 + (x1 x2^3)/48 + (x1^4 x3)/72 + 1/12 x1^2 x2 x3 + (x2^2 x3)/24 + (x1 x3^2)/18 + (x1^3 x4)/24 + (x1 x2 x4)/8 + (x3 x4)/12 + (x1^2 x5)/10 + (x2 x5)/10 + (x1 x6)/6 + x7/7
# @8 --> x1^8/40320 + (x1^6 x2)/1440 + (x1^4 x2^2)/192 + (x1^2 x2^3)/96 + x2^4/384 + (x1^5 x3)/360 + 1/36 x1^3 x2 x3 + 1/24 x1 x2^2 x3 + (x1^2 x3^2)/36 + (x2 x3^2)/36 + (x1^4 x4)/96 + 1/16 x1^2 x2 x4 + (x2^2 x4)/32 + (x1 x3 x4)/12 + x4^2/32 + ( x1^3 x5)/30 + (x1 x2 x5)/10 + (x3 x5)/15 + (x1^2 x6)/12 + (x2 x6)/12 + (x1 x7)/7 + x8/8
# @9 --> x1^9/362880 + (x1^7 x2)/10080 + (x1^5 x2^2)/960 + (x1^3 x2^3)/288 + ( x1 x2^4)/384 + (x1^6 x3)/2160 + 1/144 x1^4 x2 x3 + 1/48 x1^2 x2^2 x3 + (x2^3 x3)/144 + (x1^3 x3^2)/108 + 1/36 x1 x2 x3^2 + x3^3/162 + (x1^5 x4)/480 + 1/48 x1^3 x2 x4 + 1/32 x1 x2^2 x4 + 1/24 x1^2 x3 x4 + (x2 x3 x4)/24 + (x1 x4^2)/32 + (x1^4 x5)/120 + 1/20 x1^2 x2 x5 + (x2^2 x5)/40 + (x1 x3 x5)/15 + (x4 x5)/20 + (x1^3 x6)/36 + (x1 x2 x6)/12 + (x3 x6)/18 + (x1^2 x7)/14 + (x2 x7)/14 + (x1 x8)/8 + x9/9
# @10 --> x1^10/3628800 + x10/10 + (x1^8 x2)/80640 + (x1^6 x2^2)/5760 + (x1^4 x2^3)/1152 + (x1^2 x2^4)/768 + x2^5/3840 + (x1^7 x3)/15120 + 1/720 x1^5 x2 x3 + 1/144 x1^3 x2^2 x3 + 1/144 x1 x2^3 x3 + (x1^4 x3^2)/432 + 1/72 x1^2 x2 x3^2 + (x2^2 x3^2)/144 + (x1 x3^3)/162 + (x1^6 x4)/2880 + 1/192 x1^4 x2 x4 + 1/64 x1^2 x2^2 x4 + (x2^3 x4)/192 + 1/72 x1^3 x3 x4 + 1/24 x1 x2 x3 x4 + (x3^2 x4)/72 + (x1^2 x4^2)/64 + (x2 x4^2)/64 + (x1^5 x5)/600 + 1/60 x1^3 x2 x5 + 1/40 x1 x2^2 x5 + 1/30 x1^2 x3 x5 + (x2 x3 x5)/30 + (x1 x4 x5)/20 + x5^2/50 + (x1^4 x6)/144 + 1/24 x1^2 x2 x6 + (x2^2 x6)/48 + (x1 x3 x6)/18 + (x4 x6)/24 + (x1^3 x7)/42 + (x1 x2 x7)/14 + (x3 x7)/21 + (x1^2 x8)/16 + (x2 x8)/16 + (x1 x9)/9
# @11 --> x1^11/39916800 + (x1 x10)/10 + x11/11 + (x1^9 x2)/725760 + (x1^7 x2^2)/40320 + (x1^5 x2^3)/5760 + (x1^3 x2^4)/2304 + (x1 x2^5)/3840 + (x1^8 x3)/120960 + (x1^6 x2 x3)/4320 + 1/576 x1^4 x2^2 x3 + 1/288 x1^2 x2^3 x3 + (x2^4 x3)/1152 + (x1^5 x3^2)/2160 + 1/216 x1^3 x2 x3^2 + 1/144 x1 x2^2 x3^2 + (x1^2 x3^3)/324 + (x2 x3^3)/324 + (x1^7 x4)/20160 + 1/960 x1^5 x2 x4 + 1/192 x1^3 x2^2 x4 + 1/192 x1 x2^3 x4 + 1/288 x1^4 x3 x4 + 1/48 x1^2 x2 x3 x4 + 1/96 x2^2 x3 x4 + 1/72 x1 x3^2 x4 + (x1^3 x4^2)/192 + 1/64 x1 x2 x4^2 + (x3 x4^2)/96 + (x1^6 x5)/3600 + 1/240 x1^4 x2 x5 + 1/80 x1^2 x2^2 x5 + (x2^3 x5)/240 + 1/90 x1^3 x3 x5 + 1/30 x1 x2 x3 x5 + (x3^2 x5)/90 + 1/40 x1^2 x4 x5 + (x2 x4 x5)/40 + (x1 x5^2)/50 + (x1^5 x6)/720 + 1/72 x1^3 x2 x6 + 1/48 x1 x2^2 x6 + 1/36 x1^2 x3 x6 + (x2 x3 x6)/36 + (x1 x4 x6)/24 + (x5 x6)/30 + (x1^4 x7)/168 + 1/28 x1^2 x2 x7 + (x2^2 x7)/56 + (x1 x3 x7)/21 + (x4 x7)/28 + (x1^3 x8)/48 + (x1 x2 x8)/16 + (x3 x8)/24 + (x1^2 x9)/18 + (x2 x9)/18
# @12 --> x1^12/479001600 + (x1^2 x10)/20 + (x1 x11)/11 + x12/12 + (x1^10 x2)/7257600 + (x10 x2)/20 + (x1^8 x2^2)/322560 + (x1^6 x2^3)/34560 + (x1^4 x2^4)/9216 + (x1^2 x2^5)/7680 + x2^6/46080 + (x1^9 x3)/1088640 + (x1^7 x2 x3)/30240 + (x1^5 x2^2 x3)/2880 + 1/864 x1^3 x2^3 x3 + (x1 x2^4 x3)/1152 + (x1^6 x3^2)/12960 + 1/864 x1^4 x2 x3^2 + 1/288 x1^2 x2^2 x3^2 + (x2^3 x3^2)/864 + (x1^3 x3^3)/972 + 1/324 x1 x2 x3^3 + x3^4/1944 + (x1^8 x4)/161280 + (x1^6 x2 x4)/5760 + 1/768 x1^4 x2^2 x4 + 1/384 x1^2 x2^3 x4 + (x2^4 x4)/1536 + (x1^5 x3 x4)/1440 + 1/144 x1^3 x2 x3 x4 + 1/96 x1 x2^2 x3 x4 + 1/144 x1^2 x3^2 x4 + 1/144 x2 x3^2 x4 + (x1^4 x4^2)/768 + 1/128 x1^2 x2 x4^2 + (x2^2 x4^2)/256 + 1/96 x1 x3 x4^2 + x4^3/384 + (x1^7 x5)/25200 + (x1^5 x2 x5)/1200 + 1/240 x1^3 x2^2 x5 + 1/240 x1 x2^3 x5 + 1/360 x1^4 x3 x5 + 1/60 x1^2 x2 x3 x5 + 1/120 x2^2 x3 x5 + 1/90 x1 x3^2 x5 + 1/120 x1^3 x4 x5 + 1/40 x1 x2 x4 x5 + (x3 x4 x5)/60 + (x1^2 x5^2)/100 + (x2 x5^2)/100 + (x1^6 x6)/4320 + 1/288 x1^4 x2 x6 + 1/96 x1^2 x2^2 x6 + (x2^3 x6)/288 + 1/108 x1^3 x3 x6 + 1/36 x1 x2 x3 x6 + (x3^2 x6)/108 + 1/48 x1^2 x4 x6 + (x2 x4 x6)/48 + (x1 x5 x6)/30 + x6^2/72 + (x1^5 x7)/840 + 1/84 x1^3 x2 x7 + 1/56 x1 x2^2 x7 + 1/42 x1^2 x3 x7 + (x2 x3 x7)/42 + (x1 x4 x7)/28 + (x5 x7)/35 + (x1^4 x8)/192 + 1/32 x1^2 x2 x8 + (x2^2 x8)/64 + (x1 x3 x8)/24 + (x4 x8)/32 + (x1^3 x9)/54 + (x1 x2 x9)/18 + (x3 x9)/27


class StarGrid:
    def __init__(self):
        self.cycleIndecies = []
        self.myCycleStruct = CycleStructure(1)
        self.sym2 = "x1^3/6 + (x1*x2)/2 + x3/3"
    
    def gcd(self, a, b):
        remainder = None
        while( a % b > 0):
            remainder = a % b
            a = b
            b = remainder
        return b

    def lcm(self, a, b):
        return a*b/self.gcd(a,b)

    # https://math.stackexchange.com/questions/2056708/number-of-equivalence-classes-of-w-times-h-matrices-under-switching-rows-and
    # Returns the cycle that represents permutations across the two cycles, ie the cycles between the row and column
    # note: q = subscript of cycle = length of cycle 
    # We return: a_lcm(q1,q2)^(gcd(q1,q2)*power1*power2)
    def computePair(self, cycleStruct1, cycleStruct2):
        coefficient = cycleStruct1.coefficient * cycleStruct2.coefficient
        newCycleStruct = CycleStructure(coefficient)
        for cycle1 in cycleStruct1:
            for cycle2  in cycleStruct1:
                subscript = self.lcm(cycle1.subscript, cycle2.subscript)
                power = self.gcd(cycle1.subscript, cycle2.subscript) * cycle1.power * cycle2.power
                newCycle = CycleStructure(subscript, power)
                newCycleStruct.cycles.append(newCycle)
        return newCycleStruct


    
    # multiplying a cycle index [polynomial] by another cycle index (cycle index = group of permuations on set)
    def calcCartesianProduct(self, cycleIndex1, cycleIndex2):
        product = [] # I represent "a + b + c" as [a,b,c] instead
        for cycleStruct1 in cycleIndex1:
            for cycleStruct2 in cycleIndex2:
                newcycleStuct = self.computePair(cycleStruct1, cycleStruct2)
                product.append(newcycleStuct)
        return product

# I'm using the vocab from http://www.cs.columbia.edu/~cs4205/files/CM9.pdf (Section 9.1, page 13)
# this is equivalent to a term in a cycle index. So if a cycle Index = "(x_1 x_2)/2 + x_3/3" then (x_1*x_2/2) is a Cycle Structure
class CycleStructure(object): 

    def __init__(self, coefficient=None, cycles = []):
        # eg, if cycle = (1/6) * [(t_2)^5 + (t_3)]  --> cVars = [cycleVar1, cycleVar1], coefficient = 1/6
        self.coefficient = coefficient 
        self.cycles = cycles 

    class Cycle(object):
        def __init__(self, subscript, power):   
            #eg (t_2)^5 --> subscript = 2, power = 5
            self.subscript = subscript # cycle length
            self.power = power # is the number of cycles with length x in the permutation. Is number of occurences in the permutaton

#gram enumeration: http://www.cs.columbia.edu/~cs4205/files/CM9.pdf


# @2 --> x1^2/2 + x2/2


class Lexxer:
    def __init__(self):
        self.ass = None

class Token:
    def __init__(self, kind=None, data=None):
        self.kind = kind
        self.data = data
    def __repr__(self):
        return "[Kind: {0}, Data {1}]".format(self.kind, self.data)

    def processToken(self):
        if self.kind.upper() == "CYCLE":
            pass
        if self.kind.upper() == "COEFFICIENT":
            pass
        
def processRawToken(data):
    coeff = ""
    power = ""
    for i,e in enumerate(data):
        if e.upper == "X":
            continue
        elif e == "^":
            coeff = data[i+1:]

        
    #CycleStructure.Cycle()

def runLexxer(cycString, i=0): #Pretend it's a lexxer
    i = 0
    raw_cycles = []
    while i < len(cycString) :
        if cycString[i].upper() == "X":
            subscript = ""
            power = ""
            xvar= ""
            coeff = ""
            while (cycString[i] not in [")", "*", "/","^" ]):
                if cycString[i].isdigit():
                    subscript = subscript + cycString[i]
                i = i + 1
            while (cycString[i] not in [")", "*", "/" ]):
                if cycString[i].isdigit():
                    power = power + cycString[i]
                i = i + 1
                #if cycString[i] == "^":
                  #  i = i + 1
                 #   continue
                # if cycString[i] == " ":
                #     i = i + 1
                #     continue
            print "subscript", subscript
            print "power", power
        if cycString[i] == "/":
            #i = i + 1
            coeff = cycString[i+1:]
            break
            # while (i < len(cycString) ):
            #     coeff = coeff + cycString[i]
            #     i = i + 1
            # toke = Token("coefficient", coeff)
            # raw_cycles.append(toke)

        # toke = Token("cycle", xvar)
        # processRawToken(xvar)
        # raw_cycles.append(toke)
        
        i = i +1
    return tokens


        # while cycleStuctStr[i]


        


if __name__ == '__main__':
    
    starGrid = StarGrid()
    print starGrid.myCycleStruct.coefficient
    ns = "x1^4/24 + (x1^2*x2)/4 + x2^2/8 + (x1*x3)/3 + x4/4"
    starGrid.sym2 = ns
    print starGrid.sym2
    splited = starGrid.sym2.split('+')
    print "GOING IN"
    tokens = []
    for x in splited:
        
        print x
        tokens = runLexxer(x.strip())
        cysStruct = CycleStructure()

        #print x.find('/')


    # print splited
    # for cycleStuctStr in splited:
    #     print cycleStuctStr
    #     for i,l in enumerate(cycleStuctStr):
    #         sym = getNextSymbol(i, cycleStuctStr )
    #         print l,







