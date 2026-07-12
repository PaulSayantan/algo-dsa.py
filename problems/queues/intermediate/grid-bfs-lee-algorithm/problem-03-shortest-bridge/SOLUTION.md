# Shortest Bridge — Solution

## Optimal Approach

First locate one island with a flood fill (DFS/BFS), marking every one of its
cells as *seen* and seeding all of them into a BFS queue at distance `0`. This
turns the whole first island into a multi-source frontier. Then run a Lee-style
BFS outward over water cells: each ring of `0`-cells increases the flip count by
one. The moment the frontier reaches a `1`-cell that is not part of the first
island, that distance is the minimum number of flips — BFS guarantees it is the
shortest bridge. Runs in O(n²).

### Reference implementation

```python
class Solution:
    def shortestBridge(self, grid):
        n = len(grid)
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = deque()
        seen = set()

        def flood(sr, sc):
            stack = [(sr, sc)]
            seen.add((sr, sc))
            while stack:
                r, c = stack.pop()
                q.append((r, c, 0))
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1 and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        stack.append((nr, nc))

        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    flood(i, j)
                    found = True
                    break

        while q:
            r, c, d = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                    if grid[nr][nc] == 1:
                        return d
                    seen.add((nr, nc))
                    q.append((nr, nc, d + 1))
        return -1
```
