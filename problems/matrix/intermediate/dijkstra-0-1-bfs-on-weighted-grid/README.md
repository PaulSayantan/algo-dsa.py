# Dijkstra / 0-1 BFS on a Weighted Grid

When the cells or the moves of a grid carry a **cost** (not every step is worth
1), plain BFS no longer finds the cheapest route. You need a shortest-path
algorithm that respects those weights:

- **Dijkstra's algorithm** — a min-priority-queue (min-heap) BFS that always
  expands the cheapest-so-far cell. Works for any **non-negative** edge/cell
  weights.
- **0-1 BFS** — a specialization of Dijkstra for the case where every move
  costs only **0 or 1**. Instead of a heap it uses a **double-ended queue**:
  a 0-cost move is pushed to the **front**, a 1-cost move to the **back**. This
  keeps the deque sorted by distance automatically and runs in linear time.

## Core Idea

Model each grid cell as a graph node and each legal move as a weighted edge.
Maintain `dist[cell]` = best known cost to reach that cell (start at `0`, all
others `∞`). Repeatedly pull the cell with the smallest tentative distance,
**settle** it (its distance is now final), and **relax** its neighbours:
`dist[nb] = min(dist[nb], dist[cur] + weight(cur → nb))`.

Because Dijkstra always settles the globally cheapest frontier cell first, the
first time a cell is popped its distance is optimal — provided all weights are
non-negative (a later path can only add more non-negative cost).

The "weight" is problem-specific and is what turns a BFS question into a
Dijkstra question:

| Objective | What you minimise | Relaxation |
|-----------|-------------------|------------|
| Sum of cell costs | total cost along the path | `dist[nb] = dist[cur] + cost[nb]` |
| Obstacles removed (0/1) | count of blocked cells entered | `dist[nb] = dist[cur] + grid[nb]` (0-1 BFS) |
| Minimum effort / bottleneck | the **maximum** edge along the path | `dist[nb] = max(dist[cur], w(cur,nb))` |
| Sign changes (0/1) | direction changes | `+0` if you follow the arrow, `+1` otherwise (0-1 BFS) |

## When to Reach for It

- Moves/cells have **different, non-negative** costs -> Dijkstra (min-heap).
- Every move costs exactly **0 or 1** -> 0-1 BFS (deque) — same answer, faster
  and simpler than a heap.
- You are minimising the **worst** step on a path (a minimax / bottleneck path)
  rather than the sum -> Dijkstra with a `max` relaxation.

If every move costs the same fixed amount, you do **not** need this — plain BFS
(the Lee algorithm) already gives shortest paths. If some weights are
**negative**, Dijkstra is invalid; use Bellman-Ford / SPFA instead.

## Complexity

| Variant | Time | Space |
|---------|------|-------|
| Dijkstra with binary heap | **O(R·C · log(R·C))** — each cell is pushed/popped from the heap, `E = O(R·C)` edges relaxed | O(R·C) |
| 0-1 BFS with deque | **O(R·C)** — each cell enters the deque O(1) amortised times | O(R·C) |

`R·C` is the number of grid cells; the constant hidden in the edge count is the
fixed neighbour fan-out (4 or 8).

## Problems

| # | Problem | Technique Focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Minimum Cost Path](problem-01-minimum-cost-path/PROBLEM.md) | Dijkstra summing cell costs, 4-directional | Medium |
| 2 | [Minimum Obstacle Removal to Reach Corner](problem-02-minimum-obstacle-removal-to-reach-corner/PROBLEM.md) | 0-1 BFS (0 = empty, 1 = obstacle) | Medium |
| 3 | [Path With Minimum Effort](problem-03-path-with-minimum-effort/PROBLEM.md) | Dijkstra minimising the maximum edge (bottleneck path) | Medium |
| 4 | [Swim in Rising Water](problem-04-swim-in-rising-water/PROBLEM.md) | Dijkstra minimising the maximum cell (minimax path) | Hard |
| 5 | [Minimum Cost to Make at Least One Valid Path in a Grid](problem-05-minimum-cost-valid-path-grid/PROBLEM.md) | 0-1 BFS over directional signs | Hard |
