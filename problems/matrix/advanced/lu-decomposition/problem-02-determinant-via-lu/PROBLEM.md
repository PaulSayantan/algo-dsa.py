# Determinant via LU Decomposition

**Difficulty:** Easy

**Source:** Classic numerical linear algebra (CLRS §28.1; standard determinant-by-elimination)

## Description

Given a square `n × n` matrix `A`, compute its determinant `det(A)`.

The naive cofactor-expansion definition of the determinant runs in `O(n!)` time,
which is hopeless beyond tiny matrices. Instead, factor `A` (with partial
pivoting) as `PA = LU`, where `P` is a permutation matrix. Then use the fact that
the determinant of a triangular matrix is the product of its diagonal entries:

```
det(A) = det(P)⁻¹ · det(L) · det(U)
       = (-1)^S · Π_{i} U[i][i]
```

Here `S` is the number of **row swaps** performed during pivoting (`det(P) = ±1`,
and it is its own inverse), and `det(L) = 1` because `L` is unit lower triangular.
So the determinant is simply the product of the pivots on `U`'s diagonal, with a
sign flip for every row swap.

Return the determinant as a float.

## Constraints

- `1 <= n <= 200`
- `A` is a square matrix of real numbers.
- The answer fits in double-precision floating point; a tolerance of `1e-6` is
  acceptable when comparing.
- If `A` is singular, the determinant is `0` (a pivot column will be entirely
  zero, so the product of pivots is `0`).

## Examples

### Example 1

```
Input:  A = [[4, 3],
             [6, 3]]

Output: -6.0
```

**Explanation:** LU (no swaps needed) gives `U = [[4, 3], [0, -1.5]]`, so
`det(A) = 4 · (-1.5) = -6`. Cross-checking with the `2×2` formula:
`4·3 − 3·6 = 12 − 18 = -6`.

### Example 2

```
Input:  A = [[ 2, -1, -2],
             [-4,  6,  3],
             [-4, -2,  8]]

Output: 24.0
```

**Explanation:** Without any row swaps the pivots are `2, 4, 3`, so
`det(A) = (-1)^0 · (2 · 4 · 3) = 24`.

## Constraints on the sign

The sign factor `(-1)^S` is essential. If your pivoting logic swaps rows to place
the largest-magnitude entry on the diagonal, you **must** track how many swaps
occurred and multiply the pivot product by `-1` for each one, or the sign of your
determinant will be wrong.

## Hint

Factor the matrix with **LU Decomposition** and multiply the diagonal of `U` — the
whole `O(n!)` determinant collapses to a single `O(n)` product of the pivots
(remember the sign from any row swaps).
