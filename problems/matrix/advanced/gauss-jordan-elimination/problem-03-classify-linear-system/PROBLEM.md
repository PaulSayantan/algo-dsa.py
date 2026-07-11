# Classify a Linear System

**Difficulty:** Medium

**Source:** Classic linear-algebra / competitive-programming exercise (Rouché–Capelli)

## Description

You are given a linear system `A x = b` with `m` equations and `n` unknowns
(`A` is `m × n`, `b` has length `m`). Unlike Problem 1, `A` need **not** be square
or non-singular. Classify the system into exactly one of three cases and return a
descriptive result:

- `"NO SOLUTION"` — the system is inconsistent.
- `"INFINITE"` — the system is consistent but under-determined (at least one free
  variable).
- `("UNIQUE", x)` — there is exactly one solution; also return the solution vector
  `x` (length `n`, floats).

The classification follows the **Rouché–Capelli** theorem:

- Let `r  = rank(A)` and `r' = rank([A | b])`.
- If `r < r'` → **no solution**.
- Else if `r = n` (rank equals the number of unknowns) → **unique**.
- Else (`r = r' < n`) → **infinitely many** solutions.

## Constraints

- `1 ≤ m, n ≤ 200`
- `-1000 ≤ A[i][j], b[i] ≤ 1000`
- Accept solution entries within `1e-6` of the true value (for the UNIQUE case).

## Examples

### Example 1

```
Input:
  A = [[1,  1],
       [1, -1]]
  b = [3, 1]

Output: ("UNIQUE", [2.0, 1.0])

Explanation:
  rank(A) = 2 = number of unknowns, so there is exactly one solution.
  x₀ + x₁ = 3 and x₀ - x₁ = 1  ⇒  x₀ = 2, x₁ = 1.
```

### Example 2

```
Input:
  A = [[1, 2],
       [2, 4]]
  b = [3, 6]

Output: "INFINITE"

Explanation:
  Row 2 = 2 × Row 1 and 6 = 2 × 3, so both equations say x₀ + 2·x₁ = 3.
  rank(A) = rank([A|b]) = 1 < 2 unknowns ⇒ a whole line of solutions.
```

### Example 3

```
Input:
  A = [[1, 2],
       [2, 4]]
  b = [3, 7]

Output: "NO SOLUTION"

Explanation:
  The left sides are proportional (row 2 = 2 × row 1) but 7 ≠ 2 × 3.
  RREF produces a row [0 0 | 1], i.e. "0 = 1", which is impossible.
  rank(A) = 1 < rank([A|b]) = 2 ⇒ inconsistent.
```

## Hint

Reduce `[A | b]` to RREF with **Gauss–Jordan Elimination**, tracking a pivot in
each column where one exists. The number of pivots is `rank(A)`. A pivot-free row
whose augmented entry is non-zero (a `0 = c` row with `c ≠ 0`) means **no
solution**; otherwise compare the pivot count to `n` to distinguish unique from
infinite.
