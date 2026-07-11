# Shortest Bridge — Solution

## Brute Force

Identify both islands. Then, for **every** cell of island A and **every** cell of
island B, compute the Manhattan distance between them; the minimum such distance minus
1 is the number of water cells to flip. (Distance in cells between adjacent centers is
`|dr| + |dc|`; the bridge length is that minus 1 because both endpoints are land.)

- **Time:** `O(|A| * |B|)`, which is `O((n^2)^2) = O(n^4)` in the worst case when both
  islands are large.
- **Space:** `O(n^2)` to store the island cells.

This checks far more pairs than necessary and does not naturally handle obstacle-aware
paths (though here water is freely passable, so Manhattan distance happens to work).

## Optimal Approach (Flood Fill + Multi-Source BFS)

The two-phase idea: collapse one entire island into a *single multi-source frontier*,
then expand outward until the frontier first touches the other island. Because BFS
grows one water-ring at a time, the number of rings crossed is exactly the number of
water cells to flip.

**Algorithm:**

1. **Flood fill island A.** Scan for the first `1`. From it, run DFS or BFS over
   4-connected `1`s, marking every cell of that island (e.g. change to `2` or add to a
   visited set) and pushing each into a queue `q`. This queue is the multi-source
   frontier — *all* of island A at distance `0`.
2. **Multi-Source BFS outward.** Expand level by level. For each level (`steps`),
   drain the current frontier; for each 4-neighbor:
   - if it is water (`0`), mark it visited and enqueue it (part of the next ring);
   - if it is part of island B (a `1` that was **not** marked in step 1), you have
     reached the other island — return `steps`.
3. Increment `steps` after fully processing each ring of water.

**Why it is correct:** Marking every cell of island A as a source means the BFS
computes, for each water cell, the shortest distance to island A. The first time the
frontier expands onto an unmarked land cell, that cell belongs to island B and lies at
the minimum island-to-island distance. Since each ring is one flipped water cell, the
ring count at that moment is the minimum number of flips. BFS's non-decreasing
distance order guarantees this first contact is via a shortest bridge.

**Reference implementation:**

```python
from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = deque()

        # 1) Flood fill the first island, marking cells as 2 and seeding the queue.
        def dfs(sr: int, sc: int) -> None:
            stack = [(sr, sc)]
            grid[sr][sc] = 2
            while stack:
                r, c = stack.pop()
                q.append((r, c))
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        stack.append((nr, nc))

        found = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
            if found:
                break

        # 2) Multi-Source BFS out from all of island A until we hit island B.
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:      # reached the second island
                            return steps
                        if grid[nr][nc] == 0:      # water: expand
                            grid[nr][nc] = 2
                            q.append((nr, nc))
            steps += 1

        return -1  # unreachable given exactly two islands
```

- **Time:** `O(n^2)` — the flood fill and the BFS each touch every cell at most once.
- **Space:** `O(n^2)` for the queue / visited marking.

## Key Insights & Edge Cases

- **Two phases, one BFS.** The distinguishing move versus the earlier problems: you
  first *build* the source set with a flood fill (all of island A), then run a single
  Multi-Source BFS. Seeding the whole island — not just one cell — is what makes the
  ring count equal the true minimum bridge.
- **Mark island A distinctly** (e.g. `2`) so the BFS can tell "my own island" (skip)
  from "the other island" (`1`, the goal).
- **Return `steps` on first contact, before incrementing.** When the frontier at level
  `steps` finds a `1`, the bridge is exactly `steps` water cells; do not add 1.
- **Stop after finding the first island in the scan.** Use a flag/break so you flood
  fill only *one* island, leaving the other as `1` targets.
- **Adjacent islands (`steps == 0` scenario):** if the two islands were touching there
  would be one island; the problem guarantees exactly two, so `steps >= 1` always, but
  the code structure handles the general case regardless.
- **DFS recursion depth:** on a `100 x 100` grid a recursive flood fill could recurse
  up to `10^4` deep; an explicit stack (as above) or `sys.setrecursionlimit` avoids
  overflow.
