# Cut Off Trees for Golf Event — Solution

## Brute Force

Because trees must be cut in strictly increasing height order, the *visiting order is
forced* — there is no permutation to optimize. So the whole task is: sum the shortest
walking distance between each consecutive pair of trees. The brute force for each leg is
a **DFS that enumerates paths** and keeps the minimum length.

- **Time:** exponential per leg — path enumeration on a grid explodes combinatorially.
- **Space:** `O(m * n)` recursion depth.

Since every step costs `1`, each leg is an unweighted shortest-path problem best solved
with BFS or A\*, not path enumeration. The only real algorithmic decision is *how to
compute each point-to-point distance efficiently*.

## Optimal Approach (A\* Search per leg)

**Step 1 — fix the order.** Collect all tree cells `(height, r, c)` and sort by height.
Distinct heights guarantee a unique order. You start at `(0, 0)` and must reach the
trees in that sorted order, cutting each.

**Step 2 — shortest path per leg with A\*.** For each consecutive pair
`(current) -> (next tree)`, run A\* on the grid. Movement is 4-directional between
walkable cells (`forest[r][c] != 0`); each step costs `1`. Use the **Manhattan
distance** to that leg's target as the heuristic:

```
h(r, c) = |r - target_r| + |c - target_c|
```

**Why `h` is admissible and consistent:** with unit-cost orthogonal moves, any path to
the target needs at least `|Δr| + |Δc|` steps, so `h` never overestimates; and each move
changes Manhattan distance by exactly `±1` while `g` grows by `1`, so `h(u) ≤ 1 + h(v)`.
A\* therefore returns each leg's optimal length, and the sum of optimal legs is the
optimal total (the order being forced).

**Step 3 — accumulate / detect impossibility.** Add each leg's cost to a running total.
If any leg's A\* returns `-1` (target unreachable, e.g. walled off by `0`s), the whole
task is impossible — return `-1`.

Note that after "cutting" a tree its cell becomes `1`, but since trees (value `> 1`) are
already walkable, cutting never opens or closes any path. That means the grid's
walkability is static across all legs, so you do **not** need to mutate `forest` between
legs — a common simplification.

**Reference implementation:**

```python
import heapq
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1
        m, n = len(forest), len(forest[0])

        # 1) Trees to cut, ordered by increasing height.
        trees = sorted((forest[r][c], r, c)
                       for r in range(m) for c in range(n) if forest[r][c] > 1)

        # 2) A* shortest walking distance for one leg.
        def astar(sr: int, sc: int, tr: int, tc: int) -> int:
            if (sr, sc) == (tr, tc):
                return 0

            def h(r: int, c: int) -> int:
                return abs(r - tr) + abs(c - tc)

            best = {(sr, sc): 0}
            pq = [(h(sr, sc), 0, sr, sc)]        # (f, g, r, c)
            dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
            while pq:
                f, g, r, c = heapq.heappop(pq)
                if (r, c) == (tr, tc):
                    return g
                if g > best.get((r, c), float("inf")):
                    continue                      # stale duplicate
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and forest[nr][nc] != 0:
                        ng = g + 1
                        if ng < best.get((nr, nc), float("inf")):
                            best[(nr, nc)] = ng
                            heapq.heappush(pq, (ng + h(nr, nc), ng, nr, nc))
            return -1

        # 3) Walk to each tree in order, summing leg costs.
        total = 0
        cr, cc = 0, 0
        for _, tr, tc in trees:
            d = astar(cr, cc, tr, tc)
            if d < 0:
                return -1
            total += d
            cr, cc = tr, tc
        return total
```

- **Time:** `O(T * m * n * log(m * n))` where `T` is the number of trees — each of the
  `T` legs runs an A\* that in the worst case touches all `m * n` cells with `O(log(mn))`
  heap ops. The Manhattan heuristic typically explores far fewer cells per leg.
- **Space:** `O(m * n)` for the per-leg `best` map and heap.

## Key Insights & Edge Cases

- **The order is not a choice.** Increasing-height cutting fixes the sequence, so this is
  *not* a Traveling Salesman problem — just a sum of independent shortest paths. That is
  what makes per-leg A\* / BFS optimal overall.
- **The grid is static.** Cutting a tree (`>1 -> 1`) never changes walkability, so you
  can reuse `forest` unchanged for every leg — no need to mutate between searches.
- **Manhattan is the right heuristic** for 4-directional unit-cost movement; it is
  admissible and consistent, giving A\* correctness and pruning.
- **Start may hold a tree.** If `(0, 0)` contains the shortest tree, the first leg has
  length `0` (you cut it in place). The `(sr, sc) == (tr, tc)` early return handles this.
- **Unreachable tree ⇒ `-1`.** A wall of `0`s (Example 2) can strand later trees; the
  moment any leg returns `-1`, the answer is `-1`.
- **BFS vs A\*.** Since every leg is unweighted, plain BFS per leg is also optimal and
  slightly simpler. A\* is the goal-directed upgrade: with a single known target per leg,
  the Manhattan heuristic steers each search and cuts the explored area, which matters on
  the `50 x 50` upper bound with many trees.
