# Solution — Rotate the Boundary by K

## Brute Force

Rotate one step at a time, `k` times: on each step read the whole boundary, shift it by
one, and write it back. Each step is `O(B)`, so the total is `O(k * B)`. With `k` up to
`10^9` this is hopelessly slow. (Forgetting to reduce `k mod B` is the classic pitfall
that makes this brute force even worse than it needs to be.)

- **Time:** `O(k * B)`.
- **Space:** `O(B)`.

## Optimal Approach — Boundary / Perimeter Traversal + one cyclic shift

Extract the ring clockwise, cyclically shift the list by `k mod B` in one shot, then
write it back along the same clockwise path.

```python
from typing import List

def _clockwise_cells(m: int, n: int):
    top, bottom, left, right = 0, m - 1, 0, n - 1
    for j in range(left, right + 1):            # top row
        yield top, j
    for i in range(top + 1, bottom + 1):        # right column
        yield i, right
    if top != bottom:                           # bottom row
        for j in range(right - 1, left - 1, -1):
            yield bottom, j
    if left != right:                           # left column
        for i in range(bottom - 1, top, -1):
            yield i, left

def rotate_boundary(matrix: List[List[int]], k: int) -> List[List[int]]:
    if not matrix or not matrix[0]:
        return matrix
    m, n = len(matrix), len(matrix[0])

    cells = list(_clockwise_cells(m, n))
    values = [matrix[i][j] for i, j in cells]
    b = len(values)

    k %= b                                       # collapse full rotations
    # Clockwise-by-k: new position q holds the old element from (q - k) mod b.
    rotated = values[-k:] + values[:-k] if k else values

    for (i, j), v in zip(cells, rotated):
        matrix[i][j] = v
    return matrix
```

### Why it is correct

- `_clockwise_cells` enumerates the ring once in clockwise order (the guards prevent
  single-row/column double emission), so `values[p]` is the p-th boundary element
  clockwise from the top-left corner.
- "Rotate clockwise by `k`" means the element previously at clockwise index `p` should
  now sit at index `(p + k) mod b`. Equivalently, the value now at index `q` is the old
  value from `(q - k) mod b`. The slice `values[-k:] + values[:-k]` produces exactly this
  list (the last `k` elements move to the front).
- `k %= b` makes any `k` (even `10^9`) equivalent to a shift in `[0, b)`; `k == 0` leaves
  the ring unchanged.
- Writing `rotated` back along the identical `cells` order places each value on its
  correct boundary cell; interior cells are never in `cells`.

### Step-by-step on Example 1

Matrix `[[1,2,3],[8,9,4],[7,6,5]]`, `k = 1`.

1. Clockwise values: `[1,2,3,4,5,6,7,8]`, so `b = 8`.
2. `k %= 8` → `1`. `rotated = values[-1:] + values[:-1] = [8] + [1,2,3,4,5,6,7]
   = [8,1,2,3,4,5,6,7]`.
3. Write back clockwise: top `8,1,2`; right col `3,4`; bottom (reversed) `5,6`; left `7`.
4. Result: `[[8,1,2],[7,9,3],[6,5,4]]`; interior `9` untouched. Correct.

### Complexity

- **Time:** `O(B)` where `B = 2*(m + n) - 4` — one extraction, one slice, one write-back.
  Independent of `k` after the modulo.
- **Space:** `O(B)` for the value list.

## Key Insights & Edge Cases

- **Reduce `k` modulo `B` first.** This is what turns an `O(k*B)` approach into `O(B)`
  and is required to survive `k` up to `10^9`.
- **Direction convention.** Clockwise-by-`k` = shift the clockwise list *right* by `k`
  (`values[-k:] + values[:-k]`). Counter-clockwise would be a left shift
  (`values[k:] + values[:k]`). Match whichever the problem asks for.
- **`k == 0` (or `k % B == 0`).** No change; the slice guard returns `values` as-is.
- **Single row / single column.** `B = n` or `B = m`; rotating the ring rotates that row
  or column. Example 3 shows `k = 4, B = 3 → k = 1`.
- **`1 x 1` matrix.** `B = 1`, any `k % 1 == 0`, matrix unchanged.
- Same `extract → transform → write-back` skeleton as the "sort the boundary" problem;
  only the middle transform differs (cyclic shift vs. sort).
