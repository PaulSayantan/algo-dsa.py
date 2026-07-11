# Count Square Submatrices with All Ones — Solution

## Brute Force

Enumerate every possible square: pick a top-left corner `(i, j)` and a side `k`, then verify
all `k * k` cells are `1`. Count the ones that pass.

- **Time:** `O(m * n * min(m, n))` if you accelerate each check with a 2-D prefix-sum table
  (each square-sum query becomes `O(1)`; a square of side `k` is all-`1` iff its sum is
  `k * k`). Without prefix sums it degrades to roughly `O(m * n * min(m, n)^3)`.
- **Space:** `O(m * n)` for the prefix-sum table.

## Optimal Approach (Largest Square DP, summed)

The key observation ties this directly to Maximal Square (Problem 1):

> If `dp[i][j]` is the side of the **largest** all-`1` square ending at `(i, j)`, then there
> are **exactly `dp[i][j]` all-`1` squares whose bottom-right corner is `(i, j)`** — one of
> each side `1, 2, ..., dp[i][j]`.

**Why.** Every all-`1` square with bottom-right corner `(i, j)` has some side `s` with
`1 <= s <= dp[i][j]`, and conversely each such `s` yields exactly one square (its position is
pinned by the corner). So the squares ending at `(i, j)` are in bijection with
`{1, ..., dp[i][j]}`, giving `dp[i][j]` of them. Because every square has a unique
bottom-right corner, summing `dp[i][j]` over all cells counts every square exactly once with
no double counting.

**Recurrence** (identical to Maximal Square):

```
dp[i][j] = 0                                             if matrix[i][j] == 0
dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 if matrix[i][j] == 1
```

**Step by step.**
1. Keep a running `total = 0`.
2. Fill `dp` row by row using the recurrence (borders: `dp = matrix value`).
3. Add each `dp[i][j]` to `total`.
4. Return `total`.

```python
def countSquares(matrix):
    n = len(matrix[0])
    prev = [0] * n
    total = 0
    for row in matrix:
        curr = [0] * n
        for j in range(n):
            if row[j] == 1:
                curr[j] = 1 if j == 0 else min(prev[j], curr[j - 1], prev[j - 1]) + 1
                total += curr[j]
        prev = curr
    return total
```

- **Time:** `O(m * n)`.
- **Space:** `O(n)` with a rolling row (or `O(m * n)` with a full table).

## Key Insights & Edge Cases

- **Same DP, different aggregation.** Problem 1 takes the `max` of `dp` (and squares it);
  this problem takes the `sum`. Recognizing that one table answers both is the core insight.
- **Each square counted once.** The bottom-right-corner bijection is what prevents
  double-counting; you never need to dedupe.
- **Integer grid here.** Unlike Maximal Square (characters), this grid holds ints, so compare
  against `1`, not `'1'`.
- **All zeros / single cell.** All-zero grids give `0`; a single `1` gives `1` — both fall
  straight out of the recurrence.
- **Overflow.** Not a concern in Python; in fixed-width languages the count can reach
  `~O(m * n * min(m, n))`, so use a 64-bit accumulator.
