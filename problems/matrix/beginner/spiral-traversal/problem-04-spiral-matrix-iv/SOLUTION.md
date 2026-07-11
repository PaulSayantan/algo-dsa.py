# Solution — Spiral Matrix IV

## Brute Force

Two-pass approach: first walk the linked list and copy its values into a Python
list `vals`. Then create the `m x n` grid pre-filled with `-1` and copy `vals`
into it using any spiral routine that stops after `len(vals)` writes.

- **Time:** `O(m * n)` — one pass to read the list (`<= m * n` nodes) plus one
  spiral pass over the grid.
- **Space:** `O(m * n)` for the extra `vals` list (on top of the output).

This works but the intermediate `vals` array is unnecessary — you can consume
the list directly during the spiral.

## Optimal Approach (Spiral Traversal with a moving list pointer)

Pre-fill the grid with `-1`, then run the standard clockwise boundary spiral.
Carry a pointer `cur = head`; each time you *would* write a cell, write
`cur.val` and advance `cur = cur.next` **only while `cur is not None`**. Once the
list is exhausted, simply stop writing — the untouched cells keep their `-1`.

```python
def spiralMatrix(m, n, head):
    grid = [[-1] * n for _ in range(m)]
    top, bottom, left, right = 0, m - 1, 0, n - 1
    cur = head
    while top <= bottom and left <= right and cur:
        for col in range(left, right + 1):
            if not cur:
                break
            grid[top][col] = cur.val
            cur = cur.next
        top += 1
        for row in range(top, bottom + 1):
            if not cur:
                break
            grid[row][right] = cur.val
            cur = cur.next
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                if not cur:
                    break
                grid[bottom][col] = cur.val
                cur = cur.next
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                if not cur:
                    break
                grid[row][left] = cur.val
                cur = cur.next
            left += 1
    return grid
```

**Why it's correct:** the boundary spiral visits cells in exactly the clockwise
order the problem specifies, so the `k`-th node lands in the `k`-th spiral cell.
Adding `and cur` to the `while` guard, plus the inner `if not cur: break`, makes
the writes stop the instant the list ends, leaving the remaining `-1` padding
untouched. Since node count `<= m * n`, we never run past the grid.

- **Time:** `O(m * n)` — the grid is filled with `-1` in `O(m * n)` and each
  spiral cell is visited once.
- **Space:** `O(1)` extra beyond the required output grid.

## Key Insights & Edge Cases

- **Padding for free.** Initializing the whole grid to `-1` up front means you
  never have to explicitly write the padding; you just stop early.
- **Two termination conditions coexist:** the boundary condition
  (`top <= bottom and left <= right`) ends the spiral when the grid is full,
  while `cur` becoming `None` ends it when the list is exhausted. Whichever fires
  first wins.
- **Single row / single column:** `m = 1, n = 4, head = [0,1,2]` gives
  `[[0, 1, 2, -1]]` — the row fills left to right and the last cell stays `-1`.
- **Exactly full:** when the list has `m * n` nodes (e.g. Example 3), no `-1`
  remains and the output is a normal spiral fill.
- **Large dimensions:** `m * n` can be up to `10^5`, so avoid recursion; the
  iterative boundary loop is `O(m * n)` and safe.
