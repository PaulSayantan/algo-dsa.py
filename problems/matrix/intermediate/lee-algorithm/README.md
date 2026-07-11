# Lee Algorithm (BFS Shortest Path on a Grid)

The **Lee Algorithm** is the classic breadth-first search (BFS) technique for
finding the **shortest path between two points in a grid or maze** where every
move has the same cost (an *unweighted* graph). It was originally described by
C. Y. Lee in 1961 for routing wires on circuit boards, and today it is the
go-to pattern for maze/grid shortest-path questions.

## Core Idea

Treat each cell of the grid as a graph node and each legal move (usually the 4
orthogonal neighbours, sometimes 8 including diagonals) as an edge of weight 1.
Because every edge costs exactly 1, BFS expands cells **in order of increasing
distance from the source**. The first time BFS reaches the target, it has found
a shortest path — no other search can do better.

The algorithm works in "waves" (also called levels or ripples):

1. Put the source cell(s) in a FIFO queue and mark it visited (distance 0).
2. Repeatedly pop a cell, and for each unvisited, walkable neighbour set its
   distance to `current + 1`, mark it visited, and push it.
3. Stop when you dequeue the target (or when the queue empties).

Marking a cell visited **at enqueue time** (not dequeue time) is the key
invariant that keeps the algorithm O(R×C): every cell enters the queue at most
once.

## When to Reach for It

- Shortest path / minimum number of moves in a maze or grid.
- "Nearest source" / multi-source problems (flood fill from many origins at
  once — seed the queue with *all* sources).
- Any unweighted-grid distance question.

If edges have **different** weights, use Dijkstra instead. If they are 0/1
weights, use 0-1 BFS (a deque). If you only need *reachability* (not the
shortest distance), plain DFS or BFS both work.

## Complexity

| Metric | Cost |
|--------|------|
| Time   | **O(R × C)** — each of the R×C cells is enqueued and processed once, and each does O(1) work per fixed set of neighbours. |
| Space  | **O(R × C)** — for the visited/distance grid and the queue in the worst case. |

For the "extra state" variant (Problem 5) the state space grows by the number
of state values (e.g. obstacles remaining), giving O(R × C × K).

## Problems

| # | Problem | Technique Focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Nearest Exit from Entrance in Maze](problem-01-nearest-exit-maze/PROBLEM.md) | Single-source BFS to any border exit | Medium |
| 2 | [Shortest Path in Binary Matrix](problem-02-shortest-path-binary-matrix/PROBLEM.md) | 8-directional BFS corner-to-corner | Medium |
| 3 | [01 Matrix](problem-03-01-matrix/PROBLEM.md) | Multi-source BFS (distance to nearest 0) | Medium |
| 4 | [Rotting Oranges](problem-04-rotting-oranges/PROBLEM.md) | Multi-source level-by-level BFS (time) | Medium |
| 5 | [Shortest Path in a Grid with Obstacles Elimination](problem-05-shortest-path-grid-obstacles-elimination/PROBLEM.md) | BFS over an augmented `(row, col, k)` state | Hard |
