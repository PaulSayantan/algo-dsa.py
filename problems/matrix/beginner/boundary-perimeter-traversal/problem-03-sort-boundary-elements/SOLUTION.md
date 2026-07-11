# Solution — Sort the Boundary Elements

## Brute Force

Collect boundary coordinates by scanning all `m * n` cells and testing the border
condition, sort the *values*, then assign them back. To place values correctly you must
walk the coordinates in a consistent clockwise order anyway, so the row-major collection
step still needs a reordering pass. Correct, but it examines every interior cell for
nothing.

- **Time:** `O(m * n + B log B)` where `B` is the number of boundary cells.
- **Space:** `O(B)` for the extracted values.

## Optimal Approach — Boundary / Perimeter Traversal (twice)

The clean pattern is **extract → sort → write back**, using the *same* clockwise
traversal for both the extract and write passes. Because both passes visit the ring in
identical order, the sorted values land exactly where they belong.

```python
from typing import List

def _clockwise_cells(m: int, n: int):
    """Yield boundary coordinates clockwise from the top-left corner."""
    top, bottom, left, right = 0, m - 1, 0, n - 1
    for j in range(left, right + 1):            # top row
        yield top, j
    for i in range(top + 1, bottom + 1):        # right column
        yield i, right
    if top != bottom:                           # bottom row (skip if 1 row)
        for j in range(right - 1, left - 1, -1):
            yield bottom, j
    if left != right:                           # left column (skip if 1 col)
        for i in range(bottom - 1, top, -1):
            yield i, left

def sort_boundary(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not matrix[0]:
        return matrix
    m, n = len(matrix), len(matrix[0])

    cells = list(_clockwise_cells(m, n))        # fixed clockwise order
    values = sorted(matrix[i][j] for i, j in cells)

    for (i, j), v in zip(cells, values):        # write back in the same order
        matrix[i][j] = v
    return matrix
```

### Why it is correct

- `_clockwise_cells` is the boundary-traversal generator; it enumerates each ring cell
  exactly once (the `top != bottom` / `left != right` guards prevent single-row or
  single-column double emission).
- `values` is the multiset of boundary values, sorted ascending.
- `zip(cells, values)` pairs the k-th clockwise cell with the k-th smallest value, so the
  minimum lands at the top-left corner and values increase clockwise. Interior cells are
  never in `cells`, so they are never written.

### Step-by-step on Example 1

Matrix `[[1,4,3],[7,5,2],[9,6,8]]`.

1. Clockwise cells: `(0,0)(0,1)(0,2)(1,2)(2,2)(2,1)(2,0)(1,0)`.
2. Their values: `[1, 4, 3, 2, 8, 6, 9, 7]`; sorted → `[1, 2, 3, 4, 6, 7, 8, 9]`.
3. Write back: `(0,0)=1,(0,1)=2,(0,2)=3,(1,2)=4,(2,2)=6,(2,1)=7,(2,0)=8,(1,0)=9`.
4. Result: `[[1,2,3],[9,5,4],[8,7,6]]`. Interior `5` untouched. Correct.

### Complexity

- **Time:** `O(B log B)` where `B = 2*(m + n) - 4` — dominated by the sort. Building
  `cells` is `O(B)`; the interior is never touched.
- **Space:** `O(B)` for the coordinate list and value list.

## Key Insights & Edge Cases

- **Same order both ways.** The single most important invariant: extraction order and
  write-back order must match. Materializing `cells` once and reusing it guarantees this.
- **Stability of duplicates.** Sorting equal values is fine; where two equal values land
  among each other does not matter since they are equal.
- **Single row / single column.** The guards make the generator emit each cell once, so
  "sort the boundary" degenerates to "sort the row/column", which is the expected result.
- **`1 x 1` matrix.** One cell, already sorted; returned unchanged.
- **In place vs. copy.** This writes back into the input matrix. If the caller must keep
  the original, deep-copy first.
