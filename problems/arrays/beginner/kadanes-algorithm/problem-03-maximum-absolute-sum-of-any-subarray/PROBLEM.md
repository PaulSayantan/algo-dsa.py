# Maximum Absolute Sum of Any Subarray

**Difficulty:** Medium

**Source:** LeetCode 1749 — Maximum Absolute Sum of Any Subarray

## Description

You are given an integer array `nums`. The *absolute sum* of a subarray
`[nums[l], nums[l+1], ..., nums[r]]` is `abs(nums[l] + nums[l+1] + ... +
nums[r])`.

Return the **maximum absolute sum** of any (possibly empty) subarray of `nums`.

Note that `abs(x)` is the absolute value of `x`: `abs(-5) = 5` and `abs(5) = 5`.
Since the empty subarray (sum `0`) is allowed, the answer is always at least `0`.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [1, -3, 2, 3, -4]
Output: 5
Explanation: The subarray [2, 3] has absolute sum abs(2 + 3) = 5, which is the
             maximum. (The most-negative subarray [-4] gives abs = 4, and [-3]
             gives 3, so the positive side wins here.)
```

### Example 2

```
Input:  nums = [2, -5, 1, -4, 3, -2]
Output: 8
Explanation: The subarray [-5, 1, -4] has sum -8, and abs(-8) = 8, the maximum.
             The best positive subarray only reaches 3, so the negative side wins.
```

## Constraints on the answer

- The maximum absolute sum equals `max(maxSubarraySum, -minSubarraySum)`.
- Because the empty subarray is allowed, the result is never negative.

## Hint

The largest absolute sum comes from either the maximum-sum subarray or the
minimum-sum subarray. Run **Kadane's Algorithm** twice — once for the maximum
and once for the minimum — and take the larger magnitude.
