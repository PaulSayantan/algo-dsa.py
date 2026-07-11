# Solution — Search in a Rotated Sorted Matrix

## Brute Force

Scan every cell; return its coordinates when it equals `target`.

```python
for r, row in enumerate(matrix):
    for c, value in enumerate(row):
        if value == target:
            return [r, c]
return [-1, -1]
```

- **Time:** `O(m * n)`.
- **Space:** `O(1)`.

This throws away the rotated-sorted structure.

## Optimal Approach — Binary Search in a Fully-Sorted Matrix (rotated variant)

The row-major flattening `A[idx] = matrix[idx // n][idx % n]` is a strictly
increasing array rotated left at an unknown pivot. We binary search over
`[0, m*n - 1]` using the LeetCode 33 insight:

> For any `mid`, at least one of the two halves `[lo, mid]` and `[mid, hi]` is
> **still fully sorted** (rotation introduces at most one "drop"). Identify the
> sorted half by comparing endpoints, test whether `target` lies within its value
> range, and recurse into the appropriate half.

**Algorithm.**

1. `m, n = len(matrix), len(matrix[0])`; `lo, hi = 0, m*n - 1`.
2. While `lo <= hi`:
   - `mid = (lo + hi) // 2`; `v = A[mid]`.
   - If `v == target`: return `[mid // n, mid % n]`.
   - **Left half sorted** (`A[lo] <= v`):
     - If `A[lo] <= target < v`: `hi = mid - 1` (target is in the sorted left).
     - Else: `lo = mid + 1`.
   - **Otherwise the right half is sorted** (`v <= A[hi]`):
     - If `v < target <= A[hi]`: `lo = mid + 1` (target is in the sorted right).
     - Else: `hi = mid - 1`.
3. Return `[-1, -1]`.

```python
class Solution:
    def searchRotated(self, matrix: List[List[int]], target: int) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        def val(idx: int) -> int:
            return matrix[idx // n][idx % n]

        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            v = val(mid)
            if v == target:
                return [mid // n, mid % n]
            if val(lo) <= v:                      # left half [lo, mid] is sorted
                if val(lo) <= target < v:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:                                 # right half [mid, hi] is sorted
                if v < target <= val(hi):
                    lo = mid + 1
                else:
                    hi = mid - 1
        return [-1, -1]
```

**Why it is correct.** A single left rotation of a sorted array creates exactly
one descent. For any `mid`, the segment not containing that descent is sorted, so
`A[lo] <= A[mid]` cleanly tells us the left segment is the sorted one (else the
right is). Within the sorted segment we can decide membership by a simple range
check on its two endpoints; if `target` is in that range we keep it, otherwise the
answer (if any) must be in the other segment. Because all values are distinct, the
comparisons are unambiguous and each step halves the range, giving logarithmic
time. When the loop exits, `target` is absent.

- **Time:** `O(log(m * n))`.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **`A[lo] <= A[mid]` decides the sorted half.** Use `<=` (not `<`) so a two-element
  or degenerate range where `lo == mid` still classifies the left half as sorted.
- **Range checks use half-open bounds around `mid`.** `A[lo] <= target < v` and
  `v < target <= A[hi]` deliberately exclude `v` (already handled by the equality
  check) and include the far endpoint.
- **Distinct values are assumed.** Duplicates (LeetCode 81) break the
  `A[lo] <= A[mid]` test — when `A[lo] == A[mid] == A[hi]` you cannot tell which
  side is sorted and must shrink the range by one, degrading the worst case to
  `O(m * n)`. This problem guarantees distinctness, so the clean `O(log(m*n))`
  logic applies.
- **No rotation (pivot 0).** A non-rotated array is a special case: the left half
  is always detected as sorted and the search behaves like an ordinary binary
  search.
- **Coordinate recovery.** Convert the found flat index once at the end with
  `[mid // n, mid % n]`; the column count `n` (not `m`) is the divisor.
- **Not present.** Falling out of the loop returns `[-1, -1]`.
