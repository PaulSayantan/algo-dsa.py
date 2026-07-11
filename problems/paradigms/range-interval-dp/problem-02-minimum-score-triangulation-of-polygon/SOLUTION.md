# Minimum Score Triangulation of Polygon — Solution

## Brute Force

Recursively fix the edge `(i, j)` and try every third vertex `k` to form a
triangle, recursing on both sub-polygons `(i, k)` and `(k, j)`. Without
memoization the number of triangulations of an `n`-gon is the Catalan number
`C(n-2)`, which grows exponentially.

- **Time:** `O(Catalan(n)) ≈ O(4^n / n^{1.5})`.
- **Space:** `O(n)` recursion depth.

## Optimal Approach (Range / Interval DP)

The key modeling insight: instead of thinking about diagonals, think about the
**fixed base edge** `(i, j)` of a sub-polygon that spans vertices `i, i+1, …, j`
(in order). In *any* triangulation of that sub-polygon, the edge `(i, j)` belongs
to exactly one triangle, whose third vertex (the **apex**) is some `k` with
`i < k < j`. That triangle splits the sub-polygon into:

- the sub-polygon on vertices `i..k` (base edge `(i, k)`), and
- the sub-polygon on vertices `k..j` (base edge `(k, j)`),

which are independent subproblems.

> `dp[i][j]` = minimum score to triangulate the sub-polygon spanned by vertices
> `i, i+1, …, j`.

**Recurrence** (split by the apex `k`):
```
dp[i][j] = min over k in (i, j) of
           dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
```

**Base case:** when `j == i + 1` there are only two vertices and no triangle to
form, so `dp[i][i+1] = 0`. (Equivalently, any interval of fewer than 3 vertices
scores 0.)

**Why it is correct.** Every triangulation is uniquely decomposed by the apex of
the base edge `(i, j)`; the two resulting sub-polygons share only vertex `k` and
their triangle sets are disjoint, so the total score is the sum of the two
sub-scores plus the apex triangle's product. Taking the min over all valid apexes
explores every triangulation exactly once.

**Iteration order.** Fill by increasing interval length (number of spanned
vertices), since `dp[i][j]` depends on strictly shorter intervals.

```python
class Solution:
    def minScoreTriangulation(self, values):
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):            # gap j - i, from 2 up
            for i in range(0, n - length):
                j = i + length
                best = float("inf")
                for k in range(i + 1, j):
                    best = min(best,
                               dp[i][k] + dp[k][j]
                               + values[i] * values[k] * values[j])
                dp[i][j] = best
        return dp[0][n - 1]
```

- **Time:** `O(n^3)` — `O(n^2)` intervals times `O(n)` apex choices.
- **Space:** `O(n^2)`.

### Trace for `values = [3, 7, 4, 5]`

Only `dp[0][3]` needs a real choice (apex `k in {1, 2}`):
- `k = 1`: `dp[0][1] + dp[1][3] + 3*7*5 = 0 + (7*4*5) + 105 = 140 + 105 = 245`.
- `k = 2`: `dp[0][2] + dp[2][3] + 3*4*5 = (3*7*4) + 0 + 60 = 84 + 60 = 144`.

Minimum is `144`.

## Key Insights & Edge Cases

- This is a **split-point** interval DP: the apex `k` is the split, and the
  base edge `(i, j)` is the "glue" whose triangle cost `values[i]*values[k]*values[j]`
  is paid once per merge.
- Do **not** iterate `i, j` naively — you must go by increasing span so both
  `dp[i][k]` and `dp[k][j]` are ready.
- **`n == 3`** (a single triangle) has no interior apex besides `k = 1`; the
  answer is just `values[0]*values[1]*values[2]`.
- Structurally identical to matrix-chain multiplication and to "minimum cost to
  merge / parenthesize"; recognizing the shared skeleton makes all three easy.
