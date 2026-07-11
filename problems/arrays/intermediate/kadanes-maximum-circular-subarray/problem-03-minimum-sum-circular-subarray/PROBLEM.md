# Minimum Sum Circular Subarray

**Difficulty:** Medium

**Source:** Classic variant of LeetCode 918 (mirror of Maximum Sum Circular
Subarray); appears widely in competitive programming.

## Description

Given a **circular** integer array `nums` of length `n`, return the **minimum**
possible sum of a **non-empty** subarray of `nums`.

As in the maximum variant, the array is circular: the element after `nums[i]`
is `nums[(i + 1) % n]`, so a subarray may wrap around from the end back to the
beginning. The subarray must be non-empty and may use each element at most
once.

This is the exact mirror image of "Maximum Sum Circular Subarray." Everything
flips: you run a minimizing Kadane for the non-wrapping case, and for the
wrapping case you subtract the **maximum-sum** subarray from the total.

## Constraints

- `n == nums.length`
- `1 <= n <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`

## Examples

### Example 1

```
Input: nums = [-5, 3, 4, -2]
Output: -7
Explanation: The best (minimum) subarray wraps around: [-2, -5] using index 3
then index 0, sum = -7. Total = 0, maximum middle subarray = [3, 4] = 7,
so total - max = 0 - 7 = -7.
```

### Example 2

```
Input: nums = [1, 2, 3]
Output: 1
Explanation: All elements are positive, so no wrap helps. The minimum non-empty
subarray is the single element [1], sum = 1.
```

### Example 3

```
Input: nums = [5, -3, 5]
Output: -3
Explanation: The minimum subarray is the single element [-3] (index 1). A wrap
[5, 5] would give total - maxK = 7 - 7 = 0, which is larger, so it does not win.
```

## Hint

Mirror the maximum-circular idea: the answer is either a non-wrapping minimum
(minimizing Kadane) or `total − maxKadane` for the wrapping case. Guard the
all-positive array. This applies Kadane's — Maximum Circular Subarray in
reverse.
