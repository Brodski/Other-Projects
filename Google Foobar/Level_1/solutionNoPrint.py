# remove from the list "data" all items that occur n or more times (keep all that occur les than n)

def solution(data, n):
    dataDict = {}
    finalSol = []
    for d in data:
        if d not in dataDict.keys():
            dataDict[d] = 1
        else:
            dataDict[d] = dataDict[d] + 1
    
    for d in data:
        if dataDict[d] <= n:
            finalSol.append(d)
    return finalSol
    
    
    
    
    