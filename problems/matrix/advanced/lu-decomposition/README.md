# LU Decomposition

**Category:** Matrix / Advanced

## What it is

LU Decomposition factors a square matrix `A` into the product of a **L**ower
triangular matrix `L` and an **U**pper triangular matrix `U`:

```
A = L · U
```

In the common **Doolittle** form, `L` has 1's on its diagonal:

```
| a11 a12 a13 |     | 1    0   0 |   | u11 u12 u13 |
| a21 a22 a23 |  =  | l21  1   0 | · |  0  u22 u23 |
| a31 a32 a33 |     | l31 l32  1 |   |  0   0  u33 |
```

The factorization is essentially **Gaussian elimination remembered**: `U` is the
row-echelon result of elimination, and `L` stores the multipliers used to zero
out each column. In practice, real solvers use **partial pivoting** and produce
`PA = LU`, where `P` is a permutation matrix that swaps rows to avoid dividing by
small (or zero) pivots.

## When to reach for it

The killer feature is **amortization across many right-hand sides**. Factoring
costs `O(n³)`, but once you have `L` and `U`, each of these becomes only `O(n²)`:

- **Solve `Ax = b`** — forward-substitute `Ly = b`, then back-substitute `Ux = y`.
- **Solve `Ax = b_1, b_2, …, b_m`** — reuse the *same* `L`, `U` for every `b`.
- **Determinant** — `det(A) = (±1) · Π u_ii` (the sign comes from row swaps).
- **Matrix inverse** — solve `AX = I` column by column.

If you only ever solve one system once, plain Gaussian elimination is equivalent.
LU wins the moment you need to solve against multiple `b` vectors, invert, or
compute a determinant, because the expensive `O(n³)` work is done exactly once.

## Complexity

| Operation | Time | Space |
|---|---|---|
| Factor `A = LU` (once) | `O(n³)` | `O(n²)` (can overwrite `A` in place) |
| Forward + back substitution (per `b`) | `O(n²)` | `O(n)` |
| Solve `m` right-hand sides | `O(n³ + m·n²)` | `O(n²)` |
| Determinant | `O(n³)` | `O(n²)` |
| Inverse | `O(n³)` | `O(n²)` |

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Doolittle LU Decomposition](problem-01-doolittle-lu-decomposition/PROBLEM.md) | Factor a matrix into `L` and `U` triangular matrices | Easy |
| 2 | [Determinant via LU](problem-02-determinant-via-lu/PROBLEM.md) | Compute a determinant as the product of `U`'s pivots | Easy |
| 3 | [Solve a Linear System](problem-03-solve-linear-system/PROBLEM.md) | Solve `Ax = b` with forward + back substitution | Medium |
| 4 | [Multiple Right-Hand Sides](problem-04-multiple-right-hand-sides/PROBLEM.md) | Reuse one factorization to solve many `b` vectors | Medium |
| 5 | [Matrix Inverse via LU](problem-05-matrix-inverse-via-lu/PROBLEM.md) | Invert a matrix by solving `AX = I` column by column | Hard |

## Suggested order

Work top to bottom. Problem 1 builds the factorization you will reuse in every
later problem; Problems 3–5 are all just substitution steps layered on top of it.
