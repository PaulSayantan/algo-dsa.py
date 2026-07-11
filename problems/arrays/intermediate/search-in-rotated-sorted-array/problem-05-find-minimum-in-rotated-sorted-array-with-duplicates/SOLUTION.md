# Solution — Find Minimum in Rotated Sorted Array II

## Brute Force

Return the smallest element with a single scan.

```python
def findMin(nums):
    return min(nums)
```

- **Time:** `O(n)`.
- **Space:** `O(1)`.

Interestingly, the optimal approach also degrades to `O(n)` in the worst case,
but on typical inputs it is much faster.

## Optimal Approach (Search in Rotated Sorted Array + tie handling)

This extends Problem 1 (LeetCode 153) to allow duplicates. We still binary
search comparing `nums[mid]` with `nums[hi]`, but now there are **three** cases
instead of two:

- `nums[mid] > nums[hi]`: the minimum is strictly to the right -> `lo = mid + 1`.
- `nums[mid] < nums[hi]`: the right side is sorted; the minimum is at `mid` or to
  its left -> `hi = mid`.
- `nums[mid] == nums[hi]`: **ambiguous.** `nums[hi]` is a duplicate of
  `nums[mid]`, so it cannot be a *unique* minimum that `mid` doesn't already
  represent. Safely discard it -> `hi -= 1`.

```python
def findMin(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1        # min strictly right of mid
        elif nums[mid] < nums[hi]:
            hi = mid            # min at mid or left of it
        else:                   # nums[mid] == nums[hi]
            hi -= 1             # duplicate: drop hi, keep mid's value in play
    return nums[lo]
```

**Why `hi -= 1` is safe.** When `nums[mid] == nums[hi]`, the element at `hi` has
a twin at `mid` inside the window `[lo, hi)`. Removing index `hi` therefore
cannot remove the *only* copy of the minimum — whatever value `nums[hi]` held is
still represented at `mid` (which stays in the window). We lose the ability to
halve the search here, so we shed one element instead, guaranteeing progress
without ever discarding the true minimum.

- **Time:** `O(log n)` average, `O(n)` worst case. The pathological input is
  something like `[1,1,1,...,1,0,1,...,1]` (or all-equal), where the equality
  branch fires repeatedly and peels one element per step.
- **Space:** `O(1)`.

### Step-by-step on `nums = [3,3,1,3]`

| lo | hi | mid | nums[mid] | nums[hi] | case | action |
|----|----|-----|-----------|----------|------|--------|
| 0  | 3  | 1   | 3         | 3        | equal | hi = 2 |
| 0  | 2  | 1   | 3         | 1        | `>`   | lo = 2 |

Now `lo == hi == 2`, and `nums[2] = 1` is the minimum.

### Step-by-step on `nums = [2,2,2,0,1]`

| lo | hi | mid | nums[mid] | nums[hi] | case | action |
|----|----|-----|-----------|----------|------|--------|
| 0  | 4  | 2   | 2         | 1        | `>`  | lo = 3 |
| 3  | 4  | 3   | 0         | 1        | `<`  | hi = 3 |

`lo == hi == 3`, `nums[3] = 0` is the minimum.

## Key Insights & Edge Cases

- **Compare with `nums[hi]`, not `nums[lo]`.** Against the right endpoint the
  equality case has a clean, safe resolution (`hi -= 1`). Comparing with
  `nums[lo]` makes the duplicate case much harder to reason about.
- **Only decrement `hi` on a tie — never `lo += 1` here.** With the `nums[mid]`
  vs `nums[hi]` framing, `hi` is the endpoint proven redundant; touching `lo`
  could step over the pivot.
- **Worst case really is `O(n)`.** State this explicitly: duplicates destroy the
  guaranteed halving. `[2,2,2,2,2]` or `[1,1,1,1,0,1]` are the classic examples.
- **Fully sorted / single element:** `nums[mid] < nums[hi]` drives `hi` down to
  0, or the loop never runs — either way `nums[0]` is returned correctly.
- **Contrast with the distinct version (Problem 1):** that one has just two
  branches and is always `O(log n)`. The extra equality branch is the entire
  difference and the reason this problem is rated Hard.
