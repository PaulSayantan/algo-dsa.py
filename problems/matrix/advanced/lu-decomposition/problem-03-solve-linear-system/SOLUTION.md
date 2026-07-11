# Solution — Solve a Linear System with LU

## Brute Force

### Option A — Cramer's rule

Compute `x_i = det(A_i) / det(A)`, where `A_i` is `A` with column `i` replaced by
`b`. This requires `n + 1` determinants. Even with LU determinants that is
`O(n⁴)`; with cofactor expansion it is `O(n · n!)` — catastrophic.

### Option B — Compute `A⁻¹`, then `x = A⁻¹ b`

Inverting `A` is `O(n³)`, and forming the product is `O(n²)`. This works but is
both slower and *less numerically stable* than solving directly, because the
explicit inverse amplifies rounding error. Forming an inverse just to multiply it
by one vector is wasteful.

- **Time:** `O(n⁴)` (Cramer) or `O(n³)` (explicit inverse)
- **Space:** `O(n²)`

## Optimal Approach (LU Decomposition)

### Idea

Rewrite `A x = b` using the factorization `A = LU`:

```
A x = b   ⇒   (L U) x = b   ⇒   L (U x) = b
```

Introduce an intermediate vector `y = U x`. Then the single dense solve becomes
two **triangular** solves, each of which is trivial:

1. **Forward substitution** — solve `L y = b`. Since `L` is unit lower triangular:
   ```
   y[i] = b[i] - Σ_{k=0}^{i-1} L[i][k] * y[k]
   ```
   (No division needed because `L[i][i] = 1`.)
2. **Back substitution** — solve `U x = y`. Since `U` is upper triangular:
   ```
   x[i] = ( y[i] - Σ_{k=i+1}^{n-1} U[i][k] * x[k] ) / U[i][i]
   ```

### Reference implementation

```python
def lu_decompose(A):
    n = len(A)
    U = [row[:] for row in A]
    L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(k + 1, n):
            m = U[i][k] / U[k][k]
            L[i][k] = m
            for j in range(k, n):
                U[i][j] -= m * U[k][j]
    return L, U


def forward_sub(L, b):          # solve L y = b (unit lower triangular)
    n = len(b)
    y = [0.0] * n
    for i in range(n):
        y[i] = b[i] - sum(L[i][k] * y[k] for k in range(i))
    return y


def back_sub(U, y):             # solve U x = y (upper triangular)
    n = len(y)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = sum(U[i][k] * x[k] for k in range(i + 1, n))
        x[i] = (y[i] - s) / U[i][i]
    return x


def solve(A, b):
    L, U = lu_decompose(A)
    y = forward_sub(L, b)
    return back_sub(U, y)
```

### Worked example (Example 1)

`A = [[4, 3], [6, 3]]`, `b = [10, 12]`.

- Factor: `L = [[1, 0], [1.5, 1]]`, `U = [[4, 3], [0, -1.5]]`.
- Forward `L y = b`: `y[0] = 10`; `y[1] = 12 − 1.5·10 = −3`.
- Back `U x = y`: `x[1] = −3 / −1.5 = 2`; `x[0] = (10 − 3·2) / 4 = 1`.
- Solution `x = [1, 2]`. Check: `4·1 + 3·2 = 10`, `6·1 + 3·2 = 12`. ✓

### Why it is correct

`y = U x` is a definition, and substituting it back gives `L y = L (U x) = A x =
b`. So any `x` we recover satisfies the original system. Triangular solves are
exact (up to rounding) because at each step every already-solved unknown is known,
leaving exactly one unknown per equation.

### Complexity

- **Factorization:** `O(n³)`, done once.
- **Forward + back substitution:** `O(n²)` total.
- **Overall:** `O(n³)` — same order as Gaussian elimination, but the factorization
  is *reusable* (see Problem 4).
- **Space:** `O(n²)` for `L`, `U`; `O(n)` for the vectors.

## Key Insights & Edge Cases

- **Never invert to solve.** `x = A⁻¹ b` is slower and less stable; two triangular
  solves are the right tool.
- **Order matters:** forward *then* back. `L y = b` must be solved first because
  `y` is the RHS of the second system.
- **Unit diagonal saves a division.** In the Doolittle convention `L[i][i] = 1`,
  so forward substitution needs no division; back substitution divides by
  `U[i][i]` (the pivots), which are guaranteed non-zero for a non-singular `A`.
- **Singular / zero pivot.** If `U[i][i] = 0`, `A` is singular and no unique
  solution exists — real code detects this during factorization (and uses partial
  pivoting to avoid a spurious zero pivot from an unlucky row order).
- **`n = 1`.** `x = [b[0] / A[0][0]]`.
- **Stability.** Add partial pivoting (`PA = LU`) for production: solve
  `L y = P b`, then `U x = y`. Reordering `b` by the same permutation as the rows
  keeps the system equivalent.
