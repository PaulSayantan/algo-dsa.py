# Solution — Linear System Modulo a Prime

## Brute Force

Every unknown lives in `{0, 1, …, p-1}`, so there are `p^n` candidate vectors.
Enumerate each, plug it into all `m` congruences, and keep the ones that satisfy
`A x ≡ b (mod p)`.

- **Time:** `O(p^n · m · n)` — utterly infeasible for `p` up to `10⁹` and `n` up to
  `200`.
- **Space:** `O(m · n)`.

We need structure, not enumeration: `GF(p)` is a field (because `p` is prime), so
the entire real-number elimination theory carries over verbatim — we just replace
"divide" with "multiply by the modular inverse".

## Optimal Approach (Gauss–Jordan Elimination over GF(p))

Work on the augmented matrix `[A | b]` with all entries reduced mod `p`. The only
change from the real-valued algorithm is how we normalise a pivot:

- **Modular inverse.** Since `p` is prime, every non-zero `a` has an inverse
  `a⁻¹ ≡ a^(p-2) (mod p)` by Fermat's little theorem. To make a pivot `1`, multiply
  the pivot row by `inv(pivot)` instead of dividing.

Algorithm (rank-robust; handles non-square and rank-deficient systems):

1. Cursor `row = 0`; iterate columns `c = 0 … n-1`.
2. Find any row `≥ row` with a non-zero entry (mod `p`) in column `c`. If none,
   column `c` is **free** — skip.
3. Swap that row up to `row`. Multiply row `row` by `inv(M[row][c])` so the pivot
   becomes `1`.
4. For every other row `i ≠ row` with a non-zero entry in column `c`, subtract
   `M[i][c] × (row row)` mod `p` to clear column `c`. Record `where[c] = row`,
   `row += 1`.
5. `rank = row`.

Then classify:

- **Inconsistent:** any row with all-zero coefficients but a non-zero augmented
  entry is `0 ≡ c (mod p)`, `c ≠ 0` → `"NO SOLUTION"`.
- **Solution count:** `f = n - rank` free variables, so `count = p^f (mod 1e9+7)`
  (exactly `1` when `rank == n`). Read one particular solution by setting free
  variables to `0` and `x[c] = M[where[c]][n]` for pivot columns.

```python
MOD = 1_000_000_007

def solve_mod_p(A, b, p):
    m, n = len(A), len(A[0])
    M = [[A[i][j] % p for j in range(n)] + [b[i] % p] for i in range(m)]

    where = [-1] * n
    row = 0
    for c in range(n):
        piv = next((i for i in range(row, m) if M[i][c] % p != 0), None)
        if piv is None:
            continue                                  # free column
        M[row], M[piv] = M[piv], M[row]

        inv = pow(M[row][c], p - 2, p)                # modular inverse of pivot
        M[row] = [(v * inv) % p for v in M[row]]

        for i in range(m):
            if i != row and M[i][c] % p != 0:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[row][j]) % p for j in range(n + 1)]

        where[c] = row
        row += 1

    rank = row
    # inconsistency check
    for i in range(m):
        if all(M[i][j] % p == 0 for j in range(n)) and M[i][n] % p != 0:
            return "NO SOLUTION"

    x = [0] * n
    for c in range(n):
        if where[c] != -1:
            x[c] = M[where[c]][n] % p

    free = n - rank
    count = pow(p, free, MOD)     # exact when free == 0 (== 1), else count mod 1e9+7
    return (count, x)
```

**Why it is correct.** `GF(p)` is a field, so elementary row operations (swap,
scale by a non-zero element, add a multiple of a row) preserve the solution set
exactly as over the reals. RREF exposes the rank; Rouché–Capelli applies verbatim
over any field. In a field with `p` elements, each free variable ranges
independently over all `p` values, so a consistent system with `f` free variables
has exactly `p^f` solution vectors.

**Complexity.** `O(n)` pivot columns × `O(m)` rows × `O(n)` per row, each cell doing
`O(1)` modular ops (the `pow(pivot, p-2, p)` inverse is `O(log p)` and runs once per
pivot). Total `O(m·n² + n·log p)`, i.e. `O(n³)` for square systems. Space `O(m·n)`.

## Key Insights & Edge Cases

- **"Divide" = "multiply by inverse".** This is the single conceptual jump from
  real to modular Gauss–Jordan; everything else — pivoting, elimination, rank,
  consistency — is identical.
- **Prime modulus is essential.** Fermat's inverse `a^(p-2)` only works when `p` is
  prime (so that `GF(p)` is a field and every non-zero element is invertible). For a
  composite modulus you would need `gcd`-based inverses and elements may fail to be
  invertible, breaking the clean theory.
- **Keep everything reduced mod `p`.** Reduce inputs up front and after each
  operation to avoid overflow and to make the `!= 0` pivot test meaningful; in
  Python big-ints won't overflow, but the `% p` keeps values canonical.
- **No floating point, no `eps`.** Zero-testing is exact (`v % p == 0`), so
  classification is exact — a nice contrast with the real-valued version's `eps`
  fragility.
- **GF(2) is the special case `p = 2`.** Problem 4 (Lights Out) is exactly this
  algorithm with `p = 2`, where `inv(1) = 1` and subtraction is XOR.
- **Counting overflow.** `p^f` can be enormous; return it modulo `10⁹ + 7` via fast
  modular exponentiation. Guard the "no solution" branch first so you never report a
  count for an inconsistent system.
