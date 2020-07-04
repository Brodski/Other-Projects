def solution(data, n):
    print data
    print n
    dataDict = {}
    finalSol = []
    print '--------------'
    for k in data:
        print k
        if k not in dataDict.keys():
            print "not in"
            dataDict[k] = 1
        else:
            print "is in"
            print dataDict[k]
            dataDict[k] = dataDict[k] + 1
    print dataDict
    
    
    for d in data:
        if dataDict[d] <= n:
            print "adding: ", d
            finalSol.append(d)
    print '--------------'
    print data
    print finalSol
    return finalSol        
	
	
	
	
if __name__ == '__main__':
 #solution([1,2,3], 1)
 #solution([1,2,3,1,1,3,5, 52348,234,2,2], 3)
 #solution( [1,4,4,142,8,4,8,6,6,6,6,6,3,4], 3)
 solution( [5,10,15,10,7], 1)
	
	
#	myDict = { 1: [2], 10: [99,123]}
#	print(myDict)
#	print('----')
#	  print(it)
#	print('----')  
#	for k in myDict:
#	  print(k)
#	  print(myDict[k])
#	print('----')
#	
#	md = {}
#	md[5] = 'lol'
#	print(md)
#	md[5] = 'lol2'
#	md[4] = 123
#	print(md)
#	if 6 not in md.keys():
		#print("Not in")
		#someStuff = [1,2,21,1,1,1,4,5]
#	print(someStuff)
#	print "hellp ", someStuff