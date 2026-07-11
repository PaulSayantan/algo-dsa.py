# Sliding Puzzle — Solution

## Brute Force

Explore move sequences with plain **DFS/backtracking**, trying every legal slide and
tracking the shortest sequence that reaches the goal.

- **Time:** exponential — with branching factor up to 3 and no memoization, DFS revisits
  the same configurations over and over and can loop indefinitely without a visited set.
- **Space:** `O(depth)` for the recursion stack.

The state space is actually tiny (`6! = 720` configurations), so the real fix is to
search over **configurations** with a visited set. Plain BFS over the 720 states solves
it in `O(720)` time; A\* keeps that guarantee while expanding even fewer states via a
heuristic — the standard demonstration of A\* on an implicit graph.

## Optimal Approach (A\* Search)

Flatten the `2 x 3` board into a 6-tuple so it is hashable, e.g.
`[[4,1,2],[5,0,3]] -> (4,1,2,5,0,3)`. The goal is `(1,2,3,4,5,0)`. Precompute, for each
board index `0..5`, which indices are 4-directionally adjacent:

```
adj = {0:(1,3), 1:(0,2,4), 2:(1,5), 3:(0,4), 4:(1,3,5), 5:(2,4)}
```

A move locates the blank `0`, swaps it with one adjacent index, and yields a new state.
Each move costs `1`, so `g` = number of moves so far.

**Heuristic — sum of Manhattan distances.** For every tile (excluding the blank),
compute the Manhattan distance from its current `(row, col)` to its goal `(row, col)`,
and sum these:

```
h(state) = Σ_{tile ≠ 0}  |row_now - row_goal| + |col_now - col_goal|
```

**Why it is admissible:** each single move slides exactly one tile by one cell, so it
can reduce the total Manhattan sum by at most `1`. Hence you need at least `h(state)`
more moves — `h` never overestimates. (This heuristic is also consistent, since one move
changes `h` by at most `1` while `g` grows by `1`.) A\* therefore returns the optimal
move count.

**Reachability / parity.** Only half of the `720` permutations are reachable from the
goal (the sliding puzzle has an invariant parity). Unreachable boards — like Example 2 —
are simply never popped as the goal, so when the priority queue empties we return `-1`.

**Algorithm:**

1. Flatten `board` to `start`; if `start == target` return `0`.
2. Push `(h(start), 0, start)`; keep `best[start] = 0`.
3. Pop the smallest `f`. If it is `target`, return `g`. Skip stale entries.
4. Find the blank index; for each adjacent index, build the swapped state `ns` with
   `ng = g + 1`; if it improves `best[ns]`, push `(ng + h(ns), ng, ns)`.
5. If the heap empties, return `-1`.

**Reference implementation:**

```python
import heapq
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = tuple(board[0] + board[1])
        target = (1, 2, 3, 4, 5, 0)
        adj = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5),
               3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}
        goal_pos = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                    4: (1, 0), 5: (1, 1)}         # blank (0) excluded

        def h(state):
            total = 0
            for idx, val in enumerate(state):
                if val == 0:
                    continue
                r, c = divmod(idx, 3)
                gr, gc = goal_pos[val]
                total += abs(r - gr) + abs(c - gc)
            return total

        best = {start: 0}
        pq = [(h(start), 0, start)]              # (f, g, state)
        while pq:
            f, g, state = heapq.heappop(pq)
            if state == target:
                return g
            if g > best.get(state, float("inf")):
                continue                          # stale duplicate
            z = state.index(0)
            for nb in adj[z]:
                lst = list(state)
                lst[z], lst[nb] = lst[nb], lst[z]
                ns = tuple(lst)
                ng = g + 1
                if ng < best.get(ns, float("inf")):
                    best[ns] = ng
                    heapq.heappush(pq, (ng + h(ns), ng, ns))
        return -1
```

- **Time:** `O(S log S)` where `S = 6! = 720` is the number of states — each state is
  settled once and each heap op is `O(log S)`. Bounded and tiny in practice.
- **Space:** `O(S)` for `best` and the heap.

## Key Insights & Edge Cases

- **Configurations are the nodes.** The leap is to search over board *states* rather
  than cells. Flattening to a tuple makes states hashable for the visited/`best` map.
- **Exclude the blank from `h`.** The `0` is not a real tile with a "home"; counting its
  displacement would make `h` overestimate and can break optimality. Sum Manhattan
  distances of the numbered tiles only.
- **Admissibility gives correctness; the heuristic gives speed.** Manhattan-sum is a
  classic admissible puzzle heuristic; it prunes the frontier far below BFS while still
  yielding the optimal answer.
- **Unsolvable boards return `-1`.** Half of all permutations are unreachable by parity;
  the search naturally reports `-1` when it exhausts the reachable component.
- **Already solved.** If the input equals the target, the answer is `0` — the goal check
  fires immediately on the seeded start.
- **Generalizes.** The same A\* + Manhattan-sum recipe scales to the 8-puzzle (`3x3`) and
  15-puzzle (`4x4`), where the exponential state space makes the heuristic essential
  rather than merely nice.
