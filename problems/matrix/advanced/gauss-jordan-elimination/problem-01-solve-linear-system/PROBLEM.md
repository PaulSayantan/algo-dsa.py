# Solve a System of Linear Equations

**Difficulty:** Easy

**Source:** Classic linear-algebra exercise (CLRS §28, "Solving systems of linear equations")

## Description

You are given a square system of `n` linear equations in `n` unknowns
`x₀, x₁, …, x_{n-1}`:

```
a₀₀·x₀ + a₀₁·x₁ + … + a₀,ₙ₋₁·x_{n-1} = b₀
a₁₀·x₀ + a₁₁·x₁ + … + a₁,ₙ₋₁·x_{n-1} = b₁
                    ⋮
```

The coefficients are given as an `n × n` matrix `A` (`A[i][j] = a_{ij}`) and the
right-hand side as a length-`n` vector `b`.

For this problem you are guaranteed that the matrix `A` is **non-singular** (its
determinant is non-zero), so the system has exactly **one** solution. Return that
solution vector `x` as a list of `n` floats, in order `x₀ … x_{n-1}`.

Answers within `1e-6` of the true value are accepted.

## Constraints

- `1 ≤ n ≤ 200`
- `A` is `n × n`; `b` has length `n`.
- `-1000 ≤ A[i][j], b[i] ≤ 1000`
- `A` is guaranteed non-singular (a unique solution exists).

## Examples

### Example 1

```
Input:
  A = [[1, 1,  1],
       [0, 2,  5],
       [2, 5, -1]]
  b = [6, -4, 27]

Output: [5.0, 3.0, -2.0]

Explanation:
  x₀ = 5, x₁ = 3, x₂ = -2 satisfies all three equations, e.g.
  row 0: 5 + 3 + (-2) = 6  ✓
  row 1: 0 + 2·3 + 5·(-2) = 6 - 10 = -4  ✓
  row 2: 2·5 + 5·3 - (-2) = 10 + 15 + 2 = 27  ✓
```

### Example 2

```
Input:
  A = [[2, 1],
       [1, 3]]
  b = [3, 4]

Output: [1.0, 1.0]

Explanation:
  2·1 + 1·1 = 3  ✓  and  1·1 + 3·1 = 4  ✓, so x = (1, 1).
```

## Hint

Augment the matrix into `[A | b]` and apply **Gauss–Jordan Elimination** to reduce
the left block fully to the identity (RREF). Remember to use **partial pivoting**
(swap in the row with the largest-magnitude pivot) for numerical stability. Once
the left block is the identity, the last column *is* the solution `x`.
