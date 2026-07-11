# Solution — Multiple Right-Hand Sides with One LU

## Brute Force

Solve each system independently with full Gaussian elimination:

```python
for b in B:
    x = gaussian_eliminate(A, b)   # O(n^3) each
```

This re-does the identical elimination work on `A` for every right-hand side.

- **Time:** `O(m · n³)`
- **Space:** `O(n²)`

For `m = n`, that is `O(n⁴)` — an entire order worse than necessary.

## Optimal Approach (LU Decomposition)

### Idea

The elimination on `A` is *independent of `b`*. So do it once, capture the result
as `A = LU`, and then each right-hand side is just two cheap triangular solves.

```
Factor A = LU                       # O(n^3), ONCE
for each b_j:
    solve L y = b_j   (forward)     # O(n^2)
    solve U x_j = y   (back)        # O(n^2)
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


def solve_multiple(A, B):
    L, U = lu_decompose(A)                 # factor ONCE
    solutions = []
    for b in B:
        y = forward_sub(L, b)
        solutions.append(back_sub(U, y))
    return solutions
```

The key structural point: `lu_decompose(A)` is called **outside** the loop.

### Why it is correct

For each `j`, the pair of substitutions solves `L(U x_j) = b_j`, i.e.
`A x_j = b_j` — exactly as in Problem 3. Reusing `L` and `U` is valid because they
depend only on `A`, which never changes across right-hand sides.

### Complexity

- **Factorization:** `O(n³)`, once.
- **Per right-hand side:** `O(n²)`.
- **Total:** `O(n³ + m · n²)`.
- **Space:** `O(n²)` for the factors, plus `O(m · n)` for the outputs.

Compared to `O(m · n³)` for the brute force, the speedup factor is roughly
`min(m, n)` — large whenever you have many right-hand sides.

## Key Insights & Edge Cases

- **This is the whole point of LU.** If you only ever solve one system, plain
  Gaussian elimination is equivalent. LU pays off precisely when the same `A` is
  reused, which is extremely common: time-stepping simulations, Newton iterations
  (constant Jacobian), and column-by-column inversion (Problem 5).
- **Factor once — the classic bug is re-factoring inside the loop,** which throws
  away the entire advantage and returns you to `O(m·n³)`.
- **Batching as a matrix solve.** Stacking the `b_j` as columns of a matrix `B`
  and solving `A X = B` is the same computation; libraries expose it directly
  (e.g. `scipy.linalg.lu_solve` given a stored factorization, or
  `numpy.linalg.solve(A, B)` with a 2-D RHS).
- **Inverse alternative is inferior.** Precomputing `A⁻¹` and forming `A⁻¹ b_j` is
  also `O(n³ + m·n²)` but less numerically stable, so prefer LU + substitution.
- **Empty `B`.** Return `[]`; the factorization can be skipped if `m = 0`.
- **Stability.** Use partial pivoting in the factorization and permute each `b_j`
  by the same row permutation before the forward solve.
