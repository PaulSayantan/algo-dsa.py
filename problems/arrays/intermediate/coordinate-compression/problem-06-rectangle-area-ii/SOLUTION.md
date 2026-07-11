# Rectangle Area II — Solution

## Brute Force

Compress *both* axes and test each compressed cell. Split the plane into a grid whose
vertical lines are the distinct x-coordinates and whose horizontal lines are the distinct
y-coordinates. Each grid cell is either entirely inside some rectangle or entirely outside
it, so mark every cell covered by any rectangle and sum the areas of the marked cells.

```python
def rectangleArea(rectangles):
    MOD = 10**9 + 7
    xs = sorted({x for r in rectangles for x in (r[0], r[2])})
    ys = sorted({y for r in rectangles for y in (r[1], r[3])})
    xi = {x: i for i, x in enumerate(xs)}
    yi = {y: i for i, y in enumerate(ys)}
    covered = [[False] * (len(ys) - 1) for _ in range(len(xs) - 1)]
    for x1, y1, x2, y2 in rectangles:
        for i in range(xi[x1], xi[x2]):
            for j in range(yi[y1], yi[y2]):
                covered[i][j] = True
    area = 0
    for i in range(len(xs) - 1):
        for j in range(len(ys) - 1):
            if covered[i][j]:
                area += (xs[i + 1] - xs[i]) * (ys[j + 1] - ys[j])
    return area % MOD
```

- **Time:** `O(n^3)` in the worst case — up to `O(n^2)` cells, each possibly touched by
  `O(n)` rectangles. With `n <= 200` this is ~10^7–10^8 and still passes.
- **Space:** `O(n^2)` for the grid.

This already *uses* coordinate compression (on both axes) and is a fine accepted solution.
The sweep-line refinement below keeps compression on one axis and is asymptotically better.

## Optimal Approach (Coordinate Compression + Sweep Line)

Compress only the **x-coordinates** into `k` distinct values, splitting the plane into `k-1`
vertical strips of known widths `xs[i+1] - xs[i]`. Now sweep a horizontal line upward through
the sorted **y**-edges. Each rectangle contributes two y-events: a `+1` at its bottom edge
`y1` and a `-1` at its top edge `y2`, each carrying the x-range `[x1, x2]` it covers.

Between two consecutive event y-values `y` and `y_next`, the set of active rectangles is
fixed. The covered width is the total width of strips that lie inside at least one active
rectangle, and that band contributes `covered_width * (y_next - y)` to the area.

```python
def rectangleArea(rectangles):
    MOD = 10**9 + 7
    xs = sorted({x for r in rectangles for x in (r[0], r[2])})
    xi = {x: i for i, x in enumerate(xs)}

    # events: (y, x1, x2, type)  type = +1 entering, -1 leaving
    events = []
    for x1, y1, x2, y2 in rectangles:
        events.append((y1, x1, x2, 1))
        events.append((y2, x1, x2, -1))
    events.sort()

    count = [0] * (len(xs) - 1)   # how many active rects cover each strip
    area = 0
    prev_y = events[0][0]
    for y, x1, x2, typ in events:
        # add the band between prev_y and y using the current coverage
        if y > prev_y:
            width = 0
            for i in range(len(xs) - 1):
                if count[i] > 0:
                    width += xs[i + 1] - xs[i]
            area += width * (y - prev_y)
            prev_y = y
        # apply this event to the strip counts
        for i in range(xi[x1], xi[x2]):
            count[i] += typ
    return area % MOD
```

**Why it is correct.**

- Compressing x into strips guarantees every strip is uniformly covered or uncovered by any
  given rectangle (a rectangle edge can only fall on a strip boundary, never mid-strip), so a
  per-strip active `count` exactly describes coverage.
- Sorting events by `y` and processing bottom edges (`+1`) and top edges (`-1`) makes `count`
  reflect precisely the rectangles spanning the current horizontal band.
- A strip is covered in a band iff `count[i] > 0`; multiplying the covered width by the band
  height `y - prev_y` and summing over all bands gives the union area, counting overlaps once
  because a strip's width is added once per band regardless of how many rectangles cover it.

**Step by step** on `[[0,0,2,2], [1,0,2,3], [1,0,3,1]]`:

- `xs = [0, 1, 2, 3]` -> strips widths `[1, 1, 1]` (strip 0: `[0,1]`, strip 1: `[1,2]`,
  strip 2: `[2,3]`).
- Events sorted by y (bottoms at y=0, tops at y=1,2,3).
- Band `[0,1]`: rects [0,0,2,2] (strips 0,1), [1,0,2,3] (strip 1), [1,0,3,1] (strips 1,2)
  active -> strips 0,1,2 covered, width 3, band height 1 -> area += 3.
- Band `[1,2]`: [1,0,3,1] has left (its top is y=1) -> strips 0,1 covered, width 2, height 1
  -> area += 2.
- Band `[2,3]`: [0,0,2,2] left (top y=2) -> only [1,0,2,3] active -> strip 1, width 1, height
  1 -> area += 1.
- Total `3 + 2 + 1 = 6`.

- **Time:** `O(n^2)` — `2n` events, each recomputing covered width over `O(n)` strips. (A
  segment tree keyed by the compressed x-strips reduces the per-event work to `O(log n)` for
  `O(n log n)` overall.)
- **Space:** `O(n)` for events and strip counts.

## Key Insights & Edge Cases

- **Compression makes strips uniform:** the whole method relies on the fact that between two
  consecutive distinct x-values, coverage never changes, so a strip is an atomic unit.
- **Apply the modulo only at the end** (or carefully), because taking it mid-sweep on partial
  widths/heights can corrupt the running geometric sums. Coordinates themselves are not
  reduced mod anything — only the final area is.
- **Huge coordinates (`10^9`) with a huge single rectangle:** area `10^18` overflows 32-bit
  and even flirts with 64-bit limits in some languages; reduce mod `10^9 + 7` at the end.
  `10^18 mod (10^9 + 7) = 49` (Example 2).
- **Half-open strips:** map a rectangle `[x1, x2]` to strip indices `[xi[x1], xi[x2] - 1]`
  (the loop `range(xi[x1], xi[x2])`), so adjacent rectangles sharing an x-edge don't
  double-count a strip.
- **Overlap counted once:** because coverage is a boolean-per-band (via `count > 0`), regions
  under multiple rectangles contribute their width exactly once per band.
