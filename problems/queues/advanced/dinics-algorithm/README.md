# Dinic's Algorithm

Dinic's algorithm speeds up max-flow by working in phases: a BFS builds a level graph (shortest-distance layers from the source), then repeated DFS sends *blocking flow* along level-respecting paths. It runs in O(V²·E) — much faster than Edmonds–Karp on dense graphs.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Maximum Flow (Dinic's)](problem-01-max-flow-dinics/PROBLEM.md) | Level graph + blocking flow | Hard |
