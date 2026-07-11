# Solve a Linear System with LU

**Difficulty:** Medium

**Source:** Classic numerical linear algebra (CLRS §28.1, "Solving systems of linear equations")

## Description

Given a square, non-singular `n × n` matrix `A` and a right-hand-side vector `b`
of length `n`, solve the linear system:

```
A · x = b
```

and return the solution vector `x`.

The idea is to **not** invert `A`. Instead, factor `A = LU` (Doolittle), then
split the single hard solve into two easy triangular solves:

```
A x = b
(LU) x = b
L (U x) = b
```

Let `y = U x`. Then:

1. **Forward substitution:** solve `L y = b` for `y`. Because `L` is lower
   triangular with unit diagonal, you sweep top-to-bottom:
   `y[i] = b[i] − Σ_{k<i} L[i][k]·y[k]`.
2. **Back substitution:** solve `U x = y` for `x`. Because `U` is upper
   triangular, you sweep bottom-to-top:
   `x[i] = (y[i] − Σ_{k>i} U[i][k]·x[k]) / U[i][i]`.

Each substitution is `O(n²)`. You may assume `A` admits an LU factorization
without pivoting (all pivots non-zero); a robust implementation would add partial
pivoting.

## Constraints

- `1 <= n <= 200`
- `A` is a square, non-singular matrix of real numbers with non-zero pivots.
- `b` has exactly `n` real entries.
- A tolerance of `1e-6` is acceptable when comparing solution entries.

## Examples

### Example 1

```
Input:  A = [[4, 3],
             [6, 3]]
        b = [10, 12]

Output: x = [1.0, 2.0]
```

**Explanation:** LU gives `L = [[1, 0], [1.5, 1]]`, `U = [[4, 3], [0, -1.5]]`.
Forward solve `Ly = b`: `y[0] = 10`, `y[1] = 12 − 1.5·10 = -3`. Back solve
`Ux = y`: `x[1] = -3 / -1.5 = 2`, `x[0] = (10 − 3·2) / 4 = 1`. Check:
`4·1 + 3·2 = 10` and `6·1 + 3·2 = 12`.

### Example 2

```
Input:  A = [[1, 1,  1],
             [0, 2,  5],
             [2, 5, -1]]
        b = [6, -4, 27]

Output: x = [5.0, 3.0, -2.0]
```

**Explanation:** Solving the system yields `x = (5, 3, -2)`. Verify each
equation: `5 + 3 + (-2) = 6`; `2·3 + 5·(-2) = 6 − 10 = -4`;
`2·5 + 5·3 − (-2) = 10 + 15 + 2 = 27`. All three hold.

## Hint

Factor once with **LU Decomposition**, then solve the two triangular systems by
forward and back substitution — never form `A⁻¹`.
