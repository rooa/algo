"""
This is a way to solve shortest path problem.
I tried to implement A* algorithm.
The maze is provided below.

 **************************
 *S* *                    *
 * * *  *  *************  *
 * *   *    ************  *
 *    *                   *
 ************** ***********
 *                        *
 ** ***********************
 *      *             *G  *
 *  *  **  *********** *  *
 *    *        ******* *  *
 *       *                *
 **************************

Then, the maze is converted into a number-based form as follows.

0: space
1: wall
2: GOAL
"""
maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
        [1,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,1],
        [1,0,0,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

WIDTH = len(maze[0])
HEIGHT = len(maze)
INF = 10000000

class Node:    
    def __init__(self,x,y,f=INF):
        self.x = x
        self.y = y
        self.f = f
        self.g = 0
        self.h = 0
        self.parent = None

    def updateCost(self):
        self.f = self.g + self.h

    def isGoal(self):
        return self.h == 0

    def __eq__(self,other):
        return (self.x == other.x and self.y == other.y)

def pick(_set):
    """ Pick a node from _set that has lowest F value.(latest first)  """
    node = Node(0,0)
    idx = 0
    for i,n in enumerate(reversed(_set)):
        if n.f < node.f:
            node = n
            idx = len(_set) - 1 - i     # index of _set before "reversed"
    return node,idx                     # return the index of picked node in op 

def adjacent(node):
    """ look around 4 directions, check and add them to the "cand"  """
    cand = []
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    x,y = node.x,node.y
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[nx][ny] != 1:
            n = Node(nx,ny)
            cand.append(n)
    return cand

def h(n,g):
    """ heuristics. This time NOT the euclidean distance  """
    return abs(g.x - n.x) + abs(g.y - n.y)


if __name__ == "__main__":
    op = []
    cl = []

    # Goal node
    goal = Node(8,22)
    goal.h = 0

    # Starting node
    start = Node(1,1)
    start.h = h(start,goal)
    start.updateCost()
    op.append(start)

    ans = [["-" for i in range(WIDTH)] for j in range(HEIGHT)]

    while len(op) > 0:
        # pick up from op(Priority Queue) 
        node,idx = pick(op)
        op.pop(idx)
        # add node to the visited nodes
        cl.append(node)
        # generate a list of next nodes
        adj = adjacent(node)
        for i in range(len(adj)):
            # if you have already visited
            if adj[i] in cl:
                continue
            # calculate F value of adj[i]
            adj[i].g = node.g + 1
            adj[i].h = h(adj[i],goal)
            adj[i].updateCost()
            # check if adj[i] is in op. and whether it is the shortest path
            for n in op:
                if adj[i] == n and n.f > adj[i].f:
                    # if so, update n in op with new F value and parent
                    n.parent = node
                    n.f = adj[i].f
                    break
            # add adj[i] to op because it is not visited
            if adj[i] not in op:
                adj[i].parent = node
                op.append(adj[i])
        # print path by tracking through ".parent", if reached to the goal
        if node.isGoal():
            print "YEAH!"
            t = node
            while t.parent != None:
                ans[t.x][t.y] = "o"
                t = t.parent
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    print ans[i][j],
                print 
            break 
