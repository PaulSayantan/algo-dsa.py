# Number of Islands — Solution

## Optimal Approach

Iterate over every cell. When you find an unvisited `'1'`, increment the island
count and run a BFS from that cell, marking each reached land cell as visited (by
overwriting it with `'0'`) so it is never counted again. Because BFS drains the
entire connected component before returning, each launch corresponds to exactly
one island. Runs in O(m·n) time and O(min(m, n)) queue space.

### Reference implementation

```python
class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue
                count += 1
                grid[r][c] = "0"
                q = deque([(r, c)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                            grid[nx][ny] = "0"
                            q.append((nx, ny))
        return count
```
