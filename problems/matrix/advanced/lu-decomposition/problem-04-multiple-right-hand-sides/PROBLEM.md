# Solve Multiple Right-Hand Sides with One LU Factorization

**Difficulty:** Medium

**Source:** Classic numerical linear algebra (the headline use case for LU factorization)

## Description

Given a square, non-singular `n × n` matrix `A` and a list of `m` right-hand-side
vectors `B = [b_1, b_2, …, b_m]` (each of length `n`), solve **every** system

```
A · x_j = b_j     for j = 1 … m
```

and return the list of solution vectors `[x_1, x_2, …, x_m]`.

This is the scenario LU Decomposition was built for. The matrix `A` is fixed; only
the right-hand side changes. If you re-ran Gaussian elimination from scratch for
each `b_j`, you would pay `O(n³)` **per** system — `O(m·n³)` total. Instead:

- Factor `A = LU` **once** — `O(n³)`.
- For each `b_j`, run forward + back substitution — `O(n²)` each.

Total cost drops to `O(n³ + m·n²)`. When `m` is comparable to or larger than `n`,
this is a dramatic saving.

You may assume `A` factors without pivoting (all pivots non-zero).

## Constraints

- `1 <= n <= 200`
- `1 <= m <= 500`
- `A` is a square, non-singular matrix with non-zero pivots.
- Each `b_j` has exactly `n` real entries.
- A tolerance of `1e-6` is acceptable when comparing solution entries.

## Examples

### Example 1

```
Input:  A = [[2, 1],
             [1, 3]]
        B = [[5, 10],
             [3, 4]]

Output: [[1.0, 3.0],
         [1.0, 1.0]]
```

**Explanation:** `A` is factored once. For `b_1 = [5, 10]` the solution is
`x_1 = [1, 3]` (check: `2·1 + 1·3 = 5`, `1·1 + 3·3 = 10`). For `b_2 = [3, 4]` the
solution is `x_2 = [1, 1]` (check: `2·1 + 1·1 = 3`, `1·1 + 3·1 = 4`). The same
`L` and `U` were reused for both.

### Example 2

```
Input:  A = [[1, 1,  1],
             [0, 2,  5],
             [2, 5, -1]]
        B = [[6, -4, 27],
             [3,  7,  6]]

Output: [[5.0, 3.0, -2.0],
         [1.0, 1.0,  1.0]]
```

**Explanation:** With one factorization of `A`, `b_1 = [6, -4, 27]` gives
`x_1 = [5, 3, -2]` and `b_2 = [3, 7, 6]` gives `x_2 = [1, 1, 1]`. Verify `x_2`:
`1 + 1 + 1 = 3`; `2·1 + 5·1 = 7`; `2·1 + 5·1 − 1 = 6`. ✓

## Hint

Do the expensive `O(n³)` work **once** with **LU Decomposition**, then amortize
it: every additional right-hand side is only two `O(n²)` triangular solves.

## Note

Computing the inverse of `A` explicitly and multiplying `A⁻¹ b_j` per system is
also `O(n³ + m·n²)`, but it is less numerically stable. LU + substitution is the
preferred approach.
