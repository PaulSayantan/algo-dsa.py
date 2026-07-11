# Multi-Source BFS

## What it is

**Multi-Source BFS** is a plain breadth-first search that is *seeded with more than
one starting cell at once*. Instead of pushing a single source into the queue and
expanding outward in rings, you push **every** source into the queue at distance `0`
before the first expansion step. The frontier then grows simultaneously from all
sources, so when a cell is first dequeued its recorded distance is exactly the
distance to the **nearest** source — no per-source search required.

Mentally, you can picture a *super source* connected to all real sources with
zero-cost edges. A single BFS from that virtual node is equivalent to running BFS
from all sources in parallel.

## When to reach for it

Use Multi-Source BFS when a problem asks for, over an unweighted grid or graph:

- "distance from each cell to the **nearest** cell of some type" (nearest `0`,
  nearest gate, nearest land, nearest water), or
- "how long until **everything** is reached / infected / filled", where many things
  start spreading at the same time (rotting oranges, fire spreading), or
- the shortest number of steps to connect / bridge regions after collapsing a whole
  region into the source set.

The tell-tale sign: you would otherwise run a separate BFS from *many* sources and
take the minimum. Seeding all sources at once collapses those `k` searches into a
single `O(V + E)` pass.

## Core template

```python
from collections import deque

def multi_source_bfs(grid):
    q = deque()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if is_source(val):
                dist[r][c] = 0
                q.append((r, c))        # seed ALL sources first

    while q:
        r, c = q.popleft()
        for nr, nc in neighbors(r, c):
            if in_bounds(nr, nc) and not visited(nr, nc):
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
```

The only structural difference from ordinary BFS is the *initial loop that enqueues
every source*. Correctness relies on the same BFS invariant: cells are dequeued in
non-decreasing order of distance, so the first time a cell is reached is via a
shortest path from the closest source.

## Complexity

For a grid with `R * C = N` cells (and up to `4N` edges):

- **Time:** `O(N)` — every cell is enqueued and dequeued at most once, and each does
  `O(1)` work per (constant number of) neighbors. Seeding `k` sources is `O(N)` too.
- **Space:** `O(N)` for the distance/visited structure and the queue in the worst
  case (all cells are sources).

This is asymptotically the same as single-source BFS but answers the "nearest of
many" question in one pass instead of `k` passes.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Rotting Oranges](problem-01-rotting-oranges/PROBLEM.md) | Simultaneous spread; count BFS levels (minutes) until all fresh cells reached | Easy–Medium |
| 2 | [01 Matrix](problem-02-01-matrix/PROBLEM.md) | Distance from every cell to the nearest `0` | Medium |
| 3 | [Walls and Gates](problem-03-walls-and-gates/PROBLEM.md) | Fill each empty room with distance to nearest gate; walls block | Medium |
| 4 | [Map of Highest Peak](problem-04-map-of-highest-peak/PROBLEM.md) | Assign heights = distance to nearest water cell | Medium |
| 5 | [As Far from Land as Possible](problem-05-as-far-from-land-as-possible/PROBLEM.md) | Maximize the nearest-land distance over all water cells | Medium |
| 6 | [Shortest Bridge](problem-06-shortest-bridge/PROBLEM.md) | Flood-fill one island into the source set, then BFS out to the other | Medium–Hard |
