# Maximal Square — Solution

## Brute Force

Try every cell `(i, j)` as the top-left corner and every possible side length `k`. For each
candidate square, scan all `k * k` cells to confirm they are `1`.

- For each of the `O(m * n)` corners you try up to `O(min(m, n))` side lengths, and each
  check scans `O(k^2)` cells.
- **Time:** `O(m * n * min(m, n)^3)` in the naive form (much better with prefix sums, but
  still not the intended solution).
- **Space:** `O(1)` extra (or `O(m * n)` if you precompute a 2-D prefix-sum table to make
  each square check `O(1)`, giving `O(m * n * min(m, n))`).

## Optimal Approach (Largest Square DP)

Define `dp[i][j]` = the side length of the largest all-`1` square whose **bottom-right
corner** sits at cell `(i, j)`.

**Recurrence.** If `matrix[i][j] == '0'`, no square can end there, so `dp[i][j] = 0`.
If `matrix[i][j] == '1'`, then

```
dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
```

**Why it is correct.** A square of side `k+1` ending at `(i, j)` exists iff squares of side
at least `k` end at the cell above (`i-1, j`), the cell to the left (`i, j-1`), and the cell
diagonally up-left (`i-1, j-1`). The `min` of the three tells you the largest common side
those neighbors can all support; adding the current `1` cell extends it by one. If any
neighbor is limited, the whole square is limited — that is exactly what `min` captures. The
diagonal term is essential: without it, an L-shaped region of `1`s could be mistaken for a
full square.

**Step by step.**
1. Initialize the answer `best = 0`.
2. Row 0 and column 0: `dp` equals the cell value (`1` or `0`) since no square larger than 1
   can end on the border.
3. For every interior cell that is `1`, apply the recurrence.
4. Track `best = max(best, dp[i][j])` as you go.
5. Return `best * best` (convert side length to area).

```python
def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    prev = [0] * n           # dp values for the previous row
    best = 0
    for row in matrix:
        curr = [0] * n
        for j in range(n):
            if row[j] == '1':
                if j == 0:
                    curr[j] = 1
                else:
                    curr[j] = min(prev[j], curr[j - 1], prev[j - 1]) + 1
                best = max(best, curr[j])
        prev = curr
    return best * best
```

- **Time:** `O(m * n)` — each cell computed once.
- **Space:** `O(n)` using a rolling one-row array (or `O(m * n)` with a full table).

## Key Insights & Edge Cases

- **Return area, not side.** The DP naturally produces the side length; square it at the end.
  Forgetting this returns the side (a common bug).
- **The diagonal term is the crux.** `min` over three neighbors — up, left, *and* diagonal —
  is what guarantees a full square rather than a partial one.
- **Character vs. int.** The grid holds characters `'0'`/`'1'`, so compare against `'1'`.
- **Borders.** Cells in row 0 or column 0 can only ever host a side-1 square, handled by the
  `j == 0` / first-row base case.
- **Empty / all-zero matrix.** The answer is `0`; the initialization already covers this.
- This is a square-only technique. For a general (possibly non-square) rectangle, use the
  histogram + monotonic-stack approach (see Problem 5).
