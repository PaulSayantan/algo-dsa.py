# Shortest Path in Binary Matrix — Solution

## Brute Force

The naive approach is a **DFS that explores every clear path** and keeps the minimum
length. From each cell you branch into up to 8 neighbors, backtracking when you hit a
`1`, a visited cell, or a dead end.

- **Time:** exponential — `O(8^(n^2))` in the worst case, since without a global
  visited/distance bound the same regions are re-explored along countless paths.
- **Space:** `O(n^2)` recursion depth for the current path.

This is hopelessly slow and also error-prone (you must undo the visited marks
correctly). Since every step costs exactly `1`, a breadth-first flavored search is the
right tool.

## Optimal Approach (A\* Search)

Every move adds exactly one cell, so this is an unweighted shortest-path problem —
plain BFS already solves it in `O(n^2)`. A\* keeps that same worst-case guarantee but
**aims the search at the single goal corner**, so on large open grids it expands far
fewer cells than BFS, which fans out in all directions.

Model each cell `(r, c)` as a state. Let `g(r, c)` be the number of cells used to reach
it (the start counts as `1`). The remaining path must make at least `max(|n-1-r|,
|n-1-c|)` more diagonal-capable steps to reach `(n-1, n-1)`, so define the heuristic

```
h(r, c) = max(n - 1 - r, n - 1 - c)     # Chebyshev distance to the goal
```

**Why the heuristic is valid:** with 8-directional moves, one step changes both the
row and the column by at most `1`, so you need at least `max(Δrow, Δcol)` more steps.
Thus `h` never overestimates (**admissible**), and along any edge the Chebyshev
distance drops by at most `1` while `g` rises by exactly `1`, so `h(n) ≤ 1 + h(n')`
(**consistent**). Consistency means the first time we pop the goal, its cost is
optimal.

**Algorithm:**

1. If `grid[0][0]` or `grid[n-1][n-1]` is `1`, return `-1` (blocked endpoints).
2. Push `(f = 1 + h(0,0), g = 1, (0,0))` onto a min-heap; record `best[(0,0)] = 1`.
3. Pop the state with the smallest `f`. If it is the goal, return its `g`.
4. Skip the entry if it is stale (`g` greater than the best recorded for that cell).
5. For each of the 8 neighbors that is in bounds and `0`, compute `ng = g + 1`; if it
   improves `best[neighbor]`, update it and push `(ng + h(neighbor), ng, neighbor)`.
6. If the heap empties, the goal is unreachable — return `-1`.

**Reference implementation:**

```python
import heapq
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        if n == 1:
            return 1

        def h(r: int, c: int) -> int:                 # Chebyshev distance
            return max(n - 1 - r, n - 1 - c)

        best = {(0, 0): 1}
        pq = [(1 + h(0, 0), 1, 0, 0)]                 # (f, g, r, c)
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)]

        while pq:
            f, g, r, c = heapq.heappop(pq)
            if (r, c) == (n - 1, n - 1):
                return g
            if g > best.get((r, c), float("inf")):
                continue                              # stale duplicate
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    ng = g + 1
                    if ng < best.get((nr, nc), float("inf")):
                        best[(nr, nc)] = ng
                        heapq.heappush(pq, (ng + h(nr, nc), ng, nr, nc))
        return -1
```

- **Time:** `O(n^2 log n)` worst case — every cell can enter the heap and each heap op
  is `O(log(n^2)) = O(log n)`. (Plain BFS is `O(n^2)`; A\* trades a log factor for
  goal-directed pruning that usually wins on large sparse grids.)
- **Space:** `O(n^2)` for the `best` map and the heap.

## Key Insights & Edge Cases

- **Chebyshev, not Manhattan.** Diagonal moves are allowed and cost the same as
  orthogonal ones, so the correct admissible distance to the corner is
  `max(|dr|, |dc|)`. Using Manhattan (`|dr| + |dc|`) would **overestimate** and could
  break optimality.
- **Blocked endpoints.** If either corner is a `1`, immediately return `-1` — the path
  cannot start or cannot finish.
- **Single cell `n == 1`.** If `grid == [[0]]` the answer is `1` (start = goal). Handle
  this before the loop or ensure the goal check fires on the seeded start.
- **Path length counts cells, not edges,** so `g` starts at `1` for the start cell, and
  a `k`-edge path has length `k + 1`.
- **When A\* helps.** On tiny grids BFS is simpler and fine. A\* shines when `n` is
  large and mostly open: the Chebyshev heuristic pulls the frontier toward the goal
  instead of expanding a full disk of radius `d` around the start.
