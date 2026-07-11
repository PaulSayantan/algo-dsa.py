# Solution — Sum of Absolute Differences in a Sorted Array

## Brute Force

For each `i`, loop over every `j` and add `abs(nums[i] - nums[j])`.

```python
def getSumAbsoluteDifferences(nums):
    n = len(nums)
    result = []
    for i in range(n):
        total = 0
        for j in range(n):
            total += abs(nums[i] - nums[j])
        result.append(total)
    return result
```

- **Time:** O(n^2). With `n` up to `10^5` this is far too slow.
- **Space:** O(1) extra.

## Optimal Approach (Prefix Sum + Suffix Sum)

Because `nums` is **sorted non-decreasing**, for a fixed index `i`:

- Every element to the **left** (`j < i`) satisfies `nums[j] <= nums[i]`, so
  `|nums[i] - nums[j]| = nums[i] - nums[j]`.
- Every element to the **right** (`j > i`) satisfies `nums[j] >= nums[i]`, so
  `|nums[i] - nums[j]| = nums[j] - nums[i]`.

That removes the absolute value and lets each side collapse into a closed form.
Let `leftSum` = sum of the `i` elements before `i` (a **prefix sum**) and
`rightSum` = sum of the `n - 1 - i` elements after `i` (a **suffix sum**). Then:

```
leftContribution  = i * nums[i] - leftSum          # each of i terms contributes nums[i], minus their actual values
rightContribution = rightSum - (n - 1 - i) * nums[i]
result[i]         = leftContribution + rightContribution
```

Reference implementation:

```python
def getSumAbsoluteDifferences(nums):
    n = len(nums)
    total = sum(nums)

    result = [0] * n
    left = 0            # prefix sum of nums[0..i-1]
    for i in range(n):
        right = total - left - nums[i]      # suffix sum of nums[i+1..n-1]
        left_contrib = nums[i] * i - left
        right_contrib = right - nums[i] * (n - 1 - i)
        result[i] = left_contrib + right_contrib
        left += nums[i]
    return result
```

**Why it is correct:** `left` is the prefix sum `nums[0..i-1]`, and
`total - left - nums[i]` is the suffix sum `nums[i+1..n-1]`. The left side has
`i` elements, each contributing `nums[i]` before subtracting their true values,
giving `i * nums[i] - left`. The right side has `n - 1 - i` elements, each
contributing its true value minus `nums[i]`, giving `right - (n-1-i) * nums[i]`.
Summing the two matches the definition, and the sortedness guarantees the sign of
each term so the absolute values can be dropped safely.

**Step by step** for `nums = [2, 3, 5]` (total = 10):

```
i=0: nums=2, left=0,  right=10-0-2=8
     left_contrib  = 2*0 - 0 = 0
     right_contrib = 8 - 2*2 = 4
     result[0] = 4 ;  then left = 2
i=1: nums=3, left=2,  right=10-2-3=5
     left_contrib  = 3*1 - 2 = 1
     right_contrib = 5 - 3*1 = 2
     result[1] = 3 ;  then left = 5
i=2: nums=5, left=5,  right=10-5-5=0
     left_contrib  = 5*2 - 5 = 5
     right_contrib = 0 - 5*0 = 0
     result[2] = 5 ;  then left = 10

result = [4, 3, 5]
```

- **Time:** O(n) — one pass (plus one pass for `total`).
- **Space:** O(1) extra beyond the output.

## Key Insights & Edge Cases

- **Sortedness is the enabler.** It fixes the sign of every `nums[i] - nums[j]`,
  which is what lets prefix and suffix sums replace the inner loop. On an
  unsorted array you would sort first (O(n log n)) or need a different method.
- The pattern is again "left aggregate + right aggregate", split at `i`; here the
  left side is a prefix sum and the right side is a suffix sum, each scaled by a
  count.
- **Endpoints:** at `i = 0` there is no left part (`left = 0`, count 0); at
  `i = n - 1` there is no right part (`right = 0`, count 0). The formulas produce
  `0` for the empty side with no special casing.
- **Duplicates** (equal adjacent values) are fine: an equal element contributes
  `0`, and the derivation still holds because `<=`/`>=` remain valid.
- Values stay well within 64-bit range (`n * max ~ 10^5 * 10^4 = 10^9`); Python
  integers are unbounded, so no overflow concern here.
