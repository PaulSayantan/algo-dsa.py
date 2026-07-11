# Solution — Classify a Linear System

## Brute Force

There is no meaningful enumeration over real unknowns, so the "brute force" here is
really the *theory-by-hand* approach:

- Compute `rank(A)` and `rank([A | b])` independently (e.g. two separate
  reductions, or determinant-based minors), then apply Rouché–Capelli. Computing
  ranks via minors is exponential; via a second elimination it is another `O(n³)`.

That works but duplicates effort. A single Gauss–Jordan pass over the augmented
matrix gives *both* ranks and the solution at once.

- **Time (minors):** exponential. **Time (double elimination):** `O(n³)`.

## Optimal Approach (Gauss–Jordan Elimination)

Reduce `[A | b]` to RREF while recording, for each column, whether it received a
pivot. Do it in a rank-robust way (no assumption that `A` is square or full-rank):

1. Keep a `row` cursor starting at `0`. Iterate columns `c = 0 … n-1`.
2. Find any row `≥ row` with a non-zero entry in column `c`. If none, column `c` is
   a **free column** (no pivot) — skip it.
3. Otherwise swap that row up to `row`, normalise it so the pivot is `1`, and
   eliminate column `c` from **all** other rows (above and below). Record
   `where[c] = row`, then `row += 1`.
4. `rank = row` after the loop.

**Consistency & classification.** After reduction:

- If any row is entirely zero across the coefficient columns but has a non-zero
  augmented entry (`0 = c`, `c ≠ 0`), the system is **inconsistent** →
  `"NO SOLUTION"` (this is exactly `rank([A|b]) > rank(A)`).
- Else if `rank == n` (a pivot in every unknown's column) → **unique**; read
  `xⱼ = M[where[j]][n]`.
- Else (`rank < n`, some free column) → **`"INFINITE"`**.

```python
def classify_system(A, b, eps=1e-9):
    m, n = len(A), len(A[0])
    M = [[float(A[i][j]) for j in range(n)] + [float(b[i])] for i in range(m)]

    where = [-1] * n          # where[c] = row holding the pivot of column c
    row = 0
    for c in range(n):
        # pick the largest-magnitude candidate at/below `row` for stability
        piv = max(range(row, m), key=lambda r: abs(M[r][c]), default=row)
        if row >= m or abs(M[piv][c]) < eps:
            continue                          # free column, no pivot
        M[row], M[piv] = M[piv], M[row]
        pv = M[row][c]
        M[row] = [v / pv for v in M[row]]
        for i in range(m):
            if i != row and abs(M[i][c]) > eps:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[row][j] for j in range(n + 1)]
        where[c] = row
        row += 1

    rank = row

    # inconsistency: a "0 = nonzero" row
    for i in range(m):
        if all(abs(M[i][j]) < eps for j in range(n)) and abs(M[i][n]) > eps:
            return "NO SOLUTION"

    if rank < n:
        return "INFINITE"

    x = [M[where[j]][n] for j in range(n)]
    return ("UNIQUE", x)
```

**Why it is correct.** Row operations preserve the solution set, and RREF makes the
rank readable as the number of pivots. Rouché–Capelli states a system is consistent
iff `rank(A) = rank([A|b])`; the `0 = c` row is precisely the witness that the
augmented rank exceeds the coefficient rank. When consistent, a free column means a
free parameter (infinitely many solutions), while a full set of pivots pins down
each unknown uniquely.

**Complexity.** `O(n)` pivot columns × `O(m)` rows × `O(n)` per row ⇒ `O(m·n²)`
(so `O(n³)` for square systems). Space `O(m·n)`.

## Key Insights & Edge Cases

- **One pass, two ranks.** Reducing the *augmented* matrix yields `rank(A)`
  (pivots in coefficient columns) and detects `rank([A|b]) > rank(A)` (the `0 = c`
  row) simultaneously — no need to reduce `A` twice.
- **Order of checks matters.** Check inconsistency *before* declaring "infinite": a
  system can be under-determined *and* inconsistent, and inconsistency wins.
- **Free-column bookkeeping.** Using a `where[]` array (pivot column → row) lets you
  read the unique solution directly and, in the infinite case, identify exactly
  which variables are free (any column with `where[c] == -1`).
- **`m ≠ n`.** Over-determined (`m > n`) systems are common and often inconsistent;
  under-determined (`m < n`) systems have `rank ≤ m < n`, so they are never unique.
  The rank-cursor formulation handles both without special cases.
- **Numerical caveat.** With floats, "is this entry zero?" becomes "is `|entry| <
  eps`?" — a wrong `eps` can misclassify borderline-singular systems. For exact
  classification use rational arithmetic.
