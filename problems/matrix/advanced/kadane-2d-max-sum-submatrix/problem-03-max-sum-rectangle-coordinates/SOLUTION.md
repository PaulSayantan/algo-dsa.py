# Solution — Maximum Sum Rectangle with Coordinates

## Brute Force

Enumerate all `(top, bottom, left, right)` quadruples and, with a 2D prefix-sum
table, evaluate each rectangle's sum in `O(1)`. Keep the best sum and remember
the quadruple that produced it.

- **Time:** `O(n² · m²)`.
- **Space:** `O(n · m)` for the prefix table.

This directly reports coordinates but is too slow for `n = m = 300`.

## Optimal Approach — Kadane 2D with index tracking

Same skeleton as the plain max-sum-rectangle problem, but the 1D Kadane
subroutine now also returns *where* its best window starts and ends, and the
outer loop records the full bounding box on every strict improvement.

**Step by step:**

1. For each `top` row, reset `colSum = [0] * m`.
2. For each `bottom >= top`, add row `bottom` into `colSum` (incremental
   compression, `O(m)`).
3. Run an index-tracking Kadane on `colSum`. It returns
   `(local_best, left, right)` — the max contiguous sum and its column bounds.
   The trick is a *tentative start* pointer that resets whenever we restart the
   window.
4. If `local_best > best`, update `best` and store
   `(top, left, bottom, right)`.

```python
def kadane_with_bounds(col):
    cur = col[0]
    best = col[0]
    start = 0          # tentative window start
    left = right = 0   # best window bounds
    for j in range(1, len(col)):
        if cur < 0:            # restart is better than extending
            cur = col[j]
            start = j
        else:
            cur += col[j]
        if cur > best:         # strict improvement -> record bounds
            best = cur
            left, right = start, j
    return best, left, right


def maxSumRectangle(matrix):
    n, m = len(matrix), len(matrix[0])
    best = float("-inf")
    box = (0, 0, 0, 0)
    for top in range(n):
        col = [0] * m
        for bottom in range(top, n):
            for c in range(m):
                col[c] += matrix[bottom][c]
            local, left, right = kadane_with_bounds(col)
            if local > best:
                best = local
                box = (top, left, bottom, right)
    return best, box
```

**Why it is correct.** Correctness of the *sum* is identical to the plain
Kadane 2D argument: every rectangle maps to a (row band, column band) pair, and
the algorithm evaluates the optimum over all of them. For the *coordinates*,
note the invariant that `kadane_with_bounds` maintains: at index `j`, `start` is
the left end of the best subarray ending at `j`, because `start` is reset to `j`
exactly when extending would be worse than restarting. Whenever `cur` sets a new
window record, `[start, j]` are its true bounds. The outer loop pairs those
column bounds with the current row band, so the stored box always corresponds to
the recorded `best` sum.

- **Time:** `O(n² · m)`.
- **Space:** `O(m)`.

## Key Insights & Edge Cases

- **Strict vs. non-strict update:** Using `cur > best` (strict) for recording
  bounds yields a deterministic tie-break: the first window that reaches the max
  wins. Switching to `>=` changes *which* equal-sum rectangle you report.
- **Tentative start must reset on restart, not on improvement:** A common bug is
  updating `start` only when `best` improves. It must reset the moment the
  running window restarts (`cur < 0` branch), otherwise the reported `left` can
  precede the actual window.
- **All-negative matrix:** Both `cur` and `best` are seeded from `col[0]`, so
  the routine returns the single largest cell and a `1 × 1` box — never an empty
  rectangle and never sum `0`.
- **Ties across row bands:** With strict `>`, an earlier (smaller `top`) row
  band is preferred over a later one of equal sum.
- **Transpose optimization:** As before, orient the matrix so the squared factor
  is on the smaller dimension; remember to swap the returned coordinates back if
  you transpose.
