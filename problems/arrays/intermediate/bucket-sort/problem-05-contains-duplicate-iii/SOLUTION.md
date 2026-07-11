# Contains Duplicate III — Solution

## Brute Force

Check every pair within the index window.

```python
def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, min(i + indexDiff + 1, n)):
            if abs(nums[i] - nums[j]) <= valueDiff:
                return True
    return False
```

- **Time:** `O(n * indexDiff)`, up to `O(n^2)` when `indexDiff` is large.
- **Space:** `O(1)`.

Too slow for `n` up to `10^5` with a large window. Bucketing makes each step
`O(1)`.

## Optimal Approach (Bucketing by value)

**The insight:** partition the value axis into buckets of width `valueDiff + 1`.
Two numbers land in the **same** bucket only if they differ by at most
`valueDiff` — an instant hit. If they land in **adjacent** buckets, they *might*
be within `valueDiff`, so we do one explicit comparison. Numbers two or more
buckets apart always differ by more than `valueDiff`, so we can ignore them.

Combine this with a **sliding window of size `indexDiff`**: keep at most
`indexDiff` recent elements' buckets in a hash map. Because the window admits at
most one element per bucket at a time (any second element in the same bucket
would already be a hit), the map holds at most one value per bucket id.

### Steps

1. Let `w = valueDiff + 1` (bucket width). The bucket id of a value `x` is
   `x // w` (Python floor division works correctly for negatives).
2. Maintain a dict `bucket -> value` for elements in the current window.
3. For each index `i` with value `x` and bucket `b = x // w`:
   - If `b` is already occupied, return `True` (same bucket ⇒ diff `<= valueDiff`).
   - If bucket `b - 1` exists and `abs(x - bucket[b-1]) <= valueDiff`, return
     `True`.
   - If bucket `b + 1` exists and `abs(x - bucket[b+1]) <= valueDiff`, return
     `True`.
   - Otherwise insert `bucket[b] = x`.
   - If `i >= indexDiff`, evict the element that leaves the window:
     `del bucket[nums[i - indexDiff] // w]`.
4. If the loop finishes with no hit, return `False`.

```python
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        w = valueDiff + 1
        bucket = {}  # bucket id -> the value currently in the window

        for i, x in enumerate(nums):
            b = x // w
            if b in bucket:
                return True
            if b - 1 in bucket and abs(x - bucket[b - 1]) <= valueDiff:
                return True
            if b + 1 in bucket and abs(x - bucket[b + 1]) <= valueDiff:
                return True

            bucket[b] = x
            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // w]

        return False
```

### Why It Is Correct

Buckets have width `valueDiff + 1`, so any two values in the same bucket differ
by at most `valueDiff` — a valid pair. Any valid pair with difference
`<= valueDiff` must fall in the same bucket or in two adjacent buckets (their
ids differ by at most 1), so checking `b`, `b-1`, and `b+1` covers every
possible match. The window invariant — at most `indexDiff` most-recent elements
are in the map, and never two in one bucket (the second would have returned
`True`) — guarantees any pair we report also satisfies `abs(i - j) <= indexDiff`.
Eviction at step 3 keeps the window exactly aligned with the index constraint.

### Complexity

- **Time:** `O(n)`. Each element does `O(1)` dict lookups, one insert, and at
  most one eviction.
- **Space:** `O(min(n, indexDiff))` for the bucket map (at most `indexDiff + 1`
  entries live at once).

## Key Insights & Edge Cases

- **Bucket width `valueDiff + 1`, not `valueDiff`:** with width `valueDiff`, two
  values differing by exactly `valueDiff` could fall in adjacent buckets and be
  missed unless you also handle boundaries; the `+1` makes "same bucket" a clean
  sufficient condition.
- **`valueDiff = 0`:** width becomes `1`, so same-bucket means equal values —
  this degenerates to "Contains Duplicate II" (equal value within `indexDiff`),
  as in Example 1.
- **Negative numbers:** Python's floor division `//` buckets negatives
  consistently (e.g. `-1 // 3 == -1`). In languages with truncating division you
  must offset values or adjust the formula to avoid a broken bucket at zero.
- **Eviction timing:** evict `nums[i - indexDiff]` *after* processing `i`, so the
  window covers indices `[i - indexDiff, i]` — exactly `abs(i - j) <= indexDiff`.
- This is bucket sort's partitioning idea repurposed for *proximity search*
  rather than ordering: the buckets localize candidates so each query is `O(1)`.
