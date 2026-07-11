# Solution — Doolittle LU Decomposition

## Brute Force

There is no meaningfully cheaper "brute force" for producing `L` and `U`: you
could set up the `n²` defining equations of `A = LU` and solve them, but doing so
naively (treating each `l_ij` and `u_ij` as an unknown and back-substituting in an
unstructured order) still costs `O(n³)` arithmetic and is far more error-prone.

- **Time:** `O(n³)`
- **Space:** `O(n²)`

The structured elimination below achieves the same `O(n³)` with clean, ordered
updates, so it is the approach everyone actually uses.

## Optimal Approach (LU Decomposition)

### Key identity

Doolittle's method reads off `L` and `U` directly from the `A = LU` equations,
processing entries in the right order. Because `L` is unit lower triangular and
`U` is upper triangular, for each `(i, j)`:

```
A[i][j] = sum_{k} L[i][k] * U[k][j]
```

Solving these in the order "row of U, then column of L, alternating" gives the
familiar Gaussian-elimination update. Equivalently, and more intuitively:

1. Start with `U = A` (a working copy) and `L = I`.
2. For each pivot column `k = 0 … n-1`:
   - The pivot is `U[k][k]` (assumed non-zero — no pivoting in this problem).
   - For each row `i` below the pivot (`i = k+1 … n-1`):
     - Compute the multiplier `m = U[i][k] / U[k][k]` and store it: `L[i][k] = m`.
     - Subtract `m ×` (pivot row `k`) from row `i`: `U[i][j] -= m * U[k][j]` for
       `j = k … n-1`. This zeroes `U[i][k]`.

After processing all columns, `U` is upper triangular and `L` holds the
multipliers with 1's on the diagonal. By construction `L · U = A`.

### Reference implementation

```python
def lu_decompose(A):
    n = len(A)
    U = [row[:] for row in A]          # working copy, becomes upper triangular
    L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot = U[k][k]                # assumed non-zero (no pivoting here)
        for i in range(k + 1, n):
            m = U[i][k] / pivot
            L[i][k] = m
            for j in range(k, n):
                U[i][j] -= m * U[k][j]  # U[i][k] becomes exactly 0
    return L, U
```

### Why it is correct

Each column-`k` step is a sequence of elementary row operations
"row_i ← row_i − m·row_k". Every such operation is realized by left-multiplying
the current matrix by a lower-triangular elimination matrix `E_ik` whose only
off-diagonal entry is `−m` at position `(i, k)`. After all steps,

```
E · A = U    where E = (product of all elimination matrices)
```

`E` is unit lower triangular, so its inverse `L = E⁻¹` is also unit lower
triangular — and `A = E⁻¹ U = L U`. The beautiful fact that makes Doolittle cheap
is that `L = E⁻¹` is obtained for free: `L[i][k]` is simply the multiplier `m`
that was used, with **no** extra inversion work.

### Complexity

- **Time:** `O(n³)` — the triple nested loop does about `n³/3` multiply-adds.
- **Space:** `O(n²)` for `L` and `U`; can be reduced to overwriting `A` in place
  (store `U` on/above the diagonal and the multipliers of `L` below it).

## Key Insights & Edge Cases

- **`L` is free.** The whole trick is that Gaussian elimination already computes
  the multipliers; storing them instead of discarding them *is* the decomposition.
- **Zero pivot ⇒ failure without pivoting.** If some `U[k][k]` becomes `0` (e.g.
  `A = [[0, 1], [1, 0]]`), plain Doolittle divides by zero. The matrix may still
  be invertible — you just need row swaps (partial pivoting, `PA = LU`). This
  problem guarantees non-zero pivots so you can ignore that case here.
- **Uniqueness.** With the unit-diagonal convention on `L`, the factorization is
  unique when it exists. Other conventions (Crout: unit diagonal on `U`; or
  Cholesky for symmetric positive-definite `A`) just redistribute the diagonal.
- **`n = 1`.** `L = [[1.0]]`, `U = [[a₀₀]]`. The loops simply do nothing.
- **Floating point.** The zeroed entries `U[i][k]` may be a tiny non-zero value
  like `1e-17` due to rounding; comparisons should use a tolerance.
- **In-place variant.** Numerical libraries (LAPACK `getrf`) store both factors
  packed into `A`'s memory and track pivots separately — same `O(n³)`, half the
  storage.
