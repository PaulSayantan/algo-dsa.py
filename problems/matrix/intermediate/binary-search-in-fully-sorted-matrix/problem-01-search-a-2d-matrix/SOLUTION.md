# Solution — Search a 2D Matrix

## Brute Force

Scan every cell and compare to `target`.

```python
for row in matrix:
    for value in row:
        if value == target:
            return True
return False
```

- **Time:** `O(m * n)` — visits every element in the worst case.
- **Space:** `O(1)`.

A slightly better brute force uses the sorted property partially: binary search
the *column of first elements* to find the candidate row, then binary search that
row. That is `O(log m + log n)` and is perfectly acceptable, but the single-pass
flat binary search below is cleaner and has identical complexity.

## Optimal Approach — Binary Search in a Fully-Sorted Matrix

Because each row is sorted **and** each row starts after the previous row ends,
the row-major reading of the matrix is a single non-decreasing array of length
`m * n`. So we can binary search over the virtual index range `[0, m*n - 1]`
without ever building that array.

**The index-mapping identity.** A flat index `idx` in `[0, m*n - 1]` corresponds
to cell:

```
row = idx // n      # n = number of columns
col = idx %  n
```

This is the inverse of `idx = row * n + col`. It is the only trick you need.

**Algorithm.**

1. Let `m = len(matrix)`, `n = len(matrix[0])`.
2. Set `lo = 0`, `hi = m * n - 1`.
3. While `lo <= hi`:
   - `mid = (lo + hi) // 2`.
   - `value = matrix[mid // n][mid % n]`.
   - If `value == target`, return `True`.
   - If `value < target`, move right: `lo = mid + 1`.
   - Else move left: `hi = mid - 1`.
4. If the loop ends, `target` is absent — return `False`.

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            value = matrix[mid // n][mid % n]
            if value == target:
                return True
            if value < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
```

**Why it is correct.** The virtual array `A[idx] = matrix[idx // n][idx % n]` is
non-decreasing thanks to the two matrix properties, so standard binary-search
correctness applies: the invariant "if `target` exists, its index lies in
`[lo, hi]`" is preserved at every step, and the search space shrinks by half each
iteration until the element is found or the range is empty.

- **Time:** `O(log(m * n))`.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **Column count `n`, not `m`, drives the mapping.** `row = idx // n` uses the
  number of *columns*. Mixing up `m` and `n` is the most common bug; when the
  matrix is not square it produces silently wrong indices.
- **Guard empty input.** If the matrix or its first row could be empty, return
  `False` immediately so `m * n - 1` does not become `-1` and index out of range.
  (LeetCode 74 guarantees `m, n >= 1`, so this is optional there.)
- **Integer overflow.** Not a concern in Python, but in C++/Java prefer
  `mid = lo + (hi - lo) // 2` to avoid `lo + hi` overflowing.
- **Single-cell and single-row/column matrices** work with no special casing —
  the range `[0, m*n - 1]` handles them uniformly.
- **This only works when rows are chained.** If it is a row/column-sorted matrix
  where `matrix[i][0]` is *not* guaranteed larger than `matrix[i-1][n-1]`
  (LeetCode 240), the flat array is not sorted and you must use a different
  method (staircase search from the top-right corner).
