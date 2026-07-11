# N-Queens — Solution

## Brute Force

The most naive approach places queens in all `C(n*n, n)` ways of choosing `n` cells out of
`n*n`, then checks each configuration for attacks. This is astronomically large and wasteful
because it ignores the obvious fact that no two queens can share a row.

- **Time:** `O(C(n^2, n) * n^2)` to generate and validate every subset — completely
  intractable beyond tiny `n`.
- **Space:** `O(n)` per configuration.

A first improvement: since each row holds exactly one queen, brute force over one column
choice per row, giving `n^n` assignments, then validate each in `O(n^2)`. Still exponential,
but it motivates the pruned backtracking below.

## Optimal Approach (Backtracking on Grid)

Place queens **one row at a time**. Maintain three sets that record which columns and which
diagonals are already occupied, so a placement's legality is an `O(1)` check.

**Diagonal encoding.** For a queen at `(row, col)`:
- All cells on the same **"/" (anti-)diagonal** share `row + col`.
- All cells on the same **"\" diagonal** share `row - col`.

So we keep `cols`, `diag1 = {row + col}`, and `diag2 = {row - col}`.

**Algorithm**

1. Maintain `board`, a list of column positions (or an actual char grid), and the three sets.
2. `backtrack(row)`:
   - If `row == n`, we have placed a queen in every row without conflict — record a copy of
     the current board as a solution and return.
   - For each `col` in `0..n-1`:
     - Skip if `col in cols` or `(row + col) in diag1` or `(row - col) in diag2` (attacked).
     - **Choose:** place the queen — add `col`, `row + col`, `row - col` to the sets and
       set `board[row][col] = 'Q'`.
     - **Explore:** `backtrack(row + 1)`.
     - **Un-choose:** remove `col`, `row + col`, `row - col` from the sets and reset the cell
       to `'.'`.
3. Return all recorded solutions.

**Why it is correct.** By construction we place exactly one queen per row, so row conflicts
are impossible. The three sets guarantee at placement time that the chosen column and both
diagonals are unused, eliminating column and diagonal conflicts. When `row == n`, all `n`
queens are placed with no mutual attacks — a valid solution. Because we try every column in
every row and backtrack, we enumerate every valid configuration exactly once (each solution
corresponds to one unique column-per-row assignment).

**Reference implementation**

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, diag1, diag2 = set(), set(), set()
        board = [["."] * n for _ in range(n)]
        results: List[List[str]] = []

        def backtrack(row: int) -> None:
            if row == n:
                results.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue
                cols.add(col); diag1.add(row + col); diag2.add(row - col)
                board[row][col] = "Q"          # choose

                backtrack(row + 1)             # explore

                board[row][col] = "."          # un-choose
                cols.discard(col); diag1.discard(row + col); diag2.discard(row - col)

        backtrack(0)
        return results
```

- **Time:** `O(N!)` in the worst case — the first row has `n` choices, the next at most
  `n - 1` compatible columns, and so on; diagonal pruning removes even more. Building each
  solution string costs `O(n^2)`.
- **Space:** `O(n)` for the three sets and the recursion stack, plus `O(n^2)` per emitted
  solution board.

## Key Insights & Edge Cases

- **One queen per row** is the structural insight that turns an `O(C(n^2, n))` search into
  an `O(N!)` one — never search over rows and columns independently.
- **Diagonal identity trick:** `row + col` is constant on one diagonal direction and
  `row - col` on the other. Using sets makes the attack test `O(1)`. (Some solutions offset
  `row - col` by `n - 1` to index a boolean array instead of using a set.)
- **Symmetric backtrack:** every add to a set / write to the board must be paired with a
  matching remove / reset, or later rows will see phantom queens.
- **Edge cases:** `n = 1` yields the single board `[["Q"]]`; `n = 2` and `n = 3` yield `[]`
  (no solutions), which the algorithm returns naturally because every branch hits a conflict.
- **Counting variant (N-Queens II, LeetCode 52):** the exact same search, but increment a
  counter instead of materializing boards — cheaper because you skip the `O(n^2)` string
  build.
