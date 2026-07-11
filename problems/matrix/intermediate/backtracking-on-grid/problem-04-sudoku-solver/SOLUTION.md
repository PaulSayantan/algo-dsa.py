# Sudoku Solver — Solution

## Brute Force

The most naive approach fills all empty cells with every combination of digits `1-9` and
then validates the completed board. With up to 81 empty cells and 9 choices each, that is
`9^81` complete boards to check — utterly impossible.

- **Time:** `O(9^(empty))` where `empty` is the number of blank cells, validating each board
  in `O(81)`. With no early pruning this is intractable.
- **Space:** `O(1)` extra (fill in place) or `O(81)` for a copy.

The fix is to **validate incrementally** — reject a digit the moment it violates a rule,
instead of waiting until the board is full. That is exactly the backtracking approach.

## Optimal Approach (Backtracking on Grid)

Walk the grid to the next empty cell, try only digits that are legal *right now*, recurse,
and undo on failure. Keep constraint sets so legality is `O(1)`.

**Constraint bookkeeping.** Maintain, for fast checks:
- `rows[r]` — set of digits already used in row `r`.
- `cols[c]` — set of digits already used in column `c`.
- `boxes[b]` — set of digits used in box `b`, where `b = (r // 3) * 3 + (c // 3)`.

Seed these three structures from the given clues before searching.

**Algorithm**

1. `backtrack(pos)` where `pos` scans cells `0..80` (`r = pos // 9`, `c = pos % 9`):
   - If `pos == 81`, the board is complete — return `True`.
   - If `board[r][c] != '.'` (a clue or already filled), recurse to `backtrack(pos + 1)`.
   - Otherwise, for each digit `d` in `'1'..'9'`:
     - Skip if `d in rows[r]` or `d in cols[c]` or `d in boxes[b]`.
     - **Choose:** write `d` into the cell and add it to `rows[r]`, `cols[c]`, `boxes[b]`.
     - **Explore:** if `backtrack(pos + 1)` returns `True`, propagate `True` (solved).
     - **Un-choose:** reset the cell to `'.'` and remove `d` from the three sets.
   - If no digit works, return `False` (dead end — parent will try another digit).
2. Call `backtrack(0)`; the board is mutated in place to the solution.

**Why it is correct.** At each empty cell we only ever write a digit that is absent from its
row, column, and box, so the board stays a *valid partial* Sudoku at all times (this is the
invariant). If we reach `pos == 81` the board is fully filled and still valid, hence a
complete solution. If a cell has no legal digit, the current partial assignment cannot be
extended, so we backtrack and let an earlier cell try a different digit. Since we try every
legal digit at every cell, the search explores all completions of the partial board; because
the input has a unique solution, it returns exactly that board.

**Reference implementation**

```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                d = board[r][c]
                if d != ".":
                    b = (r // 3) * 3 + (c // 3)
                    rows[r].add(d); cols[c].add(d); boxes[b].add(d)

        def backtrack(pos: int) -> bool:
            if pos == 81:
                return True
            r, c = divmod(pos, 9)
            if board[r][c] != ".":
                return backtrack(pos + 1)

            b = (r // 3) * 3 + (c // 3)
            for d in "123456789":
                if d in rows[r] or d in cols[c] or d in boxes[b]:
                    continue
                board[r][c] = d                       # choose
                rows[r].add(d); cols[c].add(d); boxes[b].add(d)

                if backtrack(pos + 1):                # explore
                    return True

                board[r][c] = "."                     # un-choose
                rows[r].discard(d); cols[c].discard(d); boxes[b].discard(d)
            return False

        backtrack(0)
```

- **Time:** `O(9^(empty))` worst case, but constraint pruning collapses this to near-instant
  on real puzzles because most cells have very few legal candidates.
- **Space:** `O(1)` for the fixed 9x9 grid and 27 constraint sets (each bounded by 9), plus
  `O(81)` recursion depth.

## Key Insights & Edge Cases

- **Incremental validation is everything.** The `O(1)` "is digit legal here" check via
  row/column/box sets is what makes the search fast; recomputing validity by scanning the
  board each time is far slower.
- **Box index formula:** `b = (r // 3) * 3 + (c // 3)` maps each cell to one of the nine
  `3x3` boxes.
- **Solve in place, return None.** LeetCode expects `board` mutated directly; the boolean
  return is only an internal signal that a completion was found so the recursion can stop.
- **Stop at the first solution.** Because the puzzle has a unique solution, returning `True`
  up the stack the instant `pos == 81` avoids any extra work.
- **MRV heuristic (optional speedup):** instead of scanning cells in order, always fill the
  empty cell with the *fewest* legal candidates next. This "most constrained variable" order
  dramatically prunes hard puzzles, at the cost of a bit more bookkeeping.
- **Already-complete or single-empty boards** (Example 2) are handled by the same code —
  clues are skipped and the lone empty cell is filled with its only legal digit.
