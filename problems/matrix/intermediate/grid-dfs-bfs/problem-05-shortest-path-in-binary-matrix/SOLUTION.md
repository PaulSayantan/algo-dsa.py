# Shortest Path in Binary Matrix — Solution

## Brute Force

Enumerate paths with DFS/backtracking, tracking the minimum length that reaches
the target. Because you must allow revisiting cells across *different* candidate
paths, the search branches exponentially.

- **Time:** exponential — up to `O(8^(n^2))` without strong pruning.
- **Space:** `O(n^2)` recursion depth.

Plain DFS is the wrong tool here: it explores deep paths first and does not
naturally yield the *shortest* one, so it revisits cells wastefully.

## Optimal Approach (8-directional Grid BFS)

All moves cost exactly one step, so the graph is **unweighted** and BFS finds
shortest paths. Treat each open cell as a node with up to 8 edges (orthogonal +
diagonal). BFS from `(0,0)` expands cells in order of distance; the first time it
reaches `(n-1, n-1)`, that distance is optimal.

**Why it is correct:** BFS visits nodes in nondecreasing order of their distance
(in edges) from the source. On an unweighted graph this distance equals the
minimum number of moves. Marking a cell visited when first enqueued guarantees it
is reached along a shortest route and never re-expanded, keeping the run linear.

Track path length as **cells visited**: seed the start with distance `1`, and
each expansion adds `1`.

### Step by step / reference implementation

```python
from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1

    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]

    q = deque([(0, 0, 1)])   # (row, col, path_length_so_far)
    grid[0][0] = 1           # mark visited by blocking

    while q:
        r, c, dist = q.popleft()
        if r == n - 1 and c == n - 1:
            return dist
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                grid[nr][nc] = 1        # mark before enqueue -> no duplicates
                q.append((nr, nc, dist + 1))

    return -1
```

- **Time:** `O(n^2)` — each of the `n^2` cells is enqueued at most once and has 8
  neighbors (constant).
- **Space:** `O(n^2)` — the queue / visited marking.

## Key Insights & Edge Cases

- **BFS, not DFS**, because we want the *shortest* path on an unweighted grid.
- **8 directions**, including all four diagonals — forgetting diagonals inflates
  the answer.
- **Blocked endpoints:** if `grid[0][0]` or `grid[n-1][n-1]` is `1`, immediately
  return `-1`.
- **1x1 grid** of value `0`: start *is* the target, so the answer is `1` (the
  code returns `1` because the seeded start is dequeued as the target).
- **Mark visited on enqueue** (not on dequeue) to avoid pushing the same cell
  many times; mutating the grid to `1` is a clean way to do this in place.
