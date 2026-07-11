# Shortest Path in a Grid with Obstacles Elimination — Solution

## Brute Force

Try DFS/backtracking over every path, tracking how many obstacles you have broken, and
keep the shortest that reaches the goal within budget `k`.

- **Time:** exponential in the number of cells — the number of distinct simple paths in
  a grid is enormous, and naive DFS re-derives overlapping subpaths repeatedly.
- **Space:** `O(m * n)` recursion depth.

The fix is to recognize the correct **state**: not just the cell, but `(r, c, budget
left)`. Once state is defined, this is an unweighted shortest-path problem (every step
costs `1`) solvable by BFS, and A\* makes it goal-directed.

## Optimal Approach (A\* Search over an augmented state graph)

The crucial modeling insight: reaching cell `(r, c)` with `3` eliminations remaining is
a **different, generally better** situation than reaching it with `1` remaining. So the
search state is the triple

```
state = (r, c, eliminations_left)
```

There are `m * n * (k + 1)` such states. Every move costs `1` step, so shortest-path
methods apply. Use A\* with:

- `g(state)` = number of steps taken to reach it.
- `h(r, c) = (m - 1 - r) + (n - 1 - c)` — the **Manhattan distance** to the goal.

**Why `h` is admissible and consistent:** any path to the corner must make at least
`|Δrow| + |Δcol|` orthogonal moves regardless of obstacles, so `h` never overestimates
the remaining steps. Along any single move Manhattan distance changes by exactly `±1`
while `g` grows by `1`, so `h(u) ≤ 1 + h(v)` — consistent — and the first pop of any
state is optimal. The `eliminations_left` component does not affect `h` (it only gates
which transitions are legal), which keeps `h` a clean lower bound.

**A key pruning shortcut:** if `k >= (m - 1) + (n - 1)`, you have enough budget to bust
straight through everything, and the answer is simply the Manhattan distance
`m + n - 2`.

**Algorithm:**

1. If `k >= m + n - 2`, return `m + n - 2` (can go straight to the corner).
2. Seed the heap with `(f = h(0,0), g = 0, r = 0, c = 0, rem = k)`.
3. Pop the smallest `f`. If `(r, c)` is the goal, return `g`.
4. For each 4-neighbor: compute `nrem = rem - grid[nr][nc]`. If `nrem >= 0` and the new
   step count improves the best known cost for the exact state `(nr, nc, nrem)`, record
   it and push `(g + 1 + h(nr, nc), g + 1, nr, nc, nrem)`.
5. If the heap drains, return `-1`.

Keying the visited map by the full triple `(r, c, rem)` is the simplest provably
correct choice: each of the `m * n * (k + 1)` states is settled at most once. A tighter
*dominance* rule (keep only the largest remaining budget per cell) can prune further —
see the edge-cases section.

**Reference implementation:**

```python
import heapq
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        goal = (m - 1, n - 1)

        # If we can bust through everything, straight-line Manhattan is the answer.
        if k >= m + n - 2:
            return m + n - 2

        def h(r: int, c: int) -> int:
            return (m - 1 - r) + (n - 1 - c)

        # best[(r, c, rem)] = fewest steps known to reach that exact state.
        best = {(0, 0, k): 0}
        pq = [(h(0, 0), 0, 0, 0, k)]          # (f, g, r, c, rem)
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while pq:
            f, g, r, c, rem = heapq.heappop(pq)
            if (r, c) == goal:
                return g
            if g > best.get((r, c, rem), float("inf")):
                continue                       # stale duplicate
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nrem = rem - grid[nr][nc]
                    ng = g + 1
                    if nrem >= 0 and ng < best.get((nr, nc, nrem), float("inf")):
                        best[(nr, nc, nrem)] = ng
                        heapq.heappush(pq, (ng + h(nr, nc), ng, nr, nc, nrem))
        return -1
```

- **Time:** `O(m * n * k * log(m * n * k))` worst case — every `(cell, budget)` state
  may enter the heap once. The Manhattan heuristic and the "bust-through" shortcut
  usually cut this far below the worst case.
- **Space:** `O(m * n * k)` for the visited/best structure and the heap.

## Key Insights & Edge Cases

- **State must include the budget.** The single most common bug is treating a cell as
  visited regardless of remaining eliminations. Two arrivals with different budgets are
  different states; the one with more budget can unlock shorter continuations.
- **Dominance pruning (optional optimization).** Because more budget is never worse, an
  arrival at a cell with a smaller-or-equal remaining budget *and* a longer-or-equal
  distance is dominated. Tracking the largest remaining budget seen per cell lets you
  skip such arrivals and can shrink the explored set toward `O(m*n)`. Keying `best` by
  the full `(r, c, rem)` triple (as above) is the simplest provably-correct version;
  reach for the tighter dominance rule only once the basic version works.
- **Straight-shot shortcut.** When `k >= m + n - 2` the Manhattan distance is
  achievable directly, so return it without searching.
- **Endpoints are guaranteed empty** (`grid[0][0] == grid[m-1][n-1] == 0`), so no
  budget is spent on the start or the goal itself.
- **Unreachable case.** If even after exhausting the budget the goal is never popped,
  return `-1` (e.g. a thick wall requiring more than `k` breaks).
- **Manhattan is the right heuristic** here (4-directional moves, unit cost); using
  Chebyshev would *underestimate* even more (still admissible but weaker), while
  Euclidean is also admissible but non-integer and no tighter than Manhattan.
