# Solution — Lights Out

## Brute Force

There are `m·n` cells and each is either pressed or not, so there are `2^(m·n)`
candidate press subsets. For each subset, simulate all presses (`O(m·n)`) and check
whether the board is cleared.

- **Time:** `O(2^(m·n) · m·n)` — hopeless past a `5×5` board.
- **Space:** `O(m·n)`.

A common improvement is **"press the first row, then chase":** brute-force only the
`2^n` press patterns for the top row, then each lower row is forced (press a cell if
the light directly above it is still on). That is `O(2^n · m·n)` — good, but it is
really just an ad-hoc way of solving the same linear system. Gauss–Jordan solves the
whole thing directly and generalises to any toggle rule.

## Optimal Approach (Gauss–Jordan Elimination over GF(2))

**Modeling.** Number the cells `0 … m·n-1`. Let unknown `xᵢ ∈ {0,1}` mean "press
cell `i`". Because pressing twice cancels, only parity matters, so all arithmetic is
**mod 2**. The final state of light `j` is:

```
(number of pressed cells whose toggle set includes j)  ≡  grid[j]   (mod 2)
```

We want every light off, so the target for light `j` is exactly its *current* value
`grid[j]` (we must toggle it an odd number of times iff it starts on). Row `j` of
matrix `A` has a `1` in column `i` whenever pressing `i` toggles light `j` — that is,
when `i == j` or `i` is an orthogonal neighbour of `j`. This yields a square
`N × N` system `A x ≡ b (mod 2)` with `N = m·n` and `b = grid` flattened.

**Solving over GF(2).** Run Gauss–Jordan, but the field operations simplify:

- There is no "divide by pivot" — the only non-zero element is `1`, which is its own
  inverse.
- "Subtract a multiple of the pivot row" becomes **XOR the pivot row into any row
  that has a `1` in the pivot column** (both above and below, since we want RREF).

Track `where[c]` (pivot column → row). After reduction:

- **Consistency:** any all-zero coefficient row with augmented bit `1` is a `0 = 1`
  contradiction → return `None`.
- **Read a solution:** set each free variable to `0`; each pivot column `c` gets
  `x_c = augmented bit of its pivot row`. Reshape `x` back to `m × n`.

```python
def lights_out(grid):
    m, n = len(grid), len(grid[0])
    N = m * n
    idx = lambda r, c: r * n + c

    # Build augmented rows as Python ints used as bitsets:
    #   bits 0..N-1  -> coefficients, bit N -> right-hand side.
    rows = [0] * N
    for r in range(m):
        for c in range(n):
            j = idx(r, c)
            row = 1 << j                              # pressing j toggles j
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    row |= 1 << idx(nr, nc)           # ... and its neighbours
            if grid[r][c]:
                row |= 1 << N                         # rhs = current light state
            rows[j] = row

    where = [-1] * N
    piv_row = 0
    for c in range(N):                                # eliminate column c
        sel = next((i for i in range(piv_row, N) if (rows[i] >> c) & 1), None)
        if sel is None:
            continue                                  # free column
        rows[piv_row], rows[sel] = rows[sel], rows[piv_row]
        for i in range(N):                            # clear column c everywhere
            if i != piv_row and (rows[i] >> c) & 1:
                rows[i] ^= rows[piv_row]
        where[c] = piv_row
        piv_row += 1

    # consistency: a row with no coefficients but rhs bit set is "0 = 1"
    coeff_mask = (1 << N) - 1
    for i in range(N):
        if (rows[i] & coeff_mask) == 0 and (rows[i] >> N) & 1:
            return None

    x = [0] * N
    for c in range(N):
        if where[c] != -1:
            x[c] = (rows[where[c]] >> N) & 1
    return [[x[idx(r, c)] for c in range(n)] for r in range(m)]
```

**Why it is correct.** Toggling is commutative and self-inverse, so the effect of a
press subset depends only on each cell's press parity — exactly the algebra of the
vector space `GF(2)^N`. Solving `A x ≡ b (mod 2)` therefore finds a press subset (if
any) that produces the required parity of toggles at every light, clearing the
board. A `0 = 1` row certifies that `b` is outside the column space of `A`, i.e. the
configuration is unsolvable.

**Complexity.** Reducing an `N × N` GF(2) system is `O(N³)` bit operations, but
packing each row into machine words (as the Python big-int bitset above, or an
explicit bitset) makes each row XOR cost `O(N / w)`, giving `O(N³ / w)` overall with
`O(N² / w)` space. For a `15×15` board, `N = 225`, which is trivially fast.

## Key Insights & Edge Cases

- **XOR replaces subtraction.** Over GF(2) the elimination loop has no division and
  no sign handling — "add pivot row to rows with a 1 in this column" is one XOR.
- **Already-solved board.** If `grid` is all zeros, `b = 0`; the all-zero press
  pattern is a valid (and returned) solution.
- **Multiple / no solutions.** Free columns mean many valid press patterns exist
  (this solution just sets free vars to 0). A `0 = 1` row means genuinely
  unsolvable — e.g. many `5×5` boards where `A` is singular have unsolvable starting
  configurations.
- **Minimum presses (harder variant).** If you must *minimise* presses, enumerate
  the `2^(free)` assignments of free variables, complete each to a full solution, and
  keep the one with the fewest `1`s. This is cheap only when the null space is small.
- **Generalises freely.** Any deterministic toggle rule (different neighbourhood,
  wrap-around/toroidal boards, non-square grids) just changes which entries of `A`
  are `1`; the GF(2) Gauss–Jordan solver is unchanged.
