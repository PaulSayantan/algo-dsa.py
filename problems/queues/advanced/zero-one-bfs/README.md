# 0-1 BFS

When every edge weighs 0 or 1, a double-ended queue replaces Dijkstra's heap: relax a 0-edge by pushing to the FRONT and a 1-edge by pushing to the BACK. The deque stays sorted by distance, giving shortest paths in O(V+E) instead of O(E log V).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [0-1 Weighted Shortest Path](problem-01-zero-one-shortest-path/PROBLEM.md) | Deque frontier | Hard |
