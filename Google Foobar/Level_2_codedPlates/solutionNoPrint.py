   
def solution3(l):
    '''
    it is possible for len(l) = 9.
    if we try to find all combinations with 9 digits we would
    search for 9! combinations = 362,880. That would take way
    too long. a quick google search reveals a trick.
    A number is divisible by 3 if the sum of all digits is 
    divisible by 3. Cool
    '''
    i = 0
    combos = []
    while i < len(l):
        subCombo = itertools.combinations(l, i+1)
        subCombo = [list(c) for c in subCombo]
        combos = combos + subCombo
        i = i + 1
    answers = []
    for c in combos:
        if sum(c) % 3 == 0:
            answers.append(c)
    if not answers:
        return 0
        
    #do order & sort        
    answersInt = []
    for a in answers:
        a.sort(reverse=True)
        a2 = ''.join([str(i) for i in a])    
        answersInt.append(int(a2))
    answersInt.sort()
    return answersInt[-1]
    
