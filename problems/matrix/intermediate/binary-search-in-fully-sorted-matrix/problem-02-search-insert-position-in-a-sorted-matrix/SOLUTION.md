# Solution — Search Insert Position in a Sorted Matrix

## Brute Force

Walk the flattened matrix in order and count how many values are `< target`;
that count is exactly the insert position (`lower_bound`).

```python
count = 0
for row in matrix:
    for value in row:
        if value < target:
            count += 1
        else:
            return count   # first value >= target
return count               # target larger than everything -> m * n
```

- **Time:** `O(m * n)`.
- **Space:** `O(1)`.

## Optimal Approach — Binary Search in a Fully-Sorted Matrix (lower_bound)

The row-major reading of the matrix is a sorted array `A` of length `m * n`, where
`A[idx] = matrix[idx // n][idx % n]`. We want the smallest `idx` with
`A[idx] >= target` — the standard `lower_bound`. If no such element exists, the
answer is `m * n`.

Use a **half-open** binary search on `[0, m*n]`. Keeping `hi = m*n` (one past the
last index) lets the "insert at the end" case fall out naturally.

**Algorithm.**

1. `m, n = len(matrix), len(matrix[0])`.
2. `lo, hi = 0, m * n`  (note: `hi` is exclusive / one-past-the-end).
3. While `lo < hi`:
   - `mid = (lo + hi) // 2`.
   - If `matrix[mid // n][mid % n] < target`: everything up to and including `mid`
     is too small, so `lo = mid + 1`.
   - Else (`value >= target`): `mid` is a candidate, keep it in range: `hi = mid`.
4. Return `lo`.

```python
class Solution:
    def searchInsert(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n          # hi is exclusive
        while lo < hi:
            mid = (lo + hi) // 2
            if matrix[mid // n][mid % n] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
```

**Why it is correct.** The predicate `p(idx) = (A[idx] >= target)` is monotone:
once true, it stays true (the array is non-decreasing). The loop maintains the
invariant "the answer lies in `[lo, hi]`" and returns the first index where the
predicate flips from false to true — which is precisely `lower_bound`. When
`target` exceeds all elements, the predicate is false everywhere and `lo` walks up
to `hi = m * n`.

- **Time:** `O(log(m * n))`.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **Half-open interval is the clean formulation.** Initializing `hi = m * n`
  (exclusive) means the "append at the end" answer `m * n` needs no special case.
- **Never compare equal into the `lo` branch.** Use strict `<` when advancing
  `lo`; if you used `<=`, you would skip past valid equal elements and compute
  `upper_bound` instead of `lower_bound`.
- **`lower_bound` vs `upper_bound`.** To find the first index *strictly after* all
  copies of `target` (`upper_bound`), change the comparison to
  `value <= target -> lo = mid + 1`. That pairing powers the counting problem in
  problem 3.
- **Duplicates.** With repeated values, `lower_bound` returns the index of the
  *first* copy, which is the correct, stable insert position.
- **Empty matrix.** If the matrix could be empty, the loop never runs and returns
  `0`, which is the correct insert position into an empty sequence.
