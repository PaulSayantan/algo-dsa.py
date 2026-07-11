# Grid DFS / BFS

Treat each cell of a 2D grid as a **graph node**, with edges to its orthogonal
(4-directional: up/down/left/right) or diagonal-inclusive (8-directional)
neighbors. Once you view the grid this way, an enormous class of matrix problems
reduces to standard graph traversal: **Depth-First Search (DFS)** or
**Breadth-First Search (BFS)**.

## When to reach for it

Use grid DFS/BFS whenever the problem involves *connectivity, reachability, or
region propagation* over a matrix:

- Counting or measuring connected regions (islands, clusters, provinces).
- Flooding / filling a connected region with a new value.
- Shortest number of steps between cells (**BFS**, because every move has unit
  cost).
- Propagation from many sources simultaneously (**multi-source BFS**).
- Reachability from a set of border cells (often solved with a **reverse**
  traversal from the border inward).

Rule of thumb:
- **DFS** (recursion or explicit stack) is simplest for "explore/mark an entire
  region" and "does a path exist" questions.
- **BFS** (queue) is the tool for **shortest path / minimum number of steps** on
  an unweighted grid, and for **level-by-level** time propagation.

## The core mechanics

1. Define the movement offsets, e.g. `DIRS = [(-1,0),(1,0),(0,-1),(0,1)]` for 4
   directions (add the 4 diagonals for 8).
2. Track visited cells with a `visited` set, or mutate the grid in place (e.g.
   sink land to water) when allowed.
3. For each neighbor, bounds-check `0 <= r < rows and 0 <= c < cols`, then check
   the visited/validity condition before recursing or enqueuing.

## Complexity

For a grid with `R` rows and `C` columns (`N = R * C` cells):

- **Time:** `O(R * C)` — each cell is enqueued/visited at most once, and it has a
  constant number of neighbors (4 or 8).
- **Space:** `O(R * C)` — for the visited structure plus the recursion stack
  (DFS) or the queue (BFS) in the worst case.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Flood Fill](problem-01-flood-fill/PROBLEM.md) | Basic connected-region recolor (DFS or BFS) | Easy |
| 2 | [Number of Islands](problem-02-number-of-islands/PROBLEM.md) | Counting connected components | Medium |
| 3 | [Max Area of Island](problem-03-max-area-of-island/PROBLEM.md) | DFS that returns a region size | Medium |
| 4 | [Rotting Oranges](problem-04-rotting-oranges/PROBLEM.md) | Multi-source BFS / time layers | Medium |
| 5 | [Shortest Path in Binary Matrix](problem-05-shortest-path-in-binary-matrix/PROBLEM.md) | 8-directional shortest-path BFS | Medium |
| 6 | [Pacific Atlantic Water Flow](problem-06-pacific-atlantic-water-flow/PROBLEM.md) | Reverse multi-source traversal from borders | Medium/Hard |
