# Maximal Square — Solution

## Brute Force

For every cell treat it as the top-left corner of a candidate square, and for each
candidate side length expand and check that every cell in the square is `1`.

```python
best = 0
for i in range(m):
    for j in range(n):
        side = 0
        while (i + side < m and j + side < n
               and all_ones(i, j, side + 1)):  # scan the (side+1) x (side+1) block
            side += 1
        best = max(best, side)
return best * best
```

- **Time:** `O(m * n * min(m, n)^2)` — for each of `m*n` corners you try up to
  `min(m, n)` side lengths and re-scan an area up to `min(m, n)^2`.
- **Space:** `O(1)` extra.

This re-verifies overlapping regions repeatedly; DP reuses the work by remembering
the best square that ends at each cell.

## Optimal Approach (Dynamic Programming on Grid)

Let `dp[i][j]` be the **side length of the largest all-ones square whose
bottom-right corner is exactly `(i, j)`**.

**Recurrence.**

```
dp[i][j] = 0                                              if matrix[i][j] == '0'
dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])  if matrix[i][j] == '1'
```

**Base cases.** For the first row and first column, `dp[i][j] = 1` when the cell is
`'1'` (a lone cell can only anchor a 1x1 square), else `0`.

**Why it is correct.** Suppose `matrix[i][j] == '1'`. A square of side `k` ending at
`(i, j)` exists iff squares of side at least `k - 1` end at each of the three
neighbors: directly above `(i-1, j)`, directly left `(i, j-1)`, and diagonally
`(i-1, j-1)`. Intuitively, the top and left neighbors guarantee full columns/rows of
ones reaching back `k-1` cells, and the diagonal neighbor guarantees the interior
`(k-1) x (k-1)` block is solid; the largest square we can *guarantee* is therefore
limited by the **smallest** of the three neighbor squares, hence `1 + min(...)`. If
any neighbor supports only a small square, it caps the current one. The answer is
`max(dp)^2` because `dp` stores side lengths and we want area.

**Step by step (Example 1), computing the `dp` side-length table:**

```
matrix                    dp
1 0 1 0 0                 1 0 1 0 0
1 0 1 1 1        ->        1 0 1 1 1
1 1 1 1 1                  1 1 1 2 2
1 0 0 1 0                  1 0 0 1 0
```

The maximum `dp` entry is `2` (at row 2, column 3 or 4), so the area is
`2 * 2 = 4`, matching the expected output. For instance
`dp[2][3] = 1 + min(dp[1][3]=1, dp[2][2]=1, dp[1][2]=1) = 2`.

**Reference implementation (O(n) space):**

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        prev = [0] * (n + 1)   # dp for the previous row, shifted by 1
        best = 0
        for row in matrix:
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if row[j - 1] == "1":
                    # curr[j-1]=left, prev[j]=above, prev[j-1]=diagonal
                    curr[j] = 1 + min(curr[j - 1], prev[j], prev[j - 1])
                    best = max(best, curr[j])
            prev = curr
        return best * best
```

- **Time:** `O(m * n)`.
- **Space:** `O(n)` with two rolling rows (`O(m * n)` for the full table). The extra
  `+1` column is a sentinel so the first real column has a zero "left/diagonal".

## Key Insights & Edge Cases

- **Return the area, not the side.** A very common mistake is returning `best`
  instead of `best * best`.
- **The three-neighbor `min` is the crux.** Using only `min(above, left)` (dropping
  the diagonal) over-counts and is wrong — the diagonal ensures the interior is
  filled.
- **Entries are characters.** Compare against `'1'` / `'0'`, not integers.
- **All zeros / single cell.** A matrix with no `'1'` returns `0`; a single `'1'`
  returns `1`.
- **Maximal *rectangle* is different.** That harder problem (LeetCode 85) needs a
  histogram/stack approach, not this square recurrence.
