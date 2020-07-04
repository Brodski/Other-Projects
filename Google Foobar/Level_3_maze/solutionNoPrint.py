import copy

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.width  = len(matrix[0])
        self.distanceMap = []
        self.noBombSolution = None
        self.bombCandidates = []
        
        self.mapNodes = []
        self.openList = []
        self.closedList = []
        
        self.temp_closed = []
        self.temp_map = []
        self.temp_open = []
    
    class Node(object):
        def __init__(self, coords, width=0, height=0):
            self.row = coords[0]
            self.col = coords[1]
            self.isWall = False
            self.__width = width  #not the best code
            self.__height = height
            self.heuristic = (lambda : self.__width - self.col + self.__height - self.row)()
            
            self.g_cost = float('inf')
            self.f_cost = float('inf')
            self.h_cost = float('inf')                
             
    def checkIfOptimal(self, ans):
        if ans == (self.width + self.height -1):
            return True
        return False
        
    def save(self):
        if not self.temp_map:
            self.temp_open = copy.deepcopy(self.openList)
            self.temp_closed = copy.deepcopy(self.closedList)
            self.temp_map = copy.deepcopy(self.mapNodes)
            
    def addWallToBombCandidates(self, node):
        if node not in self.bombCandidates:
            neighbors = self.getNeighbors(node)
            numPaths = 0
            for neighbor in neighbors:
                if not neighbor.isWall:
                    numPaths = numPaths + 1
                if numPaths > 1:
                    self.bombCandidates.append(node)
                    break

    def rewriteMapAsNodes(self):
        self.mapNodes = copy.deepcopy(self.matrix)
        for i,row in enumerate(self.mapNodes):
            for j,ele in enumerate(row):
                if ele == 1: 
                    row[j] = self.Node([i,j], len(self.mapNodes[0]), len(self.mapNodes))
                    row[j].isWall = True
                else: 
                    row[j] = self.Node([i,j], len(self.mapNodes[0]), len(self.mapNodes))
                
        self.mapNodes[0][0].g_cost = 0
        self.mapNodes[0][0].h_cost = self.mapNodes[0][0].heuristic 
        self.mapNodes[0][0].f_cost = self.mapNodes[0][0].heuristic 

    def getNeighbors(self, node):
        adjNodes=[]
        row,col = node.row, node.col
        dx = [-1, 1, 0, 0]
        dy = [0,  0, 1, -1]
        for i in range(4):
            row2 = row + dx[i]
            col2 = col+ dy[i]
            if row2 < 0 or col2 < 0: continue
            if row2 >= self.height or col2 >= self.width: continue
            adjNodes.append( self.mapNodes[row2][col2] )
        return adjNodes
        
    def getNextNode(self):
        self.openList.sort(key=lambda n: (n.f_cost, n.h_cost))
        for node in self.openList:
            if not node.isWall:
                return node
        return []


    # A* algorithm
    def solveMap(self, removedWall=None):
    
        #set up for first run (w/o destroying wall)
        if not self.mapNodes:
            self.rewriteMapAsNodes()
            self.openList.append(self.mapNodes[0][0])
        #set up for first run (w/o destroying wall)
        else:
            self.openList = copy.deepcopy(self.temp_open)
            self.closedList = copy.deepcopy(self.temp_closed )
            self.mapNodes = copy.deepcopy(self.temp_map)
            r,c =removedWall.row, removedWall.col
            self.openList.append(self.mapNodes[r][c])
            self.mapNodes[r][c].isWall = False
            
        while 1:
            if not self.openList:
                self.save()
                return self.mapNodes[-1][-1].f_cost - 1
            current = self.getNextNode()
            self.openList.remove(current)
            self.closedList.append(current)
            
            if current.row == (self.height-1) and current.col == (self.width-1):
                self.save()
                return current.f_cost -1
            neighbors = self.getNeighbors(current)
            for neighbor in neighbors:
                if neighbor.isWall and not removedWall:
                    self.addWallToBombCandidates(neighbor)
                if neighbor in self.closedList:
                    continue
                if current.f_cost < neighbor.f_cost:
                    neighbor.g_cost = current.g_cost + 1
                    neighbor.h_cost = neighbor.heuristic
                    neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
                    if neighbor not in self.openList and not neighbor.isWall:
                        self.openList.append(neighbor)
        
def solution(matrix):
    graph = Graph(matrix)
    allPossibleAnswers = [float('inf')]
    
    # solve 1st w/o destroying a wall
    ans = graph.solveMap()
    graph.noBombSolution = graph.distanceMap
    allPossibleAnswers.append(ans)
    if graph.checkIfOptimal(ans):
        return ans
        
    # solve w/ destroying a wall
    graph.bombCandidates.sort(key=lambda n: (n.f_cost, n.h_cost))
    for wall in graph.bombCandidates:
        if wall.f_cost < min(allPossibleAnswers):
            ans = graph.solveMap(wall)
            allPossibleAnswers.append(ans)
        if graph.checkIfOptimal(ans):
            return ans

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
  
  ans ='lol'
  ilike = [maps[0], maps[1], maps[-1], maps[2]]
  #ans = solution(maps[-2])
  #ans = solution(maps[-1])
  #ans = solution(maps[1])
  #ans = solution(maps[1])
  #ans = solution(maps[2])
  #ans = solution(maps[3])
  print '======='
  print ans
  
  for map in ilike:
    ans = solution(map)
    print '+++++++++++++++++++++++++++++++++'
    print ans
      