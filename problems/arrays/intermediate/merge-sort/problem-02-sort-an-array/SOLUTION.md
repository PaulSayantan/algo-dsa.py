# Solution — Sort an Array

## Brute Force

Selection / insertion sort: repeatedly find the next smallest element (or insert
each element into a growing sorted prefix).

- **Time:** `O(n^2)` — quadratic comparisons; too slow for `n = 5 * 10^4`.
- **Space:** `O(1)`.

This meets neither the "no built-in sort" spirit nor the `O(n log n)`
requirement, so we need a smarter algorithm.

## Optimal Approach (Merge Sort)

Merge sort is divide-and-conquer:

1. **Divide.** If the array has 0 or 1 elements it is already sorted (base case).
   Otherwise split it at the midpoint into `left` and `right`.
2. **Conquer.** Recursively sort `left` and `right`.
3. **Combine.** Merge the two sorted halves into one sorted array with a linear
   two-pointer scan.

```python
def sortArray(self, nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = self.sortArray(nums[:mid])
    right = self.sortArray(nums[mid:])
    return self._merge(left, right)

def _merge(self, left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:      # <= keeps the sort STABLE
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])          # drain whichever half remains
    result.extend(right[j:])
    return result
```

**Why it is correct.** By induction: the base case (length <= 1) is trivially
sorted. Assuming the recursive calls return sorted halves, `_merge` produces a
sorted union — at every step it appends the smallest element not yet emitted,
because the fronts of `left` and `right` are the smallest remaining candidates in
each already-sorted half.

**Complexity.**

- **Time:** `T(n) = 2 T(n/2) + O(n) = O(n log n)`. There are `log n` levels; each
  level merges a total of `n` elements.
- **Space:** `O(n)` for the temporary arrays created during merging, plus
  `O(log n)` recursion stack. (An index-based bottom-up or in-place-buffer variant
  can reduce allocation but not the asymptotic auxiliary `O(n)`.)

### Worked trace on `[5,2,3,1]`

```
split      -> [5,2] | [3,1]
split      -> [5]|[2]   [3]|[1]
merge      -> [2,5]     [1,3]
merge      -> [1,2,3,5]
```

## Key Insights & Edge Cases

- **Stability:** use `left[i] <= right[j]` (not `<`) so equal elements from the
  left half are emitted first, preserving relative order. It does not change the
  numeric answer here but is a habit worth keeping.
- **Guaranteed `O(n log n)`:** unlike quicksort, merge sort has no bad pivot
  worst case, which is exactly why LeetCode 912 uses adversarial inputs designed
  to blow up naive quicksort.
- **Base case** must handle length 0 and 1 — forgetting it causes infinite
  recursion.
- **Duplicates and negatives** (Examples 2 and 3) need no special handling; the
  comparison covers them.
- If Python recursion depth is a concern for very large `n`, an iterative
  bottom-up merge sort (merge runs of size 1, 2, 4, ...) avoids deep recursion.
