import numpy as np
import copy


'''

* <----- acts on
x <----- acts on

keep in mind, when we act on the set we produce s/t in the set 
    (can be anything in the set; edges, vertices, or faces)
    
symemetrices of an object form a group. 

group acts on set of veritescs/edges/faces gives the same set

eg)
x  = set of vertices = {1, 2,3,4}

o * 1 = 1   <--- sigma acts on vertex 1, producing 1  
sigma 



'''
def mlgPrintCol(m2d, c1, c2):

    print '_____________________'
    print "Swap Col!", c1, c2
    print " ",
    for i in range(len(m2d[0])):
        if i == c1: 
            print "-".rjust(3),
        elif i == c2: 
            print "+".rjust(3),
        else:
            print "".rjust(3),
    print
        
    for i, row in enumerate(m2d):
        print "[",
        for x in row:
            print str(x).rjust(3),
        print " ]"

def mlgPrintRow(m2d, r1, r2):
    print "_____________________"
    print "Swap Row!", r1, r2
    print 
    for i, row in enumerate(m2d):
        print "[",
        for x in row:
            print str(x).rjust(3),
        if i == r1: 
            print " ] -"
        elif i == r2: 
            print " ] +"
        else: 
            print " ]"

def swapRow(the2d, r1, r2):
    m2d = copy.deepcopy(the2d)
    m2d[[r1, r2]] = m2d[[r2, r1]]
    mlgPrintRow(m2d,r1,r2)
    return m2d
    
    
def swapCol(the2d, c1, c2):
    m2d = copy.deepcopy(the2d)
    m2d[:,[c2,c1]] =  m2d[:,[c1,c2]]
    mlgPrintCol(m2d, c1, c2)
    return m2d
    
def doSwapper():
    
    a3 = np.arange(12).reshape(3,4)
    original = copy.deepcopy(a3)
    
    a3 = swapCol(a3,2,3)
    a3 = swapCol(a3,0,3)
    
    a3 = swapRow(a3,0,2)
    print "\n========================================"
    print "========================================"
    print "\nDone"
    print "Original"
    print original
    print "new"
    print a3
    
def doSwapper2():
    a3 = np.arange(6).reshape(2,3)
    original = copy.deepcopy(a3)
    
    a3 = swapCol(a3,1,2)
    a3 = swapCol(a3,0,2)
    
    a3 = swapRow(a3,0,1)
    
    
    print '=================='
    a3 = np.arange(6).reshape(2,3)
    original = copy.deepcopy(a3)
    
    a3 = swapCol(a3,0,2)
    a3 = swapCol(a3,1,2)
    
    a3 = swapRow(a3,0,1)
    
    
def doMLGSwapper():
    a3 = np.arange(16).reshape(4,4)
    original = copy.deepcopy(a3)
    cmoves = []
    rmoves = []
    cmoves.append( [1,2]  )
    cmoves.append( [2,1]  )
    rmoves.append( [1,3]  )
    rmoves.append( [4,3]  )
    cmoves.append( [0,2]  )
    a = swapCol(a3, 1,2 )
    a = swapCol(a, 2,1 )
    a = swapRow(a, 1,3 )
    a = swapRow(a, 3,2 )
    a = swapRow(a, 0,2 )
    print "og"
    print original
    print "new"
    print a
        
    
#  CycleIndexPolynomial[ SymmetricGroup[3], {x1,x2,x3}]

# @2 --> x1^2/2 + x2/2
# @3 --> x1^3/6 + x1*x2/2 + x3/3
# @4 --> x1^4/24 + (x1^2 * x2)/4 + x2^2/8 + x1x3/3 + x4/4
# @5 --> x1^5/120 + x1^3*x2/12 + x1x2^2/8 + x1^2*x3/6 + x2x3/6 + x1x4/4 + x5/5
#
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

# https://mathematica.wolframcloud.com/
# wolfram SymmetricGroup https://mathworld.wolfram.com/SymmetricGroup.html
#
# # Combinatorics 16.12 The Pattern Inventory  Polyas Method of Enumeration https://www.youtube.com/watch?v=Tkz8QGPHxdA
# Polya Theorem (Part 2) https://www.youtube.com/watch?v=zQZ4kTiaqQI
# How many distinct unsolvable Rubik's cubes exist? https://puzzling.stackexchange.com/questions/525/how-many-distinct-unsolvable-rubiks-cubes-exist
# (crl + f = matrices)     https://math.meta.stackexchange.com/questions/1868/list-of-generalizations-of-common-questions#13335
    
import math 

def M23(N):
    print "Eval at N:", N
    N = float(N)
    a = (1.0/12) *math.pow(N,6)
    a2 = (1.0/3)*math.pow(N,3 )
    a3 = (1.0/6)*math.pow(N,2 )
    a4 = (1.0/4)*math.pow(N,4 )
    a5 = (1.0/6)*math.pow(N, 1)
#    print a
 #   print a2
  #  print a3
   # print a4
    #print a5
    print a + a2 + a3 + a4 + a5
    
if __name__ == '__main__':
    #doSwapper()
    #doSwapper2()
    #doMLGSwapper()
    M23(1)
    M23(2)
    M23(3)
    M23(4)