# Maximum Absolute Sum of Any Subarray

**Difficulty:** Medium

**Source:** LeetCode 1749 — Maximum Absolute Sum of Any Subarray

## Description

You are given an integer array `nums`. The **absolute sum** of a subarray
`nums[l..r]` is `abs(nums[l] + nums[l+1] + ... + nums[r])`.

Return the **maximum absolute sum** over all (possibly empty) subarrays of
`nums`. The empty subarray has sum `0`, so the answer is always at least `0`.

This is a linear (non-circular) problem, but it drills the exact core skill of
the circular technique: running a **maximizing** Kadane and a **minimizing**
Kadane over the same array at the same time. The most positive subarray sum and
the most negative subarray sum are the only two candidates for the largest
absolute value.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input: nums = [1, -3, 2, 3, -4]
Output: 5
Explanation: The subarray [2, 3] has sum 5, giving absolute sum abs(5) = 5,
the largest possible.
```

### Example 2

```
Input: nums = [2, -5, 1, -4, 3, -2]
Output: 8
Explanation: The subarray [-5, 1, -4] has sum -8, giving absolute sum
abs(-8) = 8, the largest possible.
```

### Example 3

```
Input: nums = [-1, -2, -3]
Output: 6
Explanation: The whole array sums to -6; abs(-6) = 6. The most negative
subarray sum drives the answer here.
```

## Hint

`abs(sum)` is large when the sum is either very positive or very negative. Track
the maximum-sum subarray and the minimum-sum subarray simultaneously — the pair
of running Kadanes at the heart of Kadane's — Maximum Circular Subarray.
