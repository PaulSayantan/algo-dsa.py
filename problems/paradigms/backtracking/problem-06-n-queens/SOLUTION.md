# N-Queens — Solution

## Brute Force

The most naive approach places queens anywhere on the board: choose `n` of the
`n²` squares and test whether the chosen set is mutually non-attacking. That is
`C(n², n)` configurations — hopeless even for small `n`.

A first refinement uses the observation that each row must hold exactly one
queen, so a placement is a function `col[row] -> column`. Brute force then tries
all `n^n` column assignments (or all `n!` if you also forbid repeated columns)
and validates each fully at the end.

- **Time:** `O(n^n · n²)` for the arbitrary-column version (or `O(n! · n²)` if you
  pre-forbid duplicate columns), because validation scans all pairs.
- **Space:** `O(n)` for one candidate assignment.

Correct, but it commits to a whole board before checking anything, so it cannot
prune the huge number of assignments that fail on the very first conflict.

## Optimal Approach (Backtracking)

Place exactly one queen per row, top to bottom. Maintain three sets of "attacked"
lines so validity is `O(1)` per placement:

- `cols` — columns already used.
- `diag1` — the `↘` diagonals, identified by `row - col` (constant along a `↘`).
- `diag2` — the `↙` diagonals, identified by `row + col` (constant along a `↙`).

```python
def solveNQueens(n):
    result = []
    cols, diag1, diag2 = set(), set(), set()
    queens = []                                  # queens[r] = column in row r

    def backtrack(row):
        if row == n:                             # placed a queen in every row
            board = ['.' * c + 'Q' + '.' * (n - c - 1) for c in queens]
            result.append(board)
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue                         # prune: this square is attacked
            cols.add(col); diag1.add(row - col); diag2.add(row + col)  # choose
            queens.append(col)
            backtrack(row + 1)                   # solve the next row
            queens.pop()                         # undo
            cols.discard(col); diag1.discard(row - col); diag2.discard(row + col)

    backtrack(0)
    return result
```

**Why it is correct.**

- Placing one queen per row automatically satisfies the "no shared row" rule.
- The `cols` set enforces distinct columns; `row - col` is invariant along a `↘`
  diagonal and `row + col` along a `↙` diagonal, so the two diagonal sets reject
  any queen sharing a diagonal with an already-placed one. Thus a queen is added
  only when it attacks none of the previous queens.
- Reaching `row == n` means all `n` queens are placed with no conflicts — a valid
  solution. Iterating every legal column in every row explores all such boards
  exactly once (each solution corresponds to a unique per-row column vector).

**Step by step for `n = 4`:**

- Row 0: try col 0 → row 1 cols 0,1 blocked, col 2 → row 2 all blocked → dead;
  backtrack. Col 1 in row 0 → col 3 in row 1 → col 0 in row 2 → col 2 in row 3 →
  solution `columns = (1,3,0,2)`.
- Continue backtracking; the symmetric branch yields `columns = (2,0,3,1)`.
- No other column vector survives, so there are exactly 2 solutions.

- **Time:** `O(n!)` in the worst case — the branching per row shrinks as columns
  and diagonals fill up, so far fewer than `n^n` nodes are visited; building each
  found board costs `O(n²)`.
- **Space:** `O(n)` for the three sets, the `queens` list, and recursion depth.

## Key Insights & Edge Cases

- **`row - col` and `row + col` diagonal keys** are the crucial trick: they turn
  an `O(n)` diagonal scan into an `O(1)` set membership test. (`row - col` can be
  negative — a set handles that fine; some use `row - col + n` to index arrays.)
- **One queen per row** is what makes the search tree shallow (`depth = n`) and
  removes the shared-row check entirely.
- **Undo all three sets and the queens list** on the way out; forgetting any one
  leaves phantom attacks and drops valid solutions.
- **Known counts** (a good self-check): `n = 1 → 1`, `n = 2 → 0`, `n = 3 → 0`,
  `n = 4 → 2`, `n = 5 → 10`, `n = 6 → 4`, `n = 7 → 40`, `n = 8 → 92`, `n = 9 → 352`.
- **`n = 2` and `n = 3` have no solution**; the code correctly returns `[]` when
  every branch is pruned before reaching `row == n`.
- **Bitmask variant:** replace the three sets with integer bitmasks and use
  `available = ~(cols | diag1 | diag2)` bit tricks for a large constant-factor
  speedup (LeetCode 52, "N-Queens II", which only counts solutions).
