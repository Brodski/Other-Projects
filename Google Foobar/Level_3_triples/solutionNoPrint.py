
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
    
    sumDivisions = [0] * len(L)
    ans = 0
    
    for i,x in enumerate(L):
        for j,y in enumerate(L[i+1:], i+1):
            if y % x == 0:
                sumDivisions[j] = sumDivisions[j] + 1
                ans = ans + sumDivisions[i]
    return ans