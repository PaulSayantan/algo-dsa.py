# Minimum Knight Moves — Solution

## Brute Force

A plain **breadth-first search** from `(0, 0)` over the infinite board, expanding all 8
knight moves per state until it dequeues `(x, y)`.

- **Time:** `O(D^2)` where `D = |x| + |y|` — the number of squares within `k` knight
  moves grows quadratically, so BFS visits a full disk of radius `~D` (up to a few
  hundred thousand cells for the constraint limits).
- **Space:** `O(D^2)` for the visited set and queue.

BFS is correct but wasteful: it explores squares in *every* direction, including those
pointing away from the target. Two easy accelerators exist — exploit symmetry (fold to
`x, y ≥ 0`) and, more powerfully, add a heuristic so the search heads toward the goal.

## Optimal Approach (A\* Search)

Fold the target into the first quadrant with `x, y = abs(x), abs(y)` (the board and move
set are symmetric across both axes and the diagonal, so the answer is unchanged). Then
run A\* toward `(x, y)`.

Let `g` be the number of moves made so far. We need a heuristic `h(r, c)` that never
exceeds the true remaining number of knight moves to `(x, y)`. Two independent lower
bounds combine cleanly:

- A knight changes the **Manhattan distance** `|dr| + |dc|` by **at most 3** per move,
  so at least `ceil((|dx| + |dy|) / 3)` moves remain.
- A knight changes **either coordinate** by **at most 2** per move, so at least
  `ceil(max(|dx|, |dy|) / 2)` moves remain.

Taking the max of two valid lower bounds is still a valid lower bound:

```
h(r, c) = max( ceil((|x-r| + |y-c|) / 3),
               ceil(max(|x-r|, |y-c|) / 2) )
```

**Why it is admissible:** each term is a proven lower bound on remaining moves as
argued above, so `h ≤ true remaining cost`; therefore A\* returns the optimal count.
(This `h` is admissible; treat it as a plain admissible heuristic and keep the standard
"skip stale entries / allow re-expansion via the `best` map" bookkeeping, which is
robust even if consistency were ever in doubt.)

**Algorithm:**

1. Replace `x, y` with their absolute values; if `(x, y) == (0, 0)` return `0`.
2. Bound the search region (e.g. clamp coordinates to `[-2, x+2] x [-2, y+2]`) so the
   knight is allowed to overshoot slightly — optimal paths near an axis can dip one
   step negative — without wandering off to infinity.
3. Push `(f = h(0,0), g = 0, (0,0))`; run A\* with the 8 knight moves.
4. When `(x, y)` is popped, return its `g`.

**Reference implementation:**

```python
import heapq
from math import ceil


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)               # fold into the first quadrant

        def h(r: int, c: int) -> int:
            dx, dy = abs(x - r), abs(y - c)
            return max((dx + dy + 2) // 3, (max(dx, dy) + 1) // 2)

        moves = [(1, 2), (2, 1), (-1, 2), (-2, 1),
                 (1, -2), (2, -1), (-1, -2), (-2, -1)]
        best = {(0, 0): 0}
        pq = [(h(0, 0), 0, 0, 0)]           # (f, g, r, c)

        while pq:
            f, g, r, c = heapq.heappop(pq)
            if (r, c) == (x, y):
                return g
            if g > best.get((r, c), float("inf")):
                continue
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if -2 <= nr <= x + 2 and -2 <= nc <= y + 2:
                    ng = g + 1
                    if ng < best.get((nr, nc), float("inf")):
                        best[(nr, nc)] = ng
                        heapq.heappush(pq, (ng + h(nr, nc), ng, nr, nc))
        return -1                            # unreachable in practice (guaranteed)
```

- **Time:** `O(D^2 log D)` worst case with `D = |x| + |y|`, but the heuristic keeps the
  expanded set close to the actual optimal path, so it is dramatically smaller in
  practice than uninformed BFS.
- **Space:** `O(D^2)` worst case for `best` and the heap.

## Key Insights & Edge Cases

- **Symmetry fold.** Taking absolute values collapses four quadrants and both diagonal
  reflections into one, so you never search negative-heavy regions unnecessarily.
- **Allow a small negative overshoot.** For targets close to an axis (like `(1, 1)`,
  answer `2`), the optimal route momentarily steps to a coordinate like `-1`. Bounding
  at `-2` (not `0`) keeps those paths available.
- **Origin is the goal.** `(x, y) == (0, 0)` must return `0`; make sure the goal check
  fires on the seeded start before expansion.
- **Combine lower bounds by `max`.** Neither the Manhattan/3 bound nor the axis/2 bound
  dominates the other; their maximum is the tightest admissible estimate and never
  overestimates.
- **Closed-form alternative exists** (a constant-time formula), but the point here is
  the A\* technique: an informed priority queue turning a huge BFS disk into a narrow
  goal-directed cone.
