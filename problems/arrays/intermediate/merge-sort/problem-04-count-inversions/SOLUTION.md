# Solution — Count Inversions

## Brute Force

Check every pair `(i, j)` with `i < j` and increment a counter whenever
`nums[i] > nums[j]`.

```python
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] > nums[j]:
            count += 1
```

- **Time:** `O(n^2)` — far too slow for `n = 10^5` (`~5 * 10^9` comparisons).
- **Space:** `O(1)`.

## Optimal Approach (Merge Sort, count during merge)

Key observation: inversions can be split into three groups —

1. inversions entirely within the left half,
2. inversions entirely within the right half,
3. **split inversions**, where `i` is in the left half and `j` is in the right.

Groups 1 and 2 are counted by the recursive calls. The magic is counting group 3
*for free* during the merge, because both halves are already sorted.

During the merge, keep left pointer `i` and right pointer `j`. When
`left[i] <= right[j]`, no inversion (left element is not greater). When
`left[i] > right[j]`, then `right[j]` is smaller than `left[i]` **and every
element after `left[i]` in the (sorted) left half** — all of those are greater
than `right[j]` and sit at earlier original positions. So add `len(left) - i` to
the count in one shot.

```python
def countInversions(self, nums):
    self.count = 0
    self._sort(nums)
    return self.count

def _sort(self, arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = self._sort(arr[:mid])
    right = self._sort(arr[mid:])
    return self._merge(left, right)

def _merge(self, left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
            self.count += len(left) - i   # all remaining left > right[j]
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
```

**Why it is correct.** Using `left[i] <= right[j]` (i.e. taking from the left on
ties) ensures equal values are **not** counted as inversions (we need strict
`>`). When we take `right[j]`, the elements `left[i..end]` are all strictly
greater than `right[j]` (the left half is sorted) and all originally precede
`right[j]` (left half indices are smaller), so each is a valid inversion. Summing
`len(left) - i` over all such events, plus the recursive sub-counts, yields every
inversion exactly once, partitioned by the split above.

**Complexity.**

- **Time:** `O(n log n)` — same recurrence as merge sort; the counting is `O(1)`
  extra per merge step.
- **Space:** `O(n)` for the merge buffers plus `O(log n)` recursion.

### Worked trace on `[2,4,1,3,5]`

- Sort `[2,4]` -> `[2,4]`, 0 inversions.
- Sort `[1,3,5]`: split `[1]` and `[3,5]` -> `[1,3,5]`, 0 inversions.
- Merge `[2,4]` with `[1,3,5]`:
  - `2 > 1` -> take 1, add `len(left)-i = 2-0 = 2` (pairs `(2,1)`,`(4,1)`).
  - `2 <= 3` -> take 2.
  - `4 > 3` -> take 3, add `2-1 = 1` (pair `(4,3)`).
  - `4 <= 5` -> take 4; drain right.
- Total = `2 + 1 = 3`. Matches.

## Key Insights & Edge Cases

- **Add `len(left) - i`, not `1`:** the whole point is counting inversions in
  bulk; adding 1 degrades to the brute-force logic and misses pairs.
- **Ties:** use `<=` when comparing so equal elements are not counted (inversion
  needs strict greater-than).
- **Overflow:** the count can exceed 32-bit range (`~5 * 10^9`); use a 64-bit type
  in languages like Java/C++. Python is fine natively.
- **Already sorted / single element:** returns `0` (Example 3). **Strictly
  descending:** returns `n(n-1)/2` (Example 2), a good sanity check.
- Do not mutate the input if the caller needs it; work on copies (`arr[:mid]`).
