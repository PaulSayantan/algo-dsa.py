# Subarray Sums Divisible by K

**Difficulty:** Medium

**Source:** LeetCode 974 — Subarray Sums Divisible by K

## Description

Given an integer array `nums` and an integer `k`, return the number of
**non-empty contiguous subarrays** whose sum is divisible by `k`.

A subarray is a contiguous part of the array. A sum `s` is divisible by `k` when
`s % k == 0` (this includes a sum of `0`).

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `2 <= k <= 10^4`

## Examples

### Example 1

```
Input:  nums = [4, 5, 0, -2, -3, 1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by 5:
             [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3], [4, 5, 0, -2, -3, 1]
```

### Example 2

```
Input:  nums = [5], k = 9
Output: 0
Explanation: 5 is not divisible by 9, and it is the only subarray, so the count is 0.
```

### Example 3

```
Input:  nums = [1, 2, 3], k = 3
Output: 3
Explanation: [1, 2] sums to 3, [3] sums to 3, and [1, 2, 3] sums to 6.
             All three are divisible by 3.
```

## Hint

Use **Prefix Sum (1D)** on the running sum **modulo k**. Two prefixes with the
same remainder bound a subarray whose sum is divisible by `k`; count pairs of
equal remainders (and normalize negative remainders to `[0, k)`).
