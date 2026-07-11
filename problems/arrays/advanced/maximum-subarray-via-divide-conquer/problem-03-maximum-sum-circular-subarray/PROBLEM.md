# Maximum Sum Circular Subarray

**Difficulty:** Medium

**Source:** LeetCode 918 — Maximum Sum Circular Subarray

## Description

Given a **circular** integer array `nums` of length `n`, return the maximum
possible sum of a non-empty subarray.

A circular array means the end wraps around to the beginning: the element after
`nums[n-1]` is `nums[0]`. Formally, a subarray may be `nums[i], nums[i+1], ...,
nums[j]` where indices are taken modulo `n`, but each element may be included **at
most once** (the subarray length is at most `n`).

There are two shapes of answer:

1. A **non-wrapping** subarray — an ordinary contiguous slice. This is exactly the
   maximum-subarray problem you already know how to solve by divide & conquer.
2. A **wrapping** subarray — it uses a suffix and a prefix of the array. Its sum
   equals `total(nums) - (some interior subarray)`; it is maximized by removing
   the *minimum* interior subarray. The minimum subarray is found with the same
   divide & conquer merge, flipped to track minima.

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- The subarray must be non-empty.

## Examples

### Example 1

```
Input:  nums = [1, -2, 3, -2]
Output: 3
Explanation: The best subarray is [3] with sum 3 (non-wrapping).
```

### Example 2

```
Input:  nums = [5, -3, 5]
Output: 10
Explanation: The wrapping subarray [5, 5] (last element + first element) sums to 10.
             Equivalently, total 7 minus the minimum interior subarray [-3] = -3.
```

### Example 3

```
Input:  nums = [-3, -2, -3]
Output: -2
Explanation: Every element is negative. The wrapping formula would suggest an
             empty removal, which is not allowed, so the answer is the plain
             maximum subarray [-2] = -2.
```

## Hint

Use **Maximum Subarray via Divide & Conquer** twice. First find the ordinary
maximum subarray (the non-wrapping answer). Then find the minimum subarray with
the mirror-image merge; the best wrapping answer is `total - min_subarray`. Return
the larger of the two — but guard the all-negative case where every element would
be removed.
