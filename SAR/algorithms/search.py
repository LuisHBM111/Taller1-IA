from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    margen = utils.Stack()
    start = problem.getStartState()
    margen.push((start, []))
    visitado = set()

    while not margen.isEmpty():
        estado, camino = margen.pop()

        if problem.isGoalState(estado):
            return camino

        if estado in visitado:
            continue
        visitado.add(estado)

        for sucesor, accion, costo_paso in problem.getSuccessors(estado):
            if sucesor not in visitado:
                margen.push((sucesor, camino + [accion]))
    
    return []


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    margen = utils.Queue()
    start = problem.getStartState()
    margen.push((start, []))
    visitado = set([start])

    while not margen.isEmpty():
        estado, camino = margen.pop()

        if problem.isGoalState(estado):
            return camino

        for sucesor, accion, costo_paso in problem.getSuccessors(estado):
            if sucesor not in visitado:
                visitado.add(sucesor)
                margen.push((sucesor, camino + [accion]))

    return []

def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    # TODO: Add your code here
    utils.raiseNotDefined()


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
