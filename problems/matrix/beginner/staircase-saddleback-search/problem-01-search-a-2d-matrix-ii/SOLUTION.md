# Solution — Search a 2D Matrix II

## Brute Force

Scan every cell and compare with `target`.

```python
for row in matrix:
    for value in row:
        if value == target:
            return True
return False
```

- **Time:** `O(m · n)` — visits every element in the worst case.
- **Space:** `O(1)`.

A better-but-not-optimal idea is to binary-search each of the `m` rows
independently: `O(m · log n)`. That works but ignores the column ordering, and
the staircase walk beats it while being simpler to reason about.

> Note: You **cannot** treat the whole matrix as one sorted array and do a single
> `O(log(m·n))` binary search, because rows are not globally chained — e.g. in
> Example 1, `matrix[0][4] = 15` is larger than `matrix[1][0] = 2`.

## Optimal Approach — Staircase / Saddleback Search

Start at the **top-right** corner `(r, c) = (0, n - 1)`. At each step compare
`matrix[r][c]` with `target`:

1. **Equal** → return `True`.
2. **`matrix[r][c] > target`** → the current value is the *smallest* in its column
   (column sorted ascending downward means everything below is even bigger), so
   the target cannot be anywhere in column `c`. Eliminate the column: `c -= 1`.
3. **`matrix[r][c] < target`** → the current value is the *largest* in its row
   (row sorted ascending rightward means everything to the left is even smaller),
   so the target cannot be anywhere in row `r`. Eliminate the row: `r += 1`.

Stop when `r` runs past the last row or `c` falls below `0`; that means the target
is absent → return `False`.

### Why it is correct

The starting corner is special: it is simultaneously the **maximum of its row**
and the **minimum of its column**. That is exactly what lets each comparison
discard a *whole* line without missing the target:

- If the corner is greater than the target, no cell below it (all larger) can
  match, so the entire column is safe to drop.
- If the corner is less than the target, no cell to its left (all smaller) can
  match, so the entire row is safe to drop.

The set of not-yet-eliminated cells always stays a rectangle whose top-right
corner is `(r, c)`, and the target — if present — is guaranteed to remain inside
that shrinking rectangle. The loop maintains this invariant until it either lands
on the target or shrinks the rectangle to nothing.

### Reference implementation

```python
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    r, c = 0, len(matrix[0]) - 1          # start at the top-right corner
    while r < len(matrix) and c >= 0:
        v = matrix[r][c]
        if v == target:
            return True
        elif v > target:
            c -= 1                        # drop the current column
        else:
            r += 1                        # drop the current row
    return False
```

### Complexity

- **Time:** `O(m + n)`. Each iteration increases `r` or decreases `c`, and neither
  can move more than `m` or `n` times respectively.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **Corner choice matters.** Top-right and bottom-left both work. The top-left and
  bottom-right corners are the *extremes* (global min / max) and give no
  disambiguating information, so they cannot drive the elimination.
- **Empty / single-cell inputs:** guard against an empty matrix or empty first row
  before indexing; a `1 x 1` matrix returns whether that one value equals target.
- **Duplicates** are fine — the walk still terminates in `O(m + n)`; it simply
  returns on the first match it encounters.
- **Bottom-left variant** (mirror image): start at `(m - 1, 0)`; if the value is
  `< target` move right (`c += 1`), if `> target` move up (`r -= 1`).
- This raw walk is the foundation for the counting variants in problems 2–5.
