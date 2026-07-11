# Unique Paths II — Solution

## Brute Force

Recurse over right/down moves as in plain Unique Paths, but abandon a branch the
moment it steps onto an obstacle.

```python
def count(i, j):
    if i >= m or j >= n or grid[i][j] == 1:
        return 0
    if i == m - 1 and j == n - 1:
        return 1
    return count(i + 1, j) + count(i, j + 1)
```

- **Time:** `O(2^(m+n))` — exponential, same branching structure as Unique Paths.
- **Space:** `O(m + n)` recursion stack.

## Optimal Approach (Dynamic Programming on Grid)

Let `dp[i][j]` be the number of obstacle-free right/down paths from `(0, 0)` to
`(i, j)`.

**Recurrence.**

```
dp[i][j] = 0                          if grid[i][j] == 1   (blocked, unreachable)
dp[i][j] = dp[i-1][j] + dp[i][j-1]    otherwise
```

with the boundary convention that out-of-range predecessors contribute `0`.

**Base cases.**
- `dp[0][0] = 1` if the start is free, else `0` (and then the whole answer is `0`).
- In the first row, `dp[0][j] = dp[0][j-1]` when free, so it stays `1` until the
  first obstacle and becomes `0` from that obstacle onward (you cannot go around it
  in a single row). The first column behaves symmetrically.

**Why it is correct.** It is the exact same "sum of the two predecessors" argument
as Unique Paths, with the added rule that an obstacle cell is reachable by zero
valid paths. Setting `dp[i][j] = 0` on obstacles means any downstream cell that
would have routed through the obstacle simply does not count those routes, which is
precisely the "path cannot include an obstacle" constraint. The move monotonicity
keeps the dependency graph acyclic, so a single top-left to bottom-right sweep is
valid.

**Step by step (Example 1):**

```
grid            dp
0 0 0           1 1 1
0 1 0     ->    1 0 1
0 0 0           1 1 2
```

`dp[1][1]` is forced to `0` (obstacle). `dp[1][2] = dp[0][2] + dp[1][1] = 1`,
`dp[2][1] = dp[1][1] + dp[2][0] = 1`, and finally
`dp[2][2] = dp[1][2] + dp[2][1] = 2`, matching the expected output.

**Reference implementation:**

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1  # one way to be "at the start" before any obstacle check
        for row in obstacleGrid:
            for j in range(n):
                if row[j] == 1:
                    dp[j] = 0                 # obstacle: unreachable
                elif j > 0:
                    dp[j] += dp[j - 1]        # dp[j]=above, dp[j-1]=left
            # j == 0 free cell keeps its "above" value automatically
        return dp[-1]
```

## Key Insights & Edge Cases

- **Start or end is an obstacle.** If `grid[0][0] == 1` the answer is `0`; the
  rolling code handles this because the very first cell sets `dp[0] = 0`. Likewise a
  blocked destination yields `0` naturally.
- **Obstacles in the first row/column zero out everything after them.** Do not seed
  the whole first row/column with `1`; propagate from the previous cell so an
  obstacle correctly cuts off the rest of that line.
- **Rolling-array subtlety.** Keeping `dp[j]` as "above" and only adding `dp[j-1]`
  ("left") when `j > 0` reproduces the 2D recurrence in `O(n)` space.
- **Complexity.** `O(m * n)` time, `O(n)` space.
