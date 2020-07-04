import itertools
import copy

def solution(num_buns, num_required):
    
    keys = [0]* num_buns
    print keys
    
    someList = itertools.combinations('1234567890', 6)
    print 'combos'
    c = 0
    for l in someList:
        print 
        c += 1
        for x in l:
            print x,
        if c == 5:
            print
            break
    print '----------'
    A = {'A', 'B', 'C', 'D', 'E'} 
    B = {'1', '2', '3', '4', '5', 'A', 'C'} 
    print A
    print B
    res = A.symmetric_difference(B)
    print res
    print '----------'
    res = A.symmetric_difference_update(B)
    print A
    print B
    print res
    print '----------'
    
    a1 = {0,1,2,3,4,5 }
    a2 = {0,1,2,6,7,8 }
    a3 = {0,3,4,6,7,9 }
    a4 = {1,3,5,6,8,9 }
    a5 = {2,4,5,7,8,9 }
    
    all = [ a1,a2,a3,a4,a5]
    
    i1 = a1.intersection(a2)
    i2 = a1.intersection(a3)
    i3 = a2.intersection(a3)
    ii1 = a1.intersection(a2, a3)
    ii2 = a1.intersection(a2).intersection(a3)
    print i1
    print i2
    print i3
    print ii1
    print ii2
    print '----'
    for i,a in enumerate(all):
        #print  #a, "huh"
        print i
        for k,b in enumerate(all[i+1:], i+1):
            #print #a,b, "@", i,k            
            print i,k
            for j,c in enumerate(all[k+1:], k+1):
            #print a.intersection(b)
#                print a,b,c, "@", i,k,j
             #   print a.intersection(b,c), "@", i,k,j
                print a.difference(b).difference(c), "@", i,k,j
          #      print a.union(b,c), "@", i,k,j
          
          
    a1 = {0}
    a2 = {1}
    a3 = {2}
    a4 = {4}
    all2 = [ a1,a2,a3,a4]
    print '==============='
    print '==============='
    
    all = all2[:-1]
    print all
    interAll = all[0]
    for i,a in enumerate(all):
        print interAll, ' v ', a
        theInt = interAll.intersection(a)
        interAll.update(theInt)
        print interAll
        #for k,b in enumerate(all[i+1:], i+1):
         #   print a,b, "@", i,k            
         #   print i,k
          #  for j,c in enumerate(all[k+1:], k+1):
           # #print a.intersection(b)
            #    print a,b,c, "@", i,k,j
             #   print a.intersection(b,c), "@", i,k,j
         #       print a.symmetric_difference(b).symmetric_difference(c), "@", i,k,j
        #        print a.union(b,c), "@", i,k,j
   
#    [0 1 2 3 4 5] 
 #   [0 1 2 6 7 8] 
  #  [0 3 4 6 7 9] 
   # [1 3 5 6 8 9] 
    #[2 4 5 7 8 9]

from scipy.special import comb
import math

def mprint(msg, cond=1):
    if cond == 1:
        print msg

def nchoosek(n,k):
    return math.factorial(n) / (math.factorial(k)*math.factorial(n-k) )
    
import numpy

def other2(num_buns,num_required):
    print nchoosek(1,1)
    print 'buns', num_buns
    print 'req ', num_required
    
    max = 15
    #comboArr = []
    comboArr = numpy.zeros(shape=(max,max))
    mprint( numpy.matrix(comboArr))
    all_chains = []
    key_chain  = []
    
    
    someArr = []
    for i in range(max):
        print '-----i', i, someArr
        someArr.append(i)
        #comboArr[i] =  [0]*(i+1 )
        for k in range (0,len(someArr)):
            coms = nchoosek(i,k)
            comboArr[k,i] =  coms
    print '----------------------------------------------------------------------------------------'
    for i in range(max):
        print repr(i).rjust(4),
    print
    print '----------------------------------------------------------------------------------------'
    for j,combo in enumerate(comboArr):
        for x in combo:
            if x == 0: print "-".rjust(4),
            else: print repr(int(x)).rjust(4),
        if (j+1) % 5 == 0: print 
        print 
    
    lol = [0,1,2,3,4,5,6,7,8,9]
    x = itertools.combinations(lol,6)
    for i,combo in enumerate(x):
        print i, list(combo)
        
       
        
def checkSol(  ):
    num_buns = 5
    num_req = 3
    
    
    arr2 = [ [0,1,2,3,4,5],
        ['a0','a1','a2','a3','a4','a5'],
        ['b0','b1','b2','b3','b4','b5'],
        ['c0','c1','c2','c3','c4','c5'],
        ]
    
    marr = copy.deepcopy(arr2)
    multiArr = itertools.combinations(arr2, num_req)
    print "YREAh"
    for combo in multiArr:
        print "YEAH"
        for c in combo:
            print c
    
    key_each = []
    allKeys= []
    max = 10
    for i in range(6):
        print "TOP ", i
        allKeys.append(i)
        for j in range(1,i+1):
            print "itering @", i+1,j
            print "          ", allKeys
            someCombs = itertools.combinations(allKeys, j)
     #       doUnion(someCombs, allKeys)

def doUnion(mSet,allKeys):
    all = set()
    print "WE DOIGN THE UNIONS"
    print "      allKeys:  ", allKeys
    for s in mSet:
        all = all.union(s)
        all2 = list(all)
      #  print "      adding:   ", list(s), '--->', all2
        if allKeys == all2:
            pass
            #print "      WOAH      ", allKeys, '=', all2
            #print "      Our combs:", list(mSet)
    print "OUT"

def otherSol(num_buns, num_required):

    print 'buns', num_buns
    print 'req ', num_required
    
    all_chains = []
    key_chain  = []
    
    someArr = []
    for i in range(7):
        print '-----i', i, someArr
        someArr.append(i)
        for k in range (1,len(someArr)):
            print '++++k', k
            combo = itertools.combinations(someArr,k)
            #print combo
            for x in combo: 
                pass
             #   print list(x)
                #print len(list(x))
                #print x[0]
    
def moreThings(num_buns=None, req=None):
    num_buns = 5
    req = 3
    if num_buns < req:
        print "lol wrong input"
        return
    if req == num_buns:
        print 'are equal'
        print num_buns
        return num_buns
    Ls = None
    #width = num_buns
    width = 1
    #for width in range(1,11):
    while True:
        area = num_buns * width
        Ls = float(area) / req
        diff = num_buns - req
        value = width + (diff) # satisfies 'no group of num_requried-1 bunnies can open the lock'
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print "num_buns", num_buns, "num req", req
        print "width", width
        print "area", area, "- num locks", Ls
        print Ls.is_integer()
        print "Ls",Ls
        
        print "width + req - 1 ", 2* width + req - 1
        #print value < Ls, value, ": width - (num_buns + req ) < Ls"
        #if Ls.is_integer() and value < Ls:
        if Ls.is_integer() and Ls >= width + req - 1:
            if req > 2 and width > req:  # ??
                break
        width = width + 1
    print "\n\nDONE"
    print "width:", width
    print "locks:", Ls
    #bruteTryIt(Ls, num_buns, req, width)
    #cleverIt(Ls, num_buns, req, width)
    cleverIt2(Ls, num_buns, req, width)
    
    
def idxPrint(indexesList, lockCombos, s=0):
    print " "*s, "_________________________________ "
    for idx in indexesList:
        print " "*s, "|", idx, "-->", lockCombos[idx], "|"
    print " "*s, "_________________________________"


    
def cleverIt2(Ls, buns, req, width):
    print   '---------clever IT----------------'
    locks =  []
    bunKeys = [ [] for x in range(buns)]  
    for i in range(int(Ls)): locks.append(i) 
    lockCombos = [ set(x) for x in itertools.combinations(locks, width) ]
    sendBunnies = [ [] for x in range(req) ]
    
    #bunnyIndexes = [0] * buns
    #sendIndexes = [0] * req
    
    sendCounter = 1
    bunnyCounter = 1
    solutionCounter = 0 # ???
    magicIndex = 1
    
    #bunnyIndexes[0] = lockCombos[0]
    #sendIndexes[0] = lockCombos[0]

    bunnyIndexes = []
    sendIndexes = []
    bunnyIndexes.append(0) #point to first lock combo
    sendIndexes.append(0)
    while bunnyCounter != buns:
        mg = magicIndex
        if magicIndex == len(lockCombos)-1:
            print "hehe"
        if magicIndex == len(lockCombos):
            idxPrint(sendIndexes+ [magicIndex-1], lockCombos)
            magicIndex = sendIndexes.pop()
            bunnyIndexes.pop()
            magicIndex += 1
        keyCandidate = lockCombos[magicIndex]
        sendIndexes.append(magicIndex)
        if len(sendIndexes) < req:
            isPreGood = preCheckCandidate(keyCandidate, sendIndexes, sendBunnies, sendCounter, locks, lockCombos)
            if isPreGood:
                magicIndex += 1
                continue
            else:                
                sendIndexes.pop()
                magicIndex += 1
                continue
        if len(sendIndexes) == req:
            isPostGood = postCheckCandidate(keyCandidate, sendIndexes, sendBunnies, sendCounter, locks, lockCombos)
            if isPostGood:
                print "\nWE GOOD BABY!!!"
                print "Send:"
                idxPrint(sendIndexes, lockCombos, 10)
                print "Bunnies:"
                idxPrint(bunnyIndexes, lockCombos,10)
                isValid = checkFullValid(sendIndexes, bunnyIndexes, buns, req, lockCombos, locks)
                if isValid:
                    print " " * 8, "solutionCounter", solutionCounter
                    bunnyIndexes[solutionCounter: len(sendIndexes)] = sendIndexes
                    sendIndexes = sendIndexes[1:len(sendIndexes)]
                    magicIndex += 1
                    solutionCounter += 1
                    print "Send NEW:"
                    idxPrint(sendIndexes, lockCombos, 4)
                    print "Bunnies NEW:"
                    idxPrint(bunnyIndexes, lockCombos, 4)
                    print " Leavning\n"
                else:
                    print " IT DOESNT WORK ...Leavning\n"
                    sendIndexes.pop()
                    magicIndex += 1
            else:
                sendIndexes.pop()
                magicIndex += 1

def checkFullValid(sendIndexes, bunnyIndexes, buns, req, lockCombos, locks):
    bunnyKeys = []
    for i in bunnyIndexes:
        bunnyKeys.append(lockCombos[i])
        
    sendKeys = []
    for i in sendIndexes:
        sendKeys.append(lockCombos[i])
        
    both = copy.deepcopy(bunnyKeys)
    for x in sendKeys:
        if x not in both:
            both.append(x)
            
    # Union all = locks
    comboz = itertools.combinations(both, req)
    for c in comboz:
        ll = set()
        for cc in c:
            ll = ll.union(set(cc))
        if ll != set(locks):
            return False
    # Union n-1 != locks
    comboz2 = itertools.combinations(both, req-1)
    for c in comboz2:
        ll = set()
        for cc in c:
            ll = ll.union(set(cc))
        if ll == set(locks):
            return False
    return True
                        
        
                
                
def preCheckCandidate(keyCandidate, sendIndexes, sendBunnies, sendCounter, locks, lockCombos):
    #pre Union
    #  A union B != lcokset
    values = []
    for i in sendIndexes:
        values.append(lockCombos[i])
    if set().union(*values[0:len(sendIndexes)]) == set(locks):
        return False
    return True
                
                
def postCheckCandidate(keyCandidate, sendIndexes, sendBunnies, sendCounter, locks, lockCombos):
    #final Union
    # A union B == lockset
    values = []
    for i in sendIndexes:
        values.append(lockCombos[i])
    if set().union(*values) != set(locks):
        return False
    return True

    
    
def cleverIt(Ls, buns, req, width):
    print   '---------clever IT----------------'
    locks =  []
    bunKeys = [ [] for x in range(buns)]  
    for i in range(int(Ls)):
        locks.append(i) 
    print numpy.array(bunKeys)
    
    lockCombos = [ set(x) for x in itertools.combinations(locks, width) ]
    sendBunnies = [ [] for x in range(req) ]
    sendCount = 0
    fullCount = 0
    allAnswers = []
    for i, keySet in enumerate(lockCombos):
        print  "+++", i, "+++", keySet
        if i == 0:
            bunKeys[0] = keySet
            sendBunnies[0] = keySet
            sendCount = sendCount + 1
            fullCount = fullCount + 1
            continue
        if not bunKeys[fullCount]:
            findNextFrom(lockCombos[i:])
            wut = bunKeys[fullCount]
            for k in range(1,req+1):
                sss = sendBunnies
                sc = sendCount
                print "        k", k
                print "          - keySet        ??", keySet
                print "          -"
                for i2,b in enumerate(sendBunnies): print "          - sendbunnies[",i2,"]", b
                if k>sendCount and not sendBunnies[sendCount-k]:
                    print '          - empty'
                    break
                xx = keySet
                x2 = sendBunnies[sendCount-k]
                yy = locks
                zz = keySet.intersection(sendBunnies[sendCount-k])
                                
                if keySet.intersection(sendBunnies[sendCount-k]) == locks :
                    print "oh no - intersection", keySet, sendBunnies[sendCount-k]
                    continue
                print "         ++ adding ", keySet
                sendBunnies[sendCount] = keySet #2st req
                flip = sendBunnies[sendCount]
                sendCount = sendCount + 1
                lol = len(sendBunnies)
                kk = k
                if len(sendBunnies) == k:
                    print '          - union all =', set().union(*sendBunnies)
                    if set().union(*sendBunnies) != locks:
                        sendBunnies = [ [] for x in range(req) ]
                        sendCount = 1
                        sendBunnies[0] = bunKeys[fullCount-1]
                        #print
                        #for i2,b in enumerate(sendBunnies): print "          - sendbunnies[",i2,"]", b
                        print "\n       NOPE NOPE NOPE\n"
                        continue
                    else:
                        print "YES \n     YES \n      YES"
                        print "YES \n     YES \n      YES"
                        print "YES \n     YES \n      YES"
                        print "YES \n     YES \n      YES"
                        fullCount = fullCount + 1
                        allAnswers.append(sendBunnies)

                        for b in sendBunnies: print "BUNNIES: ", b
    print "ANYTYHING?"
    for a in allAnswers:
        print a
                        
def findNextFrom(someArr):
    
    
    
        
                
        

    
    
    
    
    '''
    top = 0
    tempStrike = copy.deepcopy(strike)
    for i in range(top+1, req + top):
        if bunKeys[i]:
            bunKeys.append(tempStrike.pop())
        else:
            bunKeys[i] =[tempStrike.pop()]
        print i
    
    print numpy.array(bunKeys)
    '''
    
    
    
    
    
    
    
    
    
    '''
    combosKeys = itertools.combinations(locks, width)
    x = 0
    chains =[]
    for c in combosKeys:
        chains.append(c)
        print x, c
        x += 1
    edited = []
    setStrike = set(strike)
    for i,c in enumerate(chains[1:]):
        if setStrike.intersection(c) == setStrike:
            #print i, "YUP - c:", c, " - setStrike", setStrike
            continue
        edited.append(c)
    
    chooseKeys = [c for c in itertools.combinations(edited, req) ]
    for c in chooseKeys:
        print c
    print len(chooseKeys)
    
    print '-------'
    print len(edited)
    print len(chains)
    '''         
    
        
    
        
def bruteTryIt(locks_num, num_buns, req, width):
    print   '---------Brute----------------'
    locks =  []
    chains = []
    for i in range(int(locks_num)):
        locks.append(i) 
    combosKeys = itertools.combinations(locks, width)
    x = 0
    for c in combosKeys:
        chains.append(set(c))
        #chains.append(c)
        print x, c
        x = x +1
    print '+++++'
    x = set()
    bunsChainsCombos = itertools.combinations(chains, req)
    print locks
    #print chains
    bunsWithChainsArr = []
    for i, bc in enumerate(bunsChainsCombos):
        bunsWithChainsArr.append(bc)
        print i, list(bc)
    
    allPossible = []
    
    
    for i, bunsWithChains in enumerate(bunsWithChainsArr):
        #print i, list(bunsWithChains)
        print i, bunsWithChains
        response = sendRBunnies(bunsWithChains, set(locks))
        if response:
            allPossible.append(response)
    print "_+_+_+_+_+_+_+_+_+_"
    for r in allPossible:
        print r
    
        
def sendRBunnies(bunsWithChains, locks_set):
    print "         In "        
    # test if Union passes
    if set().union(*bunsWithChains) != locks_set:
        print '         fail'
        return False
    
    preBunsMinus1 = itertools.combinations(bunsWithChains, len(bunsWithChains)-1 )
    
    # iterable to list
    bunsMinus1 = []
    for b in preBunsMinus1:
        bunsMinus1.append(b)
        
    #test
    for b in bunsMinus1:
      #  print "testing", b
        if locks_set == set().union(*b):
     #       print "        full fail "
            return False
    #print "         full Pass ", bunsWithChains
    return  bunsMinus1
    #x = set()
    #if set().union(*bunsMinus1)
    
        
    
    


if __name__ == '__main__':
 
  a = [2, 1]
  t0 = 1
  doIt = t0
  
  #brute(doIt)
  #solution(2, 1)
  #solution(4, 4)
  #solution(5, 3)
  
  #otherSol(3,2)
  #other2(3,2)
  #checkSol()
  moreThings()

  #gcd()