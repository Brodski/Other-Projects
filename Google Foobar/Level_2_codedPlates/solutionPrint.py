
import itertools
def makeThat(L):
    i = 0
    combos = []
    while i < len(L):
        print '++++++++++++++'
        subCombo = itertools.combinations(L, i+1)
        subCombo = [list(c) for c in subCombo]
        combos = combos + subCombo
        print subCombo

        i = i + 1
    
    
    print '----------------'
    answers = []
    for c in combos:
        if sum(c) % 3 == 0:
            print "yes"
            print c
            answers.append(c)
        
    if not answers:
        return 0
    print '----------------'
    for a in answers:
        a.sort(reverse=True)
        print a
        
    print '----------------'
  #  answers.sort(reverse=True)
  
    answersWhole = []
    for a in answers:
        a.sort(reverse=True)
        a2 = ''.join([str(i) for i in a])    
        answersWhole.append(int(a2))
    answersWhole.sort()
    for a in answersWhole:
        print a
    return answersWhole[-1]