# Rotating the Box — Solution

## Brute Force

Simulate gravity by repeatedly scanning each row and swapping any stone `#` that
has an empty `.` to its right, until no stone moves in a full pass. Then rotate
by building a new matrix cell-by-cell with the clockwise index map.

- Gravity: repeat "for each stone with `.` immediately to the right, swap them"
  until a pass makes no change. This can take up to `O(n)` passes per row.
- Rotation: `rotated[j][m-1-i] = settled[i][j]`.

**Time:** `O(m · n²)` in the worst case because a single stone can shuffle one
cell per pass and you may need `O(n)` passes.
**Space:** `O(m · n)` for the output.

## Optimal Approach (gravity + Rotate 90°)

Two clean phases.

**Phase 1 — gravity, in the original orientation.** In the pre-rotation frame,
"down" after a clockwise turn corresponds to stones sliding toward the **right
end** of each row, stopping at an obstacle `*` or the wall. Process each row from
right to left with a `write` pointer marking the next free landing slot:

```python
def rotateTheBox(box):
    m, n = len(box), len(box[0])
    for row in box:
        write = n - 1               # next slot a falling stone can occupy
        for j in range(n - 1, -1, -1):
            if row[j] == '*':       # obstacle: reset landing slot above it
                write = j - 1
            elif row[j] == '#':     # stone: move it to the landing slot
                row[j] = '.'
                row[write] = '#'
                write -= 1
    # Phase 2 — rotate 90 deg clockwise: transpose then reverse each row
    return [list(row) for row in zip(*box[::-1])]
```

The one-liner `zip(*box[::-1])` reverses the row order first and then transposes,
which is an equivalent formulation of a clockwise rotation (reverse-rows then
transpose == transpose then reverse-each-row). Written out explicitly:

```python
    transposed = [list(col) for col in zip(*box)]  # transpose
    for r in transposed:
        r.reverse()                                 # reverse each row
    return transposed
```

**Why it is correct:**

- *Gravity:* scanning right-to-left with a `write` pointer places each stone at
  the lowest available slot. When an obstacle is hit, `write` resets to just
  above it (`j - 1`), so stones cannot pass through obstacles. Each stone is
  moved at most once, so the pass is linear.
- *Rotation:* transpose-then-reverse-each-row implements the map
  `(i, j) → (j, m-1-i)`, the exact coordinate transform of a 90° clockwise
  rotation (see the folder README). The result has shape `n × m`.

**Step by step** on Example 2, `box = [["#",".","*","."],["#","#","*","."]]`:

1. Gravity row 0 (right to left): slots fill so row 0 → `[".","#","*","."]`.
   Row 1 → `[".","#","#","*"]`.
2. Rotate clockwise: transpose then reverse each row → the 4×2 grid
   `[["#","."],["#","#"],["*","*"],[".","."]]`. Correct.

**Time:** `O(m · n)` — one linear gravity pass over each row plus one `O(m · n)`
rotation. **Space:** `O(m · n)` for the returned matrix (gravity itself is
in-place; `O(1)` auxiliary beyond the output).

## Key Insights & Edge Cases

- **Do gravity BEFORE rotating.** After rotation the geometry is harder to
  reason about; settling stones in the original frame (fall = slide right) is the
  clean order.
- **Obstacles reset the landing pointer** to `j - 1`. Forgetting this lets stones
  tunnel through `*`.
- **The result is `n × m`, not `m × n`.** The box is generally not square, so the
  transpose changes the shape and you must allocate a new matrix.
- **Right-to-left scan with a single write pointer** keeps gravity at `O(n)` per
  row; a naive bubble-style simulation is `O(n²)` per row.
- Single row (`m == 1`) or single column (`n == 1`) still works: gravity settles
  within the one row, and the rotation turns a `1 × n` row into an `n × 1` column.
