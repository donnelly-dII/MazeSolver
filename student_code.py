
#Class Node stores the information of a node in the tree
        #X:             current x position
        #Y:             current y position
        #parent:        parent node
        #generated:     the move (left,right,up,down) that generated the node
class Node: 
        def __init__(self,p, x, y, g):
                self.X = x              #x position
                self.Y = y              #Y position
                self.parent = p         #Parent Node
                self.generated = g      #action generation (used to prevent cycles)

#Class Queue represents a queue data structure
class Queue:
        def __init__(self):
                self.array = []
                self.size = 0

        def put(self,node):
                self.array.append(node)
                self.size = self.size + 1
        def get(self):
                if(self.size == 0):
                        return None
                else:
                        self.size = self.size - 1
                        return self.array.pop(0)
        def empty(self):
                if(self.size == 0):
                        return True
                else:
                        return False
        

#Class Stack represents a stack data structure 
class Stack:
        def __init__(self):
                self.array = []
                self.size = 0
        def put(self, node):
                self.array.insert(0,node)
                self.size = self.size + 1
        def get(self):
                if(self.size == 0):
                        return None
                else:
                        self.size = self.size - 1
                        return self.array.pop(0)
        def empty(self):
                if(self.size == 0):
                        return True
                else:
                        return False


#NodeTraceback node,map -> null
        #NodeTraceback takes the final node of the tree (if a solution is found)
        #and it traces backwards through the parents puttng a 5 at each position on the map
def NodeTraceback(node, map):
        currNode = node
        while currNode != None:
                map[currNode.Y][currNode.X] = 5
                currNode = currNode.parent

#FindStartingPoint map -> int,int
        #FindStartingPoint takes a map and returns the x and y coordinates where the maze begins
def FindStartingPoint(map, dim):
        check = True
        ii = 0
        xStart = 0
        yStart = 0
        while(ii < dim.MAP_WIDTH and check):
                jj = 0
                while(jj < dim.MAP_HEIGHT and check):
                        if(map[jj][ii] == 2):
                                check = False
                                xStart = ii
                                yStart = jj
                        jj = jj + 1
                ii = ii + 1
        return xStart, yStart

def ShiftRightCheck(node, dim,map):
    if node.X + 1 < dim.MAP_WIDTH and node.generated != 3: 
        if map[node.Y][node.X + 1] == 0 or map[node.Y][node.X+1] == 3:
            return True
    return False

def ShiftLeftCheck(node, dim,map):
    if node.X - 1 >= 0 and node.generated != 1: 
        if map[node.Y][node.X - 1] == 0 or map[node.Y][node.X-1] == 3:
            return True
    return False

def ShiftUpCheck(node, dim,map):
    if node.Y + 1 < dim.MAP_HEIGHT and node.generated != 4: 
        if map[node.Y+1][node.X] == 0 or map[node.Y+1][node.X] == 3:
            return True
    return False

def ShiftDownCheck(node, dim,map):
    if node.Y - 1 >= 0 and node.generated != 2: 
        if map[node.Y-1][node.X] == 0 or map[node.Y-1][node.X] == 3:
            return True
    return False

def df_search(map, dim):
        found = False;
        #Find the starting point
        xStart, yStart = FindStartingPoint(map,dim)
        #Build LIFO stack, and begin iterations
        stack = Stack()
        firstNode = Node(None, xStart, yStart, 0)
        stack.put(firstNode)
        while not stack.empty():
                NodeHold = stack.get()
                xHold = NodeHold.X
                yHold = NodeHold.Y
                if map[yHold][xHold] == 3: 
                    FinalNode = Node(NodeHold.parent, xHold, yHold, NodeHold.generated)
                    found = True
                    break
                map[yHold][xHold] = 4
                #Down One
                if ShiftDownCheck(NodeHold, dim, map):
                    stack.put(Node(NodeHold, xHold, yHold-1,4))
                #Shift Left
                if ShiftLeftCheck(NodeHold,dim, map):                               
                    stack.put(Node(NodeHold, xHold - 1, yHold,3))
                #Up One
                if ShiftUpCheck(NodeHold,dim,map):
                    stack.put(Node(NodeHold, xHold, yHold + 1,2))
                #Shift right
                if ShiftRightCheck(NodeHold, dim,map):
                    stack.put(Node(NodeHold, xHold + 1, yHold,1))
        #BackTrack to Label the Paths
        if found: 
                NodeTraceback(FinalNode,map)

        return found

def bf_search(map, dim):
        found = False;

        #Find the starting point
        xStart, yStart = FindStartingPoint(map,dim)
        #Set map on start
        map[yStart][xStart] = 4
        #Build FIFO queue, and begin iterations
        q = Queue()
        firstNode = Node(None, xStart, yStart, 0)
        q.put(firstNode)
        while not q.empty() and not found:
                NodeHold = q.get()
                xHold = NodeHold.X
                yHold = NodeHold.Y
                if map[yHold][xHold] == 3: 
                    FinalNode = Node(NodeHold.parent, xHold, yHold, NodeHold.generated)
                    map[yHold][xHold] = 4
                    found = True
                    break
                map[yHold][xHold] = 4
                #Shift right
                if ShiftRightCheck(NodeHold, dim, map):
                    q.put(Node(NodeHold, xHold + 1, yHold,1))
                #Up One
                if ShiftUpCheck(NodeHold,dim,map):
                    q.put(Node(NodeHold, xHold, yHold + 1,2))
                #Shift Left
                if ShiftLeftCheck(NodeHold,dim,map):
                    q.put(Node(NodeHold, xHold-1, yHold,3))
                #Down One
                if ShiftDownCheck(NodeHold, dim, map):
                    q.put(Node(NodeHold, xHold, yHold-1,4))
        #BackTrack to Label the Paths
        if found: 
                NodeTraceback(FinalNode,map)

        return found




