# Taller1-IA

Este proyecto implementa algoritmos de búsqueda no informada e informada para guiar un agente en un entorno tipo grid y rescatar uno o múltiples sobrevivientes minimizando el costo del recorrido.

Algoritmos

DFS

BFS

Uniform Cost Search (UCS)

A* Search

Heurísticas

Null

Manhattan

Euclidiana

Survivor Heuristic (MultiSurvivor): usa distancia Manhattan al sobreviviente más lejano y el diámetro entre sobrevivientes (admisible y preferiblemente consistente).

Problemas

SimpleSurvivorProblem

MultiSurvivorProblem

Evaluación

Se compararon costo total, nodos expandidos y tiempo de ejecución. UCS garantiza optimalidad, mientras que A* mejora el rendimiento al usar heurísticas.
