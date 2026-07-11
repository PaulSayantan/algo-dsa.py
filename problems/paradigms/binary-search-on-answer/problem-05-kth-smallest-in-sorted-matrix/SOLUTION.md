# Solution - Kth Smallest Element in a Sorted Matrix

## Brute Force

Flatten all `n^2` elements, sort, and index.

```python
flat = sorted(v for row in matrix for v in row)
return flat[k - 1]
```

- **Time:** `O(n^2 log n)` — sorting all elements.
- **Space:** `O(n^2)` — violates the "better than `O(n^2)` memory" requirement.

A heap-based merge of the sorted rows does better (`O(k log n)` time,
`O(n)` space), but here we highlight the answer-space search, which is simplest to
reason about and uses `O(1)` extra memory.

## Optimal Approach (Binary Search on Answer)

Binary-search the **value** `v`, not a position. The candidate range is
`[matrix[0][0], matrix[n-1][n-1]]` (the smallest and largest entries, since rows
and columns are sorted).

Define `count_le(v)` = the number of matrix entries `<= v`. This count is
**monotonically non-decreasing** in `v`. The answer is the **smallest value `v`
that is actually present in the matrix and satisfies `count_le(v) >= k`.**
Crucially, when the loop lands on the smallest `v` with `count_le(v) >= k`, that
`v` must itself be a matrix element — otherwise `count_le(v - 1)` would already be
`>= k`, contradicting minimality — so we can return `lo` directly.

Counting `<= v` in `O(n)`: start at the **bottom-left** corner. If the current
entry `<= v`, the entire column above it in this "staircase" also qualifies, so
add `row + 1` and move right; otherwise move up.

```python
def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    n = len(matrix)

    def count_le(v: int) -> int:
        # Count entries <= v by walking from the bottom-left corner.
        count = 0
        row, col = n - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] <= v:
                count += row + 1   # this entry and all above it in the column
                col += 1
            else:
                row -= 1
        return count

    lo, hi = matrix[0][0], matrix[n - 1][n - 1]
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if count_le(mid) >= k:   # enough elements <= mid → answer is mid or lower
            hi = mid
        else:                    # too few → answer is larger
            lo = mid + 1
    return lo
```

### Why it is correct

`count_le` is non-decreasing in `v`, so `check(v) = (count_le(v) >= k)` flips from
`False` to `True` exactly once — the "first True" template applies. Let `v*` be
that first `True` value. If `v*` were **not** in the matrix, then no element lies
in `(v* - 1, v*]`, so `count_le(v* - 1) == count_le(v*) >= k`, making `v* - 1`
also `True` and contradicting that `v*` is the first. Hence `v*` is a real matrix
element and is exactly the `k`-th smallest (it has `< k` elements strictly below
it and `>= k` elements `<= it`).

### Step-by-step (Example 1, k = 8)

Range `[1, 15]`. Sorted values are `[1,5,9,10,11,12,13,13,15]`; the 8th is `13`.

| lo | hi | mid | count_le(mid) | >= 8 | action  |
|----|----|-----|---------------|------|---------|
| 1  | 15 | 8   | 2             | no   | lo = 9  |
| 9  | 15 | 12  | 6             | no   | lo = 13 |
| 13 | 15 | 14  | 8             | yes  | hi = 14 |
| 13 | 14 | 13  | 8             | yes  | hi = 13 |
| 13 | 13 | —   | —             | stop | ret 13  |

Answer: `13`.

- **Time:** `O(n * log(hi - lo))` — each `count_le` is `O(n)`, run over
  `O(log(range))` iterations. With `n <= 300` and a value range up to `2*10^9`,
  this is tiny.
- **Space:** `O(1)` extra.

## Key Insights & Edge Cases

- **Search the value axis, not the index axis.** The matrix is not fully sorted,
  but the *count of elements <= v* is monotonic, which is all binary search needs.
- **Why the result is always a real element:** the first-True value cannot fall in
  a gap between actual entries — proven above. This is what lets us `return lo`
  without a separate lookup.
- **`count_le` staircase walk is `O(n)`**, not `O(n log n)`: exploiting both row
  and column sorting from the bottom-left corner. A simpler `bisect` per row is
  `O(n log n)` and also fine for `n <= 300`.
- **Duplicates counted separately** are handled automatically because `count_le`
  counts positions, not distinct values (Example 3 returns the duplicate `1`).
- **`n == 1`** returns the single element (Example 2); the range collapses
  immediately.
- **Use `lo + (hi - lo) // 2`** for the midpoint to avoid overflow in
  fixed-width-integer languages when values are near `10^9`.
