# Edmonds–Karp (Max-Flow)

Edmonds–Karp implements Ford–Fulkerson using BFS to find the shortest augmenting path each round, then pushes flow equal to the path's bottleneck. Using shortest augmenting paths bounds it to O(V·E²), and the max-flow value is unique regardless of path choices.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Maximum Flow (Edmonds–Karp)](problem-01-max-flow-edmonds-karp/PROBLEM.md) | BFS augmenting paths | Hard |
