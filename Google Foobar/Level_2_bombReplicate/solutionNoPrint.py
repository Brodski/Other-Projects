
def solution(x, y):
    M = long(x)
    F = long(y)
    counter = 0
    
    while M >= 2 or F >= 2:
        #makes slight faster
        if M % F == 0 and F > 1:
            return "impossible"
        if F % M == 0 and M > 1:
            return "impossible"
            
        #for cases like f(9 000 000 001, 9 000 000 000)
        if M == 1:
            counter = counter + F - 1
            F = 1
            continue    
        if F == 1:
            counter = counter + M - 1
            M = 1
            continue
        
        #fast for cases like f(10^40, 101)
        if M > F:
            counter = counter + M/F
            M = M - (M/F)*F
            continue
        else:
            counter = counter + (F/M)
            F = F - (F/M)*M
            continue
    return str(counter)