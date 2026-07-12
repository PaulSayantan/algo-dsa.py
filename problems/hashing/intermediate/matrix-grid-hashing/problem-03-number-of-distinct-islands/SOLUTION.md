# Number of Distinct Islands — Solution

## Optimal Approach

Normalize each island's coordinates to its anchor; hash the sorted cell tuple.

### Reference implementation

```python
class Solution:
    def numDistinctIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        seen = [[False] * cols for _ in range(rows)]
        shapes = set()

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            seen[sr][sc] = True
            cells = []
            while q:
                r, c = q.popleft()
                cells.append((r - sr, c - sc))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not seen[nr][nc] and grid[nr][nc] == 1:
                        seen[nr][nc] = True
                        q.append((nr, nc))
            return tuple(sorted(cells))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not seen[r][c]:
                    shapes.add(bfs(r, c))
        return len(shapes)
```

### Complexity

Time O(R*C), space O(R*C).

## Key Insights & Edge Cases

Two translated 2x2 blocks share one shape; empty grid yields 0.
