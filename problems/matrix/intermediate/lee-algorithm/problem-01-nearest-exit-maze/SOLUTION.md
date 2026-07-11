# Solution — Nearest Exit from Entrance in Maze

## Brute Force

Try every path from the entrance with DFS/backtracking, tracking the length of
each path that terminates on a border cell, and keep the minimum. Because the
same cell can be revisited along exponentially many different routes, this
degenerates into exploring an enormous number of paths.

- **Time:** Exponential in the number of cells (up to O(4^(m·n)) without strong
  pruning).
- **Space:** O(m·n) recursion depth.

This is far too slow and completely unnecessary for an unweighted grid.

## Optimal Approach — Lee Algorithm (BFS)

Every move costs exactly 1 step, so the grid is an **unweighted graph** and BFS
finds shortest distances. BFS expands cells in strictly increasing distance from
the entrance, so the **first** border exit it reaches is provably the nearest.

### Why it is correct

BFS processes cells in "waves": all cells at distance `d` are dequeued before any
cell at distance `d+1`. Therefore the moment we dequeue (or enqueue) a valid exit
cell, no closer exit could exist — otherwise it would have been discovered in an
earlier wave. Marking a cell visited on enqueue guarantees each cell is processed
at most once.

### Step by step

1. Push the entrance into a queue with distance 0 and mark it visited (turn it
   into a wall, or use a separate visited set).
2. Pop a cell `(r, c)` with distance `d`. For each of the 4 neighbours:
   - Skip if out of bounds, a wall, or already visited.
   - Mark it visited and set its distance to `d + 1`.
   - If the neighbour lies on the **border** (`row == 0` or `row == m-1` or
     `col == 0` or `col == n-1`), it is an exit — return `d + 1` immediately.
   - Otherwise enqueue it.
3. If the queue empties without finding an exit, return `-1`.

Note we check "is this an exit?" for **neighbours**, not the entrance, which
elegantly excludes the entrance even though it can sit on the border.

```python
from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        er, ec = entrance
        q = deque([(er, ec, 0)])
        maze[er][ec] = "+"  # mark visited by walling it off
        while q:
            r, c, d = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".":
                    if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                        return d + 1
                    maze[nr][nc] = "+"
                    q.append((nr, nc, d + 1))
        return -1
```

- **Time:** O(m · n) — each cell is enqueued and dequeued at most once.
- **Space:** O(m · n) for the queue / visited marking.

## Key Insights & Edge Cases

- **Entrance is not an exit:** only test the border condition on *neighbours*,
  or explicitly skip the entrance cell.
- **Mark visited on enqueue**, not on dequeue, so a cell is never added twice —
  this preserves the O(m·n) bound.
- **In-place visited marking** (overwriting `'.'` with `'+'`) avoids an extra
  array; use a separate `visited` set if you must not mutate the input.
- **Single-cell / all-walls mazes:** if the entrance has no walkable neighbour,
  the queue drains immediately and the answer is `-1`.
- BFS, not DFS: DFS finds *a* path but not necessarily the *shortest* one.
