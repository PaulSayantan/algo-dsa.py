# Solution — Find Pivot Index

## Brute Force

For each candidate index `i`, sum everything to its left and everything to its
right, then compare.

```python
def pivotIndex(nums):
    n = len(nums)
    for i in range(n):
        left = sum(nums[:i])
        right = sum(nums[i + 1:])
        if left == right:
            return i
    return -1
```

- **Time:** O(n^2) — each index re-sums up to `n` elements.
- **Space:** O(1) (ignoring the slices, O(n) if you count them).

## Optimal Approach (Prefix Sum, 1D)

Compute the **total** sum once. As you scan left to right, maintain `leftSum`,
the sum of elements strictly before the current index. For index `i`, the right
sum is whatever remains after removing the left part and the current element:

```
rightSum = total - leftSum - nums[i]
```

Index `i` is a pivot exactly when `leftSum == rightSum`, i.e.
`leftSum == total - leftSum - nums[i]`.

Reference implementation:

```python
def pivotIndex(nums):
    total = sum(nums)
    left_sum = 0
    for i, x in enumerate(nums):
        if left_sum == total - left_sum - x:
            return i
        left_sum += x
    return -1
```

**Why it is correct:** `leftSum` is a running prefix sum of the elements before
`i`. `total - leftSum - nums[i]` is precisely the sum of the elements after `i`,
because the whole array splits into (left part) + (nums[i]) + (right part).
Checking `leftSum` *before* adding `nums[i]` ensures the current element is
excluded from the left side. We scan increasing `i`, so the first match is the
leftmost pivot.

**Step by step** on `[1, 7, 3, 6, 5, 6]` (total = 28):

| i | nums[i] | left_sum (before) | right = 28 - left - nums[i] | pivot? |
|---|---------|-------------------|-----------------------------|--------|
| 0 | 1       | 0                 | 27                          | no     |
| 1 | 7       | 1                 | 20                          | no     |
| 2 | 3       | 8                 | 17                          | no     |
| 3 | 6       | 11                | 11                          | **yes -> return 3** |

- **Time:** O(n) — one pass to total, one pass to scan (or a single pass if you
  compute the total first).
- **Space:** O(1).

## Key Insights & Edge Cases

- The classic prefix-sum trick here is realizing you never need an explicit right
  array: `right = total - left - current` derives it in O(1).
- **Left edge:** at `i = 0`, `left_sum` is `0`, correctly modeling "no elements
  to the left." Example 3 returns index 0 for this reason.
- **Right edge:** at the last index, `right` evaluates to `0`, again correct.
- **Negative numbers** are fine — the identity `total = left + current + right`
  holds regardless of sign, which is why Example 3 (`[2, 1, -1]`) works.
- Return the **leftmost** pivot: because we scan in increasing order and return
  immediately, the first hit is automatically the leftmost.
