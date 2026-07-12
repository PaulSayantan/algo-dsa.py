# Dijkstra (Priority Queue)

Dijkstra's algorithm computes single-source shortest paths in a graph with non-negative weights by always expanding the closest unfinalized node — pulled from a min-heap (priority queue). Lazy deletion (skipping stale heap entries) keeps it at O((V+E) log V).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Network Delay Time](problem-01-network-delay-time/PROBLEM.md) | Min-heap relaxation | Medium |
| 2 | [Dijkstra Distance Array](problem-02-dijkstra-distances/PROBLEM.md) | Distance array via heap | Medium |
