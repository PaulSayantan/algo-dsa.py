# Continuous Subarray Sum

**Difficulty:** Medium

**Source:** LeetCode 523 — Continuous Subarray Sum

## Description

Given an integer array `nums` and an integer `k`, return `true` if `nums` has a
**good subarray**, otherwise return `false`.

A **good subarray** is a contiguous subarray that:

1. has length **at least 2**, and
2. has a sum that is a **multiple of `k`** (i.e. the sum equals `n * k` for some
   integer `n`, including `0`).

Note that a subarray whose sum is `0` counts as a multiple of `k` (with
`n = 0`), as long as its length is at least 2.

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= sum(nums[i]) <= 2^31 - 1`
- `1 <= k <= 2^31 - 1`

## Examples

### Example 1

```
Input: nums = [23, 2, 4, 6, 7], k = 6
Output: true
Explanation: The subarray [2, 4] (indices 1..2) has length 2 and sums to 6,
which is 1 * 6, a multiple of 6.
```

### Example 2

```
Input: nums = [23, 2, 6, 4, 7], k = 6
Output: true
Explanation: The subarray [23, 2, 6, 4, 7] has length 5 and sums to 42 = 7 * 6,
a multiple of 6. (Several shorter good subarrays also exist.)
```

### Example 3

```
Input: nums = [23, 2, 6, 4, 7], k = 13
Output: false
Explanation: No contiguous subarray of length >= 2 has a sum that is a multiple
of 13.
```

## Hint

Two prefix sums that leave the **same remainder mod `k`** bracket a subarray
whose sum is a multiple of `k`. Store the *earliest index* of each remainder in
a **hash map**, and require the index gap to be at least 2.
