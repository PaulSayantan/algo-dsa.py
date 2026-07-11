# Solution — Search in Rotated Sorted Array

## Brute Force

Ignore the structure and scan every element.

```python
for i, v in enumerate(nums):
    if v == target:
        return i
return -1
```

- **Time:** O(n).
- **Space:** O(1).

Simple, but linear — it wastes the (rotated) sorted structure and misses the
required `O(log n)`.

## Optimal Approach (Modified Binary Search)

Key observation: when you split a rotated sorted array at any `mid`, **at least
one of the two halves `[lo, mid]` and `[mid, hi]` is fully sorted.** You can tell
which by comparing endpoints. Once you know which half is sorted, you can check
in O(1) whether the target lies within that sorted half's value range and decide
which way to go.

Algorithm (inclusive `[lo, hi]` template):

1. `lo = 0`, `hi = n - 1`.
2. While `lo <= hi`:
   - `mid = lo + (hi - lo) // 2`.
   - If `nums[mid] == target`, return `mid`.
   - **Left half sorted?** If `nums[lo] <= nums[mid]`:
     - If `nums[lo] <= target < nums[mid]`, the target is in the sorted left
       half → `hi = mid - 1`; else `lo = mid + 1`.
   - **Otherwise the right half is sorted** (`nums[mid] < nums[hi]`):
     - If `nums[mid] < target <= nums[hi]`, the target is in the sorted right
       half → `lo = mid + 1`; else `hi = mid - 1`.
3. Return -1.

```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:            # left half [lo, mid] is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                # right half [mid, hi] is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```

**Why it is correct.** The comparison `nums[lo] <= nums[mid]` cleanly separates
two cases: either the rotation pivot is to the right of `mid` (left half is a
clean ascending run) or it is within the left half (making the right half the
clean run). Within the **sorted** half, a normal ordered range check tells us
whether the target could possibly be there. If yes, we descend into it; if no,
the target — if it exists — must be in the other half. Every branch moves a
boundary past `mid`, so the range strictly shrinks and the loop terminates.

- **Time:** O(log n).
- **Space:** O(1).

## Key Insights & Edge Cases

- **One half is always sorted.** This is the invariant that makes binary search
  applicable despite the rotation.
- **Use `<=` when testing the left half** (`nums[lo] <= nums[mid]`). With a
  single-element window `lo == mid`, this correctly classifies the left side as
  "sorted" and avoids mishandling. (For distinct values `<` also works because
  equality only occurs when `lo == mid`.)
- **Boundary comparisons are inclusive on the pivot-anchored end:**
  `nums[lo] <= target` and `target <= nums[hi]` include the sorted half's
  endpoints, since `target != nums[mid]` was already handled.
- **No rotation** (`k = 0`, e.g. `[0,1,2,4,5,6,7]`): the left half is always
  sorted and the algorithm degenerates into ordinary binary search.
- **Single element** (`[1]`, target `0`): checks index 0, no match, returns -1.
- **Distinct values assumed.** Duplicates (LeetCode 81) break the
  `nums[lo] <= nums[mid]` test and require an extra `lo += 1` step to skip
  ambiguous duplicates.
