# Solution — Game of Life

## Brute Force

Allocate a full copy of the board, read neighbor counts from the copy, and write
the next generation into the original (or vice versa).

```python
def gameOfLife(board):
    m, n = len(board), len(board[0])
    snapshot = [row[:] for row in board]
    for i in range(m):
        for j in range(n):
            live = sum(
                snapshot[i + di][j + dj]
                for di in (-1, 0, 1) for dj in (-1, 0, 1)
                if (di or dj) and 0 <= i + di < m and 0 <= j + dj < n
            )
            if snapshot[i][j] == 1:
                board[i][j] = 1 if live in (2, 3) else 0
            else:
                board[i][j] = 1 if live == 3 else 0
```

- **Time:** `O(m·n)` — each cell inspects at most 8 neighbors (constant).
- **Space:** `O(m·n)` — the snapshot copy.

## Optimal Approach (Two-State Encoding in One Cell)

**Idea:** a cell only ever needs to remember two bits: its **old** state (which
neighbors read) and its **new** state (what it becomes). We can store both in a
single integer using a 2-bit encoding, so the same grid simultaneously holds
both generations and no copy is needed.

Encoding used below: **bit 0 = old state**, **bit 1 = new state**.

- Old live cell that stays/becomes live -> set bit 1 -> value becomes `3`
  (`0b11`).
- Old dead cell that becomes live -> set bit 1 -> value becomes `2` (`0b10`).
- Cells that end dead keep bit 1 clear.

Because neighbor counting always looks at `cell & 1` (the *old* bit), writes to
bit 1 do not disturb the counts of not-yet-processed neighbors.

### Step by step

1. For each cell `(i, j)`, count live neighbors as
   `sum(board[r][c] & 1 for each of the 8 in-bounds neighbors)`. The `& 1`
   guarantees we read the *original* state even if that neighbor's bit 1 was
   already set this pass.
2. Decide the next state from the rules and, if the cell should be live next
   generation, set bit 1: `board[i][j] |= 2`. Dead-next cells are left as-is
   (bit 1 stays 0).
3. After every cell is processed, do a second pass and shift each cell right by
   one bit: `board[i][j] >>= 1`, which discards the old state and promotes the
   new state to bit 0.

```python
def gameOfLife(board):
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            live = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    r, c = i + di, j + dj
                    if 0 <= r < m and 0 <= c < n:
                        live += board[r][c] & 1  # read OLD state only
            if board[i][j] & 1:
                if live == 2 or live == 3:
                    board[i][j] |= 2
            else:
                if live == 3:
                    board[i][j] |= 2
    for i in range(m):
        for j in range(n):
            board[i][j] >>= 1
```

### Why it is correct

- **Simultaneity is preserved** because the old state lives in bit 0 and is
  never modified during the counting/marking pass — we only ever *set* bit 1.
  Any neighbor read via `& 1` therefore always returns the previous generation's
  value, exactly as the simultaneous update rule demands.
- **The final shift** atomically converts every cell to its new generation:
  values `0`/`1` (bit 1 clear) become `0`, values `2`/`3` (bit 1 set) become
  `1`.

### Complexity

- **Time:** `O(m·n)` — constant work (≤8 neighbors) per cell across two passes.
- **Space:** `O(1)` extra — only the packed encoding inside the board.

## Key Insights & Edge Cases

- **Pick an encoding and be consistent.** `next*2 + old` and the bit-flag scheme
  above are equivalent; the crucial invariant is that *reads for neighbor counts
  use the old bit only*.
- **The two-pass structure is mandatory.** You cannot shift-down in the same
  pass that counts neighbors, or you would expose new states to cells not yet
  processed.
- **Boundary cells** simply have fewer in-bounds neighbors; the bounds check
  handles corners and edges uniformly.
- **1x1 board:** a lone cell has zero live neighbors, so a live cell dies and a
  dead cell stays dead (`[[0]]` -> `[[0]]`).
- **Follow-up (infinite board):** for a truly unbounded grid you would instead
  track only the coordinates of live cells in a set and tally neighbor counts
  with a dictionary — the in-place bit trick assumes a fixed finite grid.
