# Minimum Turns to Cross a Maze — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def minTurns(self, grid):
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return -1
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        INF = float("inf")
        # dist[r][c][d]: fewest turns to reach (r, c) arriving with direction d.
        # d == 4 is a sentinel "no direction yet" used only at the start cell, so
        # the very first step never costs a turn.
        dist = [[[INF] * 5 for _ in range(n)] for _ in range(m)]
        dist[0][0][4] = 0
        dq = deque([(0, 0, 4)])
        while dq:
            r, c, d = dq.popleft()
            cur = dist[r][c][d]
            for nd, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                    w = 0 if (d == 4 or d == nd) else 1
                    cost = cur + w
                    if cost < dist[nr][nc][nd]:
                        dist[nr][nc][nd] = cost
                        if w == 0:
                            dq.appendleft((nr, nc, nd))
                        else:
                            dq.append((nr, nc, nd))
        ans = min(dist[m - 1][n - 1][d] for d in range(5))
        return ans if ans != INF else -1
```

### Complexity

O(m*n) states times 4 directions -> O(m*n) time and space.

## Key Insights & Edge Cases

Turns, not steps, are the cost, so the state must remember the direction you entered a cell with. Continuing straight keeps the same direction index (weight 0, pushed to the front); switching to any of the other three directions is one turn (weight 1, pushed to the back). The sentinel direction `4` at the start makes the first move free regardless of orientation. A single cell needs `0` turns; a straight corridor (one row or one column) also needs `0`. If the start or goal is a wall, or the goal is walled off, the goal's distance stays infinite and the answer is `-1`.
