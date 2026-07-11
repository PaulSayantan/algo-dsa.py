# Unique Paths — Solution

## Brute Force

Enumerate every path by recursion: from a cell `(i, j)`, try moving right and try
moving down, and count the paths that eventually land on the bottom-right corner.

```python
def count(i, j, m, n):
    if i == m - 1 and j == n - 1:
        return 1
    if i >= m or j >= n:
        return 0
    return count(i + 1, j, m, n) + count(i, j + 1, m, n)
```

- **Time:** `O(2^(m+n))` — the recursion tree branches twice at almost every cell.
- **Space:** `O(m + n)` for the recursion stack.

This recomputes the same subproblems (the count for a given cell) exponentially
many times, which is exactly the redundancy DP removes.

## Optimal Approach (Dynamic Programming on Grid)

Let `dp[i][j]` be the number of distinct paths from the start `(0, 0)` to cell
`(i, j)` using only right and down moves.

**Recurrence.** To arrive at `(i, j)` the robot's final move was either from the
cell above `(i-1, j)` or from the cell to the left `(i, j-1)`. These two arrival
routes are disjoint and cover every path, so:

```
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

**Base cases.** Any cell in the first row can only be reached by moving right the
whole way, and any cell in the first column only by moving down the whole way, so
`dp[0][j] = 1` and `dp[i][0] = 1`. Also `dp[0][0] = 1`.

**Why it is correct.** The moves are monotone (row and column indices never
decrease), so the dependency graph is acyclic and every path to `(i, j)` passes
through exactly one of its two predecessors as its last step. Summing the two
predecessor counts therefore counts each path once and only once. Filling the table
in increasing row/column order guarantees both predecessors are ready before we use
them.

**Step by step (m = 3, n = 2):**

```
dp:
1  1
1  2
1  3
```

The bottom-right cell holds `3`, matching Example 2.

**Reference implementation:**

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]   # dp[j] (above) + dp[j-1] (left)
        return dp[-1]
```

- **Time:** `O(m * n)` — one O(1) update per cell.
- **Space:** `O(n)` using a single rolling row (`O(m * n)` for the full table).

**Closed-form bonus.** The answer also equals the binomial coefficient
`C(m + n - 2, m - 1)`, since a path is a fixed multiset of `m - 1` downs and
`n - 1` rights, but the DP formulation is what generalizes to the harder variants.

## Key Insights & Edge Cases

- **First row / first column are all 1s.** Forgetting to seed them is the most
  common bug; the recurrence relies on those base values.
- **`m = 1` or `n = 1`.** There is exactly one path (a straight line). The rolling
  array `[1] * n` already returns `1` because the inner loop never runs.
- **Rolling array trick.** `dp[j] += dp[j - 1]` works in place because after the
  update, `dp[j]` holds the *new* row value (which plays the role of "left") and the
  not-yet-updated `dp[j]` played the role of "above".
- **Overflow.** In Python integers are unbounded; in fixed-width languages note the
  guarantee that the answer fits in about 31 bits (`<= 2 * 10^9`).
