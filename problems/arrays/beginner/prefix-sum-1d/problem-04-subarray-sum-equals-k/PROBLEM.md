# Subarray Sum Equals K

**Difficulty:** Medium

**Source:** LeetCode 560 — Subarray Sum Equals K

## Description

Given an array of integers `nums` and an integer `k`, return the **total number
of contiguous subarrays** whose sum equals `k`.

A subarray is a contiguous, non-empty sequence of elements within the array.
Note that `nums` may contain negative numbers and zeros, so a two-pointer /
sliding-window approach does **not** work here — you cannot assume that growing
a window monotonically increases its sum.

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

## Examples

### Example 1

```
Input:  nums = [1, 1, 1], k = 2
Output: 2
Explanation: The subarrays [1, 1] (indices 0..1) and [1, 1] (indices 1..2)
             each sum to 2. That is 2 subarrays.
```

### Example 2

```
Input:  nums = [1, 2, 3], k = 3
Output: 2
Explanation: [3] (index 2) sums to 3, and [1, 2] (indices 0..1) sums to 3.
             That is 2 subarrays.
```

### Example 3

```
Input:  nums = [1, -1, 0], k = 0
Output: 3
Explanation: [1, -1] (indices 0..1), [-1, 0] (indices 1..2), and [0] (index 2)
             each sum to 0. That is 3 subarrays.
```

## Hint

Use **Prefix Sum (1D)** together with a hash map. A subarray `(i, j]` sums to
`k` exactly when `prefix[j] - prefix[i] = k`; rearrange to look up how many
earlier prefixes equal `prefix[j] - k`.
