# Tarjan's Strongly Connected Components

Tarjan's algorithm finds all strongly connected components in one DFS. Each vertex gets a discovery index and a low-link (the smallest index reachable via the DFS subtree + one back edge); a vertex on an explicit stack whose low-link equals its own index roots an SCC. Linear O(V+E).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Strongly Connected Components](problem-01-count-and-list-sccs/PROBLEM.md) | Low-link + on-stack | Hard |
