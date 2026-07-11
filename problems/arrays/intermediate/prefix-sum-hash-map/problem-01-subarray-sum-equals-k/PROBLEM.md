# Subarray Sum Equals K

**Difficulty:** Medium

**Source:** LeetCode 560 — Subarray Sum Equals K

## Description

Given an integer array `nums` and an integer `k`, return the **total number of
contiguous (non-empty) subarrays** whose elements sum to exactly `k`.

A subarray is a contiguous, non-empty sequence of elements within the array.
The same value can appear multiple times, and subarrays that occupy different
index ranges are counted separately even if they contain identical values.

Note that `nums` may contain negative numbers and zeros, so a simple sliding
window that only grows and shrinks will not work here.

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

## Examples

### Example 1

```
Input: nums = [1, 1, 1], k = 2
Output: 2
Explanation: The subarrays nums[0..1] = [1, 1] and nums[1..2] = [1, 1]
each sum to 2. They occupy different index ranges, so both are counted.
```

### Example 2

```
Input: nums = [1, 2, 3], k = 3
Output: 2
Explanation: The subarrays [1, 2] (indices 0..1) and [3] (index 2) both
sum to 3.
```

### Example 3

```
Input: nums = [1, -1, 0], k = 0
Output: 3
Explanation: [1, -1] (indices 0..1), [-1, 0]? no that sums to -1.
The subarrays summing to 0 are [1, -1] (0..1), [1, -1, 0] (0..2),
and [0] (index 2). That is 3 subarrays.
```

## Hint

You do not need to re-sum every candidate subarray. Track a running
(**prefix**) sum as you scan, and use a **hash map** that remembers how many
times each prefix-sum value has occurred so far.
