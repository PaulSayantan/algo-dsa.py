# Solution — Matrix Inverse via LU

## Brute Force

### Option A — Adjugate / cofactor formula

`A⁻¹ = adj(A) / det(A)`, where each entry of the adjugate is a signed
`(n-1)×(n-1)` minor. Computing `n²` cofactors by expansion is `O(n²·n!)` —
astronomically slow.

### Option B — Gauss–Jordan on `[A | I]`

Augment `A` with the identity and row-reduce until the left block becomes `I`; the
right block becomes `A⁻¹`. This is a perfectly good `O(n³)` method. Its
shortcoming relative to LU is that it does not leave you with a reusable
factorization, and it is essentially LU without the intermediate structure being
saved.

- **Time:** `O(n²·n!)` (adjugate) or `O(n³)` (Gauss–Jordan)
- **Space:** `O(n²)`

## Optimal Approach (LU Decomposition)

### Idea

`A · A⁻¹ = I`. Splitting the identity into its columns `e_0, …, e_{n-1}`, the
`j`-th column of `A⁻¹` is the solution of

```
A x_j = e_j
```

That is `n` systems sharing the same `A` — the multiple-RHS problem (Problem 4)
with the identity columns as right-hand sides. Factor `A` once and back-solve `n`
times:

```
Factor A = LU                          # O(n^3), ONCE
for j in 0 .. n-1:
    e_j = j-th column of I
    y   = forward_sub(L, e_j)          # O(n^2)
    x_j = back_sub(U, y)               # O(n^2)
    place x_j as column j of the result
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


def forward_sub(L, b):
    n = len(b)
    y = [0.0] * n
    for i in range(n):
        y[i] = b[i] - sum(L[i][k] * y[k] for k in range(i))
    return y


def back_sub(U, y):
    n = len(y)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = sum(U[i][k] * x[k] for k in range(i + 1, n))
        x[i] = (y[i] - s) / U[i][i]
    return x


def inverse(A):
    n = len(A)
    L, U = lu_decompose(A)                       # factor ONCE
    cols = []
    for j in range(n):
        e = [1.0 if i == j else 0.0 for i in range(n)]
        cols.append(back_sub(U, forward_sub(L, e)))
    # cols[j] is column j of the inverse; transpose into row-major form.
    return [[cols[j][i] for j in range(n)] for i in range(n)]
```

### Worked example (Example 1)

`A = [[1, 2], [3, 4]]`.

- Factor: `L = [[1, 0], [3, 1]]`, `U = [[1, 2], [0, -2]]`.
- Column `j = 0`, `e_0 = [1, 0]`: forward gives `y = [1, -3]`; back gives
  `x_0 = [-2, 1.5]`.
- Column `j = 1`, `e_1 = [0, 1]`: forward gives `y = [0, 1]`; back gives
  `x_1 = [1, -0.5]`.
- Assemble columns: `A⁻¹ = [[-2, 1], [1.5, -0.5]]`. Check `A·A⁻¹ = I`. ✓

### Why it is correct

Stacking the column equations `A x_j = e_j` side by side gives `A · [x_0 … x_{n-1}]
= [e_0 … e_{n-1}] = I`, so the matrix whose columns are the `x_j` is by definition
`A⁻¹`. Each `x_j` is obtained by the same correct triangular-solve argument as in
Problem 3.

### Complexity

- **Factorization:** `O(n³)`, once.
- **`n` back-solves:** `O(n · n²) = O(n³)`.
- **Overall:** `O(n³)` — asymptotically the same as one factorization, so
  inversion is only a constant factor more expensive than a single solve.
- **Space:** `O(n²)`.

A useful optimization: because `e_j` has zeros above its `1`, forward substitution
`L y = e_j` produces `y[i] = 0` for `i < j`, so the forward pass for column `j`
can start at row `j`. This roughly halves the substitution work but does not
change the `O(n³)` order.

## Key Insights & Edge Cases

- **Prefer solving over inverting.** To solve `A x = b`, use Problem 3 directly —
  do **not** compute `A⁻¹` and multiply. The explicit inverse costs more and is
  less numerically stable. Compute `A⁻¹` only when you truly need the inverse
  itself (e.g. covariance matrices, some closed-form expressions).
- **The inverse is `n` shared-`A` solves.** Recognizing this reduces the problem
  to Problem 4 and reuses one factorization for all `n` columns.
- **Singular matrices have no inverse.** If a pivot `U[i][i]` is (numerically)
  zero, `A` is singular and `inverse` should signal failure rather than divide by
  zero.
- **Watch the transpose.** The solves produce the *columns* of `A⁻¹`; assembling
  them requires placing `x_j` into column `j` (a transpose of the list of solution
  vectors), a common off-by-orientation bug.
- **`n = 1`.** `A⁻¹ = [[1 / A[0][0]]]`.
- **Stability.** Use partial pivoting; permute each identity column by the row
  permutation before forward substitution.
