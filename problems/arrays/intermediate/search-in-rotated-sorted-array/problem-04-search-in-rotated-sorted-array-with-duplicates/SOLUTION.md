# Solution — Search in Rotated Sorted Array II

## Brute Force

Linear scan; return `True` on the first match.

```python
def search(nums, target):
    return target in nums   # O(n) scan under the hood
```

- **Time:** `O(n)`.
- **Space:** `O(1)`.

## Optimal Approach (Search in Rotated Sorted Array + duplicate guard)

This is Problem 2 (LeetCode 33) with one wrinkle: **duplicates can make the
"which half is sorted" test ambiguous.** With distinct values, `nums[lo] <=
nums[mid]` reliably tells you the left half is sorted. But if
`nums[lo] == nums[mid]`, the left half could be all equal *or* could straddle
the pivot — you cannot tell. The specific killer case is
`nums[lo] == nums[mid] == nums[hi]`.

The fix: when `nums[lo] == nums[mid] == nums[hi]`, you cannot decide a side, so
just shrink the window from both ends (`lo += 1; hi -= 1`) and retry. Otherwise
fall back to the exact distinct-value logic.

```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return True
        if nums[lo] == nums[mid] == nums[hi]:
            lo += 1          # ambiguous: peel both ends
            hi -= 1
        elif nums[lo] <= nums[mid]:          # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return False
```

**Why it is correct.** The `elif`/`else` branches are identical to the
distinct-value solution and are only reached once we know the endpoints are not
all equal, so the sorted-half detection is valid there. The ambiguous branch
never discards a possible occurrence of `target`: it only drops `nums[lo]` and
`nums[hi]`, and it drops them only after confirming (via the earlier
`nums[mid] == target` check plus `nums[lo] == nums[mid]`) that if either equalled
`target` we would already have detected it through `mid`. Each iteration removes
at least one element, so the loop terminates.

- **Time:** `O(log n)` on average, but `O(n)` in the worst case. When almost all
  elements are equal (e.g. `[1,1,1,...,1,0,1,...,1]`), the ambiguous branch fires
  repeatedly and peels one or two elements at a time.
- **Space:** `O(1)`.

### Step-by-step on `nums = [1,0,1,1,1]`, `target = 0`

| lo | hi | mid | nums[lo] | nums[mid] | nums[hi] | branch | action |
|----|----|-----|----------|-----------|----------|--------|--------|
| 0  | 4  | 2   | 1        | 1         | 1        | all equal | lo=1, hi=3 |
| 1  | 3  | 2   | 0        | 1         | 1        | left sorted? `nums[1]=0<=nums[2]=1` yes; is `0<=0<1`? yes | hi=1 |
| 1  | 1  | 1   | 0        | 0         | 0        | `nums[mid]==target` | return True |

## Key Insights & Edge Cases

- **The ambiguous branch is the whole point.** Removing it makes the algorithm
  wrong on inputs like `[1,0,1,1,1]` (and `[1,1,1,0,1]`), where the endpoint
  equality hides the sorted side.
- **Worst-case `O(n)`** is unavoidable: adversarial all-equal-but-one inputs
  force linear work. Interviewers expect you to state this trade-off explicitly.
- **Return type is boolean** — LeetCode 81 asks *whether* the target exists, not
  its index (an index is unstable anyway with duplicates).
- **Target absent** (Example 2): the window collapses to empty and you return
  `False`.
- **Peel exactly the endpoints, not `mid`.** Only `nums[lo]` and `nums[hi]` are
  provably redundant when all three are equal; shrinking around `mid` instead
  could skip the answer.
