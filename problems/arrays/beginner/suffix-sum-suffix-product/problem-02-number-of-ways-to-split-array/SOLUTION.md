# Solution — Number of Ways to Split Array

## Brute Force

For each candidate split index `i` from `0` to `n - 2`, recompute the left sum
`sum(nums[:i+1])` and the right sum `sum(nums[i+1:])` from scratch and compare.

```python
def waysToSplitArray(nums):
    n = len(nums)
    count = 0
    for i in range(n - 1):
        left = sum(nums[:i + 1])
        right = sum(nums[i + 1:])
        if left >= right:
            count += 1
    return count
```

- **Time:** O(n^2) — each split re-sums the array. With `n` up to `10^5` this is
  ~10^10 operations and will time out.
- **Space:** O(1) extra.

## Optimal Approach (Suffix Sum via total minus prefix)

The right part of a split at index `i` is exactly the **suffix sum** starting at
`i + 1`. Instead of a full suffix array, use the identity

```
rightSum(i) = total - leftSum(i)
```

where `total = sum(nums)` and `leftSum(i)` is the running prefix sum through
index `i`. Sweep once, maintaining `left`; at each valid position compare
`left` against `total - left`.

Reference implementation:

```python
def waysToSplitArray(nums):
    total = sum(nums)
    left = 0
    count = 0
    for i in range(len(nums) - 1):   # stop at n-2: right part must be non-empty
        left += nums[i]
        right = total - left
        if left >= right:
            count += 1
    return count
```

**Why it is correct:** After adding `nums[i]`, `left` equals `sum(nums[0..i])`,
the sum of the first `i + 1` elements. Since `total` is the sum of the entire
array, `total - left` is precisely the sum of the remaining elements
`nums[i+1..n-1]` — the suffix. The loop stops at `i = n - 2` so the right part is
never empty, satisfying the "at least one element to the right" rule.

**Step by step** for `nums = [10, 4, -8, 7]` (total = 13):

```
i=0: left=10,  right=13-10=3   -> 10 >= 3   valid   (count=1)
i=1: left=14,  right=13-14=-1  -> 14 >= -1  valid   (count=2)
i=2: left=6,   right=13-6=7    -> 6  >= 7   invalid (count=2)
(i=3 is skipped: it would leave an empty right part)

answer = 2
```

- **Time:** O(n) — one pass for `total`, one pass for the sweep.
- **Space:** O(1) extra.

## Key Insights & Edge Cases

- "Right side of a split point" is a suffix sum. Recognizing that lets you
  replace the inner loop with a single subtraction from a precomputed total.
- **Negatives matter:** because values can be negative, the right sum can be
  negative, so you cannot assume left sums grow monotonically or prune early —
  you must check every split index.
- **Boundary:** the loop must exclude `i = n - 1`; splitting there leaves an empty
  right part, which is not a valid split. With `n >= 2` there is always at least
  one candidate index.
- Use exact integer arithmetic (Python integers are unbounded); in fixed-width
  languages the running sum can exceed 32 bits (`10^5 * 10^5 = 10^{10}`), so use
  64-bit integers.
