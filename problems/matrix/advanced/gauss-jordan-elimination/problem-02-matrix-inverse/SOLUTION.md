# Solution — Invert a Matrix

## Brute Force

The classical closed form is the **adjugate / cofactor** formula:

```
A⁻¹ = (1 / det(A)) · adj(A)
```

where `adj(A)` is the transpose of the cofactor matrix. Each of the `n²` cofactors
is itself an `(n-1)×(n-1)` determinant. Computed naively (Laplace expansion) this
is factorial-time, and even with careful reuse it is far worse than elimination.

- **Time:** `O(n · n!)` naively; astronomically slow beyond tiny `n`.
- **Space:** `O(n²)`.

It is also numerically unstable, so it is essentially never used for `n > 3`.

## Optimal Approach (Gauss–Jordan Elimination)

Key idea: the same row operations that turn `A` into `I` will turn `I` into `A⁻¹`.
Concretely, build the `n × 2n` augmented block `[A | I]` and reduce the **left**
block to the identity using Gauss–Jordan. Because a sequence of elementary row
operations is equivalent to left-multiplication by some matrix `E`, and we choose
those operations so that `E·A = I` (hence `E = A⁻¹`), the right block — which
started as `I` — becomes `E·I = A⁻¹`.

Steps, for each pivot column `c = 0 … n-1`:

1. **Find a pivot.** Among rows `c … n-1`, pick the one with the largest
   `|M[r][c]|` and swap it to row `c`. If that maximum magnitude is `≈ 0`, no pivot
   exists in this column ⇒ `A` is **singular** ⇒ return `None`.
2. **Normalise** row `c` by dividing it by `M[c][c]` (pivot becomes `1`).
3. **Eliminate** column `c` from every other row `i ≠ c` by subtracting
   `M[i][c] × (row c)`.

When done, the left block is `I` and the right block is `A⁻¹`.

```python
def invert_matrix(A, eps=1e-9):
    n = len(A)
    # Augmented matrix [A | I]
    M = [[float(A[i][j]) for j in range(n)] +
         [1.0 if j == i else 0.0 for j in range(n)] for i in range(n)]

    for c in range(n):
        # 1) partial pivot
        piv = max(range(c, n), key=lambda r: abs(M[r][c]))
        if abs(M[piv][c]) < eps:
            return None                     # singular
        M[c], M[piv] = M[piv], M[c]

        # 2) normalise pivot row
        pv = M[c][c]
        M[c] = [v / pv for v in M[c]]

        # 3) clear the rest of column c
        for i in range(n):
            if i != c and M[i][c] != 0.0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[c][j] for j in range(2 * n)]

    # right half is the inverse
    return [[M[i][n + j] for j in range(n)] for i in range(n)]
```

**Why it is correct.** Every elementary row operation on `[A | I]` corresponds to
left-multiplying *both* blocks by the same elementary matrix. If the composed
operations reduce `A` to `I`, their product is `A⁻¹`, and applying that same
product to the identity in the right block yields `A⁻¹`. A column with no non-zero
pivot means the rows are linearly dependent, so `det(A) = 0` and no inverse exists.

**Complexity.** `n` pivot columns × `O(n)` rows × `O(n)` work per row (rows now
have length `2n`) = `O(n³)` time, `O(n²)` space.

## Key Insights & Edge Cases

- **Singularity detection is built in.** The single check `|pivot| < eps` at each
  column both drives pivoting and detects non-invertibility — no separate
  determinant computation needed.
- **Choose `eps` sensibly for floats.** With bounded integer inputs a threshold
  like `1e-9` works; for exact results use `fractions.Fraction` and test `pivot == 0`.
- **`n = 1`.** `A = [[a]]` is invertible iff `a ≠ 0`, giving `[[1/a]]`; the general
  code handles it.
- **Don't invert just to solve one system.** If you only need `x = A⁻¹b`, solve
  `Ax = b` directly (Problem 1) — same `O(n³)` but a smaller constant and better
  numerical behaviour than forming the full inverse and multiplying.
- **Reusing an inverse.** Forming `A⁻¹` once pays off when you must solve `Ax = bₖ`
  for many right-hand sides `bₖ` that are not all known up front; each later solve
  is then just an `O(n²)` matrix–vector product.
