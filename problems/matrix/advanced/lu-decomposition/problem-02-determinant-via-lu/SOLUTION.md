# Solution — Determinant via LU Decomposition

## Brute Force

The textbook definition of the determinant is the Leibniz formula / cofactor
(Laplace) expansion:

```
det(A) = Σ_σ sign(σ) · Π_i A[i][σ(i)]
```

Expanding along a row recursively gives the recurrence `T(n) = n · T(n-1) + O(n)`,
which is `O(n!)`. A `13×13` matrix already needs billions of operations, and a
`25×25` matrix is effectively impossible.

- **Time:** `O(n!)`
- **Space:** `O(n²)` (or `O(n)` extra with careful recursion)

## Optimal Approach (LU Decomposition)

### The core fact

The determinant is multiplicative: `det(XY) = det(X)·det(Y)`. Factor `A` with
partial pivoting as `PA = LU`. Then:

```
det(P) · det(A) = det(L) · det(U)
```

- `det(L) = 1` — `L` is unit lower triangular, so its diagonal is all 1's, and
  the determinant of a triangular matrix is the product of its diagonal.
- `det(U) = Π_i U[i][i]` — same triangular-determinant fact.
- `det(P) = (-1)^S`, where `S` is the number of row interchanges. A permutation
  matrix is a product of transpositions; each swap flips the determinant sign.

Because `det(P) = ±1` is its own reciprocal, rearranging gives:

```
det(A) = (-1)^S · Π_i U[i][i]
```

### Step-by-step

1. Run LU factorization with **partial pivoting**: at column `k`, swap the pivot
   row with the row having the largest `|U[i][k]|`. Count each swap in `S`.
2. If any pivot `U[k][k]` is (numerically) zero, the matrix is singular — return
   `0.0`.
3. Multiply the diagonal of `U`: `p = U[0][0] · U[1][1] · … · U[n-1][n-1]`.
4. Return `(-1)^S · p`.

### Reference implementation

```python
def determinant(A):
    n = len(A)
    U = [row[:] for row in A]
    sign = 1
    for k in range(n):
        # Partial pivoting: pick the largest-magnitude entry in column k.
        pivot_row = max(range(k, n), key=lambda i: abs(U[i][k]))
        if abs(U[pivot_row][k]) < 1e-12:
            return 0.0                      # singular: a full zero column
        if pivot_row != k:
            U[k], U[pivot_row] = U[pivot_row], U[k]
            sign = -sign                    # each swap flips the sign
        for i in range(k + 1, n):
            m = U[i][k] / U[k][k]
            for j in range(k, n):
                U[i][j] -= m * U[k][j]
    det = float(sign)
    for i in range(n):
        det *= U[i][i]
    return det
```

Note we do not even need to materialize `L` — only the pivots of `U` and the swap
count matter for the determinant.

### Why it is correct

Each elimination step "row_i ← row_i − m·row_k" is an *add-a-multiple-of-another-
row* operation, which **does not change the determinant**. Each row swap
multiplies the determinant by `−1`. So after elimination, `det(A)` equals
`(−1)^S · det(U)`, and `det(U)` is the product of its diagonal. This is precisely
the LU identity above, and it is far more numerically stable than cofactor
expansion.

### Complexity

- **Time:** `O(n³)` for the elimination, plus `O(n)` for the final product.
- **Space:** `O(n²)` for the working copy `U` (or `O(1)` extra if `A` may be
  overwritten).

## Key Insights & Edge Cases

- **Do not forget the sign.** The single most common bug is dropping `(-1)^S`.
  With partial pivoting, swaps are frequent, so the sign matters constantly.
- **Singular matrices return 0.** If a whole pivot column is zero, elimination
  cannot proceed and `det = 0`; guard against dividing by a ~0 pivot.
- **Floating-point zero.** Use a tolerance (`1e-12`) rather than `== 0` to decide
  singularity, since rounding rarely produces exact zeros.
- **`n = 1`.** `det([[a]]) = a`, with `S = 0`.
- **Overflow / underflow.** For large `n` the product of pivots can overflow or
  underflow. Production code often returns the *log-determinant*
  `Σ log|U[i][i]|` together with the sign to stay in range.
- **Reusing an existing factorization.** If you already factored `A` for solving
  systems, the determinant is essentially free — just multiply `U`'s diagonal.
