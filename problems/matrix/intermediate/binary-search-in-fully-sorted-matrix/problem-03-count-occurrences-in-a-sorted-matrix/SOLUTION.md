# Solution — Count Occurrences in a Sorted Matrix

## Brute Force

Iterate over every cell and increment a counter when a cell equals `target`.

```python
count = 0
for row in matrix:
    for value in row:
        if value == target:
            count += 1
return count
```

- **Time:** `O(m * n)`.
- **Space:** `O(1)`.

This ignores the sorted structure entirely.

## Optimal Approach — Binary Search in a Fully-Sorted Matrix (two bounds)

In a sorted sequence, all copies of `target` are **contiguous**. So the count is
just the width of that block:

```
count = upper_bound(target) - lower_bound(target)
```

- `lower_bound(target)` = first flat index whose value is `>= target`.
- `upper_bound(target)` = first flat index whose value is `>  target`.

Both are binary searches over the virtual array `A[idx] = matrix[idx // n][idx % n]`.
They differ only in the comparison operator, so a single helper parameterized by
strictness is the tidy way to write it.

**Algorithm.**

1. `m, n = len(matrix), len(matrix[0])`.
2. Define a helper `bound(x)` returning the first flat index with `A[idx] >= x`
   (half-open search on `[0, m*n]`).
3. `return bound(target + 1) - bound(target)`.
   - `bound(target)` is `lower_bound(target)`.
   - `bound(target + 1)` equals `upper_bound(target)` for integer values, since the
     first index `>= target + 1` is the first index `> target`.

```python
class Solution:
    def countOccurrences(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])

        def bound(x: int) -> int:
            """First flat index whose value is >= x (in [0, m*n])."""
            lo, hi = 0, m * n
            while lo < hi:
                mid = (lo + hi) // 2
                if matrix[mid // n][mid % n] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        return bound(target + 1) - bound(target)
```

**Why it is correct.** `bound(x)` is a correct `lower_bound` (see problem 2), so
`bound(target)` is the index of the first `target` (or where it would go if absent)
and `bound(target + 1)` is the index just past the last `target`. Their difference
is the number of elements equal to `target`. If `target` is absent, both bounds
land on the same index and the difference is `0`.

- **Time:** `O(log(m * n))` — two binary searches.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **`upper_bound(target) == lower_bound(target + 1)` only for integers.** The
  `+1` trick is clean here because values are integers. For floating-point or
  generic comparables, write a genuine `upper_bound` helper using `value <= target
  -> lo = mid + 1` instead.
- **Absent target gives 0 automatically.** No special case is needed — the two
  bounds coincide.
- **All-equal matrix.** If every cell equals `target`, `lower_bound = 0` and
  `upper_bound = m * n`, so the count is the full size `m * n`.
- **Watch the mapping constant.** `idx // n` and `idx % n` both use `n` (columns);
  reusing `m` there is the classic bug on non-square matrices.
- **Overflow.** `target + 1` is safe in Python; in fixed-width languages guard
  against `target == INT_MAX` (use a dedicated strict-comparison bound instead of
  `+1`).
