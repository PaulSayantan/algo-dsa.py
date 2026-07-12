# 0-1 BFS with a Deque

When every edge weight is either 0 or 1, you don't need Dijkstra's heap — a **deque** gives shortest paths in O(V + E). Use the deque as the frontier: relaxing a weight-0 edge pushes the neighbor to the **front** (same distance level), while a weight-1 edge pushes it to the **back** (next level). This keeps the deque sorted by distance with at most two distinct values, so the first time a node is popped its distance is final — exactly Dijkstra's guarantee, but with O(1) deque operations instead of O(log V) heap pushes.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Shortest Path with 0/1 Edge Weights](problem-01-zero-one-bfs-shortest-path/PROBLEM.md) | 0-1 BFS on a graph | Medium |
| 2 | [Minimum Cost to Make at Least One Valid Path in a Grid](problem-02-min-cost-valid-path-grid/PROBLEM.md) | 0-1 BFS on a grid | Hard |
| 3 | [Minimum Obstacle Removal to Reach Corner](problem-03-minimum-obstacle-removal/PROBLEM.md) | 0-1 BFS with cell-weight edges | Medium |
| 4 | [Minimum Edge Reversals to Reach a Node](problem-04-min-edge-reversals-reach-node/PROBLEM.md) | 0-1 BFS on a directed graph | Medium |
| 5 | [Minimum Turns to Cross a Maze](problem-05-minimum-turns-in-maze/PROBLEM.md) | 0-1 BFS over direction-augmented states | Medium |
