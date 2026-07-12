# As Far from Land as Possible — Solution

## Optimal Approach

Push every land cell into the queue at distance 0 and BFS outward through water
simultaneously. Because all sources expand together in lockstep waves, each water
cell is first reached at its nearest-land distance. The distance recorded on the
final cell dequeued is the largest nearest-land distance in the grid.

If there is no land (nothing to seed) or no water (nothing to expand into), the
answer is `-1`.

### Reference implementation

```python
class Solution:
    def maxDistance(self, grid):
        n = len(grid)
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
        if not q or len(q) == n * n:
            return -1
        dist = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))
            dist += 1
        return dist
```
