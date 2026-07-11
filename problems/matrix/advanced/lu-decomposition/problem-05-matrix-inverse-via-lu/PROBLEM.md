# Matrix Inverse via LU Decomposition

**Difficulty:** Hard

**Source:** Classic numerical linear algebra (CLRS §28.2, "Inverting matrices")

## Description

Given a square, non-singular `n × n` matrix `A`, compute its inverse `A⁻¹`.

The inverse `X = A⁻¹` is defined by `A · X = I`, where `I` is the `n × n` identity
matrix. Reading this column by column: if `e_j` is the `j`-th column of `I` (the
standard basis vector with a `1` in position `j`), and `x_j` is the `j`-th column
of `X`, then

```
A · x_j = e_j     for j = 0 … n-1
```

That is exactly `n` linear systems that share the **same** matrix `A`. So this is
the multiple-right-hand-sides problem (Problem 4) with the identity columns as the
right-hand sides:

1. Factor `A = LU` **once** — `O(n³)`.
2. For each identity column `e_j`, forward + back substitute to get column `x_j` —
   `O(n²)` each, `O(n³)` for all `n` columns.
3. Assemble the `x_j` as the columns of `A⁻¹`.

You may assume `A` is invertible and factors without pivoting.

## Constraints

- `1 <= n <= 150`
- `A` is a square, non-singular matrix with non-zero pivots.
- A tolerance of `1e-6` is acceptable when comparing entries of the inverse.

## Examples

### Example 1

```
Input:  A = [[1, 2],
             [3, 4]]

Output: [[-2.0,  1.0],
         [ 1.5, -0.5]]
```

**Explanation:** `det(A) = 1·4 − 2·3 = -2`, so the `2×2` inverse formula gives
`(1/-2)·[[4, -2], [-3, 1]] = [[-2, 1], [1.5, -0.5]]`. Column-wise: solving
`A x_0 = [1, 0]` gives `[-2, 1.5]`, and `A x_1 = [0, 1]` gives `[1, -0.5]`.
Check: `A · A⁻¹ = I`.

### Example 2

```
Input:  A = [[1, 2, 3],
             [0, 1, 4],
             [5, 6, 0]]

Output: [[-24.0,  18.0,  5.0],
         [ 20.0, -15.0, -4.0],
         [ -5.0,   4.0,  1.0]]
```

**Explanation:** Solving `A x_j = e_j` for `j = 0, 1, 2` produces the three
columns of the inverse shown above. Spot-check the first row of `A · A⁻¹`:
`1·(-24) + 2·20 + 3·(-5) = -24 + 40 - 15 = 1`, and
`1·18 + 2·(-15) + 3·4 = 18 - 30 + 12 = 0`. ✓

## Hint

The inverse is just `n` systems `A x_j = e_j` sharing one matrix — factor with
**LU Decomposition** once, then back-solve against each column of the identity.

## Note

Never invert a matrix only to then solve `A x = b` — solve directly (Problem 3).
Explicit inverses are needed far less often than beginners expect, but when you
genuinely need `A⁻¹`, LU is the standard way to compute it.
