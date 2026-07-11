# Solution — Solve a System of Linear Equations

## Brute Force

For a truly naive approach you could use **Cramer's rule**: compute `det(A)` and, for each
unknown `x_i`, compute the determinant of `A` with column `i` replaced by `b`, then divide.
Computing a determinant by cofactor expansion is `O(n!)`, which is hopeless beyond
`n ~ 10`. Even computing each of the `n+1` determinants by Gaussian elimination is
`O(n^4)` overall and does redundant work.

- **Time:** `O(n * n!)` (cofactor expansion) or `O(n^4)` (determinants via elimination).
- **Space:** `O(n^2)`.

## Optimal Approach (Gaussian Elimination)

Form the **augmented matrix** `M = [A | b]` of size `n x (n+1)`. Reduce it to
upper-triangular row-echelon form, then back-substitute.

### Step by step

1. **Forward elimination.** For each pivot column `col = 0 .. n-1`:
   - **Partial pivoting:** among rows `col .. n-1`, pick the row whose entry in `col` has
     the largest absolute value and swap it into row `col`. This avoids dividing by tiny
     numbers and keeps the computation numerically stable.
   - For every row `r` below the pivot (`r = col+1 .. n-1`), compute the factor
     `f = M[r][col] / M[col][col]` and subtract `f * (pivot row)` from row `r`. After
     this, every entry below the pivot in column `col` is zero.
2. **Back-substitution.** Now `M` is upper-triangular. For `i = n-1 down to 0`:
   ```
   x[i] = (M[i][n] - sum_{j>i} M[i][j] * x[j]) / M[i][i]
   ```

### Why it is correct

Elementary row operations (row swap, scaling, adding a multiple of another row) never
change the solution set of the system — they correspond to left-multiplying `[A|b]` by an
invertible matrix. Because `A` is non-singular, every pivot `M[col][col]` is non-zero after
pivoting, so no division by zero occurs and exactly one solution exists. Back-substitution
then inverts the triangular system uniquely.

### Reference implementation

```python
from typing import List

def solve_linear_system(A: List[List[float]], b: List[float]) -> List[float]:
    n = len(A)
    # Build augmented matrix.
    M = [list(map(float, A[i])) + [float(b[i])] for i in range(n)]

    for col in range(n):
        # Partial pivoting: largest magnitude pivot.
        pivot = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[pivot] = M[pivot], M[col]

        # Eliminate this column from all rows below.
        for r in range(col + 1, n):
            f = M[r][col] / M[col][col]
            for c in range(col, n + 1):
                M[r][c] -= f * M[col][c]

    # Back-substitution.
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = s / M[i][i]
    return x
```

### Complexity

- **Time:** `O(n^3)` — the forward elimination triple loop dominates.
- **Space:** `O(n^2)` for the augmented matrix (in place).

## Key Insights & Edge Cases

- **Partial pivoting is not optional in floating point.** Without it a small pivot can
  blow up rounding error; picking the largest-magnitude candidate keeps the multipliers
  `|f| <= 1`.
- **Reduced row echelon form (Gauss–Jordan)** also eliminates *above* each pivot, letting
  you read the answer directly without back-substitution; it costs a constant factor more.
- **Singular / near-singular matrices:** if after pivoting a pivot is `~0`, the matrix is
  singular — the system has no unique solution. This problem guarantees invertibility, but
  a robust implementation should check `abs(pivot) < eps` and report no/infinite solutions.
- **`n = 1`:** the loop degenerates to `x[0] = b[0] / A[0][0]`.
- **Integer/rational systems:** to avoid floating error entirely, run the same algorithm
  with `fractions.Fraction`; complexity is unchanged asymptotically but arithmetic is
  exact.
