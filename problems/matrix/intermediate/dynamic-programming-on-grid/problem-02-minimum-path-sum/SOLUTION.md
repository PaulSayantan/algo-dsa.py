# Minimum Path Sum — Solution

## Brute Force

Recursively try both moves from every cell and take the minimum total, adding the
current cell's value along the way.

```python
def best(i, j):
    if i == m - 1 and j == n - 1:
        return grid[i][j]
    if i >= m or j >= n:
        return float("inf")
    return grid[i][j] + min(best(i + 1, j), best(i, j + 1))
```

- **Time:** `O(2^(m+n))` — exponential branching with heavy overlap.
- **Space:** `O(m + n)` recursion stack.

The same `(i, j)` subproblem is solved many times, which memoization or a bottom-up
table eliminates.

## Optimal Approach (Dynamic Programming on Grid)

Let `dp[i][j]` be the minimum sum of any right/down path from `(0, 0)` to `(i, j)`.

**Recurrence.** The last move into `(i, j)` came from above or from the left, so we
take the cheaper predecessor and add the current value:

```
dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
```

**Base cases.**
- `dp[0][0] = grid[0][0]`.
- First row: `dp[0][j] = dp[0][j-1] + grid[0][j]` (can only come from the left).
- First column: `dp[i][0] = dp[i-1][0] + grid[i][0]` (can only come from above).

**Why it is correct.** This is the shortest-path principle on a DAG. Any optimal
path to `(i, j)` must reach one of its two predecessors optimally (otherwise you
could swap in a cheaper prefix and beat the supposed optimum — a contradiction).
Taking the min over the two predecessors therefore yields the true optimum, and the
non-negative values are not even required for correctness here because the DAG is
acyclic. Processing cells in increasing row/column order ensures both predecessors
are finalized first.

**Step by step (Example 1):**

```
grid            dp
1 3 1           1 4 5
1 5 1     ->    2 7 6
4 2 1           6 8 7
```

`dp[2][2] = 7`, matching the expected output. Trace: `dp[1][2] = 1 + min(5, 7) = 6`,
then `dp[2][2] = 1 + min(6, 8) = 7`.

**Reference implementation:**

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        dp = [float("inf")] * n
        dp[0] = 0  # will be overwritten by grid[0][0] on the first cell
        for i, row in enumerate(grid):
            dp[0] = dp[0] + row[0] if i > 0 else row[0]
            for j in range(1, n):
                dp[j] = row[j] + min(dp[j], dp[j - 1])  # dp[j]=above, dp[j-1]=left
        return dp[-1]
```

- **Time:** `O(m * n)`.
- **Space:** `O(n)` with a rolling row (`O(m * n)` for the full table).

## Key Insights & Edge Cases

- **Handle the first row and first column specially.** They each have only one
  predecessor; using a generic `min(above, left)` there requires the missing
  neighbor to be treated as `+infinity` (as the rolling-array version does).
- **Single cell / single row / single column.** A `1x1` grid returns `grid[0][0]`.
  Single-row and single-column grids reduce to a prefix sum along the only line.
- **In-place variant.** You may overwrite `grid` itself as the DP table to use
  `O(1)` extra space, at the cost of mutating the input.
- **Non-negativity is a red herring for correctness** but does guarantee sums stay
  bounded (`<= 200 * (m + n) <= 80000`), so no overflow concerns.
