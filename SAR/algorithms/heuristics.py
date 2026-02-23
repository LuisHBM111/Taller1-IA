from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.
    """
    x, y = state
    gx, gy = problem.goal
    return abs(x - gx) + abs(y - gy)


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    x, y = state
    gx, gy = problem.goal
    return ((x - gx) ** 2 + (y - gy) ** 2) ** 0.5


def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    position, survivors_grid = state
    survivors = survivors_grid.asList()

    if not survivors:
        return 0

    def manhatan(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    far_from_pos = max(manhatan(position, s) for s in survivors)

    diam = 0
    for i in range(len(survivors)):
        for j in range(i + 1, len(survivors)):
            d = manhatan(survivors[i], survivors[j])
            if d > diam:
                diam = d

    return max(far_from_pos, diam)
