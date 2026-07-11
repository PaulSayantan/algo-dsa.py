# Rectangle Area II

**Difficulty:** Hard

**Source:** LeetCode 850 — Rectangle Area II

## Description

You are given a 2D array `rectangles`, where
`rectangles[i] = [x1, y1, x2, y2]` denotes the `i`-th rectangle: `(x1, y1)` is
its bottom-left corner and `(x2, y2)` is its top-right corner.

Compute the **total area covered by all rectangles in the plane**. Any area
covered by two or more rectangles should be counted **only once** (the area of
the *union*).

Since the answer may be huge, return it **modulo `10^9 + 7`**.

## Constraints

- `1 <= rectangles.length <= 200`
- `rectangles[i].length == 4`
- `0 <= x1 < x2 <= 10^9`
- `0 <= y1 < y2 <= 10^9`
- The total area, before modulo, is guaranteed to fit in a 64-bit integer.

## Examples

### Example 1

```
Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
```

**Explanation:**
The three rectangles overlap heavily. Counting the union of their covered area
(each covered region once) gives a total of `6` square units.

### Example 2

```
Input: rectangles = [[0,0,2,2],[1,1,3,3]]
Output: 7
```

**Explanation:**
Each rectangle alone has area `4`, so the naive sum is `8`. They overlap in the
`1x1` square `[1,1]`–`[2,2]` (area `1`), which is double-counted, so the union
area is `8 - 1 = 7`.

## Hint

Coordinates are up to `10^9`, so you cannot build a literal grid. **Compress**
the distinct x- and y-coordinates into a small grid of cells, mark each cell
covered by any rectangle using a **2D Difference Array** (`+1` over each
rectangle's compressed span), then prefix-sum and sum the real areas of every
cell whose coverage count is positive.
