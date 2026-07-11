# Solution — Lights Out

## Brute Force

Each cell is pressed 0 or 1 times, so there are `2^(m*n)` press patterns. Try each,
simulate the toggles, and keep the minimum press count that clears the board.

- **Time:** `O(2^(m*n) * m * n)` — only viable for tiny boards (`m*n <= ~20`).
- **Space:** `O(m * n)`.

A better brute force fixes only the **first row** of presses (`2^n` choices) and propagates
downward — each remaining press is forced because a light can only be toggled from the row
below once. That is `O(2^n * m * n)` and is the standard trick, but it still hides the
linear structure. The general, board-shape-agnostic method is Gaussian elimination.

## Optimal Approach (Gaussian Elimination over GF(2))

Number the cells `0 .. mn-1`. Let unknown `p_j in {0,1}` be "do we press cell `j`?".
Pressing cell `j` toggles cell `j` and its neighbors, so define the `mn x mn` matrix `A`
over `GF(2)` by:

```
A[i][j] = 1  if pressing cell j toggles cell i   (i == j or i,j adjacent)
```

The final state of light `i` is `b_i XOR (sum_j A[i][j] * p_j)`, and we want every light
off, i.e.

```
A p = b   (mod 2)
```

where `b_i` is the initial state of cell `i`. `A` is symmetric here (adjacency is
symmetric), but that is incidental — we just solve the system.

### Step by step

1. **Build the augmented matrix** `[A | b]` with `mn` rows. Represent each row as a Python
   integer bitset of width `mn + 1` so a whole row XOR is one operation.
2. **Forward elimination over GF(2):** for each column, find a row with a `1` in that column
   (the pivot), swap it up, and XOR it into every *other* row that has a `1` there. Over
   GF(2) there is no scaling — the pivot is already `1`. Record which column each pivot
   occupies; columns without a pivot are **free variables**.
3. **Consistency check:** if any row has all-zero coefficients but a `1` in the augmented
   (right-hand) column, the equation says `0 = 1` — the puzzle is **impossible**, return
   `-1`. (This is exactly Example 2: the 2x3 press matrix has rank 4 < 6, and a single lit
   corner falls outside its column space.)
4. **Minimize presses over the free variables:** let `f` be the number of free variables
   (`f = mn - rank`). Enumerate all `2^f` assignments of the free variables; for each,
   back-substitute to determine the pivot variables, and count the total number of `1`s
   (presses). Keep the minimum. When `f` is 0 the solution is unique.

Because `m*n <= 225` but the *nullity* `f` is small for most boards, `2^f` enumeration is
fast in practice; for the classic square boards `f` is 0 or 2.

### Reference implementation

```python
from typing import List

def min_presses_lights_out(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    N = m * n
    def idx(i, j): return i * n + j

    # rows[i] is a bitset: bits 0..N-1 are coefficients, bit N is the RHS.
    rows = [0] * N
    for i in range(m):
        for j in range(n):
            r = idx(i, j)
            # pressing cell (i2,j2) affects (i,j) iff same or adjacent
            for di, dj in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n:
                    rows[r] |= 1 << idx(i2, j2)
            if grid[i][j]:
                rows[r] |= 1 << N  # RHS bit

    # Gaussian elimination over GF(2).
    where = [-1] * N  # which row is the pivot for column col
    row = 0
    for col in range(N):
        piv = next((r for r in range(row, N) if (rows[r] >> col) & 1), None)
        if piv is None:
            continue
        rows[row], rows[piv] = rows[piv], rows[row]
        for r in range(N):
            if r != row and (rows[r] >> col) & 1:
                rows[r] ^= rows[row]
        where[col] = row
        row += 1

    # Consistency: a zero row with RHS 1 => 0 = 1.
    for r in range(row, N):
        if (rows[r] >> N) & 1:
            return -1

    free = [c for c in range(N) if where[c] == -1]
    best = None
    for mask in range(1 << len(free)):
        val = [0] * N
        for b, c in enumerate(free):
            val[c] = (mask >> b) & 1
        # Back-substitute pivot columns (rows are reduced; each pivot row's
        # only pivot-column entry is its own).
        for col in range(N - 1, -1, -1):
            if where[col] == -1:
                continue
            r = where[col]
            rhs = (rows[r] >> N) & 1
            s = rhs
            cc = col + 1
            bits = rows[r] >> (col + 1)
            while bits:
                if bits & 1 and cc < N:
                    s ^= val[cc]
                bits >>= 1
                cc += 1
            val[col] = s
        cnt = sum(val)
        if best is None or cnt < best:
            best = cnt
    return best if best is not None else 0
```

### Complexity

- **Time:** elimination is `O(N^3 / word_size)` with bitset rows, i.e. about
  `O((mn)^3 / 64)`. The free-variable enumeration adds `O(2^f * N)`, where `f = mn - rank`
  is the nullity (small for typical boards).
- **Space:** `O(N)` integers (one bitset per row), i.e. `O(mn)` machine words.

## Key Insights & Edge Cases

- **Impossibility = inconsistency.** A row reduced to all-zero coefficients with a `1` on
  the right encodes `0 = 1`; that is the *only* way the puzzle is unsolvable (Example 2).
- **Order of presses is irrelevant and pressing twice cancels**, which is exactly why the
  problem is linear over GF(2) rather than a general search.
- **Free variables = the puzzle's symmetries.** The nullity `f` counts independent "press
  patterns that toggle nothing." Every solution differs by such a pattern, so you must
  search all `2^f` to get the *minimum* press count — any single solution clears the board,
  but not necessarily with the fewest presses.
- **Already solved board** (all zeros) yields `b = 0`; the all-zero press vector is a valid
  solution and enumeration finds `0` presses (Example 3).
- **1x1 board:** `A = [[1]]`, so `p_0 = b_0`; press once iff the light is on.
- **Bitset rows are the practical accelerator:** representing each equation as one integer
  turns "add pivot row to another row" into a single `^=`, which is what makes GF(2)
  Gaussian elimination so fast.
