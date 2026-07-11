# Solution — Reverse Pairs

## Brute Force

Test every pair `(i, j)` with `i < j` for `nums[i] > 2 * nums[j]`.

```python
def reversePairs_brute(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > 2 * nums[j]:
                count += 1
    return count
```

- **Time:** `O(n^2)`.
- **Space:** `O(1)`.

Times out for `n = 5 * 10^4` (≈ 1.25 * 10^9 comparisons).

## Optimal Approach — Count Inversions (Merge Sort)

This is a generalized inversion count where the pair condition
`nums[i] > 2 * nums[j]` differs from the ordering (`<`) used to sort. That one
difference forces a structural change: we **count first, then merge**.

Within `sort_count(lo, hi)`:

1. Recurse into the two halves so each becomes sorted and its internal reverse
   pairs are counted.
2. **Counting phase (before merging).** Both halves are sorted ascending. Use a
   pointer `j` into the right half that only ever moves forward. For each `i` in
   the left half (also in ascending order), advance `j` while
   `nums[left_i] > 2 * nums[right_j]`. Add `(j - right_start)` to the count.
   Because both halves are sorted, as `left_i` increases the threshold
   `2 * nums[right_j]` requirement is easier to satisfy, so `j` never needs to
   move backward — a single linear sweep across the level.
3. **Merge phase.** Do the ordinary merge to produce the sorted combined
   subarray for the parent call.

Keeping the counting and merging as two separate passes is the clean way to
handle the fact that the condition uses `2 * nums[j]` rather than plain `nums[j]`.
Trying to fold the count into the comparison inside the merge is error-prone here.

### Why it is correct

Every reverse pair with `i` in the left half and `j` in the right half is a
"cross pair" counted in phase 2; pairs entirely inside a half are counted by
recursion. The three groups are disjoint and exhaustive, so each pair is counted
once. The monotone pointer is valid because both halves are sorted: if
`left[a] > 2*right[b]` holds, then for any larger left value `left[a'] >= left[a]`
it also holds for the same `b`, so the count of qualifying `j` for successive
`i` is non-decreasing.

### Step-by-step on `nums = [1, 3, 2, 3, 1]`

The only reverse pairs come from the trailing `1` (`j = 4`, `2*1 = 2`), paired
with the two `3`s. During the top-level merge of the sorted left half
`[1, 2, 3]` (originally indices 0–2) and sorted right half `[1, 3]` (indices
3–4), plus the deeper levels, the counting phases together find exactly the
pairs `(1,4)` and `(3,4)` → total `2`. ✓

### Reference implementation

```python
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def sort_count(arr: List[int]) -> int:
            n = len(arr)
            if n <= 1:
                return 0
            mid = n // 2
            left, right = arr[:mid], arr[mid:]
            inv = sort_count(left) + sort_count(right)

            # counting phase: both halves sorted ascending
            j = 0
            for x in left:
                while j < len(right) and x > 2 * right[j]:
                    j += 1
                inv += j

            # merge phase
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]; i += 1
                else:
                    arr[k] = right[j]; j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]; i += 1; k += 1
            while j < len(right):
                arr[k] = right[j]; j += 1; k += 1
            return inv

        return sort_count(nums[:])
```

- **Time:** `O(n log n)` — the counting sweep and the merge are each `O(n)` per
  level, over `log n` levels.
- **Space:** `O(n)` for the temporary halves plus `O(log n)` stack.

## Key Insights & Edge Cases

- **Count before merge.** The counting condition (`> 2 * right[j]`) is different
  from the merge condition (`<=`), so counting must be its own pass. Do not
  reuse the merge comparison to count.
- **Overflow.** `2 * nums[j]` and the comparison with `nums[i]` can exceed 32-bit
  range near `±2^31`. Python is safe; in C++/Java cast to 64-bit before doubling
  (`(long) nums[j] * 2`). Comparing `nums[i] > 2*nums[j]` is preferable to
  `nums[i] / 2 > nums[j]` because integer division loses information.
- **Monotone pointer.** The right pointer `j` is reset once per merge level and
  only advances; do not restart it for each left element or you get `O(n^2)`.
- **Single element / all increasing:** yields `0`. Strictly decreasing large
  values can approach the maximum count; use 64-bit accumulators.
