# Grid BFS / Lee Algorithm

The Lee algorithm is BFS on a grid maze: cells are nodes, adjacency is the 4- or 8-neighborhood, and BFS from the start labels each reachable cell with its shortest distance. It finds the shortest path length through a grid in O(rows × cols).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Shortest Path in Binary Matrix](problem-01-shortest-path-binary-matrix/PROBLEM.md) | 8-dir grid BFS | Medium |
| 2 | [Nearest Exit from Entrance in Maze](problem-02-nearest-exit-from-entrance-in-maze/PROBLEM.md) | 4-dir BFS to nearest border | Medium |
| 3 | [Shortest Bridge](problem-03-shortest-bridge/PROBLEM.md) | Flood-fill + multi-source Lee BFS | Medium |
| 4 | [The Maze](problem-04-the-maze/PROBLEM.md) | BFS over rolling stop-cells | Medium |
| 5 | [Minimum Knight Moves](problem-05-minimum-knight-moves/PROBLEM.md) | BFS on infinite board | Medium |
