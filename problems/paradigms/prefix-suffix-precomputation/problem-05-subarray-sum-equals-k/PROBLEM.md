# Subarray Sum Equals K

**Difficulty:** Medium

**Source:** LeetCode 560 — Subarray Sum Equals K

## Description

Given an array of integers `nums` and an integer `k`, return the **total number of
subarrays** whose sum equals `k`.

A subarray is a contiguous **non-empty** sequence of elements within the array.

Note that `nums` may contain negative numbers and zeros, so a sliding window does
**not** work here — you cannot assume that extending a window only increases the sum.

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

## Examples

### Example 1

```
Input:  nums = [1, 1, 1], k = 2
Output: 2
Explanation: The subarrays summing to 2 are nums[0..1] = [1,1] and
             nums[1..2] = [1,1]. That is 2 subarrays.
```

### Example 2

```
Input:  nums = [1, 2, 3], k = 3
Output: 2
Explanation: The subarrays summing to 3 are [1,2] (indices 0..1) and
             [3] (index 2). That is 2 subarrays.
```

### Example 3

```
Input:  nums = [1, -1, 0], k = 0
Output: 3
Explanation: The subarrays summing to 0 are [1,-1] (indices 0..1),
             [1,-1,0] (indices 0..2), and [0] (index 2). That is 3 subarrays.
```

## Hint

Use **Prefix / Suffix Precomputation**: a subarray `nums[i..j]` sums to `k` exactly
when `prefix[j+1] - prefix[i] == k`. Sweep left to right and use a hash map of how
many times each prefix-sum value has appeared so far to count matches in O(n).
