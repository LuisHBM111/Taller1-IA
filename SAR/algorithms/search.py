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
    
    #la pampara estuvo aqui
    pq = utils.PriorityQueue() # esto pa expandir el menor g(n)

    start = problem.getStartState()
    pq.push((start, [], 0), 0)  # esto pa llevar el estado, acciones y costo acumulado, prioridad g (n)

    visited = {}  #menor costo hasta ahora
    visited[start] = 0

    while not pq.isEmpty():
        state, path, cost = pq.pop()

        #verificar si ya tengo una mejor forma d ellegar pa saltarlo 
        if cost > visited.get(state, float("inf")):
            continue

        if problem.isGoalState(state):
            return path

        for succ, action, stepCost in problem.getSuccessors(state):
            newCost = cost + stepCost

            #verificar si lo visite o si tengo una mejor forma de llegar
            if succ not in visited or newCost < visited[succ]:
                visited[succ] = newCost
                pq.push((succ, path + [action], newCost), newCost)

    return []


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    frontier = utils.PriorityQueue()
    start = problem.getStartState()

    frontier.push((start, [], 0), heuristic(start, problem))

    best_cost = {start: 0}

    while not frontier.isEmpty():
        state, actions, g = frontier.pop()

        if g > best_cost.get(state, float("inf")):
            continue

        if problem.isGoalState(state):
            return actions

        for successor, action, stepCost in problem.getSuccessors(state):
            new_g = g + stepCost

            if new_g < best_cost.get(successor, float("inf")):
                best_cost[successor] = new_g
                new_actions = actions + [action]
                f = new_g + heuristic(successor, problem)

                frontier.push((successor, new_actions, new_g), f)

    return []


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
