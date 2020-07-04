
def solutionxd(l, t):
   # find all subsequences that sums to t
    allPossMsg = []
    msgIndices = []
    for index,val in enumerate(l):
        msg = []
        total = 0
        for i2 in l[index:]:
            total = total + i2
            msg.append(i2)
            if total == t:
                allPossMsg.append(msg)
                break
            if total > t:
                break
            
    if not allPossMsg:
        print 'we going home'
        msgIndices = [-1,-1]
        print msgIndices
        return msgIndices
        
    # find index of our msg
    allPossMsg.sort()
    want = allPossMsg[0]
    print l
    print allPossMsg
    print want
    # get all indices in l which might have our subsequence
    indices = [i for i, val in enumerate(l) if val == want[0]]
    for i in indices:
        print 'going'
        subseq = l[i: i + len(want)]
        if sum(subseq) == t:
            msgIndices = [i, i + len(want)-1]
            break
    print msgIndices
    return msgIndices

    