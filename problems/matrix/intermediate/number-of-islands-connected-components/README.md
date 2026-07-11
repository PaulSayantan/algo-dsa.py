# Number of Islands / Connected Components

## What it is

Many grid and graph problems boil down to a single question: **how many
connected regions are there, and how big are they?** A "region" (island,
province, component) is a maximal set of cells/nodes that are reachable from
one another by moving along allowed edges (usually the 4 orthogonal neighbours
in a grid, sometimes 8, or explicit edges in an adjacency matrix).

Three interchangeable tools solve this family:

- **DFS** — recursively (or with an explicit stack) walk out from a seed cell,
  marking everything reachable as visited. Each fresh, unvisited seed you find
  starts a new component.
- **BFS** — the same traversal with a queue instead of recursion. Preferred
  when the grid is huge and recursion could overflow the call stack.
- **Union-Find (Disjoint Set Union)** — union every pair of adjacent
  "land" cells, then count distinct roots. Shines when edges arrive
  incrementally (online / streaming) or when the input is an adjacency matrix.

## When to reach for it

Reach for connected-components counting whenever you see phrases like
*"number of islands"*, *"connected groups"*, *"provinces"*, *"regions"*,
*"friend circles"*, *"largest blob"*, or any grid where you flood outward from
a cell until you hit a boundary or a wall.

## Typical complexity

For a grid with `R` rows and `C` columns (`V = R*C` cells, up to `~4V` edges):

- **DFS / BFS:** `O(V + E) = O(R*C)` time, `O(R*C)` worst-case space (recursion
  stack / queue, or a visited set).
- **Union-Find:** `O(V * α(V))` time with path compression + union by rank
  (`α` = inverse Ackermann, effectively constant), `O(V)` space.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Flood Fill](problem-01-flood-fill/PROBLEM.md) | Warm-up: single-region DFS/BFS repaint | Easy |
| 2 | [Number of Islands](problem-02-number-of-islands/PROBLEM.md) | Count components on a binary grid | Medium |
| 3 | [Max Area of Island](problem-03-max-area-of-island/PROBLEM.md) | Component counting that returns region sizes | Medium |
| 4 | [Number of Provinces](problem-04-number-of-provinces/PROBLEM.md) | Components on an adjacency matrix (Union-Find) | Medium |
| 5 | [Surrounded Regions](problem-05-surrounded-regions/PROBLEM.md) | Border-anchored flood fill to protect regions | Medium |
| 6 | [Making A Large Island](problem-06-making-a-large-island/PROBLEM.md) | Label components, then merge across one flip | Hard |
