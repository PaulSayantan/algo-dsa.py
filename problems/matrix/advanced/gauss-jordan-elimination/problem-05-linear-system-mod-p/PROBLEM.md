# Linear System Modulo a Prime

**Difficulty:** Hard

**Source:** Competitive-programming classic (modular linear algebra over a finite field `GF(p)`)

## Description

You are given an `m × n` matrix `A`, a length-`m` vector `b`, and a **prime** `p`.
Consider the system of congruences over the finite field `GF(p)`:

```
A x ≡ b   (mod p)
```

All arithmetic — addition, subtraction, multiplication, and **division** — is done
modulo `p`. Division by a non-zero element `a` uses its modular inverse
`a^(p-2) mod p` (Fermat's little theorem).

Return one of:

- `"NO SOLUTION"` — the system is inconsistent mod `p`.
- `(count, x)` — where `count` is the **number of distinct solution vectors** in
  `GF(p)^n` and `x` is one particular solution (a length-`n` list of integers in
  `[0, p)`). If the system has free variables, `count = p^(number of free
  variables)`; if the solution is unique, `count = 1`.

## Constraints

- `1 ≤ m, n ≤ 200`
- `p` is prime and `2 ≤ p ≤ 10⁹ + 7`
- `0 ≤ A[i][j], b[i] < p`
- `count` may be astronomically large (`p^f`). Return the exact value when it fits
  in a 64-bit integer; otherwise return `count mod (10⁹ + 7)`. Reporting
  `count mod (10⁹ + 7)` is always acceptable. In the "no solution" case `count` is
  irrelevant — just return `"NO SOLUTION"`.

## Examples

### Example 1

```
Input:
  A = [[2, 3],
       [1, 2]]
  b = [1, 2]
  p = 7

Output: (1, [3, 3])

Explanation:
  Solving mod 7: from RREF, x = (3, 3). Check:
  2·3 + 3·3 = 6 + 9 = 15 ≡ 1 (mod 7)  ✓
  1·3 + 2·3 = 3 + 6 = 9  ≡ 2 (mod 7)  ✓
  rank = 2 = number of unknowns ⇒ exactly one solution, so count = 1.
```

### Example 2

```
Input:
  A = [[1, 1, 1]]
  b = [0]
  p = 3

Output: (9, [0, 0, 0])

Explanation:
  One equation x₀ + x₁ + x₂ ≡ 0 (mod 3) in 3 unknowns: rank = 1, so
  there are n - rank = 2 free variables. The number of solutions is
  p^(free) = 3² = 9. (0, 0, 0) is one valid solution since 0+0+0 ≡ 0.
```

### Example 3

```
Input:
  A = [[1, 1],
       [2, 3]]
  b = [3, 4]
  p = 5

Output: (1, [0, 3])

Explanation:
  Mod 5: x₀ + x₁ ≡ 3 and 2·x₀ + 3·x₁ ≡ 4. RREF gives x = (0, 3).
  Check: 0 + 3 = 3 ≡ 3 ✓ ; 2·0 + 3·3 = 9 ≡ 4 (mod 5) ✓. Unique ⇒ count = 1.
```

## Hint

Run **Gauss–Jordan Elimination**, but do every operation in modular arithmetic. The
only real change from the real-number version is the pivot-normalisation step:
instead of dividing the pivot row by the pivot value, **multiply it by the pivot's
modular inverse** `pow(pivot, p - 2, p)` (valid because `p` is prime). Count the
pivots to get the rank; the number of free columns `f = n - rank` gives
`count = p^f`, and a `0 ≡ c` row with `c ≠ 0` means `"NO SOLUTION"`.
