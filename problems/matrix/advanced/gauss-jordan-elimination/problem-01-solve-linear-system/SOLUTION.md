# Solution — Solve a System of Linear Equations

## Brute Force

For a general dense system there is no genuinely "brute-force" enumeration (the
unknowns are real numbers), but two textbook baselines exist:

- **Cramer's rule.** Compute `det(A)` and, for each `i`, the determinant of `A`
  with column `i` replaced by `b`; then `xᵢ = det(Aᵢ) / det(A)`. Computing `n+1`
  determinants naively is `O(n · n!)` (or `O(n⁴)` if each determinant is itself
  found by elimination). Numerically poor and far too slow.
- **Gaussian elimination + back-substitution.** Reduce `[A | b]` only to *upper
  triangular* form, then substitute from the bottom row upward. This is `O(n³)`
  and is the standard efficient baseline — Gauss–Jordan is a close cousin that
  does slightly more arithmetic but avoids the separate back-substitution pass.

Cramer's-rule complexity: `O(n · n!)` time. Gaussian elimination: `O(n³)` time,
`O(n²)` space.

## Optimal Approach (Gauss–Jordan Elimination)

Form the augmented matrix `M = [A | b]` of size `n × (n+1)`. Then, for each pivot
column `c = 0 … n-1`:

1. **Pivot selection (partial pivoting).** Among rows `c … n-1`, find the row with
   the largest `|M[r][c]|` and swap it into position `c`. This keeps the pivot as
   far from zero as possible, which controls floating-point error growth.
2. **Normalise the pivot row.** Divide row `c` by `M[c][c]` so the pivot becomes
   `1`.
3. **Eliminate the whole column.** For *every* other row `i ≠ c`, subtract
   `M[i][c] × (row c)` from row `i`, so column `c` becomes all zeros except the `1`
   at the pivot.

After processing every column, the left block is the identity matrix `I`, so the
system reads `I·x = (last column)`, i.e. the final column *is* `x`.

```python
def solve_linear_system(A, b):
    n = len(A)
    # Build the augmented matrix [A | b] as floats.
    M = [[float(A[i][j]) for j in range(n)] + [float(b[i])] for i in range(n)]

    for c in range(n):
        # 1) partial pivoting: largest-magnitude entry in column c
        piv = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[piv] = M[piv], M[c]

        # 2) normalise the pivot row so M[c][c] == 1
        pv = M[c][c]
        M[c] = [v / pv for v in M[c]]

        # 3) eliminate column c from every other row
        for i in range(n):
            if i != c and M[i][c] != 0.0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[c][j] for j in range(n + 1)]

    return [M[i][n] for i in range(n)]
```

**Why it is correct.** Each of the three elementary row operations (row swap,
scaling a row by a non-zero constant, adding a multiple of one row to another)
preserves the solution set of the linear system. When `A` is non-singular the RREF
of `[A | b]` is exactly `[I | x]`, and `I·x = x` says the augmented column holds
the unique solution.

**Complexity.** The outer loop runs `n` times; each iteration touches `O(n)` rows
of length `O(n)`, giving `O(n³)` time. Storage is the `n × (n+1)` augmented matrix,
`O(n²)` space.

## Key Insights & Edge Cases

- **Partial pivoting is not optional in floating point.** Skipping it can turn a
  perfectly solvable system into garbage when a pivot is tiny (dividing by
  `1e-15`). Always swap in the largest-magnitude candidate.
- **`n = 1`.** The system is `a·x = b`, so `x = b / a`; the general code handles
  this with no special case.
- **Read off, don't back-substitute.** The payoff of Gauss–Jordan (vs. plain
  Gaussian elimination) is that after the loop the answer is literally the last
  column — no second pass.
- **Singular `A`.** This problem guarantees `A` is non-singular, but in general a
  pivot column can be all (near-)zero. Detect `|pivot| < eps` and treat the system
  as singular (see Problem 3 for the full classification).
- **Integer-friendliness.** If you need exact answers rather than floats, run the
  same steps with `fractions.Fraction`; then "largest magnitude" pivoting can be
  replaced by "first non-zero" pivoting since there is no rounding error.
