import math
import sys  


def bombHelp2(M,F):
    counter = 0
    print '(F % M)', F,"%",M ,"=",    float(F) % float(M)
    print '(M % F)', M,"%",F,"=",   float(M) % float(F)
    
    while M >= 2 or F >= 2:
    
        print counter, "(M,F)", [M,F]        
        
        if M < 1 or F < 1:
            print "------> SOMETHING IS WRONG"
            return "impossible"
        if M % F == 0 and F > 1:
            print "------> SOMETHING IS WRONG"
            return "impossible"
        if F % M == 0 and M > 1:
            print "------> SOMETHING IS WRONG"
            return "impossible"
        
        if M == 1:
            print "->          M,F :", M,F
            counter = counter + F - 1
            F = 1
            continue    
        if F == 1:
            print "->          M,F :", M,F
            counter = counter + M - 1
            M = 1
            continue
              
        if M > F:
            print "    M", F, "diff"
            print "     ", M/F, "floor(big/diff)" #math.floor(M/F) = number of times the diff can go into big
            print "     ", ((M-F)/F), "steps"
            print "     ", (M/F)*F, "dist"
            counter = counter + M/F
            M = M - (M/F)*F
            continue
        else:
            print "    F", M, "diff"
            print "     ", F/M, "fllor(big/diff)"
            print "     ", (F-M)/M, "steps"
            print "     ", (F/M)*M, "dist"
           #print "     ", F - ((F-M)/M)*M
            counter = counter + (F/M)
            F = F - (F/M-0)*M
            continue
    return counter


def solBomb(M,F):
    x = bombHelp2(M,F)
    print 'DONE'
    return str(x)
            
if __name__ == '__main__':

 #x2 = makeThat([3,4,5,7,6,1,2,1])
 
 #x = solBomb(812,131)
 arrOfTests = []
 arrOfTests.append( [1,3]  )
 arrOfTests.append( [12,3]  )
 arrOfTests.append( [143,3]  )
 arrOfTests.append( [17,34]  )
 arrOfTests.append( [1,1]  )
 arrOfTests.append( [10**3,3]  )
 arrOfTests.append( [31,546]  )
 arrOfTests.append( [64351,344]  )
 arrOfTests.append( [10,55]  )
 arrOfTests.append( [103030,3234]  )
 arrOfTests.append( [69,42]  )
 arrOfTests.append( [42,69]  )
 arrOfTests.append( [13,4]  )
 
 arrOfTests.append( [12,24]  )
 arrOfTests.append( [12,36]  )
 arrOfTests.append( [18,36]  )
 arrOfTests.append( [17,35]  )
 
 arrOfTests.append( [121,122]  )
 arrOfTests.append( [21,22]  )
 arrOfTests.append( [9,8]  )
 arrOfTests.append( [9111111111111111111,9111111111111111112]  )
 arrOfTests.append( [13, 147]  )
 wtf =  1.6248*(10**42 )
 wtf2 =  1.234*(10**4)
 arrOfTests.append( [ wtf,wtf2]  )
 wtf =  10**40
 wtf2 =  101
 arrOfTests.append( [ wtf,wtf2]  )
 #arrOfTests.append( [1030303237,13234]  )
 #
 
 for i in arrOfTests:
    print '+++++++++++++++++++++++++'
    x = solBomb(i[0],i[1])
    print x
 
 
 #x = solBomb(10**43,9**44)
 #x = solBomb(41,69)
 #x = solBomb(42,69)
 #x = solBomb(2,4)
 #x = solBomb(2,1)
 #x = solBomb(11,12)
 #x = solBomb(2**25,9**13)
 #x = solBomb(4,7) 
 #print x
 
 
 
 
 