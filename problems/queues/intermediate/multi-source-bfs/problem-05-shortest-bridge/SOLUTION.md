# Shortest Bridge — Solution

## Optimal Approach

Two phases. First, locate one island and flood-fill it (a DFS/BFS from the first
`1` found), marking every cell of it and collecting them into a queue. Second,
run a *multi-source* BFS from all those cells at once, expanding through water in
distance-ordered waves. The first time the frontier touches a cell belonging to
the other island, the number of waves taken is the minimum bridge length.

Seeding the queue with the entire first island (not a single cell) is what makes
this a multi-source BFS: every border cell of the island advances together, so
the wave count is exactly the shortest water gap to the second island.

### Reference implementation

```python
class Solution:
    def shortestBridge(self, grid):
        n = len(grid)
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # Phase 1: flood-fill the first island, marking its cells as 2.
        def find_first():
            for r in range(n):
                for c in range(n):
                    if grid[r][c] == 1:
                        return (r, c)
            return None

        q = deque()
        start = find_first()
        stack = [start]
        grid[start[0]][start[1]] = 2
        while stack:
            r, c = stack.pop()
            q.append((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    stack.append((nr, nc))

        # Phase 2: multi-source BFS from the whole island toward the other one.
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return steps
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
            steps += 1
        return -1
```
