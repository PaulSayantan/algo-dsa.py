# Solution — Maximum Rectangle Overlap

## Brute Force

Keep a `count` grid, and for each rectangle increment every interior cell; then
scan for the maximum.

```python
for x1, y1, x2, y2 in rectangles:
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            count[x][y] += 1
return max(max(row) for row in count)
```

- **Time:** `O(R * A)` where `R` is the number of rectangles and `A` is the
  area of the largest rectangle. With `R = 10^5` and rectangles up to
  `1001 x 1001`, this is on the order of `10^11` — far too slow.
- **Space:** `O(C^2)` for a `C x C` coordinate grid.

## Optimal Approach (2D Difference Array)

The coverage count is exactly "how many rectangles add `+1` to this cell." That
is a batch of rectangle range-adds followed by one readout — the textbook use of
a 2D difference array.

### Steps

1. Allocate `diff` of size `(C + 2) x (C + 2)` where `C = 1000` (max coordinate),
   so the `x2 + 1` / `y2 + 1` writes stay in bounds.
2. For each rectangle apply the four corner deltas (`O(1)` each):

   ```
   diff[x1  ][y1  ] += 1
   diff[x2+1][y1  ] -= 1
   diff[x1  ][y2+1] -= 1
   diff[x2+1][y2+1] += 1
   ```

3. Run the 2D prefix sum. After the sweep, `diff[x][y]` holds the number of
   rectangles covering cell `(x, y)`.
4. The answer is the maximum value in the reconstructed grid.

### Why it is correct

Each rectangle contributes `+1` to precisely the cells it covers (the
inclusion–exclusion corners confine the flood to the rectangle). Summed over all
rectangles, the prefix-sum value at a cell equals its overlap depth. The maximum
depth is then a single grid scan.

### Reference implementation

```python
def max_rectangle_overlap(rectangles):
    C = 1000
    diff = [[0] * (C + 2) for _ in range(C + 2)]

    for x1, y1, x2, y2 in rectangles:      # O(1) per rectangle
        diff[x1][y1]         += 1
        diff[x2 + 1][y1]     -= 1
        diff[x1][y2 + 1]     -= 1
        diff[x2 + 1][y2 + 1] += 1

    best = 0
    for x in range(C + 1):
        for y in range(C + 1):
            top    = diff[x - 1][y] if x else 0
            left   = diff[x][y - 1] if y else 0
            corner = diff[x - 1][y - 1] if (x and y) else 0
            diff[x][y] += top + left - corner
            best = max(best, diff[x][y])
    return best
```

- **Time:** `O(R + C^2)` — constant work per rectangle plus one grid sweep.
- **Space:** `O(C^2)` for the difference grid.

## Key Insights & Edge Cases

- Grid dimensions are driven by the **coordinate bound**, not the rectangle
  count, so many rectangles cost only `O(R)` extra time.
- Always pad by an extra row/column so `x2 + 1` and `y2 + 1` are valid indices.
- If coordinates were large or sparse (e.g. up to `10^9`) you would first
  **compress coordinates** and treat cells as compressed blocks (see Rectangle
  Area II) — but with a small bound a direct grid is simplest.
- A single rectangle yields answer `1`; fully nested identical rectangles yield
  `R`.
- Overlap "depth" counts touching-inclusive corners, so rectangles sharing only
  an edge or corner **do** overlap on that shared cell.
