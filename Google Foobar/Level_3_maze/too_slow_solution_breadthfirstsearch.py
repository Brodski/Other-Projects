import copy

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.width  = len(matrix[0])
        self.distanceMap = []
        self.noBombSolution = None
        self.bombCandidates = []
        
    def mlgPrint(self, map ):
        for row in map:
            for e in row:
                print '%4s' % e,
            print

    def isBlockedInWall(self, row, col):
        if row + 1 >= self.height or col + 1 >= self.width:
            return False
        dx = [ 0, 1, 1, 1, 0,-1,-1,-1 ]
        dy = [ 1, 1, 0,-1,-1,-1, 0, 1]
        
        if col+1 < self.width and row+1 < self.height and col-1 >= 0 and row-1 >= 0 :
            surEles = []
            for i in range(8):
                surEles.append( self.matrix[row+dy[i]][col+dx[i]] )
            for x in range(0,8,2):
                strike = []
                for r in range(5):
                    strike.append( surEles[(x-2)%8] )
                    if surEles[(x-2)%8] == 0:
                        continue
                if sum(strike) == 5:
                    return True
            return False
        return False

    def findRemovableWalls(self):
        removables = []
        for i,row in enumerate(self.matrix):
            for j,ele in enumerate(row):
                if ele == 1 and not self.isBlockedInWall(i,j):
                    removables.append([i,j])
        return removables

    def addWallToBombCandidates(self, node):
        if node not in self.bombCandidates:
            self.bombCandidates.append(node)

    def rewriteMap(self, rem):
        for i,row in enumerate(self.distanceMap):
            for j,ele in enumerate(row):
                if ele == 1: row[j] = "#"
                else: row[j] = float('inf')
        self.distanceMap[0][0] = 0
        print "REMOVEING HERE:", rem
        if rem: self.distanceMap[rem[0]][rem[1]] = None
        return self.distanceMap
        
    def getAdj(self, que):
        adjNodes=[]
        dx = [-1, 1, 0, 0]
        dy = [0,  0, 1, -1]
        for node in que:
            row,col = node
            for i in range(4):
               # print adjNodes
                row2 = row + dx[i]
                col2 = col+ dy[i]
                if row2 < 0 or col2 < 0: continue
                if row2 >= self.height or col2 >= self.width: continue
                if [row2,col2] in adjNodes: continue
                if self.distanceMap[row2][col2] == "#":
                    self.addWallToBombCandidates([row2,col2])
                    continue
                if self.distanceMap[row2][col2] == None or (self.distanceMap[row2][col2] > self.distanceMap[row][col]):# and self.distanceMap[row2][col2] != "#"):
                    
#                    self.distanceMap[row2][col2] = self.distanceMap[row][col] + 1
                    adjNodes.append([row2,col2])
        return adjNodes       

    def calcNextDist(self,que):
        nextNodes = []
   #     print "QUEUE"
   #     print que
        for node in que:
            row, col = node
            
            adjNodes = self.actualGetAdj(node)
            for adj in adjNodes:
                row2, col2 = adj
                if adj in nextNodes: continue
                if self.distanceMap[row2][col2] == "#":
                    self.addWallToBombCandidates([row2,col2])
                    continue
                if self.distanceMap[row2][col2] == None or (self.distanceMap[row2][col2] > self.distanceMap[row][col]):# and self.distanceMap[row2][col2] != "#"):
                    
#                    self.distanceMap[row2][col2] = self.distanceMap[row][col] + 1
                    nextNodes.append([row2,col2])
        return nextNodes       
                
            
    def actualGetAdj(self, node):
        adjNodes=[]
        row,col = node
 #       print " GETTING ADJ"
 #       print "(",row, col,")", "->", self.distanceMap[row][col]
        dx = [-1, 1, 0, 0]
        dy = [0,  0, 1, -1]
        for i in range(4):
            row2 = row + dx[i]
            col2 = col+ dy[i]
            if row2 < 0 or col2 < 0: continue
            if row2 >= self.height or col2 >= self.width: continue
            adjNodes.append([row2, col2])
     #   print adjNodes
        return adjNodes
        
    def smallestSurronding(self, rem):
    
            print "HERE WE GO"
            print "HERE WE GO"
            print "HERE WE GO"
            self.distanceMap = copy.deepcopy(self.noBombSolution)
            # 'destroy the wall then find a spot to begin algorithm
            self.distanceMap[rem[0]][rem[1]] = float('inf')
            startHere = [rem[0], rem[1]]
            adjNodes = self.actualGetAdj(rem)
            for adj in adjNodes:
                s0 = startHere[0]
                s1 = startHere[1]
                a0 = adj[0]
                a1 = adj[1]
                start = self.distanceMap[s0][s1]
                other = self.distanceMap[adj[0]] [adj[1]]
                if self.distanceMap[ startHere[0]] [startHere[1]] > self.distanceMap[adj[0]] [adj[1]]:
                    if not self.distanceMap[adj[0]] [adj[1]]:
                        print  adj
                        print self.distanceMap[adj[0]] [adj[1]]
                        print 'wtf mate'
                        print 'wtf mate'
                        print 'wtf mate'
                    #print "SWAPING"
                    s = startHere
                    a = adj
                    startHere = adj
            print "WE ARE STSRTING HRER"
            print startHere
            return startHere
    
    def solveMap(self, rem=None):
        que = []
     #   que.append([0,0])
        if not self.distanceMap:
            self.distanceMap = copy.deepcopy(self.matrix)
            self.distanceMap = self.rewriteMap(rem)
            que.append([0,0])
        else:
            que.append( self.smallestSurronding(rem) )
      #  self.distanceMap = copy.deepcopy(self.matrix)
     #   self.distanceMap = self.rewriteMap(rem)
        count = 0
        while que:
            print '===================',count,'============================'
            self.mlgPrint(self.distanceMap)
            count = count + 1
            allAdjList = []
            pop = que[-1]
            adjacents = self.calcNextDist(que)
            
            allAdjList = allAdjList + adjacents
            que = []
            for adj in allAdjList:
                que.append(adj)
                #self.distanceMap[row2][col2] = self.distanceMap[row][col] + 1
                self.distanceMap[adj[0]][adj[1]] = self.distanceMap[pop[0]][pop[1]] + 1
        
        if (self.distanceMap[-1][-1]):
  #          self.mlgPrint(self.distanceMap)
            #self.mlgPrint(self.bombCandidates)
            return self.distanceMap[-1][-1] + 1
        else:
            return float('inf')

    def checkIfOptimal(self, ans):
        if ans == (self.width + self.height -1):
            print "IS OPTIMAL"
            return True
        return False
        
def solution(matrix):
    graph = Graph(matrix)
    removables = graph.findRemovableWalls()
    allPossibleAnswers = []
    
    # 1st get solution w/o removing walls
    ans = graph.solveMap()
    graph.noBombSolution = graph.distanceMap
    allPossibleAnswers.append(ans)
    if graph.checkIfOptimal(ans):
        return ans
        
    # check solution after removing walls
    print graph.bombCandidates
    for rem in removables:
        print "removing here: ", rem
        ans = graph.solveMap(rem)
        allPossibleAnswers.append(ans)
        if graph.checkIfOptimal(ans):
            return ans
            
    print "v"
    print allPossibleAnswers
    print "^"
    return min(allPossibleAnswers)
       
if __name__ == '__main__':

  maps = []
  maps.append([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0] ] )
  
  maps.append([[0, 0, 0, 0, 0, 0], 
              [1, 1, 1, 1, 1, 0], 
              [0, 0, 0, 0, 0, 0], 
              [0, 1, 1, 1, 1, 1], 
              [0, 1, 1, 1, 1, 1], 
              [0, 0, 0, 0, 0, 0]])
  
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
                  [0, 1,
                   1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],    
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                  [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                  [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                ])
  maps.append([
                [0, 1, 0, 1, 0, 0, 0], 
                [0, 0, 0, 1, 0, 1, 0]
                ])
  
  
  #ans = solution(maps[-2])
  #ans = solution(maps[-1])
  #ans = solution(maps[0])
  ans = solution(maps[1])
  #ans = solution(maps[2])
  #ans = solution(maps[3])
  print '======='
  print ans
  
  #for map in maps:
#    ans = solution(map)
   # print '+++++++++++++++++++++++++++++++++'
    #print ans
    