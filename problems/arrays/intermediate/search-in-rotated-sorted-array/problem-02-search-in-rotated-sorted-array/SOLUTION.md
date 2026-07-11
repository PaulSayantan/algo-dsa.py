# Solution — Search in Rotated Sorted Array

## Brute Force

Linear scan: walk the array and return the first index whose value equals
`target`.

```python
def search(nums, target):
    for i, v in enumerate(nums):
        if v == target:
            return i
    return -1
```

- **Time:** `O(n)`.
- **Space:** `O(1)`.

Simple and correct, but ignores the sorted structure and misses the required
`O(log n)` bound.

## Optimal Approach (Search in Rotated Sorted Array)

The key observation: when you split the window at `mid`, **at least one of the
two halves is fully sorted**, because a single rotation creates at most one
"drop". Compare `nums[lo]` with `nums[mid]` to find the sorted half, then check
whether `target` falls inside that sorted half's value range.

Single-pass binary search over window `[lo, hi]`:

1. `mid = (lo + hi) // 2`. If `nums[mid] == target`, return `mid`.
2. If `nums[lo] <= nums[mid]`, the **left half `[lo..mid]` is sorted**:
   - If `nums[lo] <= target < nums[mid]`, the target is in the left half:
     `hi = mid - 1`.
   - Otherwise search the right half: `lo = mid + 1`.
3. Else the **right half `[mid..hi]` is sorted**:
   - If `nums[mid] < target <= nums[hi]`, the target is in the right half:
     `lo = mid + 1`.
   - Otherwise search the left half: `hi = mid - 1`.

Loop while `lo <= hi`; return `-1` if it exits without a hit.

```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:            # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```

**Why it is correct.** Because values are distinct, the test `nums[lo] <=
nums[mid]` cleanly identifies which side is sorted. Once you know a side is
sorted, its endpoints bound every value in it, so a simple range check decides
in `O(1)` whether `target` can be there. If it is, keep that side; if not, the
answer (if any) must be in the other side. Every branch strictly shrinks the
window, so the search terminates.

- **Time:** `O(log n)`.
- **Space:** `O(1)`.

### Step-by-step on `nums = [4,5,6,7,0,1,2]`, `target = 0`

| lo | hi | mid | nums[mid] | sorted half | reasoning | action |
|----|----|-----|-----------|-------------|-----------|--------|
| 0  | 6  | 3   | 7         | left `[4..7]` | 0 not in `[4,7)` | lo = 4 |
| 4  | 6  | 5   | 1         | left `[0..1]` (nums[4]=0<=1) | 0 in `[0,1)` | hi = 4 |
| 4  | 4  | 4   | 0         | — | `nums[mid] == target` | return 4 |

## Key Insights & Edge Cases

- **The `<=` in `nums[lo] <= nums[mid]` matters.** When `lo == mid` (window of
  size 1 or 2), this keeps the "left is sorted" branch valid instead of
  misclassifying.
- **Boundary of the range checks:** use half-open comparisons (`nums[lo] <=
  target < nums[mid]`) so the already-checked `nums[mid]` is excluded and you
  never loop forever.
- **Target absent:** the window collapses (`lo > hi`) and you return `-1`
  (Example 2).
- **Single element:** `lo == hi == 0`; either it matches or you return `-1`.
- **Not rotated at all:** the left-half-sorted branch handles a fully ascending
  array exactly like ordinary binary search.
- **Alternative two-pass method:** find the pivot (minimum) with Problem 1, then
  run a classic binary search on the correct sorted segment (or map indices with
  modular arithmetic). Same `O(log n)`, but the one-pass version above avoids the
  extra pass.
