# Solve a System of Linear Equations

**Difficulty:** Medium

**Source:** Classic (CLRS "Solving Systems of Linear Equations"; equivalent to many
online-judge "Gauss" problems, e.g. Timus 1041, SPOJ style).

## Description

You are given a system of `n` linear equations in `n` unknowns
`x_0, x_1, ..., x_{n-1}`:

```
A[0][0]*x_0 + A[0][1]*x_1 + ... + A[0][n-1]*x_{n-1} = b[0]
A[1][0]*x_0 + A[1][1]*x_1 + ... + A[1][n-1]*x_{n-1} = b[1]
...
A[n-1][0]*x_0 + ... + A[n-1][n-1]*x_{n-1} = b[n-1]
```

The coefficient matrix `A` (size `n x n`) and the right-hand-side vector `b` (length `n`)
are given. It is guaranteed that the system has **exactly one** solution (i.e. `A` is
non-singular).

Return the solution vector `x` of length `n`. Because the arithmetic is over the real
numbers, return floating-point values; answers within `1e-6` of the true value are
accepted.

## Constraints

- `1 <= n <= 200`
- `-1000.0 <= A[i][j] <= 1000.0`
- `-1000.0 <= b[i] <= 1000.0`
- `A` is guaranteed invertible (a unique solution exists).

## Examples

### Example 1

```
Input:
A = [[2, 1],
     [1, -1]]
b = [5, 1]

Output: [2.0, 1.0]

Explanation:
  2*x0 + 1*x1 = 5
  1*x0 - 1*x1 = 1
Adding the two equations: 3*x0 = 6 => x0 = 2, then x1 = x0 - 1 = 1.
Check: 2*2 + 1 = 5 and 2 - 1 = 1. Correct.
```

### Example 2

```
Input:
A = [[1, 1, 1],
     [2, 1, 1],
     [1, 3, 2]]
b = [6, 7, 13]

Output: [1.0, 2.0, 3.0]

Explanation:
  x0 + x1 + x2 = 6
  2*x0 + x1 + x2 = 7
  x0 + 3*x1 + 2*x2 = 13
Subtracting eq1 from eq2 gives x0 = 1. Substituting back and eliminating leaves
x1 = 2 and x2 = 3. Check: 1+2+3=6, 2+2+3=7, 1+6+6=13. Correct.
```

## Hint

Use **Gaussian Elimination**: reduce the augmented matrix `[A | b]` to upper-triangular
row-echelon form using row operations (with partial pivoting for numerical stability),
then recover `x` by back-substitution.
