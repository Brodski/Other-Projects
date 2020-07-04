
'''
Recall: x divides y and y divides z => x|z

Algorithm works like this (abridged version):
Solve the smallest case, first 3 elements of L. 
Record if any elements are divisible by each other.
Add the next element. Check if it divides any 
previous element, if so record it and for each 
element it can divide we add it to the number of 
times that the element divides previous elements 
in the list.

   1  2  3  4  5  6
1 [0, 1, 1, 1, 1, 1]
2 [0, 0, 0, 1, 0, 1]
3 [0, 0, 0, 0, 0, 1]
4 [0, 0, 0, 0, 0, 0]
5 [0, 0, 0, 0, 0, 0]
6 [0, 0, 0, 0, 0, 0]

SUM
[0, 1, 1, 2, 1, 3]

'''
def solution(L):
    print '------------------------------'
    arrIsDivisible = [[0 for x in range(len(L)) ] for y in range(len(L) ) ] 
    sumDivisions = [0] * len(L)
    print L
    ans = 0
            
    for row,x in enumerate(L):
  #      print 
        for col,y in enumerate(L[row+1:], row+1):
   #         print x,y, '=>',(y % x)==0,'     @'.ljust(2), row,col
            if y % x == 0:
                arrIsDivisible[row][col] = arrIsDivisible[row][col] + 1 # 1 => true, is divisible
                sumDivisions[col] = sumDivisions[col] + 1
                ans = ans + sumDivisions[row]
    print
    print "SUM"
    print sumDivisions
    print
    
    for a in arrIsDivisible:
        print a
    print 
    print L
    print "ANS"
    print ans
    
def brute(L):
    myL = len(L)
    cnt = 0
    for i in range(len(L)):
        ii = i
        for j in range(i+1, len( L ) ):
            jj = j
     #       print "----------",i,j,"----------"
            for k in range(j+1, len( L ) ):

                kk = k
                x = L[i]
                y = L[j]
                z = L[k]
                if (y % x ==0) and (z % y == 0):
                    print 'yes', x,y,z
                    cnt = cnt + 1
    print "DONE!!!"
    print cnt
    
if __name__ == '__main__':
 

  t0 = [ 1,2,3,4,5,6]
  t = [5,10,15,10,7]
  t1 = [ 1,1,1]
  t2 = [ 1,1,1,1,1,1]
  t3 = [5,10,15,10]
  
  a = [5,10,15,10,2]
  a2 = [5,10,15,10,2,10]
  
  b = [1,2,4]
  b2 = [1,2,4,8]
  z = [5,10,15,10,2,10, 5,10,15,10,2,10]
  
  doIt = t0
  brute(doIt)
  
  solution(doIt)
  