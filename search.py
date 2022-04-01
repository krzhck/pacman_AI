"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

#######################################################
#            This portion is written for you          #
#######################################################

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A example of heuristic function which estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial. You don't need to edit this function
    """
    return 0

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

#####################################################
# This portion is incomplete.  Time to write code!  #
#####################################################

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    actions = []
    visited = set()

    stack.push(problem.getStartState())
    visited.add(problem.getStartState())

    while not stack.isEmpty():
        top = stack.pop()
        if problem.isGoalState(top):
            return actions

        children = [child for child in problem.expand(top) if child[0] not in visited]
        if len(children) == 0:
            actions.pop()
            continue
            
        stack.push(top)
        (s, a, _) = children[0]
        stack.push(s)
        visited.add(s)
        actions.append(a)
    
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    visited = set()

    queue.push((problem.getStartState(), None, None, None)) # (state, action, cost, parent)
    visited.add(problem.getStartState())

    while not queue.isEmpty():
        top = queue.pop()
        (top_state, action, cost, parent) = top
        if problem.isGoalState(top_state):
            actions = []
            while action:
                actions.append(action)
                action = parent[1]
                parent = parent[3]
            actions.reverse()
            return actions

        for (s, a, c) in problem.expand(top_state):
            if s in visited: continue
            queue.push((s, a, c, top))
            visited.add(s)

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least cost from the root."""
    "*** YOUR CODE HERE ***"
    queue = util.PriorityQueue()
    startState = problem.getStartState()
    visited = set()

    queue.push((startState, None, 0, None, 0), 0) # (state, action, cost, parent, totalcost)
    visited.add(startState)

    while not queue.isEmpty():
        top = queue.pop()
        (top_state, action, cost, parent, total_cost) = top
        if problem.isGoalState(top_state):
            actions = []
            while action:
                actions.append(action)
                (_, action, _, parent, _) = parent
            actions.reverse()
            return actions

        for (s, a, c) in problem.expand(top_state):
            if s in visited: continue
            new_total_cost = total_cost + c
            queue.push((s, a, c, top, new_total_cost), new_total_cost)
            visited.add(s)

    util.raiseNotDefined()

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    queue = util.PriorityQueue()
    startState = problem.getStartState()
    visited = set()

    queue.push((startState, None, 0, None, 0), 0) # (state, action, cost, parent, totalcost)
    visited.add(startState)

    while not queue.isEmpty():
        top = queue.pop()
        (top_state, action, cost, parent, total_cost) = top
        if problem.isGoalState(top_state):
            actions = []
            while action:
                actions.append(action)
                (_, action, _, parent, _) = parent
            actions.reverse()
            return actions

        for (s, a, c) in problem.expand(top_state):
            if s in visited: continue
            new_total_cost = total_cost + c
            f = new_total_cost + heuristic(s, problem)
            queue.push((s, a, c, top, new_total_cost), f)
            visited.add(s)

    util.raiseNotDefined()
