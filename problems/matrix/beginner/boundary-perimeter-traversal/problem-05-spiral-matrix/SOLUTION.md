# Solution — Spiral Matrix

## Brute Force

Simulate a walker that moves in the current direction (right, down, left, up) and turns
clockwise whenever the next cell is out of bounds or already visited. Maintain a
`visited` boolean grid the same size as the matrix.

```python
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
```

This works and also runs in `O(m * n)` time, but it costs `O(m * n)` **extra space** for
the `visited` grid and pays a bounds/visited check per cell.

- **Time:** `O(m * n)`.
- **Space:** `O(m * n)` for the visited grid.

## Optimal Approach — Boundary / Perimeter Traversal, ring by ring

Keep four shrinking boundaries. Each iteration of the outer `while` loop traverses **one
ring** (a boundary traversal of the current sub-matrix), then contracts the boundaries
inward. No visited grid is needed — the boundaries themselves encode what is left.

```python
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result: List[int] = []

        while top <= bottom and left <= right:
            # top row, left -> right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # right column, top -> bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # bottom row, right -> left (only if a row remains)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # left column, bottom -> top (only if a column remains)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
```

### Why it is correct

- Each `while` iteration emits the perimeter of the rectangle
  `[top..bottom] x [left..right]` in clockwise order, then shrinks that rectangle by one
  on every side. Because every cell belongs to exactly one ring, each cell is emitted
  once.
- After emitting the top row we do `top += 1`; the right-column sweep therefore starts at
  the new `top`, avoiding a repeat of the top-right corner. The same offset logic applies
  at each corner.
- The `if top <= bottom` guard before the bottom-row sweep prevents re-emitting a row
  that the top-row sweep already consumed in a thin (1-row-tall) leftover strip. The
  `if left <= right` guard does the same for a 1-column-wide leftover strip. These are
  the spiral analogues of the `top != bottom` / `left != right` guards in a single
  boundary traversal.
- The loop stops as soon as the boundaries cross (`top > bottom` or `left > right`),
  i.e. when nothing is left.

### Step-by-step on Example 1

Matrix `[[1,2,3],[4,5,6],[7,8,9]]`.

- **Ring 1:** top row `1,2,3` (`top→1`); right col `6,9` (`right→1`);
  `top(1)<=bottom(2)` bottom row `8,7` (`bottom→1`); `left(0)<=right(1)` left col `4`
  (`left→1`).
- Now `top=1, bottom=1, left=1, right=1`. **Ring 2:** top row `5` (`top→2`); right-col
  sweep `range(2,2)` empty (`right→0`); `top(2)<=bottom(1)` is false, skip; `left(1)<=
  right(0)` is false, skip.
- Loop condition `top(2) <= bottom(1)` now false → stop.
- Result: `[1,2,3,6,9,8,7,4,5]`. Correct.

### Complexity

- **Time:** `O(m * n)` — every cell is appended exactly once.
- **Space:** `O(1)` beyond the output list (no visited grid).

## Key Insights & Edge Cases

- **Spiral = iterated boundary traversal.** One ring per outer-loop pass; shrinking the
  four bounds is what makes the traversal spiral inward. This is the payoff of mastering
  the single-ring version in problems 1–4.
- **The two inner guards are essential.** Without `if top <= bottom` / `if left <= right`,
  a leftover single row or single column gets traversed twice (once as "top/right", once
  as "bottom/left"), producing duplicates. Examples 2 and 3 both exercise these guards.
- **Single row (`1 x n`).** First ring emits the whole row via the top-row sweep; the
  bottom-row and left-column sweeps are guarded out; loop then ends.
- **Single column (`m x 1`).** Top-row sweep emits `matrix[0][0]`, right-column sweep
  emits the rest; the guards skip the bottom/left sweeps. (See Example 3.)
- **`1 x 1` matrix.** One element emitted, then bounds cross.
- **Non-square matrices** are handled uniformly; there is no assumption that `m == n`.
