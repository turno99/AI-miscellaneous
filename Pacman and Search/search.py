# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# Implementation of DFS for pacman, returns path to goal.
# The frontier is a LIFO Stack (imported from util) containing
# nodes and respective list of actions to reach them from the starting
# state. We begin from the start state, and on every iteration, we check 
# if the current node has already been explored. If not, we check if the 
# current state is the goal state. If yes, we return the actions. Else, we 
# update the list of actions by adding the current action, and push it to 
# the stack to continue further searching.

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    frontier = util.Stack()
    explored = []
    frontier.push((startState, []))

    while not frontier.isEmpty():
        node, actions = frontier.pop()
        if node not in explored:
            explored.append(node)

            if problem.isGoalState(node):
                return actions

            for child, action, cost in problem.getSuccessors(node):
                newAction = actions + [action]
                frontier.push((child, newAction))

# Implementation of BFS for pacman, returns path to goal.
# The frontier is a FIFO Queue (imported from util) containing
# nodes and respective list of actions to reach them from the starting
# state. We begin from the start state, and on every iteration, we 
# check if the current node has already been explored. If not, we 
# check if the current state is the goal state. If yes, we return the
# actions. Else, we update the list of actions by adding the current 
# action, and push it to the queue to continue further searching.

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    frontier = util.Queue()
    explored = []
    frontier.push((startState, []))

    while not frontier.isEmpty():
        node, actions = frontier.pop()
        if node not in explored:
            explored.append(node)

            if problem.isGoalState(node):
                return actions

            for child, action, cost in problem.getSuccessors(node):
                newAction = actions + [action]
                frontier.push((child, newAction))

    util.raiseNotDefined()

# Implementation of UCS for pacman, returns path to goal.
# The frontier is a Priority Queue (imported from util) containing
# nodes, respective list of actions to reach them from the starting
# state and their priority, (set equal to the cost) which is used to order
# the queue. We begin from the start state, and on every iteration, we 
# check if the current node has already been explored. If not, we check if 
# the current state is the goal state. If yes, we return the actions. Else, we 
# update the list of actions by adding the current action, and push it to the
# priority queue to continue further searching. The main difference with
# BFS here is that BFS explores the shallowest node first, whereas
# UCS chooses the node with the least path cost first instead.

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    explored = []

    frontier = util.PriorityQueue()
    frontier.push((startState, [], 0), 0)

    while not frontier.isEmpty():

        node, actions, oldCost = frontier.pop()
        if node not in explored:
            explored.append(node)

            if problem.isGoalState(node):
                return actions

            for child, action, cost in problem.getSuccessors(node):
                newAction = actions + [action]
                priority = oldCost + cost
                frontier.push((child, newAction, priority),priority)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# Implementation of A* search for pacman, returns path to goal.
# The frontier is a Priority Queue (imported from util) containing
# nodes, respective list of actions to reach them from the starting
# state and their priority, (set equal to a heuristic function), which is 
# used to order the queue. We begin from the start state, and on every 
# iteration, we check if the current node has already been explored. If not, 
# we check if  the current state is the goal state. If yes, we return the actions.
# Else, we update the list of actions by adding the current action, and push it
# to the priority queue to continue further searching. The main difference with
# UCS lies in choosing the goal to minimize: UCS chooses the least cost nodes
# first, but A* search minimizes the sum of the cost function and a chosen
# heuristic function.

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    explored = []

    frontier = util.PriorityQueue()
    frontier.push((startState, [], 0), 0)

    while not frontier.isEmpty():

        node, actions, oldCost = frontier.pop()

        if node not in explored:
            explored.append(node)

            if problem.isGoalState(node):
                return actions

            for child, action, cost in problem.getSuccessors(node):
                newAction = actions + [action]
                newCost = oldCost + cost
                heuristicCost = newCost + heuristic(child,problem)
                frontier.push((child, newAction, newCost),heuristicCost)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch