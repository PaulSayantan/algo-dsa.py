# Articulation Points & Bridges

In an undirected graph, a DFS with discovery times and low-link values finds cut vertices (articulation points) and cut edges (bridges): an edge (u,v) is a bridge when low[v] > disc[u], and u is an articulation point when a child cannot reach an ancestor. Both are single-DFS O(V+E) routines.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Critical Connections in a Network (Bridges)](problem-01-critical-connections/PROBLEM.md) | Bridge low-link | Hard |
| 2 | [Articulation Points](problem-02-articulation-points/PROBLEM.md) | Cut-vertex low-link | Hard |
