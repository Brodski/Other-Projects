import copy
def mlgPrint(matrix):
    for row in matrix:
        for e in row:
            print '%4s' % e,
        print

def isBlockedInWall(matrix, row, col):
    
    width = len(matrix[0])
    height = len(matrix)
    if row + 1 >= height or col + 1 >= width:
        return False
    dx = [ 0, 1, 1, 1, 0,-1,-1,-1 ]
    dy = [ 1, 1, 0,-1,-1,-1, 0, 1]
    if col+1 < width and row+1 < height and col-1 >= 0 and row-1 >= 0 :
        surEles = []
        for i in range(8):
            surEles.append( matrix[row+dy[i]][col+dx[i]] )
        for x in range(0,8,2):
            strike = []
            for r in range(5):
                wtf = surEles[(x-2)%8]
                strike.append(wtf)
                if wtf == 0:
                    continue
            if sum(strike) == 5:
                return True
        return False
    return False


def findRemovableWalls(matrix):
    removables = []
    for i,row in enumerate(matrix):
        for j,ele in enumerate(row):
            #if ele == 1 and isZeroAdjacent(matrix,i,j):
            if ele == 1 and not isBlockedInWall(matrix,i,j):
                removables.append([i,j])
    return removables

def rewriteMap(distanceList, rem):
    for i,row in enumerate(distanceList):
        for j,ele in enumerate(row):
            if ele == 1: row[j] = "#"
            else: row[j] = None
    distanceList[0][0] = 0
    if rem: distanceList[rem[0]][rem[1]] = None
    return distanceList

def solveMap(matrix, rem=None):
    width = len(matrix[0])
    height = len(matrix)
    distanceList = copy.deepcopy(matrix)
    que = []
    que.append([0,0])
    count = 0
    distanceList = rewriteMap(distanceList, rem)
    
    def getAdj(row,col):
        adjNodes=[]
        dx = [-1, 1, 0, 0]
        dy = [0,  0, 1, -1]
        for i in range(4):
            row2 = row + dx[i]
            col2 = col+ dy[i]
            if row2 < 0 or col2 < 0: continue
            if row2 >= height or col2 >= width: continue

            if distanceList[row2][col2] == None:
                distanceList[row2][col2] = distanceList[row][col] + 1
                adjNodes.append([row2,col2])
        return adjNodes        

    while que:
        count = count + 1
        allAdj = []
        while que:
            node = que.pop()
            adjacents = getAdj(node[0],node[1])
            allAdj = allAdj + adjacents
        for adj in allAdj:
            que.append(adj)
    print ''
    mlgPrint(distanceList)
    return distanceList[-1][-1] + 1

def checkIfOptimal(ans, width, height):
    if ans == (width + height -1):
        return True
    return False
    
def solution(matrix):
    width = len(matrix[0])
    height = len(matrix)
    removables = findRemovableWalls(matrix)
    allPossibleAnswers = []
    
    # 1st get solution w/o removing walls
    ans = solveMap(matrix)
    if checkIfOptimal(ans, width,height):
        return ans
        
    # check solution after removing walls
    for rem in removables:
        ans = solveMap(matrix, rem)
        allPossibleAnswers.append(ans)
        if checkIfOptimal(ans,width,height):
            return ans

    return min(allPossibleAnswers)
   
if __name__ == '__main__':

  maps = []
  maps.append([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0] ] )
  
  maps.append([ [0, 1, 1, 0, 0,0,0,0,0,0,0,0,0], 
                [0, 0, 0, 1, 0,0,0,0,0,0,0,0,0], 
                [1, 1, 0, 0, 0,0,0,0,0,0,0,0,0], 
                [1, 1, 1, 0, 0,0,0,0,0,0,0,0,0], 
                [1, 1, 1, 0, 0,0,0,0,0,0,0,0,0], 
                [1, 1, 1, 0, 0,0,0,0,0,0,0,0,0], 
                [1, 1, 1, 0, 0,0,0,0,0,0,0,0,0], 
                [1, 1, 1, 0, 0,0,0,0,0,0,0,0,0], 
                [1, 1, 1, 0, 0,0,0,0,0,0,0,0,0], 
            ] )
            
  maps.append([ [0, 0, 0, 1, 0,0,0,1], 
                [1, 0, 0, 0, 0,1,0,0], 
                [0, 1, 0, 0, 0,0,1,0], 
                [1, 0, 0, 1, 0,0,0,0], 
                [1, 0, 0, 1, 1,0,0,1], 
                [0, 0, 0, 1, 1,0,0,0], 
                [0, 1, 0, 0, 1,0,0,0], 
                [0, 1, 0, 1, 1,0,1,1], 
                [0, 1, 0, 1, 1,0,0,0], 
                [0, 1, 0, 0, 0,0,0,1], 
                [0, 1, 0, 0, 0,1,0,1], 
                [0, 1, 0, 1, 0,0,0,0], 
            ] )
            
  maps.append([[0, 0, 0, 0, 0, 0], 
              [1, 1, 1, 1, 1, 0], 
              [0, 0, 0, 0, 0, 0], 
              [0, 1, 1, 1, 1, 1], 
              [0, 1, 1, 1, 1, 1], 
              [0, 0, 0, 0, 0, 0]])
            
  
  maps.append([ [0, 1, 1, 0, 0,0,0,0,0,0,0,0,0], 
                [0, 0, 0, 1, 0,1,0,1,1,1,0,0,0], 
                [1, 1, 0, 0, 0,1,0,1,1,0,1,1,0], 
                [1, 1, 1, 0, 0,1,0,1,1,0,0,0,0], 
                [1, 1, 1, 0, 0,1,0,1,1,0,1,1,1], 
                [1, 1, 1, 0, 0,1,0,1,1,0,0,0,0], 
                [1, 1, 1, 0, 0,1,0,1,1,0,0,0,0], 
                [1, 1, 1, 0, 0,1,0,1,1,0,1,1,0], 
                [1, 1, 1, 0, 0,1,0,0,0,0,1,0,0], 
            ] )
  maps.append([ [0, 1, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 1, 1],
                [1, 1, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1, 0, 1],
                [0, 0, 1, 1, 1, 0, 1],
                [0, 0, 0, 0, 0, 0, 0],
            ])  
  maps.append([   [0, 0, 0, 0, 1, 1],
                  [1, 1, 0, 1, 0, 1],
                  [0, 0, 0, 1, 0, 1],
                  [0, 1, 1, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0],
            ])    
  maps.append([   [0, 1, 0, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 1, 1],
                  [1, 1, 1, 0, 1, 0, 1],
                  [1, 0, 0, 0, 1, 0, 1],
                  [0, 0, 1, 1, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0],
            ])  
  maps.append([ [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],    
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
                [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                ])
  
  
  maps.append([ [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                  [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                ])
  #for i in range(100):
  #ans = solution(maps[-1]) 
  ans = solution(maps[0])
  print ans
  print ans
  print ans
  print ans
  print ans