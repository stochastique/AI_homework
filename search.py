"""
Здесь надо реализовать dfs, bfs, ucs, A*. Первые два у меня получились, я их выложил. Подсмотрел немного,
как делают другие, заменил bfs т.к. предыдущий оценку не проходил, хотя и работал. Добавил ucs, a*.
"""



"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""


import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    route = [problem.getStartState()]    # "movement" vector     [ (),...,() ]
    result = []   # result vector with solution
    succs = {}    # copy of Successors
    
    while not problem.isGoalState(route[0]):
		l = len(route)
		if route[0] not in succs.keys():
			succs.update({route[0]:problem.getSuccessors(route[0])})
		for dir in succs[route[0]]:   
			if dir[0] not in succs.keys():
				route.insert(0,dir[0])
				result.append(dir[1])
			if l != len(route): break
		if l == len(route):
			route.remove(route[0])
			del result[len(result)-1]
    return result

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    fringe = util.Queue()
    visitedNodes = []
    fringe.push([problem.getStartState(),[]])

    while not fringe.isEmpty(): 
        currNode = fringe.pop()
        if problem.isGoalState(currNode[0]):
            return currNode[1]
        if currNode[0] not in visitedNodes: 
            visitedNodes.append(currNode[0])   
            for State, Way, Price in problem.getSuccessors(currNode[0]):
                path = currNode[1][:]
                path.append(Way)
                fringe.push([State, path])

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    
    fringe = util.PriorityQueue()
    visitedNodes = []
    fringe.push([problem.getStartState(),[],0],0)
    while not fringe.isEmpty():
        currNode = fringe.pop()
        if problem.isGoalState(currNode[0]):
            return currNode[1]
        if currNode[0] not in visitedNodes: 
            visitedNodes.append(currNode[0])   
            for State, Way, Price in problem.getSuccessors(currNode[0]):
                path = currNode[1][:] 
                totalCost = currNode[2] + Price
                print currNode[2]
                path.append(Way)
                fringe.push([State, path, totalCost],totalCost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    
    
    fringe = util.PriorityQueue()
    visitedNodes = []
    fringe.push([problem.getStartState(),[],0],0)
    while not fringe.isEmpty():
        currNode = fringe.pop()
        if problem.isGoalState(currNode[0]):
            return currNode[1]
        if currNode[0] not in visitedNodes: 
            visitedNodes.append(currNode[0])   
            for State, Way, Price in problem.getSuccessors(currNode[0]):
                path = currNode[1][:] 
                totalCost = currNode[2] + Price
                path.append(Way)
                fringe.push([State, path, totalCost],totalCost + heuristic(State, problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
