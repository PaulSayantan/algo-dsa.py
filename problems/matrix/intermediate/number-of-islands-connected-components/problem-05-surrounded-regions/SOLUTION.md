# Surrounded Regions — Solution

## Brute Force

For each `'O'` region (a connected component), flood it and simultaneously check
whether **any** of its cells touches the border. If none do, flip the whole
region to `'X'`; otherwise leave it. This actually works and is `O(m*n)` if done
carefully — but the bookkeeping ("did this component touch an edge?") is
error-prone, and a naive implementation that re-checks reachability to the
border for *every* `'O'` independently degrades to `O((m*n)^2)`.

- **Naive time:** `O((m*n)^2)`; **careful time:** `O(m*n)`.
- **Space:** `O(m*n)`.

## Optimal Approach (Inverted Connected-Components Flood)

The clean trick is to solve the **complement**: rather than hunt for regions to
capture, mark all regions that are **safe**, then capture everything else.

An `'O'` is safe **iff** it is connected to the border. So:

1. **Flood from the border.** For every `'O'` on the four edges of the board,
   run DFS/BFS over connected `'O'`s and mark each one with a temporary
   sentinel (e.g. `'#'`).
2. **Final sweep.** Walk the whole board:
   - `'O'` (still unmarked) → it was *not* reachable from the border, so it is
     surrounded → flip to `'X'`.
   - `'#'` (marked safe) → restore to `'O'`.
   - `'X'` → leave as is.

**Why it is correct:** by definition an `'O'` survives exactly when it connects
to a border `'O'`. Step 1 marks precisely that set (the union of all connected
components that touch an edge). Any `'O'` left unmarked belongs to a component
with no border cell, i.e. one fully enclosed by `'X'`, which is what we must
capture.

### Reference implementation

```python
def solve(board):
    if not board or not board[0]:
        return
    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if board[r][c] != "O":
            return
        board[r][c] = "#"                 # mark safe
        dfs(r + 1, c); dfs(r - 1, c)
        dfs(r, c + 1); dfs(r, c - 1)

    # 1. Flood from every border 'O'.
    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    # 2. Final sweep.
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"          # surrounded → capture
            elif board[r][c] == "#":
                board[r][c] = "O"          # safe → restore
```

- **Time:** `O(m*n)` — the border floods touch each cell at most once, and the
  final sweep is one pass.
- **Space:** `O(m*n)` worst case for the recursion stack / BFS queue (no extra
  visited matrix needed since `'#'` doubles as the marker).

## Key Insights & Edge Cases

- **Solve the complement.** Marking "safe" (border-connected) regions is far
  simpler than tracking whether each interior region touches an edge.
- **Only border cells seed the flood** — that is the whole insight. Interior
  `'O'`s are never used as DFS roots.
- **Three-symbol state** (`'X'`, `'O'`, `'#'`) lets you distinguish safe from
  surrounded in the final pass; remember to restore `'#'` back to `'O'`.
- **No `'O'`s / all border `'O'`s** → board unchanged (Examples 2 and 3).
- **`1 x n` or `m x 1` boards:** every cell is on the border, so nothing is ever
  captured.
- **In-place mutation** is required — return `None`, do not build a new board.
