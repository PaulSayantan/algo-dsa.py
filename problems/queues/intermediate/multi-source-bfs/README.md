# Multi-Source BFS

When several sources spread simultaneously, seed the BFS queue with *all* of them at distance 0 and expand together. One pass computes, for every cell, the distance to the nearest source — perfect for 'rotting oranges' or 'distance to nearest 0'.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Rotting Oranges](problem-01-rotting-oranges/PROBLEM.md) | Simultaneous waves | Medium |
| 2 | [01 Matrix](problem-02-01-matrix/PROBLEM.md) | Nearest-zero distance | Medium |
| 3 | [Walls and Gates](problem-03-walls-and-gates/PROBLEM.md) | Distance to nearest gate | Medium |
| 4 | [As Far from Land as Possible](problem-04-as-far-from-land-as-possible/PROBLEM.md) | Max nearest-land distance | Medium |
| 5 | [Shortest Bridge](problem-05-shortest-bridge/PROBLEM.md) | Island flood-fill + wave expansion | Medium |
