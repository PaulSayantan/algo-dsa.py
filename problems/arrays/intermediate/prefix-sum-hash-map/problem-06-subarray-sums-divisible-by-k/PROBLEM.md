# Subarray Sums Divisible by K

**Difficulty:** Medium

**Source:** LeetCode 974 — Subarray Sums Divisible by K

## Description

Given an integer array `nums` and an integer `k`, return the **number of
non-empty contiguous subarrays** whose sum is **divisible by `k`**.

The array can contain negative numbers, so you must normalize remainders into
the range `0 .. k-1` (in Python, `x % k` already does this for positive `k`).
This is the *counting* companion to LeetCode 523.

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `2 <= k <= 10^4`

## Examples

### Example 1

```
Input: nums = [4, 5, 0, -2, -3, 1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3].
```

### Example 2

```
Input: nums = [5], k = 9
Output: 0
Explanation: The only subarray is [5], whose sum 5 is not divisible by 9.
```

### Example 3

```
Input: nums = [-1, 2, 9], k = 2
Output: 2
Explanation: The subarrays with sum divisible by 2 are [-1, 2, 9] (sum 10)
and [2] (sum 2). No other subarray qualifies.
```

## Hint

Two prefix sums with the **same remainder mod `k`** bound a subarray whose sum
is divisible by `k`. Count, for each remainder, how many prefix sums produced
it using a **hash map**, and add `C(count, 2)` pairs. Watch out for negative
remainders.
